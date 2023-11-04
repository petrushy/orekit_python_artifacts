import java.util
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.ode
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.attitudes
import org.orekit.data
import org.orekit.estimation.leastsquares
import org.orekit.estimation.measurements
import org.orekit.forces
import org.orekit.forces.gravity.potential
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.analytical.tle.generation
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.propagation.semianalytical.dsst
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.time
import org.orekit.utils
import typing



_FieldODEIntegratorBuilder__T = typing.TypeVar('_FieldODEIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEIntegratorBuilder(typing.Generic[_FieldODEIntegratorBuilder__T]):
    """
    public interface FieldODEIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        This interface is the top-level abstraction to build first order integrators for propagators conversion.
    
        Since:
            12.0
    """
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldODEIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_FieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldODEIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_FieldODEIntegratorBuilder__T]: ...

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
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List['PropagatorBuilder'], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'PropagatorBuilder':
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
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
    def getMu(self) -> float:
        """
            Get the central attraction coefficient (µ - m³/s²) value.
        
            Returns:
                the central attraction coefficient (µ - m³/s²) value
        
            Since:
                12.0
        
        
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
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngleType`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters. Orbital drivers should have only 1 value estimated (1 span)
        
            Returns:
                drivers for the configurable orbital parameters
        
            Since:
                8.0
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
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
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None:
        """
            Reset the orbit in the propagator builder.
        
            Parameters:
                newOrbit (:class:`~org.orekit.orbits.Orbit`): New orbit to set in the propagator builder
        
            Since:
                12.0
        
        
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
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, *string: str) -> org.orekit.propagation.Propagator:
        """
            Convert a propagator into another one.
        
            Parameters:
                source (:class:`~org.orekit.propagation.Propagator`): propagator to convert
                timeSpan (double): time span considered for conversion
                nbPoints (int): number of points for sampling over the time span
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`...): names of the free parameters
        
            Returns:
                adapted propagator
        
        :class:`~org.orekit.propagation.Propagator` convert (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`> freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Parameters:
                states (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
        :class:`~org.orekit.propagation.Propagator` convert (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`... freeParameters)
        
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
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, *string: str) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator: ...

_AbstractFieldIntegratorBuilder__T = typing.TypeVar('_AbstractFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractFieldIntegratorBuilder(FieldODEIntegratorBuilder[_AbstractFieldIntegratorBuilder__T], typing.Generic[_AbstractFieldIntegratorBuilder__T]):
    """
    public abstract class AbstractFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.FieldODEIntegratorBuilder`<T>
    
        Abstract class for :class:`~org.orekit.propagation.conversion.FieldODEIntegratorBuilder`.
    """
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_AbstractFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AbstractFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_AbstractFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AbstractFieldIntegratorBuilder__T]: ...

class AbstractPropagatorBuilder(PropagatorBuilder):
    """
    public abstract class AbstractPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
    
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
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getMu` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                the central attraction coefficient (µ - m³/s²) value
        
        
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
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngleType`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters. Orbital drivers should have only 1 value estimated (1 span)
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable orbital parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the position angle type expected for the 6 first parameters in
            :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngleType` in
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
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.resetOrbit` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
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
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, *string: str) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, *string: str) -> org.orekit.propagation.Propagator: ...
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

_PythonFieldODEIntegratorBuilder__T = typing.TypeVar('_PythonFieldODEIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldODEIntegratorBuilder(FieldODEIntegratorBuilder[_PythonFieldODEIntegratorBuilder__T], typing.Generic[_PythonFieldODEIntegratorBuilder__T]):
    """
    public class PythonFieldODEIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.FieldODEIntegratorBuilder`<T>
    """
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_PythonFieldODEIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_PythonFieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_PythonFieldODEIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_PythonFieldODEIntegratorBuilder__T]: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...

class PythonODEIntegratorBuilder(ODEIntegratorBuilder):
    """
    public class PythonODEIntegratorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`
    """
    def __init__(self): ...
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
    public class PythonPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
    """
    def __init__(self): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
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
    def copy(self) -> PropagatorBuilder:
        """
            Create a new instance identical to this one.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.copy` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                new instance identical to this one
        
        
        """
        ...
    def finalize(self) -> None: ...
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
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getMu` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                the central attraction coefficient (µ - m³/s²) value
        
        
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
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngleType`
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
            Get the drivers for the configurable orbital parameters. Orbital drivers should have only 1 value estimated (1 span)
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitalParametersDrivers` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                drivers for the configurable orbital parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the position angle type expected for the 6 first parameters in
            :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getPositionAngleType` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Returns:
                position angle type to use in :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`
        
            Also see:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.buildPropagator`,
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.getOrbitType`
        
        
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
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
        public long pythonExtension()
        
        
        """
        ...
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit) -> None:
        """
            Reset the orbit in the propagator builder.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorBuilder.resetOrbit` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorBuilder`
        
            Parameters:
                newOrbit (:class:`~org.orekit.orbits.Orbit`): New orbit to set in the propagator builder
        
        
        """
        ...

class PythonPropagatorConverter(PropagatorConverter):
    """
    public class PythonPropagatorConverter extends :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.PropagatorConverter`
    """
    def __init__(self): ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, list: java.util.List[str]) -> org.orekit.propagation.Propagator:
        """
            Convert a propagator into another one.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                source (:class:`~org.orekit.propagation.Propagator`): propagator to convert
                timeSpan (double): time span considered for conversion
                nbPoints (int): number of points for sampling over the time span
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`...): names of the free parameters
        
            Returns:
                adapted propagator
        
        public :class:`~org.orekit.propagation.Propagator` convert (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`> freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                states (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`> freeParameters): names of the free parameters
        
            Returns:
                adapted propagator
        
        public :class:`~org.orekit.propagation.Propagator` convert (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states, boolean positionOnly, :class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`... freeParameters)
        
            Find the propagator that minimize the mean square error for a sample of
            :class:`~org.orekit.propagation.SpacecraftState`.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.PropagatorConverter.convert` in
                interface :class:`~org.orekit.propagation.conversion.PropagatorConverter`
        
            Parameters:
                states (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<:class:`~org.orekit.propagation.SpacecraftState`> states): spacecraft states sample to fit
                positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
                freeParameters (:class:`~org.orekit.propagation.conversion.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`...): names of the free parameters
        
            Returns:
                adapted propagator
        
        
        """
        ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, *string: str) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def convert(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, *string: str) -> org.orekit.propagation.Propagator: ...
    def convert_LbL(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, list2: java.util.List[str]) -> org.orekit.propagation.Propagator: ...
    def convert_LbS(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, *string: str) -> org.orekit.propagation.Propagator: ...
    def convert_PdiS(self, propagator: org.orekit.propagation.Propagator, double: float, int: int, *string: str) -> org.orekit.propagation.Propagator: ...
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

_AbstractFixedStepFieldIntegratorBuilder__T = typing.TypeVar('_AbstractFixedStepFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractFixedStepFieldIntegratorBuilder(AbstractFieldIntegratorBuilder[_AbstractFixedStepFieldIntegratorBuilder__T], typing.Generic[_AbstractFixedStepFieldIntegratorBuilder__T]):
    """
    public abstract class AbstractFixedStepFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFieldIntegratorBuilder`<T>
    
        Abstract class for integrator builder using fixed step size.
    """
    ...

_AbstractVariableStepFieldIntegratorBuilder__T = typing.TypeVar('_AbstractVariableStepFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractVariableStepFieldIntegratorBuilder(AbstractFieldIntegratorBuilder[_AbstractVariableStepFieldIntegratorBuilder__T], typing.Generic[_AbstractVariableStepFieldIntegratorBuilder__T]):
    """
    public abstract class AbstractVariableStepFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFieldIntegratorBuilder`<T>
    
        Abstract class for integrator builder using variable step size.
    """
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_AbstractVariableStepFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AbstractVariableStepFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_AbstractVariableStepFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AbstractVariableStepFieldIntegratorBuilder__T]: ...

class BrouwerLyddanePropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class BrouwerLyddanePropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
        Builder for Brouwer-Lyddane propagator.
    
        By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth
        orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992
        thesis considered the atmospheric drag by time derivatives of the *mean* mean anomaly using the catch-all coefficient
        M2. Usually, M2 is adjusted during an orbit determination process and it represents the combination of all unmodeled
        secular along-track effects (i.e. not just the atmospheric drag). The behavior of M2 is closed to the
        :meth:`~org.orekit.propagation.analytical.tle.TLE.getBStar` parameter for the TLE. If the value of M2 is equal to
        :meth:`~org.orekit.propagation.analytical.BrouwerLyddanePropagator.M2`, the along-track secular effects are not
        considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value
        of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/s².
    
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
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, double3: float, double4: float, double5: float, double6: float, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, double7: float, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, double2: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double2: float): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.analytical.BrouwerLyddanePropagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'BrouwerLyddanePropagatorBuilder':
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
        """
        ...

class DSSTPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class DSSTPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
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
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.DSSTBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
            Build a propagator.
        
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

class EcksteinHechlerPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class EcksteinHechlerPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
        Builder for Eckstein-Hechler propagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, double: float, double2: float, tideSystem: org.orekit.forces.gravity.potential.TideSystem, double3: float, double4: float, double5: float, double6: float, double7: float, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType, double8: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngleType: org.orekit.orbits.PositionAngleType, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'EcksteinHechlerPropagatorBuilder':
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
        """
        ...

class EphemerisPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class EphemerisPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
        Builder for Ephemeris propagator.
    
        Since:
            11.3
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator..
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'EphemerisPropagatorBuilder':
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
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
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngleType: org.orekit.orbits.PositionAngleType, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'KeplerianPropagatorBuilder':
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
        """
        ...

class NumericalPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class NumericalPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
        Builder for numerical propagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngleType: org.orekit.orbits.PositionAngleType, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, forceModel: org.orekit.forces.ForceModel) -> None:
        """
            Add a force model to the global perturbation model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                model (:class:`~org.orekit.forces.ForceModel`): perturbing :class:`~org.orekit.forces.ForceModel` to add
        
        
        """
        ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.BatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.numerical.NumericalPropagator:
        """
            Build a propagator.
        
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
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, boolean: bool): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.Propagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> PropagatorBuilder:
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
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
                :meth:`~org.orekit.propagation.conversion.AbstractPropagatorConverter.getModel` in
                class :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
        
            Returns:
                Jacobian of the function computing position/velocity at sample points
        
        
        """
        ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.MultivariateVectorFunction:
        """
            Get the function computing position/velocity at sample points. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.AbstractPropagatorConverter.getObjectiveFunction` in
                class :class:`~org.orekit.propagation.conversion.AbstractPropagatorConverter`
        
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

class TLEPropagatorBuilder(AbstractPropagatorBuilder):
    """
    public class TLEPropagatorBuilder extends :class:`~org.orekit.propagation.conversion.AbstractPropagatorBuilder`
    
        Builder for TLEPropagator.
    
        Since:
            6.0
    """
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, dataContext: org.orekit.data.DataContext, tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm): ...
    def buildLeastSquaresModel(self, propagatorBuilderArray: typing.List[PropagatorBuilder], list: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], parameterDriversList: org.orekit.utils.ParameterDriversList, modelObserver: org.orekit.estimation.leastsquares.ModelObserver) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel: ...
    def buildPropagator(self, doubleArray: typing.List[float]) -> org.orekit.propagation.analytical.tle.TLEPropagator:
        """
            Build a propagator.
        
            Parameters:
                normalizedParameters (double[]): normalized values for the selected parameters
        
            Returns:
                an initialized propagator
        
        
        """
        ...
    def copy(self) -> 'TLEPropagatorBuilder':
        """
            Create a new instance identical to this one.
        
            Returns:
                new instance identical to this one
        
        
        """
        ...
    def getTemplateTLE(self) -> org.orekit.propagation.analytical.tle.TLE:
        """
            Getter for the template TLE.
        
            Returns:
                the template TLE
        
        
        """
        ...

_AbstractLimitedVariableStepFieldIntegratorBuilder__T = typing.TypeVar('_AbstractLimitedVariableStepFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AbstractLimitedVariableStepFieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_AbstractLimitedVariableStepFieldIntegratorBuilder__T], typing.Generic[_AbstractLimitedVariableStepFieldIntegratorBuilder__T]):
    """
    public abstract class AbstractLimitedVariableStepFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractVariableStepFieldIntegratorBuilder`<T>
    
        Abstract class for integrator using a limited number of variable steps.
    """
    ...

_ClassicalRungeKuttaFieldIntegratorBuilder__T = typing.TypeVar('_ClassicalRungeKuttaFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ClassicalRungeKuttaFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_ClassicalRungeKuttaFieldIntegratorBuilder__T], typing.Generic[_ClassicalRungeKuttaFieldIntegratorBuilder__T]):
    """
    public class ClassicalRungeKuttaFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFixedStepFieldIntegratorBuilder`<T>
    
        Builder for ClassicalRungeKuttaFieldIntegrator.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _ClassicalRungeKuttaFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_ClassicalRungeKuttaFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_ClassicalRungeKuttaFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_ClassicalRungeKuttaFieldIntegratorBuilder__T]: ...

_DormandPrince54FieldIntegratorBuilder__T = typing.TypeVar('_DormandPrince54FieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince54FieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_DormandPrince54FieldIntegratorBuilder__T], typing.Generic[_DormandPrince54FieldIntegratorBuilder__T]):
    """
    public class DormandPrince54FieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractVariableStepFieldIntegratorBuilder`<T>
    
        Builder for DormandPrince54FieldIntegrator.
    
        Since:
            12.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_DormandPrince54FieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_DormandPrince54FieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_DormandPrince54FieldIntegratorBuilder__T]: ...

_DormandPrince853FieldIntegratorBuilder__T = typing.TypeVar('_DormandPrince853FieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince853FieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_DormandPrince853FieldIntegratorBuilder__T], typing.Generic[_DormandPrince853FieldIntegratorBuilder__T]):
    """
    public class DormandPrince853FieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractVariableStepFieldIntegratorBuilder`<T>
    
        Builder for DormandPrince853FieldIntegrator.
    
        Since:
            12.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_DormandPrince853FieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_DormandPrince853FieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_DormandPrince853FieldIntegratorBuilder__T]: ...

_EulerFieldIntegratorBuilder__T = typing.TypeVar('_EulerFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EulerFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_EulerFieldIntegratorBuilder__T], typing.Generic[_EulerFieldIntegratorBuilder__T]):
    """
    public class EulerFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFixedStepFieldIntegratorBuilder`<T>
    
        Builder for EulerFieldIntegrator.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _EulerFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_EulerFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_EulerFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_EulerFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_EulerFieldIntegratorBuilder__T]: ...

_GillFieldIntegratorBuilder__T = typing.TypeVar('_GillFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class GillFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_GillFieldIntegratorBuilder__T], typing.Generic[_GillFieldIntegratorBuilder__T]):
    """
    public class GillFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFixedStepFieldIntegratorBuilder`<T>
    
        Builder for GillFieldIntegrator.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _GillFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_GillFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_GillFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_GillFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_GillFieldIntegratorBuilder__T]: ...

_HighamHall54FieldIntegratorBuilder__T = typing.TypeVar('_HighamHall54FieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class HighamHall54FieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_HighamHall54FieldIntegratorBuilder__T], typing.Generic[_HighamHall54FieldIntegratorBuilder__T]):
    """
    public class HighamHall54FieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractVariableStepFieldIntegratorBuilder`<T>
    
        Builder for HighamHall54Integrator.
    
        Since:
            12.0
    """
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_HighamHall54FieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_HighamHall54FieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_HighamHall54FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_HighamHall54FieldIntegratorBuilder__T]: ...

_LutherFieldIntegratorBuilder__T = typing.TypeVar('_LutherFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class LutherFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_LutherFieldIntegratorBuilder__T], typing.Generic[_LutherFieldIntegratorBuilder__T]):
    """
    public class LutherFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFixedStepFieldIntegratorBuilder`<T>
    
        Builder for LutherFieldIntegrator.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _LutherFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_LutherFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_LutherFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_LutherFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_LutherFieldIntegratorBuilder__T]: ...

_MidpointFieldIntegratorBuilder__T = typing.TypeVar('_MidpointFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MidpointFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_MidpointFieldIntegratorBuilder__T], typing.Generic[_MidpointFieldIntegratorBuilder__T]):
    """
    public class MidpointFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFixedStepFieldIntegratorBuilder`<T>
    
        Builder for MidpointFieldIntegrator.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _MidpointFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_MidpointFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_MidpointFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_MidpointFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_MidpointFieldIntegratorBuilder__T]: ...

_ThreeEighthesFieldIntegratorBuilder__T = typing.TypeVar('_ThreeEighthesFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ThreeEighthesFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_ThreeEighthesFieldIntegratorBuilder__T], typing.Generic[_ThreeEighthesFieldIntegratorBuilder__T]):
    """
    public class ThreeEighthesFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractFixedStepFieldIntegratorBuilder`<T>
    
        Builder for ThreeEighthesFieldIntegrator.
    
        Since:
            12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _ThreeEighthesFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_ThreeEighthesFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_ThreeEighthesFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_ThreeEighthesFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_ThreeEighthesFieldIntegratorBuilder__T]: ...

_AdamsBashforthFieldIntegratorBuilder__T = typing.TypeVar('_AdamsBashforthFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsBashforthFieldIntegratorBuilder(AbstractLimitedVariableStepFieldIntegratorBuilder[_AdamsBashforthFieldIntegratorBuilder__T], typing.Generic[_AdamsBashforthFieldIntegratorBuilder__T]):
    """
    public class AdamsBashforthFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractLimitedVariableStepFieldIntegratorBuilder`<T>
    
        Builder for AdamsBashforthFieldIntegrator.
    
        Since:
            12.0
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_AdamsBashforthFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AdamsBashforthFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_AdamsBashforthFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AdamsBashforthFieldIntegratorBuilder__T]: ...

_AdamsMoultonFieldIntegratorBuilder__T = typing.TypeVar('_AdamsMoultonFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsMoultonFieldIntegratorBuilder(AbstractLimitedVariableStepFieldIntegratorBuilder[_AdamsMoultonFieldIntegratorBuilder__T], typing.Generic[_AdamsMoultonFieldIntegratorBuilder__T]):
    """
    public class AdamsMoultonFieldIntegratorBuilder<T extends :class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.conversion.AbstractLimitedVariableStepFieldIntegratorBuilder`<T>
    
        Builder for AdamsMoultonFieldIntegrator.
    
        Since:
            12.0
    """
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_AdamsMoultonFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AdamsMoultonFieldIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_AdamsMoultonFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_AdamsMoultonFieldIntegratorBuilder__T]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion")``.

    AbstractFieldIntegratorBuilder: typing.Type[AbstractFieldIntegratorBuilder]
    AbstractFixedStepFieldIntegratorBuilder: typing.Type[AbstractFixedStepFieldIntegratorBuilder]
    AbstractLimitedVariableStepFieldIntegratorBuilder: typing.Type[AbstractLimitedVariableStepFieldIntegratorBuilder]
    AbstractPropagatorBuilder: typing.Type[AbstractPropagatorBuilder]
    AbstractPropagatorConverter: typing.Type[AbstractPropagatorConverter]
    AbstractVariableStepFieldIntegratorBuilder: typing.Type[AbstractVariableStepFieldIntegratorBuilder]
    AdamsBashforthFieldIntegratorBuilder: typing.Type[AdamsBashforthFieldIntegratorBuilder]
    AdamsBashforthIntegratorBuilder: typing.Type[AdamsBashforthIntegratorBuilder]
    AdamsMoultonFieldIntegratorBuilder: typing.Type[AdamsMoultonFieldIntegratorBuilder]
    AdamsMoultonIntegratorBuilder: typing.Type[AdamsMoultonIntegratorBuilder]
    BrouwerLyddanePropagatorBuilder: typing.Type[BrouwerLyddanePropagatorBuilder]
    ClassicalRungeKuttaFieldIntegratorBuilder: typing.Type[ClassicalRungeKuttaFieldIntegratorBuilder]
    ClassicalRungeKuttaIntegratorBuilder: typing.Type[ClassicalRungeKuttaIntegratorBuilder]
    DSSTPropagatorBuilder: typing.Type[DSSTPropagatorBuilder]
    DormandPrince54FieldIntegratorBuilder: typing.Type[DormandPrince54FieldIntegratorBuilder]
    DormandPrince54IntegratorBuilder: typing.Type[DormandPrince54IntegratorBuilder]
    DormandPrince853FieldIntegratorBuilder: typing.Type[DormandPrince853FieldIntegratorBuilder]
    DormandPrince853IntegratorBuilder: typing.Type[DormandPrince853IntegratorBuilder]
    EcksteinHechlerPropagatorBuilder: typing.Type[EcksteinHechlerPropagatorBuilder]
    EphemerisPropagatorBuilder: typing.Type[EphemerisPropagatorBuilder]
    EulerFieldIntegratorBuilder: typing.Type[EulerFieldIntegratorBuilder]
    EulerIntegratorBuilder: typing.Type[EulerIntegratorBuilder]
    FieldODEIntegratorBuilder: typing.Type[FieldODEIntegratorBuilder]
    FiniteDifferencePropagatorConverter: typing.Type[FiniteDifferencePropagatorConverter]
    GillFieldIntegratorBuilder: typing.Type[GillFieldIntegratorBuilder]
    GillIntegratorBuilder: typing.Type[GillIntegratorBuilder]
    GraggBulirschStoerIntegratorBuilder: typing.Type[GraggBulirschStoerIntegratorBuilder]
    HighamHall54FieldIntegratorBuilder: typing.Type[HighamHall54FieldIntegratorBuilder]
    HighamHall54IntegratorBuilder: typing.Type[HighamHall54IntegratorBuilder]
    JacobianPropagatorConverter: typing.Type[JacobianPropagatorConverter]
    KeplerianPropagatorBuilder: typing.Type[KeplerianPropagatorBuilder]
    LutherFieldIntegratorBuilder: typing.Type[LutherFieldIntegratorBuilder]
    LutherIntegratorBuilder: typing.Type[LutherIntegratorBuilder]
    MidpointFieldIntegratorBuilder: typing.Type[MidpointFieldIntegratorBuilder]
    MidpointIntegratorBuilder: typing.Type[MidpointIntegratorBuilder]
    NumericalPropagatorBuilder: typing.Type[NumericalPropagatorBuilder]
    ODEIntegratorBuilder: typing.Type[ODEIntegratorBuilder]
    OsculatingToMeanElementsConverter: typing.Type[OsculatingToMeanElementsConverter]
    PropagatorBuilder: typing.Type[PropagatorBuilder]
    PropagatorConverter: typing.Type[PropagatorConverter]
    PythonAbstractPropagatorBuilder: typing.Type[PythonAbstractPropagatorBuilder]
    PythonAbstractPropagatorConverter: typing.Type[PythonAbstractPropagatorConverter]
    PythonFieldODEIntegratorBuilder: typing.Type[PythonFieldODEIntegratorBuilder]
    PythonODEIntegratorBuilder: typing.Type[PythonODEIntegratorBuilder]
    PythonPropagatorBuilder: typing.Type[PythonPropagatorBuilder]
    PythonPropagatorConverter: typing.Type[PythonPropagatorConverter]
    TLEPropagatorBuilder: typing.Type[TLEPropagatorBuilder]
    ThreeEighthesFieldIntegratorBuilder: typing.Type[ThreeEighthesFieldIntegratorBuilder]
    ThreeEighthesIntegratorBuilder: typing.Type[ThreeEighthesIntegratorBuilder]
