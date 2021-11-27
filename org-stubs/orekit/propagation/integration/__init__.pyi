import java.util
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
    public abstract class AbstractGradientConverter extends Object
    
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

class AbstractIntegratedPropagator(org.orekit.propagation.AbstractPropagator):
    """
    public abstract class AbstractIntegratedPropagator extends :class:`~org.orekit.propagation.AbstractPropagator`
    
        Common handling of :class:`~org.orekit.propagation.Propagator` methods for both numerical and semi-analytical
        propagators.
    """
    def addAdditionalEquations(self, additionalEquations: 'AdditionalEquations') -> None:
        """
            Add a set of user-specified equations to be integrated along with the orbit propagation.
        
            Parameters:
                additional (:class:`~org.orekit.propagation.integration.AdditionalEquations`): additional equations
        
        
        """
        ...
    def addEventDetector(self, eventDetector: org.orekit.propagation.events.EventDetector) -> None:
        """
            Add an event detector.
        
            Parameters:
                detector (:class:`~org.orekit.propagation.events.EventDetector`): event detector to add
        
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
        
            The number of calls is reset each time the
            :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.propagate` method is called.
        
            Returns:
                number of calls to the differential equations computation method
        
        
        """
        ...
    def getEphemerisGenerator(self) -> org.orekit.propagation.EphemerisGenerator:
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
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getManagedAdditionalStates`Â in
                interfaceÂ :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getManagedAdditionalStates`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient Î¼.
        
            Returns:
                mu central attraction coefficient (mÂ³/sÂ²)
        
            Also see:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setMu`
        
        
        """
        ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which an :class:`~org.orekit.propagation.AdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider` method. If the propagator is an
            :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`, the states for which a set of
            :class:`~org.orekit.propagation.integration.AdditionalEquations` has been registered by calling the
            :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.addAdditionalEquations` method are also counted
            as managed additional states.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.Propagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.EventHandler.resetState` method is called at an event occurrence
            and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.isAdditionalStateManaged`Â in
                interfaceÂ :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.isAdditionalStateManaged`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                name (String): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
            Propagate towards a target date.
        
            Simple propagators use only the target date as the specification for computing the propagated state. More feature rich
            propagators can consider other information and provide different operating modes or G-stop facilities to stop at
            pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.propagate`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
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
                tStart (:class:`~org.orekit.time.AbsoluteDate`): start date from which orbit state should be propagated
                tEnd (:class:`~org.orekit.time.AbsoluteDate`): target date to which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.setAttitudeProvider`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    def setMu(self, double: float) -> None:
        """
            Set the central attraction coefficient Î¼.
        
            Parameters:
                mu (double): central attraction coefficient (mÂ³/sÂ²)
        
        
        """
        ...
    def setResetAtEnd(self, boolean: bool) -> None:
        """
            Allow/disallow resetting the initial state at end of propagation.
        
            By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a
            new propagation to be started from there without recomputing the part already performed. Calling this method with
            :code:`resetAtEnd` set to false changes prevents such reset.
        
            Parameters:
                resetAtEnd (boolean): if true, at end of each propagation, the :meth:`~org.orekit.propagation.AbstractPropagator.getInitialState` will be
                    reset to the final state of the propagation, otherwise the initial state will be preserved
        
            Since:
                9.0
        
        
        """
        ...
    class MainStateEquations:
        def computeDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]: ...
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class AbstractJacobiansMapper:
    """
    public abstract class AbstractJacobiansMapper extends Object
    
        Base class for jacobian mapper.
    
        Since:
            10.0
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int STATE_DIMENSION
    
        State dimension, fixed to 6.
    
        Since:
            9.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def analyticalDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Compute the derivatives needed by analytical orbit determination methods.
        
            Analytical derivatives are used to calculate state transition matrix of analytical orbit propagators and short period
            derivatives of DSST orbit propagator. In other word, this method does nothing for the numerical propagator.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state with respect to which calculate derivatives
        
        
        """
        ...
    def getAdditionalStateDimension(self) -> int:
        """
            Compute the length of the one-dimensional additional state array needed.
        
            Returns:
                length of the one-dimensional additional state array
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the partial Jacobians.
        
            Returns:
                name of the Jacobians
        
        
        """
        ...
    def getParameters(self) -> int:
        """
            Get the number of parameters.
        
            Returns:
                number of parameters
        
        
        """
        ...
    def getParametersJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Get the Jacobian with respect to parameters from a one-dimensional additional state array.
        
            This method extract the data from the :code:`state` and put it in the :code:`dYdP` array.
        
            If no parameters have been set in the constructor, the method returns immediately and does not reference :code:`dYdP`
            which can safely be null in this case.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dYdP (double[][]): placeholder where to put the Jacobian with respect to parameters
        
            Also see:
        
        
        """
        ...
    def getStateJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Get the Jacobian with respect to state from a one-dimensional additional state array.
        
            This method extract the data from the :code:`state` and put it in the :code:`dYdY0` array.
        
            For :class:`~org.orekit.propagation.numerical.JacobiansMapper` and
            :class:`~org.orekit.propagation.analytical.tle.TLEJacobiansMapper`, the method provides the Jacobian with respect to
            Cartesian elements. For :class:`~org.orekit.propagation.semianalytical.dsst.DSSTJacobiansMapper` the method provides the
            Jacobian with respect to Equinoctial elements.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dYdY0 (double[][]): placeholder where to put the Jacobian with respect to state
        
            Also see:
        
        
        """
        ...
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[float]) -> None:
        """
            Set the Jacobian with respect to state into a one-dimensional additional state array.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dY1dY0 (double[][]): Jacobian of current state at time tâ‚� with respect to state at some previous time tâ‚€
                dY1dP (double[][]): Jacobian of current state at time tâ‚� with respect to parameters (may be null if there are no parameters)
                p (double[]): placeholder where to put the one-dimensional additional state
        
            Also see:
        
        
        """
        ...

class AdditionalEquations:
    """
    public interface AdditionalEquations
    
        This interface allows users to add their own differential equations to a numerical propagator.
    
        In some cases users may need to integrate some problem-specific equations along with classical spacecraft equations of
        motions. One example is optimal control in low thrust where adjoint parameters linked to the minimized Hamiltonian must
        be integrated. Another example is formation flying or rendez-vous which use the Clohessy-Whiltshire equations for the
        relative motion.
    
        This interface allows users to add such equations to a :class:`~org.orekit.propagation.numerical.NumericalPropagator` or
        a :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`. Users provide the equations as an implementation
        of this interface and register it to the propagator thanks to its
        :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.addAdditionalEquations` method. Several such
        objects can be registered with each numerical propagator, but it is recommended to gather in the same object the sets of
        parameters which equations can interact on each others states.
    
        The additional parameters are gathered in a simple p array. The additional equations compute the pDot array, which is
        the time-derivative of the p array. Since the additional parameters p may also have an influence on the equations of
        motion themselves that should be accumulated to the main state derivatives (for example an equation linked to a complex
        thrust model may induce an acceleration and a mass change), the null method can return a double array that will be
        *added* to the main state derivatives. This means these equations can be used as an additional force model if needed. If
        the additional parameters have no influence at all on the main spacecraft state, a null reference may be returned.
    
        This interface is the numerical (read not already integrated) counterpart of the
        :class:`~org.orekit.propagation.AdditionalStateProvider` interface. It allows to append various additional state
        parameters to any :class:`~org.orekit.propagation.numerical.NumericalPropagator` or
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        Also see:
            :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`,
            :class:`~org.orekit.propagation.AdditionalStateProvider`
    """
    def computeDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Compute the derivatives related to the additional state parameters.
        
            When this method is called, the spacecraft state contains the main state (orbit, attitude and mass), all the states
            provided through the :class:`~org.orekit.propagation.AdditionalStateProvider` registered to the propagator, and the
            additional state integrated using this equation. It does *not* contains any other states to be integrated alongside
            during the same propagation.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional state
                pDot (double[]): placeholder where the derivatives of the additional parameters should be put
        
            Returns:
                cumulative effect of the equations on the main state (may be null if equations do not change main state at all)
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Returns:
                name of the additional state
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the equations at the start of propagation.
        
            This method will be called once at propagation start, before any calls to null.
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...

_FieldAbstractIntegratedPropagator__MainStateEquations__T = typing.TypeVar('_FieldAbstractIntegratedPropagator__MainStateEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldAbstractIntegratedPropagator__T = typing.TypeVar('_FieldAbstractIntegratedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractIntegratedPropagator(org.orekit.propagation.FieldAbstractPropagator[_FieldAbstractIntegratedPropagator__T], typing.Generic[_FieldAbstractIntegratedPropagator__T]):
    """
    public abstract class FieldAbstractIntegratedPropagator<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.FieldAbstractPropagator`<T>
    
        Common handling of :class:`~org.orekit.propagation.FieldPropagator` methods for both numerical and semi-analytical
        propagators.
    """
    def addAdditionalEquations(self, fieldAdditionalEquations: 'FieldAdditionalEquations'[_FieldAbstractIntegratedPropagator__T]) -> None: ...
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
        
            The number of calls is reset each time the
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.propagate` method is called.
        
            Returns:
                number of calls to the differential equations computation method
        
        
        """
        ...
    def getEphemerisGenerator(self) -> org.orekit.propagation.FieldEphemerisGenerator[_FieldAbstractIntegratedPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_FieldAbstractIntegratedPropagator__T]]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]:
        """
            Get all the names of all managed states.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getManagedAdditionalStates`Â in
                interfaceÂ :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.FieldAbstractPropagator.getManagedAdditionalStates`Â in
                classÂ :class:`~org.orekit.propagation.FieldAbstractPropagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMu(self) -> _FieldAbstractIntegratedPropagator__T:
        """
            Get the central attraction coefficient Î¼.
        
            Returns:
                mu central attraction coefficient (mÂ³/sÂ²)
        
            Also see:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setMu`
        
        
        """
        ...
    def isAdditionalStateManaged(self, string: str) -> bool:
        """
            Check if an additional state is managed.
        
            Managed states are states for which the propagators know how to compute its evolution. They correspond to additional
            states for which an :class:`~org.orekit.propagation.FieldAdditionalStateProvider` has been registered by calling the
            :meth:`~org.orekit.propagation.FieldPropagator.addAdditionalStateProvider` method. If the propagator is an
            :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`, the states for which a set of
            :class:`~org.orekit.propagation.integration.FieldAdditionalEquations` has been registered by calling the
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalEquations` method are also
            counted as managed additional states.
        
            Additional states that are present in the :meth:`~org.orekit.propagation.FieldPropagator.getInitialState` but have no
            evolution method registered are *not* considered as managed states. These unmanaged additional states are not lost
            during propagation, though. Their value are piecewise constant between state resets that may change them if some event
            handler :meth:`~org.orekit.propagation.events.handlers.FieldEventHandler.resetState` method is called at an event
            occurrence and happens to change the unmanaged additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.isAdditionalStateManaged`Â in
                interfaceÂ :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.FieldAbstractPropagator.isAdditionalStateManaged`Â in
                classÂ :class:`~org.orekit.propagation.FieldAbstractPropagator`
        
            Parameters:
                name (String): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__T]: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.setAttitudeProvider`Â in
                interfaceÂ :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.FieldAbstractPropagator.setAttitudeProvider`Â in
                classÂ :class:`~org.orekit.propagation.FieldAbstractPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    def setMu(self, t: _FieldAbstractIntegratedPropagator__T) -> None:
        """
            Set the central attraction coefficient Î¼.
        
            Parameters:
                mu (:class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`): central attraction coefficient (mÂ³/sÂ²)
        
        
        """
        ...
    def setResetAtEnd(self, boolean: bool) -> None:
        """
            Allow/disallow resetting the initial state at end of propagation.
        
            By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a
            new propagation to be started from there without recomputing the part already performed. Calling this method with
            :code:`resetAtEnd` set to false changes prevents such reset.
        
            Parameters:
                resetAtEnd (boolean): if true, at end of each propagation, the :meth:`~org.orekit.propagation.FieldAbstractPropagator.getInitialState` will be
                    reset to the final state of the propagation, otherwise the initial state will be preserved
        
            Since:
                9.0
        
        
        """
        ...
    class MainStateEquations(typing.Generic[_FieldAbstractIntegratedPropagator__MainStateEquations__T]):
        def computeDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__MainStateEquations__T]) -> typing.List[_FieldAbstractIntegratedPropagator__MainStateEquations__T]: ...
        def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAbstractIntegratedPropagator__MainStateEquations__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractIntegratedPropagator__MainStateEquations__T]) -> None: ...

_FieldAdditionalEquations__T = typing.TypeVar('_FieldAdditionalEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAdditionalEquations(typing.Generic[_FieldAdditionalEquations__T]):
    """
    public interface FieldAdditionalEquations<T extends CalculusFieldElement<T>>
    
        This interface allows users to add their own differential equations to a numerical propagator.
    
        In some cases users may need to integrate some problem-specific equations along with classical spacecraft equations of
        motions. One example is optimal control in low thrust where adjoint parameters linked to the minimized Hamiltonian must
        be integrated. Another example is formation flying or rendez-vous which use the Clohessy-Whiltshire equations for the
        relative motion.
    
        This interface allows users to add such equations to a
        :class:`~org.orekit.propagation.numerical.FieldNumericalPropagator`. Users provide the equations as an implementation of
        this interface and register it to the propagator thanks to its
        :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalEquations` method. Several
        such objects can be registered with each numerical propagator, but it is recommended to gather in the same object the
        sets of parameters which equations can interact on each others states.
    
        The additional parameters are gathered in a simple p array. The additional equations compute the pDot array, which is
        the time-derivative of the p array. Since the additional parameters p may also have an influence on the equations of
        motion themselves that should be accumulated to the main state derivatives (for example an equation linked to a complex
        thrust model may induce an acceleration and a mass change), the null method can return a double array that will be
        *added* to the main state derivatives. This means these equations can be used as an additional force model if needed. If
        the additional parameters have no influence at all on the main spacecraft state, a null reference may be returned.
    
        This interface is the numerical (read not already integrated) counterpart of the
        :class:`~org.orekit.propagation.FieldAdditionalStateProvider` interface. It allows to append various additional state
        parameters to any :class:`~org.orekit.propagation.numerical.FieldNumericalPropagator`.
    
        Also see:
            :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`,
            :class:`~org.orekit.propagation.AdditionalStateProvider`
    """
    def computeDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdditionalEquations__T], tArray: typing.List[_FieldAdditionalEquations__T]) -> typing.List[_FieldAdditionalEquations__T]: ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Returns:
                name of the additional state
        
        
        """
        ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldAdditionalEquations__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAdditionalEquations__T]) -> None: ...

_FieldIntegratedEphemeris__T = typing.TypeVar('_FieldIntegratedEphemeris__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldIntegratedEphemeris(org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldIntegratedEphemeris__T], org.orekit.propagation.FieldBoundedPropagator[_FieldIntegratedEphemeris__T], typing.Generic[_FieldIntegratedEphemeris__T]):
    """
    public class FieldIntegratedEphemeris<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T> implements :class:`~org.orekit.propagation.FieldBoundedPropagator`<T>
    
        This class stores sequentially generated orbital parameters for later retrieval.
    
        Instances of this class are built automatically when the
        :meth:`~org.orekit.propagation.FieldPropagator.getEphemerisGenerator` method has been called. They are created when
        propagation is over. Random access to any intermediate state of the orbit throughout the propagation range is possible
        afterwards through this object.
    
        A typical use case is for numerically integrated orbits, which can be used by algorithms that need to wander around
        according to their own algorithm without cumbersome tight links with the integrator.
    
        As this class implements the :class:`~org.orekit.propagation.Propagator` interface, it can itself be used in batch mode
        to build another instance of the same type. This is however not recommended since it would be a waste of resources.
    
        Note that this class stores all intermediate states along with interpolation models, so it may be memory intensive.
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`
    """
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], fieldAbsoluteDate3: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], fieldStateMapper: 'FieldStateMapper'[_FieldIntegratedEphemeris__T], propagationType: org.orekit.propagation.PropagationType, fieldDenseOutputModel: org.hipparchus.ode.FieldDenseOutputModel[_FieldIntegratedEphemeris__T], map: typing.Union[java.util.Map[str, typing.List[_FieldIntegratedEphemeris__T]], typing.Mapping[str, typing.List[_FieldIntegratedEphemeris__T]]], list: java.util.List[org.orekit.propagation.FieldAdditionalStateProvider[_FieldIntegratedEphemeris__T]], stringArray: typing.List[str]): ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Description copied from class: :meth:`~org.orekit.propagation.FieldAbstractPropagator.getFrame`
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getFrame` in interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.FieldAbstractPropagator.getFrame`Â in
                classÂ :class:`~org.orekit.propagation.FieldAbstractPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]: ...
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T]: ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldIntegratedEphemeris__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldIntegratedEphemeris__T]: ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldIntegratedEphemeris__T]) -> None: ...

_FieldStateMapper__T = typing.TypeVar('_FieldStateMapper__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStateMapper(typing.Generic[_FieldStateMapper__T]):
    """
    public abstract class FieldStateMapper<T extends CalculusFieldElement<T>> extends Object
    
        This class maps between raw double elements and :class:`~org.orekit.propagation.FieldSpacecraftState` instances.
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
            Get the central attraction coefficient Î¼.
        
            Returns:
                mu central attraction coefficient (mÂ³/sÂ²)
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get propagation parameter type.
        
            Returns:
                orbit type used for propagation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngle:
        """
            Get propagation parameter type.
        
            Returns:
                angle type to use for propagation
        
        
        """
        ...
    def getReferenceDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]: ...
    @typing.overload
    def mapArrayToState(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T], tArray: typing.List[_FieldStateMapper__T], tArray2: typing.List[_FieldStateMapper__T], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.FieldSpacecraftState[_FieldStateMapper__T]: ...
    @typing.overload
    def mapArrayToState(self, t: _FieldStateMapper__T, tArray: typing.List[_FieldStateMapper__T], tArray2: typing.List[_FieldStateMapper__T], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.FieldSpacecraftState[_FieldStateMapper__T]: ...
    def mapDateToDouble(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]) -> _FieldStateMapper__T: ...
    @typing.overload
    def mapDoubleToDate(self, t: _FieldStateMapper__T) -> org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]: ...
    @typing.overload
    def mapDoubleToDate(self, t: _FieldStateMapper__T, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]) -> org.orekit.time.FieldAbsoluteDate[_FieldStateMapper__T]: ...
    def mapStateToArray(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldStateMapper__T], tArray: typing.List[_FieldStateMapper__T], tArray2: typing.List[_FieldStateMapper__T]) -> None: ...
    def setPositionAngleType(self) -> None:
        """
            Set position angle type.
        
        """
        ...

class IntegratedEphemeris(org.orekit.propagation.analytical.AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator):
    """
    public class IntegratedEphemeris extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator` implements :class:`~org.orekit.propagation.BoundedPropagator`
    
        This class stores sequentially generated orbital parameters for later retrieval.
    
        Instances of this class are built automatically when the
        :meth:`~org.orekit.propagation.Propagator.getEphemerisGenerator` method has been called. They are created when
        propagation is over. Random access to any intermediate state of the orbit throughout the propagation range is possible
        afterwards through this object.
    
        A typical use case is for numerically integrated orbits, which can be used by algorithms that need to wander around
        according to their own algorithm without cumbersome tight links with the integrator.
    
        As this class implements the :class:`~org.orekit.propagation.Propagator` interface, it can itself be used in batch mode
        to build another instance of the same type. This is however not recommended since it would be a waste of resources.
    
        Note that this class stores all intermediate states along with interpolation models, so it may be memory intensive.
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, absoluteDate3: org.orekit.time.AbsoluteDate, stateMapper: 'StateMapper', propagationType: org.orekit.propagation.PropagationType, denseOutputModel: org.hipparchus.ode.DenseOutputModel, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]], list: java.util.List[org.orekit.propagation.AdditionalStateProvider], stringArray: typing.List[str]): ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Description copied from class: :meth:`~org.orekit.propagation.AbstractPropagator.getFrame`
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getFrame` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getFrame`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState`
        
        
        """
        ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Get the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getInitialState`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Returns:
                initial state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the last date of the range.
        
            Specified by:
                :meth:`~org.orekit.propagation.BoundedPropagator.getMaxDate`Â in
                interfaceÂ :class:`~org.orekit.propagation.BoundedPropagator`
        
            Returns:
                the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.propagation.BoundedPropagator.getMinDate`Â in
                interfaceÂ :class:`~org.orekit.propagation.BoundedPropagator`
        
            Returns:
                the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getPVCoordinates`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.setAttitudeProvider`Â in
                classÂ :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...

class StateMapper:
    """
    public abstract class StateMapper extends Object
    
        This class maps between raw double elements and :class:`~org.orekit.propagation.SpacecraftState` instances.
    
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
            Get the central attraction coefficient Î¼.
        
            Returns:
                mu central attraction coefficient (mÂ³/sÂ²)
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get propagation parameter type.
        
            Returns:
                orbit type used for propagation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngle:
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
    def mapArrayToState(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float], doubleArray2: typing.List[float], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.SpacecraftState:
        """
            Map the raw double components to a spacecraft state.
        
            Parameters:
                t (double): date offset
                y (double[]): state components
                yDot (double[]): time derivatives of the state components (null if unknown, in which case Keplerian motion is assumed)
                type (:class:`~org.orekit.propagation.PropagationType`): type of the elements used to build the state (mean or osculating).
        
            Returns:
                spacecraft state
        
            Map the raw double components to a spacecraft state.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): of the state components
                y (double[]): state components
                yDot (double[]): time derivatives of the state components (null if unknown, in which case Keplerian motion is assumed)
                type (:class:`~org.orekit.propagation.PropagationType`): type of the elements used to build the state (mean or osculating).
        
            Returns:
                spacecraft state
        
        
        """
        ...
    @typing.overload
    def mapArrayToState(self, double: float, doubleArray: typing.List[float], doubleArray2: typing.List[float], propagationType: org.orekit.propagation.PropagationType) -> org.orekit.propagation.SpacecraftState: ...
    def mapDateToDouble(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Map a date to a raw double time offset.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
        
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
                date (:class:`~org.orekit.time.AbsoluteDate`): The expected date.
        
            Returns:
                :code:`date` if it is the same time as :code:`t` to within the lower precision of the latter. Otherwise a new date is
                returned that corresponds to time :code:`t`.
        
        
        """
        ...
    @typing.overload
    def mapDoubleToDate(self, double: float, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.time.AbsoluteDate: ...
    def mapStateToArray(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None:
        """
            Map a spacecraft state to raw double components.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state to map
                y (double[]): placeholder where to put the components
                yDot (double[]): placeholder where to put the components derivatives
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set the attitude provider.
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the provider to set
        
        
        """
        ...

class PythonAbstractGradientConverter(AbstractGradientConverter):
    def __init__(self, int: int): ...
    @typing.overload
    def extend(self, gradient: org.hipparchus.analysis.differentiation.Gradient, int: int) -> org.hipparchus.analysis.differentiation.Gradient: ...
    @typing.overload
    def extend(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.Gradient], int: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def extend(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.Gradient], int: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.Gradient]: ...
    def extend_FRi(self, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.Gradient], int: int) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[org.hipparchus.analysis.differentiation.Gradient]: ...
    def extend_FVi(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.Gradient], int: int) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.Gradient]: ...
    def getFreeStateParameters(self) -> int: ...

class PythonAbstractIntegratedPropagator(AbstractIntegratedPropagator):
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator, propagationType: org.orekit.propagation.PropagationType): ...
    def createMapper(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, orbitType: org.orekit.orbits.OrbitType, positionAngle: org.orekit.orbits.PositionAngle, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame) -> StateMapper: ...
    def finalize(self) -> None: ...
    def getMainStateEquations(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator) -> AbstractIntegratedPropagator.MainStateEquations: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonAdditionalEquations(AdditionalEquations):
    def __init__(self): ...
    def computeDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> typing.List[float]: ...
    def finalize(self) -> None: ...
    def getName(self) -> str: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldAbstractIntegratedPropagator__T = typing.TypeVar('_PythonFieldAbstractIntegratedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractIntegratedPropagator(FieldAbstractIntegratedPropagator[_PythonFieldAbstractIntegratedPropagator__T], typing.Generic[_PythonFieldAbstractIntegratedPropagator__T]):
    def __init__(self, field: org.hipparchus.Field[_PythonFieldAbstractIntegratedPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_PythonFieldAbstractIntegratedPropagator__T], propagationType: org.orekit.propagation.PropagationType): ...
    def createMapper(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractIntegratedPropagator__T], t: _PythonFieldAbstractIntegratedPropagator__T, orbitType: org.orekit.orbits.OrbitType, positionAngle: org.orekit.orbits.PositionAngle, attitudeProvider: org.orekit.attitudes.AttitudeProvider, frame: org.orekit.frames.Frame) -> FieldStateMapper[_PythonFieldAbstractIntegratedPropagator__T]: ...
    def finalize(self) -> None: ...
    def getMainStateEquations(self, fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_PythonFieldAbstractIntegratedPropagator__T]) -> FieldAbstractIntegratedPropagator.MainStateEquations[_PythonFieldAbstractIntegratedPropagator__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldAdditionalEquations__T = typing.TypeVar('_PythonFieldAdditionalEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdditionalEquations(FieldAdditionalEquations[_PythonFieldAdditionalEquations__T], typing.Generic[_PythonFieldAdditionalEquations__T]):
    def __init__(self): ...
    def computeDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdditionalEquations__T], tArray: typing.List[_PythonFieldAdditionalEquations__T]) -> typing.List[_PythonFieldAdditionalEquations__T]: ...
    def finalize(self) -> None: ...
    def getName(self) -> str: ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAdditionalEquations__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAdditionalEquations__T]) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.integration")``.

    AbstractGradientConverter: typing.Type[AbstractGradientConverter]
    AbstractIntegratedPropagator: typing.Type[AbstractIntegratedPropagator]
    AbstractJacobiansMapper: typing.Type[AbstractJacobiansMapper]
    AdditionalEquations: typing.Type[AdditionalEquations]
    FieldAbstractIntegratedPropagator: typing.Type[FieldAbstractIntegratedPropagator]
    FieldAdditionalEquations: typing.Type[FieldAdditionalEquations]
    FieldIntegratedEphemeris: typing.Type[FieldIntegratedEphemeris]
    FieldStateMapper: typing.Type[FieldStateMapper]
    IntegratedEphemeris: typing.Type[IntegratedEphemeris]
    PythonAbstractGradientConverter: typing.Type[PythonAbstractGradientConverter]
    PythonAbstractIntegratedPropagator: typing.Type[PythonAbstractIntegratedPropagator]
    PythonAdditionalEquations: typing.Type[PythonAdditionalEquations]
    PythonFieldAbstractIntegratedPropagator: typing.Type[PythonFieldAbstractIntegratedPropagator]
    PythonFieldAdditionalEquations: typing.Type[PythonFieldAdditionalEquations]
    StateMapper: typing.Type[StateMapper]
