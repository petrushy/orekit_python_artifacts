
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.orekit.control.indirect.shooting.boundary
import org.orekit.control.indirect.shooting.propagation
import org.orekit.propagation
import typing



class AbstractIndirectShooting:
    """
    public abstract class AbstractIndirectShooting extends :class:`~org.orekit.control.indirect.shooting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Abstract class for indirect shooting methods with numerical propagation.
    
        Since:
            12.2
    """
    DEFAULT_TOLERANCE_MASS_ADJOINT: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_TOLERANCE_MASS_ADJOINT
    
        Default value for convergence tolerance on mass adjoint variable.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def getPropagationSettings(self) -> org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings:
        """
            Getter for the propagation settings.
        
            Returns:
                propagation settings
        
        
        """
        ...
    def solve(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> 'ShootingBoundaryOutput':
        """
            Solve for the boundary conditions, given an initial mass and an initial guess for the adjoint variables.
        
            Parameters:
                initialMass (double): initial mass
                initialGuess (double[]): initial guess
        
            Returns:
                boundary problem solution
        
        
        """
        ...

class ShootingBoundaryOutput:
    """
    public class ShootingBoundaryOutput extends :class:`~org.orekit.control.indirect.shooting.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Data container for two-point boundary output of indirect shooting methods.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.AbstractIndirectShooting`
    """
    def __init__(self, boolean: bool, int: int, spacecraftState: org.orekit.propagation.SpacecraftState, shootingPropagationSettings: org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings, spacecraftState2: org.orekit.propagation.SpacecraftState): ...
    def getInitialState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Getter for the initial state.
        
            Returns:
                initial state
        
        
        """
        ...
    def getIterationCount(self) -> int:
        """
            Getter for the iteration number.
        
            Returns:
                count
        
        
        """
        ...
    def getShootingPropagationSettings(self) -> org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings:
        """
            Getter for the shooting propagation settings.
        
            Returns:
                propagation settings
        
        
        """
        ...
    def getTerminalState(self) -> org.orekit.propagation.SpacecraftState:
        """
            Getter for the terminal state.
        
            Returns:
                terminal state
        
        
        """
        ...
    def isConverged(self) -> bool:
        """
            Getter for convergence flag.
        
            Returns:
                convergence flag
        
        
        """
        ...

class AbstractFixedInitialCartesianSingleShooting(AbstractIndirectShooting):
    """
    public abstract class AbstractFixedInitialCartesianSingleShooting extends :class:`~org.orekit.control.indirect.shooting.AbstractIndirectShooting`
    
        Abstract class for indirect single shooting methods with fixed initial Cartesian state. Inheritors must implement the
        iteration update, assuming derivatives are needed.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`,
            :class:`~org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider`
    """
    def computeCandidateSolution(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int) -> ShootingBoundaryOutput:
        """
            Form solution container with input initial state.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                iterationCount (int): iteration count
        
            Returns:
                candidate solution
        
        
        """
        ...
    def getMaximumIterationCount(self) -> int:
        """
            Returns the maximum number of iterations.
        
            Returns:
                maximum iterations
        
        
        """
        ...
    @typing.overload
    def solve(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> ShootingBoundaryOutput:
        """
            Solve for the boundary conditions, given an initial mass and an initial guess for the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.AbstractIndirectShooting.solve` in
                class :class:`~org.orekit.control.indirect.shooting.AbstractIndirectShooting`
        
            Parameters:
                initialMass (double): initial mass
                initialGuess (double[]): initial guess
        
            Returns:
                boundary problem solution
        
            Solve for the boundary conditions, given an initial mass and an initial guess for the adjoint variables. Uses scales for
            automatic differentiation.
        
            Parameters:
                initialMass (double): initial mass
                initialGuess (double[]): initial guess
                userScales (double[]): scales
        
            Returns:
                boundary problem solution
        
        
        """
        ...
    @typing.overload
    def solve(self, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> ShootingBoundaryOutput: ...

class AbstractFixedBoundaryCartesianSingleShooting(AbstractFixedInitialCartesianSingleShooting):
    """
    public abstract class AbstractFixedBoundaryCartesianSingleShooting extends :class:`~org.orekit.control.indirect.shooting.AbstractFixedInitialCartesianSingleShooting`
    
        Abstract class for indirect single shooting methods with Cartesian coordinates for fixed time fixed boundary. Terminal
        mass is assumed to be free, thus corresponding adjoint must vanish at terminal time. On the other hand, other terminal
        adjoint variables are free because the Cartesian state is fixed.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`,
            :class:`~org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider`
    """
    def computeCandidateSolution(self, spacecraftState: org.orekit.propagation.SpacecraftState, int: int) -> ShootingBoundaryOutput:
        """
            Form solution container with input initial state.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.AbstractFixedInitialCartesianSingleShooting.computeCandidateSolution` in
                class :class:`~org.orekit.control.indirect.shooting.AbstractFixedInitialCartesianSingleShooting`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state
                iterationCount (int): iteration count
        
            Returns:
                candidate solution
        
        
        """
        ...
    def getScalePositionDefects(self) -> float:
        """
            Getter for scale of position defects.
        
            Returns:
                scale
        
        
        """
        ...
    def getScaleVelocityDefects(self) -> float:
        """
            Getter for scale of velocity defects.
        
            Returns:
                scale
        
        
        """
        ...
    def setScalePositionDefects(self, double: float) -> None:
        """
            Setter for scale of position defects.
        
            Parameters:
                scalePositionDefects (double): new scale
        
        
        """
        ...
    def setScaleVelocityDefects(self, double: float) -> None:
        """
            Setter for scale of velocity defects.
        
            Parameters:
                scaleVelocityDefects (double): new scale
        
        
        """
        ...
    def setToleranceMassAdjoint(self, double: float) -> None:
        """
            Setter for mass adjoint tolerance.
        
            Parameters:
                toleranceMassAdjoint (double): new tolerance value
        
        
        """
        ...

class NewtonFixedBoundaryCartesianSingleShooting(AbstractFixedBoundaryCartesianSingleShooting):
    """
    public class NewtonFixedBoundaryCartesianSingleShooting extends :class:`~org.orekit.control.indirect.shooting.AbstractFixedBoundaryCartesianSingleShooting`
    
        Class for indirect single shooting methods with Cartesian coordinates for fixed time fixed boundary. Update is the
        classical Newton-Raphson one. It is computed using an LU matrix decomposition.
    
        Since:
            12.2
    """
    @typing.overload
    def __init__(self, shootingPropagationSettings: org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings, fixedTimeBoundaryOrbits: org.orekit.control.indirect.shooting.boundary.FixedTimeBoundaryOrbits, cartesianBoundaryConditionChecker: org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker): ...
    @typing.overload
    def __init__(self, shootingPropagationSettings: org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings, fixedTimeCartesianBoundaryStates: org.orekit.control.indirect.shooting.boundary.FixedTimeCartesianBoundaryStates, cartesianBoundaryConditionChecker: org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker): ...
    def getMaximumIterationCount(self) -> int:
        """
            Description copied from
            class: :meth:`~org.orekit.control.indirect.shooting.AbstractFixedInitialCartesianSingleShooting.getMaximumIterationCount`
            Returns the maximum number of iterations.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.AbstractFixedInitialCartesianSingleShooting.getMaximumIterationCount` in
                class :class:`~org.orekit.control.indirect.shooting.AbstractFixedInitialCartesianSingleShooting`
        
            Returns:
                maximum iterations
        
        
        """
        ...
    def getSingularityThreshold(self) -> float:
        """
            Getter for singularity threshold in LU decomposition.
        
            Returns:
                threshold
        
            Since:
                13.0
        
        
        """
        ...
    def setSingularityThreshold(self, double: float) -> None:
        """
            Setter for singularity threshold in LU decomposition.
        
            Parameters:
                singularityThreshold (double): new threshold value
        
            Since:
                13.0
        
        
        """
        ...
    def setStepFactor(self, double: float) -> None:
        """
            Setter for the step factor.
        
            Parameters:
                stepFactor (double): new value for the step factor
        
            Since:
                13.0
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.shooting")``.

    AbstractFixedBoundaryCartesianSingleShooting: typing.Type[AbstractFixedBoundaryCartesianSingleShooting]
    AbstractFixedInitialCartesianSingleShooting: typing.Type[AbstractFixedInitialCartesianSingleShooting]
    AbstractIndirectShooting: typing.Type[AbstractIndirectShooting]
    NewtonFixedBoundaryCartesianSingleShooting: typing.Type[NewtonFixedBoundaryCartesianSingleShooting]
    ShootingBoundaryOutput: typing.Type[ShootingBoundaryOutput]
    boundary: org.orekit.control.indirect.shooting.boundary.__module_protocol__
    propagation: org.orekit.control.indirect.shooting.propagation.__module_protocol__
