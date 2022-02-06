import java.util
import org.hipparchus.analysis
import org.hipparchus.ode
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.attitudes
import org.orekit.data
import org.orekit.estimation.leastsquares
import org.orekit.estimation.measurements
import org.orekit.estimation.sequential
import org.orekit.forces
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.propagation.semianalytical.dsst
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.time
import org.orekit.utils
import typing



class ODEIntegratorBuilder:
    """
    public interface ODEIntegratorBuilder
    
        This interface is the top-level abstraction to build first order integrators for propagators conversion.
    
        Since:
            6.0
    """
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class OsculatingToMeanElementsConverter:
    """
    public class OsculatingToMeanElementsConverter extends Object
    
        This class converts osculating orbital elements into mean elements.
    
        As this process depends on the force models used to average the orbit, a :class:`~org.orekit.propagation.Propagator` is
        given as input. The force models used will be those contained into the propagator. This propagator *must* support its
        initial state to be reset, and this initial state *must* represent some mean value. This implies that this method will
        not work with :class:`~org.orekit.propagation.analytical.tle.TLEPropagator` because their initial state cannot be reset,
        and it won't work either with :class:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator` as their initial
        state is osculating and not mean. As of 6.0, this works mainly for
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    """
    def __init__(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int, propagator: org.orekit.propagation.Propagator, double: float): ...
    def convert(self) -> org.orekit.propagation.SpacecraftState:
        """
            Convert an osculating orbit into a mean orbit, in DSST sense.
        
            Returns:
                mean orbit state, in DSST sense
        
        
        """
        ...

class PropagatorBuilder:
    """
    public interface PropagatorBuilder
    
        This interface is the top-level abstraction to build propagators for conversion.
    
        Since:
            6.0
    """
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            Returns:
                frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the initial orbit.
        
            Returns:
                date of the initial orbit
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type expected for the 6 first parameters in null.
        
            Returns:
                orbit type to use in null
        
            Since:
                7.1
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters.
        
            Returns:
                drivers for the configurable orbital parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle:
        """
            Get the position angle type expected for the 6 first parameters in null.
        
            Returns:
                position angle type to use in null
        
            Since:
                7.1
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`
        
        
        """
        ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable propagation parameters.
        
            The parameters typically correspond to force models.
        
            Returns:
                drivers for the configurable propagation parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]:
        """
            Get the current value of selected normalized parameters.
        
            Returns:
                current value of selected normalized parameters
        
        
        """
        ...

class PropagatorConverter:
    """
    public interface PropagatorConverter
    
        This interface is the top-level abstraction for propagators conversions.
    
        It provides a way to convert a given propagator or a set of :class:`~org.orekit.propagation.SpacecraftState` into a
        wanted propagator that minimize the mean square error over a time span.
    
        Since:
            6.0
    """
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator:
        """
            Convert a propagator into another one.
        
            Parameters:
                source (:class:`~org.orekit.propagation.Propagator`): propagator to convert
                timeSpan (double): time span considered for conversion
                nbPoints (int): number of points for sampling over the time span
                freeParameters (List<String> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
            Convert a propagator into another one.
        
            Parameters:
                source (:class:`~org.orekit.propagation.Propagator`): propagator to convert
                timeSpan (double): time span considered for conversion
                nbPoints (int): number of points for sampling over the time span
                freeParameters (String...): names of the free parameters
        
            Returns:
                adapted propagator
        
        :class:`~org.orekit.propagation.Propagator` convert(List<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, List<String> freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Parameters:
                states (List<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (List<String> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
        :class:`~org.orekit.propagation.Propagator` convert(List<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, String... freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Parameters:
                states (List<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (String...): names of the free parameters
        
            Returns:
                adapted propagator
        
        
        """
        ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator: ...

class AbstractPropagatorBuilder(PropagatorBuilder):
    """
    public abstract class AbstractPropagatorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
    
        Base class for propagator builders.
    
        Since:
            7.1
    """
    def addAdditionalDerivativesProvider(self, additionalDerivativesProvider: org.orekit.propagation.integration.AdditionalDerivativesProvider) -> None:
        """
            Add a set of user-specified equations to be integrated along with the orbit propagation (author Shiva Iyer).
        
            Parameters:
                provider (:class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`): provider for additional derivatives
        
            Since:
                11.1
        
        
        """
        ...
    def addAdditionalEquations(self, additionalEquations: org.orekit.propagation.integration.AdditionalEquations) -> None: ...
    def deselectDynamicParameters(self) -> None:
        """
            Deselects orbital and propagation drivers.
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Get the attitude provider.
        
            Returns:
                the attitude provider
        
            Since:
                10.1
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getFrame`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the initial orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getInitialOrbitDate`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                date of the initial orbit
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient (Âµ - mÂ³/sÂ²) value.
        
            Returns:
                the central attraction coefficient (Âµ - mÂ³/sÂ²) value
        
            Since:
                9.2
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type expected for the 6 first parameters in null.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                orbit type to use in null
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable orbital parameters
        
        
        """
        ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle:
        """
            Get the position angle type expected for the 6 first parameters in null.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                position angle type to use in null
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`
        
        
        """
        ...
    def getPositionScale(self) -> float:
        """
            Get the position scale.
        
            Returns:
                the position scale used to scale the orbital drivers
        
        
        """
        ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable propagation parameters.
        
            The parameters typically correspond to force models.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable propagation parameters
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]:
        """
            Get the current value of selected normalized parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getSelectedNormalizedParameters`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                current value of selected normalized parameters
        
        
        """
        ...
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None:
        """
            Reset the orbit in the propagator builder.
        
            Parameters:
                newOrbit (:class:`~org.orekit.orbits.Orbit`): New orbit to set in the propagator builder
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set the attitude provider.
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
            Since:
                10.1
        
        
        """
        ...

class AbstractPropagatorConverter(PropagatorConverter):
    """
    public abstract class AbstractPropagatorConverter extends Object implements :class:`~org.orekit.propagation.conversion.PropagatorConverter`
    
        Common handling of :class:`~org.orekit.propagation.conversion.PropagatorConverter` methods for propagators conversions.
    
        This abstract class factors the common code for propagators conversion. Only one method must be implemented by derived
        classes: :meth:`~org.orekit.propagation.conversion.AbstractPropagatorConverter.getObjectiveFunction`.
    
        The converter uses the LevenbergMarquardtOptimizer from the Hipparchus library. Different implementations correspond to
        different methods for computing the Jacobian.
    
        Since:
            6.0
    """
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    def getAdaptedPropagator(self) -> org.orekit.propagation.Propagator:
        """
            Get the adapted propagator.
        
            Returns:
                adapted propagator
        
        
        """
        ...
    def getEvaluations(self) -> int:
        """
            Get the number of objective function evaluations.
        
            Returns:
                the number of objective function evaluations.
        
        
        """
        ...
    def getRMS(self) -> float:
        """
            Get the Root Mean Square Deviation of the fitting.
        
            Returns:
                RMSD
        
        
        """
        ...

class AdamsBashforthIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class AdamsBashforthIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for AdamsBashforthIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class AdamsMoultonIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class AdamsMoultonIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for AdamsMoultonIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class ClassicalRungeKuttaIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class ClassicalRungeKuttaIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for ClassicalRungeKuttaIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class DormandPrince54IntegratorBuilder(ODEIntegratorBuilder):
    """
    public class DormandPrince54IntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for DormandPrince54Integrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class DormandPrince853IntegratorBuilder(ODEIntegratorBuilder):
    """
    public class DormandPrince853IntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for DormandPrince853Integrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class EulerIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class EulerIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for EulerIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class GillIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class GillIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for GillIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class GraggBulirschStoerIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class GraggBulirschStoerIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for GraggBulirschStoerIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class HighamHall54IntegratorBuilder(ODEIntegratorBuilder):
    """
    public class HighamHall54IntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for HighamHall54Integrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class LutherIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class LutherIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for LutherIntegrator.
    
        Since:
            7.1
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class MidpointIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class MidpointIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for MidpointIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class OrbitDeterminationPropagatorBuilder(PropagatorBuilder):
    """
    public interface OrbitDeterminationPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
    
        Base class for orbit determination model builders.
    
        Since:
            11.0
    """
    def buildKalmanModel(self, list: java.util.List['OrbitDeterminationPropagatorBuilder'], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List['OrbitDeterminationPropagatorBuilder'], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None:
        """
            Reset the orbit in the propagator builder.
        
            Parameters:
                newOrbit (:class:`~org.orekit.orbits.Orbit`): New orbit to set in the propagator builder
        
        
        """
        ...

class PythonODEIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class PythonODEIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    """
    def __init__(self): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
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

class PythonPropagatorBuilder(PropagatorBuilder):
    """
    public class PythonPropagatorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
    """
    def __init__(self): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getFrame`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the initial orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getInitialOrbitDate`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                date of the initial orbit
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type expected for the 6 first parameters in null.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                orbit type to use in null
        
            Since:
                7.1
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PythonPropagatorBuilder.getPositionAngle`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable orbital parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle:
        """
            Get the position angle type expected for the 6 first parameters in null.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                position angle type to use in null
        
            Since:
                7.1
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PythonPropagatorBuilder.getOrbitType`
        
        
        """
        ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable propagation parameters.
        
            The parameters typically correspond to force models.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable propagation parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]:
        """
            Get the current value of selected normalized parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getSelectedNormalizedParameters`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                current value of selected normalized parameters
        
        
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

class PythonPropagatorConverter(PropagatorConverter):
    """
    public class PythonPropagatorConverter extends Object implements :class:`~org.orekit.propagation.conversion.PropagatorConverter`
    """
    def __init__(self): ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator:
        """
            Convert a propagator into another one.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                source (:class:`~org.orekit.propagation.Propagator`): propagator to convert
                timeSpan (double): time span considered for conversion
                nbPoints (int): number of points for sampling over the time span
                freeParameters (List<String> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
            Convert a propagator into another one.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                source (:class:`~org.orekit.propagation.Propagator`): propagator to convert
                timeSpan (double): time span considered for conversion
                nbPoints (int): number of points for sampling over the time span
                freeParameters (String...): names of the free parameters
        
            Returns:
                adapted propagator
        
        public :class:`~org.orekit.propagation.Propagator` convert(List<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, List<String> freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                states (List<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (List<String> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
        public :class:`~org.orekit.propagation.Propagator` convert(List<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, String... freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                states (List<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (String...): names of the free parameters
        
            Returns:
                adapted propagator
        
        
        """
        ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_LbL(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_LbS(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_PdiS(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, stringArray: typing.List[str]) -> org.orekit.propagation.Propagator: ...
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

class ThreeEighthesIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class ThreeEighthesIntegratorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for ThreeEighthesIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class BrouwerLyddanePropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    """
    public class BrouwerLyddanePropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder` implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    
        Builder for Brouwer-Lyddane propagator.
    
        By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth
        orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992
        thesis considered the atmospheric drag by time derivatives of the *mean* mean anomaly using the catch-all coefficient
        M2. Usually, M2 is adjusted during an orbit determination process and it represents the combination of all unmodeled
        secular along-track effects (i.e. not just the atmospheric drag). The behavior of M2 is closed to the
        :meth:`~org.orekit.propagation.analytical.tle.TLE.getBStar` parameter for the TLE. If the value of M2 is equal to
        :meth:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator.M2`, the along-track secular effects are not
        considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value
        of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/sÃ‚Â².
    
        To estimate the M2 parameter, it is necessary to call the
        :meth:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder.getPropagationParametersDrivers` method as follow:
    
        .. code-block: java
        
        
          for (ParameterDriver driver : builder.getPropagationParametersDrivers().getDrivers()) {
             if (BrouwerLyddanePropagator.M2_NAME.equals(driver.getName())) {
                driver.setSelected(true);
             }
          }
         
    
        Since:
            11.1
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, double3: float, double4: float, double5: float, double6: float, orbitType: org.orekit.orbits.OrbitType, positionAngle: org.orekit.orbits.PositionAngle, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngle: org.orekit.orbits.PositionAngle, double: float, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double2: float): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.analytical.BrouwerLyddanePropagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...

class DSSTPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    """
    public class DSSTPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder` implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    
        Builder for DSST propagator.
    
        Since:
            10.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, double: float, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, double: float, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, dSSTForceModel: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None:
        """
            Add a force model to the global perturbation model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                model (:class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`): perturbing :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel` to add
        
        
        """
        ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.DSSTBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'DSSTPropagatorBuilder':
        """
            Create a copy of a DSSTPropagatorBuilder object.
        
            Returns:
                Copied version of the DSSTPropagatorBuilder
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]: ...
    def getIntegratorBuilder(self) -> ODEIntegratorBuilder:
        """
            Get the integrator builder.
        
            Returns:
                the integrator builder
        
        
        """
        ...
    def getMass(self) -> float:
        """
            Get the mass.
        
            Returns:
                the mass
        
        
        """
        ...
    def getPropagationType(self) -> org.orekit.propagation.PropagationType:
        """
            Get the type of the orbit used for the propagation (mean or osculating).
        
            Returns:
                the type of the orbit used for the propagation
        
        
        """
        ...
    def getStateType(self) -> org.orekit.propagation.PropagationType:
        """
            Get the type of the elements used to define the orbital state (mean or osculating).
        
            Returns:
                the type of the elements used to define the orbital state
        
        
        """
        ...
    @typing.overload
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None:
        """
            Reset the orbit in the propagator builder.
        
            Parameters:
                newOrbit (:class:`~org.orekit.orbits.Orbit`): newOrbit New orbit to set in the propagator builder
                orbitType (:class:`~org.orekit.propagation.PropagationType`): orbit type (MEAN or OSCULATING)
        
        
        """
        ...
    @typing.overload
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    def setMass(self, double: float) -> None:
        """
            Set the initial mass.
        
            Parameters:
                mass (double): the mass (kg)
        
        
        """
        ...

class EcksteinHechlerPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    """
    public class EcksteinHechlerPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder` implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    
        Builder for Eckstein-Hechler propagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, double3: float, double4: float, double5: float, double6: float, double7: float, orbitType: org.orekit.orbits.OrbitType, positionAngle: org.orekit.orbits.PositionAngle, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...

class FiniteDifferencePropagatorConverter(AbstractPropagatorConverter):
    """
    public class FiniteDifferencePropagatorConverter extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
    
        Propagator converter using finite differences to compute the Jacobian.
    
        Since:
            6.0
    """
    def __init__(self, propagatorBuilder: PropagatorBuilder, double: float, int: int): ...

class JacobianPropagatorConverter(AbstractPropagatorConverter):
    """
    public class JacobianPropagatorConverter extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
    
        Propagator converter using the real Jacobian.
    
        Since:
            6.0
    """
    def __init__(self, numericalPropagatorBuilder: 'NumericalPropagatorBuilder', double: float, int: int): ...

class KeplerianPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    """
    public class KeplerianPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder` implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    
        Builder for Keplerian propagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...

class NumericalPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    """
    public class NumericalPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder` implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    
        Builder for numerical propagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, forceModel: org.orekit.forces.ForceModel) -> None:
        """
            Add a force model to the global perturbation model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                model (:class:`~org.orekit.forces.ForceModel`): perturbing :class:`~org.orekit.forces.ForceModel` to add
        
        
        """
        ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.KalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.BatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.numerical.NumericalPropagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'NumericalPropagatorBuilder':
        """
            Create a copy of a NumericalPropagatorBuilder object.
        
            Returns:
                Copied version of the NumericalPropagatorBuilder
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]: ...
    def getIntegratorBuilder(self) -> ODEIntegratorBuilder:
        """
            Get the integrator builder.
        
            Returns:
                the integrator builder
        
            Since:
                9.2
        
        
        """
        ...
    def getMass(self) -> float:
        """
            Get the mass.
        
            Returns:
                the mass
        
            Since:
                9.2
        
        
        """
        ...
    def setMass(self, double: float) -> None:
        """
            Set the initial mass.
        
            Parameters:
                mass (double): the mass (kg)
        
        
        """
        ...

class PythonAbstractPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class PythonAbstractPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    """
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float, boolean: bool): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator. Extension point for Python.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
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

class PythonAbstractPropagatorConverter(AbstractPropagatorConverter):
    """
    public class PythonAbstractPropagatorConverter extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
    """
    def __init__(self, propagatorBuilder: PropagatorBuilder, double: float, int: int): ...
    def finalize(self) -> None: ...
    def getModel(self) -> org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction:
        """
            Get the Jacobian of the function computing position/velocity at sample points. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.AbstractPropagatorConverter.getModel`Â in
                classÂ :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
        
            Returns:
                Jacobian of the function computing position/velocity at sample points
        
        
        """
        ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.MultivariateVectorFunction:
        """
            Get the function computing position/velocity at sample points. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.AbstractPropagatorConverter.getObjectiveFunction`Â in
                classÂ :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
        
            Returns:
                function computing position/velocity at sample points
        
        
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

class PythonOrbitDeterminationPropagatorBuilder(OrbitDeterminationPropagatorBuilder):
    """
    public class PythonOrbitDeterminationPropagatorBuilder extends Object implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    """
    def __init__(self): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def finalize(self) -> None: ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the frame in which the orbit is propagated.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getFrame`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the initial orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getInitialOrbitDate`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                date of the initial orbit
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type expected for the 6 first parameters in null.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                orbit type to use in null
        
            Since:
                7.1
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PythonOrbitDeterminationPropagatorBuilder.getPositionAngle`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable orbital parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle:
        """
            Get the position angle type expected for the 6 first parameters in null.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                position angle type to use in null
        
            Since:
                7.1
        
            Also see:
                null, :meth:`~org.orekit.propagation.conversion.PythonOrbitDeterminationPropagatorBuilder.getOrbitType`
        
        
        """
        ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable propagation parameters.
        
            The parameters typically correspond to force models.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable propagation parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]:
        """
            Get the current value of selected normalized parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getSelectedNormalizedParameters`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                current value of selected normalized parameters
        
        
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
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None:
        """
            Reset the orbit in the propagator builder.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder.resetOrbit`Â in
                interfaceÂ :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
        
            Parameters:
                newOrbit (:class:`~org.orekit.orbits.Orbit`): New orbit to set in the propagator builder
        
        
        """
        ...

class TLEPropagatorBuilder(AbstractPropagatorBuilder, OrbitDeterminationPropagatorBuilder):
    """
    public class TLEPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder` implements :class:`~org.orekit.propagation.conversion.OrbitDeterminationPropagatorBuilder`
    
        Builder for TLEPropagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float, double2: float, int: int): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float, dataContext: org.orekit.data.DataContext, double2: float, int: int): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.analytical.tle.TLEPropagator:
        """
            Build a propagator.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def getTemplateTLE(self) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Getter for the template TLE.
        
            Returns:
                the template TLE
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion")``.

    AbstractPropagatorBuilder: typing.Type[AbstractPropagatorBuilder]
    AbstractPropagatorConverter: typing.Type[AbstractPropagatorConverter]
    AdamsBashforthIntegratorBuilder: typing.Type[AdamsBashforthIntegratorBuilder]
    AdamsMoultonIntegratorBuilder: typing.Type[AdamsMoultonIntegratorBuilder]
    BrouwerLyddanePropagatorBuilder: typing.Type[BrouwerLyddanePropagatorBuilder]
    ClassicalRungeKuttaIntegratorBuilder: typing.Type[ClassicalRungeKuttaIntegratorBuilder]
    DSSTPropagatorBuilder: typing.Type[DSSTPropagatorBuilder]
    DormandPrince54IntegratorBuilder: typing.Type[DormandPrince54IntegratorBuilder]
    DormandPrince853IntegratorBuilder: typing.Type[DormandPrince853IntegratorBuilder]
    EcksteinHechlerPropagatorBuilder: typing.Type[EcksteinHechlerPropagatorBuilder]
    EulerIntegratorBuilder: typing.Type[EulerIntegratorBuilder]
    FiniteDifferencePropagatorConverter: typing.Type[FiniteDifferencePropagatorConverter]
    GillIntegratorBuilder: typing.Type[GillIntegratorBuilder]
    GraggBulirschStoerIntegratorBuilder: typing.Type[GraggBulirschStoerIntegratorBuilder]
    HighamHall54IntegratorBuilder: typing.Type[HighamHall54IntegratorBuilder]
    JacobianPropagatorConverter: typing.Type[JacobianPropagatorConverter]
    KeplerianPropagatorBuilder: typing.Type[KeplerianPropagatorBuilder]
    LutherIntegratorBuilder: typing.Type[LutherIntegratorBuilder]
    MidpointIntegratorBuilder: typing.Type[MidpointIntegratorBuilder]
    NumericalPropagatorBuilder: typing.Type[NumericalPropagatorBuilder]
    ODEIntegratorBuilder: typing.Type[ODEIntegratorBuilder]
    OrbitDeterminationPropagatorBuilder: typing.Type[OrbitDeterminationPropagatorBuilder]
    OsculatingToMeanElementsConverter: typing.Type[OsculatingToMeanElementsConverter]
    PropagatorBuilder: typing.Type[PropagatorBuilder]
    PropagatorConverter: typing.Type[PropagatorConverter]
    PythonAbstractPropagatorBuilder: typing.Type[PythonAbstractPropagatorBuilder]
    PythonAbstractPropagatorConverter: typing.Type[PythonAbstractPropagatorConverter]
    PythonODEIntegratorBuilder: typing.Type[PythonODEIntegratorBuilder]
    PythonOrbitDeterminationPropagatorBuilder: typing.Type[PythonOrbitDeterminationPropagatorBuilder]
    PythonPropagatorBuilder: typing.Type[PythonPropagatorBuilder]
    PythonPropagatorConverter: typing.Type[PythonPropagatorConverter]
    TLEPropagatorBuilder: typing.Type[TLEPropagatorBuilder]
    ThreeEighthesIntegratorBuilder: typing.Type[ThreeEighthesIntegratorBuilder]
