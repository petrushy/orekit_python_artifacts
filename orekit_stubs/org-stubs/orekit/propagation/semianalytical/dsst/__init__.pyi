import java.util
import org.hipparchus
import org.hipparchus.ode
import org.orekit.attitudes
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.propagation.semianalytical.dsst.utilities
import typing



class DSSTJacobiansMapper(org.orekit.propagation.integration.AbstractJacobiansMapper):
    """
    public class DSSTJacobiansMapper extends :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
    
        Mapper between two-dimensional Jacobian matrices and one-dimensional
        :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`.
    
        This class does not hold the states by itself. Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPartialDerivativesEquations`,
            :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`,
            :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`, :class:`~org.orekit.propagation.AbstractPropagator`
    """
    STATE_DIMENSION: typing.ClassVar[int] = ...
    """
    public static final int STATE_DIMENSION
    
        State dimension, fixed to 6.
    
        Since:
            9.0
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getParametersJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Get the Jacobian with respect to parameters from a one-dimensional additional state array.
        
            This method extract the data from the :code:`state` and put it in the :code:`dYdP` array.
        
            If no parameters have been set in the constructor, the method returns immediately and does not reference :code:`dYdP`
            which can safely be null in this case.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AbstractJacobiansMapper.getParametersJacobian` in
                class :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dYdP (double[][]): placeholder where to put the Jacobian with respect to parameters
        
            Also see:
                :meth:`~org.orekit.propagation.integration.AbstractJacobiansMapper.getStateJacobian`
        
        
        """
        ...
    def getStateJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]]) -> None:
        """
            Get the Jacobian with respect to state from a one-dimensional additional state array.
        
            This method extract the data from the :code:`state` and put it in the :code:`dYdY0` array.
        
            For :class:`~org.orekit.propagation.numerical.JacobiansMapper` and
            :class:`~org.orekit.propagation.analytical.tle.TLEJacobiansMapper`, the method provides the Jacobian with respect to
            Cartesian elements. For :class:`~org.orekit.propagation.semianalytical.dsst.DSSTJacobiansMapper` the method provides the
            Jacobian with respect to Equinoctial elements.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AbstractJacobiansMapper.getStateJacobian` in
                class :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dYdY0 (double[][]): placeholder where to put the Jacobian with respect to state
        
            Also see:
                :meth:`~org.orekit.propagation.integration.AbstractJacobiansMapper.getParametersJacobian`
        
        
        """
        ...
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[float]) -> None:
        """
            Set the Jacobian with respect to state into a one-dimensional additional state array.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AbstractJacobiansMapper.setInitialJacobians` in
                class :class:`~org.orekit.propagation.integration.AbstractJacobiansMapper`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                dY1dY0 (double[][]): Jacobian of current state at time t₁ with respect to state at some previous time t₀
                dY1dP (double[][]): Jacobian of current state at time t₁ with respect to parameters (may be null if there are no parameters)
                p (double[]): placeholder where to put the one-dimensional additional state
        
            Also see:
                :meth:`~org.orekit.propagation.integration.AbstractJacobiansMapper.getStateJacobian`
        
        
        """
        ...
    def setShortPeriodJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Compute the derivatives of the short period terms related to the additional state parameters.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): Current state information: date, kinematics, attitude, and additional state
        
        
        """
        ...

class DSSTPartialDerivativesEquations(org.orekit.propagation.integration.AdditionalEquations):
    """
    public class DSSTPartialDerivativesEquations extends :class:`~org.orekit.propagation.semianalytical.dsst.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.integration.AdditionalEquations`
    
        Set of :class:`~org.orekit.propagation.integration.AdditionalEquations` computing the partial derivatives of the state
        (orbit) with respect to initial state and force models parameters.
    
        This set of equations are automatically added to a :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`
        in order to compute partial derivatives of the orbit along with the orbit itself. This is useful for example in orbit
        determination applications.
    
        The partial derivatives with respect to initial state are dimension 6 (orbit only).
    
        The partial derivatives with respect to force models parameters has a dimension equal to the number of selected
        parameters. Parameters selection is implemented at
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel` level. Users must retrieve a
        :class:`~org.orekit.utils.ParameterDriver` by looping on all drivers using
        :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getParametersDrivers` and then select it by
        calling :meth:`~org.orekit.utils.ParameterDriver.setSelected`.
    
        Since:
            10.0
    """
    def __init__(self, string: str, dSSTPropagator: 'DSSTPropagator', propagationType: org.orekit.propagation.PropagationType): ...
    def computeDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Compute the derivatives related to the additional state parameters.
        
            When this method is called, the spacecraft state contains the main state (orbit, attitude and mass), all the states
            provided through the :class:`~org.orekit.propagation.AdditionalStateProvider` registered to the propagator, and the
            additional state integrated using this equation. It does *not* contains any other states to be integrated alongside
            during the same propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalEquations.computeDerivatives` in
                interface :class:`~org.orekit.propagation.integration.AdditionalEquations`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional state
                pDot (double[]): placeholder where the derivatives of the additional parameters should be put
        
            Returns:
                cumulative effect of the equations on the main state (may be null if equations do not change main state at all)
        
        
        """
        ...
    def getMapper(self) -> DSSTJacobiansMapper:
        """
            Get a mapper between two-dimensional Jacobians and one-dimensional additional state.
        
            Returns:
                a mapper between two-dimensional Jacobians and one-dimensional additional state, with the same name as the instance
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPartialDerivativesEquations.setInitialJacobians`,
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPartialDerivativesEquations.setInitialJacobians`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional state.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalEquations.getName` in
                interface :class:`~org.orekit.propagation.integration.AdditionalEquations`
        
            Returns:
                name of the additional state
        
        
        """
        ...
    @typing.overload
    def setInitialJacobians(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Set the initial value of the Jacobian with respect to state and parameter.
        
            This method is equivalent to call
            :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPartialDerivativesEquations.setInitialJacobians` with dYdY0 set
            to the identity matrix and dYdP set to a zero matrix.
        
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
        
        
        """
        ...

class DSSTPropagator(org.orekit.propagation.integration.AbstractIntegratedPropagator):
    """
    public class DSSTPropagator extends :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
    
        This class propagates :class:`~org.orekit.orbits.Orbit` using the DSST theory.
    
        Whereas analytical propagators are configured only thanks to their various constructors and can be used immediately
        after construction, such a semianalytical propagator configuration involves setting several parameters between
        construction time and propagation time, just as numerical propagators.
    
        The configuration parameters that can be set are:
    
          - the initial spacecraft state (:meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInitialState`)
          - the various force models (:meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.addForceModel`,
            :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.removeForceModels`)
          - the discrete events that should be triggered during propagation (
            :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.addEventDetector`,
            :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.clearEventsDetectors`)
          - the binding logic with the rest of the application (:meth:`~org.orekit.propagation.AbstractPropagator.getMultiplexer`)
    
    
        From these configuration parameters, only the initial state is mandatory. The default propagation settings are in
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` parameters with :meth:`~org.orekit.orbits.PositionAngle.TRUE` longitude
        argument. The central attraction coefficient used to define the initial orbit will be used. However, specifying only the
        initial state would mean the propagator would use only Keplerian forces. In this case, the simpler
        :class:`~org.orekit.propagation.analytical.KeplerianPropagator` class would be more effective.
    
        The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical
        configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the
        absolute and/or relative errors thresholds.
    
        The state that is seen by the integrator is a simple six elements double array. These six elements are:
    
          - the :class:`~org.orekit.orbits.EquinoctialOrbit` (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ :sub:`m` )
            in meters and radians,
    
    
        By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a
        new propagation to be started from there without recomputing the part already performed. This behaviour can be chenged
        by calling :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setResetAtEnd`.
    
        Beware the same instance cannot be used simultaneously by different threads, the class is *not* thread-safe.
    
        Also see:
            :class:`~org.orekit.propagation.SpacecraftState`,
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    """
    @typing.overload
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator): ...
    @typing.overload
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, oDEIntegrator: org.hipparchus.ode.ODEIntegrator, propagationType: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, dSSTForceModel: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None:
        """
            Add a force model to the global perturbation model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                force (:class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`): perturbing :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel` to add
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.removeForceModels`,
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setMu`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanState(spacecraftState: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.SpacecraftState: ...
    @typing.overload
    @staticmethod
    def computeMeanState(spacecraftState: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], double: float, int: int) -> org.orekit.propagation.SpacecraftState: ...
    @staticmethod
    def computeOsculatingState(spacecraftState: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.SpacecraftState: ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.getOrbitType` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Returns:
                orbit type used for propagation
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngle:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.getPositionAngleType` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Returns:
                angle type to use for propagation
        
        
        """
        ...
    def getSatelliteRevolution(self) -> int:
        """
            Get the number of satellite revolutions to use for converting osculating to mean elements.
        
            Returns:
                number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def getSelectedCoefficients(self) -> java.util.Set[str]: ...
    def initialIsOsculating(self) -> bool:
        """
            Check if the initial state is provided in osculating elements.
        
            Returns:
                true if initial state is provided in osculating elements
        
        
        """
        ...
    def removeForceModels(self) -> None:
        """
            Remove all perturbing force models from the global perturbation model (except central attraction).
        
            Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will
            follow a Keplerian evolution only.
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.addForceModel`
        
        
        """
        ...
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Reset the initial state.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.resetInitialState` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state
        
        
        """
        ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setAttitudeProvider` in interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setAttitudeProvider` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    @typing.overload
    def setInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Set the initial state with osculating orbital elements.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state (defined with osculating elements)
        
            Set the initial state.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                stateType (:class:`~org.orekit.propagation.PropagationType`): defined if the orbital state is defined with osculating or mean elements
        
        
        """
        ...
    @typing.overload
    def setInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    def setInterpolationGridToFixedNumberOfPoints(self, int: int) -> None:
        """
            Set the interpolation grid generator.
        
            The generator will create an interpolation grid with a fixed number of points for each mean element integration step.
        
            If neither :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInterpolationGridToFixedNumberOfPoints`
            nor :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInterpolationGridToMaxTimeGap` has been called,
            by default the propagator is set as to 3 interpolations points per step.
        
            Parameters:
                interpolationPoints (int): number of interpolation points at each integration step
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInterpolationGridToMaxTimeGap`
        
        
        """
        ...
    def setInterpolationGridToMaxTimeGap(self, double: float) -> None:
        """
            Set the interpolation grid generator.
        
            The generator will create an interpolation grid with a maximum time gap between interpolation points.
        
            If neither :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInterpolationGridToFixedNumberOfPoints`
            nor :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInterpolationGridToMaxTimeGap` has been called,
            by default the propagator is set as to 3 interpolations points per step.
        
            Parameters:
                maxGap (double): maximum time gap between interpolation points (seconds)
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.setInterpolationGridToFixedNumberOfPoints`
        
        
        """
        ...
    def setMu(self, double: float) -> None:
        """
            Set the central attraction coefficient μ.
        
            Setting the central attraction coefficient is equivalent to
            :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.addForceModel` a
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTNewtonianAttraction` force model.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.setMu` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                mu (double): central attraction coefficient (m³/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.addForceModel`,
                :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.getAllForceModels`
        
        
        """
        ...
    def setSatelliteRevolution(self, int: int) -> None:
        """
            Override the default value of the parameter.
        
            By default, if the initial orbit is defined as osculating, it will be averaged over 2 satellite revolutions. This can be
            changed by using this method.
        
            Parameters:
                satelliteRevolution (int): number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def setSelectedCoefficients(self, set: java.util.Set[str]) -> None: ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, double2: float, orbit: org.orekit.orbits.Orbit) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for an AdaptativeStepsizeIntegrator.
        
            The errors are estimated from partial derivatives properties of orbits, starting from scalar position and velocity
            errors specified by the user.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (double): user specified position error (m)
                dV (double): user specified velocity error (m/s)
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
            Since:
                10.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, orbit: org.orekit.orbits.Orbit) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for an AdaptativeStepsizeIntegrator.
        
            The errors are estimated from partial derivatives properties of orbits, starting from a scalar position error specified
            by the user. Considering the energy conservation equation V = sqrt(mu (2/r - 1/a)), we get at constant energy (i.e. on a
            Keplerian trajectory):
        
            .. code-block: java
            
              V² r |dV| = mu |dr|
              
        
            So we deduce a scalar velocity error consistent with the position error. From here, we apply orbits Jacobians matrices
            to get consistent errors on orbital parameters.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (double): user specified position error (m)
                orbit (:class:`~org.orekit.orbits.Orbit`): reference orbit
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
        """
        ...

_FieldDSSTPropagator__T = typing.TypeVar('_FieldDSSTPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTPropagator(org.orekit.propagation.integration.FieldAbstractIntegratedPropagator[_FieldDSSTPropagator__T], typing.Generic[_FieldDSSTPropagator__T]):
    """
    public class FieldDSSTPropagator<T extends :class:`~org.orekit.propagation.semianalytical.dsst.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`<T>
    
        This class propagates :class:`~org.orekit.orbits.FieldOrbit` using the DSST theory.
    
        Whereas analytical propagators are configured only thanks to their various constructors and can be used immediately
        after construction, such a semianalytical propagator configuration involves setting several parameters between
        construction time and propagation time, just as numerical propagators.
    
        The configuration parameters that can be set are:
    
          - the initial spacecraft state (:meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInitialState`)
          - the various force models (:meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.addForceModel`,
            :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.removeForceModels`)
          - the discrete events that should be triggered during propagation (
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.addEventDetector`,
            :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.clearEventsDetectors`)
          - the binding logic with the rest of the application
            (:meth:`~org.orekit.propagation.FieldAbstractPropagator.getMultiplexer`)
    
    
        From these configuration parameters, only the initial state is mandatory. The default propagation settings are in
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` parameters with :meth:`~org.orekit.orbits.PositionAngle.TRUE` longitude
        argument. The central attraction coefficient used to define the initial orbit will be used. However, specifying only the
        initial state would mean the propagator would use only Keplerian forces. In this case, the simpler
        :class:`~org.orekit.propagation.analytical.KeplerianPropagator` class would be more effective.
    
        The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical
        configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the
        absolute and/or relative errors thresholds.
    
        The state that is seen by the integrator is a simple six elements double array. These six elements are:
    
          - the :class:`~org.orekit.orbits.FieldEquinoctialOrbit` (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ
            :sub:`m` ) in meters and radians,
    
    
        By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a
        new propagation to be started from there without recomputing the part already performed. This behaviour can be chenged
        by calling :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setResetAtEnd`.
    
        Beware the same instance cannot be used simultaneously by different threads, the class is *not* thread-safe.
    
        Since:
            10.0
    
        Also see:
            :class:`~org.orekit.propagation.FieldSpacecraftState`,
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T], propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T], propagationType: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, dSSTForceModel: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None:
        """
            Add a force model to the global perturbation model.
        
            If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
            Parameters:
                force (:class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`): perturbing :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel` to add
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.removeForceModels`,
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setMu`
        
        
        """
        ...
    _computeMeanState_0__T = typing.TypeVar('_computeMeanState_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanState_1__T = typing.TypeVar('_computeMeanState_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanState(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_0__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_0__T]: ...
    @typing.overload
    @staticmethod
    def computeMeanState(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_1__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], double: float, int: int) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_1__T]: ...
    _computeOsculatingState__T = typing.TypeVar('_computeOsculatingState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def computeOsculatingState(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeOsculatingState__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.FieldSpacecraftState[_computeOsculatingState__T]: ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]: ...
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
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngle:
        """
            Get propagation parameter type.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.getPositionAngleType` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Returns:
                angle type to use for propagation
        
        
        """
        ...
    def getSatelliteRevolution(self) -> int:
        """
            Get the number of satellite revolutions to use for converting osculating to mean elements.
        
            Returns:
                number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def getSelectedCoefficients(self) -> java.util.Set[str]: ...
    def initialIsOsculating(self) -> bool:
        """
            Check if the initial state is provided in osculating elements.
        
            Returns:
                true if initial state is provided in osculating elements
        
        
        """
        ...
    def removeForceModels(self) -> None:
        """
            Remove all perturbing force models from the global perturbation model (except central attraction).
        
            Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will
            follow a Keplerian evolution only.
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.addForceModel`
        
        
        """
        ...
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T]) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Set attitude provider.
        
            Specified by:
                :meth:`~org.orekit.propagation.FieldPropagator.setAttitudeProvider` in
                interface :class:`~org.orekit.propagation.FieldPropagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setAttitudeProvider` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): attitude provider
        
        
        """
        ...
    @typing.overload
    def setInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T]) -> None: ...
    @typing.overload
    def setInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T], propagationType: org.orekit.propagation.PropagationType) -> None: ...
    def setInterpolationGridToFixedNumberOfPoints(self, int: int) -> None:
        """
            Set the interpolation grid generator.
        
            The generator will create an interpolation grid with a fixed number of points for each mean element integration step.
        
            If neither
            :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInterpolationGridToFixedNumberOfPoints` nor
            :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInterpolationGridToMaxTimeGap` has been
            called, by default the propagator is set as to 3 interpolations points per step.
        
            Parameters:
                interpolationPoints (int): number of interpolation points at each integration step
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInterpolationGridToMaxTimeGap`
        
        
        """
        ...
    def setInterpolationGridToMaxTimeGap(self, t: _FieldDSSTPropagator__T) -> None:
        """
            Set the interpolation grid generator.
        
            The generator will create an interpolation grid with a maximum time gap between interpolation points.
        
            If neither
            :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInterpolationGridToFixedNumberOfPoints` nor
            :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInterpolationGridToMaxTimeGap` has been
            called, by default the propagator is set as to 3 interpolations points per step.
        
            Parameters:
                maxGap (:class:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator`): maximum time gap between interpolation points (seconds)
        
            Since:
                7.1
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.setInterpolationGridToFixedNumberOfPoints`
        
        
        """
        ...
    def setMu(self, t: _FieldDSSTPropagator__T) -> None:
        """
            Set the central attraction coefficient μ.
        
            Setting the central attraction coefficient is equivalent to
            :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.addForceModel` a
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTNewtonianAttraction` force model.
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator.setMu` in
                class :class:`~org.orekit.propagation.integration.FieldAbstractIntegratedPropagator`
        
            Parameters:
                mu (:class:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator`): central attraction coefficient (m³/s²)
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.addForceModel`,
                :meth:`~org.orekit.propagation.semianalytical.dsst.FieldDSSTPropagator.getAllForceModels`
        
        
        """
        ...
    def setSatelliteRevolution(self, int: int) -> None:
        """
            Override the default value of the parameter.
        
            By default, if the initial orbit is defined as osculating, it will be averaged over 2 satellite revolutions. This can be
            changed by using this method.
        
            Parameters:
                satelliteRevolution (int): number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def setSelectedCoefficients(self, set: java.util.Set[str]) -> None: ...
    _tolerances_0__T = typing.TypeVar('_tolerances_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _tolerances_1__T = typing.TypeVar('_tolerances_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tolerances(t: _tolerances_0__T, t2: _tolerances_0__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_tolerances_0__T]) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for an AdaptativeStepsizeIntegrator.
        
            The errors are estimated from partial derivatives properties of orbits, starting from scalar position and velocity
            errors specified by the user.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (T): user specified position error (m)
                dV (T): user specified velocity error (m/s)
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): reference orbit
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
            Since:
                10.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(t: _tolerances_1__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_tolerances_1__T]) -> typing.List[typing.List[float]]:
        """
            Estimate tolerance vectors for an AdaptativeStepsizeIntegrator.
        
            The errors are estimated from partial derivatives properties of orbits, starting from a scalar position error specified
            by the user. Considering the energy conservation equation V = sqrt(mu (2/r - 1/a)), we get at constant energy (i.e. on a
            Keplerian trajectory):
        
            .. code-block: java
            
              V² r |dV| = mu |dr|
              
        
            So we deduce a scalar velocity error consistent with the position error. From here, we apply orbits Jacobians matrices
            to get consistent errors on orbital parameters.
        
            The tolerances are only *orders of magnitude*, and integrator tolerances are only local estimates, not global ones. So
            some care must be taken when using these tolerances. Setting 1mm as a position error does NOT mean the tolerances will
            guarantee a 1mm error position after several orbits integration.
        
            Parameters:
                dP (T): user specified position error (m)
                orbit (:class:`~org.orekit.orbits.FieldOrbit`<T> orbit): reference orbit
        
            Returns:
                a two rows array, row 0 being the absolute tolerance error and row 1 being the relative tolerance error
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst")``.

    DSSTJacobiansMapper: typing.Type[DSSTJacobiansMapper]
    DSSTPartialDerivativesEquations: typing.Type[DSSTPartialDerivativesEquations]
    DSSTPropagator: typing.Type[DSSTPropagator]
    FieldDSSTPropagator: typing.Type[FieldDSSTPropagator]
    forces: org.orekit.propagation.semianalytical.dsst.forces.__module_protocol__
    utilities: org.orekit.propagation.semianalytical.dsst.utilities.__module_protocol__
