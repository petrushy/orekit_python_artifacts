
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
    public interface CartesianBoundaryConditionChecker
    
        Interface defining convergence criterion when the terminal condition is on a Cartesian state.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.AbstractFixedBoundaryCartesianSingleShooting`
    """
    def getMaximumIterationCount(self) -> int:
        """
            Returns the maximum number of iterations.
        
            Returns:
                maximum iterations
        
        
        """
        ...
    def isConverged(self, pVCoordinates: org.orekit.utils.PVCoordinates, pVCoordinates2: org.orekit.utils.PVCoordinates) -> bool:
        """
            Asserts convergence.
        
            Parameters:
                targetPV (:class:`~org.orekit.utils.PVCoordinates`): target position-velocity
                actualPV (:class:`~org.orekit.utils.PVCoordinates`): actual position-velocity
        
            Returns:
                convergence flag
        
        
        """
        ...

class FixedTimeBoundaryOrbits:
    """
    public class FixedTimeBoundaryOrbits extends :class:`~org.orekit.control.indirect.shooting.boundary.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Defines two-point boundary values for indirect shooting methods with Cartesian coordinates. This class represents the
        case where the initial and terminal times are fixed as well as the full Cartesian coordinates (position and velocity
        vectors in some frame), using :class:`~org.orekit.orbits.Orbit` as data holder.
    
    
        The terminal condition can be anterior in time to the initial one, it just means that the shooting method will perform
        backward propagation. Also note that any acceleration vector passed in the :class:`~org.orekit.orbits.Orbit` is ignored.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.boundary.FixedTimeCartesianBoundaryStates`
    """
    def __init__(self, orbit: org.orekit.orbits.Orbit, orbit2: org.orekit.orbits.Orbit): ...
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
    public class FixedTimeCartesianBoundaryStates extends :class:`~org.orekit.control.indirect.shooting.boundary.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Defines two-point boundary values for indirect shooting methods with Cartesian coordinates. This class represents the
        case where the initial and terminal times are fixed as well as the full Cartesian coordinates (position and velocity
        vectors in some frame), using :class:`~org.orekit.utils.AbsolutePVCoordinates` as data holder.
    
    
        The terminal condition can be anterior in time to the initial one, it just means that the shooting method will perform
        backward propagation. Also note that any acceleration vector passed in the
        :class:`~org.orekit.utils.AbsolutePVCoordinates` is ignored.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.boundary.FixedTimeBoundaryOrbits`
    """
    def __init__(self, absolutePVCoordinates: org.orekit.utils.AbsolutePVCoordinates, absolutePVCoordinates2: org.orekit.utils.AbsolutePVCoordinates): ...
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
    public class NormBasedCartesianConditionChecker extends :class:`~org.orekit.control.indirect.shooting.boundary.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker`
    
        Class defining convergence criterion on the norm of relative position and velocity vectors, with absolute tolerances.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.AbstractFixedBoundaryCartesianSingleShooting`
    """
    def __init__(self, int: int, double: float, double2: float): ...
    def getMaximumIterationCount(self) -> int:
        """
            Returns the maximum number of iterations.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker.getMaximumIterationCount` in
                interface :class:`~org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker`
        
            Returns:
                maximum iterations
        
        
        """
        ...
    def isConverged(self, pVCoordinates: org.orekit.utils.PVCoordinates, pVCoordinates2: org.orekit.utils.PVCoordinates) -> bool:
        """
            Asserts convergence.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker.isConverged` in
                interface :class:`~org.orekit.control.indirect.shooting.boundary.CartesianBoundaryConditionChecker`
        
            Parameters:
                targetPV (:class:`~org.orekit.utils.PVCoordinates`): target position-velocity
                actualPV (:class:`~org.orekit.utils.PVCoordinates`): actual position-velocity
        
            Returns:
                convergence flag
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.shooting.boundary")``.

    CartesianBoundaryConditionChecker: typing.Type[CartesianBoundaryConditionChecker]
    FixedTimeBoundaryOrbits: typing.Type[FixedTimeBoundaryOrbits]
    FixedTimeCartesianBoundaryStates: typing.Type[FixedTimeCartesianBoundaryStates]
    NormBasedCartesianConditionChecker: typing.Type[NormBasedCartesianConditionChecker]
