
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.hipparchus
import org.hipparchus.linear
import org.hipparchus.ode
import org.orekit.attitudes
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.conversion.osc2mean
import org.orekit.propagation.integration
import org.orekit.propagation.semianalytical.dsst.forces
import org.orekit.propagation.semianalytical.dsst.utilities
import org.orekit.utils
import typing



class DSSTHarvester(org.orekit.propagation.AbstractMatricesHarvester):
    """
    public class DSSTHarvester extends :class:`~org.orekit.propagation.AbstractMatricesHarvester`
    
        Harvester between two-dimensional Jacobian matrices and one-dimensional
        :meth:`~org.orekit.propagation.SpacecraftState.getAdditionalState`.
    
        Since:
            11.1
    """
    def freezeColumnsNames(self) -> None:
        """
            Freeze the names of the Jacobian columns.
        
            This method is called when proagation starts, i.e. when configuration is completed
        
            Specified by:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.freezeColumnsNames` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
        
        """
        ...
    def getB1(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian matrix B1 (B1 = ∂εη/∂Y).
        
            B1 represents the partial derivatives of the short period motion with respect to the mean equinoctial elements.
        
            Returns:
                the B1 jacobian matrix
        
        
        """
        ...
    def getB2(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian matrix B2 (B2 = ∂Y/∂Y₀).
        
            B2 represents the partial derivatives of the mean equinoctial elements with respect to the initial ones.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                the B2 jacobian matrix
        
        
        """
        ...
    def getB3(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian matrix B3 (B3 = ∂Y/∂P).
        
            B3 represents the partial derivatives of the mean equinoctial elements with respect to the estimated propagation
            parameters.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                the B3 jacobian matrix
        
        
        """
        ...
    def getB4(self) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian matrix B4 (B4 = ∂εη/∂c).
        
            B4 represents the partial derivatives of the short period motion with respect to the estimated propagation parameters.
        
            Returns:
                the B4 jacobian matrix
        
        
        """
        ...
    def getJacobiansColumnsNames(self) -> java.util.List[str]: ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
            Get the orbit type used for the matrix computation.
        
            Returns:
                the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Get the Jacobian with respect to propagation parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getParametersJacobian` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.getParametersJacobian` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
            Get the position angle used for the matrix computation.
        
            Irrelevant if :meth:`~org.orekit.propagation.MatricesHarvester.getOrbitType` returns
            :meth:`~org.orekit.orbits.OrbitType.CARTESIAN`.
        
            Returns:
                the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Extract state transition matrix from state.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.getStateTransitionMatrix` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.getStateTransitionMatrix` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
        
            Returns:
                state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
                :class:`~org.orekit.orbits.OrbitType`.
        
        
        """
        ...
    @typing.overload
    def initializeFieldShortPeriodTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Initialize the short periodic terms for the "field" elements.
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): current mean spacecraft state
        
            Initialize the short periodic terms for the "field" elements.
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): current mean spacecraft state
                type (:class:`~org.orekit.propagation.PropagationType`): MEAN or OSCULATING
        
        
        """
        ...
    @typing.overload
    def initializeFieldShortPeriodTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
    def setReferenceState(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Set up reference state.
        
            This method is called whenever the global propagation reference state changes. This corresponds to the start of
            propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering.
            Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute
            analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not
            use it at all.
        
            Specified by:
                :meth:`~org.orekit.propagation.MatricesHarvester.setReferenceState` in
                interface :class:`~org.orekit.propagation.MatricesHarvester`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractMatricesHarvester.setReferenceState` in
                class :class:`~org.orekit.propagation.AbstractMatricesHarvester`
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): reference state to set
        
        
        """
        ...
    def updateFieldShortPeriodTerms(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> None:
        """
            Update the short periodic terms for the "field" elements.
        
            Parameters:
                reference (:class:`~org.orekit.propagation.SpacecraftState`): current mean spacecraft state
        
        
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
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` parameters with :meth:`~org.orekit.orbits.PositionAngleType.TRUE`
        longitude argument. The central attraction coefficient used to define the initial orbit will be used. However,
        specifying only the initial state would mean the propagator would use only Keplerian forces. In this case, the simpler
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
    @typing.overload
    @staticmethod
    def computeMeanState(spacecraftState: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], osculatingToMeanConverter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.propagation.SpacecraftState: ...
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
    def getSatelliteRevolution(self) -> int:
        """
            Get the number of satellite revolutions to use for converting osculating to mean elements.
        
            Returns:
                number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def getSelectedCoefficients(self) -> java.util.Set[str]: ...
    def getShortPeriodTerms(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms]: ...
    def getShortPeriodTermsValue(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
            Get the short period terms value.
        
            Parameters:
                meanState (:class:`~org.orekit.propagation.SpacecraftState`): the mean state
        
            Returns:
                shortPeriodTerms short period terms
        
            Since:
                7.1
        
        
        """
        ...
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
    @typing.overload
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
        
            Reset initial state with a given propagation type.
        
            By default this method returns the same as :meth:`~org.orekit.propagation.AbstractPropagator.resetInitialState`
        
            Its purpose is mostly to be derived in DSSTPropagator.
        
            Change parameter :meth:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator.initialIsOsculating` accordingly
        
            Overrides:
                :meth:`~org.orekit.propagation.integration.AbstractIntegratedPropagator.resetInitialState` in
                class :class:`~org.orekit.propagation.integration.AbstractIntegratedPropagator`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): new initial state to consider
                stateType (:class:`~org.orekit.propagation.PropagationType`): type of the new state (mean or osculating)
        
            Since:
                12.1.3
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, spacecraftState: org.orekit.propagation.SpacecraftState, propagationType: org.orekit.propagation.PropagationType) -> None: ...
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
    def setShortPeriodTerms(self, list: java.util.List[org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms]) -> None: ...
    def setupMatricesComputation(self, string: str, realMatrix: org.hipparchus.linear.RealMatrix, doubleArrayDictionary: org.orekit.utils.DoubleArrayDictionary) -> DSSTHarvester:
        """
            Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
            If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that
            will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
            The arguments for initial matrices *must* be compatible with the :class:`~org.orekit.orbits.OrbitType` and
            :class:`~org.orekit.orbits.PositionAngleType` that will be used by the propagator.
        
            The default implementation throws an exception as the method is not supported by all propagators.
        
            Specified by:
                :meth:`~org.orekit.propagation.Propagator.setupMatricesComputation` in
                interface :class:`~org.orekit.propagation.Propagator`
        
            Overrides:
                :meth:`~org.orekit.propagation.AbstractPropagator.setupMatricesComputation` in
                class :class:`~org.orekit.propagation.AbstractPropagator`
        
            Parameters:
                stmName (:class:`~org.orekit.propagation.semianalytical.dsst.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): State Transition Matrix state name
                initialStm (:class:`~org.orekit.propagation.semianalytical.dsst.https:.www.hipparchus.org.apidocs.org.hipparchus.linear.RealMatrix?is`): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
                initialJacobianColumns (:class:`~org.orekit.utils.DoubleArrayDictionary`): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                    from the dictionary, the corresponding initial column is assumed to be 0
        
            Returns:
                harvester to retrieve computed matrices during and after propagation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, double2: float, orbit: org.orekit.orbits.Orbit) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(double: float, orbit: org.orekit.orbits.Orbit) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

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
        :meth:`~org.orekit.orbits.OrbitType.EQUINOCTIAL` parameters with :meth:`~org.orekit.orbits.PositionAngleType.TRUE`
        longitude argument. The central attraction coefficient used to define the initial orbit will be used. However,
        specifying only the initial state would mean the propagator would use only Keplerian forces. In this case, the simpler
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
    _computeMeanState_2__T = typing.TypeVar('_computeMeanState_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanState(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_0__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_0__T]: ...
    @typing.overload
    @staticmethod
    def computeMeanState(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_1__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], double: float, int: int) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_1__T]: ...
    @typing.overload
    @staticmethod
    def computeMeanState(fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_2__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, collection: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], osculatingToMeanConverter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_2__T]: ...
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
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T], propagationType: org.orekit.propagation.PropagationType) -> None: ...
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
    def tolerances(t: _tolerances_0__T, t2: _tolerances_0__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_tolerances_0__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(t: _tolerances_1__T, fieldOrbit: org.orekit.orbits.FieldOrbit[_tolerances_1__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst")``.

    DSSTHarvester: typing.Type[DSSTHarvester]
    DSSTPropagator: typing.Type[DSSTPropagator]
    FieldDSSTPropagator: typing.Type[FieldDSSTPropagator]
    forces: org.orekit.propagation.semianalytical.dsst.forces.__module_protocol__
    utilities: org.orekit.propagation.semianalytical.dsst.utilities.__module_protocol__
