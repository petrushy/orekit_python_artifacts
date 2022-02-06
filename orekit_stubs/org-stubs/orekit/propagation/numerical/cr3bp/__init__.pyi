import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.linear
import org.orekit.bodies
import org.orekit.forces
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.integration
import org.orekit.propagation.numerical
import org.orekit.time
import org.orekit.utils
import typing



class CR3BPConstants:
    """
    public class CR3BPConstants extends Object
    
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

class CR3BPForceModel(org.orekit.forces.AbstractForceModel):
    """
    public class CR3BPForceModel extends :class:`~org.orekit.forces.AbstractForceModel`
    
        Class calculating the acceleration induced by CR3BP model.
    
        Since:
            10.2
    
        Also see:
            "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    MASS_RATIO_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final String MASS_RATIO_SUFFIX
    
        Suffix for parameter name for Mass Ratio enabling Jacobian processing.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
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
        
            Calculate spacecraft potential.
        
            Parameters:
                s (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> s): SpacecraftState
        
            Returns:
                Spacecraft Potential
        
        
        """
        ...
    @typing.overload
    def getPotential(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getPotential_1__T]) -> org.hipparchus.analysis.differentiation.FieldDerivativeStructure[_getPotential_1__T]: ...

class CR3BPMultipleShooter(org.orekit.utils.AbstractMultipleShooting):
    """
    public class CR3BPMultipleShooter extends :class:`~org.orekit.utils.AbstractMultipleShooting`
    
        Multiple shooting method applicable for orbits, either propagation in CR3BP, or in an ephemeris model.
    
        Also see:
            "TRAJECTORY DESIGN AND ORBIT MAINTENANCE STRATEGIES IN MULTI-BODY DYNAMICAL REGIMES by Thomas A. Pavlak, Purdue
            University"
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], list3: java.util.List[org.orekit.propagation.integration.AdditionalEquations], double: float, double2: float): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.propagation.SpacecraftState], list2: java.util.List[org.orekit.propagation.numerical.NumericalPropagator], list3: java.util.List['STMEquations'], double: float, double2: float, int: int): ...

class STMEquations(org.orekit.propagation.integration.AdditionalDerivativesProvider, org.orekit.propagation.integration.AdditionalEquations):
    """
    public class STMEquations extends Object implements :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`, :class:`~org.orekit.propagation.integration.AdditionalEquations`
    
        Class calculating the state transition matrix coefficient for CR3BP Computation.
    
        Since:
            10.2
    
        Also see:
            "Dynamical systems, the three-body problem, and space mission design, Koon, Lo, Marsden, Ross"
    """
    def __init__(self, cR3BPSystem: org.orekit.bodies.CR3BPSystem): ...
    def computeDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Compute the derivatives related to the additional state parameters.
        
            When this method is called, the spacecraft state contains the main state (orbit, attitude and mass), all the states
            provided through the :class:`~org.orekit.propagation.AdditionalStateProvider` registered to the propagator, and the
            additional state integrated using this equation. It does *not* contains any other states to be integrated alongside
            during the same propagation.
        
            Specified by:
                 in interface :class:`~org.orekit.propagation.integration.AdditionalEquations`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional state
                pDot (double[]): placeholder where the derivatives of the additional parameters should be put
        
            Returns:
                cumulative effect of the equations on the main state (may be null if equations do not change main state at all)
        
        
        """
        ...
    def derivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> typing.List[float]:
        """
            Compute the derivatives related to the additional state parameters.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.derivatives`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Parameters:
                s (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                    :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.yield` method)
        
            Returns:
                computed derivatives
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Get the dimension of the generated derivative.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getDimension`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                dimension of the generated
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the additional derivatives (which will become state once integrated).
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getName`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalEquations.getName`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalEquations`
        
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
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the generator at the start of propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalEquations.init`Â in
                interfaceÂ :class:`~org.orekit.propagation.integration.AdditionalEquations`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation
        
        
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


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.numerical.cr3bp")``.

    CR3BPConstants: typing.Type[CR3BPConstants]
    CR3BPForceModel: typing.Type[CR3BPForceModel]
    CR3BPMultipleShooter: typing.Type[CR3BPMultipleShooter]
    STMEquations: typing.Type[STMEquations]
