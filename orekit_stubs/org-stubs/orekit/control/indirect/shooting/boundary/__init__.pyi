
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.orbits
import org.orekit.utils
import typing



class CartesianBoundaryConditionChecker:
    """
    Interface defining convergence criterion when the terminal condition is on a Cartesian state.
    
    Since:
        12.2
    
    Also see:
        AbstractFixedBoundaryCartesianSingleShooting
    """
    def getMaximumIterationCount(self) -> int:
        """
        Returns the maximum number of iterations.
        
        Returns:
            maximum iterations
        
        
        """
        ...
    def isConverged(self, targetPV: org.orekit.utils.PVCoordinates, actualPV: org.orekit.utils.PVCoordinates) -> bool:
        """
        Asserts convergence.
        
        Parameters:
            targetPV (PVCoordinates): target position-velocity
            actualPV (PVCoordinates): actual position-velocity
        
        Returns:
            convergence flag
        
        
        """
        ...

class FixedTimeBoundaryOrbits:
    """
    Defines two-point boundary values for indirect shooting methods with Cartesian coordinates. This class represents the case where the initial and terminal times are fixed as well as the full Cartesian coordinates (position and velocity vectors in some frame), using Orbit as data holder.
    
    The terminal condition can be anterior in time to the initial one, it just means that the shooting method will perform backward propagation. Also note that any acceleration vector passed in the Orbit is ignored.
    
    Since:
        12.2
    
    Also see:
        FixedTimeCartesianBoundaryStates
    """
    def __init__(self, initialOrbit: org.orekit.orbits.Orbit, terminalOrbit: org.orekit.orbits.Orbit):
        """
        Constructor.
        
        Parameters:
            initialOrbit (Orbit): initial condition
            terminalOrbit (Orbit): terminal condition
        
        
        """
        ...
    def getInitialOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Getter for the initial condition.
        
        Returns:
            initial condition
        
        
        """
        ...
    def getTerminalOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Getter for the terminal condition.
        
        Returns:
            terminal condition
        
        
        """
        ...

class FixedTimeCartesianBoundaryStates:
    """
    Defines two-point boundary values for indirect shooting methods with Cartesian coordinates. This class represents the case where the initial and terminal times are fixed as well as the full Cartesian coordinates (position and velocity vectors in some frame), using AbsolutePVCoordinates as data holder.
    
    The terminal condition can be anterior in time to the initial one, it just means that the shooting method will perform backward propagation. Also note that any acceleration vector passed in the AbsolutePVCoordinates is ignored.
    
    Since:
        12.2
    
    Also see:
        FixedTimeBoundaryOrbits
    """
    def __init__(self, initialCartesianState: org.orekit.utils.AbsolutePVCoordinates, terminalCartesianState: org.orekit.utils.AbsolutePVCoordinates):
        """
        Constructor.
        
        Parameters:
            initialCartesianState (AbsolutePVCoordinates): initial condition
            terminalCartesianState (AbsolutePVCoordinates): terminal condition
        
        
        """
        ...
    def getInitialCartesianState(self) -> org.orekit.utils.AbsolutePVCoordinates:
        """
        Getter for the initial Cartesian condition.
        
        Returns:
            initial condition
        
        
        """
        ...
    def getTerminalCartesianState(self) -> org.orekit.utils.AbsolutePVCoordinates:
        """
        Getter for the terminal Cartesian condition.
        
        Returns:
            terminal condition
        
        
        """
        ...

class NormBasedCartesianConditionChecker(CartesianBoundaryConditionChecker):
    """
    Class defining convergence criterion on the norm of relative position and velocity vectors, with absolute tolerances.
    
    Since:
        12.2
    
    Also see:
        AbstractFixedBoundaryCartesianSingleShooting
    """
    def __init__(self, maximumIterationCount: int, absoluteToleranceDistance: float, absoluteToleranceSpeed: float):
        """
        Constructor.
        
        Parameters:
            maximumIterationCount (int): maximum iteration count
            absoluteToleranceDistance (double): absolute tolerance on distance
            absoluteToleranceSpeed (double): absolute tolerance on speed
        
        
        """
        ...
    def getMaximumIterationCount(self) -> int:
        """
        Returns the maximum number of iterations.
        
        Specified by: getMaximumIterationCount in interface CartesianBoundaryConditionChecker
        
        Returns:
            maximum iterations
        
        
        """
        ...
    def isConverged(self, targetPV: org.orekit.utils.PVCoordinates, actualPV: org.orekit.utils.PVCoordinates) -> bool:
        """
        Asserts convergence.
        
        Specified by: isConverged in interface CartesianBoundaryConditionChecker
        
        Parameters:
            targetPV (PVCoordinates): target position-velocity
            actualPV (PVCoordinates): actual position-velocity
        
        Returns:
            convergence flag
        
        
        """
        ...

class PythonCartesianBoundaryConditionChecker(CartesianBoundaryConditionChecker):
    """
    Python implementation of the CartesianBoundaryConditionChecker interface. This class is part of the JCC Python interface and exposes all methods natively.
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.control.indirect.shooting.boundary.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getMaximumIterationCount(self) -> int:
        """
        Returns the maximum number of iterations.
        
        Specified by: getMaximumIterationCount in interface CartesianBoundaryConditionChecker
        
        Returns:
            maximum iterations
        
        
        """
        ...
    def isConverged(self, targetPV: org.orekit.utils.PVCoordinates, actualPV: org.orekit.utils.PVCoordinates) -> bool:
        """
        Asserts convergence.
        
        Specified by: isConverged in interface CartesianBoundaryConditionChecker
        
        Parameters:
            targetPV (PVCoordinates): target position-velocity
            actualPV (PVCoordinates): actual position-velocity
        
        Returns:
            convergence flag
        
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.shooting.boundary")``.

    CartesianBoundaryConditionChecker: typing.Type[CartesianBoundaryConditionChecker]
    FixedTimeBoundaryOrbits: typing.Type[FixedTimeBoundaryOrbits]
    FixedTimeCartesianBoundaryStates: typing.Type[FixedTimeCartesianBoundaryStates]
    NormBasedCartesianConditionChecker: typing.Type[NormBasedCartesianConditionChecker]
    PythonCartesianBoundaryConditionChecker: typing.Type[PythonCartesianBoundaryConditionChecker]
