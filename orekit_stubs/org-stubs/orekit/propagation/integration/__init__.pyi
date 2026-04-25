
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.ode
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AbstractGradientConverter:
    """
    Converter for states and parameters arrays.
    
    Since:
        10.2
    """
    def getFreeStateParameters(self) -> int:
        """
        Get the number of free state parameters.
        
        Returns:
            number of free state parameters
        
        
        """
        ...
    def getParameters(self, state: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], parametricModel: typing.Union[org.orekit.utils.ParameterDriversProvider, typing.Callable]) -> typing.MutableSequence[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get the parametric model parameters, return gradient values for each span of each driver (several gradient values for each parameter). Different from getParametersAtStateDate which return a Gradient list containing for each driver the gradient value at state date (only 1 gradient value for each parameter).
        
        Parameters:
            state (FieldSpacecraftState<Gradient> state): state as returned by getState
            parametricModel (ParameterDriversProvider): parametric model associated with the parameters
        
        Returns:
            parametric model parameters (for all span of each driver)
        
        
        """
        ...
    def getParametersAtStateDate(self, state: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], parametricModel: typing.Union[org.orekit.utils.ParameterDriversProvider, typing.Callable]) -> typing.MutableSequence[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get the parametric model parameters, return gradient values at state date for each driver (only 1 gradient value for each parameter). Different from getParameters which return a Gradient list containing for each driver the gradient values for each span value (several gradient values for each parameter).
        
        Parameters:
            state (FieldSpacecraftState<Gradient> state): state as returned by getState
            parametricModel (ParameterDriversProvider): parametric model associated with the parameters
        
        Returns:
            parametric model parameters (for all span of each driver)
        
        
        """
        ...
    def getState(self, parametricModel: typing.Union[org.orekit.utils.ParameterDriversProvider, typing.Callable]) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get the state with the number of parameters consistent with parametric model.
        
        Parameters:
            parametricModel (ParameterDriversProvider): parametric model
        
        Returns:
            state with the number of parameters consistent with parametric model
        
        
        """
        ...

class AbstractIntegratedPropagator(org.orekit.propagation.AbstractPropagator):
    """
    Common handling of Propagator methods for both numerical and semi-analytical propagators.
    """
    def addAdditionalDerivativesProvider(self, provider: 'AdditionalDerivativesProvider') -> None:
        """
        Add a provider for user-specified state derivatives to be integrated along with the orbit propagation.
        
        Parameters:
            provider (AdditionalDerivativesProvider): provider for additional derivatives
        
        Since:
            11.1
        
        Also see:
            addAdditionalDataProvider
        
        
        """
        ...
    def addEventDetector(self, detector: org.orekit.propagation.events.EventDetector) -> None:
        """
        Add an event detector.
        
        Parameters:
            detector (EventDetector): event detector to add
        
        Also see:
            clearEventsDetectors,
            getEventDetectors
        
        
        """
        ...
    def clearEphemerisGenerators(self) -> None:
        """
        Clear the ephemeris generators.
        
        Since:
            13.0
        
        
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
    def clearMatricesComputation(self) -> None: ...
    def getAdditionalDerivativesProviders(self) -> java.util.List['AdditionalDerivativesProvider']:
        """
        Get an unmodifiable list of providers for additional derivatives.
        
        Returns:
            providers for the additional derivatives
        
        Since:
            11.1
        
        
        """
        ...
    def getBasicDimension(self) -> int:
        """
        Get state vector dimension without additional parameters.
        
        Returns:
            state vector dimension without additional parameters.
        
        
        """
        ...
    def getCalls(self) -> int:
        """
        Get the number of calls to the differential equations computation method.
        
        The number of calls is reset each time the propagate method is called.
        
        Returns:
            number of calls to the differential equations computation method
        
        
        """
        ...
    def getEphemerisGenerator(self) -> org.orekit.propagation.EphemerisGenerator:
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
    def getIntegratorName(self) -> str:
        """
        Get the integrator's name.
        
        Returns:
            name of underlying integrator
        
        Since:
            12.0
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed additional data.
        
        Specified by: getManagedAdditionalData in interface Propagator
        
        Overrides: getManagedAdditionalData in class AbstractPropagator
        
        Returns:
            names of all managed additional data
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central attraction coefficient μ.
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        Also see:
            setMu
        
        
        """
        ...
    def getPropagationType(self) -> org.orekit.propagation.PropagationType:
        """
        Get the propagation type.
        
        Returns:
            propagation type.
        
        Since:
            11.1
        
        
        """
        ...
    def getResetAtEnd(self) -> bool:
        """
        Getter for the resetting flag regarding initial state.
        
        Returns:
            resetting flag
        
        Since:
            12.0
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which a AdditionalDataProvider has been registered by calling the addAdditionalDataProvider method.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface Propagator
        
        Overrides: isAdditionalDataManaged in class AbstractPropagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Propagate towards a target date.
        
        Simple propagators use only the target date as the specification for computing the propagated state. More feature rich propagators can consider other information and provide different operating modes or G-stop facilities to stop at pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
        Specified by: propagate in interface Propagator
        
        Overrides: propagate in class AbstractPropagator
        
        Parameters:
            target (AbsoluteDate): target date towards which orbit state should be propagated
        
        Returns:
            propagated state
        
        Propagate from a start date towards a target date.
        
        Those propagators use a start date and a target date to compute the propagated state. For propagators using event detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is performed, without processing any event computation. Then complete propagation is performed from start date to target date.
        
        Parameters:
            tStart (AbsoluteDate): start date from which orbit state should be propagated
            tEnd (AbsoluteDate): target date to which orbit state should be propagated
        
        Returns:
            propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState: ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset initial state with a given propagation type.
        
        By default this method returns the same as resetInitialState
        
        Its purpose is mostly to be derived in DSSTPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): type of the new state (mean or osculating)
        
        Since:
            12.1.3
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface Propagator
        
        Overrides: setAttitudeProvider in class AbstractPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    def setMu(self, mu: float) -> None:
        """
        Set the central attraction coefficient μ.
        
        Parameters:
            mu (double): central attraction coefficient (m³/s²)
        
        
        """
        ...
    def setResetAtEnd(self, resetAtEnd: bool) -> None:
        """
        Allow/disallow resetting the initial state at end of propagation.
        
        By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a new propagation to be started from there without recomputing the part already performed. Calling this method with resetAtEnd set to false changes prevents such reset.
        
        Parameters:
            resetAtEnd (boolean): if true, at end of each propagation, the getInitialState will be
                reset to the final state of the propagation, otherwise the initial state will be preserved
        
        Since:
            9.0
        
        
        """
        ...
    class MainStateEquations:
        def computeDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]: ...
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class AdditionalDerivativesProvider:
    """
    Provider for additional derivatives.
    
    In some cases users may need to integrate some problem-specific equations along with classical spacecraft equations of motions. One example is optimal control in low thrust where adjoint parameters linked to the minimized Hamiltonian must be integrated. Another example is formation flying or rendez-vous which use the Clohessy-Whiltshire equations for the relative motion.
    
    This interface allows users to add such equations to a NumericalPropagator or a DSSTPropagator. Users provide the equations as an implementation of this interface and register it to the propagator thanks to its addAdditionalDerivativesProvider method. Several such objects can be registered with each numerical propagator, but it is recommended to gather in the same object the sets of parameters which equations can interact on each others states.
    
    This interface is the numerical (read not already integrated) counterpart of the AdditionalDataProvider interface. It allows to append various additional state parameters to any NumericalPropagator or DSSTPropagator.
    
    Since:
        11.1
    
    Also see:
        AbstractIntegratedPropagator
    """
    def combinedDerivatives(self, s: org.orekit.propagation.SpacecraftState) -> 'CombinedDerivatives':
        """
        Compute the derivatives related to the additional state (and optionally main state increments).
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        Since:
            11.2
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the generated derivative.
        
        Returns:
            dimension of the generated
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional derivatives (which will become state once integrated).
        
        Returns:
            name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the generator at the start of propagation.
        
        Parameters:
            initialState (SpacecraftState): initial state information at the start of propagation
            target (AbsoluteDate): date of propagation
        
        
        """
        ...
    def yields(self, state: org.orekit.propagation.SpacecraftState) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional state being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.getAdditionalStates().containsKey("STM");
         }
         
        
        The default implementation returns false, meaning that derivative data can be combinedDerivatives immediately.
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

class CombinedDerivatives:
    """
    Container for additional derivatives.
    
    Since:
        11.2
    
    Also see:
        AdditionalDerivativesProvider
    """
    def __init__(self, additionalDerivatives: typing.Union[typing.List[float], jpype.JArray], mainStateDerivativesIncrements: typing.Union[typing.List[float], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            additionalDerivatives (double[]): additional state derivatives
            mainStateDerivativesIncrements (double[]): increments related to the main state parameters (may be null if main state should not be incremented)
        
        
        """
        ...
    def getAdditionalDerivatives(self) -> typing.MutableSequence[float]:
        """
        Get the derivatives related to the additional state.
        
        Returns:
            additional state derivatives
        
        
        """
        ...
    def getMainStateDerivativesIncrements(self) -> typing.MutableSequence[float]:
        """
        Get the derivatives increments related to the main state.
        
        Returns:
            primary state derivatives increments, or null if main state should not be incremented
        
        
        """
        ...

_FieldAbstractIntegratedPropagator__MainStateEquations__T = typing.TypeVar('_FieldAbstractIntegratedPropagator__MainStateEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldAbstractIntegratedPropagator__T = typing.TypeVar('_FieldAbstractIntegratedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractIntegratedPropagator(org.orekit.propagation.FieldAbstractPropagator[_FieldAbstractIntegratedPropagator__T], typing.Generic[_FieldAbstractIntegratedPropagator__T]):
    """
    Common handling of FieldPropagator methods for both numerical and semi-analytical propagators.
    """
    def addAdditionalDerivativesProvider(self, provider: 'FieldAdditionalDerivativesProvider'[_FieldAbstractIntegratedPropagator__T]) -> None:
        """
        Add a provider for user-specified state derivatives to be integrated along with the orbit propagation.
        
        Parameters:
            provider (FieldAdditionalDerivativesProvider<FieldAbstractIntegratedPropagator> provider): provider for additional derivatives
        
        Since:
            11.1
        
        Also see:
            addAdditionalDataProvider
        
        
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
    def clearEphemerisGenerators(self) -> None:
        """
        Clear the ephemeris generators.
        
        Since:
            13.0
        
        
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
    def getAdditionalDerivativesProviders(self) -> java.util.List['FieldAdditionalDerivativesProvider'[_FieldAbstractIntegratedPropagator__T]]:
        """
        Get an unmodifiable list of providers for additional derivatives.
        
        Returns:
            providers for additional derivatives
        
        Since:
            11.1
        
        
        """
        ...
    def getBasicDimension(self) -> int:
        """
        Get state vector dimension without additional parameters.
        
        Returns:
            state vector dimension without additional parameters.
        
        
        """
        ...
    def getCalls(self) -> int:
        """
        Get the number of calls to the differential equations computation method.
        
        The number of calls is reset each time the propagate method is called.
        
        Returns:
            number of calls to the differential equations computation method
        
        
        """
        ...
    def getEphemerisGenerator(self) -> org.orekit.propagation.FieldEphemerisGenerator[_FieldAbstractIntegratedPropagator__T]:
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
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_FieldAbstractIntegratedPropagator__T]]:
        """
        Get all the events detectors that have been added.
        
        Returns:
            an unmodifiable collection of the added detectors
        
        Also see:
            addEventDetector,
            clearEventsDetectors
        
        
        """
        ...
    def getIntegratorName(self) -> str:
        """
        Get the integrator's name.
        
        Returns:
            name of underlying integrator
        
        Since:
            12.0
        
        
        """
        ...
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed data.
        
        Specified by: getManagedAdditionalData in interface FieldPropagator
        
        Overrides: getManagedAdditionalData in class FieldAbstractPropagator
        
        Returns:
            names of all managed data
        
        
        """
        ...
    def getMu(self) -> _FieldAbstractIntegratedPropagator__T:
        """
        Get the central attraction coefficient μ.
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        Also see:
            setMu
        
        
        """
        ...
    def getPropagationType(self) -> org.orekit.propagation.PropagationType:
        """
        Get the propagation type.
        
        Returns:
            propagation type.
        
        Since:
            11.3.2
        
        
        """
        ...
    def getResetAtEnd(self) -> bool:
        """
        Getter for the resetting flag regarding initial state.
        
        Returns:
            resetting flag
        
        Since:
            12.0
        
        
        """
        ...
    def isAdditionalDataManaged(self, name: str) -> bool:
        """
        Check if an additional data is managed.
        
        Managed data are the ones for which the propagators know how to compute its evolution. They correspond to additional data for which an FieldAdditionalDataProvider has been registered by calling the addAdditionalDataProvider method. If the propagator is an FieldAbstractIntegratedPropagator, the states for which a set of FieldAdditionalDerivativesProvider has been registered by calling the addAdditionalDerivativesProvider method are also counted as managed additional states.
        
        Additional data that are present in the getInitialState but have no evolution method registered are not considered as managed data. These unmanaged additional data are not lost during propagation, though. Their value are piecewise constant between state resets that may change them if some event handler resetState method is called at an event occurrence and happens to change the unmanaged additional data.
        
        Specified by: isAdditionalDataManaged in interface FieldPropagator
        
        Overrides: isAdditionalDataManaged in class FieldAbstractPropagator
        
        Parameters:
            name (String): name of the additional data
        
        Returns:
            true if the additional data is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__T]: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__T], propagationType: org.orekit.propagation.PropagationType) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface FieldPropagator
        
        Overrides: setAttitudeProvider in class FieldAbstractPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    def setMu(self, mu: _FieldAbstractIntegratedPropagator__T) -> None:
        """
        Set the central attraction coefficient μ.
        
        Parameters:
            mu (FieldAbstractIntegratedPropagator): central attraction coefficient (m³/s²)
        
        
        """
        ...
    def setResetAtEnd(self, resetAtEnd: bool) -> None:
        """
        Allow/disallow resetting the initial state at end of propagation.
        
        By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a new propagation to be started from there without recomputing the part already performed. Calling this method with resetAtEnd set to false changes prevents such reset.
        
        Parameters:
            resetAtEnd (boolean): if true, at end of each propagation, the getInitialState will be
                reset to the final state of the propagation, otherwise the initial state will be preserved
        
        Since:
            9.0
        
        
        """
        ...
    class MainStateEquations(typing.Generic[_FieldAbstractIntegratedPropagator__MainStateEquations__T]):
        def computeDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__MainStateEquations__T]) -> typing.MutableSequence[_FieldAbstractIntegratedPropagator__MainStateEquations__T]: ...
        def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__MainStateEquations__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__MainStateEquations__T]) -> None: ...

_FieldAdditionalDerivativesProvider__T = typing.TypeVar('_FieldAdditionalDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdditionalDerivativesProvider(typing.Generic[_FieldAdditionalDerivativesProvider__T]):
    """
    Provider for additional derivatives.
    
    In some cases users may need to integrate some problem-specific equations along with classical spacecraft equations of motions. One example is optimal control in low thrust where adjoint parameters linked to the minimized Hamiltonian must be integrated. Another example is formation flying or rendez-vous which use the Clohessy-Whiltshire equations for the relative motion.
    
    This interface allows users to add such equations to a FieldNumericalPropagator or a FieldDSSTPropagator. Users provide the equations as an implementation of this interface and register it to the propagator thanks to its addAdditionalDerivativesProvider method. Several such objects can be registered with each numerical propagator, but it is recommended to gather in the same object the sets of parameters which equations can interact on each others states.
    
    This interface is the numerical (read not already integrated) counterpart of the FieldAdditionalDataProvider interface. It allows to append various additional state parameters to any FieldNumericalPropagator or FieldDSSTPropagator.
    
    Since:
        11.1
    
    Also see:
        FieldAbstractIntegratedPropagator
    """
    def combinedDerivatives(self, s: org.orekit.propagation.FieldSpacecraftState[_FieldAdditionalDerivativesProvider__T]) -> 'FieldCombinedDerivatives'[_FieldAdditionalDerivativesProvider__T]:
        """
        Compute the derivatives related to the additional state (and optionally main state increments).
        
        Parameters:
            s (FieldSpacecraftState<FieldAdditionalDerivativesProvider> s): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        Since:
            11.2
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the generated derivative.
        
        Returns:
            dimension of the generated
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional derivatives (which will become state once integrated).
        
        Returns:
            name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldAdditionalDerivativesProvider__T], target: org.orekit.time.FieldAbsoluteDate[_FieldAdditionalDerivativesProvider__T]) -> None:
        """
        Initialize the generator at the start of propagation.
        
        Parameters:
            initialState (FieldSpacecraftState<FieldAdditionalDerivativesProvider> initialState): initial state information at the start of propagation
            target (FieldAbsoluteDate<FieldAdditionalDerivativesProvider> target): date of propagation
        
        
        """
        ...
    def yields(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldAdditionalDerivativesProvider__T]) -> bool:
        """
        Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional state being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final FieldSpacecraftState<T> state) {
             return !state.getAdditionalStates().containsKey("STM");
         }
         
        
        The default implementation returns false, meaning that derivative data can be combinedDerivatives immediately.
        
        Parameters:
            state (FieldSpacecraftState<FieldAdditionalDerivativesProvider> state): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

_FieldCombinedDerivatives__T = typing.TypeVar('_FieldCombinedDerivatives__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCombinedDerivatives(typing.Generic[_FieldCombinedDerivatives__T]):
    """
    Container for additional derivatives.
    
    Since:
        11.2
    
    Also see:
        FieldAdditionalDerivativesProvider
    """
    def __init__(self, additionalDerivatives: typing.Union[typing.List[_FieldCombinedDerivatives__T], jpype.JArray], mainStateDerivativesIncrements: typing.Union[typing.List[_FieldCombinedDerivatives__T], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            additionalDerivatives (FieldCombinedDerivatives[]): additional state derivatives
            mainStateDerivativesIncrements (FieldCombinedDerivatives[]): increments related to the main state parameters (may be null if main state should not be incremented)
        
        
        """
        ...
    def getAdditionalDerivatives(self) -> typing.MutableSequence[_FieldCombinedDerivatives__T]:
        """
        Get the derivatives related to the additional state.
        
        Returns:
            additional state derivatives
        
        
        """
        ...
    def getMainStateDerivativesIncrements(self) -> typing.MutableSequence[_FieldCombinedDerivatives__T]:
        """
        Get the derivatives increments related to the main state.
        
        Returns:
            primary state derivatives increments, or null if main state should not be incremented
        
        
        """
        ...

_FieldIntegratedEphemeris__T = typing.TypeVar('_FieldIntegratedEphemeris__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldIntegratedEphemeris(org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldIntegratedEphemeris__T], org.orekit.propagation.FieldBoundedPropagator[_FieldIntegratedEphemeris__T], typing.Generic[_FieldIntegratedEphemeris__T]):
    """
    This class stores sequentially generated orbital parameters for later retrieval.
    
    Instances of this class are built automatically when the getEphemerisGenerator method has been called. They are created when propagation is over. Random access to any intermediate state of the orbit throughout the propagation range is possible afterwards through this object.
    
    A typical use case is for numerically integrated orbits, which can be used by algorithms that need to wander around according to their own algorithm without cumbersome tight links with the integrator.
    
    As this class implements the Propagator interface, it can itself be used in batch mode to build another instance of the same type. This is however not recommended since it would be a waste of resources.
    
    Note that this class stores all intermediate states along with interpolation models, so it may be memory intensive.
    
    Also see:
        NumericalPropagator
    """
    def __init__(self, startDate: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], minDate: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], maxDate: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], mapper: 'FieldStateMapper'[_FieldIntegratedEphemeris__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, type: org.orekit.propagation.PropagationType, model: org.hipparchus.ode.FieldDenseOutputModel[_FieldIntegratedEphemeris__T], unmanaged: org.orekit.utils.FieldDataDictionary[_FieldIntegratedEphemeris__T], providers: java.util.List[org.orekit.propagation.FieldAdditionalDataProvider[typing.Any, _FieldIntegratedEphemeris__T]], equations: typing.Union[typing.List[str], jpype.JArray], dimensions: typing.Union[typing.List[int], jpype.JArray]):
        """
        Creates a new instance of IntegratedEphemeris.
        
        Parameters:
            startDate (FieldAbsoluteDate<FieldIntegratedEphemeris> startDate): Start date of the integration (can be minDate or maxDate)
            minDate (FieldAbsoluteDate<FieldIntegratedEphemeris> minDate): first date of the range
            maxDate (FieldAbsoluteDate<FieldIntegratedEphemeris> maxDate): last date of the range
            mapper (FieldStateMapper<FieldIntegratedEphemeris> mapper): mapper between raw double components and spacecraft state
            attitudeProvider (AttitudeProvider): attitude provider
            type (PropagationType): type of orbit to output (mean or osculating)
            model (FieldDenseOutputModel<FieldIntegratedEphemeris> model): underlying raw mathematical model
            unmanaged (FieldDataDictionary<FieldIntegratedEphemeris> unmanaged): unmanaged additional states that must be simply copied
            providers (List<FieldAdditionalDataProvider<?, FieldIntegratedEphemeris>>): generators for pre-integrated states
            equations (String[]): names of additional equations
            dimensions (int[]): dimensions of additional equations
        
        Since:
            13.0
        
        
        """
        ...
    def basicPropagate(self, date: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]:
        """
        Propagate an orbit without any fancy features.
        
        This method is similar in spirit to the propagate method, except that it does not call any handler during propagation, nor any discrete events, not additional states. It always stop exactly at the specified date.
        
        Overrides: basicPropagate in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldIntegratedEphemeris> date): target date for propagation
        
        Returns:
            state at specified date
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Description copied from class: getFrame Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface FieldPropagator
        
        Overrides: getFrame in class FieldAbstractPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface FieldPropagator
        
        Overrides: getInitialState in class FieldAbstractPropagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T]:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface FieldBoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T]:
        """
        Get the first date of the range.
        
        Specified by: getMinDate in interface FieldBoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
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
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], parameters: typing.Union[typing.List[_FieldIntegratedEphemeris__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_FieldIntegratedEphemeris__T]:
        """
        Propagate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldIntegratedEphemeris> date): target date for the orbit
            parameters (FieldIntegratedEphemeris[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Overrides: resetInitialState in class FieldAbstractPropagator
        
        Parameters:
            state (FieldSpacecraftState<FieldIntegratedEphemeris> state): new initial state to consider
        
        
        """
        ...
    def updateAdditionalData(self, original: org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]:
        """
        Update state by adding all additional data.
        
        Overrides: updateAdditionalData in class FieldAbstractPropagator
        
        Parameters:
            original (FieldSpacecraftState<FieldIntegratedEphemeris> original): original state
        
        Returns:
            updated state, with all additional data included
        
        Also see:
            addAdditionalDataProvider
        
        
        """
        ...

_FieldStateMapper__T = typing.TypeVar('_FieldStateMapper__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStateMapper(typing.Generic[_FieldStateMapper__T]):
    """
    This class maps between raw double elements and FieldSpacecraftState instances.
    """
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get the attitude provider.
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the inertial frame.
        
        Returns:
            inertial frame
        
        
        """
        ...
    def getMu(self) -> _FieldStateMapper__T:
        """
        Get the central attraction coefficient μ.
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get propagation parameter type.
        
        Returns:
            orbit type used for propagation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get propagation parameter type.
        
        Returns:
            angle type to use for propagation
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]:
        """
        Get reference date.
        
        Returns:
            reference date
        
        
        """
        ...
    @typing.overload
    def mapArrayToState(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T], tArray: typing.Union[typing.List[_FieldStateMapper__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldStateMapper__T], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.FieldSpacecraftState[_FieldStateMapper__T]: ...
    @typing.overload
    def mapArrayToState(self, t: _FieldStateMapper__T, tArray: typing.Union[typing.List[_FieldStateMapper__T], jpype.JArray], tArray2: typing.Union[typing.List[_FieldStateMapper__T], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.FieldSpacecraftState[_FieldStateMapper__T]: ...
    def mapDateToDouble(self, date: org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]) -> _FieldStateMapper__T:
        """
        Map a date to a raw double time offset.
        
        Parameters:
            date (FieldAbsoluteDate<FieldStateMapper> date): date
        
        Returns:
            time offset
        
        
        """
        ...
    @typing.overload
    def mapDoubleToDate(self, t: _FieldStateMapper__T) -> org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]: ...
    @typing.overload
    def mapDoubleToDate(self, t: _FieldStateMapper__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]) -> org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]: ...
    def mapStateToArray(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldStateMapper__T], y: typing.Union[typing.List[_FieldStateMapper__T], jpype.JArray], yDot: typing.Union[typing.List[_FieldStateMapper__T], jpype.JArray]) -> None:
        """
        Map a spacecraft state to raw double components.
        
        Parameters:
            state (FieldSpacecraftState<FieldStateMapper> state): state to map
            y (FieldStateMapper[]): placeholder where to put the components
            yDot (FieldStateMapper[]): placeholder where to put the components derivatives
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Setter for the attitude provider.
        
        Parameters:
            attitudeProvider (AttitudeProvider): new attitude provider
        
        
        """
        ...
    def setPositionAngleType(self) -> None:
        """
        Set position angle type.
        """
        ...

class IntegratedEphemeris(org.orekit.propagation.analytical.AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator):
    """
    This class stores sequentially generated orbital parameters for later retrieval.
    
    Instances of this class are built automatically when the getEphemerisGenerator method has been called. They are created when propagation is over. Random access to any intermediate state of the orbit throughout the propagation range is possible afterwards through this object.
    
    A typical use case is for numerically integrated orbits, which can be used by algorithms that need to wander around according to their own algorithm without cumbersome tight links with the integrator.
    
    As this class implements the Propagator interface, it can itself be used in batch mode to build another instance of the same type. This is however not recommended since it would be a waste of resources.
    
    Note that this class stores all intermediate states along with interpolation models, so it may be memory intensive.
    
    Also see:
        NumericalPropagator
    """
    def __init__(self, startDate: org.orekit.time.AbsoluteDate, minDate: org.orekit.time.AbsoluteDate, maxDate: org.orekit.time.AbsoluteDate, mapper: 'StateMapper', attitudeProvider: org.orekit.attitudes.AttitudeProvider, type: org.orekit.propagation.PropagationType, model: org.hipparchus.ode.DenseOutputModel, unmanaged: org.orekit.utils.DataDictionary, providers: java.util.List[org.orekit.propagation.AdditionalDataProvider[typing.Any]], equations: typing.Union[typing.List[str], jpype.JArray], dimensions: typing.Union[typing.List[int], jpype.JArray]):
        """
        Creates a new instance of IntegratedEphemeris.
        
        Parameters:
            startDate (AbsoluteDate): Start date of the integration (can be minDate or maxDate)
            minDate (AbsoluteDate): first date of the range
            maxDate (AbsoluteDate): last date of the range
            mapper (StateMapper): mapper between raw double components and spacecraft state
            attitudeProvider (AttitudeProvider): attitude provider
            type (PropagationType): type of orbit to output (mean or osculating)
            model (DenseOutputModel): underlying raw mathematical model
            unmanaged (DataDictionary): unmanaged additional states that must be simply copied
            providers (List<AdditionalDataProvider<?>>): providers for pre-integrated states
            equations (String[]): names of additional equations
            dimensions (int[]): dimensions of additional equations
        
        Since:
            13.0
        
        
        """
        ...
    def basicPropagate(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Propagate an orbit without any fancy features.
        
        This method is similar in spirit to the propagate method, except that it does not call any handler during propagation, nor any discrete events, not additional states. It always stops exactly at the specified date.
        
        Overrides: basicPropagate in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for propagation
        
        Returns:
            state at specified date
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Description copied from class: getFrame Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null.
        
        Specified by: getFrame in interface Propagator
        
        Overrides: getFrame in class AbstractPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Get the propagator initial state.
        
        Specified by: getInitialState in interface Propagator
        
        Overrides: getInitialState in class AbstractPropagator
        
        Returns:
            initial state
        
        
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
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface Propagator
        
        Overrides: setAttitudeProvider in class AbstractPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    def updateAdditionalData(self, original: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Update state by adding all additional data.
        
        Overrides: updateAdditionalData in class AbstractPropagator
        
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

class StateMapper:
    """
    This class maps between raw double elements and SpacecraftState instances.
    
    Since:
        6.0
    """
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get the attitude provider.
        
        Returns:
            attitude provider
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the inertial frame.
        
        Returns:
            inertial frame
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central attraction coefficient μ.
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get propagation parameter type.
        
        Returns:
            orbit type used for propagation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get propagation parameter type.
        
        Returns:
            angle type to use for propagation
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get reference date.
        
        Returns:
            reference date
        
        
        """
        ...
    @typing.overload
    def mapArrayToState(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.SpacecraftState:
        """
        Map the raw double components to a spacecraft state.
        
        Parameters:
            t (double): date offset
            y (double[]): state components
            yDot (double[]): time derivatives of the state components (null if unknown, in which case Keplerian motion is assumed)
            type (PropagationType): type of the elements used to build the state (mean or osculating).
        
        Returns:
            spacecraft state
        
        Map the raw double components to a spacecraft state.
        
        Parameters:
            date (AbsoluteDate): of the state components
            y (double[]): state components
            yDot (double[]): time derivatives of the state components (null if unknown, in which case Keplerian motion is assumed)
            type (PropagationType): type of the elements used to build the state (mean or osculating).
        
        Returns:
            spacecraft state
        
        
        """
        ...
    @typing.overload
    def mapArrayToState(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.SpacecraftState: ...
    def mapDateToDouble(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Map a date to a raw double time offset.
        
        Parameters:
            date (AbsoluteDate): date
        
        Returns:
            time offset
        
        
        """
        ...
    @typing.overload
    def mapDoubleToDate(self, double: float) -> org.orekit.time.AbsoluteDate:
        """
        Map the raw double time offset to a date.
        
        Parameters:
            t (double): date offset
        
        Returns:
            date
        
        Map the raw double time offset to a date.
        
        Parameters:
            t (double): date offset
            date (AbsoluteDate): The expected date.
        
        Returns:
            date if it is the same time as t to within the lower precision of the latter. Otherwise a new date is
            returned that corresponds to time t.
        
        
        """
        ...
    @typing.overload
    def mapDoubleToDate(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.time.AbsoluteDate: ...
    def mapStateToArray(self, state: org.orekit.propagation.SpacecraftState, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Map a spacecraft state to raw double components.
        
        Parameters:
            state (SpacecraftState): state to map
            y (double[]): placeholder where to put the components
            yDot (double[]): placeholder where to put the components derivatives
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set the attitude provider.
        
        Parameters:
            attitudeProvider (AttitudeProvider): the provider to set
        
        
        """
        ...

class PythonAbstractGradientConverter(AbstractGradientConverter):
    def __init__(self, freeStateParameters: int):
        """
        Simple constructor.
        
        Parameters:
            freeStateParameters (int): number of free parameters
        
        
        """
        ...
    @typing.overload
    def extend(self, gradient: org.hipparchus.analysis.differentiation.Gradient, int: int) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Add zero derivatives.
        
        Overrides: extend in class AbstractGradientConverter
        
        Parameters:
            original (Gradient): original scalar
            freeParameters (int): total number of free parameters in the gradient
        
        Returns:
            extended scalar
        
        public FieldVector3D<Gradient> extend (FieldVector3D<Gradient> original, int freeParameters)
        
        Add zero derivatives.
        
        Overrides: extend in class AbstractGradientConverter
        
        Parameters:
            original (FieldVector3D<Gradient> original): original vector
            freeParameters (int): total number of free parameters in the gradient
        
        Returns:
            extended vector
        
        public FieldRotation<Gradient> extend (FieldRotation<Gradient> original, int freeParameters)
        
        Add zero derivatives.
        
        Overrides: extend in class AbstractGradientConverter
        
        Parameters:
            original (FieldRotation<Gradient> original): original rotation
            freeParameters (int): total number of free parameters in the gradient
        
        Returns:
            extended rotation
        
        
        """
        ...
    @typing.overload
    def extend(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.Gradient], int: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def extend(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.Gradient], int: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.Gradient]: ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getFreeStateParameters(self) -> int:
        """
        Get the number of free state parameters.
        
        Overrides: getFreeStateParameters in class AbstractGradientConverter
        
        Returns:
            number of free state parameters
        
        
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

class PythonAbstractIntegratedPropagator(AbstractIntegratedPropagator):
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator, propagationType: org.orekit.propagation.PropagationType): ...
    def createMapper(self, referenceDate: org.orekit.time.AbsoluteDate, mu: float, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame) -> StateMapper:
        """
        Create a mapper between raw double components and spacecraft state. /** Simple constructor.
        
        The position parameter type is meaningful only if getOrbitType support it. As an example, it is not meaningful for propagation in CARTESIAN parameters.
        
        Specified by: createMapper in class AbstractIntegratedPropagator
        
        Parameters:
            referenceDate (AbsoluteDate): reference date
            mu (double): central attraction coefficient (m³/s²)
            orbitType (OrbitType): orbit type to use for mapping
            positionAngleType (PositionAngleType): angle type to use for propagation
            attitudeProvider (AttitudeProvider): attitude provider
            frame (Frame): inertial frame
        
        Returns:
            new mapper
        
        
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
    def getMainStateEquations(self, integ: org.hipparchus.ode.ODEIntegrator) -> AbstractIntegratedPropagator.MainStateEquations:
        """
        Get the differential equations to integrate (for main state only).
        
        Specified by: getMainStateEquations in class AbstractIntegratedPropagator
        
        Parameters:
            integ (ODEIntegrator): numerical integrator to use for propagation.
        
        Returns:
            differential equations for main state
        
        
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

class PythonAdditionalDerivativesProvider(AdditionalDerivativesProvider):
    def __init__(self): ...
    def combinedDerivatives(self, s: org.orekit.propagation.SpacecraftState) -> CombinedDerivatives:
        """
        Description copied from interface: combinedDerivatives Compute the derivatives related to the additional state (and optionally main state increments).
        
        Specified by: combinedDerivatives in interface AdditionalDerivativesProvider
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
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
    def getDimension(self) -> int:
        """
        Get the dimension of the generated derivative.
        
        Specified by: getDimension in interface AdditionalDerivativesProvider
        
        Returns:
            dimension of the generated
        
        
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
    def yields(self, state: org.orekit.propagation.SpacecraftState) -> bool:
        """
        Description copied from interface: yields Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional state being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final SpacecraftState state) {
             return !state.getAdditionalStates().containsKey("STM");
         }
         
        
        The default implementation returns false, meaning that derivative data can be combinedDerivatives immediately.
        
        Specified by: yields in interface AdditionalDerivativesProvider
        
        Parameters:
            state (SpacecraftState): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

_PythonFieldAbstractIntegratedPropagator__T = typing.TypeVar('_PythonFieldAbstractIntegratedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractIntegratedPropagator(FieldAbstractIntegratedPropagator[_PythonFieldAbstractIntegratedPropagator__T], typing.Generic[_PythonFieldAbstractIntegratedPropagator__T]):
    def __init__(self, integrator: org.hipparchus.Field[_PythonFieldAbstractIntegratedPropagator__T], propagationType: org.hipparchus.ode.FieldODEIntegrator[_PythonFieldAbstractIntegratedPropagator__T], field: org.orekit.propagation.PropagationType):
        """
        Build a new instance.
        
        Parameters:
            integrator (Field<PythonFieldAbstractIntegratedPropagator> field): numerical integrator to use for propagation.
            propagationType (FieldODEIntegrator<PythonFieldAbstractIntegratedPropagator> integrator): type of orbit to output (mean or osculating).
            field (PropagationType): Field used by default
        
        
        """
        ...
    def createMapper(self, referenceDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractIntegratedPropagator__T], mu: _PythonFieldAbstractIntegratedPropagator__T, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame) -> FieldStateMapper[_PythonFieldAbstractIntegratedPropagator__T]:
        """
        Create a mapper between raw double components and spacecraft state. /** Simple constructor.
        
        The position parameter type is meaningful only if getOrbitType support it. As an example, it is not meaningful for propagation in CARTESIAN parameters.
        
        Specified by: createMapper in class FieldAbstractIntegratedPropagator
        
        Parameters:
            referenceDate (FieldAbsoluteDate<PythonFieldAbstractIntegratedPropagator> referenceDate): reference date
            mu (PythonFieldAbstractIntegratedPropagator): central attraction coefficient (m³/s²)
            orbitType (OrbitType): orbit type to use for mapping
            positionAngleType (PositionAngleType): angle type to use for propagation
            attitudeProvider (AttitudeProvider): attitude provider
            frame (Frame): inertial frame
        
        Returns:
            new mapper
        
        
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
    def getMainStateEquations(self, integ: org.hipparchus.ode.FieldODEIntegrator[_PythonFieldAbstractIntegratedPropagator__T]) -> FieldAbstractIntegratedPropagator.MainStateEquations[_PythonFieldAbstractIntegratedPropagator__T]:
        """
        Get the differential equations to integrate (for main state only).
        
        Specified by: getMainStateEquations in class FieldAbstractIntegratedPropagator
        
        Parameters:
            integ (FieldODEIntegrator<PythonFieldAbstractIntegratedPropagator> integ): numerical integrator to use for propagation.
        
        Returns:
            differential equations for main state
        
        
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

_PythonFieldAdditionalDerivativesProvider__T = typing.TypeVar('_PythonFieldAdditionalDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdditionalDerivativesProvider(FieldAdditionalDerivativesProvider[_PythonFieldAdditionalDerivativesProvider__T], typing.Generic[_PythonFieldAdditionalDerivativesProvider__T]):
    def __init__(self): ...
    def combinedDerivatives(self, s: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdditionalDerivativesProvider__T]) -> FieldCombinedDerivatives[_PythonFieldAdditionalDerivativesProvider__T]:
        """
        Description copied from interface: combinedDerivatives Compute the derivatives related to the additional state (and optionally main state increments).
        
        Specified by: combinedDerivatives in interface FieldAdditionalDerivativesProvider
        
        Parameters:
            s (FieldSpacecraftState<PythonFieldAdditionalDerivativesProvider> s): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the generated derivative.
        
        Specified by: getDimension in interface FieldAdditionalDerivativesProvider
        
        Returns:
            dimension of the generated
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional derivatives (which will become state once integrated).
        
        Specified by: getName in interface FieldAdditionalDerivativesProvider
        
        Returns:
            name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdditionalDerivativesProvider__T], target: org.orekit.time.FieldAbsoluteDate[_PythonFieldAdditionalDerivativesProvider__T]) -> None:
        """
        Description copied from interface: init Initialize the generator at the start of propagation.
        
        Specified by: init in interface FieldAdditionalDerivativesProvider
        
        Parameters:
            initialState (FieldSpacecraftState<PythonFieldAdditionalDerivativesProvider> initialState): initial state information at the start of propagation
            target (FieldAbsoluteDate<PythonFieldAdditionalDerivativesProvider> target): date of propagation
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def yields(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdditionalDerivativesProvider__T]) -> bool:
        """
        Description copied from interface: yields Check if this provider should yield so another provider has an opportunity to add missing parts.
        
        Decision to yield is often based on an additional state being hasAdditionalData in the provided state (but it could theoretically also depend on an additional state derivative being hasAdditionalStateDerivative, or any other criterion). If for example a provider needs the state transition matrix, it could implement this method as:
        
        
         public boolean yields(final FieldSpacecraftState<T> state) {
             return !state.getAdditionalStates().containsKey("STM");
         }
         
        
        The default implementation returns false, meaning that derivative data can be combinedDerivatives immediately.
        
        Specified by: yields in interface FieldAdditionalDerivativesProvider
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldAdditionalDerivativesProvider> state): state to handle
        
        Returns:
            true if this provider should yield so another provider has an opportunity to add missing parts as the state is
            incrementally built up
        
        
        """
        ...

_PythonFieldStateMapper__T = typing.TypeVar('_PythonFieldStateMapper__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldStateMapper(FieldStateMapper[_PythonFieldStateMapper__T], typing.Generic[_PythonFieldStateMapper__T]):
    def __init__(self, referenceDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldStateMapper__T], mu: _PythonFieldStateMapper__T, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        The position parameter type is meaningful only if getOrbitType support it. As an example, it is not meaningful for propagation in CARTESIAN parameters.
        
        Parameters:
            referenceDate (FieldAbsoluteDate<PythonFieldStateMapper> referenceDate): reference date
            mu (PythonFieldStateMapper): central attraction coefficient (m³/s²)
            orbitType (OrbitType): orbit type to use for mapping
            positionAngleType (PositionAngleType): angle type to use for propagation
            attitudeProvider (AttitudeProvider): attitude provider
            frame (Frame): inertial frame
        
        
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
    @typing.overload
    def mapArrayToState(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldStateMapper__T], tArray: typing.Union[typing.List[_PythonFieldStateMapper__T], jpype.JArray], tArray2: typing.Union[typing.List[_PythonFieldStateMapper__T], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldStateMapper__T]: ...
    @typing.overload
    def mapArrayToState(self, t: _PythonFieldStateMapper__T, tArray: typing.Union[typing.List[_PythonFieldStateMapper__T], jpype.JArray], tArray2: typing.Union[typing.List[_PythonFieldStateMapper__T], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.FieldSpacecraftState[_PythonFieldStateMapper__T]: ...
    def mapStateToArray(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldStateMapper__T], y: typing.Union[typing.List[_PythonFieldStateMapper__T], jpype.JArray], yDot: typing.Union[typing.List[_PythonFieldStateMapper__T], jpype.JArray]) -> None:
        """
        Map a spacecraft state to raw double components.
        
        Specified by: mapStateToArray in class FieldStateMapper
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldStateMapper> state): state to map
            y (PythonFieldStateMapper[]): placeholder where to put the components
            yDot (PythonFieldStateMapper[]): placeholder where to put the components derivatives
        
        
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

class PythonStateMapper(StateMapper):
    def __init__(self, referenceDate: org.orekit.time.AbsoluteDate, mu: float, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame):
        """
        Simple constructor.
        
        The position parameter type is meaningful only if getOrbitType support it. As an example, it is not meaningful for propagation in CARTESIAN parameters.
        
        Parameters:
            referenceDate (AbsoluteDate): reference date
            mu (double): central attraction coefficient (m³/s²)
            orbitType (OrbitType): orbit type to use for mapping, null for propagating using AbsolutePVCoordinates rather than
                package
            positionAngleType (PositionAngleType): angle type to use for propagation
            attitudeProvider (AttitudeProvider): attitude provider
            frame (Frame): inertial frame
        
        
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
    @typing.overload
    def mapArrayToState(self, date: org.orekit.time.AbsoluteDate, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray], type: org.orekit.propagation.PropagationType) -> org.orekit.propagation.SpacecraftState:
        """
        Map the raw double components to a spacecraft state.
        
        Specified by: mapArrayToState in class StateMapper
        
        Parameters:
            date (AbsoluteDate): of the state components
            y (double[]): state components
            yDot (double[]): time derivatives of the state components (null if unknown, in which case Keplerian motion is assumed)
            type (PropagationType): type of the elements used to build the state (mean or osculating).
        
        Returns:
            spacecraft state
        
        
        """
        ...
    @typing.overload
    def mapArrayToState(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.SpacecraftState: ...
    def mapStateToArray(self, state: org.orekit.propagation.SpacecraftState, y: typing.Union[typing.List[float], jpype.JArray], yDot: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Map a spacecraft state to raw double components.
        
        Specified by: mapStateToArray in class StateMapper
        
        Parameters:
            state (SpacecraftState): state to map
            y (double[]): placeholder where to put the components
            yDot (double[]): placeholder where to put the components derivatives
        
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.integration")``.

    AbstractGradientConverter: typing.Type[AbstractGradientConverter]
    AbstractIntegratedPropagator: typing.Type[AbstractIntegratedPropagator]
    AdditionalDerivativesProvider: typing.Type[AdditionalDerivativesProvider]
    CombinedDerivatives: typing.Type[CombinedDerivatives]
    FieldAbstractIntegratedPropagator: typing.Type[FieldAbstractIntegratedPropagator]
    FieldAdditionalDerivativesProvider: typing.Type[FieldAdditionalDerivativesProvider]
    FieldCombinedDerivatives: typing.Type[FieldCombinedDerivatives]
    FieldIntegratedEphemeris: typing.Type[FieldIntegratedEphemeris]
    FieldStateMapper: typing.Type[FieldStateMapper]
    IntegratedEphemeris: typing.Type[IntegratedEphemeris]
    PythonAbstractGradientConverter: typing.Type[PythonAbstractGradientConverter]
    PythonAbstractIntegratedPropagator: typing.Type[PythonAbstractIntegratedPropagator]
    PythonAdditionalDerivativesProvider: typing.Type[PythonAdditionalDerivativesProvider]
    PythonFieldAbstractIntegratedPropagator: typing.Type[PythonFieldAbstractIntegratedPropagator]
    PythonFieldAdditionalDerivativesProvider: typing.Type[PythonFieldAdditionalDerivativesProvider]
    PythonFieldStateMapper: typing.Type[PythonFieldStateMapper]
    PythonStateMapper: typing.Type[PythonStateMapper]
    StateMapper: typing.Type[StateMapper]
