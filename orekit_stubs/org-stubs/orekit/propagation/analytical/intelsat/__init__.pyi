
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
    public class FieldIntelsatElevenElements<T extends :class:`~org.orekit.propagation.analytical.intelsat.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.intelsat.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class is a container for a single set of Intelsat's 11 Elements data.
    
        Intelsat's 11 elements are defined in ITU-R S.1525 standard.
    
        Since:
            12.1
    """
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElements__T], t: _FieldIntelsatElevenElements__T, t2: _FieldIntelsatElevenElements__T, t3: _FieldIntelsatElevenElements__T, t4: _FieldIntelsatElevenElements__T, t5: _FieldIntelsatElevenElements__T, t6: _FieldIntelsatElevenElements__T, t7: _FieldIntelsatElevenElements__T, t8: _FieldIntelsatElevenElements__T, t9: _FieldIntelsatElevenElements__T, t10: _FieldIntelsatElevenElements__T, t11: _FieldIntelsatElevenElements__T): ...
    def getEpoch(self) -> org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElements__T]: ...
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
    public class FieldIntelsatElevenElementsPropagator<T extends :class:`~org.orekit.propagation.analytical.intelsat.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.analytical.FieldAbstractAnalyticalPropagator`<T>
    
        This class provides elements to propagate Intelsat's 11 elements.
    
        Intelsat's 11 elements propagation is defined in ITU-R S.1525 standard.
    
        Since:
            12.1
    """
    @typing.overload
    def __init__(self, fieldIntelsatElevenElements: FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T]): ...
    @typing.overload
    def __init__(self, fieldIntelsatElevenElements: FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T], frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, fieldIntelsatElevenElements: FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T], frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, attitudeProvider: org.orekit.attitudes.AttitudeProvider, t: _FieldIntelsatElevenElementsPropagator__T): ...
    def getEastLongitudeDegrees(self) -> org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldIntelsatElevenElementsPropagator__T]: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
            .
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.getFrame` in interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.FieldAbstractPropagator.getFrame` in
                class :class:`~org.orekit.propagation.FieldAbstractPropagator`
        
            Returns:
                frame in which the orbit is propagated
        
            Also see:
                :meth:`~org.orekit.propagation.FieldPropagator.resetInitialState`
        
        
        """
        ...
    def getGeocentricLatitudeDegrees(self) -> org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldIntelsatElevenElementsPropagator__T]: ...
    def getIntelsatElevenElements(self) -> FieldIntelsatElevenElements[_FieldIntelsatElevenElementsPropagator__T]: ...
    def getOrbitRadius(self) -> org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_FieldIntelsatElevenElementsPropagator__T]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def propagateInEcef(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElementsPropagator__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldIntelsatElevenElementsPropagator__T]: ...
    def propagateOrbit(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldIntelsatElevenElementsPropagator__T], tArray: typing.Union[typing.List[_FieldIntelsatElevenElementsPropagator__T], jpype.JArray]) -> org.orekit.orbits.FieldOrbit[_FieldIntelsatElevenElementsPropagator__T]: ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldIntelsatElevenElementsPropagator__T]) -> None: ...

class IntelsatElevenElements:
    """
    public class IntelsatElevenElements extends :class:`~org.orekit.propagation.analytical.intelsat.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class is a container for a single set of Intelsat's 11 Elements data.
    
        Intelsat's 11 elements are defined in ITU-R S.1525 standard.
    
        Since:
            12.1
    """
    SYNCHRONOUS_RADIUS_KM: typing.ClassVar[float] = ...
    """
    public static final double SYNCHRONOUS_RADIUS_KM
    
        Sun synchronous radius in kilometers.
    
        Also see:
            :meth:`~constant`
    
    
    """
    K: typing.ClassVar[float] = ...
    """
    public static final double K
    
        PI over 360.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DRIFT_RATE_SHIFT_DEG_PER_DAY: typing.ClassVar[float] = ...
    """
    public static final double DRIFT_RATE_SHIFT_DEG_PER_DAY
    
        Longitude drift rate.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float): ...
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
    public class IntelsatElevenElementsPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        This class provides elements to propagate Intelsat's 11 elements.
    
        Intelsat's 11 elements propagation is defined in ITU-R S.1525 standard.
    
        Since:
            12.1
    """
    @typing.overload
    def __init__(self, intelsatElevenElements: IntelsatElevenElements): ...
    @typing.overload
    def __init__(self, intelsatElevenElements: IntelsatElevenElements, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, intelsatElevenElements: IntelsatElevenElements, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float): ...
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
        
            The propagation frame is the definition frame of the initial state, so this method should be called after this state has
            been set, otherwise it may return null.
            .
        
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
    def propagateInEcef(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
            Converts the Intelsat's 11 elements into Position/Velocity coordinates in ECEF.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): computation epoch
        
            Returns:
                Position/Velocity coordinates in ECEF
        
        
        """
        ...
    def propagateOrbit(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.orbits.Orbit:
        """
            Extrapolate an orbit up to a specific target date..
        
            Specified by:
                :meth:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator.propagateOrbit` in
                class :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date for the orbit
        
            Returns:
                extrapolated parameters
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state..
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.intelsat")``.

    FieldIntelsatElevenElements: typing.Type[FieldIntelsatElevenElements]
    FieldIntelsatElevenElementsPropagator: typing.Type[FieldIntelsatElevenElementsPropagator]
    IntelsatElevenElements: typing.Type[IntelsatElevenElements]
    IntelsatElevenElementsPropagator: typing.Type[IntelsatElevenElementsPropagator]
