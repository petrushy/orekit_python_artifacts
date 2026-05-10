
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.ode
import org.hipparchus.ode.nonstiff
import org.orekit.attitudes
import org.orekit.data
import org.orekit.forces
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.gnss.data
import org.orekit.propagation.integration
import org.orekit.propagation.numerical.cr3bp
import org.orekit.time
import org.orekit.utils
import typing



class EpochDerivativesEquations(org.orekit.propagation.integration.AdditionalDerivativesProvider):
    """
    Computes derivatives of the acceleration, including ThirdBodyAttraction. AdditionalDerivativesProvider computing the partial derivatives of the state (orbit) with respect to initial state and force models parameters.
    
    This set of equations are automatically added to a NumericalPropagator in order to compute partial derivatives of the orbit along with the orbit itself. This is useful for example in orbit determination applications.
    
    The partial derivatives with respect to initial state can be either dimension 6 (orbit only) or 7 (orbit and mass).
    
    The partial derivatives with respect to force models parameters has a dimension equal to the number of selected parameters. Parameters selection is implemented at ForceModel level. Users must retrieve a ParameterDriver using getParameterDriver and then select it by calling setSelected.
    
    If several force models provide different ParameterDriver for the same parameter name, selecting any of these drivers has the side effect of selecting all the drivers for this shared parameter. In this case, the partial derivatives will be the sum of the partial derivatives contributed by the corresponding force models. This case typically arises for central attraction coefficient, which has an influence on NewtonianAttraction, HolmesFeatherstoneAttractionModel, and Relativity.
    
    Since:
        10.2
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    State dimension, fixed to 6.
    
    Also see:
        constant
    
    
    """
    def __init__(self, name: str, propagator: 'NumericalPropagator'):
        """
        Simple constructor.
        
        Upon construction, this set of equations is automatically added to the propagator by calling its addAdditionalDerivativesProvider method. So there is no need to call this method explicitly for these equations.
        
        Parameters:
            name (String): name of the partial derivatives equations
            propagator (NumericalPropagator): the propagator that will handle the orbit propagation
        
        
        """
        ...
    def combinedDerivatives(self, s: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.integration.CombinedDerivatives:
        """
        Compute the derivatives related to the additional state (and optionally main state increments).
        
        Specified by: combinedDerivatives in interface AdditionalDerivativesProvider
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Get the dimension of the generated derivative.
        
        Specified by: getDimension in interface AdditionalDerivativesProvider
        
        Returns:
            dimension of the generated
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name of the additional derivatives (which will become state once integrated).
        
        Specified by: getName in interface AdditionalDerivativesProvider
        
        Returns:
            name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, s0: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Set the initial value of the Jacobian with respect to state and parameter.
        
        This method is equivalent to call setInitialJacobians with dYdY0 set to the identity matrix and dYdP set to a zero matrix.
        
        The force models parameters for which partial derivatives are desired, must have been setSelected before this method is called, so proper matrices dimensions are used.
        
        Parameters:
            s0 (SpacecraftState): initial state
        
        Returns:
            state with initial Jacobians added
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, s1: org.orekit.propagation.SpacecraftState, dY1dY0: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], dY1dP: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> org.orekit.propagation.SpacecraftState:
        """
        Set the initial value of the Jacobian with respect to state and parameter.
        
        The returned state must be added to the propagator (it is not done automatically, as the user may need to add more states to it).
        
        The force models parameters for which partial derivatives are desired, must have been setSelected before this method is called, and the dY1dP matrix dimension must be consistent with the selection.
        
        Parameters:
            s1 (SpacecraftState): current state
            dY1dY0 (double[][]): Jacobian of current state at time t₁ with respect to state at some previous time t₀ (must be 6x6)
            dY1dP (double[][]): Jacobian of current state at time t₁ with respect to parameters (may be null if no parameters are selected)
        
        Returns:
            state with initial Jacobians added
        
        Set the Jacobian with respect to state into a one-dimensional additional state array.
        
        This method converts the Jacobians to Cartesian parameters and put the converted data in the one-dimensional p array.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            dY1dY0 (double[][]): Jacobian of current state at time t₁ with respect to state at some previous time t₀
            dY1dP (double[][]): Jacobian of current state at time t₁ with respect to parameters (may be null if there are no parameters)
            p (double[]): placeholder where to put the one-dimensional additional state
        
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, state: org.orekit.propagation.SpacecraftState, dY1dY0: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], dY1dP: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], p: typing.Union[typing.List[float], jpype.JArray]) -> None: ...

_FieldNumericalPropagator__T = typing.TypeVar('_FieldNumericalPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNumericalPropagator(org.orekit.propagation.integration.FieldAbstractIntegratedPropagator[_FieldNumericalPropagator__T], typing.Generic[_FieldNumericalPropagator__T]):
    """
    This class propagates FieldOrbit using numerical integration.
    
    Numerical propagation is much more accurate than analytical propagation like for example KeplerianPropagator or EcksteinHechlerPropagator, but requires a few more steps to set up to be used properly. Whereas analytical propagators are configured only thanks to their various constructors and can be used immediately after construction, numerical propagators configuration involve setting several parameters between construction time and propagation time.
    
    The configuration parameters that can be set are:
    
      - the initial spacecraft state (setInitialState)
      - the central attraction coefficient (setMu)
      - the various force models (addForceModel,
        removeForceModels)
      - the OrbitType of orbital parameters to be used for propagation
        (setOrbitType),
      - the PositionAngleType of position angle to be used in orbital parameters to be used for
        propagation where it is relevant
        (setPositionAngleType),
      - whether FieldAdditionalDerivativesProvider should be propagated along with
        orbital state
        (addAdditionalDerivativesProvider),
      - the discrete events that should be triggered during propagation
        (addEventDetector,
        clearEventsDetectors)
      - the binding logic with the rest of the application
        (getMultiplexer)
    
    From these configuration parameters, only the initial state is mandatory. The default propagation settings are in EQUINOCTIAL parameters with ECCENTRIC longitude argument. If the central attraction coefficient is not explicitly specified, the one used to define the initial orbit will be used. However, specifying only the initial state and perhaps the central attraction coefficient would mean the propagator would use only Keplerian forces. In this case, the simpler KeplerianPropagator class would perhaps be more effective.
    
    The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the absolute and/or relative errors thresholds.
    
    The state that is seen by the integrator is a simple seven elements double array. The six first elements are either:
    
      - the FieldEquinoctialOrbit (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ
        :sub:`M` or λ :sub:`E` or λ :sub:`v` ) in meters and radians,
      - the FieldKeplerianOrbit (a, e, i, ω, Ω, M or E or v) in meters and radians,
      - the FieldCircularOrbit (a, e :sub:`x` , e :sub:`y` , i, Ω, α :sub:`M` or α :sub:`E` or α
        :sub:`v` ) in meters and radians,
      - the FieldCartesianOrbit (x, y, z, v :sub:`x` , v :sub:`y` , v :sub:`z` ) in meters and
        meters per seconds.
    
    The last element is the mass in kilograms.
    
    The following code snippet shows a typical setting for Low Earth Orbit propagation in equinoctial parameters and true longitude argument:
    
    
     final T          zero      = field.getZero();
     final T          dP        = zero.add(0.001);
     final T          minStep   = zero.add(0.001);
     final T          maxStep   = zero.add(500);
     final T          initStep  = zero.add(60);
     final double[][] tolerance = ToleranceProvider.getDefaultToleranceProvider(dP).getTolerances(orbit, OrbitType.EQUINOCTIAL);
     AdaptiveStepsizeFieldIntegrator<T> integrator = new DormandPrince853FieldIntegrator<>(field, minStep, maxStep, tolerance[0], tolerance[1]);
     integrator.setInitialStepSize(initStep);
     propagator = new FieldNumericalPropagator<>(field, integrator);
     
    
    By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a new propagation to be started from there without recomputing the part already performed. This behaviour can be changed by calling setResetAtEnd.
    
    Beware the same instance cannot be used simultaneously by different threads, the class is not thread-safe.
    
    Also see:
        FieldSpacecraftState, ForceModel,
        FieldOrekitStepHandler,
        FieldOrekitFixedStepHandler,
        FieldIntegratedEphemeris,
        FieldTimeDerivativesEquations
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNumericalPropagator__T], integrator: org.hipparchus.ode.FieldODEIntegrator[_FieldNumericalPropagator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNumericalPropagator__T], integrator: org.hipparchus.ode.FieldODEIntegrator[_FieldNumericalPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, model: org.orekit.forces.ForceModel) -> None:
        """
        Add a force model to the global perturbation model.
        
        If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
        Parameters:
            model (ForceModel): perturbing ForceModel to add
        
        Also see:
            removeForceModels,
            setMu
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]:
        """
        Get all the force models, perturbing forces and Newtonian attraction included.
        
        Returns:
            list of perturbing force models, with Newtonian attraction being the last one
        
        Since:
            9.1
        
        Also see:
            addForceModel,
            setMu
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get propagation parameter type.
        
        Overrides: getOrbitType in class FieldAbstractIntegratedPropagator
        
        Returns:
            orbit type used for propagation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get propagation parameter type.
        
        Overrides: getPositionAngleType in class FieldAbstractIntegratedPropagator
        
        Returns:
            angle type to use for propagation
        
        
        """
        ...
    def removeForceModels(self) -> None:
        """
        Remove all perturbing force models from the global perturbation model.
        
        Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will follow a Keplerian evolution only.
        
        Also see:
            addForceModel
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldNumericalPropagator__T], propagationType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldNumericalPropagator__T]) -> None: ...
    def setIgnoreCentralAttraction(self, ignoreCentralAttraction: bool) -> None:
        """
        Set the flag to ignore or not the creation of a NewtonianAttraction.
        
        Parameters:
            ignoreCentralAttraction (boolean): if true, NewtonianAttraction is not added automatically if missing
        
        
        """
        ...
    def setInitialState(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldNumericalPropagator__T]) -> None:
        """
        Set the initial state.
        
        Parameters:
            initialState (FieldSpacecraftState<FieldNumericalPropagator> initialState): initial state
        
        
        """
        ...
    def setMu(self, mu: _FieldNumericalPropagator__T) -> None:
        """
        Set the central attraction coefficient μ.
        
        Setting the central attraction coefficient is equivalent to addForceModel a NewtonianAttraction force model.
        
        Overrides: setMu in class FieldAbstractIntegratedPropagator
        
        Parameters:
            mu (FieldNumericalPropagator): central attraction coefficient (m³/s²)
        
        Also see:
            addForceModel,
            getAllForceModels
        
        
        """
        ...
    def setOrbitType(self, orbitType: org.orekit.orbits.OrbitType) -> None:
        """
        Set propagation orbit type.
        
        Overrides: setOrbitType in class FieldAbstractIntegratedPropagator
        
        Parameters:
            orbitType (OrbitType): orbit type to use for propagation
        
        
        """
        ...
    def setPositionAngleType(self, positionAngleType: org.orekit.orbits.PositionAngleType) -> None:
        """
        Set position angle type.
        
        The position parameter type is meaningful only if getOrbitType support it. As an example, it is not meaningful for propagation in CARTESIAN parameters.
        
        Overrides: setPositionAngleType in class FieldAbstractIntegratedPropagator
        
        Parameters:
            positionAngleType (PositionAngleType): angle type to use for propagation
        
        
        """
        ...
    _tolerances_0__T = typing.TypeVar('_tolerances_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _tolerances_1__T = typing.TypeVar('_tolerances_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tolerances(dP: _tolerances_0__T, dV: _tolerances_0__T, orbit: org.orekit.orbits.FieldOrbit[_tolerances_0__T], type: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(dP: _tolerances_1__T, orbit: org.orekit.orbits.FieldOrbit[_tolerances_1__T], type: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

_FieldTimeDerivativesEquations__T = typing.TypeVar('_FieldTimeDerivativesEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTimeDerivativesEquations(typing.Generic[_FieldTimeDerivativesEquations__T]):
    """
    Interface summing up the contribution of several forces into orbit and mass derivatives.
    
    The aim of this interface is to gather the contributions of various perturbing forces expressed as accelerations into one set of time-derivatives of Orbit plus one mass derivatives. It implements Gauss equations for different kind of parameters.
    
    An implementation of this interface is automatically provided by AbstractIntegratedPropagator, which are either semi-analytical or numerical propagators.
    
    Also see:
        ForceModel, NumericalPropagator
    """
    def addKeplerContribution(self, mu: _FieldTimeDerivativesEquations__T) -> None:
        """
        Add the contribution of the Kepler evolution.
        
        Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve numerical accuracy.
        
        Parameters:
            mu (FieldTimeDerivativesEquations): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, q: _FieldTimeDerivativesEquations__T) -> None:
        """
        Add the contribution of the flow rate (dm/dt).
        
        Parameters:
            q (FieldTimeDerivativesEquations): the flow rate, must be negative (dm/dt)
        
        Raises:
            IllegalArgumentException: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, gamma: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTimeDerivativesEquations__T]) -> None:
        """
        Add the contribution of an acceleration expressed in some inertial frame.
        
        Parameters:
            gamma (FieldVector3D<FieldTimeDerivativesEquations> gamma): acceleration vector in the same inertial frame the spacecraft state is defined in (m/s²)
        
        Since:
            9.0
        
        
        """
        ...

class GLONASSNumericalPropagator(org.orekit.propagation.integration.AbstractIntegratedPropagator):
    """
    This class propagates GLONASS orbits using numerical integration.
    
    As recommended by the GLONASS Interface Control Document (ICD), a ClassicalRungeKuttaIntegrator shall be used to integrate the equations.
    
    Classical used of this orbit propagator is to compute GLONASS satellite coordinates from the navigation message.
    
    If the projections of luni-solar accelerations to axes of Greenwich geocentric coordinates getXDotDot, getYDotDot and getZDotDot are available in the navigation message; a transformation is performed to convert these accelerations into the correct coordinate system. In the case where they are not available into the navigation message, these accelerations are computed.
    
    Caution: The Glonass numerical propagator can only be used with GLONASSNavigationMessage. Using this propagator with a GLONASSAlmanac is prone to error.
    
    Also see:
        ` GLONASS Interface Control Document
        <http://russianspacesystems.ru/wp-content/uploads/2016/08/ICD-GLONASS-CDMA-General.-Edition-1.0-2016.pdf>`
    """
    def __init__(self, integrator: org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator, glonassOrbit: typing.Union[org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, typing.Callable], eci: org.orekit.frames.Frame, provider: org.orekit.attitudes.AttitudeProvider, mass: float, context: org.orekit.data.DataContext, isAccAvailable: bool):
        """
        Private constructor.
        
        Parameters:
            integrator (ClassicalRungeKuttaIntegrator): Runge-Kutta integrator
            glonassOrbit (GLONASSOrbitalElements): Glonass orbital elements
            eci (Frame): Earth Centered Inertial frame
            provider (AttitudeProvider): Attitude provider
            mass (double): Satellite mass (kg)
            context (DataContext): Data context
            isAccAvailable (boolean): true if the acceleration is transmitted within the navigation message
        
        
        """
        ...
    def getGLONASSOrbitalElements(self) -> org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements:
        """
        Gets the underlying GLONASS orbital elements.
        
        Returns:
            the underlying GLONASS orbital elements
        
        
        """
        ...
    @typing.overload
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState: ...
    @typing.overload
    def propagate(self, date: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
        Propagate towards a target date.
        
        Simple propagators use only the target date as the specification for computing the propagated state. More feature rich propagators can consider other information and provide different operating modes or G-stop facilities to stop at pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
        Specified by: propagate in interface Propagator
        
        Overrides: propagate in class AbstractIntegratedPropagator
        
        Parameters:
            date (AbsoluteDate): target date towards which orbit state should be propagated
        
        Returns:
            propagated state
        
        
        """
        ...

class GLONASSNumericalPropagatorBuilder:
    """
    This nested class aims at building a GLONASSNumericalPropagator.
    
    It implements the classical builder pattern.
    
    Caution: The Glonass numerical propagator can only be used with GLONASSNavigationMessage. Using this propagator with a GLONASSAlmanac is prone to error.
    
    Since:
        11.0
    """
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator, glonassOrbElt: typing.Union[org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, typing.Callable], isAccAvailable: bool): ...
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator, glonassOrbElt: typing.Union[org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, typing.Callable], isAccAvailable: bool, context: org.orekit.data.DataContext): ...
    def attitudeProvider(self, userProvider: org.orekit.attitudes.AttitudeProvider) -> 'GLONASSNumericalPropagatorBuilder':
        """
        Sets the attitude provider.
        
        Parameters:
            userProvider (AttitudeProvider): the attitude provider
        
        Returns:
            the updated builder
        
        
        """
        ...
    def build(self) -> GLONASSNumericalPropagator:
        """
        Finalizes the build.
        
        Returns:
            the built Glonass numerical propagator
        
        
        """
        ...
    def eci(self, inertial: org.orekit.frames.Frame) -> 'GLONASSNumericalPropagatorBuilder':
        """
        Sets the Earth Centered Inertial frame used for propagation.
        
        Parameters:
            inertial (Frame): the ECI frame
        
        Returns:
            the updated builder
        
        
        """
        ...
    def mass(self, userMass: float) -> 'GLONASSNumericalPropagatorBuilder':
        """
        Sets the mass.
        
        Parameters:
            userMass (double): the mass (in kg)
        
        Returns:
            the updated builder
        
        
        """
        ...

class NumericalPropagator(org.orekit.propagation.integration.AbstractIntegratedPropagator):
    """
    This class propagates Orbit using numerical integration.
    
    Numerical propagation is much more accurate than analytical propagation like for example KeplerianPropagator or EcksteinHechlerPropagator, but requires a few more steps to set up to be used properly. Whereas analytical propagators are configured only thanks to their various constructors and can be used immediately after construction, numerical propagators configuration involve setting several parameters between construction time and propagation time.
    
    The configuration parameters that can be set are:
    
      - the initial spacecraft state (setInitialState)
      - the central attraction coefficient (setMu)
      - the various force models (addForceModel,
        removeForceModels)
      - the OrbitType of orbital parameters to be used for propagation
        (setOrbitType),
      - the PositionAngleType of position angle to be used in orbital parameters to be used for
        propagation where it is relevant (setPositionAngleType),
      - whether MatricesHarvester (with the option to include mass if a 7x7 initial matrix is
        passed) should be propagated along with orbital state
        (setupMatricesComputation),
      - whether AdditionalDerivativesProvider should be propagated along with
        orbital state
        (addAdditionalDerivativesProvider),
      - the discrete events that should be triggered during propagation
        (addEventDetector,
        clearEventsDetectors)
      - the binding logic with the rest of the application (getMultiplexer)
    
    From these configuration parameters, only the initial state is mandatory. The default propagation settings are in EQUINOCTIAL parameters with ECCENTRIC longitude argument. If the central attraction coefficient is not explicitly specified, the one used to define the initial orbit will be used. However, specifying only the initial state and perhaps the central attraction coefficient would mean the propagator would use only Keplerian forces. In this case, the simpler KeplerianPropagator class would perhaps be more effective.
    
    The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the absolute and/or relative errors thresholds.
    
    The state that is seen by the integrator is a simple seven elements double array. The six first elements are either:
    
      - the EquinoctialOrbit (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ :sub:`M` or
        λ :sub:`E` or λ :sub:`v` ) in meters and radians,
      - the KeplerianOrbit (a, e, i, ω, Ω, M or E or v) in meters and radians,
      - the CircularOrbit (a, e :sub:`x` , e :sub:`y` , i, Ω, α :sub:`M` or α :sub:`E` or α
        :sub:`v` ) in meters and radians,
      - the CartesianOrbit (x, y, z, v :sub:`x` , v :sub:`y` , v :sub:`z` ) in meters and meters per
        seconds.
    
    The last element is the mass in kilograms and changes only during thrusters firings
    
    The following code snippet shows a typical setting for Low Earth Orbit propagation in equinoctial parameters and true longitude argument:
    
    
     final double dP       = 0.001;
     final double minStep  = 0.001;
     final double maxStep  = 500;
     final double initStep = 60;
     final double[][] tolerance = ToleranceProvider.getDefaultToleranceProvider(dP).getTolerances(orbit, OrbitType.EQUINOCTIAL);
     AdaptiveStepsizeIntegrator integrator = new DormandPrince853Integrator(minStep, maxStep, tolerance[0], tolerance[1]);
     integrator.setInitialStepSize(initStep);
     propagator = new NumericalPropagator(integrator);
     
    
    By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a new propagation to be started from there without recomputing the part already performed. This behaviour can be changed by calling setResetAtEnd.
    
    Beware the same instance cannot be used simultaneously by different threads, the class is not thread-safe.
    
    Also see:
        SpacecraftState, ForceModel,
        OrekitStepHandler,
        OrekitFixedStepHandler,
        IntegratedEphemeris,
        TimeDerivativesEquations
    """
    DEFAULT_ORBIT_TYPE: typing.ClassVar[org.orekit.orbits.OrbitType] = ...
    """
    Default orbit type.
    """
    DEFAULT_POSITION_ANGLE_TYPE: typing.ClassVar[org.orekit.orbits.PositionAngleType] = ...
    """
    Default position angle type.
    """
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.ODEIntegrator): ...
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.ODEIntegrator, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, model: org.orekit.forces.ForceModel) -> None:
        """
        Add a force model.
        
        If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
        Parameters:
            model (ForceModel): ForceModel to add (it can be either a perturbing force model or an instance of
                NewtonianAttraction)
        
        Also see:
            removeForceModels,
            setMu
        
        
        """
        ...
    def clearMatricesComputation(self) -> None:
        """
        Erases the internal matrices harvester.
        
        Overrides: clearMatricesComputation in class AbstractIntegratedPropagator
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]:
        """
        Get all the force models, perturbing forces and Newtonian attraction included.
        
        Returns:
            list of perturbing force models, with Newtonian attraction being the last one
        
        Also see:
            addForceModel,
            setMu
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get propagation parameter type.
        
        Overrides: getOrbitType in class AbstractIntegratedPropagator
        
        Returns:
            orbit type used for propagation, null for propagating using AbsolutePVCoordinates rather than
            Orbit
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get propagation parameter type.
        
        Overrides: getPositionAngleType in class AbstractIntegratedPropagator
        
        Returns:
            angle type to use for propagation
        
        
        """
        ...
    def removeForceModels(self) -> None:
        """
        Remove all force models (except central attraction).
        
        Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will follow a Keplerian evolution only.
        
        Also see:
            addForceModel
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the propagator initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
        
        
        """
        ...
    def setIgnoreCentralAttraction(self, ignoreCentralAttraction: bool) -> None:
        """
        Set the flag to ignore or not the creation of a NewtonianAttraction.
        
        Parameters:
            ignoreCentralAttraction (boolean): if true, NewtonianAttraction is not added automatically if missing
        
        
        """
        ...
    def setInitialState(self, initialState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Set the initial state.
        
        Parameters:
            initialState (SpacecraftState): initial state
        
        
        """
        ...
    def setMu(self, mu: float) -> None:
        """
        Set the central attraction coefficient μ.
        
        Setting the central attraction coefficient is equivalent to addForceModel a NewtonianAttraction force model. *
        
        Overrides: setMu in class AbstractIntegratedPropagator
        
        Parameters:
            mu (double): central attraction coefficient (m³/s²)
        
        Also see:
            addForceModel,
            getAllForceModels
        
        
        """
        ...
    def setOrbitType(self, orbitType: org.orekit.orbits.OrbitType) -> None:
        """
        Set propagation orbit type.
        
        Overrides: setOrbitType in class AbstractIntegratedPropagator
        
        Parameters:
            orbitType (OrbitType): orbit type to use for propagation, null for propagating using AbsolutePVCoordinates rather
                than Orbit
        
        
        """
        ...
    def setPositionAngleType(self, positionAngleType: org.orekit.orbits.PositionAngleType) -> None:
        """
        Set position angle type.
        
        The position parameter type is meaningful only if getOrbitType support it. As an example, it is not meaningful for propagation in CARTESIAN parameters.
        
        Overrides: setPositionAngleType in class AbstractIntegratedPropagator
        
        Parameters:
            positionAngleType (PositionAngleType): angle type to use for propagation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(dP: float, dV: float, orbit: org.orekit.orbits.Orbit, type: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(dP: float, orbit: org.orekit.orbits.Orbit, type: org.orekit.orbits.OrbitType) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(dP: float, absPva: org.orekit.utils.AbsolutePVCoordinates) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

class TimeDerivativesEquations:
    """
    Interface summing up the contribution of several forces into orbit and mass derivatives.
    
    The aim of this interface is to gather the contributions of various perturbing forces expressed as accelerations into one set of time-derivatives of Orbit plus one mass derivatives. It implements Gauss equations for different kind of parameters.
    
    An implementation of this interface is automatically provided by AbstractIntegratedPropagator, which are either semi-analytical or numerical propagators.
    
    Also see:
        ForceModel, NumericalPropagator
    """
    def addKeplerContribution(self, mu: float) -> None:
        """
        Add the contribution of the Kepler evolution.
        
        Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve numerical accuracy.
        
        Parameters:
            mu (double): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, q: float) -> None:
        """
        Add the contribution of the flow rate (dm/dt).
        
        Parameters:
            q (double): the flow rate, must be negative (dm/dt)
        
        Raises:
            IllegalArgumentException: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, gamma: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Add the contribution of a non-Keplerian acceleration.
        
        Parameters:
            gamma (Vector3D): acceleration vector in the same inertial frame the spacecraft state is defined in (m/s²)
        
        Since:
            9.0
        
        
        """
        ...

_PythonFieldTimeDerivativesEquations__T = typing.TypeVar('_PythonFieldTimeDerivativesEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldTimeDerivativesEquations(FieldTimeDerivativesEquations[_PythonFieldTimeDerivativesEquations__T], typing.Generic[_PythonFieldTimeDerivativesEquations__T]):
    def __init__(self): ...
    def addKeplerContribution(self, mu: _PythonFieldTimeDerivativesEquations__T) -> None:
        """
        Add the contribution of the Kepler evolution.
        
        Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve numerical accuracy.
        
        Specified by: addKeplerContribution in interface FieldTimeDerivativesEquations
        
        Parameters:
            mu (PythonFieldTimeDerivativesEquations): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, q: _PythonFieldTimeDerivativesEquations__T) -> None:
        """
        Add the contribution of the flow rate (dm/dt).
        
        Specified by: addMassDerivative in interface FieldTimeDerivativesEquations
        
        Parameters:
            q (PythonFieldTimeDerivativesEquations): the flow rate, must be negative (dm/dt)
        
        Raises:
            IllegalArgumentException: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, gamma: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_PythonFieldTimeDerivativesEquations__T]) -> None:
        """
        Add the contribution of an acceleration expressed in some inertial frame.
        
        Specified by: addNonKeplerianAcceleration in interface FieldTimeDerivativesEquations
        
        Parameters:
            gamma (FieldVector3D<PythonFieldTimeDerivativesEquations> gamma): acceleration vector in the same inertial frame the spacecraft state is defined in (m/s²)
        
        Since:
            9.0
        
        
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

class PythonTimeDerivativesEquations(TimeDerivativesEquations):
    def __init__(self): ...
    def addKeplerContribution(self, mu: float) -> None:
        """
        Add the contribution of the Kepler evolution.
        
        Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve numerical accuracy.
        
        Specified by: addKeplerContribution in interface TimeDerivativesEquations
        
        Parameters:
            mu (double): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, q: float) -> None:
        """
        Add the contribution of the flow rate (dm/dt).
        
        Specified by: addMassDerivative in interface TimeDerivativesEquations
        
        Parameters:
            q (double): the flow rate, must be negative (dm/dt)
        
        Raises:
            IllegalArgumentException: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, gamma: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Add the contribution of a non-Keplerian acceleration.
        
        Specified by: addNonKeplerianAcceleration in interface TimeDerivativesEquations
        
        Parameters:
            gamma (Vector3D): acceleration vector in the same inertial frame the spacecraft state is defined in (m/s²)
        
        Since:
            9.0
        
        
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

class PythonPartialsObserver(org.orekit.propagation.numerical.AbstractStateTransitionMatrixGenerator.PartialsObserver):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def partialsComputed(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.numerical")``.

    EpochDerivativesEquations: typing.Type[EpochDerivativesEquations]
    FieldNumericalPropagator: typing.Type[FieldNumericalPropagator]
    FieldTimeDerivativesEquations: typing.Type[FieldTimeDerivativesEquations]
    GLONASSNumericalPropagator: typing.Type[GLONASSNumericalPropagator]
    GLONASSNumericalPropagatorBuilder: typing.Type[GLONASSNumericalPropagatorBuilder]
    NumericalPropagator: typing.Type[NumericalPropagator]
    PythonFieldTimeDerivativesEquations: typing.Type[PythonFieldTimeDerivativesEquations]
    PythonPartialsObserver: typing.Type[PythonPartialsObserver]
    PythonTimeDerivativesEquations: typing.Type[PythonTimeDerivativesEquations]
    TimeDerivativesEquations: typing.Type[TimeDerivativesEquations]
    cr3bp: org.orekit.propagation.numerical.cr3bp.__module_protocol__
