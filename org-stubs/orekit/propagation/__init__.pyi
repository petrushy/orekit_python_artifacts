import java.io
import java.lang
import java.util
import java.util.stream
import org.hipparchus
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



class AdditionalStateProvider:
    """
    public interface AdditionalStateProvider
    
        This interface represents providers for additional state data beyond :class:`~org.orekit.propagation.SpacecraftState`.
    
        This interface is the analytical (read already integrated) counterpart of the
        :class:`~org.orekit.propagation.integration.AdditionalEquations` interface. It allows to append various additional state
        parameters to any :class:`~org.orekit.propagation.AbstractPropagator`.
    
        Also see:
            :class:`~org.orekit.propagation.AbstractPropagator`, :class:`~org.orekit.propagation.integration.AdditionalEquations`
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
        
            Returns:
                name of the additional state
        
        
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
    public interface FieldAdditionalStateProvider<T extends CalculusFieldElement<T>>
    
        This interface represents providers for additional state data beyond :class:`~org.orekit.propagation.SpacecraftState`.
    
        This interface is the analytical (read already integrated) counterpart of the
        :class:`~org.orekit.propagation.integration.AdditionalEquations` interface. It allows to append various additional state
        parameters to any :class:`~org.orekit.propagation.AbstractPropagator`.
    
        Also see:
            :class:`~org.orekit.propagation.AbstractPropagator`, :class:`~org.orekit.propagation.integration.AdditionalEquations`
    """
    def getAdditionalState(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldAdditionalStateProvider__T]) -> typing.List[_FieldAdditionalStateProvider__T]: ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Returns:
                name of the additional state
        
        
        """
        ...

_FieldEphemerisGenerator__T = typing.TypeVar('_FieldEphemerisGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEphemerisGenerator(typing.Generic[_FieldEphemerisGenerator__T]):
    """
    public interface FieldEphemerisGenerator<T extends CalculusFieldElement<T>>
    
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
    public interface FieldPropagator<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.utils.FieldPVCoordinatesProvider`<T>
    
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
        
            Parameters:
                name (String): name of the additional state
        
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
class FieldSpacecraftState(org.orekit.time.FieldTimeStamped[_FieldSpacecraftState__T], org.orekit.time.FieldTimeShiftable['FieldSpacecraftState'[_FieldSpacecraftState__T], _FieldSpacecraftState__T], org.orekit.time.FieldTimeInterpolable['FieldSpacecraftState'[_FieldSpacecraftState__T], _FieldSpacecraftState__T], typing.Generic[_FieldSpacecraftState__T]):
    """
    public class FieldSpacecraftState<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.time.FieldTimeStamped`<T>, :class:`~org.orekit.time.FieldTimeShiftable`<:class:`~org.orekit.propagation.FieldSpacecraftState`<T>,T>, :class:`~org.orekit.time.FieldTimeInterpolable`<:class:`~org.orekit.propagation.FieldSpacecraftState`<T>,T>
    
        This class is the representation of a complete state holding orbit, attitude and mass information at a given date.
    
        It contains an :class:`~org.orekit.orbits.FieldOrbit` at a current :class:`~org.orekit.time.FieldAbsoluteDate` both
        handled by an :class:`~org.orekit.orbits.FieldOrbit`, plus the current mass and attitude. FieldOrbitand state are
        guaranteed to be consistent in terms of date and reference frame. The spacecraft state may also contain additional
        states, which are simply named double arrays which can hold any user-defined data.
    
        The state can be slightly shifted to close dates. This shift is based on a simple Keplerian model for orbit, a linear
        extrapolation for attitude taking the spin rate into account and no mass change. It is *not* intended as a replacement
        for proper orbit and attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
        The instance :code:`FieldSpacecraftState` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldSpacecraftState__T], spacecraftState: 'SpacecraftState'): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T): ...
    @typing.overload
    def __init__(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T], fieldAttitude: org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T], t: _FieldSpacecraftState__T, map: typing.Union[java.util.Map[str, typing.List[_FieldSpacecraftState__T]], typing.Mapping[str, typing.List[_FieldSpacecraftState__T]]]): ...
    def addAdditionalState(self, string: str, tArray: typing.List[_FieldSpacecraftState__T]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]: ...
    def ensureCompatibleAdditionalStates(self, fieldSpacecraftState: 'FieldSpacecraftState'[_FieldSpacecraftState__T]) -> None: ...
    def getA(self) -> _FieldSpacecraftState__T:
        """
            Get the semi-major axis.
        
            Returns:
                semi-major axis (m), or {code Double.NaN} if the state is contains an absolute position-velocity-acceleration rather
                than an orbit
        
        
        """
        ...
    def getAbsPVA(self) -> org.orekit.utils.FieldAbsolutePVCoordinates[_FieldSpacecraftState__T]: ...
    def getAdditionalState(self, string: str) -> typing.List[_FieldSpacecraftState__T]:
        """
            Get an additional state.
        
            Parameters:
                name (String): name of the additional state
        
            Returns:
                value of the additional state
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStates`
        
        
        """
        ...
    def getAdditionalStates(self) -> java.util.Map[str, typing.List[_FieldSpacecraftState__T]]: ...
    def getAttitude(self) -> org.orekit.attitudes.FieldAttitude[_FieldSpacecraftState__T]: ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftState__T]: ...
    def getE(self) -> _FieldSpacecraftState__T:
        """
            Get the eccentricity.
        
            Returns:
                eccentricity, or {code Double.NaN} if the state is contains an absolute position-velocity-acceleration rather than an
                orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getEquinoctialEx`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getEquinoctialEy`
        
        
        """
        ...
    def getEquinoctialEx(self) -> _FieldSpacecraftState__T:
        """
            Get the first component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e cos(Ã�â€° + ÃŽÂ©), first component of eccentricity vector, or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getE`
        
        
        """
        ...
    def getEquinoctialEy(self) -> _FieldSpacecraftState__T:
        """
            Get the second component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e sin(Ã�â€° + ÃŽÂ©), second component of the eccentricity vector, or {code Double.NaN} if the state is contains an
                absolute position-velocity-acceleration rather than an orbit
        
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
                tan(i/2) cos(ÃŽÂ©), first component of the inclination vector, or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getI`
        
        
        """
        ...
    def getHy(self) -> _FieldSpacecraftState__T:
        """
            Get the second component of the inclination vector (as per equinoctial parameters).
        
            Returns:
                tan(i/2) sin(ÃŽÂ©), second component of the inclination vector, or {code Double.NaN} if the state is contains an
                absolute position-velocity-acceleration rather than an orbit
        
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
                keplerian mean motion in radians per second, or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getKeplerianPeriod(self) -> _FieldSpacecraftState__T:
        """
            Get the Keplerian period.
        
            The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                keplerian period in seconds, or {code Double.NaN} if the state is contains an absolute position-velocity-acceleration
                rather than an orbit
        
        
        """
        ...
    def getLE(self) -> _FieldSpacecraftState__T:
        """
            Get the eccentric latitude argument (as per equinoctial parameters).
        
            Returns:
                E + Ã�â€° + ÃŽÂ© eccentric longitude argument (rad), or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getLv`, :meth:`~org.orekit.propagation.FieldSpacecraftState.getLM`
        
        
        """
        ...
    def getLM(self) -> _FieldSpacecraftState__T:
        """
            Get the mean longitude argument (as per equinoctial parameters).
        
            Returns:
                M + Ã�â€° + ÃŽÂ© mean latitude argument (rad), or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getLv`, :meth:`~org.orekit.propagation.FieldSpacecraftState.getLE`
        
        
        """
        ...
    def getLv(self) -> _FieldSpacecraftState__T:
        """
            Get the true latitude argument (as per equinoctial parameters).
        
            Returns:
                v + Ã�â€° + ÃŽÂ© true longitude argument (rad), or {code Double.NaN} if the state is contains an absolute
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
                mu central attraction coefficient (m^3/s^2), or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getOrbit(self) -> org.orekit.orbits.FieldOrbit[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPVCoordinates(self) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldSpacecraftState__T]: ...
    @typing.overload
    def getPVCoordinates(self, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldSpacecraftState__T]: ...
    def hasAdditionalState(self, string: str) -> bool:
        """
            Check if an additional state is available.
        
            Parameters:
                name (String): name of the additional state
        
            Returns:
                true if the additional state is available
        
            Also see:
                :meth:`~org.orekit.propagation.FieldSpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalState`,
                :meth:`~org.orekit.propagation.FieldSpacecraftState.getAdditionalStates`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldSpacecraftState__T], typing.Sequence[_FieldSpacecraftState__T], typing.Set[_FieldSpacecraftState__T]]) -> _FieldSpacecraftState__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldSpacecraftState__T], stream: java.util.stream.Stream['FieldSpacecraftState'[_FieldSpacecraftState__T]]) -> 'FieldSpacecraftState'[_FieldSpacecraftState__T]: ...
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
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def toTransform(self) -> org.orekit.frames.FieldTransform[_FieldSpacecraftState__T]: ...

class PropagationType(java.lang.Enum['PropagationType']):
    """
    public enum PropagationType extends Enum<:class:`~org.orekit.propagation.PropagationType`>
    
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
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
        
            Parameters:
                name (String): name of the additional state
        
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

class PropagatorsParallelizer:
    """
    public class PropagatorsParallelizer extends Object
    
        This class provides a way to propagate simultaneously several orbits.
    
        Multi-satellites propagation is based on multi-threading. Therefore, care must be taken so that all propagators can be
        run in a multi-thread context. This implies that all propagators are built independently and that they rely on force
        models that are also built independently. An obvious mistake would be to reuse a maneuver force model, as these models
        need to cache the firing/not-firing status. Objects used by force models like atmosphere models for drag force or others
        may also cache intermediate variables, so separate instances for each propagator must be set up.
    
        This class *will* create new threads for running the propagators and it *will* override the underlying propagators step
        handlers. The intent is anyway to manage the steps all at once using the global
        :class:`~org.orekit.propagation.sampling.MultiSatStepHandler` set up at construction.
    
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
    def __init__(self, list: java.util.List[Propagator], multiSatStepHandler: org.orekit.propagation.sampling.MultiSatStepHandler): ...
    def getPropagators(self) -> java.util.List[Propagator]: ...
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> java.util.List['SpacecraftState']: ...

class SpacecraftState(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['SpacecraftState'], org.orekit.time.TimeInterpolable['SpacecraftState'], java.io.Serializable):
    """
    public class SpacecraftState extends Object implements :class:`~org.orekit.time.TimeStamped`, :class:`~org.orekit.time.TimeShiftable`<:class:`~org.orekit.propagation.SpacecraftState`>, :class:`~org.orekit.time.TimeInterpolable`<:class:`~org.orekit.propagation.SpacecraftState`>, Serializable
    
        This class is the representation of a complete state holding orbit, attitude and mass information at a given date.
    
        It contains an :class:`~org.orekit.orbits.Orbit` at a current :class:`~org.orekit.time.AbsoluteDate` both handled by an
        :class:`~org.orekit.orbits.Orbit`, plus the current mass and attitude. Orbit and state are guaranteed to be consistent
        in terms of date and reference frame. The spacecraft state may also contain additional states, which are simply named
        double arrays which can hold any user-defined data.
    
        The state can be slightly shifted to close dates. This shift is based on a simple Keplerian model for orbit, a linear
        extrapolation for attitude taking the spin rate into account and no mass change. It is *not* intended as a replacement
        for proper orbit and attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
        The instance :code:`SpacecraftState` is guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, double: float, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, attitude: org.orekit.attitudes.Attitude, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, double: float): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, double: float, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, double: float, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    @typing.overload
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, attitude: org.orekit.attitudes.Attitude, map: typing.Union[java.util.Map[str, typing.List[float]], typing.Mapping[str, typing.List[float]]]): ...
    def addAdditionalState(self, string: str, doubleArray: typing.List[float]) -> 'SpacecraftState':
        """
            Add an additional state.
        
            :class:`~org.orekit.propagation.SpacecraftState` instances are immutable, so this method does *not* change the instance,
            but rather creates a new instance, which has the same orbit, attitude, mass and additional states as the original
            instance, except it also has the specified state. If the original instance already had an additional state with the same
            name, it will be overridden. If it did not have any additional state with that name, the new instance will have one more
            additional state than the original instance.
        
            Parameters:
                name (String): name of the additional state
                value (double...): value of the additional state
        
            Returns:
                a new instance, with the additional state added
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStates`
        
        
        """
        ...
    def ensureCompatibleAdditionalStates(self, spacecraftState: 'SpacecraftState') -> None: ...
    def getA(self) -> float:
        """
            Get the semi-major axis.
        
            Returns:
                semi-major axis (m), or {code Double.NaN} if the state is contains an absolute position-velocity-acceleration rather
                than an orbit
        
        
        """
        ...
    def getAbsPVA(self) -> org.orekit.utils.AbsolutePVCoordinates: ...
    def getAdditionalState(self, string: str) -> typing.List[float]:
        """
            Get an additional state.
        
            Parameters:
                name (String): name of the additional state
        
            Returns:
                value of the additional state
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.hasAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStates`
        
        
        """
        ...
    def getAdditionalStates(self) -> java.util.Map[str, typing.List[float]]:
        """
            Get an unmodifiable map of additional states.
        
            Returns:
                unmodifiable map of additional states
        
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
                date
        
        
        """
        ...
    def getE(self) -> float:
        """
            Get the eccentricity.
        
            Returns:
                eccentricity, or {code Double.NaN} if the state is contains an absolute position-velocity-acceleration rather than an
                orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getEquinoctialEx`,
                :meth:`~org.orekit.propagation.SpacecraftState.getEquinoctialEy`
        
        
        """
        ...
    def getEquinoctialEx(self) -> float:
        """
            Get the first component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e cos(Ã�â€° + ÃŽÂ©), first component of eccentricity vector, or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getE`
        
        
        """
        ...
    def getEquinoctialEy(self) -> float:
        """
            Get the second component of the eccentricity vector (as per equinoctial parameters).
        
            Returns:
                e sin(Ã�â€° + ÃŽÂ©), second component of the eccentricity vector, or {code Double.NaN} if the state is contains an
                absolute position-velocity-acceleration rather than an orbit
        
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
                tan(i/2) cos(ÃŽÂ©), first component of the inclination vector, or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getI`
        
        
        """
        ...
    def getHy(self) -> float:
        """
            Get the second component of the inclination vector (as per equinoctial parameters).
        
            Returns:
                tan(i/2) sin(ÃŽÂ©), second component of the inclination vector, or {code Double.NaN} if the state is contains an
                absolute position-velocity-acceleration rather than an orbit
        
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
                keplerian mean motion in radians per second, or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
        
        """
        ...
    def getKeplerianPeriod(self) -> float:
        """
            Get the Keplerian period.
        
            The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                keplerian period in seconds, or {code Double.NaN} if the state is contains an absolute position-velocity-acceleration
                rather than an orbit
        
        
        """
        ...
    def getLE(self) -> float:
        """
            Get the eccentric latitude argument (as per equinoctial parameters).
        
            Returns:
                E + Ã�â€° + ÃŽÂ© eccentric longitude argument (rad), or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getLv`, :meth:`~org.orekit.propagation.SpacecraftState.getLM`
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude argument (as per equinoctial parameters).
        
            Returns:
                M + Ã�â€° + ÃŽÂ© mean latitude argument (rad), or {code Double.NaN} if the state is contains an absolute
                position-velocity-acceleration rather than an orbit
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.getLv`, :meth:`~org.orekit.propagation.SpacecraftState.getLE`
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true latitude argument (as per equinoctial parameters).
        
            Returns:
                v + Ã�â€° + ÃŽÂ© true longitude argument (rad), or {code Double.NaN} if the state is contains an absolute
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
                mu central attraction coefficient (m^3/s^2), or {code Double.NaN} if the state is contains an absolute
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
    def hasAdditionalState(self, string: str) -> bool:
        """
            Check if an additional state is available.
        
            Parameters:
                name (String): name of the additional state
        
            Returns:
                true if the additional state is available
        
            Also see:
                :meth:`~org.orekit.propagation.SpacecraftState.addAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`,
                :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalStates`
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream['SpacecraftState']) -> 'SpacecraftState': ...
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
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
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

class AbstractPropagator(Propagator):
    """
    public abstract class AbstractPropagator extends Object implements :class:`~org.orekit.propagation.Propagator`
    
        Common handling of :class:`~org.orekit.propagation.Propagator` methods for analytical propagators.
    
        This abstract class allows to provide easily the full set of :class:`~org.orekit.propagation.Propagator` methods,
        including all propagation modes support and discrete events support for any simple propagation method.
    """
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None:
        """
            Add a set of user-specified state parameters to be computed along with the orbit propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.addAdditionalStateProvider`Â in
                interfaceÂ :class:`~org.orekit.propagation.Propagator`
        
            Parameters:
                additionalStateProvider (:class:`~org.orekit.propagation.AdditionalStateProvider`): provider for additional state
        
        
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
                :meth:`~org.orekit.propagation.Propagator.getManagedAdditionalStates`Â in
                interfaceÂ :class:`~org.orekit.propagation.Propagator`
        
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
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates`Â in
                interfaceÂ :class:`~org.orekit.utils.PVCoordinatesProvider`
        
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
        
            Parameters:
                name (String): name of the additional state
        
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
    public abstract class FieldAbstractPropagator<T extends CalculusFieldElement<T>> extends Object implements :class:`~org.orekit.propagation.FieldPropagator`<T>
    
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
                :meth:`~org.orekit.propagation.FieldPropagator.getAttitudeProvider`Â in
                interfaceÂ :class:`~org.orekit.propagation.FieldPropagator`
        
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
                :meth:`~org.orekit.propagation.FieldPropagator.getManagedAdditionalStates`Â in
                interfaceÂ :class:`~org.orekit.propagation.FieldPropagator`
        
            Returns:
                names of all managed states
        
        
        """
        ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_FieldAbstractPropagator__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAbstractPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldAbstractPropagator__T]: ...
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
        
            Parameters:
                name (String): name of the additional state
        
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
                :meth:`~org.orekit.propagation.FieldPropagator.setAttitudeProvider`Â in
                interfaceÂ :class:`~org.orekit.propagation.FieldPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...

_FieldBoundedPropagator__T = typing.TypeVar('_FieldBoundedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBoundedPropagator(FieldPropagator[_FieldBoundedPropagator__T], typing.Generic[_FieldBoundedPropagator__T]):
    """
    public interface FieldBoundedPropagator<T extends CalculusFieldElement<T>> extends :class:`~org.orekit.propagation.FieldPropagator`<T>
    
        This interface is intended for ephemerides valid only during a time range.
    
        This interface provides a mean to retrieve orbital parameters at any time within a given range. It should be implemented
        by orbit readers based on external data files and by continuous models built after numerical integration has been
        completed and dense output data as been gathered.
    """
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldBoundedPropagator__T]: ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldBoundedPropagator__T]: ...

class PythonAdditionalStateProvider(AdditionalStateProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAdditionalState(self, spacecraftState: SpacecraftState) -> typing.List[float]: ...
    def getName(self) -> str: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonEphemerisGenerator(EphemerisGenerator):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getGeneratedEphemeris(self) -> BoundedPropagator: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldAdditionalStateProvider__T = typing.TypeVar('_PythonFieldAdditionalStateProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAdditionalStateProvider(FieldAdditionalStateProvider[_PythonFieldAdditionalStateProvider__T], typing.Generic[_PythonFieldAdditionalStateProvider__T]):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAdditionalState(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldAdditionalStateProvider__T]) -> typing.List[_PythonFieldAdditionalStateProvider__T]: ...
    def getName(self) -> str: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldEphemerisGenerator__T = typing.TypeVar('_PythonFieldEphemerisGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldEphemerisGenerator(FieldEphemerisGenerator[_PythonFieldEphemerisGenerator__T], typing.Generic[_PythonFieldEphemerisGenerator__T]):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getGeneratedEphemeris(self) -> FieldBoundedPropagator[_PythonFieldEphemerisGenerator__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldPropagator__T = typing.TypeVar('_PythonFieldPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldPropagator(FieldPropagator[_PythonFieldPropagator__T], typing.Generic[_PythonFieldPropagator__T]):
    def __init__(self): ...
    def addAdditionalStateProvider(self, fieldAdditionalStateProvider: FieldAdditionalStateProvider[_PythonFieldPropagator__T]) -> None: ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None: ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[FieldAdditionalStateProvider[_PythonFieldPropagator__T]]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider: ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldPropagator__T]]: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialState(self) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]: ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_PythonFieldPropagator__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_PythonFieldPropagator__T]: ...
    def isAdditionalStateManaged(self, string: str) -> bool: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T]) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T]) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
    def propagate_FF(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldPropagator__T]) -> FieldSpacecraftState[_PythonFieldPropagator__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetInitialState(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None: ...
    def setMasterMode_TF(self, t: _PythonFieldPropagator__T, fieldOrekitFixedStepHandler: org.orekit.propagation.sampling.FieldOrekitFixedStepHandler[_PythonFieldPropagator__T]) -> None: ...

class PythonPropagator(Propagator):
    def __init__(self): ...
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None: ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None: ...
    def clearEventsDetectors(self) -> None: ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[AdditionalStateProvider]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider: ...
    def getEphemerisGenerator(self) -> EphemerisGenerator: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialState(self) -> SpacecraftState: ...
    def getManagedAdditionalStates(self) -> typing.List[str]: ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer: ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def isAdditionalStateManaged(self, string: str) -> bool: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    def propagate_AA(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetInitialState(self, spacecraftState: SpacecraftState) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None: ...
    def setEphemerisModeHandler(self, orekitStepHandler: org.orekit.propagation.sampling.OrekitStepHandler) -> None: ...

class PythonAbstractPropagator(AbstractPropagator):
    def __init__(self): ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None: ...
    def clearEventsDetectors(self) -> None: ...
    def finalize(self) -> None: ...
    def getEphemerisGenerator(self) -> EphemerisGenerator: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonBoundedPropagator(BoundedPropagator):
    def __init__(self): ...
    def addAdditionalStateProvider(self, additionalStateProvider: AdditionalStateProvider) -> None: ...
    _addEventDetector__T = typing.TypeVar('_addEventDetector__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addEventDetector(self, t: _addEventDetector__T) -> None: ...
    def clearEventsDetectors(self) -> None: ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[AdditionalStateProvider]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider: ...
    def getEphemerisGenerator(self) -> EphemerisGenerator: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.EventDetector]: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialState(self) -> SpacecraftState: ...
    def getManagedAdditionalStates(self) -> typing.List[str]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.StepHandlerMultiplexer: ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def isAdditionalStateManaged(self, string: str) -> bool: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    def propagate_AA(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> SpacecraftState: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetInitialState(self, spacecraftState: SpacecraftState) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None: ...

_PythonFieldAbstractPropagator__T = typing.TypeVar('_PythonFieldAbstractPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldAbstractPropagator(FieldAbstractPropagator[_PythonFieldAbstractPropagator__T], typing.Generic[_PythonFieldAbstractPropagator__T]):
    def __init__(self, field: org.hipparchus.Field[_PythonFieldAbstractPropagator__T]): ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None: ...
    def finalize(self) -> None: ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldAbstractPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldAbstractPropagator__T]]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractPropagator__T]) -> FieldSpacecraftState[_PythonFieldAbstractPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldAbstractPropagator__T]) -> FieldSpacecraftState[_PythonFieldAbstractPropagator__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

_PythonFieldBoundedPropagator__T = typing.TypeVar('_PythonFieldBoundedPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldBoundedPropagator(FieldBoundedPropagator[_PythonFieldBoundedPropagator__T], typing.Generic[_PythonFieldBoundedPropagator__T]):
    def __init__(self): ...
    def addAdditionalStateProvider(self, fieldAdditionalStateProvider: FieldAdditionalStateProvider[_PythonFieldBoundedPropagator__T]) -> None: ...
    _addEventDetector__D = typing.TypeVar('_addEventDetector__D', bound=org.orekit.propagation.events.FieldEventDetector)  # <D>
    def addEventDetector(self, d: _addEventDetector__D) -> None: ...
    def clearEventsDetectors(self) -> None: ...
    def finalize(self) -> None: ...
    def getAdditionalStateProviders(self) -> java.util.List[FieldAdditionalStateProvider[_PythonFieldBoundedPropagator__T]]: ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider: ...
    def getEphemerisGenerator(self) -> FieldEphemerisGenerator[_PythonFieldBoundedPropagator__T]: ...
    def getEventsDetectors(self) -> java.util.Collection[org.orekit.propagation.events.FieldEventDetector[_PythonFieldBoundedPropagator__T]]: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getInitialState(self) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
    def getManagedAdditionalStates(self) -> typing.List[str]: ...
    def getMaxDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]: ...
    def getMinDate(self) -> org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]: ...
    def getMultiplexer(self) -> org.orekit.propagation.sampling.FieldStepHandlerMultiplexer[_PythonFieldBoundedPropagator__T]: ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_PythonFieldBoundedPropagator__T]: ...
    def isAdditionalStateManaged(self, string: str) -> bool: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
    @typing.overload
    def propagate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
    def propagate_FF(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T], fieldAbsoluteDate2: org.orekit.time.FieldAbsoluteDate[_PythonFieldBoundedPropagator__T]) -> FieldSpacecraftState[_PythonFieldBoundedPropagator__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetInitialState(self, fieldSpacecraftState: FieldSpacecraftState[_PythonFieldBoundedPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation")``.

    AbstractPropagator: typing.Type[AbstractPropagator]
    AdditionalStateProvider: typing.Type[AdditionalStateProvider]
    BoundedPropagator: typing.Type[BoundedPropagator]
    EphemerisGenerator: typing.Type[EphemerisGenerator]
    FieldAbstractPropagator: typing.Type[FieldAbstractPropagator]
    FieldAdditionalStateProvider: typing.Type[FieldAdditionalStateProvider]
    FieldBoundedPropagator: typing.Type[FieldBoundedPropagator]
    FieldEphemerisGenerator: typing.Type[FieldEphemerisGenerator]
    FieldPropagator: typing.Type[FieldPropagator]
    FieldSpacecraftState: typing.Type[FieldSpacecraftState]
    PropagationType: typing.Type[PropagationType]
    Propagator: typing.Type[Propagator]
    PropagatorsParallelizer: typing.Type[PropagatorsParallelizer]
    PythonAbstractPropagator: typing.Type[PythonAbstractPropagator]
    PythonAdditionalStateProvider: typing.Type[PythonAdditionalStateProvider]
    PythonBoundedPropagator: typing.Type[PythonBoundedPropagator]
    PythonEphemerisGenerator: typing.Type[PythonEphemerisGenerator]
    PythonFieldAbstractPropagator: typing.Type[PythonFieldAbstractPropagator]
    PythonFieldAdditionalStateProvider: typing.Type[PythonFieldAdditionalStateProvider]
    PythonFieldBoundedPropagator: typing.Type[PythonFieldBoundedPropagator]
    PythonFieldEphemerisGenerator: typing.Type[PythonFieldEphemerisGenerator]
    PythonFieldPropagator: typing.Type[PythonFieldPropagator]
    PythonPropagator: typing.Type[PythonPropagator]
    SpacecraftState: typing.Type[SpacecraftState]
    analytical: org.orekit.propagation.analytical.__module_protocol__
    conversion: org.orekit.propagation.conversion.__module_protocol__
    events: org.orekit.propagation.events.__module_protocol__
    integration: org.orekit.propagation.integration.__module_protocol__
    numerical: org.orekit.propagation.numerical.__module_protocol__
    sampling: org.orekit.propagation.sampling.__module_protocol__
    semianalytical: org.orekit.propagation.semianalytical.__module_protocol__
