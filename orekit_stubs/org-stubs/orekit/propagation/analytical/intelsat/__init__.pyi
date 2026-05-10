
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.orekit.attitudes
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.time
import org.orekit.utils
import typing



_FieldIntelsatElevenElements__T = typing.TypeVar('_FieldIntelsatElevenElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldIntelsatElevenElements(typing.Generic[_FieldIntelsatElevenElements__T]):
    """
    This class is a container for a single set of Intelsat's 11 Elements data.
    
    Intelsat's 11 elements are defined in ITU-R S.1525 standard.
    
    Since:
        12.1
    """
    def __init__(self, epoch: org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElements__T], lm0: _FieldIntelsatElevenElements__T, lm1: _FieldIntelsatElevenElements__T, lm2: _FieldIntelsatElevenElements__T, lonC: _FieldIntelsatElevenElements__T, lonC1: _FieldIntelsatElevenElements__T, lonS: _FieldIntelsatElevenElements__T, lonS1: _FieldIntelsatElevenElements__T, latC: _FieldIntelsatElevenElements__T, latC1: _FieldIntelsatElevenElements__T, latS: _FieldIntelsatElevenElements__T, latS1: _FieldIntelsatElevenElements__T):
        """
        Constructor.
        
        Parameters:
            epoch (FieldAbsoluteDate<FieldIntelsatElevenElements> epoch): elements epoch
            lm0 (FieldIntelsatElevenElements): mean longitude (East of Greenwich) in degrees
            lm1 (FieldIntelsatElevenElements): drift rate in degrees/day
            lm2 (FieldIntelsatElevenElements): drift acceleration in degrees/day/day
            lonC (FieldIntelsatElevenElements): longitude oscillation-amplitude for the cosine term in degrees
            lonC1 (FieldIntelsatElevenElements): rate of change of longitude, for the cosine term, in degrees/day
            lonS (FieldIntelsatElevenElements): longitude oscillation-amplitude for the sine term in degrees
            lonS1 (FieldIntelsatElevenElements): rate of change of longitude, for the sine term, in degrees/day
            latC (FieldIntelsatElevenElements): latitude oscillation-amplitude for the cosine term in degrees
            latC1 (FieldIntelsatElevenElements): rate of change of latitude, for the cosine term, in degrees/day
            latS (FieldIntelsatElevenElements): latitude oscillation-amplitude for the sine term in degrees
            latS1 (FieldIntelsatElevenElements): rate of change of latitude, for the sine term, in degrees/day
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElements__T]:
        """
        Get the elements epoch.
        
        Returns:
            elements epoch
        
        
        """
        ...
    def getLatC(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the latitude oscillation-amplitude for the cosine term.
        
        Returns:
            the latitude oscillation-amplitude for the cosine term in degrees
        
        
        """
        ...
    def getLatC1(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the rate of change of latitude, for the cosine term.
        
        Returns:
            the rate of change of latitude, for the cosine term, in degrees/day
        
        
        """
        ...
    def getLatS(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the latitude oscillation-amplitude for the sine term.
        
        Returns:
            the latitude oscillation-amplitude for the sine term in degrees
        
        
        """
        ...
    def getLatS1(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the rate of change of latitude, for the sine term.
        
        Returns:
            the rate of change of latitude, for the sine term, in degrees/day
        
        
        """
        ...
    def getLm0(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the mean longitude (East of Greenwich).
        
        Returns:
            the mean longitude (East of Greenwich) in degrees
        
        
        """
        ...
    def getLm1(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the drift rate.
        
        Returns:
            the drift rate in degrees/day
        
        
        """
        ...
    def getLm2(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the drift acceleration.
        
        Returns:
            the drift acceleration in degrees/day/day
        
        
        """
        ...
    def getLonC(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the longitude oscillation-amplitude for the cosine term.
        
        Returns:
            the longitude oscillation-amplitude for the cosine term in degrees
        
        
        """
        ...
    def getLonC1(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the rate of change of longitude, for the cosine term.
        
        Returns:
            the rate of change of longitude, for the cosine term, in degrees/day
        
        
        """
        ...
    def getLonS(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the longitude oscillation-amplitude for the sine term.
        
        Returns:
            the longitude oscillation-amplitude for the sine term in degrees
        
        
        """
        ...
    def getLonS1(self) -> _FieldIntelsatElevenElements__T:
        """
        Get the rate of change of longitude, for the sine term.
        
        Returns:
            the rate of change of longitude, for the sine term, in degrees/day
        
        
        """
        ...

_FieldIntelsatElevenElementsPropagator__T = typing.TypeVar('_FieldIntelsatElevenElementsPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldIntelsatElevenElementsPropagator(org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator[_FieldIntelsatElevenElementsPropagator__T], typing.Generic[_FieldIntelsatElevenElementsPropagator__T]):
    """
    This class provides elements to propagate Intelsat's 11 elements.
    
    Intelsat's 11 elements propagation is defined in ITU-R S.1525 standard.
    
    Since:
        12.1
    """
    @typing.overload
    def __init__(self, elements: FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T]): ...
    @typing.overload
    def __init__(self, elements: FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T], inertialFrame: org.orekit.frames.Frame, ecefFrame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, elements: FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T], inertialFrame: org.orekit.frames.Frame, ecefFrame: org.orekit.frames.Frame, attitudeProvider: org.orekit.attitudes.AttitudeProvider, mass: _FieldIntelsatElevenElementsPropagator__T): ...
    def getEastLongitudeDegrees(self) -> org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldIntelsatElevenElementsPropagator__T]:
        """
        Get the computed satellite's east longitude.
        
        Returns:
            the satellite's east longitude in degrees
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null. .
        
        Specified by: getFrame in interface FieldPropagator
        
        Overrides: getFrame in class FieldAbstractPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getGeocentricLatitudeDegrees(self) -> org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldIntelsatElevenElementsPropagator__T]:
        """
        Get the computed satellite's geocentric latitude.
        
        Returns:
            the satellite's geocentric latitude in degrees
        
        
        """
        ...
    def getIntelsatElevenElements(self) -> FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T]:
        """
        Get the Intelsat's 11 elements used by the propagator.
        
        Returns:
            the Intelsat's 11 elements used by the propagator
        
        
        """
        ...
    def getOrbitRadius(self) -> org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldIntelsatElevenElementsPropagator__T]:
        """
        Get the computed satellite's orbit.
        
        Returns:
            satellite's orbit radius in meters
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters..
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def propagateInEcef(self, date: org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElementsPropagator__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldIntelsatElevenElementsPropagator__T]:
        """
        Converts the Intelsat's 11 elements into Position/Velocity coordinates in ECEF.
        
        Parameters:
            date (FieldAbsoluteDate<FieldIntelsatElevenElementsPropagator> date): computation epoch
        
        Returns:
            Position/Velocity coordinates in ECEF
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElementsPropagator__T], parameters: typing.Union[typing.List[_FieldIntelsatElevenElementsPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_FieldIntelsatElevenElementsPropagator__T]:
        """
        Propagate an orbit up to a specific target date..
        
        Specified by: propagateOrbit in class FieldAbstractAnalyticalPropagator
        
        Parameters:
            date (FieldAbsoluteDate<FieldIntelsatElevenElementsPropagator> date): target date for the orbit
            parameters (FieldIntelsatElevenElementsPropagator[]): model parameters
        
        Returns:
            propagated orbit
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldIntelsatElevenElementsPropagator__T]) -> None:
        """
        Reset the propagator initial state..
        
        Specified by: resetInitialState in interface FieldPropagator
        
        Overrides: resetInitialState in class FieldAbstractPropagator
        
        Parameters:
            state (FieldSpacecraftState<FieldIntelsatElevenElementsPropagator> state): new initial state to consider
        
        
        """
        ...

class IntelsatElevenElements:
    """
    This class is a container for a single set of Intelsat's 11 Elements data.
    
    Intelsat's 11 elements are defined in ITU-R S.1525 standard.
    
    Since:
        12.1
    """
    SYNCHRONOUS_RADIUS_KM: typing.ClassVar[float] = ...
    """
    Sun synchronous radius in kilometers.
    
    Also see:
        constant
    
    
    """
    K: typing.ClassVar[float] = ...
    """
    PI over 360.
    
    Also see:
        constant
    
    
    """
    DRIFT_RATE_SHIFT_DEG_PER_DAY: typing.ClassVar[float] = ...
    """
    Longitude drift rate.
    
    Also see:
        constant
    
    
    """
    def __init__(self, epoch: org.orekit.time.AbsoluteDate, lm0: float, lm1: float, lm2: float, lonC: float, lonC1: float, lonS: float, lonS1: float, latC: float, latC1: float, latS: float, latS1: float):
        """
        Constructor.
        
        Parameters:
            epoch (AbsoluteDate): elements epoch
            lm0 (double): mean longitude (East of Greenwich) in degrees
            lm1 (double): drift rate in degrees/day
            lm2 (double): drift acceleration in degrees/day/day
            lonC (double): longitude oscillation-amplitude for the cosine term in degrees
            lonC1 (double): rate of change of longitude, for the cosine term, in degrees/day
            lonS (double): longitude oscillation-amplitude for the sine term in degrees
            lonS1 (double): rate of change of longitude, for the sine term, in degrees/day
            latC (double): latitude oscillation-amplitude for the cosine term in degrees
            latC1 (double): rate of change of latitude, for the cosine term, in degrees/day
            latS (double): latitude oscillation-amplitude for the sine term in degrees
            latS1 (double): rate of change of latitude, for the sine term, in degrees/day
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the elements epoch.
        
        Returns:
            elements epoch
        
        
        """
        ...
    def getLatC(self) -> float:
        """
        Get the latitude oscillation-amplitude for the cosine term.
        
        Returns:
            the latitude oscillation-amplitude for the cosine term in degrees
        
        
        """
        ...
    def getLatC1(self) -> float:
        """
        Get the rate of change of latitude, for the cosine term.
        
        Returns:
            the rate of change of latitude, for the cosine term, in degrees/day
        
        
        """
        ...
    def getLatS(self) -> float:
        """
        Get the latitude oscillation-amplitude for the sine term.
        
        Returns:
            the latitude oscillation-amplitude for the sine term in degrees
        
        
        """
        ...
    def getLatS1(self) -> float:
        """
        Get the rate of change of latitude, for the sine term.
        
        Returns:
            the rate of change of latitude, for the sine term, in degrees/day
        
        
        """
        ...
    def getLm0(self) -> float:
        """
        Get the mean longitude (East of Greenwich).
        
        Returns:
            the mean longitude (East of Greenwich) in degrees
        
        
        """
        ...
    def getLm1(self) -> float:
        """
        Get the drift rate.
        
        Returns:
            the drift rate in degrees/day
        
        
        """
        ...
    def getLm2(self) -> float:
        """
        Get the drift acceleration.
        
        Returns:
            the drift acceleration in degrees/day/day
        
        
        """
        ...
    def getLonC(self) -> float:
        """
        Get the longitude oscillation-amplitude for the cosine term.
        
        Returns:
            the longitude oscillation-amplitude for the cosine term in degrees
        
        
        """
        ...
    def getLonC1(self) -> float:
        """
        Get the rate of change of longitude, for the cosine term.
        
        Returns:
            the rate of change of longitude, for the cosine term, in degrees/day
        
        
        """
        ...
    def getLonS(self) -> float:
        """
        Get the longitude oscillation-amplitude for the sine term.
        
        Returns:
            the longitude oscillation-amplitude for the sine term in degrees
        
        
        """
        ...
    def getLonS1(self) -> float:
        """
        Get the rate of change of longitude, for the sine term.
        
        Returns:
            the rate of change of longitude, for the sine term, in degrees/day
        
        
        """
        ...

class IntelsatElevenElementsPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    """
    This class provides elements to propagate Intelsat's 11 elements.
    
    Intelsat's 11 elements propagation is defined in ITU-R S.1525 standard.
    
    Since:
        12.1
    """
    @typing.overload
    def __init__(self, elements: IntelsatElevenElements): ...
    @typing.overload
    def __init__(self, elements: IntelsatElevenElements, inertialFrame: org.orekit.frames.Frame, ecefFrame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, elements: IntelsatElevenElements, inertialFrame: org.orekit.frames.Frame, ecefFrame: org.orekit.frames.Frame, attitudeProvider: org.orekit.attitudes.AttitudeProvider, mass: float): ...
    def getEastLongitudeDegrees(self) -> org.hipparchus.analysis.differentiation.UnivariateDerivative2:
        """
        Get the computed satellite's east longitude.
        
        Returns:
            the satellite's east longitude in degrees
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        The propagation frame is the definition frame of the initial state, so this method should be called after this state has been set, otherwise it may return null. .
        
        Specified by: getFrame in interface Propagator
        
        Overrides: getFrame in class AbstractPropagator
        
        Returns:
            frame in which the orbit is propagated
        
        Also see:
            resetInitialState
        
        
        """
        ...
    def getGeocentricLatitudeDegrees(self) -> org.hipparchus.analysis.differentiation.UnivariateDerivative2:
        """
        Get the computed satellite's geocentric latitude.
        
        Returns:
            the satellite's geocentric latitude in degrees
        
        
        """
        ...
    def getIntelsatElevenElements(self) -> IntelsatElevenElements:
        """
        Get the Intelsat's 11 elements used by the propagator.
        
        Returns:
            the Intelsat's 11 elements used by the propagator
        
        
        """
        ...
    def getOrbitRadius(self) -> org.hipparchus.analysis.differentiation.UnivariateDerivative2:
        """
        Get the computed satellite's orbit.
        
        Returns:
            satellite's orbit radius in meters
        
        
        """
        ...
    def propagateInEcef(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
        Converts the Intelsat's 11 elements into Position/Velocity coordinates in ECEF.
        
        Parameters:
            date (AbsoluteDate): computation epoch
        
        Returns:
            Position/Velocity coordinates in ECEF
        
        
        """
        ...
    def propagateOrbit(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
        Extrapolate an orbit up to a specific target date..
        
        Specified by: propagateOrbit in class AbstractAnalyticalPropagator
        
        Parameters:
            date (AbsoluteDate): target date for the orbit
        
        Returns:
            extrapolated parameters
        
        
        """
        ...
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the propagator initial state..
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.intelsat")``.

    FieldIntelsatElevenElements: typing.Type[FieldIntelsatElevenElements]
    FieldIntelsatElevenElementsPropagator: typing.Type[FieldIntelsatElevenElementsPropagator]
    IntelsatElevenElements: typing.Type[IntelsatElevenElements]
    IntelsatElevenElementsPropagator: typing.Type[IntelsatElevenElementsPropagator]
