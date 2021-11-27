import java.util
import org.hipparchus.ode
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
    public class OsculatingToMeanElementsConverter extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
            Get the orbit type expected for the 6 first parameters in
            :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`.
        
            Returns:
                orbit type to use in :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`
        
        
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
            Get the position angle type expected for the 6 first parameters in
            :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`.
        
            Returns:
                position angle type to use in :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`
        
        
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
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`...): names of the free parameters
        
            Returns:
                adapted propagator
        
        :class:`~org.orekit.propagation.Propagator` convert(:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`> freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Parameters:
                states (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
        :class:`~org.orekit.propagation.Propagator` convert(:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`... freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Parameters:
                states (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`...): names of the free parameters
        
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
    public abstract class AbstractPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
    
        Base class for propagator builders.
    
        Since:
            7.1
    """
    def addAdditionalEquations(self, additionalEquations: org.orekit.propagation.integration.AdditionalEquations) -> None:
        """
            Add a set of user-specified equations to be integrated along with the orbit propagation (author Shiva Iyer).
        
            Parameters:
                additional (:class:`~org.orekit.propagation.integration.AdditionalEquations`): additional equations
        
            Since:
                10.1
        
        
        """
        ...
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
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getFrame` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the initial orbit.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getInitialOrbitDate` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                date of the initial orbit
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient (µ - m³/s²) value.
        
            Returns:
                the central attraction coefficient (µ - m³/s²) value
        
            Since:
                9.2
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type expected for the 6 first parameters in
            :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                orbit type to use in :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable orbital parameters
        
        
        """
        ...
    def getPositionAngle(self) -> org.orekit.orbits.PositionAngle:
        """
            Get the position angle type expected for the 6 first parameters in
            :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngle` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                position angle type to use in :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`
        
        
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
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPropagationParametersDrivers` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable propagation parameters
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.List[float]:
        """
            Get the current value of selected normalized parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getSelectedNormalizedParameters` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
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
    public abstract class AbstractPropagatorConverter extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.PropagatorConverter`
    
        Common handling of :class:`~org.orekit.propagation.conversion.PropagatorConverter` methods for propagators conversions.
    
        This abstract class factors the common code for propagators conversion. Only one method must be implemented by derived
        classes: :meth:`~org.orekit.propagation.conversion.AbstractPropagatorConverter.getObjectiveFunction`.
    
        The converter uses the LevenbergMarquardtOptimizer from the
        :class:`~org.orekit.propagation.conversion.https:.hipparchus.org` library. Different implementations correspond to
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
    public class AdamsBashforthIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for AdamsBashforthIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class AdamsMoultonIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class AdamsMoultonIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for AdamsMoultonIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class ClassicalRungeKuttaIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class ClassicalRungeKuttaIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for ClassicalRungeKuttaIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class DormandPrince54IntegratorBuilder(ODEIntegratorBuilder):
    """
    public class DormandPrince54IntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for DormandPrince54Integrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class DormandPrince853IntegratorBuilder(ODEIntegratorBuilder):
    """
    public class DormandPrince853IntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for DormandPrince853Integrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class EulerIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class EulerIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for EulerIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class GillIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class GillIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for GillIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class GraggBulirschStoerIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class GraggBulirschStoerIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for GraggBulirschStoerIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class HighamHall54IntegratorBuilder(ODEIntegratorBuilder):
    """
    public class HighamHall54IntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for HighamHall54Integrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class LutherIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class LutherIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for LutherIntegrator.
    
        Since:
            7.1
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
        """
        ...

class MidpointIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class MidpointIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for MidpointIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
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

class ThreeEighthesIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class ThreeEighthesIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    
        Builder for ThreeEighthesIntegrator.
    
        Since:
            6.0
    """
    def __init__(self, double: float): ...
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
            Build a first order integrator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.ODEIntegratorBuilder.buildIntegrator` in
                interface :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
        
            Parameters:
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use
        
            Returns:
                a first order integrator ready to use
        
        
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
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.DSSTKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.DSSTBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
            Build a propagator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
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
    def setMass(self, double: float) -> None:
        """
            Set the initial mass.
        
            Parameters:
                mass (double): the mass (kg)
        
        
        """
        ...

class EcksteinHechlerPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class EcksteinHechlerPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
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
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
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

class KeplerianPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class KeplerianPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
        Builder for Keplerian propagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngle: org.orekit.orbits.PositionAngle, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
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
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
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
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngle: org.orekit.orbits.PositionAngle, double: float, dataContext: org.orekit.data.DataContext): ...
    def buildKalmanModel(self, list: java.util.List[OrbitDeterminationPropagatorBuilder], list2: java.util.List[org.orekit.estimation.sequential.CovarianceMatrixProvider], parameterDriversList: org.orekit.utils.ParameterDriversList, covarianceMatrixProvider: org.orekit.estimation.sequential.CovarianceMatrixProvider) -> org.orekit.estimation.sequential.AbstractKalmanModel: ...
    def buildLSModel(self, orbitDeterminationPropagatorBuilderArray: typing.List[OrbitDeterminationPropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.analytical.tle.TLEPropagator:
        """
            Build a propagator.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
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
    TLEPropagatorBuilder: typing.Type[TLEPropagatorBuilder]
    ThreeEighthesIntegratorBuilder: typing.Type[ThreeEighthesIntegratorBuilder]
