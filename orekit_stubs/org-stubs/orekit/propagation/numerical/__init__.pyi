import java.util
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
    public class EpochDerivativesEquations extends :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
    
        Computes derivatives of the acceleration, including ThirdBodyAttraction.
        :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider` computing the partial derivatives of the
        state (orbit) with respect to initial state and force models parameters.
    
        This set of equations are automatically added to a :class:`~org.orekit.propagation.numerical.NumericalPropagator` in
        order to compute partial derivatives of the orbit along with the orbit itself. This is useful for example in orbit
        determination applications.
    
        The partial derivatives with respect to initial state can be either dimension 6 (orbit only) or 7 (orbit and mass).
    
        The partial derivatives with respect to force models parameters has a dimension equal to the number of selected
        parameters. Parameters selection is implemented at :class:`~org.orekit.forces.ForceModel` level. Users must retrieve a
        :class:`~org.orekit.utils.ParameterDriver` using :meth:`~org.orekit.utils.ParameterDriversProvider.getParameterDriver`
        and then select it by calling :meth:`~org.orekit.utils.ParameterDriver.setSelected`.
    
        If several force models provide different :class:`~org.orekit.utils.ParameterDriver` for the same parameter name,
        selecting any of these drivers has the side effect of selecting all the drivers for this shared parameter. In this case,
        the partial derivatives will be the sum of the partial derivatives contributed by the corresponding force models. This
        case typically arises for central attraction coefficient, which has an influence on
        :class:`~org.orekit.forces.gravity.NewtonianAttraction`,
        :class:`~org.orekit.forces.gravity.HolmesFeatherstoneAttractionModel`, and
        :class:`~org.orekit.forces.gravity.Relativity`.
    
        Since:
            10.2
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int STATE_DIMENSION
    
        State dimension, fixed to 6.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, string: str, numericalPropagator: 'NumericalPropagator'): ...
    def combinedDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.integration.CombinedDerivatives:
        """
            Compute the derivatives related to the additional state (and optionally main state increments).
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.combinedDerivatives` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                    :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.yields` method)
        
            Returns:
                computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the generated derivative.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getDimension` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                dimension of the generated
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional derivatives (which will become state once integrated).
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getName` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                name of the additional state (names containing "orekit" with any case are reserved for the library internal use)
        
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Set the initial value of the Jacobian with respect to state and parameter.
        
            This method is equivalent to call
            :meth:`~org.orekit.propagation.numerical.EpochDerivativesEquations.setInitialJacobians` with dYdY0 set to the identity
            matrix and dYdP set to a zero matrix.
        
            The force models parameters for which partial derivatives are desired, *must* have been
            :meth:`~org.orekit.utils.ParameterDriver.setSelected` before this method is called, so proper matrices dimensions are
            used.
        
            Parameters:
                s0 (:class:`~org.orekit.propagation.SpacecraftState`): initial state
        
            Returns:
                state with initial Jacobians added
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]]) -> org.orekit.propagation.SpacecraftState:
        """
            Set the initial value of the Jacobian with respect to state and parameter.
        
            The returned state must be added to the propagator (it is not done automatically, as the user may need to add more
            states to it).
        
            The force models parameters for which partial derivatives are desired, *must* have been
            :meth:`~org.orekit.utils.ParameterDriver.setSelected` before this method is called, and the :code:`dY1dP` matrix
            dimension *must* be consistent with the selection.
        
            Parameters:
                s1 (:class:`~org.orekit.propagation.SpacecraftState`): current state
                dY1dY0 (double[][]): Jacobian of current state at time t₁ with respect to state at some previous time t₀ (must be 6x6)
                dY1dP (double[][]): Jacobian of current state at time t₁ with respect to parameters (may be null if no parameters are selected)
        
            Returns:
                state with initial Jacobians added
        
            Set the Jacobian with respect to state into a one-dimensional additional state array.
        
            This method converts the Jacobians to Cartesian parameters and put the converted data in the one-dimensional :code:`p`
            array.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dY1dY0 (double[][]): Jacobian of current state at time t₁ with respect to state at some previous time t₀
                dY1dP (double[][]): Jacobian of current state at time t₁ with respect to parameters (may be null if there are no parameters)
                p (double[]): placeholder where to put the one-dimensional additional state
        
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[float]) -> None: ...

_FieldNumericalPropagator__T = typing.TypeVar('_FieldNumericalPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldNumericalPropagator(org.orekit.propagation.integration.FieldAbstractIntegratedPropagator[_FieldNumericalPropagator__T], typing.Generic[_FieldNumericalPropagator__T]):
    """
    public class FieldNumericalPropagator<T extends :class:`~org.orekit.propagation.numerical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`<T>
    
        This class propagates :class:`~org.orekit.orbits.FieldOrbit` using numerical integration.
    
        Numerical propagation is much more accurate than analytical propagation like for example
        :class:`~org.orekit.propagation.analytical.KeplerianPropagator` or
        :class:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator`, but requires a few more steps to set up to be
        used properly. Whereas analytical propagators are configured only thanks to their various constructors and can be used
        immediately after construction, numerical propagators configuration involve setting several parameters between
        construction time and propagation time.
    
        The configuration parameters that can be set are:
    
          - the initial spacecraft state (:meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.setInitialState`)
          - the central attraction coefficient (:meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.setMu`)
          - the various force models (:meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.addForceModel`,
            :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.removeForceModels`)
          - the :class:`~org.orekit.orbits.OrbitType` of orbital parameters to be used for propagation
            (:meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.setOrbitType`),
          - the :class:`~org.orekit.orbits.PositionAngleType` of position angle to be used in orbital parameters to be used for
            propagation where it is relevant
            (:meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.setPositionAngleType`),
          - whether :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider` should be propagated along with
            orbital state
            (:meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addAdditionalDerivativesProvider`),
          - the discrete events that should be triggered during propagation
            (:meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addEventDetector`,
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.clearEventsDetectors`)
          - the binding logic with the rest of the application
            (:meth:`~org.orekit.propagation.FieldAbstractPropagator.getMultiplexer`)
    
    
        From these configuration parameters, only the initial state is mandatory. The default propagation settings are in
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` parameters with :meth:`~org.orekit.orbits.PositionAngleType.TRUE`
        longitude argument. If the central attraction coefficient is not explicitly specified, the one used to define the
        initial orbit will be used. However, specifying only the initial state and perhaps the central attraction coefficient
        would mean the propagator would use only Keplerian forces. In this case, the simpler
        :class:`~org.orekit.propagation.analytical.KeplerianPropagator` class would perhaps be more effective.
    
        The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical
        configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the
        absolute and/or relative errors thresholds.
    
        The state that is seen by the integrator is a simple seven elements double array. The six first elements are either:
    
          - the :class:`~org.orekit.orbits.FieldEquinoctialOrbit` (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ
            :sub:`M` or λ :sub:`E` or λ :sub:`v` ) in meters and radians,
          - the :class:`~org.orekit.orbits.FieldKeplerianOrbit` (a, e, i, ω, Ω, M or E or v) in meters and radians,
          - the :class:`~org.orekit.orbits.FieldCircularOrbit` (a, e :sub:`x` , e :sub:`y` , i, Ω, α :sub:`M` or α :sub:`E` or α
            :sub:`v` ) in meters and radians,
          - the :class:`~org.orekit.orbits.FieldCartesianOrbit` (x, y, z, v :sub:`x` , v :sub:`y` , v :sub:`z` ) in meters and
            meters per seconds.
    
        The last element is the mass in kilograms.
    
        The following code snippet shows a typical setting for Low Earth Orbit propagation in equinoctial parameters and true
        longitude argument:
    
        .. code-block: java
        
         final T          zero      = field.getZero();
         final T          dP        = zero.add(0.001);
         final T          minStep   = zero.add(0.001);
         final T          maxStep   = zero.add(500);
         final T          initStep  = zero.add(60);
         final double[][] tolerance = FieldNumericalPropagator.tolerances(dP, orbit, OrbitType.EQUINOCTIAL);
         AdaptiveStepsizeFieldIntegrator<T> integrator = new DormandPrince853FieldIntegrator<>(field, minStep, maxStep, tolerance[0], tolerance[1]);
         integrator.setInitialStepSize(initStep);
         propagator = new FieldNumericalPropagator<>(field, integrator);
         
    
        By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a
        new propagation to be started from there without recomputing the part already performed. This behaviour can be chenged
        by calling :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setResetAtEnd`.
    
        Beware the same instance cannot be used simultaneously by different threads, the class is *not* thread-safe.
    
        Also see:
            :class:`~org.orekit.propagation.FieldSpacecraftState`, :class:`~org.orekit.forces.ForceModel`,
            :class:`~org.orekit.propagation.sampling.FieldOrekitStepHandler`,
            :class:`~org.orekit.propagation.sampling.FieldOrekitFixedStepHandler`,
            :class:`~org.orekit.propagation.integration.FieldIntegratedEphemeris`,
            :class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNumericalPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldNumericalPropagator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldNumericalPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldNumericalPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, forceModel: org.orekit.forces.ForceModel) -> None:
        """
            Add a force model to the global perturbation model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                model (:class:`~org.orekit.forces.ForceModel`): perturbing :class:`~org.orekit.forces.ForceModel` to add
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.removeForceModels`,
                :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.setMu`
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.getOrbitType` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Returns:
                orbit type used for propagation
        
        
        """
        ...
    def getPVCoordinates(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldNumericalPropagator__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldNumericalPropagator__T]: ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.getPositionAngleType` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Returns:
                angle type to use for propagation
        
        
        """
        ...
    def removeForceModels(self) -> None:
        """
            Remove all perturbing force models from the global perturbation model.
        
            Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will
            follow a Keplerian evolution only.
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.addForceModel`
        
        
        """
        ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldNumericalPropagator__T]) -> None: ...
    def setIgnoreCentralAttraction(self, boolean: bool) -> None:
        """
            Set the flag to ignore or not the creation of a :class:`~org.orekit.forces.gravity.NewtonianAttraction`.
        
            Parameters:
                ignoreCentralAttraction (boolean): if true, :class:`~org.orekit.forces.gravity.NewtonianAttraction` is *not* added automatically if missing
        
        
        """
        ...
    def setInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldNumericalPropagator__T]) -> None: ...
    def setMu(self, t: _FieldNumericalPropagator__T) -> None:
        """
            Set the central attraction coefficient μ.
        
            Setting the central attraction coefficient is equivalent to
            :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.addForceModel` a
            :class:`~org.orekit.forces.gravity.NewtonianAttraction` force model.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setMu` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Parameters:
                mu (:class:`~org.orekit.propagation.numerical.FieldNumericalPropagator`): central attraction coefficient (m³/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.addForceModel`,
                :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.getAllForceModels`
        
        
        """
        ...
    def setOrbitType(self, orbitType: org.orekit.orbits.OrbitType) -> None:
        """
            Set propagation orbit type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setOrbitType` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Parameters:
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use for propagation
        
        
        """
        ...
    def setPositionAngleType(self, positionAngleType: org.orekit.orbits.PositionAngleType) -> None:
        """
            Set position angle type.
        
            The position parameter type is meaningful only if
            :meth:`~org.orekit.propagation.numerical.FieldNumericalPropagator.getOrbitType` support it. As an example, it is not
            meaningful for propagation in :meth:`~org.orekit.orbits.OrbitType.CARTESIAN` parameters.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setPositionAngleType` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Parameters:
                positionAngleType (:class:`~org.orekit.orbits.PositionAngleType`): angle type to use for propagation
        
        
        """
        ...
    _tolerances_0__T = typing.TypeVar('_tolerances_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _tolerances_1__T = typing.TypeVar('_tolerances_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tolerances(t: _tolerances_0__T, t2: _tolerances_0__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_tolerances_0__T], orbitType: org.orekit.orbits.OrbitType) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for integrators when propagating in orbits.
        
            The errors are estimated from partial derivatives properties of orbits, starting from scalar position and velocity
            errors specified by the user.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (T): user specified position error
                dV (T): user specified velocity error
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): reference orbit
                type (:class:`~org.orekit.orbits.OrbitType`): propagation type for the meaning of the tolerance vectors elements (it may be different from :code:`orbit.getType()`)
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
            Since:
                10.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(t: _tolerances_1__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_tolerances_1__T], orbitType: org.orekit.orbits.OrbitType) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for integrators.
        
            The errors are estimated from partial derivatives properties of orbits, starting from a scalar position error specified
            by the user. Considering the energy conservation equation V = sqrt(mu (2/r - 1/a)), we get at constant energy (i.e. on a
            Keplerian trajectory):
        
            .. code-block: java
            
             V r² |dV| = mu |dr|
             
            So we deduce a scalar velocity error consistent with the position error. From here, we apply orbits Jacobians matrices
            to get consistent errors on orbital parameters.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (T): user specified position error
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): reference orbit
                type (:class:`~org.orekit.orbits.OrbitType`): propagation type for the meaning of the tolerance vectors elements (it may be different from :code:`orbit.getType()`)
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
        """
        ...

_FieldTimeDerivativesEquations__T = typing.TypeVar('_FieldTimeDerivativesEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTimeDerivativesEquations(typing.Generic[_FieldTimeDerivativesEquations__T]):
    """
    public interface FieldTimeDerivativesEquations<T extends :class:`~org.orekit.propagation.numerical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        Interface summing up the contribution of several forces into orbit and mass derivatives.
    
        The aim of this interface is to gather the contributions of various perturbing forces expressed as accelerations into
        one set of time-derivatives of :class:`~org.orekit.orbits.Orbit` plus one mass derivatives. It implements Gauss
        equations for different kind of parameters.
    
        An implementation of this interface is automatically provided by
        :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`, which are either semi-analytical or numerical
        propagators.
    
        Also see:
            :class:`~org.orekit.forces.ForceModel`, :class:`~org.orekit.propagation.numerical.NumericalPropagator`
    """
    def addKeplerContribution(self, t: _FieldTimeDerivativesEquations__T) -> None:
        """
            Add the contribution of the Kepler evolution.
        
            Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve
            numerical accuracy.
        
            Parameters:
                mu (:class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, t: _FieldTimeDerivativesEquations__T) -> None:
        """
            Add the contribution of the flow rate (dm/dt).
        
            Parameters:
                q (:class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`): the flow rate, must be negative (dm/dt)
        
            Raises:
                :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTimeDerivativesEquations__T]) -> None: ...

class GLONASSNumericalPropagator(org.orekit.propagation.integration.AbstractIntegratedPropagator):
    """
    public class GLONASSNumericalPropagator extends :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
    
        This class propagates GLONASS orbits using numerical integration.
    
        As recommended by the GLONASS Interface Control Document (ICD), a
        :class:`~org.orekit.propagation.numerical.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator?is`
        shall be used to integrate the equations.
    
        Classical used of this orbit propagator is to compute GLONASS satellite coordinates from the navigation message.
    
        If the projections of luni-solar accelerations to axes of Greenwich geocentric coordinates
        :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getXDotDot`,
        :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getYDotDot` and
        :meth:`~org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements.getZDotDot` are available in the navigation
        message; a transformation is performed to convert these accelerations into the correct coordinate system. In the case
        where they are not available into the navigation message, these accelerations are computed.
    
        **Caution:** The Glonass numerical propagator can only be used with
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage`. Using this propagator with a
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac` is prone to error.
    
        Also see:
            ` GLONASS Interface Control Document
            <http://russianspacesystems.ru/wp-content/uploads/2016/08/ICD-GLONASS-CDMA-General.-Edition-1.0-2016.pdf>`
    """
    def __init__(self, classicalRungeKuttaIntegrator: org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator, gLONASSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, frame: org.orekit.frames.Frame, attitudeProvider: org.orekit.attitudes.AttitudeProvider, double: float, dataContext: org.orekit.data.DataContext, boolean: bool): ...
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
    def propagate(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.propagation.SpacecraftState:
        """
            Propagate towards a target date.
        
            Simple propagators use only the target date as the specification for computing the propagated state. More feature rich
            propagators can consider other information and provide different operating modes or G-stop facilities to stop at
            pinpointed events occurrences. In these cases, the target date is only a hint, not a mandatory objective.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.propagate` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.propagate` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): target date towards which orbit state should be propagated
        
            Returns:
                propagated state
        
        
        """
        ...

class GLONASSNumericalPropagatorBuilder:
    """
    public class GLONASSNumericalPropagatorBuilder extends :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This nested class aims at building a GLONASSNumericalPropagator.
    
        It implements the classical builder pattern.
    
        **Caution:** The Glonass numerical propagator can only be used with
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSNavigationMessage`. Using this propagator with a
        :class:`~org.orekit.propagation.analytical.gnss.data.GLONASSAlmanac` is prone to error.
    
        Since:
            11.0
    """
    @typing.overload
    def __init__(self, classicalRungeKuttaIntegrator: org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator, gLONASSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, boolean: bool): ...
    @typing.overload
    def __init__(self, classicalRungeKuttaIntegrator: org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator, gLONASSOrbitalElements: org.orekit.propagation.analytical.gnss.data.GLONASSOrbitalElements, boolean: bool, dataContext: org.orekit.data.DataContext): ...
    def attitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> 'GLONASSNumericalPropagatorBuilder':
        """
            Sets the attitude provider.
        
            Parameters:
                userProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the attitude provider
        
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
    def eci(self, frame: org.orekit.frames.Frame) -> 'GLONASSNumericalPropagatorBuilder':
        """
            Sets the Earth Centered Inertial frame used for propagation.
        
            Parameters:
                inertial (:class:`~org.orekit.frames.Frame`): the ECI frame
        
            Returns:
                the updated builder
        
        
        """
        ...
    def mass(self, double: float) -> 'GLONASSNumericalPropagatorBuilder':
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
    public class NumericalPropagator extends :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
    
        This class propagates :class:`~org.orekit.orbits.Orbit` using numerical integration.
    
        Numerical propagation is much more accurate than analytical propagation like for example
        :class:`~org.orekit.propagation.analytical.KeplerianPropagator` or
        :class:`~org.orekit.propagation.analytical.EcksteinHechlerPropagator`, but requires a few more steps to set up to be
        used properly. Whereas analytical propagators are configured only thanks to their various constructors and can be used
        immediately after construction, numerical propagators configuration involve setting several parameters between
        construction time and propagation time.
    
        The configuration parameters that can be set are:
    
          - the initial spacecraft state (:meth:`~org.orekit.propagation.numerical.NumericalPropagator.setInitialState`)
          - the central attraction coefficient (:meth:`~org.orekit.propagation.numerical.NumericalPropagator.setMu`)
          - the various force models (:meth:`~org.orekit.propagation.numerical.NumericalPropagator.addForceModel`,
            :meth:`~org.orekit.propagation.numerical.NumericalPropagator.removeForceModels`)
          - the :class:`~org.orekit.orbits.OrbitType` of orbital parameters to be used for propagation
            (:meth:`~org.orekit.propagation.numerical.NumericalPropagator.setOrbitType`),
          - the :class:`~org.orekit.orbits.PositionAngleType` of position angle to be used in orbital parameters to be used for
            propagation where it is relevant (:meth:`~org.orekit.propagation.numerical.NumericalPropagator.setPositionAngleType`),
          - whether :class:`~org.orekit.propagation.MatricesHarvester` should be propagated along with orbital state
            (:meth:`~org.orekit.propagation.AbstractPropagator.setupMatricesComputation`),
          - whether :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider` should be propagated along with
            orbital state
            (:meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.addAdditionalDerivativesProvider`),
          - the discrete events that should be triggered during propagation
            (:meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.addEventDetector`,
            :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.clearEventsDetectors`)
          - the binding logic with the rest of the application (:meth:`~org.orekit.propagation.AbstractPropagator.getMultiplexer`)
    
    
        From these configuration parameters, only the initial state is mandatory. The default propagation settings are in
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` parameters with :meth:`~org.orekit.orbits.PositionAngleType.TRUE`
        longitude argument. If the central attraction coefficient is not explicitly specified, the one used to define the
        initial orbit will be used. However, specifying only the initial state and perhaps the central attraction coefficient
        would mean the propagator would use only Keplerian forces. In this case, the simpler
        :class:`~org.orekit.propagation.analytical.KeplerianPropagator` class would perhaps be more effective.
    
        The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical
        configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the
        absolute and/or relative errors thresholds.
    
        The state that is seen by the integrator is a simple seven elements double array. The six first elements are either:
    
          - the :class:`~org.orekit.orbits.EquinoctialOrbit` (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ :sub:`M` or
            λ :sub:`E` or λ :sub:`v` ) in meters and radians,
          - the :class:`~org.orekit.orbits.KeplerianOrbit` (a, e, i, ω, Ω, M or E or v) in meters and radians,
          - the :class:`~org.orekit.orbits.CircularOrbit` (a, e :sub:`x` , e :sub:`y` , i, Ω, α :sub:`M` or α :sub:`E` or α
            :sub:`v` ) in meters and radians,
          - the :class:`~org.orekit.orbits.CartesianOrbit` (x, y, z, v :sub:`x` , v :sub:`y` , v :sub:`z` ) in meters and meters per
            seconds.
    
    
        The last element is the mass in kilograms and changes only during thrusters firings
    
        The following code snippet shows a typical setting for Low Earth Orbit propagation in equinoctial parameters and true
        longitude argument:
    
        .. code-block: java
        
         final double dP       = 0.001;
         final double minStep  = 0.001;
         final double maxStep  = 500;
         final double initStep = 60;
         final double[][] tolerance = NumericalPropagator.tolerances(dP, orbit, OrbitType.EQUINOCTIAL);
         AdaptiveStepsizeIntegrator integrator = new DormandPrince853Integrator(minStep, maxStep, tolerance[0], tolerance[1]);
         integrator.setInitialStepSize(initStep);
         propagator = new NumericalPropagator(integrator);
         
    
        By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a
        new propagation to be started from there without recomputing the part already performed. This behaviour can be chenged
        by calling :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setResetAtEnd`.
    
        Beware the same instance cannot be used simultaneously by different threads, the class is *not* thread-safe.
    
        Also see:
            :class:`~org.orekit.propagation.SpacecraftState`, :class:`~org.orekit.forces.ForceModel`,
            :class:`~org.orekit.propagation.sampling.OrekitStepHandler`,
            :class:`~org.orekit.propagation.sampling.OrekitFixedStepHandler`,
            :class:`~org.orekit.propagation.integration.IntegratedEphemeris`,
            :class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`
    """
    @typing.overload
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator): ...
    @typing.overload
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, forceModel: org.orekit.forces.ForceModel) -> None:
        """
            Add a force model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                model (:class:`~org.orekit.forces.ForceModel`): :class:`~org.orekit.forces.ForceModel` to add (it can be either a perturbing force model or an instance of
                    :class:`~org.orekit.forces.gravity.NewtonianAttraction`)
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.NumericalPropagator.removeForceModels`,
                :meth:`~org.orekit.propagation.numerical.NumericalPropagator.setMu`
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.getOrbitType` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Returns:
                orbit type used for propagation, null for propagating using :class:`~org.orekit.utils.AbsolutePVCoordinates` rather than
                :class:`~org.orekit.orbits.Orbit`
        
        
        """
        ...
    def getPVCoordinates(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
            Get the :class:`~org.orekit.utils.PVCoordinates` of the body in the selected frame.
        
            Specified by:
                :meth:`~org.orekit.utils.PVCoordinatesProvider.getPVCoordinates` in
                interface :class:`~org.orekit.utils.PVCoordinatesProvider`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.getPVCoordinates` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                frame (:class:`~org.orekit.frames.Frame`): the frame where to define the position
        
            Returns:
                time-stamped position/velocity of the body (m and m/s)
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.getPositionAngleType` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Returns:
                angle type to use for propagation
        
        
        """
        ...
    def removeForceModels(self) -> None:
        """
            Remove all force models (except central attraction).
        
            Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will
            follow a Keplerian evolution only.
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.NumericalPropagator.addForceModel`
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the propagator initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
        
        
        """
        ...
    def setIgnoreCentralAttraction(self, boolean: bool) -> None:
        """
            Set the flag to ignore or not the creation of a :class:`~org.orekit.forces.gravity.NewtonianAttraction`.
        
            Parameters:
                ignoreCentralAttraction (boolean): if true, :class:`~org.orekit.forces.gravity.NewtonianAttraction` is *not* added automatically if missing
        
        
        """
        ...
    def setInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Set the initial state.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
        
        
        """
        ...
    def setMu(self, double: float) -> None:
        """
            Set the central attraction coefficient μ.
        
            Setting the central attraction coefficient is equivalent to
            :meth:`~org.orekit.propagation.numerical.NumericalPropagator.addForceModel` a
            :class:`~org.orekit.forces.gravity.NewtonianAttraction` force model.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setMu` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                mu (double): central attraction coefficient (m³/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.NumericalPropagator.addForceModel`,
                :meth:`~org.orekit.propagation.numerical.NumericalPropagator.getAllForceModels`
        
        
        """
        ...
    def setOrbitType(self, orbitType: org.orekit.orbits.OrbitType) -> None:
        """
            Set propagation orbit type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setOrbitType` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                orbitType (:class:`~org.orekit.orbits.OrbitType`): orbit type to use for propagation, null for propagating using :class:`~org.orekit.utils.AbsolutePVCoordinates` rather
                    than :class:`~org.orekit.orbits.Orbit`
        
        
        """
        ...
    def setPositionAngleType(self, positionAngleType: org.orekit.orbits.PositionAngleType) -> None:
        """
            Set position angle type.
        
            The position parameter type is meaningful only if
            :meth:`~org.orekit.propagation.numerical.NumericalPropagator.getOrbitType` support it. As an example, it is not
            meaningful for propagation in :meth:`~org.orekit.orbits.OrbitType.CARTESIAN` parameters.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setPositionAngleType` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                positionAngleType (:class:`~org.orekit.orbits.PositionAngleType`): angle type to use for propagation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, double2: float, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for integrators when propagating in orbits.
        
            The errors are estimated from partial derivatives properties of orbits, starting from scalar position and velocity
            errors specified by the user.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (double): user specified position error
                dV (double): user specified velocity error
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                type (:class:`~org.orekit.orbits.OrbitType`): propagation type for the meaning of the tolerance vectors elements (it may be different from :code:`orbit.getType()`)
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
            Since:
                10.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, orbit: org.orekit.orbits.Orbit, orbitType: org.orekit.orbits.OrbitType) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for integrators when propagating in orbits.
        
            The errors are estimated from partial derivatives properties of orbits, starting from a scalar position error specified
            by the user. Considering the energy conservation equation V = sqrt(mu (2/r - 1/a)), we get at constant energy (i.e. on a
            Keplerian trajectory):
        
            .. code-block: java
            
             V r² |dV| = mu |dr|
             
        
            So we deduce a scalar velocity error consistent with the position error. From here, we apply orbits Jacobians matrices
            to get consistent errors on orbital parameters.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (double): user specified position error
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
                type (:class:`~org.orekit.orbits.OrbitType`): propagation type for the meaning of the tolerance vectors elements (it may be different from :code:`orbit.getType()`)
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for integrators when propagating in absolute position-velocity-acceleration.
        
            Parameters:
                dP (double): user specified position error
                absPva (:class:`~org.orekit.utils.AbsolutePVCoordinates`): reference absolute position-velocity-acceleration
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
            Also see:
                :meth:`~org.orekit.propagation.numerical.NumericalPropagator.tolerances`
        
        """
        ...

class TimeDerivativesEquations:
    """
    public interface TimeDerivativesEquations
    
        Interface summing up the contribution of several forces into orbit and mass derivatives.
    
        The aim of this interface is to gather the contributions of various perturbing forces expressed as accelerations into
        one set of time-derivatives of :class:`~org.orekit.orbits.Orbit` plus one mass derivatives. It implements Gauss
        equations for different kind of parameters.
    
        An implementation of this interface is automatically provided by
        :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`, which are either semi-analytical or numerical
        propagators.
    
        Also see:
            :class:`~org.orekit.forces.ForceModel`, :class:`~org.orekit.propagation.numerical.NumericalPropagator`
    """
    def addKeplerContribution(self, double: float) -> None:
        """
            Add the contribution of the Kepler evolution.
        
            Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve
            numerical accuracy.
        
            Parameters:
                mu (double): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, double: float) -> None:
        """
            Add the contribution of the flow rate (dm/dt).
        
            Parameters:
                q (double): the flow rate, must be negative (dm/dt)
        
            Raises:
                :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Add the contribution of a non-Keplerian acceleration.
        
            Parameters:
                gamma (:class:`~org.orekit.propagation.numerical.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): acceleration vector in the same inertial frame the spacecraft state is defined in (m/s²)
        
            Since:
                9.0
        
        
        """
        ...

_PythonFieldTimeDerivativesEquations__T = typing.TypeVar('_PythonFieldTimeDerivativesEquations__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldTimeDerivativesEquations(FieldTimeDerivativesEquations[_PythonFieldTimeDerivativesEquations__T], typing.Generic[_PythonFieldTimeDerivativesEquations__T]):
    """
    public class PythonFieldTimeDerivativesEquations<T extends :class:`~org.orekit.propagation.numerical.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`<T>
    """
    def __init__(self): ...
    def addKeplerContribution(self, t: _PythonFieldTimeDerivativesEquations__T) -> None:
        """
            Add the contribution of the Kepler evolution.
        
            Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve
            numerical accuracy.
        
            Specified by:
                :meth:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations.addKeplerContribution` in
                interface :class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`
        
            Parameters:
                mu (:class:`~org.orekit.propagation.numerical.PythonFieldTimeDerivativesEquations`): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, t: _PythonFieldTimeDerivativesEquations__T) -> None:
        """
            Add the contribution of the flow rate (dm/dt).
        
            Specified by:
                :meth:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations.addMassDerivative` in
                interface :class:`~org.orekit.propagation.numerical.FieldTimeDerivativesEquations`
        
            Parameters:
                q (:class:`~org.orekit.propagation.numerical.PythonFieldTimeDerivativesEquations`): the flow rate, must be negative (dm/dt)
        
            Raises:
                :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_PythonFieldTimeDerivativesEquations__T]) -> None: ...
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

class PythonTimeDerivativesEquations(TimeDerivativesEquations):
    """
    public class PythonTimeDerivativesEquations extends :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`
    """
    def __init__(self): ...
    def addKeplerContribution(self, double: float) -> None:
        """
            Add the contribution of the Kepler evolution.
        
            Since the Kepler evolution is the most important, it should be added after all the other ones, in order to improve
            numerical accuracy.
        
            Specified by:
                :meth:`~org.orekit.propagation.numerical.TimeDerivativesEquations.addKeplerContribution` in
                interface :class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`
        
            Parameters:
                mu (double): central body gravitational constant
        
        
        """
        ...
    def addMassDerivative(self, double: float) -> None:
        """
            Add the contribution of the flow rate (dm/dt).
        
            Specified by:
                :meth:`~org.orekit.propagation.numerical.TimeDerivativesEquations.addMassDerivative` in
                interface :class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`
        
            Parameters:
                q (double): the flow rate, must be negative (dm/dt)
        
            Raises:
                :class:`~org.orekit.propagation.numerical.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if flow-rate is positive
        
        
        """
        ...
    def addNonKeplerianAcceleration(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
            Add the contribution of a non-Keplerian acceleration.
        
            Specified by:
                :meth:`~org.orekit.propagation.numerical.TimeDerivativesEquations.addNonKeplerianAcceleration` in
                interface :class:`~org.orekit.propagation.numerical.TimeDerivativesEquations`
        
            Parameters:
                gamma (:class:`~org.orekit.propagation.numerical.https:.www.hipparchus.org.apidocs.org.hipparchus.geometry.euclidean.threed.Vector3D?is`): acceleration vector in the same inertial frame the spacecraft state is defined in (m/s²)
        
            Since:
                9.0
        
        
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

class PythonPartialsObserver(org.orekit.propagation.numerical.StateTransitionMatrixGenerator.PartialsObserver):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def partialsComputed(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float], doubleArray2: typing.List[float]) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
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
