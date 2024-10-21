import java.util
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.class-use
import org.orekit.propagation.analytical.gnss
import org.orekit.propagation.analytical.intelsat
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.events
import org.orekit.propagation.integration
import org.orekit.time
import org.orekit.utils
import typing



class AbstractAnalyticalGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter, org.orekit.utils.ParameterDriversProvider):
    """
    public abstract class AbstractAnalyticalGradientConverter extends :class:`~org.orekit.propagation.integration.AbstractGradientConverter` implements :class:`~org.orekit.utils.ParameterDriversProvider`
    
        Converter for analytical orbit propagator.
    
        Since:
            11.1
    """
    def getPropagator(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], gradientArray: typing.List[org.hipparchus.analysis.differentiation.Gradient]) -> 'FieldAbstractAnalyticalPropagator'[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getState(self) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]: ...
    @typing.overload
    def getState(self, parameterDriversProvider: org.orekit.utils.ParameterDriversProvider) -> org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient]: ...

class AbstractAnalyticalMatricesHarvester(org.orekit.propagation.AbstractMatricesHarvester, org.orekit.propagation.AdditionalStateProvider):
    """
    public abstract class AbstractAnalyticalMatricesHarvester extends :class:`~org.orekit.propagation.AbstractMatricesHarvester` implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    
        Base class harvester between two-dimensional Jacobian matrices and analytical orbit propagator.
    
        Since:
            11.1
    """
    def freezeColumnsNames(self) -> None:
        """
            Freeze the names of the Jacobian columns.
        
            This method is called when propagation starts, i.e. when configuration is completed
        
            Specified by:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.freezeColumnsNames` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
        
        """
        ...
    def getAdditionalState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
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
    def getGradientConverter(self) -> AbstractAnalyticalGradientConverter:
        """
            Get the gradient converter related to the analytical orbit propagator.
        
            Returns:
                the gradient converter
        
        
        """
        ...
    def getJacobiansColumnsNames(self) -> java.util.List[str]: ...
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
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type used for the matrix computation.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Returns:
                the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian with respect to propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getParametersJacobian` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.getParametersJacobian` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
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
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getPositionAngleType` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Returns:
                the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Extract state transition matrix from state.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getStateTransitionMatrix` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.getStateTransitionMatrix` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
                :class:`~org.orekit.orbits.OrbitType`.
        
        
        """
        ...
    def setReferenceState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
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
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.setReferenceState` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): reference state to set
        
        
        """
        ...

class AbstractAnalyticalPropagator(org.orekit.propagation.AbstractPropagator):
    """
    public abstract class AbstractAnalyticalPropagator extends :class:`~org.orekit.propagation.AbstractPropagator`
    
        Common handling of :class:`~org.orekit.propagation.Propagator` methods for analytical propagators.
    
        This abstract class allows to provide easily the full set of :class:`~org.orekit.propagation.Propagator` methods,
        including all propagation modes support and discrete events support for any simple propagation method. Only two methods
        must be implemented by derived classes:
        :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.propagateOrbit` and
        :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.getMass`. The first method should perform
        straightforward propagation starting from some internally stored initial state up to the specified target date.
    """
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
    def getPvProvider(self) -> org.orekit.utils.PVCoordinatesProvider:
        """
            Get PV coordinates provider.
        
            Returns:
                PV coordinates provider
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
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
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState: ...

_FieldAbstractAnalyticalPropagator__T = typing.TypeVar('_FieldAbstractAnalyticalPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractAnalyticalPropagator(org.orekit.propagation.FieldAbstractPropagator[_FieldAbstractAnalyticalPropagator__T], org.orekit.utils.ParameterDriversProvider, typing.Generic[_FieldAbstractAnalyticalPropagator__T]):
    """
    public abstract class FieldAbstractAnalyticalPropagator<T extends :class:`~org.orekit.propagation.analytical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.FieldAbstractPropagator`<T> implements :class:`~org.orekit.utils.ParameterDriversProvider`
    
        Common handling of :class:`~org.orekit.propagation.FieldPropagator` methods for analytical propagators.
    
        This abstract class allows to provide easily the full set of :class:`~org.orekit.propagation.FieldPropagator` methods,
        including all propagation modes support and discrete events support for any simple propagation method. Only two methods
        must be implemented by derived classes:
        :meth:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator.propagateOrbit` and
        :meth:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator.getMass`. The first method should perform
        straightforward propagation starting from some internally stored initial state up to the specified target date.
    """
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
    def getEphemerisGenerator(self) -> org.orekit.propagation.FieldEphemerisGenerator[_FieldAbstractAnalyticalPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_FieldAbstractAnalyticalPropagator__T]]: ...
    def getPvProvider(self) -> org.orekit.utils.FieldPVCoordinatesProvider[_FieldAbstractAnalyticalPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractAnalyticalPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractAnalyticalPropagator__T]: ...

class AdapterPropagator(AbstractAnalyticalPropagator):
    """
    public class AdapterPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        Orbit propagator that adapts an underlying propagator, adding
        :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`.
    
        This propagator is used when a reference propagator does not handle some effects that we need. A typical example would
        be an ephemeris that was computed for a reference orbit, and we want to compute a station-keeping maneuver on top of
        this ephemeris, changing its final state. The principal is to add one or more
        :class:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel` to it and use it as a new propagator, which takes the
        maneuvers into account.
    
        From a space flight dynamics point of view, this is a differential correction approach. From a computer science point of
        view, this is a use of the decorator design pattern.
    
        Also see:
            :class:`~org.orekit.propagation.Propagator`, :class:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel`
    """
    def __init__(self, propagator: org.orekit.propagation.Propagator): ...
    def addEffect(self, differentialEffect: 'AdapterPropagator.DifferentialEffect') -> None:
        """
            Add a differential effect.
        
            Parameters:
                effect (:class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`): differential effect
        
        
        """
        ...
    def getEffects(self) -> java.util.List['AdapterPropagator.DifferentialEffect']: ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Get the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Returns:
                initial state
        
        
        """
        ...
    def getPropagator(self) -> org.orekit.propagation.Propagator:
        """
            Get the reference propagator.
        
            Returns:
                reference propagator
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    class DifferentialEffect:
        def apply(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...

class AggregateBoundedPropagator(AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator):
    """
    public class AggregateBoundedPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator` implements :class:`~org.orekit.propagation.BoundedPropagator`
    
        A :class:`~org.orekit.propagation.BoundedPropagator` that covers a larger time span from several constituent propagators
        that cover shorter time spans.
    
        Since:
            9.0
    
        Also see:
            :meth:`~org.orekit.propagation.analytical.AggregateBoundedPropagator.%3Cinit%3E`
    """
    @typing.overload
    def __init__(self, collection: typing.Union[java.util.Collection[org.orekit.propagation.BoundedPropagator], typing.Sequence[org.orekit.propagation.BoundedPropagator]]): ...
    @typing.overload
    def __init__(self, navigableMap: java.util.NavigableMap[org.orekit.time.AbsoluteDate, org.orekit.propagation.BoundedPropagator], absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Description copied from class: :meth:`~org.orekit.propagation.AbstractPropagator.getInitialState`
            Get the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Returns:
                initial state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.BoundedPropagator.getMaxDate`
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
            Description copied from interface: :meth:`~org.orekit.propagation.BoundedPropagator.getMinDate`
            Get the first date of the range.
        
            Specified by:
                :meth:`~org.orekit.propagation.BoundedPropagator.getMinDate` in
                interface :class:`~org.orekit.propagation.BoundedPropagator`
        
            Returns:
                the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.Propagator.getPVCoordinates`
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
    def getPosition(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.Propagator.getPosition`
            Get the position of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getPosition` in interface :class:`~org.orekit.propagation.Propagator`
        
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
    def getPropagators(self) -> java.util.NavigableMap[org.orekit.time.AbsoluteDate, org.orekit.propagation.BoundedPropagator]: ...
    def getPropagatorsMap(self) -> org.orekit.utils.TimeSpanMap[org.orekit.propagation.BoundedPropagator]: ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Description copied from class: :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState`
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...

class BrouwerLyddanePropagator(AbstractAnalyticalPropagator, org.orekit.utils.ParameterDriversProvider):
    """
    public class BrouwerLyddanePropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator` implements :class:`~org.orekit.utils.ParameterDriversProvider`
    
        This class propagates a :class:`~org.orekit.propagation.SpacecraftState` using the analytical Brouwer-Lyddane model
        (from J2 to J5 zonal harmonics).
    
        At the opposite of the :class:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator`, the Brouwer-Lyddane model
        is suited for elliptical orbits, there is no problem having a rather small eccentricity or inclination (Lyddane helped
        to solve this issue with the Brouwer model). Singularity for the critical inclination i = 63.4° is avoided using the
        method developed in Warren Phipps' 1992 thesis.
    
        By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth
        orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992
        thesis considered the atmospheric drag by time derivatives of the *mean* mean anomaly using the catch-all coefficient
        :code:`M2Driver`. Beware that M2Driver must have only 1 span on its TimeSpanMap value. Usually, M2 is adjusted during an
        orbit determination process and it represents the combination of all unmodeled secular along-track effects (i.e. not
        just the atmospheric drag). The behavior of M2 is close to the
        :meth:`~org.orekit.propagation.analytical.tle.TLE.getBStar` parameter for the TLE. If the value of M2 is equal to
        :meth:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator.M2`, the along-track secular effects are not
        considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value
        of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/s². The along-track effects,
        represented by the secular rates of the mean semi-major axis and eccentricity, are computed following Eq. 2.38, 2.41,
        and 2.45 of Warren Phipps' thesis.
    
        Since:
            11.1
    
        Also see:
            "Brouwer, Dirk. Solution of the problem of artificial satellite theory without drag. YALE UNIV NEW HAVEN CT NEW HAVEN
            United States, 1959.", "Lyddane, R. H. Small eccentricities or inclinations in the Brouwer theory of the artificial
            satellite. The Astronomical Journal 68 (1963): 555.", "Phipps Jr, Warren E. Parallelization of the Navy Space
            Surveillance Center (NAVSPASUR) Satellite Model. NAVAL POSTGRADUATE SCHOOL MONTEREY CA, 1992.", "Solomon, Daniel, THE
            NAVSPASUR Satellite Motion Model, Naval Research Laboratory, August 8, 1991."
    """
    M2_NAME: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.analytical.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` M2_NAME
    
        Parameter name for M2 coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    M2: typing.ClassVar[float] = ...
    """
    public static final double M2
    
        Default value for M2 coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    EPSILON_DEFAULT: typing.ClassVar[float] = ...
    """
    public static final double EPSILON_DEFAULT
    
        Default convergence threshold for mean parameters conversion.
    
        Also see:
            :meth:`~constant`
    
    
    """
    MAX_ITERATIONS_DEFAULT: typing.ClassVar[int] = ...
    """
    public static final int MAX_ITERATIONS_DEFAULT
    
        Default value for maxIterations.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DAMPING_DEFAULT: typing.ClassVar[float] = ...
    """
    public static final double DAMPING_DEFAULT
    
        Default value for damping.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, propagationType: org.orekit.propagation.PropagationType, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, propagationType: org.orekit.propagation.PropagationType, double8: float, double9: float, int: int): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, propagationType: org.orekit.propagation.PropagationType, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int: int) -> org.orekit.orbits.KeplerianOrbit:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Brouwer-Lyddane sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on both the gravity field parameterized in input and the atmospheric drag represented by the :code:`m2`
            parameter.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit to convert
                referenceRadius (double): reference radius of the Earth for the potential model (m)
                mu (double): central attraction coefficient (m³/s²)
                c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
                c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
                c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
                c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
                M2Value (double): value of empirical drag coefficient in rad/s². If equal to :code:`BrouwerLyddanePropagator.M2` drag is not considered
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Brouwer-Lyddane sense
        
            Since:
                11.2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float) -> org.orekit.orbits.KeplerianOrbit:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Brouwer-Lyddane sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on both the gravity field parameterized in input and the atmospheric drag represented by the :code:`m2`
            parameter.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
                M2Value (double): value of empirical drag coefficient in rad/s². If equal to :code:`BrouwerLyddanePropagator.M2` drag is not considered
        
            Returns:
                mean orbit in a Brouwer-Lyddane sense
        
            Since:
                11.2
        
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Brouwer-Lyddane sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on both the gravity field parameterized in input and the atmospheric drag represented by the :code:`m2`
            parameter.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
                M2Value (double): value of empirical drag coefficient in rad/s². If equal to :code:`BrouwerLyddanePropagator.M2` drag is not considered
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Brouwer-Lyddane sense
        
            Since:
                11.2
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float, double2: float, int: int) -> org.orekit.orbits.KeplerianOrbit: ...
    def getCk0(self) -> typing.List[float]:
        """
            Get the un-normalized zonal coefficients.
        
            Returns:
                the un-normalized zonal coefficients
        
        
        """
        ...
    def getM2(self) -> float:
        """
            Get the value of the M2 drag parameter. Beware that M2Driver must have only 1 span on its TimeSpanMap value (that is to
            say setPeriod method should not be called)
        
            Returns:
                the value of the M2 drag parameter
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient μ.
        
            Returns:
                mu central attraction coefficient (m³/s²)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getReferenceRadius(self) -> float:
        """
            Get the reference radius of the central body attraction model.
        
            Returns:
                the reference radius in meters
        
        
        """
        ...
    def propagateOrbit(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.KeplerianOrbit:
        """
            Extrapolate an orbit up to a specific target date.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.propagateOrbit` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date for the orbit
        
            Returns:
                extrapolated parameters
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            The new initial state to consider must be defined with an osculating orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator.resetInitialState`
        
            Reset the propagator initial state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
                stateType (:class:`~org.orekit.propagation.PropagationType`): mean Brouwer-Lyddane orbit or osculating orbit
        
            Reset the propagator initial state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
                stateType (:class:`~org.orekit.propagation.PropagationType`): mean Brouwer-Lyddane orbit or osculating orbit
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Since:
                11.2
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType, double: float, int: int) -> None: ...

class EcksteinHechlerPropagator(AbstractAnalyticalPropagator):
    """
    public class EcksteinHechlerPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        This class propagates a :class:`~org.orekit.propagation.SpacecraftState` using the analytical Eckstein-Hechler model.
    
        The Eckstein-Hechler model is suited for near circular orbits (e < 0.1, with poor accuracy between 0.005 and 0.1) and
        inclination neither equatorial (direct or retrograde) nor critical (direct or retrograde).
    
        Note that before version 7.0, there was a large inconsistency in the generated orbits, and it was fixed as of version
        7.0 of Orekit, with a visible side effect. The problems is that if the circular parameters produced by the
        Eckstein-Hechler model are used to build an orbit considered to be osculating, the velocity deduced from this orbit was
        *inconsistent with the position evolution*! The reason is that the model includes non-Keplerian effects but it does not
        include a corresponding circular/Cartesian conversion. As a consequence, all subsequent computation involving velocity
        were wrong. This includes attitude modes like yaw compensation and Doppler effect. As this effect was considered serious
        enough and as accurate velocities were considered important, the propagator now generates
        :class:`~org.orekit.orbits.CartesianOrbit` which are built in a special way to ensure consistency throughout
        propagation. A side effect is that if circular parameters are rebuilt by user from these propagated Cartesian orbit, the
        circular parameters will generally *not* match the initial orbit (differences in semi-major axis can exceed 120 m). The
        position however *will* match to sub-micrometer level, and this position will be identical to the positions that were
        generated by previous versions (in other words, the internals of the models have not been changed, only the output
        parameters have been changed). The correctness of the initialization has been assessed and is good, as it allows the
        subsequent orbit to remain close to a numerical reference orbit.
    
        If users need a more definitive initialization of an Eckstein-Hechler propagator, they should consider using a
        :class:`~org.orekit.propagation.conversion.PropagatorConverter` to initialize their Eckstein-Hechler propagator using a
        complete sample instead of just a single initial orbit.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, propagationType: org.orekit.propagation.PropagationType, double9: float, int: int): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int: int) -> org.orekit.orbits.CircularOrbit:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Eckstein-Hechler sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on the gravity field parameterized in input.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit to convert
                referenceRadius (double): reference radius of the Earth for the potential model (m)
                mu (double): central attraction coefficient (m³/s²)
                c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
                c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
                c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
                c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
                c60 (double): un-normalized zonal coefficient (about -5.41e-7 for Earth)
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Eckstein-Hechler sense
        
            Since:
                11.2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics) -> org.orekit.orbits.CircularOrbit:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Eckstein-Hechler sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on the gravity field parameterized in input.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
        
            Returns:
                mean orbit in a Eckstein-Hechler sense
        
            Since:
                11.2
        
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Eckstein-Hechler sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on the gravity field parameterized in input.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.Orbit`): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Eckstein-Hechler sense
        
            Since:
                11.2
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float, int: int) -> org.orekit.orbits.CircularOrbit: ...
    def getCk0(self) -> typing.List[float]:
        """
            Get the un-normalized zonal coefficients.
        
            Returns:
                the un-normalized zonal coefficients
        
            Since:
                11.1
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient μ.
        
            Returns:
                mu central attraction coefficient (m³/s²)
        
            Since:
                11.1
        
        
        """
        ...
    def getReferenceRadius(self) -> float:
        """
            Get the reference radius of the central body attraction model.
        
            Returns:
                the reference radius in meters
        
            Since:
                11.1
        
        
        """
        ...
    def propagateOrbit(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.CartesianOrbit:
        """
            Extrapolate an orbit up to a specific target date.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.propagateOrbit` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date for the orbit
        
            Returns:
                extrapolated parameters
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            The new initial state to consider must be defined with an osculating orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator.resetInitialState`
        
            Reset the propagator initial state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
                stateType (:class:`~org.orekit.propagation.PropagationType`): mean Eckstein-Hechler orbit or osculating orbit
        
            Since:
                10.2
        
            Reset the propagator initial state.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
                stateType (:class:`~org.orekit.propagation.PropagationType`): mean Eckstein-Hechler orbit or osculating orbit
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Since:
                11.2
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType, double: float, int: int) -> None: ...

class Ephemeris(AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator):
    """
    public class Ephemeris extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator` implements :class:`~org.orekit.propagation.BoundedPropagator`
    
        This class is designed to accept and handle tabulated orbital entries. Tabulated entries are classified and then
        extrapolated in way to obtain continuous output, with accuracy and computation methods configured by the user.
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], int: int): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def basicPropagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
            Propagate an orbit without any fancy features.
        
            This method is similar in spirit to the
            :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.propagate` method, except that it does **not**
            call any handler during propagation, nor any discrete events, not additional states. It always stop exactly at the
            specified date.
        
            Overrides:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.basicPropagate` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date for propagation
        
            Returns:
                state at specified date
        
        
        """
        ...
    @staticmethod
    def checkInputConsistency(list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]) -> None: ...
    @staticmethod
    def checkStatesAndCovariancesConsistency(list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance]) -> None: ...
    def getCovariance(self, absoluteDate: org.orekit.time.AbsoluteDate) -> java.util.Optional[org.orekit.propagation.StateCovariance]: ...
    def getCovarianceInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.getFrame` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getFrame` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
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
                :meth:`~org.orekit.propagation.AbstractPropagator.getInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
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
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getManagedAdditionalStates` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
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
    def getStateInterpolator(self) -> org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState]: ...
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
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.isAdditionalStateManaged` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                name (:class:`~org.orekit.propagation.analytical.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the additional state
        
            Returns:
                true if the additional state is managed
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Try (and fail) to reset the initial state.
        
            This method always throws an exception, as ephemerides cannot be reset.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...

_FieldBrouwerLyddanePropagator__T = typing.TypeVar('_FieldBrouwerLyddanePropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBrouwerLyddanePropagator(FieldAbstractAnalyticalPropagator[_FieldBrouwerLyddanePropagator__T], typing.Generic[_FieldBrouwerLyddanePropagator__T]):
    """
    public class FieldBrouwerLyddanePropagator<T extends :class:`~org.orekit.propagation.analytical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T>
    
        This class propagates a :class:`~org.orekit.propagation.FieldSpacecraftState` using the analytical Brouwer-Lyddane model
        (from J2 to J5 zonal harmonics).
    
        At the opposite of the :class:`~org.orekit.propagation.analytical.FieldEcksteinHechlerPropagator`, the Brouwer-Lyddane
        model is suited for elliptical orbits, there is no problem having a rather small eccentricity or inclination (Lyddane
        helped to solve this issue with the Brouwer model). Singularity for the critical inclination i = 63.4° is avoided using
        the method developed in Warren Phipps' 1992 thesis.
    
        By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth
        orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992
        thesis considered the atmospheric drag by time derivatives of the *mean* mean anomaly using the catch-all coefficient
        :code:`M2Driver`. Usually, M2 is adjusted during an orbit determination process and it represents the combination of all
        unmodeled secular along-track effects (i.e. not just the atmospheric drag). The behavior of M2 is close to the
        :meth:`~org.orekit.propagation.analytical.tle.FieldTLE.getBStar` parameter for the TLE. If the value of M2 is equal to
        :meth:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator.M2`, the along-track secular effects are not
        considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value
        of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/s². The along-track effects,
        represented by the secular rates of the mean semi-major axis and eccentricity, are computed following Eq. 2.38, 2.41,
        and 2.45 of Warren Phipps' thesis.
    
        Since:
            11.1
    
        Also see:
            "Brouwer, Dirk. Solution of the problem of artificial satellite theory without drag. YALE UNIV NEW HAVEN CT NEW HAVEN
            United States, 1959.", "Lyddane, R. H. Small eccentricities or inclinations in the Brouwer theory of the artificial
            satellite. The Astronomical Journal 68 (1963): 555.", "Phipps Jr, Warren E. Parallelization of the Navy Space
            Surveillance Center (NAVSPASUR) Satellite Model. NAVAL POSTGRADUATE SCHOOL MONTEREY CA, 1992.", "Solomon, Daniel, THE
            NAVSPASUR Satellite Motion Model, Naval Research Laboratory, August 8, 1991."
    """
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], double: float, t: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], t: _FieldBrouwerLyddanePropagator__T, double: float, t2: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, t: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, double: float, t2: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, double: float, t2: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, propagationType: org.orekit.propagation.PropagationType, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, double: float, t2: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, propagationType: org.orekit.propagation.PropagationType, double6: float, double7: float, int: int): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    _computeMeanOrbit_0__T = typing.TypeVar('_computeMeanOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_1__T = typing.TypeVar('_computeMeanOrbit_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_2__T = typing.TypeVar('_computeMeanOrbit_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanOrbit(fieldOrbit: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_0__T], double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int: int) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_0__T]:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Brouwer-Lyddane sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on both the gravity field parameterized in input and the atmospheric drag represented by the :code:`m2`
            parameter.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit to convert
                referenceRadius (double): reference radius of the Earth for the potential model (m)
                mu (double): central attraction coefficient (m³/s²)
                c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
                c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
                c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
                c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
                M2Value (double): value of empirical drag coefficient in rad/s². If equal to :code:`BrouwerLyddanePropagator.M2` drag is not considered
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Brouwer-Lyddane sense
        
            Since:
                11.2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(fieldOrbit: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_1__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_1__T]:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Brouwer-Lyddane sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on both the gravity field parameterized in input and the atmospheric drag represented by the :code:`m2`
            parameter.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
                M2Value (double): value of empirical drag coefficient in rad/s². If equal to :code:`BrouwerLyddanePropagator.M2` drag is not considered
        
            Returns:
                mean orbit in a Brouwer-Lyddane sense
        
            Since:
                11.2
        
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Brouwer-Lyddane sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on both the gravity field parameterized in input and the atmospheric drag represented by the :code:`m2`
            parameter.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
                M2Value (double): value of empirical drag coefficient in rad/s². If equal to :code:`BrouwerLyddanePropagator.M2` drag is not considered
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Brouwer-Lyddane sense
        
            Since:
                11.2
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(fieldOrbit: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_2__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float, double2: float, int: int) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_2__T]: ...
    @typing.overload
    def getM2(self) -> float:
        """
            Get the value of the M2 drag parameter.
        
            Returns:
                the value of the M2 drag parameter
        
        """
        ...
    @typing.overload
    def getM2(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the value of the M2 drag parameter.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the model parameters want to be known
        
            Returns:
                the value of the M2 drag parameter
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def propagateOrbit(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldBrouwerLyddanePropagator__T], tArray: typing.List[_FieldBrouwerLyddanePropagator__T]) -> org.orekit.orbits.FieldKeplerianOrbit[_FieldBrouwerLyddanePropagator__T]: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T], propagationType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T], propagationType: org.orekit.propagation.PropagationType, double: float, int: int) -> None: ...

_FieldEcksteinHechlerPropagator__T = typing.TypeVar('_FieldEcksteinHechlerPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEcksteinHechlerPropagator(FieldAbstractAnalyticalPropagator[_FieldEcksteinHechlerPropagator__T], typing.Generic[_FieldEcksteinHechlerPropagator__T]):
    """
    public class FieldEcksteinHechlerPropagator<T extends :class:`~org.orekit.propagation.analytical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T>
    
        This class propagates a :class:`~org.orekit.propagation.FieldSpacecraftState` using the analytical Eckstein-Hechler
        model.
    
        The Eckstein-Hechler model is suited for near circular orbits (e < 0.1, with poor accuracy between 0.005 and 0.1) and
        inclination neither equatorial (direct or retrograde) nor critical (direct or retrograde).
    
        Also see:
            :class:`~org.orekit.orbits.FieldOrbit`
    """
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], double: float, t: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], t: _FieldEcksteinHechlerPropagator__T, double: float, t2: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, t: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, double: float, t2: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, double: float, t2: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, double: float, t2: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float, propagationType: org.orekit.propagation.PropagationType, double7: float, int: int): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    _computeMeanOrbit_0__T = typing.TypeVar('_computeMeanOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_1__T = typing.TypeVar('_computeMeanOrbit_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_2__T = typing.TypeVar('_computeMeanOrbit_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanOrbit(fieldOrbit: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_0__T], double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, int: int) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_0__T]:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Eckstein-Hechler sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on the gravity field parameterized in input.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit to convert
                referenceRadius (double): reference radius of the Earth for the potential model (m)
                mu (double): central attraction coefficient (m³/s²)
                c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
                c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
                c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
                c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
                c60 (double): un-normalized zonal coefficient (about -5.41e-7 for Earth)
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Eckstein-Hechler sense
        
            Since:
                11.2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(fieldOrbit: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_1__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_1__T]:
        """
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Eckstein-Hechler sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on the gravity field parameterized in input.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
        
            Returns:
                mean orbit in a Eckstein-Hechler sense
        
            Since:
                11.2
        
            Conversion from osculating to mean orbit.
        
            Compute mean orbit **in a Eckstein-Hechler sense**, corresponding to the osculating SpacecraftState in input.
        
            Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will
            depend on the gravity field parameterized in input.
        
            The computation is done through a fixed-point iteration process.
        
            Parameters:
                osculating (:class:`~org.orekit.orbits.FieldOrbit`<T> osculating): osculating orbit to convert
                provider (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider`): for un-normalized zonal coefficients
                harmonics (:class:`~org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics`): :code:`provider.onDate(osculating.getDate())`
                epsilon (double): convergence threshold for mean parameters conversion
                maxIterations (int): maximum iterations for mean parameters conversion
        
            Returns:
                mean orbit in a Eckstein-Hechler sense
        
            Since:
                11.2
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(fieldOrbit: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_2__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float, int: int) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_2__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def propagateOrbit(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldEcksteinHechlerPropagator__T], tArray: typing.List[_FieldEcksteinHechlerPropagator__T]) -> org.orekit.orbits.FieldCartesianOrbit[_FieldEcksteinHechlerPropagator__T]: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T], propagationType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T], propagationType: org.orekit.propagation.PropagationType, double: float, int: int) -> None: ...

_FieldKeplerianPropagator__T = typing.TypeVar('_FieldKeplerianPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldKeplerianPropagator(FieldAbstractAnalyticalPropagator[_FieldKeplerianPropagator__T], typing.Generic[_FieldKeplerianPropagator__T]):
    """
    public class FieldKeplerianPropagator<T extends :class:`~org.orekit.propagation.analytical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T>
    
        Simple Keplerian orbit propagator.
    
        Also see:
            :class:`~org.orekit.orbits.FieldOrbit`
    """
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], t: _FieldKeplerianPropagator__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldKeplerianPropagator__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldKeplerianPropagator__T, t2: _FieldKeplerianPropagator__T): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldKeplerianPropagator__T]) -> None: ...

class KeplerianPropagator(AbstractAnalyticalPropagator):
    """
    public class KeplerianPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        Simple Keplerian orbit propagator.
    
        Also see:
            :class:`~org.orekit.orbits.Orbit`
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float): ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...

class PythonAbstractAnalyticalGradientConverter(AbstractAnalyticalGradientConverter):
    """
    public class PythonAbstractAnalyticalGradientConverter extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalGradientConverter`
    """
    def __init__(self, abstractAnalyticalPropagator: AbstractAnalyticalPropagator, double: float, int: int): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPropagator(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[org.hipparchus.analysis.differentiation.Gradient], gradientArray: typing.List[org.hipparchus.analysis.differentiation.Gradient]) -> FieldAbstractAnalyticalPropagator[org.hipparchus.analysis.differentiation.Gradient]: ...
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

class PythonAbstractAnalyticalMatricesHarvester(AbstractAnalyticalMatricesHarvester):
    """
    public class PythonAbstractAnalyticalMatricesHarvester extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalMatricesHarvester`
    """
    def __init__(self, abstractAnalyticalPropagator: AbstractAnalyticalPropagator, string: str, realMatrix: org.hipparchus.linear.RealMatrix, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary): ...
    def finalize(self) -> None: ...
    def getGradientConverter(self) -> AbstractAnalyticalGradientConverter:
        """
            Get the gradient converter related to the analytical orbit propagator.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalMatricesHarvester.getGradientConverter` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalMatricesHarvester`
        
            Returns:
                the gradient converter
        
        
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

class PythonAbstractAnalyticalPropagator(AbstractAnalyticalPropagator):
    """
    public class PythonAbstractAnalyticalPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    """
    def __init__(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def finalize(self) -> None: ...
    def getMass(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the mass. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.getMass` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date for the orbit
        
            Returns:
                mass mass
        
        
        """
        ...
    def propagateOrbit(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
            Extrapolate an orbit up to a specific target date. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.propagateOrbit` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date for the orbit
        
            Returns:
                extrapolated parameters
        
        
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
    def resetIntermediateState(self, spacecraftState: org.orekit.propagation.SpacecraftState, boolean: bool) -> None:
        """
            Reset an intermediate state. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.resetIntermediateState` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new intermediate state to consider
                forward (boolean): if true, the intermediate state is valid for
        
        
        """
        ...

_PythonFieldAbstractAnalyticalPropagator__T = typing.TypeVar('_PythonFieldAbstractAnalyticalPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractAnalyticalPropagator(FieldAbstractAnalyticalPropagator[_PythonFieldAbstractAnalyticalPropagator__T], typing.Generic[_PythonFieldAbstractAnalyticalPropagator__T]):
    """
    public class PythonFieldAbstractAnalyticalPropagator<T extends :class:`~org.orekit.propagation.analytical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T>
    """
    def __init__(self, field: org.hipparchus.Field[_PythonFieldAbstractAnalyticalPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def finalize(self) -> None: ...
    def getMass(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractAnalyticalPropagator__T]) -> _PythonFieldAbstractAnalyticalPropagator__T: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def propagateOrbit(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractAnalyticalPropagator__T], tArray: typing.List[_PythonFieldAbstractAnalyticalPropagator__T]) -> org.orekit.orbits.FieldOrbit[_PythonFieldAbstractAnalyticalPropagator__T]: ...
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
    def resetIntermediateState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAbstractAnalyticalPropagator__T], boolean: bool) -> None: ...

class J2DifferentialEffect(AdapterPropagator.DifferentialEffect):
    """
    public class J2DifferentialEffect extends :class:`~org.orekit.propagation.analytical.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`
    
        Analytical model for J2 effect.
    
        This class computes the differential effect of J2 due to an initial orbit offset. A typical case is when an inclination
        maneuver changes an orbit inclination at time t₀. As ascending node drift rate depends on inclination, the change
        induces a time-dependent change in ascending node for later dates.
    
        Also see:
            :class:`~org.orekit.forces.maneuvers.SmallManeuverAnalyticalModel`
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit, boolean: bool, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit, boolean: bool, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, differentialEffect: AdapterPropagator.DifferentialEffect, boolean: bool, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, differentialEffect: AdapterPropagator.DifferentialEffect, boolean: bool, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def apply(self, orbit: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
            Compute the effect of the maneuver on an orbit.
        
            Parameters:
                orbit1 (:class:`~org.orekit.orbits.Orbit`): original orbit at t₁, without maneuver
        
            Returns:
                orbit at t₁, taking the maneuver into account if t₁ > t₀
        
            Also see:
                :meth:`~org.orekit.propagation.analytical.J2DifferentialEffect.apply`
        
            Apply the effect to a :class:`~org.orekit.propagation.SpacecraftState`.
        
            Applying the effect may be a no-op in some cases. A typical example is maneuvers, for which the state is changed only
            for time *after* the maneuver occurrence.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect.apply` in
                interface :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`
        
            Parameters:
                state1 (:class:`~org.orekit.propagation.SpacecraftState`): original state *without* the effect
        
            Returns:
                updated state at the same date, taking the effect into account if meaningful
        
        
        """
        ...
    @typing.overload
    def apply(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...

class PythonDifferentialEffect(AdapterPropagator.DifferentialEffect):
    """
    public class PythonDifferentialEffect extends :class:`~org.orekit.propagation.analytical.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`
    """
    def __init__(self): ...
    def apply(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Apply the effect to a :class:`~org.orekit.propagation.SpacecraftState`.
        
            Applying the effect may be a no-op in some cases. A typical example is maneuvers, for which the state is changed only
            for time *after* the maneuver occurrence.
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect.apply` in
                interface :class:`~org.orekit.propagation.analytical.AdapterPropagator.DifferentialEffect`
        
            Parameters:
                original (:class:`~org.orekit.propagation.SpacecraftState`): original state *without* the effect
        
            Returns:
                updated state at the same date, taking the effect into account if meaningful
        
        
        """
        ...
    def finalize(self) -> None: ...
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical")``.

    AbstractAnalyticalGradientConverter: typing.Type[AbstractAnalyticalGradientConverter]
    AbstractAnalyticalMatricesHarvester: typing.Type[AbstractAnalyticalMatricesHarvester]
    AbstractAnalyticalPropagator: typing.Type[AbstractAnalyticalPropagator]
    AdapterPropagator: typing.Type[AdapterPropagator]
    AggregateBoundedPropagator: typing.Type[AggregateBoundedPropagator]
    BrouwerLyddanePropagator: typing.Type[BrouwerLyddanePropagator]
    EcksteinHechlerPropagator: typing.Type[EcksteinHechlerPropagator]
    Ephemeris: typing.Type[Ephemeris]
    FieldAbstractAnalyticalPropagator: typing.Type[FieldAbstractAnalyticalPropagator]
    FieldBrouwerLyddanePropagator: typing.Type[FieldBrouwerLyddanePropagator]
    FieldEcksteinHechlerPropagator: typing.Type[FieldEcksteinHechlerPropagator]
    FieldKeplerianPropagator: typing.Type[FieldKeplerianPropagator]
    J2DifferentialEffect: typing.Type[J2DifferentialEffect]
    KeplerianPropagator: typing.Type[KeplerianPropagator]
    PythonAbstractAnalyticalGradientConverter: typing.Type[PythonAbstractAnalyticalGradientConverter]
    PythonAbstractAnalyticalMatricesHarvester: typing.Type[PythonAbstractAnalyticalMatricesHarvester]
    PythonAbstractAnalyticalPropagator: typing.Type[PythonAbstractAnalyticalPropagator]
    PythonDifferentialEffect: typing.Type[PythonDifferentialEffect]
    PythonFieldAbstractAnalyticalPropagator: typing.Type[PythonFieldAbstractAnalyticalPropagator]
    class-use: org.orekit.propagation.analytical.class-use.__module_protocol__
    gnss: org.orekit.propagation.analytical.gnss.__module_protocol__
    intelsat: org.orekit.propagation.analytical.intelsat.__module_protocol__
    tle: org.orekit.propagation.analytical.tle.__module_protocol__
