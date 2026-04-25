
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.control.indirect.adjoint.cost
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.integration
import org.orekit.time
import org.orekit.utils
import typing



class CartesianAdjointDerivativesProvider(org.orekit.propagation.integration.AdditionalDerivativesProvider):
    """
    Class defining the adjoint dynamics, as defined in the Pontryagin Maximum Principle, in the case where Cartesian coordinates in an inertial frame are the dependent variable. The time derivatives of the adjoint variables are obtained by differentiating the so-called Hamiltonian. They depend on the force model and the cost being minimized. For the former, it is the user's responsibility to make sure the provided CartesianAdjointEquationTerm are consistent with the ForceModel. For the latter, the cost function is represented through the interface CartesianCost.
    
    Since:
        12.2
    
    Also see:
        AdditionalDerivativesProvider,
        NumericalPropagator
    """
    def __init__(self, cost: org.orekit.control.indirect.adjoint.cost.CartesianCost, *adjointEquationTerms: 'CartesianAdjointEquationTerm'):
        """
        Constructor.
        
        Parameters:
            cost (CartesianCost): cost function
            adjointEquationTerms (CartesianAdjointEquationTerm...): terms contributing to the adjoint equations. If none, then the propagator should have no forces, not even a Newtonian
                attraction.
        
        
        """
        ...
    def combinedDerivatives(self, state: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.integration.CombinedDerivatives:
        """
        Compute the derivatives related to the additional state (and optionally main state increments).
        
        Specified by: combinedDerivatives in interface AdditionalDerivativesProvider
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def evaluateHamiltonian(self, state: org.orekit.propagation.SpacecraftState) -> float:
        """
        Evaluate the Hamiltonian from Pontryagin's Maximum Principle.
        
        Parameters:
            state (SpacecraftState): state assumed to hold the adjoint variables
        
        Returns:
            Hamiltonian
        
        
        """
        ...
    def getCost(self) -> org.orekit.control.indirect.adjoint.cost.CartesianCost:
        """
        Getter for the cost.
        
        Returns:
            cost
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Getter for the dimension.
        
        Specified by: getDimension in interface AdditionalDerivativesProvider
        
        Returns:
            dimension
        
        
        """
        ...
    def getName(self) -> str:
        """
        Getter for the name.
        
        Specified by: getName in interface AdditionalDerivativesProvider
        
        Returns:
            name
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the generator at the start of propagation.
        
        Specified by: init in interface AdditionalDerivativesProvider
        
        Parameters:
            initialState (SpacecraftState): initial state information at the start of propagation
            target (AbsoluteDate): date of propagation
        
        
        """
        ...

class CartesianAdjointEquationTerm:
    """
    Interface to define terms in the adjoint equations and Hamiltonian for Cartesian coordinates.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointDerivativesProvider,
        FieldCartesianAdjointDerivativesProvider
    """
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldHamiltonianContribution__T], stateVariables: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> _getFieldHamiltonianContribution__T:
        """
        Computes the contribution to the Hamiltonian.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the Hamiltonian
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], stateVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...
    def getHamiltonianContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> float:
        """
        Computes the contribution to the Hamiltonian.
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the Hamiltonian
        
        
        """
        ...
    def getRatesContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...

_FieldCartesianAdjointDerivativesProvider__T = typing.TypeVar('_FieldCartesianAdjointDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianAdjointDerivativesProvider(org.orekit.propagation.integration.FieldAdditionalDerivativesProvider[_FieldCartesianAdjointDerivativesProvider__T], typing.Generic[_FieldCartesianAdjointDerivativesProvider__T]):
    """
    Class defining the Field version of the adjoint dynamics for Cartesian coordinates, as defined in the Pontryagin Maximum Principle.
    
    Since:
        12.2
    
    Also see:
        FieldAdditionalDerivativesProvider,
        FieldNumericalPropagator,
        CartesianAdjointDerivativesProvider
    """
    def __init__(self, cost: org.orekit.control.indirect.adjoint.cost.FieldCartesianCost[_FieldCartesianAdjointDerivativesProvider__T], *adjointEquationTerms: CartesianAdjointEquationTerm):
        """
        Constructor.
        
        Parameters:
            cost (FieldCartesianCost<FieldCartesianAdjointDerivativesProvider> cost): cost function
            adjointEquationTerms (CartesianAdjointEquationTerm...): terms contributing to the adjoint equations
        
        
        """
        ...
    def combinedDerivatives(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldCartesianAdjointDerivativesProvider__T]) -> org.orekit.propagation.integration.FieldCombinedDerivatives[_FieldCartesianAdjointDerivativesProvider__T]:
        """
        Compute the derivatives related to the additional state (and optionally main state increments).
        
        Specified by: combinedDerivatives in interface FieldAdditionalDerivativesProvider
        
        Parameters:
            state (FieldSpacecraftState<FieldCartesianAdjointDerivativesProvider> state): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                yields method)
        
        Returns:
            computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def evaluateHamiltonian(self, state: org.orekit.propagation.FieldSpacecraftState[_FieldCartesianAdjointDerivativesProvider__T]) -> _FieldCartesianAdjointDerivativesProvider__T:
        """
        Evaluate the Hamiltonian from Pontryagin's Maximum Principle.
        
        Parameters:
            state (FieldSpacecraftState<FieldCartesianAdjointDerivativesProvider> state): state assumed to hold the adjoint variables
        
        Returns:
            Hamiltonian
        
        
        """
        ...
    def getCost(self) -> org.orekit.control.indirect.adjoint.cost.FieldCartesianCost[_FieldCartesianAdjointDerivativesProvider__T]:
        """
        Getter for the cost.
        
        Returns:
            cost
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Getter for the dimension.
        
        Specified by: getDimension in interface FieldAdditionalDerivativesProvider
        
        Returns:
            dimension
        
        
        """
        ...
    def getName(self) -> str:
        """
        Getter for the name.
        
        Specified by: getName in interface FieldAdditionalDerivativesProvider
        
        Returns:
            name
        
        
        """
        ...
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_FieldCartesianAdjointDerivativesProvider__T], target: org.orekit.time.FieldAbsoluteDate[_FieldCartesianAdjointDerivativesProvider__T]) -> None:
        """
        Initialize the generator at the start of propagation.
        
        Specified by: init in interface FieldAdditionalDerivativesProvider
        
        Parameters:
            initialState (FieldSpacecraftState<FieldCartesianAdjointDerivativesProvider> initialState): initial state information at the start of propagation
            target (FieldAbsoluteDate<FieldCartesianAdjointDerivativesProvider> target): date of propagation
        
        
        """
        ...

class AbstractCartesianAdjointEquationTerm(CartesianAdjointEquationTerm):
    """
    Abstract class to define terms in the adjoint equations and Hamiltonian for Cartesian coordinates.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointDerivativesProvider,
        FieldCartesianAdjointDerivativesProvider
    """
    def __init__(self): ...
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldHamiltonianContribution__T], stateVariables: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> _getFieldHamiltonianContribution__T:
        """
        Computes the contribution to the Hamiltonian.
        
        Specified by: getFieldHamiltonianContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the Hamiltonian
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], stateVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getFieldRatesContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...
    def getHamiltonianContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> float:
        """
        Computes the contribution to the Hamiltonian.
        
        Specified by: getHamiltonianContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the Hamiltonian
        
        
        """
        ...
    def getRatesContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getRatesContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...

class PythonCartesianAdjointEquationTerm(CartesianAdjointEquationTerm):
    """
    Python implementation of the CartesianAdjointEquationTerm interface. This class is part of the JCC Python interface and exposes all methods natively.
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldHamiltonianContribution__T], stateVariables: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> _getFieldHamiltonianContribution__T:
        """
        Computes the contribution to the Hamiltonian.
        
        Specified by: getFieldHamiltonianContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the Hamiltonian
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], stateVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getFieldRatesContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...
    def getHamiltonianContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> float:
        """
        Computes the contribution to the Hamiltonian.
        
        Specified by: getHamiltonianContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the Hamiltonian
        
        
        """
        ...
    def getRatesContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getRatesContribution in interface CartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
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

class AbstractCartesianAdjointGravitationalTerm(AbstractCartesianAdjointEquationTerm):
    """
    Abstract class for common computations regarding adjoint dynamics and gravity for Cartesian coordinates.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm
    """
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], stateVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getFieldRatesContribution in interface CartesianAdjointEquationTerm
        
        Overrides: getFieldRatesContribution in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Getter for the gravitational constant.
        
        Returns:
            mu
        
        
        """
        ...
    def getRatesContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getRatesContribution in interface CartesianAdjointEquationTerm
        
        Overrides: getRatesContribution in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...

class CartesianAdjointInertialTerm(AbstractCartesianAdjointEquationTerm):
    """
    Class defining inertial forces' contributions in the adjoint equations for Cartesian coordinates. If present, then the propagator should also include inertial forces.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm,
        InertialForces
    """
    def __init__(self, referenceInertialFrame: org.orekit.frames.Frame):
        """
        Constructor.
        
        Parameters:
            referenceInertialFrame (Frame): reference inertial frame
        
        
        """
        ...
    def getAcceleration(self, transform: org.orekit.frames.Transform, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration vector.
        
        Specified by: getAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        public Vector3D getAcceleration (Transform inertialToPropagationFrame, double[] stateVariables)
        
        Evaluates the inertial acceleration vector.
        
        Parameters:
            inertialToPropagationFrame (Transform): transform from inertial to propagation frame
            stateVariables (double[]): state variables
        
        Returns:
            acceleration
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], stateVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getFieldRatesContribution in interface CartesianAdjointEquationTerm
        
        Overrides: getFieldRatesContribution in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...
    def getRatesContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to the rates of the adjoint variables.
        
        Specified by: getRatesContribution in interface CartesianAdjointEquationTerm
        
        Overrides: getRatesContribution in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to the adjoint derivative vector
        
        
        """
        ...
    def getReferenceInertialFrame(self) -> org.orekit.frames.Frame:
        """
        Getter for reference frame.
        
        Returns:
            frame
        
        
        """
        ...

class AbstractCartesianAdjointNewtonianTerm(AbstractCartesianAdjointGravitationalTerm):
    """
    Abstract class for common computations regarding adjoint dynamics and Newtonian gravity for Cartesian coordinates.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm
    """
    ...

class CartesianAdjointJ2Term(AbstractCartesianAdjointGravitationalTerm):
    """
    Class defining a (constant) J2 contributions in the adjoint equations for Cartesian coordinates. If present, then the propagator should also include a constant J2 term (oblateness) of the central body.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm,
        J2OnlyPerturbation
    """
    def __init__(self, mu: float, rEq: float, j2: float, j2Frame: org.orekit.frames.Frame):
        """
        Constructor.
        
        Parameters:
            mu (double): central body gravitational parameter.
            rEq (double): equatorial radius
            j2 (double): J2 coefficient
            j2Frame (Frame): J2 frame
        
        
        """
        ...
    def getAcceleration(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration vector.
        
        Specified by: getAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        
        """
        ...
    _getFieldAcceleration__T = typing.TypeVar('_getFieldAcceleration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldAcceleration(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldAcceleration__T], stateVariables: typing.Union[typing.List[_getFieldAcceleration__T], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldAcceleration__T]:
        """
        Compute the acceleration vector.
        
        Specified by: getFieldAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        
        """
        ...
    def getJ2(self) -> float:
        """
        Getter for J2.
        
        Returns:
            J2 coefficient
        
        
        """
        ...
    def getPositionAdjointContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to position adjoint derivatives.
        
        Specified by: meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointContribution` in class AbstractCartesianAdjointGravitationalTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to position adjoint derivatives
        
        
        """
        ...
    _getPositionAdjointFieldContribution__T = typing.TypeVar('_getPositionAdjointFieldContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPositionAdjointFieldContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getPositionAdjointFieldContribution__T], stateVariables: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getPositionAdjointFieldContribution__T]:
        """
        Computes the contribution to position adjoint derivatives.
        
        Specified by: meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointFieldContribution` in class AbstractCartesianAdjointGravitationalTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to position adjoint derivatives
        
        
        """
        ...
    def getrEq(self) -> float:
        """
        Getter for central body equatorial radius.
        
        Returns:
            equatorial radius
        
        
        """
        ...

class AbstractCartesianAdjointNonCentralBodyTerm(AbstractCartesianAdjointNewtonianTerm):
    """
    Abstract class defining the contributions of a point-mass, single body gravity in the adjoint equations for Cartesian coordinates.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm
    """
    def getPositionAdjointContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to position adjoint derivatives.
        
        Specified by: meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointContribution` in class AbstractCartesianAdjointGravitationalTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to position adjoint derivatives
        
        
        """
        ...
    _getPositionAdjointFieldContribution__T = typing.TypeVar('_getPositionAdjointFieldContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPositionAdjointFieldContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getPositionAdjointFieldContribution__T], stateVariables: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getPositionAdjointFieldContribution__T]:
        """
        Computes the contribution to position adjoint derivatives.
        
        Specified by: meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointFieldContribution` in class AbstractCartesianAdjointGravitationalTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to position adjoint derivatives
        
        
        """
        ...

class CartesianAdjointKeplerianTerm(AbstractCartesianAdjointNewtonianTerm):
    """
    Class defining the Keplerian contributions in the adjoint equations for Cartesian coordinates. If present, then the propagator should also include the Newtonian attraction of a central body.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm,
        NewtonianAttraction
    """
    def __init__(self, mu: float):
        """
        Constructor.
        
        Parameters:
            mu (double): central body gravitational parameter
        
        
        """
        ...
    def getPositionAdjointContribution(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], adjointVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
        Computes the contribution to position adjoint derivatives.
        
        Specified by: meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointContribution` in class AbstractCartesianAdjointGravitationalTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            adjointVariables (double[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to position adjoint derivatives
        
        
        """
        ...
    _getPositionAdjointFieldContribution__T = typing.TypeVar('_getPositionAdjointFieldContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPositionAdjointFieldContribution(self, date: org.orekit.time.FieldAbsoluteDate[_getPositionAdjointFieldContribution__T], stateVariables: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], adjointVariables: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getPositionAdjointFieldContribution__T]:
        """
        Computes the contribution to position adjoint derivatives.
        
        Specified by: meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointFieldContribution` in class AbstractCartesianAdjointGravitationalTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            adjointVariables (T[]): adjoint variables
            frame (Frame): propagation frame
        
        Returns:
            contribution to position adjoint derivatives
        
        
        """
        ...

class CartesianAdjointSingleBodyTerm(AbstractCartesianAdjointNonCentralBodyTerm):
    """
    Class defining the contributions of a point-mass, single body gravity in the adjoint equations for Cartesian coordinates. If present, then the propagator should also include the Newtonian attraction of a body. This is similar to CartesianAdjointKeplerianTerm but with the body not necessarily a central one.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm,
        SingleBodyAbsoluteAttraction
    """
    def __init__(self, mu: float, bodyPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]):
        """
        Constructor.
        
        Parameters:
            mu (double): body gravitational parameter.
            bodyPositionProvider (ExtendedPositionProvider): body position provider
        
        
        """
        ...
    def getAcceleration(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration vector.
        
        Specified by: getAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        
        """
        ...
    _getFieldAcceleration__T = typing.TypeVar('_getFieldAcceleration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldAcceleration(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldAcceleration__T], stateVariables: typing.Union[typing.List[_getFieldAcceleration__T], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldAcceleration__T]:
        """
        Compute the acceleration vector.
        
        Specified by: getFieldAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        
        """
        ...

class CartesianAdjointThirdBodyTerm(AbstractCartesianAdjointNonCentralBodyTerm):
    """
    Class defining the contributions of a point-mass, third body in the adjoint equations for Cartesian coordinates. If present, then the propagator should also include a ThirdBodyAttraction.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointEquationTerm,
        ThirdBodyAttraction
    """
    def __init__(self, mu: float, bodyPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]):
        """
        Constructor.
        
        Parameters:
            mu (double): body gravitational parameter.
            bodyPositionProvider (ExtendedPositionProvider): body position provider
        
        
        """
        ...
    def getAcceleration(self, date: org.orekit.time.AbsoluteDate, stateVariables: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration vector.
        
        Specified by: getAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (AbsoluteDate): date
            stateVariables (double[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        
        """
        ...
    _getFieldAcceleration__T = typing.TypeVar('_getFieldAcceleration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldAcceleration(self, date: org.orekit.time.FieldAbsoluteDate[_getFieldAcceleration__T], stateVariables: typing.Union[typing.List[_getFieldAcceleration__T], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldAcceleration__T]:
        """
        Compute the acceleration vector.
        
        Specified by: getFieldAcceleration in class AbstractCartesianAdjointEquationTerm
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date
            stateVariables (T[]): state variables
            frame (Frame): propagation frame
        
        Returns:
            acceleration vector
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.adjoint")``.

    AbstractCartesianAdjointEquationTerm: typing.Type[AbstractCartesianAdjointEquationTerm]
    AbstractCartesianAdjointGravitationalTerm: typing.Type[AbstractCartesianAdjointGravitationalTerm]
    AbstractCartesianAdjointNewtonianTerm: typing.Type[AbstractCartesianAdjointNewtonianTerm]
    AbstractCartesianAdjointNonCentralBodyTerm: typing.Type[AbstractCartesianAdjointNonCentralBodyTerm]
    CartesianAdjointDerivativesProvider: typing.Type[CartesianAdjointDerivativesProvider]
    CartesianAdjointEquationTerm: typing.Type[CartesianAdjointEquationTerm]
    CartesianAdjointInertialTerm: typing.Type[CartesianAdjointInertialTerm]
    CartesianAdjointJ2Term: typing.Type[CartesianAdjointJ2Term]
    CartesianAdjointKeplerianTerm: typing.Type[CartesianAdjointKeplerianTerm]
    CartesianAdjointSingleBodyTerm: typing.Type[CartesianAdjointSingleBodyTerm]
    CartesianAdjointThirdBodyTerm: typing.Type[CartesianAdjointThirdBodyTerm]
    FieldCartesianAdjointDerivativesProvider: typing.Type[FieldCartesianAdjointDerivativesProvider]
    PythonCartesianAdjointEquationTerm: typing.Type[PythonCartesianAdjointEquationTerm]
    cost: org.orekit.control.indirect.adjoint.cost.__module_protocol__
