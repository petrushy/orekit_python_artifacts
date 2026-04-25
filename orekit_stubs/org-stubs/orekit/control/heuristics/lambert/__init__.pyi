
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.euclidean.twod
import org.hipparchus.linear
import org.orekit.frames
import org.orekit.propagation
import org.orekit.time
import typing



class LambertBoundaryConditions:
    """
    Class holding values defining the boundary conditions to a Lambert arc.
    
    Since:
        13.1
    """
    def __init__(self, initialDate: org.orekit.time.AbsoluteDate, initialPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, terminalDate: org.orekit.time.AbsoluteDate, terminalPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, referenceFrame: org.orekit.frames.Frame):
        """
        Constructor.
        
        Parameters:
            initialDate (AbsoluteDate): initial date
            initialPosition (Vector3D): initial position vector
            terminalDate (AbsoluteDate): terminal date
            terminalPosition (Vector3D): terminal position vector
            referenceFrame (Frame): reference frame
        
        
        """
        ...
    def getInitialDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the initial date.
        
        Returns:
            initial date
        
        
        """
        ...
    def getInitialPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Getter for the initial position vector.
        
        Returns:
            initial position
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for the reference frame.
        
        Returns:
            frame
        
        
        """
        ...
    def getTerminalDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Getter for the terminal date.
        
        Returns:
            terminal date
        
        
        """
        ...
    def getTerminalPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Getter for the terminal position vector.
        
        Returns:
            terminal position
        
        
        """
        ...

class LambertBoundaryVelocities:
    """
    Class holding the two velocity vectors of a Lambert arc.
    
    Since:
        13.1
    """
    def __init__(self, initialVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D, terminalVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Constructor.
        
        Parameters:
            initialVelocity (Vector3D): initial velocity
            terminalVelocity (Vector3D): terminal velocity
        
        
        """
        ...
    def getInitialVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Getter for the initial velocity vector.
        
        Returns:
            initial velocity
        
        
        """
        ...
    def getTerminalVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Getter for the terminal velocity vector.
        
        Returns:
            terminal velocity
        
        
        """
        ...

class LambertDifferentialCorrector:
    """
    Class implementing a differential correction for extended (meaning under arbitrary dynamics) Lambert arc (fixed initial and terminal position vectors with fixed time). Given boundary conditions and a guess, applies Newton-Raphson algorithm to find the solution (initial and terminal velocity vectors) according to the propagator used. The latter must be compatible with resetting the initial state and computing state transition matrices. Note that propagation is not required to be forward in time.
    
    Since:
        13.1
    
    Also see:
        AbstractPropagator,
        LambertBoundaryConditions
    """
    DEFAULT_POSITION_TOLERANCE: typing.ClassVar[float] = ...
    """
    Default value for convergence (on the position vector).
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITER: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations.
    
    Also see:
        constant
    
    
    """
    def __init__(self, lambertBoundaryConditions: LambertBoundaryConditions):
        """
        Constructor.
        
        Parameters:
            lambertBoundaryConditions (LambertBoundaryConditions): boundary conditions
        
        
        """
        ...
    def getCurrentIter(self) -> int:
        """
        Getter for the current iteration number.
        
        Returns:
            iteration number
        
        
        """
        ...
    def getInitialMass(self) -> float:
        """
        Getter for the initial mass.
        
        Returns:
            initial mass
        
        
        """
        ...
    def getLambertBoundaryConditions(self) -> LambertBoundaryConditions:
        """
        Getter for the boundary conditions.
        
        Returns:
            conditions
        
        
        """
        ...
    def getMaxIter(self) -> int:
        """
        Getter for the maximum number of iterations.
        
        Returns:
            maximum iterations
        
        
        """
        ...
    def getPositionTolerance(self) -> float:
        """
        Getter for the position tolerance.
        
        Returns:
            tolerance
        
        
        """
        ...
    def getStmName(self) -> str:
        """
        Getter for the state transition matrix name.
        
        Returns:
            name
        
        
        """
        ...
    def getThresholdMatrixSolver(self) -> float:
        """
        Getter for the threshold used in linear system solving.
        
        Returns:
            threshold
        
        
        """
        ...
    def setInitialMass(self, initialMass: float) -> None:
        """
        Setter for the initial mass.
        
        Parameters:
            initialMass (double): initial mass
        
        
        """
        ...
    def setMaxIter(self, maxIter: int) -> None:
        """
        Setter for the maximum number of iterations.
        
        Parameters:
            maxIter (int): maximum iterations
        
        
        """
        ...
    def setPositionTolerance(self, positionTolerance: float) -> None:
        """
        Setter for the position tolerance.
        
        Parameters:
            positionTolerance (double): tolerance
        
        
        """
        ...
    def setStmName(self, stmName: str) -> None:
        """
        Setter for the state transition matrix name.
        
        Parameters:
            stmName (String): name
        
        
        """
        ...
    def setThresholdMatrixSolver(self, thresholdMatrixSolver: float) -> None:
        """
        Setter for the threshold used in linear system solving.
        
        Parameters:
            thresholdMatrixSolver (double): threshold
        
        
        """
        ...
    def solve(self, propagator: org.orekit.propagation.AbstractPropagator, guessInitialVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D) -> LambertBoundaryVelocities:
        """
        Method applying differential correction on the guess (Newton-Raphson algorithm).
        
        Parameters:
            propagator (AbstractPropagator): propagator to be used for differential corrections
            guessInitialVelocity (Vector3D): guess on the initial velocity vector
        
        Returns:
            boundary velocities (null if not converged)
        
        
        """
        ...

class LambertSolver:
    """
    Lambert solver, assuming Keplerian motion.
    
    An orbit is determined from two position vectors.
    
    References: Battin, R.H., An Introduction to the Mathematics and Methods of Astrodynamics, AIAA Education, 1999. Lancaster, E.R. and Blanchard, R.C., A Unified Form of Lambert’s Theorem, Goddard Space Flight Center, 1968.
    
    Since:
        13.1
    
    Also see:
        LambertBoundaryConditions,
        LambertBoundaryVelocities
    """
    def __init__(self, mu: float):
        """
        Creator.
        
        Parameters:
            mu (double): gravitational constant
        
        
        """
        ...
    def computeJacobian(self, posigrade: bool, nRev: int, boundaryConditions: LambertBoundaryConditions) -> org.hipparchus.linear.RealMatrix:
        """
        Computes the Jacobian matrix of the Lambert solution. The rows represent the initial and terminal velocity vectors. The columns represent the parameters: initial time, initial position, terminal time, terminal velocity.
        
        Reference: Di Lizia, P., Armellin, R., Zazzera, F. B., and Berz, M. High Order Expansion of the Solution of Two-Point Boundary Value Problems using Differential Algebra: Applications to Spacecraft Dynamics.
        
        Parameters:
            posigrade (boolean): direction flag
            nRev (int): number of revolutions
            boundaryConditions (LambertBoundaryConditions): Lambert boundary conditions
        
        Returns:
            Jacobian matrix
        
        
        """
        ...
    def solve(self, posigrade: bool, nRev: int, boundaryConditions: LambertBoundaryConditions) -> LambertBoundaryVelocities:
        """
        Solve for the corresponding velocity vectors given two position vectors and a duration.
        
        The logic for setting posigrade and nRev is that the sweep angle Δυ travelled by the object between t1 and t2 is 2π nRev +1 - α if posigrade is false and 2π nRev + α if posigrade is true, where α is the separation angle between p1 and p2, which is always computed between 0 and π (because in 3D without a normal reference, vector angles cannot go past π).
        
        This implies that posigrade should be set to true if p2 is located in the half orbit starting at p1 and it should be set to false if p2 is located in the half orbit ending at p1, regardless of the number of periods between t1 and t2, and nRev should be set accordingly.
        
        As an example, if t2 is less than half a period after t1, then posigrade should be true and nRev should be 0. If t2 is more than half a period after t1 but less than one period after t1, posigrade should be false and nRev should be 0.
        
        If solving fails completely, null is returned. If only the computation of terminal velocity fails, a partial pair of velocities is returned (with some NaNs).
        
        Parameters:
            posigrade (boolean): flag indicating the direction of motion
            nRev (int): number of revolutions
            boundaryConditions (LambertBoundaryConditions): Lambert problem boundary conditions
        
        Returns:
            boundary velocity vectors
        
        
        """
        ...
    @staticmethod
    def solveNormalized2D(r1: float, r2: float, dth: float, tau: float, mRev: int) -> org.hipparchus.geometry.euclidean.twod.Vector2D:
        """
        Lambert's solver for the historical, planar problem. Assume mu=1.
        
        Parameters:
            r1 (double): radius 1
            r2 (double): radius 2
            dth (double): sweep angle
            tau (double): time of flight
            mRev (int): number of revs
        
        Returns:
            velocity at departure in (T, N) basis. Is Vector2D.NaN if solving fails
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.heuristics.lambert")``.

    LambertBoundaryConditions: typing.Type[LambertBoundaryConditions]
    LambertBoundaryVelocities: typing.Type[LambertBoundaryVelocities]
    LambertDifferentialCorrector: typing.Type[LambertDifferentialCorrector]
    LambertSolver: typing.Type[LambertSolver]
