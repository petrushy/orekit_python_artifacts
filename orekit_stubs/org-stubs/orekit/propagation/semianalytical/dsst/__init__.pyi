
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
    Harvester between two-dimensional Jacobian matrices and one-dimensional getAdditionalState.
    
    Since:
        11.1
    """
    def freezeColumnsNames(self) -> None:
        """
        Freeze the names of the Jacobian columns.
        
        This method is called when proagation starts, i.e. when configuration is completed
        
        Specified by: freezeColumnsNames in class AbstractMatricesHarvester
        
        
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
    def getB2(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian matrix B2 (B2 = ∂Y/∂Y₀).
        
        B2 represents the partial derivatives of the mean equinoctial elements with respect to the initial ones.
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            the B2 jacobian matrix
        
        
        """
        ...
    def getB3(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian matrix B3 (B3 = ∂Y/∂P).
        
        B3 represents the partial derivatives of the mean equinoctial elements with respect to the estimated propagation parameters.
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
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
    def getJacobiansColumnsNames(self) -> java.util.List[str]:
        """
        Get the names of the parameters in the matrix returned by getParametersJacobian.
        
        Beware that the names of the parameters are fully known only once all force models have been set up and their parameters properly selected. Applications that retrieve the matrices harvester first and select the force model parameters to retrieve afterwards (but obviously before starting propagation) must take care to wait until the parameters have been set up before they call this method. Calling the method too early would return wrong results.
        
        The names are returned in the Jacobians matrix columns order
        
        Returns:
            names of the parameters (i.e. columns) of the Jacobian matrix
        
        
        """
        ...
    def getOrbitType(self) -> org.orekit.orbits.OrbitType:
        """
        Get the orbit type used for the matrix computation.
        
        Returns:
            the orbit type used for the matrix computation
        
        
        """
        ...
    def getParametersJacobian(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Get the Jacobian with respect to propagation parameters.
        
        Specified by: getParametersJacobian in interface MatricesHarvester
        
        Overrides: getParametersJacobian in class AbstractMatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            Jacobian with respect to propagation parameters, or null if there are no parameters
        
        
        """
        ...
    def getPositionAngleType(self) -> org.orekit.orbits.PositionAngleType:
        """
        Get the position angle used for the matrix computation.
        
        Irrelevant if getOrbitType returns CARTESIAN.
        
        Returns:
            the position angle used for the matrix computation
        
        
        """
        ...
    def getStateTransitionMatrix(self, state: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Extract state transition matrix from state.
        
        Specified by: getStateTransitionMatrix in interface MatricesHarvester
        
        Overrides: getStateTransitionMatrix in class AbstractMatricesHarvester
        
        Parameters:
            state (SpacecraftState): spacecraft state
        
        Returns:
            state transition matrix, with semantics consistent with propagation, or null if no state transition matrix is available
            OrbitType.
        
        
        """
        ...
    @typing.overload
    def initializeFieldShortPeriodTerms(self, reference: org.orekit.propagation.SpacecraftState) -> None:
        """
        Initialize the short periodic terms for the "field" elements.
        
        Parameters:
            reference (SpacecraftState): current mean spacecraft state
        
        Initialize the short periodic terms for the "field" elements.
        
        Parameters:
            reference (SpacecraftState): current mean spacecraft state
            type (PropagationType): MEAN or OSCULATING
        
        
        """
        ...
    @typing.overload
    def initializeFieldShortPeriodTerms(self, reference: org.orekit.propagation.SpacecraftState, type: org.orekit.propagation.PropagationType) -> None: ...
    def setReferenceState(self, reference: org.orekit.propagation.SpacecraftState) -> None:
        """
        Set up reference state.
        
        This method is called whenever the global propagation reference state changes. This corresponds to the start of propagation in batch least squares orbit determination or at prediction step for each measurement in Kalman filtering. Its goal is to allow the harvester to compute some internal data. Analytical models like TLE use it to compute analytical derivatives, semi-analytical models like DSST use it to compute short periodic terms, numerical models do not use it at all.
        
        Specified by: setReferenceState in interface MatricesHarvester
        
        Overrides: setReferenceState in class AbstractMatricesHarvester
        
        Parameters:
            reference (SpacecraftState): reference state to set
        
        
        """
        ...
    def updateFieldShortPeriodTerms(self, reference: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short periodic terms for the "field" elements.
        
        Parameters:
            reference (SpacecraftState): current mean spacecraft state
        
        
        """
        ...

class DSSTPropagator(org.orekit.propagation.integration.AbstractIntegratedPropagator):
    """
    This class propagates Orbit using the DSST theory.
    
    Whereas analytical propagators are configured only thanks to their various constructors and can be used immediately after construction, such a semianalytical propagator configuration involves setting several parameters between construction time and propagation time, just as numerical propagators.
    
    The configuration parameters that can be set are:
    
      - the initial spacecraft state (setInitialState)
      - the various force models (addForceModel,
        removeForceModels)
      - the discrete events that should be triggered during propagation (
        addEventDetector,
        clearEventsDetectors)
      - the binding logic with the rest of the application (getMultiplexer)
    
    From these configuration parameters, only the initial state is mandatory. The default propagation settings are in EQUINOCTIAL parameters with TRUE longitude argument. The central attraction coefficient used to define the initial orbit will be used. However, specifying only the initial state would mean the propagator would use only Keplerian forces. In this case, the simpler KeplerianPropagator class would be more effective.
    
    The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the absolute and/or relative errors thresholds.
    
    The state that is seen by the integrator is a simple six elements double array. These six elements are:
    
      - the EquinoctialOrbit (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ :sub:`m` )
        in meters and radians,
    
    By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a new propagation to be started from there without recomputing the part already performed. This behaviour can be chenged by calling setResetAtEnd.
    
    Beware the same instance cannot be used simultaneously by different threads, the class is not thread-safe.
    
    Also see:
        SpacecraftState,
        DSSTForceModel
    """
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.ODEIntegrator): ...
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.ODEIntegrator, propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, integrator: org.hipparchus.ode.ODEIntegrator, propagationType: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, force: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None:
        """
        Add a force model to the global perturbation model.
        
        If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
        Parameters:
            force (DSSTForceModel): perturbing DSSTForceModel to add
        
        Also see:
            removeForceModels,
            setMu
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeMeanState(osculating: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, forceModels: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.SpacecraftState: ...
    @typing.overload
    @staticmethod
    def computeMeanState(osculating: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, forceModels: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], epsilon: float, maxIterations: int) -> org.orekit.propagation.SpacecraftState: ...
    @typing.overload
    @staticmethod
    def computeMeanState(osculating: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, forceModels: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.propagation.SpacecraftState: ...
    @staticmethod
    def computeOsculatingState(mean: org.orekit.propagation.SpacecraftState, attitudeProvider: org.orekit.attitudes.AttitudeProvider, forces: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.SpacecraftState:
        """
        Conversion from mean to osculating orbit.
        
        Compute osculating state in a DSST sense, corresponding to the mean SpacecraftState in input, and according to the Force models taken into account.
        
        Since the osculating state is obtained by adding short-periodic variation of each force model, the resulting output will depend on the force models parameterized in input.
        
        Parameters:
            mean (SpacecraftState): Mean state to convert
            forces (AttitudeProvider): Forces to take into account
            attitudeProvider (Collection<DSSTForceModel> forces): attitude provider (may be null if there are no Gaussian force models like atmospheric drag, radiation pressure or
                specific user-defined models)
        
        Returns:
            osculating state in a DSST sense
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]:
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
            orbit type used for propagation
        
        
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
    def getSatelliteRevolution(self) -> int:
        """
        Get the number of satellite revolutions to use for converting osculating to mean elements.
        
        Returns:
            number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def getSelectedCoefficients(self) -> java.util.Set[str]:
        """
        Get the selected short periodic coefficients that must be stored as additional states.
        
        Returns:
            short periodic coefficients that must be stored as additional states (null means no coefficients are selected, empty set
            means all coefficients are selected)
        
        
        """
        ...
    def getShortPeriodTerms(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms]:
        """
        Get the short periodic terms.
        
        Returns:
            the short periodic terms
        
        
        """
        ...
    def getShortPeriodTermsValue(self, meanState: org.orekit.propagation.SpacecraftState) -> typing.MutableSequence[float]:
        """
        Get the short period terms value.
        
        Parameters:
            meanState (SpacecraftState): the mean state
        
        Returns:
            short period terms
        
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
        
        Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will follow a Keplerian evolution only.
        
        Also see:
            addForceModel
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Reset the initial state.
        
        Specified by: resetInitialState in interface Propagator
        
        Overrides: resetInitialState in class AbstractPropagator
        
        Parameters:
            state (SpacecraftState): new initial state
        
        Reset initial state with a given propagation type.
        
        By default this method returns the same as resetInitialState
        
        Its purpose is mostly to be derived in DSSTPropagator.
        
        Change parameter initialIsOsculating accordingly
        
        Overrides: resetInitialState in class AbstractIntegratedPropagator
        
        Parameters:
            state (SpacecraftState): new initial state to consider
            stateType (PropagationType): type of the new state (mean or osculating)
        
        Since:
            12.1.3
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface Propagator
        
        Overrides: setAttitudeProvider in class AbstractIntegratedPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    @typing.overload
    def setInitialState(self, initialState: org.orekit.propagation.SpacecraftState) -> None:
        """
        Set the initial state with osculating orbital elements.
        
        Parameters:
            initialState (SpacecraftState): initial state (defined with osculating elements)
        
        Set the initial state.
        
        Parameters:
            initialState (SpacecraftState): initial state
            stateType (PropagationType): defined if the orbital state is defined with osculating or mean elements
        
        
        """
        ...
    @typing.overload
    def setInitialState(self, initialState: org.orekit.propagation.SpacecraftState, stateType: org.orekit.propagation.PropagationType) -> None: ...
    def setInterpolationGridToFixedNumberOfPoints(self, interpolationPoints: int) -> None:
        """
        Set the interpolation grid generator.
        
        The generator will create an interpolation grid with a fixed number of points for each mean element integration step.
        
        If neither setInterpolationGridToFixedNumberOfPoints nor setInterpolationGridToMaxTimeGap has been called, by default the propagator is set as to 3 interpolations points per step.
        
        Parameters:
            interpolationPoints (int): number of interpolation points at each integration step
        
        Since:
            7.1
        
        Also see:
            setInterpolationGridToMaxTimeGap
        
        
        """
        ...
    def setInterpolationGridToMaxTimeGap(self, maxGap: float) -> None:
        """
        Set the interpolation grid generator.
        
        The generator will create an interpolation grid with a maximum time gap between interpolation points.
        
        If neither setInterpolationGridToFixedNumberOfPoints nor setInterpolationGridToMaxTimeGap has been called, by default the propagator is set as to 3 interpolations points per step.
        
        Parameters:
            maxGap (double): maximum time gap between interpolation points (seconds)
        
        Since:
            7.1
        
        Also see:
            setInterpolationGridToFixedNumberOfPoints
        
        
        """
        ...
    def setMu(self, mu: float) -> None:
        """
        Set the central attraction coefficient μ.
        
        Setting the central attraction coefficient is equivalent to addForceModel a DSSTNewtonianAttraction force model.
        
        Overrides: setMu in class AbstractIntegratedPropagator
        
        Parameters:
            mu (double): central attraction coefficient (m³/s²)
        
        Also see:
            addForceModel,
            getAllForceModels
        
        
        """
        ...
    def setSatelliteRevolution(self, satelliteRevolution: int) -> None:
        """
        Override the default value of the parameter.
        
        By default, if the initial orbit is defined as osculating, it will be averaged over 2 satellite revolutions. This can be changed by using this method.
        
        Parameters:
            satelliteRevolution (int): number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def setSelectedCoefficients(self, selectedCoefficients: java.util.Set[str]) -> None:
        """
        Set the selected short periodic coefficients that must be stored as additional states.
        
        Parameters:
            selectedCoefficients (Set<String> selectedCoefficients): short periodic coefficients that must be stored as additional states (null means no coefficients are selected, empty set
                means all coefficients are selected)
        
        
        """
        ...
    def setShortPeriodTerms(self, shortPeriodTerms: java.util.List[org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms]) -> None:
        """
        Override the default value short periodic terms.
        
        By default, short periodic terms are initialized before the numerical integration of the mean orbital elements.
        
        Parameters:
            shortPeriodTerms (List<ShortPeriodTerms> shortPeriodTerms): short periodic terms
        
        
        """
        ...
    def setupMatricesComputation(self, stmName: str, initialStm: org.hipparchus.linear.RealMatrix, initialJacobianColumns: org.orekit.utils.DoubleArrayDictionary) -> DSSTHarvester:
        """
        Set up computation of State Transition Matrix and Jacobians matrix with respect to parameters.
        
        If this method is called, both State Transition Matrix and Jacobians with respect to the force models parameters that will be selected when propagation starts will be automatically computed, and the harvester will allow to retrieve them.
        
        The arguments for initial matrices must be compatible with the OrbitType and PositionAngleType that will be used by the propagator.
        
        The default implementation throws an exception as the method is not supported by all propagators.
        
        Specified by: setupMatricesComputation in interface Propagator
        
        Overrides: setupMatricesComputation in class AbstractPropagator
        
        Parameters:
            stmName (String): State Transition Matrix state name
            initialStm (RealMatrix): initial State Transition Matrix ∂Y/∂Y₀, if null (which is the most frequent case), assumed to be 6x6 identity
            initialJacobianColumns (DoubleArrayDictionary): initial columns of the Jacobians matrix with respect to parameters, if null or if some selected parameters are missing
                from the dictionary, the corresponding initial column is assumed to be 0
        
        Returns:
            harvester to retrieve computed matrices during and after propagation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def tolerances(dP: float, dV: float, orbit: org.orekit.orbits.Orbit) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(dP: float, orbit: org.orekit.orbits.Orbit) -> typing.MutableSequence[typing.MutableSequence[float]]: ...

_FieldDSSTPropagator__T = typing.TypeVar('_FieldDSSTPropagator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTPropagator(org.orekit.propagation.integration.FieldAbstractIntegratedPropagator[_FieldDSSTPropagator__T], typing.Generic[_FieldDSSTPropagator__T]):
    """
    This class propagates FieldOrbit using the DSST theory.
    
    Whereas analytical propagators are configured only thanks to their various constructors and can be used immediately after construction, such a semianalytical propagator configuration involves setting several parameters between construction time and propagation time, just as numerical propagators.
    
    The configuration parameters that can be set are:
    
      - the initial spacecraft state (setInitialState)
      - the various force models (addForceModel,
        removeForceModels)
      - the discrete events that should be triggered during propagation (
        addEventDetector,
        clearEventsDetectors)
      - the binding logic with the rest of the application
        (getMultiplexer)
    
    From these configuration parameters, only the initial state is mandatory. The default propagation settings are in EQUINOCTIAL parameters with TRUE longitude argument. The central attraction coefficient used to define the initial orbit will be used. However, specifying only the initial state would mean the propagator would use only Keplerian forces. In this case, the simpler KeplerianPropagator class would be more effective.
    
    The underlying numerical integrator set up in the constructor may also have its own configuration parameters. Typical configuration parameters for adaptive stepsize integrators are the min, max and perhaps start step size as well as the absolute and/or relative errors thresholds.
    
    The state that is seen by the integrator is a simple six elements double array. These six elements are:
    
      - the FieldEquinoctialOrbit (a, e :sub:`x` , e :sub:`y` , h :sub:`x` , h :sub:`y` , λ
        :sub:`m` ) in meters and radians,
    
    By default, at the end of the propagation, the propagator resets the initial state to the final state, thus allowing a new propagation to be started from there without recomputing the part already performed. This behaviour can be chenged by calling setResetAtEnd.
    
    Beware the same instance cannot be used simultaneously by different threads, the class is not thread-safe.
    
    Since:
        10.0
    
    Also see:
        FieldSpacecraftState,
        DSSTForceModel
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], integrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], fieldODEIntegrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T], propagationType: org.orekit.propagation.PropagationType): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldDSSTPropagator__T], integrator: org.hipparchus.ode.FieldODEIntegrator[_FieldDSSTPropagator__T], propagationType: org.orekit.propagation.PropagationType, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def addForceModel(self, force: org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel) -> None:
        """
        Add a force model to the global perturbation model.
        
        If this method is not called at all, the integrated orbit will follow a Keplerian evolution only.
        
        Parameters:
            force (DSSTForceModel): perturbing DSSTForceModel to add
        
        Also see:
            removeForceModels,
            setMu
        
        
        """
        ...
    _computeMeanState_0__T = typing.TypeVar('_computeMeanState_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanState_1__T = typing.TypeVar('_computeMeanState_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _computeMeanState_2__T = typing.TypeVar('_computeMeanState_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeMeanState(osculating: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_0__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, forceModel: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_0__T]: ...
    @typing.overload
    @staticmethod
    def computeMeanState(osculating: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_1__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, forceModel: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], epsilon: float, maxIterations: int) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_1__T]: ...
    @typing.overload
    @staticmethod
    def computeMeanState(osculating: org.orekit.propagation.FieldSpacecraftState[_computeMeanState_2__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, forceModel: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]], converter: org.orekit.propagation.conversion.osc2mean.OsculatingToMeanConverter) -> org.orekit.propagation.FieldSpacecraftState[_computeMeanState_2__T]: ...
    _computeOsculatingState__T = typing.TypeVar('_computeOsculatingState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def computeOsculatingState(mean: org.orekit.propagation.FieldSpacecraftState[_computeOsculatingState__T], attitudeProvider: org.orekit.attitudes.AttitudeProvider, forces: typing.Union[java.util.Collection[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Sequence[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel], typing.Set[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]]) -> org.orekit.propagation.FieldSpacecraftState[_computeOsculatingState__T]:
        """
        Conversion from mean to osculating orbit.
        
        Compute osculating state in a DSST sense, corresponding to the mean SpacecraftState in input, and according to the Force models taken into account.
        
        Since the osculating state is obtained by adding short-periodic variation of each force model, the resulting output will depend on the force models parameterized in input.
        
        Parameters:
            mean (FieldSpacecraftState<T> mean): Mean state to convert
            forces (AttitudeProvider): Forces to take into account
            attitudeProvider (Collection<DSSTForceModel> forces): attitude provider (may be null if there are no Gaussian force models like atmospheric drag, radiation pressure or
                specific user-defined models)
        
        Returns:
            osculating state in a DSST sense
        
        
        """
        ...
    def getAllForceModels(self) -> java.util.List[org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel]:
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
    def getSatelliteRevolution(self) -> int:
        """
        Get the number of satellite revolutions to use for converting osculating to mean elements.
        
        Returns:
            number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def getSelectedCoefficients(self) -> java.util.Set[str]:
        """
        Get the selected short periodic coefficients that must be stored as additional states.
        
        Returns:
            short periodic coefficients that must be stored as additional states (null means no coefficients are selected, empty set
            means all coefficients are selected)
        
        
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
        
        Once all perturbing forces have been removed (and as long as no new force model is added), the integrated orbit will follow a Keplerian evolution only.
        
        Also see:
            addForceModel
        
        
        """
        ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T]) -> None: ...
    @typing.overload
    def resetInitialState(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T], stateType: org.orekit.propagation.PropagationType) -> None: ...
    def setAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Set attitude provider.
        
        Specified by: setAttitudeProvider in interface FieldPropagator
        
        Overrides: setAttitudeProvider in class FieldAbstractIntegratedPropagator
        
        Parameters:
            attitudeProvider (AttitudeProvider): attitude provider
        
        
        """
        ...
    @typing.overload
    def setInitialState(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T]) -> None: ...
    @typing.overload
    def setInitialState(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldDSSTPropagator__T], stateType: org.orekit.propagation.PropagationType) -> None: ...
    def setInterpolationGridToFixedNumberOfPoints(self, interpolationPoints: int) -> None:
        """
        Set the interpolation grid generator.
        
        The generator will create an interpolation grid with a fixed number of points for each mean element integration step.
        
        If neither setInterpolationGridToFixedNumberOfPoints nor setInterpolationGridToMaxTimeGap has been called, by default the propagator is set as to 3 interpolations points per step.
        
        Parameters:
            interpolationPoints (int): number of interpolation points at each integration step
        
        Since:
            7.1
        
        Also see:
            setInterpolationGridToMaxTimeGap
        
        
        """
        ...
    def setInterpolationGridToMaxTimeGap(self, maxGap: _FieldDSSTPropagator__T) -> None:
        """
        Set the interpolation grid generator.
        
        The generator will create an interpolation grid with a maximum time gap between interpolation points.
        
        If neither setInterpolationGridToFixedNumberOfPoints nor setInterpolationGridToMaxTimeGap has been called, by default the propagator is set as to 3 interpolations points per step.
        
        Parameters:
            maxGap (FieldDSSTPropagator): maximum time gap between interpolation points (seconds)
        
        Since:
            7.1
        
        Also see:
            setInterpolationGridToFixedNumberOfPoints
        
        
        """
        ...
    def setMu(self, mu: _FieldDSSTPropagator__T) -> None:
        """
        Set the central attraction coefficient μ.
        
        Setting the central attraction coefficient is equivalent to addForceModel a DSSTNewtonianAttraction force model.
        
        Overrides: setMu in class FieldAbstractIntegratedPropagator
        
        Parameters:
            mu (FieldDSSTPropagator): central attraction coefficient (m³/s²)
        
        Also see:
            addForceModel,
            getAllForceModels
        
        
        """
        ...
    def setSatelliteRevolution(self, satelliteRevolution: int) -> None:
        """
        Override the default value of the parameter.
        
        By default, if the initial orbit is defined as osculating, it will be averaged over 2 satellite revolutions. This can be changed by using this method.
        
        Parameters:
            satelliteRevolution (int): number of satellite revolutions to use for converting osculating to mean elements
        
        
        """
        ...
    def setSelectedCoefficients(self, selectedCoefficients: java.util.Set[str]) -> None:
        """
        Set the selected short periodic coefficients that must be stored as additional states.
        
        Parameters:
            selectedCoefficients (Set<String> selectedCoefficients): short periodic coefficients that must be stored as additional states (null means no coefficients are selected, empty set
                means all coefficients are selected)
        
        
        """
        ...
    _tolerances_0__T = typing.TypeVar('_tolerances_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _tolerances_1__T = typing.TypeVar('_tolerances_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def tolerances(dP: _tolerances_0__T, dV: _tolerances_0__T, orbit: org.orekit.orbits.FieldOrbit[_tolerances_0__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    @staticmethod
    def tolerances(dP: _tolerances_1__T, orbit: org.orekit.orbits.FieldOrbit[_tolerances_1__T]) -> typing.MutableSequence[typing.MutableSequence[float]]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst")``.

    DSSTHarvester: typing.Type[DSSTHarvester]
    DSSTPropagator: typing.Type[DSSTPropagator]
    FieldDSSTPropagator: typing.Type[FieldDSSTPropagator]
    forces: org.orekit.propagation.semianalytical.dsst.forces.__module_protocol__
    utilities: org.orekit.propagation.semianalytical.dsst.utilities.__module_protocol__
