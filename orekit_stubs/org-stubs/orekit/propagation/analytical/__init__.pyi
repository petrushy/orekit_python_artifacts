
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
import org.hipparchus.linear
import org.orekit.attitudes
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.gnss
import org.orekit.propagation.analytical.intelsat
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.conversion.osc2mean
import org.orekit.propagation.events
import org.orekit.propagation.integration
import org.orekit.time
import org.orekit.utils
import typing



class AbstractAnalyticalGradientConverter(org.orekit.propagation.integration.AbstractGradientConverter, org.orekit.utils.ParameterDriversProvider):
    """
    Converter for analytical orbit propagator.
    
    Since:
        11.1
    """
    def getPropagator(self) -> 'FieldAbstractAnalyticalPropagator'[org.hipparchus.analysis.differentiation.Gradient]:
        """
        Get the converted analytical orbit propagator.
        
        Returns:
            the converted analytical orbit propagator
        
        
        """
        ...

class AbstractAnalyticalMatricesHarvester(org.orekit.propagation.AbstractMatricesHarvester, org.orekit.propagation.AdditionalDataProvider[typing.MutableSequence[float]]):
    """
    Base class harvester between two-dimensional Jacobian matrices and analytical orbit propagator.
    
    Since:
        11.1
    """
    def freezeColumnsNames(self) -> None:
        """
        Freeze the names of the Jacobian columns.
        
        This method is called when propagation starts, i.e. when configuration is completed
        
        Specified by: freezeColumnsNames in class AbstractMatricesHarvester
        
        
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
    def getGradientConverter(self) -> AbstractAnalyticalGradientConverter:
        """
        Get the gradient converter related to the analytical orbit propagator.
        
        Returns:
            the gradient converter
        
        
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
    def getName(self) -> str:
        """
        Get the name of the additional data.
        
        If a provider just modifies one of the basic elements (orbit, attitude or mass) without adding any new data, it should return the empty string as its name.
        
        Specified by: getName in interface AdditionalDataProvider
        
        Returns:
            name of the additional data (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get the orbit type used for the matrix computation.
        
        Specified by: getOrbitType in interface MatricesHarvester
        
        Returns:
            the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian with respect to propagation parameters.
        
        Specified by: getParametersJacobian in interface MatricesHarvester
        
        Overrides: getParametersJacobian in class AbstractMatricesHarvester
        
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
        
        Specified by: getPositionAngleType in interface MatricesHarvester
        
        Returns:
            the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Extract state transition matrix from state.
        
        Specified by: getStateTransitionMatrix in interface MatricesHarvester
        
        Overrides: getStateTransitionMatrix in class AbstractMatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
            OrbitType.
        
        
        """
        ...
    def setReferenceState(self, reference: org.orekit.propagation.SpacecraftState) -> None:
        """
        Set up reference state.
        
        This method is called whenever the global propagation reference state changes. This corresponds to the start of propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering. Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not use it at all.
        
        Specified by: setReferenceState in interface MatricesHarvester
        
        Overrides: setReferenceState in class AbstractMatricesHarvester
        
        Parameters:
            reference (SpacecraftState): reference state to set
        
        
        """
        ...

class AbstractAnalyticalPropagator(org.orekit.propagation.AbstractPropagator):
    """
    Common handling of Propagator methods for analytical propagators.
    
    This abstract class allows to provide easily the full set of Propagator methods, including all propagation modes support and discrete events support for any simple propagation method. Only two methods must be implemented by derived classes: propagateOrbit and getMass. The first method should perform straightforward propagation starting from some internally stored initial state up to the specified target date.
    """
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
    def basicPropagate(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Propagate an orbit without any fancy features.
        
        This method is similar in spirit to the propagate method, except that it does not call any handler during propagation, nor any discrete events, not additional states. It always stops exactly at the specified date.
        
        Parameters:
            date (AbsoluteDate): target date for propagation
        
        Returns:
            state at specified date
        
        
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
    def clearMatricesComputation(self) -> None:
        """
        Description copied from class: clearMatricesComputation Erases the internal matrices harvester.
        
        Overrides: clearMatricesComputation in class AbstractPropagator
        
        
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
        
        Those propagators use a start date and a target date to compute the propagated state. For propagators using event detection mechanism, if the provided start date is different from the initial state date, a first, simple propagation is performed, without processing any event computation. Then complete propagation is performed from start date to target date.
        
        Parameters:
            start (AbsoluteDate): start date from which orbit state should be propagated
            target (AbsoluteDate): target date to which orbit state should be propagated
        
        Returns:
            propagated state
        
        
        """
        ...
    @typing.overload
    def propagate(self, start: org.orekit.time.AbsoluteDate, target: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState: ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Extrapolate an orbit up to a specific target date.
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...

_FieldAbstractAnalyticalPropagator__T = typing.TypeVar('_FieldAbstractAnalyticalPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractAnalyticalPropagator(org.orekit.propagation.FieldAbstractPropagator[_FieldAbstractAnalyticalPropagator__T], org.orekit.utils.ParameterDriversProvider, typing.Generic[_FieldAbstractAnalyticalPropagator__T]):
    """
    Common handling of FieldPropagator methods for analytical propagators.
    
    This abstract class allows to provide easily the full set of FieldPropagator methods, including all propagation modes support and discrete events support for any simple propagation method. Only two methods must be implemented by derived classes: propagateOrbit and getMass. The first method should perform straightforward propagation starting from some internally stored initial state up to the specified target date.
    """
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
    def basicPropagate(self, date: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractAnalyticalPropagator__T]:
        """
        Propagate an orbit without any fancy features.
        
        This method is similar in spirit to the propagate method, except that it does not call any handler during propagation, nor any discrete events, not additional states. It always stop exactly at the specified date.
        
        Parameters:
            date (FieldAbsoluteDate<FieldAbstractAnalyticalPropagator> date): target date for propagation
        
        Returns:
            state at specified date
        
        
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
    def getEphemerisGenerator(self) -> org.orekit.propagation.FieldEphemerisGenerator[_FieldAbstractAnalyticalPropagator__T]:
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
    def getEventDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_FieldAbstractAnalyticalPropagator__T]]:
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
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractAnalyticalPropagator__T]: ...
    @typing.overload
    def propagate(self, start: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T], target: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T]) -> org.orekit.propagation.FieldSpacecraftState[_FieldAbstractAnalyticalPropagator__T]: ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldAbstractAnalyticalPropagator__T], parameters: typing.Union[typing.List[_FieldAbstractAnalyticalPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_FieldAbstractAnalyticalPropagator__T]:
        """
        Propagate an orbit up to a specific target date.
        
        Parameters:
            date (FieldAbsoluteDate<FieldAbstractAnalyticalPropagator> date): target date for the orbit
            parameters (FieldAbstractAnalyticalPropagator[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...

class AdapterPropagator(AbstractAnalyticalPropagator):
    """
    Orbit propagator that adapts an underlying propagator, adding DifferentialEffect.
    
    This propagator is used when a reference propagator does not handle some effects that we need. A typical example would be an ephemeris that was computed for a reference orbit, and we want to compute a station-keeping maneuver on top of this ephemeris, changing its final state. The principal is to add one or more SmallManeuverAnalyticalModel to it and use it as a new propagator, which takes the maneuvers into account.
    
    From a space flight dynamics point of view, this is a differential correction approach. From a computer science point of view, this is a use of the decorator design pattern.
    
    Also see:
        Propagator, SmallManeuverAnalyticalModel
    """
    def __init__(self, reference: org.orekit.propagation.Propagator):
        """
        Build a propagator from an underlying reference propagator.
        
        The reference propagator can be almost anything, numerical, analytical, and even an ephemeris. It may already take some maneuvers into account.
        
        Parameters:
            reference (Propagator): reference propagator
        
        
        """
        ...
    def addEffect(self, effect: typing.Union['AdapterPropagator.DifferentialEffect', typing.Callable]) -> None:
        """
        Add a differential effect.
        
        Parameters:
            effect (DifferentialEffect): differential effect
        
        
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
    def getEffects(self) -> java.util.List['AdapterPropagator.DifferentialEffect']:
        """
        Get the differential effects.
        
        Returns:
            differential effects models, as an unmodifiable list
        
        
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
    def getPropagator(self) -> org.orekit.propagation.Propagator:
        """
        Get the reference propagator.
        
        Returns:
            reference propagator
        
        
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
    class DifferentialEffect:
        def apply(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...

class AggregateBoundedPropagator(AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator):
    """
    A BoundedPropagator that covers a larger time span from several constituent propagators that cover shorter time spans.
    
    Since:
        9.0
    """
    @typing.overload
    def __init__(self, propagators: typing.Union[java.util.Collection[org.orekit.propagation.BoundedPropagator], typing.Sequence[org.orekit.propagation.BoundedPropagator], typing.Set[org.orekit.propagation.BoundedPropagator]]): ...
    @typing.overload
    def __init__(self, propagators: java.util.NavigableMap[org.orekit.time.AbsoluteDate, org.orekit.propagation.BoundedPropagator], min: org.orekit.time.AbsoluteDate, max: org.orekit.time.AbsoluteDate): ...
    def basicPropagate(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Description copied from class: basicPropagate Propagate an orbit without any fancy features.
        
        This method is similar in spirit to the propagate method, except that it does not call any handler during propagation, nor any discrete events, not additional states. It always stops exactly at the specified date.
        
        Overrides: basicPropagate in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for propagation
        
        Returns:
            state at specified date
        
        
        """
        ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
        Description copied from class: getInitialState Get the propagator initial state.
        
        Specified by: getInitialState in interface Propagator
        
        Overrides: getInitialState in class AbstractPropagator
        
        Returns:
            initial state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMaxDate Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMinDate Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedPVCoordinatesProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Description copied from interface: getPVCoordinates Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface Propagator
        
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
        Description copied from interface: getPosition Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface Propagator
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        
        """
        ...
    def getPropagatorsMap(self) -> org.orekit.utils.TimeSpanMap[org.orekit.propagation.BoundedPropagator]:
        """
        Get the propagators map.
        
        Returns:
            propagators map
        
        Since:
            12.1
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Description copied from class: propagateOrbit Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from class: resetInitialState Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...

class BrouwerLyddanePropagator(AbstractAnalyticalPropagator, org.orekit.utils.ParameterDriversProvider):
    """
    This class propagates a SpacecraftState using the analytical Brouwer-Lyddane model (from J2 to J5 zonal harmonics).
    
    At the opposite of the EcksteinHechlerPropagator, the Brouwer-Lyddane model is suited for elliptical orbits, there is no problem having a rather small eccentricity or inclination (Lyddane helped to solve this issue with the Brouwer model). Singularity for the critical inclination i = 63.4° is avoided using the method developed in Warren Phipps' 1992 thesis.
    
    By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992 thesis considered the atmospheric drag by time derivatives of the mean mean anomaly using the catch-all coefficient M2Driver. Beware that M2Driver must have only 1 span on its TimeSpanMap value. Usually, M2 is adjusted during an orbit determination process and it represents the combination of all unmodeled secular along-track effects (i.e. not just the atmospheric drag). The behavior of M2 is close to the getBStar parameter for the TLE. If the value of M2 is equal to M2, the along-track secular effects are not considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/s². The along-track effects, represented by the secular rates of the mean semi-major axis and eccentricity, are computed following Eq. 2.38, 2.41, and 2.45 of Warren Phipps' thesis.
    
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
    Parameter name for M2 coefficient.
    
    Also see:
        constant
    
    
    """
    M2: typing.ClassVar[float] = ...
    """
    Default value for M2 coefficient.
    
    Also see:
        constant
    
    
    """
    EPSILON_DEFAULT: typing.ClassVar[float] = ...
    """
    Default convergence threshold for mean parameters conversion.
    
    Also see:
        constant
    
    
    """
    MAX_ITERATIONS_DEFAULT: typing.ClassVar[int] = ...
    """
    Default value for maxIterations.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, m2Value: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, m2Value: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, initialType: org.orekit.propagation.PropagationType, m2Value: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, initialType: org.orekit.propagation.PropagationType, m2Value: float, epsilon: float, maxIterations: int): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, initialType: org.orekit.propagation.PropagationType, m2Value: float, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, m2Value: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, initialType: org.orekit.propagation.PropagationType, m2Value: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, m2Value: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, m2Value: float, epsilon: float, maxIterations: int) -> org.orekit.orbits.KeplerianOrbit:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2Value parameter.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            referenceRadius (double): reference radius of the Earth for the potential model (m)
            mu (double): central attraction coefficient (m³/s²)
            c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
            c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
            c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
            c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to
                M2 drag is not considered
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
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, m2Value: float, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.orbits.KeplerianOrbit:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2Value parameter.
        
        The computation is done through the given osculating to mean orbit converter.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            referenceRadius (double): reference radius of the Earth for the potential model (m)
            mu (double): central attraction coefficient (m³/s²)
            c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
            c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
            c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
            c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to
                M2 drag is not considered
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Returns:
            mean orbit in a Brouwer-Lyddane sense
        
        Since:
            13.0
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: float, m2Value: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.orbits.KeplerianOrbit:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2Value parameter.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to
                M2 drag is not considered
        
        Returns:
            mean orbit in a Brouwer-Lyddane sense
        
        Since:
            11.2
        
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2Value parameter.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to
                M2 drag is not considered
            epsilon (double): convergence threshold for mean parameters conversion
            maxIterations (int): maximum iterations for mean parameters conversion
        
        Returns:
            mean orbit in a Brouwer-Lyddane sense
        
        Since:
            11.2
        
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2Value parameter.
        
        The computation is done through the given osculating to mean orbit converter.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to
                M2 drag is not considered
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Returns:
            mean orbit in a Brouwer-Lyddane sense
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float) -> org.orekit.orbits.KeplerianOrbit: ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, m2Value: float, epsilon: float, maxIterations: int) -> org.orekit.orbits.KeplerianOrbit: ...
    def getCk0(self) -> typing.MutableSequence[float]:
        """
        Get the un-normalized zonal coefficients.
        
        Returns:
            the un-normalized zonal coefficients
        
        
        """
        ...
    def getM2(self) -> float:
        """
        Get the value of the M2 drag parameter. Beware that M2Driver must have only 1 span on its TimeSpanMap value (that is to say setPeriod method should not be called)
        
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
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the parameters driver for propagation model.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for propagation model
        
        
        """
        ...
    def getReferenceRadius(self) -> float:
        """
        Get the reference radius of the central body attraction model.
        
        Returns:
            the reference radius in meters
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.KeplerianOrbit:
        """
        Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        The new initial state to consider must be defined with an osculating orbit.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        Also see:
            resetInitialState
        
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): mean Brouwer-Lyddane orbit or osculating orbit
        
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): mean Brouwer-Lyddane orbit or osculating orbit
            epsilon (double): convergence threshold for mean parameters conversion
            maxIterations (int): maximum iterations for mean parameters conversion
        
        Since:
            11.2
        
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): mean Brouwer-Lyddane orbit or osculating orbit
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType, epsilon: float, maxIterations: int) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> None: ...

class EcksteinHechlerPropagator(AbstractAnalyticalPropagator):
    """
    This class propagates a SpacecraftState using the analytical Eckstein-Hechler model.
    
    The Eckstein-Hechler model is suited for near circular orbits (e < 0.1, with poor accuracy between 0.005 and 0.1) and inclination neither equatorial (direct or retrograde) nor critical (direct or retrograde).
    
    Note that before version 7.0, there was a large inconsistency in the generated orbits, and it was fixed as of version 7.0 of Orekit, with a visible side effect. The problems is that if the circular parameters produced by the Eckstein-Hechler model are used to build an orbit considered to be osculating, the velocity deduced from this orbit was inconsistent with the position evolution! The reason is that the model includes non-Keplerian effects but it does not include a corresponding circular/Cartesian conversion. As a consequence, all subsequent computation involving velocity were wrong. This includes attitude modes like yaw compensation and Doppler effect. As this effect was considered serious enough and as accurate velocities were considered important, the propagator now generates CartesianOrbit which are built in a special way to ensure consistency throughout propagation. A side effect is that if circular parameters are rebuilt by user from these propagated Cartesian orbit, the circular parameters will generally not match the initial orbit (differences in semi-major axis can exceed 120 m). The position however will match to sub-micrometer level, and this position will be identical to the positions that were generated by previous versions (in other words, the internals of the models have not been changed, only the output parameters have been changed). The correctness of the initialization has been assessed and is good, as it allows the subsequent orbit to remain close to a numerical reference orbit.
    
    If users need a more definitive initialization of an Eckstein-Hechler propagator, they should consider using a PropagatorConverter to initialize their Eckstein-Hechler propagator using a complete sample instead of just a single initial orbit.
    
    Also see:
        Orbit
    """
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, initialType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, initialType: org.orekit.propagation.PropagationType, epsilon: float, maxIterations: int): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, initialType: org.orekit.propagation.PropagationType, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: float, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.AttitudeProvider, mass: float, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, initialType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, epsilon: float, maxIterations: int) -> org.orekit.orbits.CircularOrbit:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
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
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.orbits.CircularOrbit:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            referenceRadius (double): reference radius of the Earth for the potential model (m)
            mu (double): central attraction coefficient (m³/s²)
            c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
            c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
            c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
            c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
            c60 (double): un-normalized zonal coefficient (about -5.41e-7 for Earth)
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Returns:
            mean orbit in a Eckstein-Hechler sense
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics) -> org.orekit.orbits.CircularOrbit:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
        
        Returns:
            mean orbit in a Eckstein-Hechler sense
        
        Since:
            11.2
        
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (Orbit): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
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
    def computeMeanOrbit(osculating: org.orekit.orbits.Orbit, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, epsilon: float, maxIterations: int) -> org.orekit.orbits.CircularOrbit: ...
    def getCk0(self) -> typing.MutableSequence[float]:
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
    def getOsculatingCircularOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.CircularOrbit:
        """
        Get the osculating circular orbit from the EH model.
        
        This method is only relevant for the conversion from osculating to mean orbit.
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            the osculating circular orbite
        
        
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
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.CartesianOrbit:
        """
        Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        The new initial state to consider must be defined with an osculating orbit.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        Also see:
            resetInitialState
        
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): mean Eckstein-Hechler orbit or osculating orbit
        
        Since:
            10.2
        
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): mean Eckstein-Hechler orbit or osculating orbit
            epsilon (double): convergence threshold for mean parameters conversion
            maxIterations (int): maximum iterations for mean parameters conversion
        
        Since:
            11.2
        
        Reset the propagator initial state.
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): mean Eckstein-Hechler orbit or osculating orbit
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType, epsilon: float, maxIterations: int) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> None: ...

class Ephemeris(AbstractAnalyticalPropagator, org.orekit.propagation.BoundedPropagator):
    """
    This class is designed to accept and handle tabulated orbital entries. Tabulated entries are classified and then extrapolated in way to obtain continuous output, with accuracy and computation methods configured by the user.
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], int: int): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState]): ...
    @typing.overload
    def __init__(self, states: java.util.List[org.orekit.propagation.SpacecraftState], stateInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], covariances: java.util.List[org.orekit.propagation.StateCovariance], covarianceInterpolator: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]): ...
    @typing.overload
    def __init__(self, states: java.util.List[org.orekit.propagation.SpacecraftState], stateInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], covariances: java.util.List[org.orekit.propagation.StateCovariance], covarianceInterpolator: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, states: java.util.List[org.orekit.propagation.SpacecraftState], stateInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
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
    @staticmethod
    def checkInputConsistency(states: java.util.List[org.orekit.propagation.SpacecraftState], stateInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], covariances: java.util.List[org.orekit.propagation.StateCovariance], covarianceInterpolator: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]) -> None:
        """
        Check input consistency between states, covariances and their associated interpolators.
        
        Parameters:
            states (List<SpacecraftState> states): spacecraft states sample
            stateInterpolator (TimeInterpolator<SpacecraftState> stateInterpolator): spacecraft state interpolator
            covariances (List<StateCovariance> covariances): covariances sample
            covarianceInterpolator (TimeInterpolator<TimeStampedPair<Orbit, StateCovariance>>): covariance interpolator
        
        
        """
        ...
    @staticmethod
    def checkStatesAndCovariancesConsistency(states: java.util.List[org.orekit.propagation.SpacecraftState], covariances: java.util.List[org.orekit.propagation.StateCovariance]) -> None:
        """
        Check that given states and covariances are consistent.
        
        Parameters:
            states (List<SpacecraftState> states): tabulates states to check
            covariances (List<StateCovariance> covariances): tabulated covariances associated to tabulated states to check
        
        
        """
        ...
    def getCovariance(self, date: org.orekit.time.AbsoluteDate) -> java.util.Optional[org.orekit.propagation.StateCovariance]:
        """
        Get the covariance at given date.
        
        BEWARE : If this instance has been created without sample of covariances and/or with spacecraft states defined with absolute position-velocity-acceleration, it will return an empty Optional.
        
        Parameters:
            date (AbsoluteDate): date at which the covariance is desired
        
        Returns:
            covariance at given date
        
        Also see:
            Optional
        
        
        """
        ...
    def getCovarianceInterpolator(self) -> java.util.Optional[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]]:
        """
        Get covariance interpolator.
        
        Returns:
            optional covariance interpolator
        
        Also see:
            Optional
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
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
    def getManagedAdditionalData(self) -> typing.MutableSequence[str]:
        """
        Get all the names of all managed additional data.
        
        Specified by: getManagedAdditionalData in interface Propagator
        
        Overrides: getManagedAdditionalData in class AbstractPropagator
        
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
    def getStateInterpolator(self) -> org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState]:
        """
        Get state interpolator.
        
        Returns:
            state interpolator
        
        
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
        Try (and fail) to reset the initial state.
        
        This method always throws an exception, as ephemerides cannot be reset.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...

_FieldBrouwerLyddanePropagator__T = typing.TypeVar('_FieldBrouwerLyddanePropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBrouwerLyddanePropagator(FieldAbstractAnalyticalPropagator[_FieldBrouwerLyddanePropagator__T], typing.Generic[_FieldBrouwerLyddanePropagator__T]):
    """
    This class propagates a FieldSpacecraftState using the analytical Brouwer-Lyddane model (from J2 to J5 zonal harmonics).
    
    At the opposite of the FieldEcksteinHechlerPropagator, the Brouwer-Lyddane model is suited for elliptical orbits, there is no problem having a rather small eccentricity or inclination (Lyddane helped to solve this issue with the Brouwer model). Singularity for the critical inclination i = 63.4° is avoided using the method developed in Warren Phipps' 1992 thesis.
    
    By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992 thesis considered the atmospheric drag by time derivatives of the mean mean anomaly using the catch-all coefficient M2Driver. Usually, M2 is adjusted during an orbit determination process and it represents the combination of all unmodeled secular along-track effects (i.e. not just the atmospheric drag). The behavior of M2 is close to the getBStar parameter for the TLE. If the value of M2 is equal to M2, the along-track secular effects are not considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/s². The along-track effects, represented by the secular rates of the mean semi-major axis and eccentricity, are computed following Eq. 2.38, 2.41, and 2.45 of Warren Phipps' thesis.
    
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
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], referenceRadius: float, mu: _FieldBrouwerLyddanePropagator__T, c20: float, c30: float, c40: float, c50: float, m2Value: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], t: _FieldBrouwerLyddanePropagator__T, double: float, t2: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, t: _FieldBrouwerLyddanePropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldBrouwerLyddanePropagator__T, referenceRadius: float, mu: _FieldBrouwerLyddanePropagator__T, c20: float, c30: float, c40: float, c50: float, m2Value: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldBrouwerLyddanePropagator__T, referenceRadius: float, mu: _FieldBrouwerLyddanePropagator__T, c20: float, c30: float, c40: float, c50: float, initialType: org.orekit.propagation.PropagationType, m2Value: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldBrouwerLyddanePropagator__T, referenceRadius: float, mu: _FieldBrouwerLyddanePropagator__T, c20: float, c30: float, c40: float, c50: float, initialType: org.orekit.propagation.PropagationType, m2Value: float, epsilon: float, maxIterations: int): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldBrouwerLyddanePropagator__T, referenceRadius: float, mu: _FieldBrouwerLyddanePropagator__T, c20: float, c30: float, c40: float, c50: float, initialType: org.orekit.propagation.PropagationType, m2Value: float, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldBrouwerLyddanePropagator__T, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, m2Value: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, double: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitude: org.orekit.attitudes.AttitudeProvider, mass: _FieldBrouwerLyddanePropagator__T, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, initialType: org.orekit.propagation.PropagationType, m2Value: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldBrouwerLyddanePropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, double: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, m2Value: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldBrouwerLyddanePropagator__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType, double: float): ...
    _computeMeanOrbit_0__T = typing.TypeVar('_computeMeanOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_1__T = typing.TypeVar('_computeMeanOrbit_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_2__T = typing.TypeVar('_computeMeanOrbit_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_3__T = typing.TypeVar('_computeMeanOrbit_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_0__T], referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, m2Value: float, epsilon: float, maxIterations: int) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_0__T]:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2 parameter.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            referenceRadius (double): reference radius of the Earth for the potential model (m)
            mu (double): central attraction coefficient (m³/s²)
            c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
            c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
            c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
            c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to M2 drag is not considered
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
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_1__T], referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, m2Value: float, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_1__T]:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2 parameter.
        
        The computation is done through the given osculating to mean orbit converter.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            referenceRadius (double): reference radius of the Earth for the potential model (m)
            mu (double): central attraction coefficient (m³/s²)
            c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
            c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
            c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
            c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to M2 drag is not considered
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Returns:
            mean orbit in a Brouwer-Lyddane sense
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_2__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, m2Value: float) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_2__T]:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2 parameter.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to M2 drag is not considered
        
        Returns:
            mean orbit in a Brouwer-Lyddane sense
        
        Since:
            11.2
        
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Brouwer-Lyddane sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on both the gravity field parameterized in input and the atmospheric drag represented by the m2 parameter.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
            m2Value (double): value of empirical drag coefficient in rad/s². If equal to M2 drag is not considered
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
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_3__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, m2Value: float, epsilon: float, maxIterations: int) -> org.orekit.orbits.FieldKeplerianOrbit[_computeMeanOrbit_3__T]: ...
    @typing.overload
    def getM2(self) -> float:
        """
        Get the value of the M2 drag parameter.
        
        Returns:
            the value of the M2 drag parameter
        
        """
        ...
    @typing.overload
    def getM2(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the M2 drag parameter.
        
        Parameters:
            date (AbsoluteDate): date at which the model parameters want to be known
        
        Returns:
            the value of the M2 drag parameter
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldBrouwerLyddanePropagator__T], parameters: typing.Union[typing.List[_FieldBrouwerLyddanePropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldKeplerianOrbit[_FieldBrouwerLyddanePropagator__T]:
        """
        Propagate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldBrouwerLyddanePropagator> date): target date for the orbit
            parameters (FieldBrouwerLyddanePropagator[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T], stateType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T], stateType: org.orekit.propagation.PropagationType, epsilon: float, maxIterations: int) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldBrouwerLyddanePropagator__T], stateType: org.orekit.propagation.PropagationType, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> None: ...

_FieldEcksteinHechlerPropagator__T = typing.TypeVar('_FieldEcksteinHechlerPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEcksteinHechlerPropagator(FieldAbstractAnalyticalPropagator[_FieldEcksteinHechlerPropagator__T], typing.Generic[_FieldEcksteinHechlerPropagator__T]):
    """
    This class propagates a FieldSpacecraftState using the analytical Eckstein-Hechler model.
    
    The Eckstein-Hechler model is suited for near circular orbits (e < 0.1, with poor accuracy between 0.005 and 0.1) and inclination neither equatorial (direct or retrograde) nor critical (direct or retrograde).
    
    Also see:
        FieldOrbit
    """
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], referenceRadius: float, mu: _FieldEcksteinHechlerPropagator__T, c20: float, c30: float, c40: float, c50: float, c60: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], t: _FieldEcksteinHechlerPropagator__T, double: float, t2: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, t: _FieldEcksteinHechlerPropagator__T, double2: float, double3: float, double4: float, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldEcksteinHechlerPropagator__T, referenceRadius: float, mu: _FieldEcksteinHechlerPropagator__T, c20: float, c30: float, c40: float, c50: float, c60: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldEcksteinHechlerPropagator__T, referenceRadius: float, mu: _FieldEcksteinHechlerPropagator__T, c20: float, c30: float, c40: float, c50: float, c60: float, initialType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldEcksteinHechlerPropagator__T, referenceRadius: float, mu: _FieldEcksteinHechlerPropagator__T, c20: float, c30: float, c40: float, c50: float, c60: float, initialType: org.orekit.propagation.PropagationType, epsilon: float, maxIterations: int): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldEcksteinHechlerPropagator__T, referenceRadius: float, mu: _FieldEcksteinHechlerPropagator__T, c20: float, c30: float, c40: float, c50: float, c60: float, initialType: org.orekit.propagation.PropagationType, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mass: _FieldEcksteinHechlerPropagator__T, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, unnormalizedSphericalHarmonics2: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitude: org.orekit.attitudes.AttitudeProvider, mass: _FieldEcksteinHechlerPropagator__T, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, initialType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldEcksteinHechlerPropagator__T, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldEcksteinHechlerPropagator__T], unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, propagationType: org.orekit.propagation.PropagationType): ...
    _computeMeanOrbit_0__T = typing.TypeVar('_computeMeanOrbit_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_1__T = typing.TypeVar('_computeMeanOrbit_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_2__T = typing.TypeVar('_computeMeanOrbit_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanOrbit_3__T = typing.TypeVar('_computeMeanOrbit_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_0__T], referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, epsilon: float, maxIterations: int) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_0__T]:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
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
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_1__T], referenceRadius: float, mu: float, c20: float, c30: float, c40: float, c50: float, c60: float, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_1__T]:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through the given osculating to mean orbit converter.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            referenceRadius (double): reference radius of the Earth for the potential model (m)
            mu (double): central attraction coefficient (m³/s²)
            c20 (double): un-normalized zonal coefficient (about -1.08e-3 for Earth)
            c30 (double): un-normalized zonal coefficient (about +2.53e-6 for Earth)
            c40 (double): un-normalized zonal coefficient (about +1.62e-6 for Earth)
            c50 (double): un-normalized zonal coefficient (about +2.28e-7 for Earth)
            c60 (double): un-normalized zonal coefficient (about -5.41e-7 for Earth)
            converter (OsculatingToMeanConverter): osculating to mean orbit converter
        
        Returns:
            mean orbit in a Eckstein-Hechler sense
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_2__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_2__T]:
        """
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
        
        Returns:
            mean orbit in a Eckstein-Hechler sense
        
        Since:
            11.2
        
        Conversion from osculating to mean orbit.
        
        Compute mean orbit in a Eckstein-Hechler sense, corresponding to the osculating SpacecraftState in input.
        
        Since the osculating orbit is obtained with the computation of short-periodic variation, the resulting output will depend on the gravity field parameterized in input.
        
        The computation is done through a fixed-point iteration process.
        
        Parameters:
            osculating (FieldOrbit<T> osculating): osculating orbit to convert
            provider (UnnormalizedSphericalHarmonicsProvider): for un-normalized zonal coefficients
            harmonics (UnnormalizedSphericalHarmonics): getDate())
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
    def computeMeanOrbit(osculating: org.orekit.orbits.FieldOrbit[_computeMeanOrbit_3__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, harmonics: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider.UnnormalizedSphericalHarmonics, epsilon: float, maxIterations: int) -> org.orekit.orbits.FieldCircularOrbit[_computeMeanOrbit_3__T]: ...
    def getOsculatingCircularOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldEcksteinHechlerPropagator__T]) -> org.orekit.orbits.FieldCircularOrbit[_FieldEcksteinHechlerPropagator__T]:
        """
        Get the osculating circular orbit from the EH model.
        
        This method is only relevant for the conversion from osculating to mean orbit.
        
        Parameters:
            date (FieldAbsoluteDate<FieldEcksteinHechlerPropagator> date): target date for the orbit
        
        Returns:
            the osculating circular orbite
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldEcksteinHechlerPropagator__T], parameters: typing.Union[typing.List[_FieldEcksteinHechlerPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldCartesianOrbit[_FieldEcksteinHechlerPropagator__T]:
        """
        Propagate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldEcksteinHechlerPropagator> date): target date for the orbit
            parameters (FieldEcksteinHechlerPropagator[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T], stateType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T], stateType: org.orekit.propagation.PropagationType, epsilon: float, maxIterations: int) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldEcksteinHechlerPropagator__T], stateType: org.orekit.propagation.PropagationType, converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> None: ...

_FieldKeplerianPropagator__T = typing.TypeVar('_FieldKeplerianPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldKeplerianPropagator(FieldAbstractAnalyticalPropagator[_FieldKeplerianPropagator__T], typing.Generic[_FieldKeplerianPropagator__T]):
    """
    Simple Keplerian orbit propagator.
    
    Also see:
        FieldOrbit
    """
    @typing.overload
    def __init__(self, initialFieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], t: _FieldKeplerianPropagator__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, initialFieldOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mu: _FieldKeplerianPropagator__T): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T], attitudeProv: org.orekit.attitudes.AttitudeProvider, mu: _FieldKeplerianPropagator__T, mass: _FieldKeplerianPropagator__T): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldKeplerianPropagator__T], parameters: typing.Union[typing.List[_FieldKeplerianPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_FieldKeplerianPropagator__T]:
        """
        Propagate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldKeplerianPropagator> date): target date for the orbit
            parameters (FieldKeplerianPropagator[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldKeplerianPropagator__T]) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Overrides: resetInitialState in class FieldAbstractPropagator
        
        Parameters:
            state (FieldSpacecraftState<FieldKeplerianPropagator> state): new initial state to consider
        
        
        """
        ...

class KeplerianPropagator(AbstractAnalyticalPropagator):
    """
    Simple Keplerian orbit propagator.
    
    Also see:
        Orbit
    """
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mu: float): ...
    @typing.overload
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, attitudeProv: org.orekit.attitudes.AttitudeProvider, mu: float, mass: float): ...
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

class PythonAbstractAnalyticalGradientConverter(AbstractAnalyticalGradientConverter):
    def __init__(self, abstractAnalyticalPropagator: AbstractAnalyticalPropagator, int: int): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getPropagator(self) -> FieldAbstractAnalyticalPropagator[org.hipparchus.analysis.differentiation.Gradient]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonAbstractAnalyticalMatricesHarvester(AbstractAnalyticalMatricesHarvester):
    def __init__(self, propagator: AbstractAnalyticalPropagator, stmName: str, initialStm: org.hipparchus.linear.RealMatrix, initialJacobianColumns: org.orekit.utils.DoubleArrayDictionary):
        """
        Simple constructor.
        
        The arguments for initial matrices must be compatible with the OrbitType and PositionAngleType that will be used by propagator
        
        Parameters:
            propagator (AbstractAnalyticalPropagator): propagator bound to this harvester
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
    def getGradientConverter(self) -> AbstractAnalyticalGradientConverter:
        """
        Get the gradient converter related to the analytical orbit propagator.
        
        Specified by: getGradientConverter in class AbstractAnalyticalMatricesHarvester
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonAbstractAnalyticalPropagator(AbstractAnalyticalPropagator):
    def __init__(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider):
        """
        Build a new instance.
        
        Parameters:
            attitudeProvider (AttitudeProvider): provider for attitude computation
        
        
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
    def getMass(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the mass. Extension point for Python.
        
        Specified by: getMass in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            mass mass
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Extrapolate an orbit up to a specific target date. Extension point for Python.
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def resetIntermediateState(self, state: org.orekit.propagation.SpacecraftState, forward: bool) -> None:
        """
        Reset an intermediate state. Extension point for Python.
        
        Specified by: resetIntermediateState in class AbstractAnalyticalPropagator
        
        Parameters:
            state (SpacecraftState): new intermediate state to consider
            forward (boolean): if true, the intermediate state is valid for
        
        
        """
        ...

_PythonFieldAbstractAnalyticalPropagator__T = typing.TypeVar('_PythonFieldAbstractAnalyticalPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractAnalyticalPropagator(FieldAbstractAnalyticalPropagator[_PythonFieldAbstractAnalyticalPropagator__T], typing.Generic[_PythonFieldAbstractAnalyticalPropagator__T]):
    def __init__(self, field: org.hipparchus.Field[_PythonFieldAbstractAnalyticalPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider):
        """
        Build a new instance.
        
        Parameters:
            field (Field<PythonFieldAbstractAnalyticalPropagator> field): field used as default
            attitudeProvider (AttitudeProvider): provider for attitude computation
        
        
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
    def getMass(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractAnalyticalPropagator__T]) -> _PythonFieldAbstractAnalyticalPropagator__T:
        """
        Get the mass.
        
        Specified by: getMass in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldAbstractAnalyticalPropagator> date): target date for the orbit
        
        Returns:
            mass mass
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the parameters driver for propagation model.
        
        Returns:
            drivers for propagation model
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractAnalyticalPropagator__T], parameters: typing.Union[typing.List[_PythonFieldAbstractAnalyticalPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_PythonFieldAbstractAnalyticalPropagator__T]:
        """
        Extrapolate an orbit up to a specific target date.
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldAbstractAnalyticalPropagator> date): target date for the orbit
            parameters (PythonFieldAbstractAnalyticalPropagator[]): model parameters
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def resetIntermediateState(self, state: org.orekit.propagation.FieldSpacecraftState[_PythonFieldAbstractAnalyticalPropagator__T], forward: bool) -> None:
        """
        Reset an intermediate state.
        
        Specified by: resetIntermediateState in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            state (FieldSpacecraftState<PythonFieldAbstractAnalyticalPropagator> state): new intermediate state to consider
            forward (boolean): if true, the intermediate state is valid for
        
        
        """
        ...

class J2DifferentialEffect(AdapterPropagator.DifferentialEffect):
    """
    Analytical model for J2 effect.
    
    This class computes the differential effect of J2 due to an initial orbit offset. A typical case is when an inclination maneuver changes an orbit inclination at time t₀. As ascending node drift rate depends on inclination, the change induces a time-dependent change in ascending node for later dates.
    
    Also see:
        SmallManeuverAnalyticalModel
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit, boolean: bool, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit, boolean: bool, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, differentialEffect: typing.Union[AdapterPropagator.DifferentialEffect, typing.Callable], boolean: bool, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, differentialEffect: typing.Union[AdapterPropagator.DifferentialEffect, typing.Callable], boolean: bool, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def apply(self, orbit1: org.orekit.orbits.Orbit) -> org.orekit.orbits.Orbit:
        """
        Compute the effect of the maneuver on an orbit.
        
        Parameters:
            orbit1 (Orbit): original orbit at t₁, without maneuver
        
        Returns:
            orbit at t₁, taking the maneuver into account if t₁ > t₀
        
        Also see:
            apply
        
        Apply the effect to a SpacecraftState.
        
        Applying the effect may be a no-op in some cases. A typical example is maneuvers, for which the state is changed only for time after the maneuver occurrence.
        
        Specified by: apply in interface DifferentialEffect
        
        Parameters:
            state1 (SpacecraftState): original state without the effect
        
        Returns:
            updated state at the same date, taking the effect into account if meaningful
        
        
        """
        ...
    @typing.overload
    def apply(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState: ...

class PythonDifferentialEffect(AdapterPropagator.DifferentialEffect):
    def __init__(self): ...
    def apply(self, original: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Apply the effect to a SpacecraftState.
        
        Applying the effect may be a no-op in some cases. A typical example is maneuvers, for which the state is changed only for time after the maneuver occurrence.
        
        Specified by: apply in interface DifferentialEffect
        
        Parameters:
            original (SpacecraftState): original state without the effect
        
        Returns:
            updated state at the same date, taking the effect into account if meaningful
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...


class __module_protocol__(Protocol):
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
    gnss: org.orekit.propagation.analytical.gnss.__module_protocol__
    intelsat: org.orekit.propagation.analytical.intelsat.__module_protocol__
    tle: org.orekit.propagation.analytical.tle.__module_protocol__
