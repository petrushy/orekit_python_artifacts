
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.bodies
import org.orekit.forces
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class CR3BPConstants:
    """
    Set of useful physical CR3BP constants using JPL data.
    
    Since:
        11.0
    """
    @staticmethod
    def getEarthMoonBarycenterSemiMajorAxis(date: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> float:
        """
        Get the Earth-Moon barycenter semi-major axis.
        
        Parameters:
            date (AbsoluteDate): date
            timeScale (TimeScale): time scale
        
        Returns:
            the Earth-Moon barycenter semi-major axis in meters
        
        
        """
        ...
    @staticmethod
    def getJupiterSemiMajorAxis(date: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> float:
        """
        Get the Jupiter semi-major axis.
        
        Parameters:
            date (AbsoluteDate): date
            timeScale (TimeScale): time scale
        
        Returns:
            the Jupiter semi-major axis in meters
        
        
        """
        ...
    @staticmethod
    def getMoonSemiMajorAxis() -> float:
        """
        Get the Moon semi-major axis.
        
        Returns:
            the Moon semi-major axis in meters
        
        
        """
        ...

class CR3BPForceModel(org.orekit.forces.ForceModel):
    """
    Class calculating the acceleration induced by CR3BP model.
    
    Since:
        10.2
    
    Also see:
        "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    MASS_RATIO_SUFFIX: typing.ClassVar[str] = ...
    """
    Suffix for parameter name for Mass Ratio enabling Jacobian processing.
    
    Also see:
        constant
    
    
    """
    def __init__(self, cr3bp: org.orekit.bodies.CR3BPSystem):
        """
        Simple constructor.
        
        Parameters:
            cr3bp (CR3BPSystem): Name of the CR3BP System
        
        
        """
        ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Specified by: acceleration in interface ForceModel
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Specified by: dependsOnPositionOnly in interface ForceModel
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _getPotential_1__T = typing.TypeVar('_getPotential_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPotential(self, s: org.orekit.propagation.SpacecraftState) -> org.hipparchus.analysis.differentiation.DerivativeStructure:
        """
        Calculate spacecraft potential.
        
        Parameters:
            s (SpacecraftState): SpacecraftState
        
        Returns:
            Spacecraft Potential
        
        """
        ...
    @typing.overload
    def getPotential(self, s: org.orekit.propagation.FieldSpacecraftState[_getPotential_1__T]) -> org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_getPotential_1__T]:
        """
        Calculate spacecraft potential.
        
        Parameters:
            s (FieldSpacecraftState<T> s): SpacecraftState
        
        Returns:
            Spacecraft Potential
        
        
        """
        ...

class CR3BPMultipleShooter(org.orekit.utils.AbstractMultipleShooting):
    """
    Multiple shooting method applicable for orbits, either propagation in CR3BP, or in an ephemeris model.
    
    Also see:
        "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
        University"
    """
    def __init__(self, initialGuessList: java.util.List[org.orekit.propagation.SpacecraftState], propagatorList: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], stmEquations: java.util.List['STMEquations'], tolerance: float, maxIter: int):
        """
        Simple Constructor.
        
        Standard constructor for multiple shooting which can be used with the CR3BP model.
        
        Parameters:
            initialGuessList (List<SpacecraftState> initialGuessList): initial patch points to be corrected
            propagatorList (List<NumericalPropagator> propagatorList): list of propagators associated to each patch point
            stmEquations (List<STMEquations> stmEquations): list of additional derivatives providers linked to propagatorList
            tolerance (double): convergence tolerance on the constraint vector
            maxIter (int): maximum number of iterations
        
        
        """
        ...
    def setClosedOrbitConstraint(self, isClosed: bool) -> None:
        """
        Set the constraint of a closed orbit or not.
        
        Parameters:
            isClosed (boolean): true if orbit should be closed
        
        
        """
        ...
    def setEpochFreedom(self, patchIndex: int, isFree: bool) -> None:
        """
        Set the epoch of a patch point to free or not.
        
        Overrides: setEpochFreedom in class AbstractMultipleShooting
        
        Parameters:
            patchIndex (int): Patch point index (zero-based)
            isFree (boolean): constraint value
        
        
        """
        ...
    def setScaleLength(self, scaleLength: float) -> None:
        """
        Set the scale length.
        
        Overrides: setScaleLength in class AbstractMultipleShooting
        
        Parameters:
            scaleLength (double): scale length in meters
        
        
        """
        ...
    def setScaleTime(self, scaleTime: float) -> None:
        """
        Set the scale time.
        
        Overrides: setScaleTime in class AbstractMultipleShooting
        
        Parameters:
            scaleTime (double): scale time in seconds
        
        
        """
        ...

class STMEquations(org.orekit.propagation.integration.AdditionalDerivativesProvider):
    """
    Class calculating the state transition matrix coefficient for CR3BP Computation.
    
    Since:
        10.2
    
    Also see:
        "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    def __init__(self, syst: org.orekit.bodies.CR3BPSystem):
        """
        Simple constructor.
        
        Parameters:
            syst (CR3BPSystem): CR3BP System considered
        
        
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
    def getStateTransitionMatrix(self, s: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
        Method returning the State Transition Matrix.
        
        Parameters:
            s (SpacecraftState): SpacecraftState of the system
        
        Returns:
            State Transition Matrix
        
        
        """
        ...
    def setInitialPhi(self, s: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
        Method adding the standard initial values of the additional state to the initial spacecraft state.
        
        Parameters:
            s (SpacecraftState): Initial state of the system
        
        Returns:
            s Initial augmented (with the additional equations) state
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.numerical.cr3bp")``.

    CR3BPConstants: typing.Type[CR3BPConstants]
    CR3BPForceModel: typing.Type[CR3BPForceModel]
    CR3BPMultipleShooter: typing.Type[CR3BPMultipleShooter]
    STMEquations: typing.Type[STMEquations]
