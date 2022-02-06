import org.orekit.attitudes
import org.orekit.data
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.analytical.gnss.data
import org.orekit.time
import org.orekit.utils
import typing



class ClockCorrectionsProvider(org.orekit.propagation.AdditionalStateProvider):
    """
    public class ClockCorrectionsProvider extends Object implements :class:`~org.orekit.propagation.AdditionalStateProvider`
    
        Provider for clock corrections as additional states.
    
        The value of this additional state is a three elements array containing
    
          - at index 0, the polynomial satellite clock model ÃŽâ€�tÃ¢â€šâ€ºÃ¢â€šï¿½Ã¢â€šÅ“ =
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf0` +
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1` (t -
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getToc`) +
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getAf1` (t -
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getToc`)Ã‚Â²
          - at index 1 the relativistic clock correction due to eccentricity
          - at index 2 the estimated group delay differential
            :meth:`~org.orekit.propagation.analytical.gnss.data.GNSSClockElements.getTGD` for L1-L2 correction
    
    
        Since Orekit 10.3 the relativistic clock correction can be used as an
        :class:`~org.orekit.estimation.measurements.EstimationModifier` in orbit determination applications to take into
        consideration this effect in measurement modeling.
    
    
        Since:
            9.3
    """
    CLOCK_CORRECTIONS: typing.ClassVar[str] = ...
    """
    public static final String CLOCK_CORRECTIONS
    
        Name of the additional state for satellite clock corrections.
    
        Since:
            9.3
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, gNSSClockElements: org.orekit.propagation.analytical.gnss.data.GNSSClockElements): ...
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

class GLONASSAnalyticalPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    """
    public class GLONASSAnalyticalPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        This class aims at propagating a GLONASS orbit from
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements`.
    
        Since:
            10.0
    
        Also see:
            ` GLONASS Interface Control Document
            <http://russianspacesystems.ru/wp-content/uploads/2016/08/ICD-GLONASS-CDMA-General.-Edition-1.0-2016.pdf>`
    """
    def getECEF(self) -> org.orekit.frames.Frame:
        """
            Gets the Earth Centered Earth Fixed frame used to propagate GLONASS orbits.
        
            Returns:
                the ECEF frame
        
        
        """
        ...
    def getECI(self) -> org.orekit.frames.Frame:
        """
            Gets the Earth Centered Inertial frame used to propagate the orbit.
        
            Returns:
                the ECI frame
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
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
    def getGLONASSOrbitalElements(self) -> org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements:
        """
            Gets the underlying GLONASS orbital elements.
        
            Returns:
                the underlying GLONASS orbital elements
        
        
        """
        ...
    @staticmethod
    def getMU() -> float:
        """
            Get the Earth gravity coefficient used for GLONASS propagation.
        
            Returns:
                the Earth gravity coefficient.
        
        
        """
        ...
    def propagateInEcef(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
            Gets the PVCoordinates of the GLONASS SV in
            :meth:`~org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator.getECEF`.
        
            The algorithm is defined at Appendix M.1 from GLONASS Interface Control Document, with automatic differentiation added
            to compute velocity and acceleration.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the computation date
        
            Returns:
                the GLONASS SV PVCoordinates in :meth:`~org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagator.getECEF`
        
        
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

class GLONASSAnalyticalPropagatorBuilder:
    """
    public class GLONASSAnalyticalPropagatorBuilder extends Object
    
        This nested class aims at building a GLONASSAnalyticalPropagator.
    
        It implements the classical builder pattern.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, gLONASSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements): ...
    @typing.overload
    def __init__(self, gLONASSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, dataContext: org.orekit.data.DataContext): ...
    def attitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> 'GLONASSAnalyticalPropagatorBuilder':
        """
            Sets the attitude provider.
        
            Parameters:
                userProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the attitude provider
        
            Returns:
                the updated builder
        
        
        """
        ...
    def build(self) -> GLONASSAnalyticalPropagator:
        """
            Finalizes the build.
        
            Returns:
                the built GLONASSPropagator
        
        
        """
        ...
    def dataContext(self, dataContext: org.orekit.data.DataContext) -> 'GLONASSAnalyticalPropagatorBuilder':
        """
            Sets the data context used by the propagator. Does not update the ECI or ECEF frames which must be done separately using
            :meth:`~org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagatorBuilder.eci` and
            :meth:`~org.orekit.propagation.analytical.gnss.GLONASSAnalyticalPropagatorBuilder.ecef`.
        
            Parameters:
                context (:class:`~org.orekit.data.DataContext`): used for propagation.
        
            Returns:
                the updated builder.
        
        
        """
        ...
    def ecef(self, frame: org.orekit.frames.Frame) -> 'GLONASSAnalyticalPropagatorBuilder':
        """
            Sets the Earth Centered Earth Fixed frame assimilated to the WGS84 ECEF.
        
            Parameters:
                bodyFixed (:class:`~org.orekit.frames.Frame`): the ECEF frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def eci(self, frame: org.orekit.frames.Frame) -> 'GLONASSAnalyticalPropagatorBuilder':
        """
            Sets the Earth Centered Inertial frame used for propagation.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): the ECI frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def mass(self, double: float) -> 'GLONASSAnalyticalPropagatorBuilder':
        """
            Sets the mass.
        
            Parameters:
                userMass (double): the mass (in kg)
        
            Returns:
                the updated builder
        
        
        """
        ...

class GNSSPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    """
    public class GNSSPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        Common handling of :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator` methods for GNSS
        propagators.
    
        This class allows to provide easily a subset of :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
        methods for specific GNSS propagators.
    """
    def getECEF(self) -> org.orekit.frames.Frame:
        """
            Gets the Earth Centered Earth Fixed frame used to propagate GNSS orbits according to the Interface Control Document.
        
            Returns:
                the ECEF frame
        
        
        """
        ...
    def getECI(self) -> org.orekit.frames.Frame:
        """
            Gets the Earth Centered Inertial frame used to propagate the orbit.
        
            Returns:
                the ECI frame
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
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
    def getMU(self) -> float:
        """
            Gets the Earth gravity coefficient used for GNSS propagation.
        
            Returns:
                the Earth gravity coefficient.
        
        
        """
        ...
    def getOrbitalElements(self) -> org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements:
        """
            Get the underlying GNSS orbital elements.
        
            Returns:
                the underlying GNSS orbital elements
        
        
        """
        ...
    def propagateInEcef(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
            Gets the PVCoordinates of the GNSS SV in :meth:`~org.orekit.propagation.analytical.gnss.GNSSPropagator.getECEF`.
        
            The algorithm uses automatic differentiation to compute velocity and acceleration.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the computation date
        
            Returns:
                the GNSS SV PVCoordinates in :meth:`~org.orekit.propagation.analytical.gnss.GNSSPropagator.getECEF`
        
        
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

class GNSSPropagatorBuilder:
    """
    public class GNSSPropagatorBuilder extends Object
    
        This nested class aims at building a GNSSPropagator.
    
        It implements the classical builder pattern.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, gNSSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements): ...
    @typing.overload
    def __init__(self, gNSSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GNSSOrbitalElements, frames: org.orekit.frames.Frames): ...
    def attitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> 'GNSSPropagatorBuilder':
        """
            Sets the attitude provider.
        
            Parameters:
                userProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the attitude provider
        
            Returns:
                the updated builder
        
        
        """
        ...
    def build(self) -> GNSSPropagator:
        """
            Finalizes the build.
        
            Returns:
                the built GNSSPropagator
        
        
        """
        ...
    def ecef(self, frame: org.orekit.frames.Frame) -> 'GNSSPropagatorBuilder':
        """
            Sets the Earth Centered Earth Fixed frame assimilated to the WGS84 ECEF.
        
            Parameters:
                bodyFixed (:class:`~org.orekit.frames.Frame`): the ECEF frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def eci(self, frame: org.orekit.frames.Frame) -> 'GNSSPropagatorBuilder':
        """
            Sets the Earth Centered Inertial frame used for propagation.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): the ECI frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def mass(self, double: float) -> 'GNSSPropagatorBuilder':
        """
            Sets the mass.
        
            Parameters:
                userMass (double): the mass (in kg)
        
            Returns:
                the updated builder
        
        
        """
        ...

class SBASPropagator(org.orekit.propagation.analytical.AbstractAnalyticalPropagator):
    """
    public class SBASPropagator extends :class:`~org.orekit.propagation.analytical.AbstractAnalyticalPropagator`
    
        This class aims at propagating a SBAS orbit from
        :class:`~org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements`.
    
        Since:
            10.1
    
        Also see:
            "Tyler Reid, Todd Walker, Per Enge, L1/L5 SBAS MOPS Ephemeris Message to Support Multiple Orbit Classes, ION ITM, 2013"
    """
    def getECEF(self) -> org.orekit.frames.Frame:
        """
            Gets the Earth Centered Earth Fixed frame used to propagate GNSS orbits.
        
            Returns:
                the ECEF frame
        
        
        """
        ...
    def getECI(self) -> org.orekit.frames.Frame:
        """
            Gets the Earth Centered Inertial frame used to propagate the orbit.
        
            Returns:
                the ECI frame
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
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
    def getMU(self) -> float:
        """
            Get the Earth gravity coefficient used for SBAS propagation.
        
            Returns:
                the Earth gravity coefficient.
        
        
        """
        ...
    def getSBASOrbitalElements(self) -> org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements:
        """
            Get the underlying SBAS orbital elements.
        
            Returns:
                the underlying SBAS orbital elements
        
        
        """
        ...
    def propagateInEcef(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.PVCoordinates:
        """
            Gets the PVCoordinates of the GNSS SV in :meth:`~org.orekit.propagation.analytical.gnss.SBASPropagator.getECEF`.
        
            The algorithm uses automatic differentiation to compute velocity and acceleration.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): the computation date
        
            Returns:
                the GNSS SV PVCoordinates in :meth:`~org.orekit.propagation.analytical.gnss.SBASPropagator.getECEF`
        
        
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

class SBASPropagatorBuilder:
    """
    public class SBASPropagatorBuilder extends Object
    
        This nested class aims at building a SBASPropagator.
    
        It implements the classical builder pattern.
    
        Since:
            11.0
    """
    def __init__(self, sBASOrbitalElements: org.orekit.propagation.analytical.gnss.data.SBASOrbitalElements, frames: org.orekit.frames.Frames): ...
    def attitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> 'SBASPropagatorBuilder':
        """
            Sets the attitude provider.
        
            Parameters:
                userProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the attitude provider
        
            Returns:
                the updated builder
        
        
        """
        ...
    def build(self) -> SBASPropagator:
        """
            Finalizes the build.
        
            Returns:
                the built SBASPropagator
        
        
        """
        ...
    def ecef(self, frame: org.orekit.frames.Frame) -> 'SBASPropagatorBuilder':
        """
            Sets the Earth Centered Earth Fixed frame assimilated to the WGS84 ECEF.
        
            Parameters:
                bodyFixed (:class:`~org.orekit.frames.Frame`): the ECEF frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def eci(self, frame: org.orekit.frames.Frame) -> 'SBASPropagatorBuilder':
        """
            Sets the Earth Centered Inertial frame used for propagation.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): the ECI frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def mass(self, double: float) -> 'SBASPropagatorBuilder':
        """
            Sets the mass.
        
            Parameters:
                userMass (double): the mass (in kg)
        
            Returns:
                the updated builder
        
        
        """
        ...
    def mu(self, double: float) -> 'SBASPropagatorBuilder':
        """
            Sets the Earth gravity coefficient.
        
            Parameters:
                coefficient (double): the Earth gravity coefficient
        
            Returns:
                the updated builder
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.gnss")``.

    ClockCorrectionsProvider: typing.Type[ClockCorrectionsProvider]
    GLONASSAnalyticalPropagator: typing.Type[GLONASSAnalyticalPropagator]
    GLONASSAnalyticalPropagatorBuilder: typing.Type[GLONASSAnalyticalPropagatorBuilder]
    GNSSPropagator: typing.Type[GNSSPropagator]
    GNSSPropagatorBuilder: typing.Type[GNSSPropagatorBuilder]
    SBASPropagator: typing.Type[SBASPropagator]
    SBASPropagatorBuilder: typing.Type[SBASPropagatorBuilder]
    data: org.orekit.propagation.analytical.gnss.data.__module_protocol__
