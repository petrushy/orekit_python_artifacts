
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.ode
import org.hipparchus.ode.nonstiff
import org.hipparchus.optim.nonlinear.vector.leastsquares
import org.orekit.attitudes
import org.orekit.data
import org.orekit.estimation.leastsquares
import org.orekit.estimation.measurements
import org.orekit.forces
import org.orekit.forces.gravity.potential
import org.orekit.forces.maneuvers
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.analytical.tle.generation
import org.orekit.propagation.conversion.averaging
import org.orekit.propagation.conversion.osc2mean
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
    This interface is the top-level abstraction to build first order integrators for propagators conversion.
    
    Since:
        12.0
    """
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldODEIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.FieldODEIntegrator[_FieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldODEIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.FieldODEIntegrator[_FieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldODEIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.FieldODEIntegrator[_FieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldODEIntegratorBuilder__T]) -> org.hipparchus.ode.FieldODEIntegrator[_FieldODEIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'ODEIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Returns:
            ODE integrator builder
        
        Since:
            13.0
        
        
        """
        ...

class ODEIntegratorBuilder:
    """
    This interface is the top-level abstraction to build first order integrators for propagators conversion.
    
    Since:
        6.0
    """
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.ODEIntegrator:
        """
        Build a first order integrator.
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        Since:
            13.0
        
        Build a first order integrator.
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.ODEIntegrator: ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.ODEIntegrator:
        """
        Build a first order integrator. Non-orbit version.
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): absolute position-velocity vector
        
        Returns:
            a first order integrator ready to use
        
        Since:
            12.2
        
        
        """
        ...

class OsculatingToMeanElementsConverter:
    """
    This class converts osculating orbital elements into mean elements.
    
    As this process depends on the force models used to average the orbit, a Propagator is given as input. The force models used will be those contained into the propagator. This propagator must support its initial state to be reset, and this initial state must represent some mean value. This implies that this method will not work with TLEPropagator because their initial state cannot be reset, and it won't work either with EcksteinHechlerPropagator as their initial state is osculating and not mean. As of 6.0, this works mainly for DSSTPropagator.
    """
    def __init__(self, state: org.orekit.propagation.SpacecraftState, satelliteRevolution: int, propagator: org.orekit.propagation.Propagator, positionScale: float):
        """
        Constructor.
        
        Parameters:
            state (SpacecraftState): initial orbit to convert
            satelliteRevolution (int): number of satellite revolutions in the averaging interval
            propagator (Propagator): propagator used to compute mean orbit
            positionScale (double): scaling factor used for orbital parameters normalization (typically set to the expected standard deviation of the
                position)
        
        
        """
        ...
    def convert(self) -> org.orekit.propagation.SpacecraftState:
        """
        Convert an osculating orbit into a mean orbit, in DSST sense.
        
        Returns:
            mean orbit state, in DSST sense
        
        
        """
        ...

class PropagatorBuilder(java.lang.Cloneable):
    """
    This interface is the top-level abstraction to build propagators for conversion.
    
    Since:
        6.0
    """
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List['PropagatorBuilder'], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel:
        """
        Build a new batch least squares model.
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.Propagator:
        """
        Build a propagator.
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.Propagator:
        """
        Build a propagator from current value of selected normalized parameters.
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Get the attitude provider.
        
        Returns:
            the attitude provider
        
        Since:
            13.0
        
        
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
    def getMass(self) -> float:
        """
        Get the initial mass.
        
        Returns:
            the mass (kg)
        
        Since:
            13.0
        
        
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
        Get the orbit type expected for the 6 first parameters in buildPropagator.
        
        Returns:
            orbit type to use in buildPropagator
        
        Since:
            7.1
        
        Also see:
            buildPropagator,
            getPositionAngleType
        
        
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
        Get the position angle type expected for the 6 first parameters in buildPropagator.
        
        Returns:
            position angle type to use in buildPropagator
        
        Since:
            7.1
        
        Also see:
            buildPropagator,
            getOrbitType
        
        
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
    def getSelectedNormalizedParameters(self) -> typing.MutableSequence[float]:
        """
        Get the current value of selected normalized parameters.
        
        Returns:
            current value of selected normalized parameters
        
        
        """
        ...
    def resetOrbit(self, newOrbit: org.orekit.orbits.Orbit) -> None:
        """
        Reset the orbit in the propagator builder.
        
        Parameters:
            newOrbit (Orbit): New orbit to set in the propagator builder
        
        Since:
            12.0
        
        
        """
        ...

class PropagatorConverter:
    """
    This interface is the top-level abstraction for propagators conversions.
    
    It provides a way to convert a given propagator or a set of SpacecraftState into a wanted propagator that minimize the mean square error over a time span.
    
    Since:
        6.0
    """
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, *string: str) -> org.orekit.propagation.Propagator:
        """
        Convert a propagator into another one.
        
        Parameters:
            source (Propagator): propagator to convert
            timeSpan (double): time span considered for conversion
            nbPoints (int): number of points for sampling over the time span
            freeParameters (String...): names of the free parameters
        
        Returns:
            adapted propagator
        
        Propagator convert (List<SpacecraftState> states, boolean positionOnly, List<String> freeParameters)
        
        Find the propagator that minimize the mean square error for a sample of SpacecraftState.
        
        Parameters:
            states (List<SpacecraftState> states): spacecraft states sample to fit
            positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
            freeParameters (List<String> freeParameters): names of the free parameters
        
        Returns:
            adapted propagator
        
        Propagator convert (List<SpacecraftState> states, boolean positionOnly, String... freeParameters)
        
        Find the propagator that minimize the mean square error for a sample of SpacecraftState.
        
        Parameters:
            states (List<SpacecraftState> states): spacecraft states sample to fit
            positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
            freeParameters (String...): names of the free parameters
        
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

_AbstractIntegratorBuilder__T = typing.TypeVar('_AbstractIntegratorBuilder__T', bound=org.hipparchus.ode.AbstractIntegrator)  # <T>
class AbstractIntegratorBuilder(ODEIntegratorBuilder, typing.Generic[_AbstractIntegratorBuilder__T]):
    """
    Abstract class for integrator builder.
    
    Since:
        13.0
    """
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, angleType: org.orekit.orbits.PositionAngleType) -> _AbstractIntegratorBuilder__T:
        """
        Description copied from interface: buildIntegrator Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> _AbstractIntegratorBuilder__T:
        """
        Description copied from interface: buildIntegrator Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> _AbstractIntegratorBuilder__T:
        """
        Description copied from interface: buildIntegrator Build a first order integrator. Non-orbit version.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): absolute position-velocity vector
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...

_AbstractPropagatorBuilder__T = typing.TypeVar('_AbstractPropagatorBuilder__T', bound=org.orekit.propagation.AbstractPropagator)  # <T>
class AbstractPropagatorBuilder(PropagatorBuilder, typing.Generic[_AbstractPropagatorBuilder__T]):
    """
    Base class for propagator builders.
    
    Since:
        7.1
    """
    def addAdditionalDerivativesProvider(self, provider: org.orekit.propagation.integration.AdditionalDerivativesProvider) -> None:
        """
        Add a set of user-specified equations to be integrated along with the orbit propagation (author Shiva Iyer).
        
        Parameters:
            provider (AdditionalDerivativesProvider): provider for additional derivatives
        
        Since:
            11.1
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> _AbstractPropagatorBuilder__T:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> _AbstractPropagatorBuilder__T:
        """
        Build a propagator from current value of selected normalized parameters.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'AbstractPropagatorBuilder'[_AbstractPropagatorBuilder__T]:
        """
        .
        
        Overrides: Object in class Object
        
        
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
        
        Specified by: getAttitudeProvider in interface PropagatorBuilder
        
        Returns:
            the attitude provider
        
        Since:
            10.1
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        Specified by: getFrame in interface PropagatorBuilder
        
        Returns:
            frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date of the initial orbit.
        
        Specified by: getInitialOrbitDate in interface PropagatorBuilder
        
        Returns:
            date of the initial orbit
        
        
        """
        ...
    def getMass(self) -> float:
        """
        Get the mass.
        
        Specified by: getMass in interface PropagatorBuilder
        
        Returns:
            the mass (kg)
        
        Since:
            9.2
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central attraction coefficient (µ - m³/s²) value.
        
        Specified by: getMu in interface PropagatorBuilder
        
        Returns:
            the central attraction coefficient (µ - m³/s²) value
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get the orbit type expected for the 6 first parameters in buildPropagator.
        
        Specified by: getOrbitType in interface PropagatorBuilder
        
        Returns:
            orbit type to use in buildPropagator
        
        Also see:
            buildPropagator,
            getPositionAngleType
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the drivers for the configurable orbital parameters. Orbital drivers should have only 1 value estimated (1 span)
        
        Specified by: getOrbitalParametersDrivers in interface PropagatorBuilder
        
        Returns:
            drivers for the configurable orbital parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get the position angle type expected for the 6 first parameters in buildPropagator.
        
        Specified by: getPositionAngleType in interface PropagatorBuilder
        
        Returns:
            position angle type to use in buildPropagator
        
        Also see:
            buildPropagator,
            getOrbitType
        
        
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
        
        Specified by: getPropagationParametersDrivers in interface PropagatorBuilder
        
        Returns:
            drivers for the configurable propagation parameters
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.MutableSequence[float]:
        """
        Get the current value of selected normalized parameters.
        
        Specified by: getSelectedNormalizedParameters in interface PropagatorBuilder
        
        Returns:
            current value of selected normalized parameters
        
        
        """
        ...
    def resetOrbit(self, newOrbit: org.orekit.orbits.Orbit) -> None:
        """
        Reset the orbit in the propagator builder.
        
        Specified by: resetOrbit in interface PropagatorBuilder
        
        Parameters:
            newOrbit (Orbit): New orbit to set in the propagator builder
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set the attitude provider.
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        Since:
            10.1
        
        
        """
        ...
    def setMass(self, mass: float) -> None:
        """
        Set the initial mass.
        
        Parameters:
            mass (double): the mass (kg)
        
        
        """
        ...

class AbstractPropagatorConverter(PropagatorConverter):
    """
    Common handling of PropagatorConverter methods for propagators conversions.
    
    This abstract class factors the common code for propagators conversion. Only one method must be implemented by derived classes: getObjectiveFunction.
    
    The converter uses the LevenbergMarquardtOptimizer from the org library. Different implementations correspond to different methods for computing the Jacobian.
    
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

class ExplicitRungeKuttaIntegratorBuilder(ODEIntegratorBuilder):
    """
    This interface is for builders of explicit Runge-Kutta integrators (adaptive or not).
    
    Since:
        13.0
    
        class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator?is`
    """
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator: ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator:
        """
        Build a first order integrator. Non-orbit version.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): absolute position-velocity vector
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...

_FieldAbstractIntegratorBuilder__T = typing.TypeVar('_FieldAbstractIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldAbstractIntegratorBuilder__W = typing.TypeVar('_FieldAbstractIntegratorBuilder__W', bound=org.hipparchus.ode.AbstractFieldIntegrator)  # <W>
class FieldAbstractIntegratorBuilder(FieldODEIntegratorBuilder[_FieldAbstractIntegratorBuilder__T], typing.Generic[_FieldAbstractIntegratorBuilder__T, _FieldAbstractIntegratorBuilder__W]):
    """
    This abstract class implements some of the required methods for integrators in propagators conversion.
    
    Since:
        13.0
    """
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldAbstractIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> _FieldAbstractIntegratorBuilder__W: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldAbstractIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> _FieldAbstractIntegratorBuilder__W: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldAbstractIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> _FieldAbstractIntegratorBuilder__W: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldAbstractIntegratorBuilder__T]) -> _FieldAbstractIntegratorBuilder__W: ...

_FieldExplicitRungeKuttaIntegratorBuilder__T = typing.TypeVar('_FieldExplicitRungeKuttaIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldExplicitRungeKuttaIntegratorBuilder(FieldODEIntegratorBuilder[_FieldExplicitRungeKuttaIntegratorBuilder__T], typing.Generic[_FieldExplicitRungeKuttaIntegratorBuilder__T]):
    """
    This interface is the top-level abstraction to build first order integrators for propagators conversion.
    
    Since:
        13.0
    """
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldExplicitRungeKuttaIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_FieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_FieldExplicitRungeKuttaIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_FieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldExplicitRungeKuttaIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_FieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_FieldExplicitRungeKuttaIntegratorBuilder__T]) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_FieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> ExplicitRungeKuttaIntegratorBuilder:
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

_PythonFieldODEIntegratorBuilder__T = typing.TypeVar('_PythonFieldODEIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldODEIntegratorBuilder(FieldODEIntegratorBuilder[_PythonFieldODEIntegratorBuilder__T], typing.Generic[_PythonFieldODEIntegratorBuilder__T]):
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_PythonFieldODEIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_PythonFieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_PythonFieldODEIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator[_PythonFieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_PythonFieldODEIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.FieldODEIntegrator[_PythonFieldODEIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_PythonFieldODEIntegratorBuilder__T]) -> org.hipparchus.ode.FieldODEIntegrator[_PythonFieldODEIntegratorBuilder__T]: ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def toODEIntegratorBuilder(self) -> ODEIntegratorBuilder:
        """
        Description copied from interface: toODEIntegratorBuilder Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class PythonODEIntegratorBuilder(ODEIntegratorBuilder):
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
        
        Returns:
            a first order integrator ready to use
        
        Description copied from interface: buildIntegrator Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.ODEIntegrator: ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.ODEIntegrator:
        """
        Description copied from interface: buildIntegrator Build a first order integrator. Non-orbit version.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): absolute position-velocity vector
        
        Returns:
            a first order integrator ready to use
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonPropagatorBuilder(PropagatorBuilder):
    def __init__(self): ...
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List[PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel:
        """
        Build a new batch least squares model.
        
        Specified by: buildLeastSquaresModel in interface PropagatorBuilder
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.Propagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.Propagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Description copied from interface: getAttitudeProvider Get the attitude provider.
        
        Specified by: getAttitudeProvider in interface PropagatorBuilder
        
        Returns:
            the attitude provider
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame in which the orbit is propagated.
        
        Specified by: getFrame in interface PropagatorBuilder
        
        Returns:
            frame in which the orbit is propagated
        
        
        """
        ...
    def getInitialOrbitDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date of the initial orbit.
        
        Specified by: getInitialOrbitDate in interface PropagatorBuilder
        
        Returns:
            date of the initial orbit
        
        
        """
        ...
    def getMass(self) -> float:
        """
        Description copied from interface: getMass Get the initial mass.
        
        Specified by: getMass in interface PropagatorBuilder
        
        Returns:
            the mass (kg)
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get the central attraction coefficient (µ - m³/s²) value.
        
        Specified by: getMu in interface PropagatorBuilder
        
        Returns:
            the central attraction coefficient (µ - m³/s²) value
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get the orbit type expected for the 6 first parameters in buildPropagator.
        
        Specified by: getOrbitType in interface PropagatorBuilder
        
        Returns:
            orbit type to use in buildPropagator
        
        Also see:
            buildPropagator,
            getPositionAngleType
        
        
        """
        ...
    def getOrbitalParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the drivers for the configurable orbital parameters. Orbital drivers should have only 1 value estimated (1 span)
        
        Specified by: getOrbitalParametersDrivers in interface PropagatorBuilder
        
        Returns:
            drivers for the configurable orbital parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get the position angle type expected for the 6 first parameters in buildPropagator.
        
        Specified by: getPositionAngleType in interface PropagatorBuilder
        
        Returns:
            position angle type to use in buildPropagator
        
        Also see:
            buildPropagator,
            getOrbitType
        
        
        """
        ...
    def getPropagationParametersDrivers(self) -> org.orekit.utils.ParameterDriversList:
        """
        Get the drivers for the configurable propagation parameters.
        
        The parameters typically correspond to force models.
        
        Specified by: getPropagationParametersDrivers in interface PropagatorBuilder
        
        Returns:
            drivers for the configurable propagation parameters
        
        
        """
        ...
    def getSelectedNormalizedParameters(self) -> typing.MutableSequence[float]:
        """
        Get the current value of selected normalized parameters.
        
        Specified by: getSelectedNormalizedParameters in interface PropagatorBuilder
        
        Returns:
            current value of selected normalized parameters
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def resetOrbit(self, newOrbit: org.orekit.orbits.Orbit) -> None:
        """
        Reset the orbit in the propagator builder.
        
        Specified by: resetOrbit in interface PropagatorBuilder
        
        Parameters:
            newOrbit (Orbit): New orbit to set in the propagator builder
        
        
        """
        ...

class PythonPropagatorConverter(PropagatorConverter):
    def __init__(self): ...
    @typing.overload
    def convert(self, list: java.util.List[org.orekit.propagation.SpacecraftState], boolean: bool, *string: str) -> org.orekit.propagation.Propagator:
        """
        Convert a propagator into another one.
        
        Specified by: convert in interface PropagatorConverter
        
        Parameters:
            source (Propagator): propagator to convert
            timeSpan (double): time span considered for conversion
            nbPoints (int): number of points for sampling over the time span
            freeParameters (String...): names of the free parameters
        
        Returns:
            adapted propagator
        
        public Propagator convert (List<SpacecraftState> states, boolean positionOnly, List<String> freeParameters)
        
        Find the propagator that minimize the mean square error for a sample of SpacecraftState.
        
        Specified by: convert in interface PropagatorConverter
        
        Parameters:
            states (List<SpacecraftState> states): spacecraft states sample to fit
            positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
            freeParameters (List<String> freeParameters): names of the free parameters
        
        Returns:
            adapted propagator
        
        public Propagator convert (List<SpacecraftState> states, boolean positionOnly, String... freeParameters)
        
        Find the propagator that minimize the mean square error for a sample of SpacecraftState.
        
        Specified by: convert in interface PropagatorConverter
        
        Parameters:
            states (List<SpacecraftState> states): spacecraft states sample to fit
            positionOnly (boolean): if true, consider only position data otherwise both position and velocity are used
            freeParameters (String...): names of the free parameters
        
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

_AbstractAnalyticalPropagatorBuilder__T = typing.TypeVar('_AbstractAnalyticalPropagatorBuilder__T', bound=org.orekit.propagation.analytical.AbstractAnalyticalPropagator)  # <T>
class AbstractAnalyticalPropagatorBuilder(AbstractPropagatorBuilder[_AbstractAnalyticalPropagatorBuilder__T], typing.Generic[_AbstractAnalyticalPropagatorBuilder__T]):
    """
    Abstract class for propagator builders of analytical models (except for ephemeris i.e. interpolated ones).
    
    Since:
        12.2
    """
    def addImpulseManeuver(self, impulseManeuver: org.orekit.forces.maneuvers.ImpulseManeuver) -> None:
        """
        Add impulse maneuver.
        
        Parameters:
            impulseManeuver (ImpulseManeuver): impulse maneuver
        
        
        """
        ...
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List[PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel:
        """
        Build a new batch least squares model.
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        
        """
        ...
    def clearImpulseManeuvers(self) -> None:
        """
        Remove all impulse maneuvers.
        """
        ...

_AbstractFixedSingleStepIntegratorBuilder__T = typing.TypeVar('_AbstractFixedSingleStepIntegratorBuilder__T', bound=org.hipparchus.ode.nonstiff.FixedStepRungeKuttaIntegrator)  # <T>
class AbstractFixedSingleStepIntegratorBuilder(AbstractIntegratorBuilder[_AbstractFixedSingleStepIntegratorBuilder__T], ExplicitRungeKuttaIntegratorBuilder, typing.Generic[_AbstractFixedSingleStepIntegratorBuilder__T]):
    """
    Abstract class for fixed-step, single-step integrator builder.
    
    Since:
        13.0
    
        class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.FixedStepRungeKuttaIntegrator?is`
    """
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> _AbstractFixedSingleStepIntegratorBuilder__T: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> _AbstractFixedSingleStepIntegratorBuilder__T: ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> _AbstractFixedSingleStepIntegratorBuilder__T: ...
    def getStep(self) -> float:
        """
        Getter for the step size.
        
        Returns:
            step
        
        
        """
        ...

_AbstractFixedStepFieldIntegratorBuilder__T = typing.TypeVar('_AbstractFixedStepFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_AbstractFixedStepFieldIntegratorBuilder__W = typing.TypeVar('_AbstractFixedStepFieldIntegratorBuilder__W', bound=org.hipparchus.ode.AbstractFieldIntegrator)  # <W>
class AbstractFixedStepFieldIntegratorBuilder(FieldAbstractIntegratorBuilder[_AbstractFixedStepFieldIntegratorBuilder__T, _AbstractFixedStepFieldIntegratorBuilder__W], typing.Generic[_AbstractFixedStepFieldIntegratorBuilder__T, _AbstractFixedStepFieldIntegratorBuilder__W]):
    """
    Abstract class for integrator builder using fixed step size.
    """
    ...

_AbstractIntegratedPropagatorBuilder__T = typing.TypeVar('_AbstractIntegratedPropagatorBuilder__T', bound=org.orekit.propagation.integration.AbstractIntegratedPropagator)  # <T>
class AbstractIntegratedPropagatorBuilder(AbstractPropagatorBuilder[_AbstractIntegratedPropagatorBuilder__T], typing.Generic[_AbstractIntegratedPropagatorBuilder__T]):
    """
    Abstract class for builders for integrator-based propagators.
    
    Since:
        13.0
    """
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> _AbstractIntegratedPropagatorBuilder__T:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> _AbstractIntegratedPropagatorBuilder__T:
        """
        Build a propagator from current value of selected normalized parameters.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Overrides: buildPropagator in class AbstractPropagatorBuilder
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def getIntegratorBuilder(self) -> ODEIntegratorBuilder:
        """
        Getter for integrator builder.
        
        Returns:
            builder
        
        
        """
        ...
    def getPropagationType(self) -> org.orekit.propagation.PropagationType:
        """
        Getter for the propagation type.
        
        Returns:
            propagation type
        
        
        """
        ...

_AbstractVariableStepFieldIntegratorBuilder__T = typing.TypeVar('_AbstractVariableStepFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_AbstractVariableStepFieldIntegratorBuilder__W = typing.TypeVar('_AbstractVariableStepFieldIntegratorBuilder__W', bound=org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator)  # <W>
class AbstractVariableStepFieldIntegratorBuilder(FieldAbstractIntegratorBuilder[_AbstractVariableStepFieldIntegratorBuilder__T, _AbstractVariableStepFieldIntegratorBuilder__W], typing.Generic[_AbstractVariableStepFieldIntegratorBuilder__T, _AbstractVariableStepFieldIntegratorBuilder__W]):
    """
    Abstract class for integrator builder using variable step size.
    """
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_AbstractVariableStepFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> _AbstractVariableStepFieldIntegratorBuilder__W: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_AbstractVariableStepFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> _AbstractVariableStepFieldIntegratorBuilder__W: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_AbstractVariableStepFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> _AbstractVariableStepFieldIntegratorBuilder__W: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_AbstractVariableStepFieldIntegratorBuilder__T]) -> _AbstractVariableStepFieldIntegratorBuilder__W: ...
    def getMaxStep(self) -> float:
        """
        Getter for the maximum step.
        
        Returns:
            max stepsize
        
        Since:
            13.0
        
        
        """
        ...
    def getMinStep(self) -> float:
        """
        Getter for the minimum step.
        
        Returns:
            min stepsize
        
        Since:
            13.0
        
        
        """
        ...
    def getToleranceProvider(self) -> org.orekit.propagation.ToleranceProvider:
        """
        Getter for the integration tolerance provider.
        
        Returns:
            tolerance provider
        
        Since:
            13.0
        
        
        """
        ...

_AbstractVariableStepIntegratorBuilder__T = typing.TypeVar('_AbstractVariableStepIntegratorBuilder__T', bound=org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator)  # <T>
class AbstractVariableStepIntegratorBuilder(AbstractIntegratorBuilder[_AbstractVariableStepIntegratorBuilder__T], typing.Generic[_AbstractVariableStepIntegratorBuilder__T]):
    """
    Abstract class for integrator builder using variable step size.
    
    Since:
        12.2
    """
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> _AbstractVariableStepIntegratorBuilder__T:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> _AbstractVariableStepIntegratorBuilder__T: ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> _AbstractVariableStepIntegratorBuilder__T:
        """
        Build a first order integrator. Non-orbit version.
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Overrides: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): absolute position-velocity vector
        
        Returns:
            a first order integrator ready to use
        
        Builds an integrator from input absolute and relative tolerances.
        
        Parameters:
            tolerances (double[][]): tolerance array
        
        Returns:
            integrator
        
        Since:
            13.0
        
        
        """
        ...
    def getMaxStep(self) -> float:
        """
        Getter for the maximum step.
        
        Returns:
            max stepsize
        
        Since:
            13.0
        
        
        """
        ...
    def getMinStep(self) -> float:
        """
        Getter for the minimum step.
        
        Returns:
            min stepsize
        
        Since:
            13.0
        
        
        """
        ...

class EphemerisPropagatorBuilder(AbstractPropagatorBuilder[org.orekit.propagation.analytical.Ephemeris]):
    """
    Builder for Ephemeris propagator.
    
    Since:
        11.3
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], int: int, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.StateCovariance], timeInterpolator2: org.orekit.time.TimeInterpolator[org.orekit.time.TimeStampedPair[org.orekit.orbits.Orbit, org.orekit.propagation.StateCovariance]], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], timeInterpolator: org.orekit.time.TimeInterpolator[org.orekit.propagation.SpacecraftState], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List[PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel:
        """
        Build a new batch least squares model.
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.AbstractPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.analytical.Ephemeris:
        """
        Build a propagator..
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'EphemerisPropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...

class FiniteDifferencePropagatorConverter(AbstractPropagatorConverter):
    """
    Propagator converter using finite differences to compute the Jacobian.
    
    Since:
        6.0
    """
    def __init__(self, factory: PropagatorBuilder, threshold: float, maxIterations: int):
        """
        Simple constructor.
        
        Parameters:
            factory (PropagatorBuilder): builder for adapted propagator
            threshold (double): absolute threshold for optimization algorithm
            maxIterations (int): maximum number of iterations for fitting
        
        
        """
        ...

class JacobianPropagatorConverter(AbstractPropagatorConverter):
    """
    Propagator converter using the real Jacobian.
    
    Since:
        6.0
    """
    def __init__(self, builder: 'NumericalPropagatorBuilder', threshold: float, maxIterations: int):
        """
        Simple constructor.
        
        Parameters:
            builder (NumericalPropagatorBuilder): builder for adapted propagator, it must be configured to generate CARTESIAN
                states
            threshold (double): absolute threshold for optimization algorithm
            maxIterations (int): maximum number of iterations for fitting
        
        
        """
        ...

_PythonAbstractPropagatorBuilder__T = typing.TypeVar('_PythonAbstractPropagatorBuilder__T', bound=org.orekit.propagation.AbstractPropagator)  # <T>
class PythonAbstractPropagatorBuilder(AbstractPropagatorBuilder[_PythonAbstractPropagatorBuilder__T], typing.Generic[_PythonAbstractPropagatorBuilder__T]):
    def __init__(self, templateOrbit: org.orekit.orbits.Orbit, PositionAngleType: org.orekit.orbits.PositionAngleType, positionScale: float, addDriverForCentralAttraction: bool):
        """
        Build a new instance.
        
        The template orbit is used as a model to createInitialOrbit. It defines the inertial frame, the central attraction coefficient, the orbit type, and is also used together with the positionScale to convert from the setNormalizedValue parameters used by the callers of this builder to the real orbital parameters.
        
        By default, all the getOrbitalParametersDrivers are selected, which means that if the builder is used for orbit determination or propagator conversion, all orbital parameters will be estimated. If only a subset of the orbital parameters must be estimated, caller must retrieve the orbital parameters by calling getOrbitalParametersDrivers and then call setSelected.
        
        Parameters:
            templateOrbit (Orbit): reference orbit from which real orbits will be built
            PositionAngleType (PositionAngleType): position angle type to use
            positionScale (double): scaling factor used for orbital parameters normalization (typically set to the expected standard deviation of the
                position)
            addDriverForCentralAttraction (boolean): if true, a ParameterDriver should be set up for central attraction coefficient
        
        Since:
            8.0
        
        
        """
        ...
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List[PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.AbstractBatchLSModel:
        """
        Build a new batch least squares model.
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> _PythonAbstractPropagatorBuilder__T:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> _PythonAbstractPropagatorBuilder__T: ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonAbstractPropagatorConverter(AbstractPropagatorConverter):
    def __init__(self, builder: PropagatorBuilder, threshold: float, maxIterations: int):
        """
        Build a new instance.
        
        Parameters:
            builder (PropagatorBuilder): propagator builder
            threshold (double): absolute convergence threshold for optimization algorithm
            maxIterations (int): maximum number of iterations for fitting
        
        
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
    def getModel(self) -> org.hipparchus.optim.nonlinear.vector.leastsquares.MultivariateJacobianFunction:
        """
        Get the Jacobian of the function computing position/velocity at sample points. Extension point for Python.
        
        Specified by: getModel in class AbstractPropagatorConverter
        
        Returns:
            Jacobian of the function computing position/velocity at sample points
        
        
        """
        ...
    def getObjectiveFunction(self) -> org.hipparchus.analysis.MultivariateVectorFunction:
        """
        Get the function computing position/velocity at sample points. Extension point for Python.
        
        Specified by: getObjectiveFunction in class AbstractPropagatorConverter
        
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

class PythonExplicitRungeKuttaIntegratorBuilder(ExplicitRungeKuttaIntegratorBuilder):
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
        
        Returns:
            a first order integrator ready to use
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator: ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.nonstiff.ExplicitRungeKuttaIntegrator:
        """
        Build a first order integrator. Non-orbit version.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Parameters:
            absolutePVCoordinates (AbsolutePVCoordinates): absolute position-velocity vector
        
        Returns:
            a first order integrator ready to use
        
        
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

_PythonFieldExplicitRungeKuttaIntegratorBuilder__T = typing.TypeVar('_PythonFieldExplicitRungeKuttaIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldExplicitRungeKuttaIntegratorBuilder(FieldExplicitRungeKuttaIntegratorBuilder[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T], typing.Generic[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T]):
    def __init__(self): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T]: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T]) -> org.hipparchus.ode.nonstiff.FieldExplicitRungeKuttaIntegrator[_PythonFieldExplicitRungeKuttaIntegratorBuilder__T]: ...
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
    def pythonExtension(self, long: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def toODEIntegratorBuilder(self) -> ExplicitRungeKuttaIntegratorBuilder:
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

_AbstractLimitedVariableStepFieldIntegratorBuilder__T = typing.TypeVar('_AbstractLimitedVariableStepFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_AbstractLimitedVariableStepFieldIntegratorBuilder__W = typing.TypeVar('_AbstractLimitedVariableStepFieldIntegratorBuilder__W', bound=org.hipparchus.ode.MultistepFieldIntegrator)  # <W>
class AbstractLimitedVariableStepFieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_AbstractLimitedVariableStepFieldIntegratorBuilder__T, _AbstractLimitedVariableStepFieldIntegratorBuilder__W], typing.Generic[_AbstractLimitedVariableStepFieldIntegratorBuilder__T, _AbstractLimitedVariableStepFieldIntegratorBuilder__W]):
    """
    Abstract class for integrator using a limited number of variable steps.
    """
    ...

class AdamsBashforthIntegratorBuilder(AbstractVariableStepIntegratorBuilder[org.hipparchus.ode.nonstiff.AdamsBashforthIntegrator]):
    """
    Builder for AdamsBashforthIntegrator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...

class AdamsMoultonIntegratorBuilder(AbstractVariableStepIntegratorBuilder[org.hipparchus.ode.nonstiff.AdamsMoultonIntegrator]):
    """
    Builder for AdamsMoultonIntegrator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...

class BrouwerLyddanePropagatorBuilder(AbstractAnalyticalPropagatorBuilder[org.orekit.propagation.analytical.BrouwerLyddanePropagator]):
    """
    Builder for Brouwer-Lyddane propagator.
    
    By default, Brouwer-Lyddane model considers only the perturbations due to zonal harmonics. However, for low Earth orbits, the magnitude of the perturbative acceleration due to atmospheric drag can be significant. Warren Phipps' 1992 thesis considered the atmospheric drag by time derivatives of the mean mean anomaly using the catch-all coefficient M2.
    
    Usually, M2 is adjusted during an orbit determination process, and it represents the combination of all un-modeled secular along-track effects (i.e. not just the atmospheric drag). The behavior of M2 is closed to the getBStar parameter for the TLE.
    
    If the value of M2 is equal to M2, the along-track secular effects are not considered in the dynamical model. Typical values for M2 are not known. It depends on the orbit type. However, the value of M2 must be very small (e.g. between 1.0e-14 and 1.0e-15). The unit of M2 is rad/s².
    
    To estimate the M2 parameter, it is necessary to call the getPropagationParametersDrivers method as follows:
    
    
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
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.AbstractPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.analytical.BrouwerLyddanePropagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'BrouwerLyddanePropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...
    def getM2Value(self) -> float:
        """
        Get the value of the M2 parameter.
        
        M2 represents the combination of all un-modeled secular along-track effects (e.g. drag). It is usually fitted during an orbit determination.
        
        Returns:
            the value of the M2 parameter
        
        Since:
            12.2
        
        
        """
        ...

_ClassicalRungeKuttaFieldIntegratorBuilder__T = typing.TypeVar('_ClassicalRungeKuttaFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ClassicalRungeKuttaFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_ClassicalRungeKuttaFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator[_ClassicalRungeKuttaFieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_ClassicalRungeKuttaFieldIntegratorBuilder__T], typing.Generic[_ClassicalRungeKuttaFieldIntegratorBuilder__T]):
    """
    Builder for ClassicalRungeKuttaFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _ClassicalRungeKuttaFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_ClassicalRungeKuttaFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_ClassicalRungeKuttaFieldIntegratorBuilder__T]) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_ClassicalRungeKuttaFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ClassicalRungeKuttaFieldIntegrator[_ClassicalRungeKuttaFieldIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'ClassicalRungeKuttaIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class ClassicalRungeKuttaIntegratorBuilder(AbstractFixedSingleStepIntegratorBuilder[org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator]):
    """
    Builder for ClassicalRungeKuttaIntegrator.
    
    Since:
        6.0
    """
    def __init__(self, step: float):
        """
        Build a new instance.
        
        Parameters:
            step (double): step size (s)
        
            class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator?is`
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator: ...

class DSSTPropagatorBuilder(AbstractIntegratedPropagatorBuilder[org.orekit.propagation.semianalytical.dsst.DSSTPropagator]):
    """
    Builder for DSST propagator.
    
    Since:
        10.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, double: float, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, double: float, propagationType: org.orekit.propagation.PropagationType, propagationType2: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, model: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None:
        """
        Add a force model to the global perturbation model.
        
        If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
        Parameters:
            model (DSSTForceModel): perturbing DSSTForceModel to add
        
        
        """
        ...
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List[PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.DSSTBatchLSModel:
        """
        Build a new batch least squares model.
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.integration.AbstractIntegratedPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.semianalytical.dsst.DSSTPropagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractIntegratedPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'DSSTPropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]:
        """
        Get the list of all force models.
        
        Returns:
            the list of all force models
        
        
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
            newOrbit (Orbit): newOrbit New orbit to set in the propagator builder
            orbitType (PropagationType): orbit type (MEAN or OSCULATING)
        
        
        """
        ...
    @typing.overload
    def resetOrbit(self, orbit: org.orekit.orbits.Orbit, propagationType: org.orekit.propagation.PropagationType) -> None: ...

_DormandPrince54FieldIntegratorBuilder__T = typing.TypeVar('_DormandPrince54FieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince54FieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_DormandPrince54FieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.DormandPrince54FieldIntegrator[_DormandPrince54FieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_DormandPrince54FieldIntegratorBuilder__T], typing.Generic[_DormandPrince54FieldIntegratorBuilder__T]):
    """
    Builder for DormandPrince54FieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_DormandPrince54FieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_DormandPrince54FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_DormandPrince54FieldIntegratorBuilder__T]) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator: ...
    def toODEIntegratorBuilder(self) -> 'DormandPrince54IntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class DormandPrince54IntegratorBuilder(AbstractVariableStepIntegratorBuilder[org.hipparchus.ode.nonstiff.DormandPrince54Integrator], ExplicitRungeKuttaIntegratorBuilder):
    """
    Builder for DormandPrince54Integrator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator: ...
    @typing.overload
    def buildIntegrator(self, tolerances: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator:
        """
        Builds an integrator from input absolute and relative tolerances.
        
        Specified by: buildIntegrator in class AbstractVariableStepIntegratorBuilder
        
        Parameters:
            tolerances (double[][]): tolerance array
        
        Returns:
            integrator
        
        
        """
        ...

_DormandPrince853FieldIntegratorBuilder__T = typing.TypeVar('_DormandPrince853FieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class DormandPrince853FieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_DormandPrince853FieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.DormandPrince853FieldIntegrator[_DormandPrince853FieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_DormandPrince853FieldIntegratorBuilder__T], typing.Generic[_DormandPrince853FieldIntegratorBuilder__T]):
    """
    Builder for DormandPrince853FieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_DormandPrince853FieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_DormandPrince853FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_DormandPrince853FieldIntegratorBuilder__T]) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator: ...
    def toODEIntegratorBuilder(self) -> 'DormandPrince853IntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class DormandPrince853IntegratorBuilder(AbstractVariableStepIntegratorBuilder[org.hipparchus.ode.nonstiff.DormandPrince853Integrator], ExplicitRungeKuttaIntegratorBuilder):
    """
    Builder for DormandPrince853Integrator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator: ...
    @typing.overload
    def buildIntegrator(self, tolerances: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator:
        """
        Builds an integrator from input absolute and relative tolerances.
        
        Specified by: buildIntegrator in class AbstractVariableStepIntegratorBuilder
        
        Parameters:
            tolerances (double[][]): tolerance array
        
        Returns:
            integrator
        
        
        """
        ...

class EcksteinHechlerPropagatorBuilder(AbstractAnalyticalPropagatorBuilder[org.orekit.propagation.analytical.EcksteinHechlerPropagator]):
    """
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
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.AbstractPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.analytical.EcksteinHechlerPropagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'EcksteinHechlerPropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...

_EulerFieldIntegratorBuilder__T = typing.TypeVar('_EulerFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class EulerFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_EulerFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.EulerFieldIntegrator[_EulerFieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_EulerFieldIntegratorBuilder__T], typing.Generic[_EulerFieldIntegratorBuilder__T]):
    """
    Builder for EulerFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _EulerFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_EulerFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_EulerFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_EulerFieldIntegratorBuilder__T]) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_EulerFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.EulerFieldIntegrator[_EulerFieldIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'EulerIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class EulerIntegratorBuilder(AbstractFixedSingleStepIntegratorBuilder[org.hipparchus.ode.nonstiff.EulerIntegrator]):
    """
    Builder for EulerIntegrator.
    
    Since:
        6.0
    """
    def __init__(self, step: float):
        """
        Build a new instance.
        
        Parameters:
            step (double): step size (s)
        
            class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.EulerIntegrator?is`
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.EulerIntegrator: ...

_GillFieldIntegratorBuilder__T = typing.TypeVar('_GillFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class GillFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_GillFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.GillFieldIntegrator[_GillFieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_GillFieldIntegratorBuilder__T], typing.Generic[_GillFieldIntegratorBuilder__T]):
    """
    Builder for GillFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _GillFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_GillFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_GillFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_GillFieldIntegratorBuilder__T]) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_GillFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.GillFieldIntegrator[_GillFieldIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'GillIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class GillIntegratorBuilder(AbstractFixedSingleStepIntegratorBuilder[org.hipparchus.ode.nonstiff.GillIntegrator]):
    """
    Builder for GillIntegrator.
    
    Since:
        6.0
    """
    def __init__(self, step: float):
        """
        Build a new instance.
        
        Parameters:
            step (double): step size (s)
        
            class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.GillIntegrator?is`
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.GillIntegrator: ...

class GraggBulirschStoerIntegratorBuilder(AbstractVariableStepIntegratorBuilder[org.hipparchus.ode.nonstiff.GraggBulirschStoerIntegrator]):
    """
    Builder for GraggBulirschStoerIntegrator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...

_HighamHall54FieldIntegratorBuilder__T = typing.TypeVar('_HighamHall54FieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class HighamHall54FieldIntegratorBuilder(AbstractVariableStepFieldIntegratorBuilder[_HighamHall54FieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.HighamHall54FieldIntegrator[_HighamHall54FieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_HighamHall54FieldIntegratorBuilder__T], typing.Generic[_HighamHall54FieldIntegratorBuilder__T]):
    """
    Builder for HighamHall54Integrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_HighamHall54FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_HighamHall54FieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_HighamHall54FieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_HighamHall54FieldIntegratorBuilder__T]) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeFieldIntegrator: ...
    def toODEIntegratorBuilder(self) -> 'HighamHall54IntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class HighamHall54IntegratorBuilder(AbstractVariableStepIntegratorBuilder[org.hipparchus.ode.nonstiff.HighamHall54Integrator], ExplicitRungeKuttaIntegratorBuilder):
    """
    Builder for HighamHall54Integrator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator: ...
    @typing.overload
    def buildIntegrator(self, tolerances: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.nonstiff.AdaptiveStepsizeIntegrator:
        """
        Builds an integrator from input absolute and relative tolerances.
        
        Specified by: buildIntegrator in class AbstractVariableStepIntegratorBuilder
        
        Parameters:
            tolerances (double[][]): tolerance array
        
        Returns:
            integrator
        
        
        """
        ...

class KeplerianPropagatorBuilder(AbstractAnalyticalPropagatorBuilder[org.orekit.propagation.analytical.KeplerianPropagator]):
    """
    Builder for Keplerian propagator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngleType: org.orekit.orbits.PositionAngleType, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.AbstractPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.analytical.KeplerianPropagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'KeplerianPropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...

_LutherFieldIntegratorBuilder__T = typing.TypeVar('_LutherFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class LutherFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_LutherFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.LutherFieldIntegrator[_LutherFieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_LutherFieldIntegratorBuilder__T], typing.Generic[_LutherFieldIntegratorBuilder__T]):
    """
    Builder for LutherFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _LutherFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_LutherFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_LutherFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_LutherFieldIntegratorBuilder__T]) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_LutherFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.LutherFieldIntegrator[_LutherFieldIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'LutherIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class LutherIntegratorBuilder(AbstractFixedSingleStepIntegratorBuilder[org.hipparchus.ode.nonstiff.LutherIntegrator]):
    """
    Builder for LutherIntegrator.
    
    Since:
        7.1
    """
    def __init__(self, step: float):
        """
        Build a new instance.
        
        Parameters:
            step (double): step size (s)
        
            class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.LutherIntegrator?is`
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.LutherIntegrator: ...

_MidpointFieldIntegratorBuilder__T = typing.TypeVar('_MidpointFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class MidpointFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_MidpointFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.MidpointFieldIntegrator[_MidpointFieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_MidpointFieldIntegratorBuilder__T], typing.Generic[_MidpointFieldIntegratorBuilder__T]):
    """
    Builder for MidpointFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _MidpointFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_MidpointFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_MidpointFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_MidpointFieldIntegratorBuilder__T]) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_MidpointFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.MidpointFieldIntegrator[_MidpointFieldIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'MidpointIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class MidpointIntegratorBuilder(AbstractFixedSingleStepIntegratorBuilder[org.hipparchus.ode.nonstiff.MidpointIntegrator]):
    """
    Builder for MidpointIntegrator.
    
    Since:
        6.0
    """
    def __init__(self, step: float):
        """
        Build a new instance.
        
        Parameters:
            step (double): step size (s)
        
            class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.MidpointIntegrator?is`
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.MidpointIntegrator: ...

class NumericalPropagatorBuilder(AbstractIntegratedPropagatorBuilder[org.orekit.propagation.numerical.NumericalPropagator]):
    """
    Builder for numerical propagator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngleType: org.orekit.orbits.PositionAngleType, double: float): ...
    @typing.overload
    def __init__(self, orbit: org.orekit.orbits.Orbit, oDEIntegratorBuilder: ODEIntegratorBuilder, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, model: org.orekit.forces.ForceModel) -> None:
        """
        Add a force model to the global perturbation model.
        
        If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
        Parameters:
            model (ForceModel): perturbing ForceModel to add
        
        
        """
        ...
    def addImpulseManeuver(self, impulseManeuver: org.orekit.forces.maneuvers.ImpulseManeuver) -> None:
        """
        Add impulse maneuver.
        
        Parameters:
            impulseManeuver (ImpulseManeuver): impulse maneuver
        
        Since:
            12.2
        
        
        """
        ...
    def buildLeastSquaresModel(self, builders: typing.Union[typing.List[PropagatorBuilder], jpype.JArray], measurements: java.util.List[org.orekit.estimation.measurements.ObservedMeasurement[typing.Any]], estimatedMeasurementsParameters: org.orekit.utils.ParameterDriversList, observer: typing.Union[org.orekit.estimation.leastsquares.ModelObserver, typing.Callable]) -> org.orekit.estimation.leastsquares.BatchLSModel:
        """
        Build a new batch least squares model.
        
        Parameters:
            builders (PropagatorBuilder[]): builders to use for propagation
            measurements (List<ObservedMeasurement<?>>): measurements
            estimatedMeasurementsParameters (ParameterDriversList): estimated measurements parameters
            observer (ModelObserver): observer to be notified at model calls
        
        Returns:
            a new model for the Batch Least Squares orbit determination
        
        
        """
        ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.integration.AbstractIntegratedPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.numerical.NumericalPropagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractIntegratedPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clearImpulseManeuvers(self) -> None:
        """
        Remove all impulse maneuvers.
        
        Since:
            12.2
        
        
        """
        ...
    def clone(self) -> 'NumericalPropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]:
        """
        Get the list of all force models.
        
        Returns:
            the list of all force models
        
        Since:
            9.2
        
        
        """
        ...

class TLEPropagatorBuilder(AbstractAnalyticalPropagatorBuilder[org.orekit.propagation.analytical.tle.TLEPropagator]):
    """
    Builder for TLEPropagator.
    
    Since:
        6.0
    """
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, dataContext: org.orekit.data.DataContext, tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, dataContext: org.orekit.data.DataContext, tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, tLE: org.orekit.propagation.analytical.tle.TLE, positionAngleType: org.orekit.orbits.PositionAngleType, double: float, tleGenerationAlgorithm: org.orekit.propagation.analytical.tle.generation.TleGenerationAlgorithm): ...
    @typing.overload
    def buildPropagator(self) -> org.orekit.propagation.AbstractPropagator: ...
    @typing.overload
    def buildPropagator(self, normalizedParameters: typing.Union[typing.List[float], jpype.JArray]) -> org.orekit.propagation.analytical.tle.TLEPropagator:
        """
        Build a propagator.
        
        Specified by: buildPropagator in interface PropagatorBuilder
        
        Specified by: buildPropagator in class AbstractPropagatorBuilder
        
        Parameters:
            normalizedParameters (double[]): normalized values for the selected parameters
        
        Returns:
            an initialized propagator
        
        
        """
        ...
    def clone(self) -> 'TLEPropagatorBuilder':
        """
        ..
        
        Overrides: clone in class AbstractPropagatorBuilder
        
        
        """
        ...
    def getTemplateTLE(self) -> org.orekit.propagation.analytical.tle.TLE:
        """
        Getter for the template TLE.
        
        Returns:
            the template TLE
        
        
        """
        ...

_ThreeEighthesFieldIntegratorBuilder__T = typing.TypeVar('_ThreeEighthesFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class ThreeEighthesFieldIntegratorBuilder(AbstractFixedStepFieldIntegratorBuilder[_ThreeEighthesFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator[_ThreeEighthesFieldIntegratorBuilder__T]], FieldExplicitRungeKuttaIntegratorBuilder[_ThreeEighthesFieldIntegratorBuilder__T], typing.Generic[_ThreeEighthesFieldIntegratorBuilder__T]):
    """
    Builder for ThreeEighthesFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, double: float): ...
    @typing.overload
    def __init__(self, t: _ThreeEighthesFieldIntegratorBuilder__T): ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_ThreeEighthesFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_ThreeEighthesFieldIntegratorBuilder__T], orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, fieldAbsolutePVCoordinates: org.orekit.utils.FieldAbsolutePVCoordinates[_ThreeEighthesFieldIntegratorBuilder__T]) -> org.hipparchus.ode.AbstractFieldIntegrator: ...
    @typing.overload
    def buildIntegrator(self, field: org.hipparchus.Field[_ThreeEighthesFieldIntegratorBuilder__T], orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ThreeEighthesFieldIntegrator[_ThreeEighthesFieldIntegratorBuilder__T]: ...
    def toODEIntegratorBuilder(self) -> 'ThreeEighthesIntegratorBuilder':
        """
        Form a non-Field equivalent.
        
        Specified by: toODEIntegratorBuilder in interface FieldExplicitRungeKuttaIntegratorBuilder
        
        Specified by: toODEIntegratorBuilder in interface FieldODEIntegratorBuilder
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

class ThreeEighthesIntegratorBuilder(AbstractFixedSingleStepIntegratorBuilder[org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator]):
    """
    Builder for ThreeEighthesIntegrator.
    
    Since:
        6.0
    """
    def __init__(self, step: float):
        """
        Build a new instance.
        
        Parameters:
            step (double): step size (s)
        
            class:`~org.orekit.propagation.conversion.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator?is`
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> org.hipparchus.ode.AbstractIntegrator:
        """
        Build a first order integrator.
        
        Specified by: buildIntegrator in interface ExplicitRungeKuttaIntegratorBuilder
        
        Specified by: buildIntegrator in interface ODEIntegratorBuilder
        
        Specified by: buildIntegrator in class AbstractIntegratorBuilder
        
        Parameters:
            orbit (Orbit): reference orbit
            orbitType (OrbitType): orbit type to use
            angleType (PositionAngleType): position angle type to use
        
        Returns:
            a first order integrator ready to use
        
        
        """
        ...
    @typing.overload
    def buildIntegrator(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> org.hipparchus.ode.AbstractIntegrator: ...
    @typing.overload
    def buildIntegrator(self, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType, positionAngleType: org.orekit.orbits.PositionAngleType) -> org.hipparchus.ode.nonstiff.ThreeEighthesIntegrator: ...

_AdamsBashforthFieldIntegratorBuilder__T = typing.TypeVar('_AdamsBashforthFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsBashforthFieldIntegratorBuilder(AbstractLimitedVariableStepFieldIntegratorBuilder[_AdamsBashforthFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.AdamsBashforthFieldIntegrator[_AdamsBashforthFieldIntegratorBuilder__T]], typing.Generic[_AdamsBashforthFieldIntegratorBuilder__T]):
    """
    Builder for AdamsBashforthFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    def toODEIntegratorBuilder(self) -> AdamsBashforthIntegratorBuilder:
        """
        Form a non-Field equivalent.
        
        Returns:
            ODE integrator builder
        
        
        """
        ...

_AdamsMoultonFieldIntegratorBuilder__T = typing.TypeVar('_AdamsMoultonFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class AdamsMoultonFieldIntegratorBuilder(AbstractLimitedVariableStepFieldIntegratorBuilder[_AdamsMoultonFieldIntegratorBuilder__T, org.hipparchus.ode.nonstiff.AdamsMoultonFieldIntegrator[_AdamsMoultonFieldIntegratorBuilder__T]], typing.Generic[_AdamsMoultonFieldIntegratorBuilder__T]):
    """
    Builder for AdamsMoultonFieldIntegrator.
    
    Since:
        12.0
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider): ...
    def toODEIntegratorBuilder(self) -> AdamsMoultonIntegratorBuilder:
        """
        Form a non-Field equivalent.
        
        Returns:
            ODE integrator builder
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion")``.

    AbstractAnalyticalPropagatorBuilder: typing.Type[AbstractAnalyticalPropagatorBuilder]
    AbstractFixedSingleStepIntegratorBuilder: typing.Type[AbstractFixedSingleStepIntegratorBuilder]
    AbstractFixedStepFieldIntegratorBuilder: typing.Type[AbstractFixedStepFieldIntegratorBuilder]
    AbstractIntegratedPropagatorBuilder: typing.Type[AbstractIntegratedPropagatorBuilder]
    AbstractIntegratorBuilder: typing.Type[AbstractIntegratorBuilder]
    AbstractLimitedVariableStepFieldIntegratorBuilder: typing.Type[AbstractLimitedVariableStepFieldIntegratorBuilder]
    AbstractPropagatorBuilder: typing.Type[AbstractPropagatorBuilder]
    AbstractPropagatorConverter: typing.Type[AbstractPropagatorConverter]
    AbstractVariableStepFieldIntegratorBuilder: typing.Type[AbstractVariableStepFieldIntegratorBuilder]
    AbstractVariableStepIntegratorBuilder: typing.Type[AbstractVariableStepIntegratorBuilder]
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
    ExplicitRungeKuttaIntegratorBuilder: typing.Type[ExplicitRungeKuttaIntegratorBuilder]
    FieldAbstractIntegratorBuilder: typing.Type[FieldAbstractIntegratorBuilder]
    FieldExplicitRungeKuttaIntegratorBuilder: typing.Type[FieldExplicitRungeKuttaIntegratorBuilder]
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
    PythonExplicitRungeKuttaIntegratorBuilder: typing.Type[PythonExplicitRungeKuttaIntegratorBuilder]
    PythonFieldExplicitRungeKuttaIntegratorBuilder: typing.Type[PythonFieldExplicitRungeKuttaIntegratorBuilder]
    PythonFieldODEIntegratorBuilder: typing.Type[PythonFieldODEIntegratorBuilder]
    PythonODEIntegratorBuilder: typing.Type[PythonODEIntegratorBuilder]
    PythonPropagatorBuilder: typing.Type[PythonPropagatorBuilder]
    PythonPropagatorConverter: typing.Type[PythonPropagatorConverter]
    TLEPropagatorBuilder: typing.Type[TLEPropagatorBuilder]
    ThreeEighthesFieldIntegratorBuilder: typing.Type[ThreeEighthesFieldIntegratorBuilder]
    ThreeEighthesIntegratorBuilder: typing.Type[ThreeEighthesIntegratorBuilder]
    averaging: org.orekit.propagation.conversion.averaging.__module_protocol__
    osc2mean: org.orekit.propagation.conversion.osc2mean.__module_protocol__
