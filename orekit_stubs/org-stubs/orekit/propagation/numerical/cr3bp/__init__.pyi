
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
    public class CR3BPConstants extends :class:`~org.orekit.propagation.numerical.cr3bp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Set of useful physical CR3BP constants using JPL data.
    
        Since:
            11.0
    """
    @staticmethod
    def getEarthMoonBarycenterSemiMajorAxis(absoluteDate: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> float:
        """
            Get the Earth-Moon barycenter semi-major axis.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale
        
            Returns:
                the Earth-Moon barycenter semi-major axis in meters
        
        
        """
        ...
    @staticmethod
    def getJupiterSemiMajorAxis(absoluteDate: org.orekit.time.AbsoluteDate, timeScale: org.orekit.time.TimeScale) -> float:
        """
            Get the Jupiter semi-major axis.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                timeScale (:class:`~org.orekit.time.TimeScale`): time scale
        
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
    public class CR3BPForceModel extends :class:`~org.orekit.propagation.numerical.cr3bp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.forces.ForceModel`
    
        Class calculating the acceleration induced by CR3BP model.
    
        Since:
            10.2
    
        Also see:
            "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    MASS_RATIO_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.numerical.cr3bp.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` MASS_RATIO_SUFFIX
    
        Suffix for parameter name for Mass Ratio enabling Jacobian processing.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.acceleration` in interface :class:`~org.orekit.forces.ForceModel`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force model depends on position only at a given, fixed date.
        
            Specified by:
                :meth:`~org.orekit.forces.ForceModel.dependsOnPositionOnly` in interface :class:`~org.orekit.forces.ForceModel`
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _getPotential_1__T = typing.TypeVar('_getPotential_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPotential(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.analysis.differentiation.DerivativeStructure:
        """
            Calculate spacecraft potential.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpacecraftState
        
            Returns:
                Spacecraft Potential
        
        """
        ...
    @typing.overload
    def getPotential(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getPotential_1__T]) -> org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_getPotential_1__T]:
        """
            Calculate spacecraft potential.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): SpacecraftState
        
            Returns:
                Spacecraft Potential
        
        
        """
        ...

class CR3BPMultipleShooter(org.orekit.utils.AbstractMultipleShooting):
    """
    public class CR3BPMultipleShooter extends :class:`~org.orekit.utils.AbstractMultipleShooting`
    
        Multiple shooting method applicable for orbits, either propagation in CR3BP, or in an ephemeris model.
    
        Also see:
            "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
            University"
    """
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], list3: java.util.List['STMEquations'], double: float, int: int): ...
    def setClosedOrbitConstraint(self, boolean: bool) -> None:
        """
            Set the constraint of a closed orbit or not.
        
            Parameters:
                isClosed (boolean): true if orbit should be closed
        
        
        """
        ...
    def setEpochFreedom(self, int: int, boolean: bool) -> None:
        """
            Set the epoch of a patch point to free or not.
        
            Overrides:
                :meth:`~org.orekit.utils.AbstractMultipleShooting.setEpochFreedom` in
                class :class:`~org.orekit.utils.AbstractMultipleShooting`
        
            Parameters:
                patchIndex (int): Patch point index (zero-based)
                isFree (boolean): constraint value
        
        
        """
        ...
    def setScaleLength(self, double: float) -> None:
        """
            Set the scale length.
        
            Overrides:
                :meth:`~org.orekit.utils.AbstractMultipleShooting.setScaleLength` in
                class :class:`~org.orekit.utils.AbstractMultipleShooting`
        
            Parameters:
                scaleLength (double): scale length in meters
        
        
        """
        ...
    def setScaleTime(self, double: float) -> None:
        """
            Set the scale time.
        
            Overrides:
                :meth:`~org.orekit.utils.AbstractMultipleShooting.setScaleTime` in
                class :class:`~org.orekit.utils.AbstractMultipleShooting`
        
            Parameters:
                scaleTime (double): scale time in seconds
        
        
        """
        ...

class STMEquations(org.orekit.propagation.integration.AdditionalDerivativesProvider):
    """
    public class STMEquations extends :class:`~org.orekit.propagation.numerical.cr3bp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
    
        Class calculating the state transition matrix coefficient for CR3BP Computation.
    
        Since:
            10.2
    
        Also see:
            "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem): ...
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
    def getStateTransitionMatrix(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.hipparchus.linear.RealMatrix:
        """
            Method returning the State Transition Matrix.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): SpacecraftState of the system
        
            Returns:
                phiM State Transition Matrix
        
        
        """
        ...
    def setInitialPhi(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.SpacecraftState:
        """
            Method adding the standard initial values of the additional state to the initial spacecraft state.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): Initial state of the system
        
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
