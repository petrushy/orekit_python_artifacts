
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
    public class CartesianAdjointDerivativesProvider extends :class:`~org.orekit.control.indirect.adjoint.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
    
        Class defining the adjoint dynamics, as defined in the Pontryagin Maximum Principle, in the case where Cartesian
        coordinates in an inertial frame are the dependent variable. The time derivatives of the adjoint variables are obtained
        by differentiating the so-called Hamiltonian. They depend on the force model and the cost being minimized. For the
        former, it is the user's responsibility to make sure the provided
        :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm` are consistent with the
        :class:`~org.orekit.forces.ForceModel`. For the latter, the cost function is represented through the interface
        :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`,
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`
    """
    def __init__(self, cartesianCost: org.orekit.control.indirect.adjoint.cost.CartesianCost, *cartesianAdjointEquationTerm: 'CartesianAdjointEquationTerm'): ...
    def combinedDerivatives(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> org.orekit.propagation.integration.CombinedDerivatives:
        """
            Compute the derivatives related to the additional state (and optionally main state increments).
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.combinedDerivatives` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude, and additional states this equations depend on (according to the
                    :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.yields` method)
        
            Returns:
                computed combined derivatives, which may include some incremental coupling effect to add to main state derivatives
        
        
        """
        ...
    def evaluateHamiltonian(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float:
        """
            Evaluate the Hamiltonian from Pontryagin's Maximum Principle.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): state assumed to hold the adjoint variables
        
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
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getDimension` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                dimension
        
        
        """
        ...
    def getName(self) -> str:
        """
            Getter for the name.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.getName` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Returns:
                name
        
        
        """
        ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the generator at the start of propagation.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.AdditionalDerivativesProvider.init` in
                interface :class:`~org.orekit.propagation.integration.AdditionalDerivativesProvider`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): initial state information at the start of propagation
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation
        
        
        """
        ...

class CartesianAdjointEquationTerm:
    """
    public interface CartesianAdjointEquationTerm
    
        Interface to define terms in the adjoint equations and Hamiltonian for Cartesian coordinates.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`,
            :class:`~org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider`
    """
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldHamiltonianContribution__T], tArray: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> _getFieldHamiltonianContribution__T:
        """
            Computes the contribution to the Hamiltonian.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the Hamiltonian
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], tArray: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the adjoint derivative vector
        
        
        """
        ...
    def getHamiltonianContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> float:
        """
            Computes the contribution to the Hamiltonian.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the Hamiltonian
        
        
        """
        ...
    def getRatesContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the adjoint derivative vector
        
        
        """
        ...

_FieldCartesianAdjointDerivativesProvider__T = typing.TypeVar('_FieldCartesianAdjointDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianAdjointDerivativesProvider(org.orekit.propagation.integration.FieldAdditionalDerivativesProvider[_FieldCartesianAdjointDerivativesProvider__T], typing.Generic[_FieldCartesianAdjointDerivativesProvider__T]):
    """
    public class FieldCartesianAdjointDerivativesProvider<T extends :class:`~org.orekit.control.indirect.adjoint.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider`<T>
    
        Class defining the Field version of the adjoint dynamics for Cartesian coordinates, as defined in the Pontryagin Maximum
        Principle.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider`,
            :class:`~org.orekit.propagation.numerical.FieldNumericalPropagator`,
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`
    """
    def __init__(self, fieldCartesianCost: org.orekit.control.indirect.adjoint.cost.FieldCartesianCost[_FieldCartesianAdjointDerivativesProvider__T], *cartesianAdjointEquationTerm: CartesianAdjointEquationTerm): ...
    def combinedDerivatives(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldCartesianAdjointDerivativesProvider__T]) -> org.orekit.propagation.integration.FieldCombinedDerivatives[_FieldCartesianAdjointDerivativesProvider__T]: ...
    def evaluateHamiltonian(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldCartesianAdjointDerivativesProvider__T]) -> _FieldCartesianAdjointDerivativesProvider__T: ...
    def getCost(self) -> org.orekit.control.indirect.adjoint.cost.FieldCartesianCost[_FieldCartesianAdjointDerivativesProvider__T]: ...
    def getDimension(self) -> int:
        """
            Getter for the dimension.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider.getDimension` in
                interface :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider`
        
            Returns:
                dimension
        
        
        """
        ...
    def getName(self) -> str:
        """
            Getter for the name.
        
            Specified by:
                :meth:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider.getName` in
                interface :class:`~org.orekit.propagation.integration.FieldAdditionalDerivativesProvider`
        
            Returns:
                name
        
        
        """
        ...
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_FieldCartesianAdjointDerivativesProvider__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldCartesianAdjointDerivativesProvider__T]) -> None: ...

class AbstractCartesianAdjointEquationTerm(CartesianAdjointEquationTerm):
    """
    public abstract class AbstractCartesianAdjointEquationTerm extends :class:`~org.orekit.control.indirect.adjoint.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
    
        Abstract class to define terms in the adjoint equations and Hamiltonian for Cartesian coordinates.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`,
            :class:`~org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider`
    """
    def __init__(self): ...
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldHamiltonianContribution__T], tArray: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getFieldHamiltonianContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> _getFieldHamiltonianContribution__T:
        """
            Computes the contribution to the Hamiltonian.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getFieldHamiltonianContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the Hamiltonian
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], tArray: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getFieldRatesContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the adjoint derivative vector
        
        
        """
        ...
    def getHamiltonianContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> float:
        """
            Computes the contribution to the Hamiltonian.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getHamiltonianContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the Hamiltonian
        
        
        """
        ...
    def getRatesContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getRatesContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the adjoint derivative vector
        
        
        """
        ...

class AbstractCartesianAdjointGravitationalTerm(AbstractCartesianAdjointEquationTerm):
    """
    public abstract class AbstractCartesianAdjointGravitationalTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
    
        Abstract class for common computations regarding adjoint dynamics and gravity for Cartesian coordinates.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
    """
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], tArray: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getFieldRatesContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Overrides:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getFieldRatesContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
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
    def getRatesContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getRatesContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Overrides:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getRatesContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the adjoint derivative vector
        
        
        """
        ...

class CartesianAdjointInertialTerm(AbstractCartesianAdjointEquationTerm):
    """
    public class CartesianAdjointInertialTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
    
        Class defining inertial forces' contributions in the adjoint equations for Cartesian coordinates. If present, then the
        propagator should also include inertial forces.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`,
            :class:`~org.orekit.forces.inertia.InertialForces`
    """
    def __init__(self, frame: org.orekit.frames.Frame): ...
    def getAcceleration(self, transform: org.orekit.frames.Transform, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                acceleration vector
        
            Evaluates the inertial acceleration vector.
        
            Parameters:
                inertialToPropagationFrame (:class:`~org.orekit.frames.Transform`): transform from inertial to propagation frame
                stateVariables (double[]): state variables
        
            Returns:
                acceleration
        
        
        """
        ...
    _getFieldRatesContribution__T = typing.TypeVar('_getFieldRatesContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldRatesContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldRatesContribution__T], tArray: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getFieldRatesContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getFieldRatesContribution__T]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getFieldRatesContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Overrides:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getFieldRatesContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to the adjoint derivative vector
        
        
        """
        ...
    def getRatesContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to the rates of the adjoint variables.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm.getRatesContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
        
            Overrides:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getRatesContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
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
    public abstract class AbstractCartesianAdjointNewtonianTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
    
        Abstract class for common computations regarding adjoint dynamics and Newtonian gravity for Cartesian coordinates.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
    """
    ...

class CartesianAdjointJ2Term(AbstractCartesianAdjointGravitationalTerm):
    """
    public class CartesianAdjointJ2Term extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
    
        Class defining a (constant) J2 contributions in the adjoint equations for Cartesian coordinates. If present, then the
        propagator should also include a constant J2 term (oblateness) of the central body.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`,
            :class:`~org.orekit.forces.gravity.J2OnlyPerturbation`
    """
    def __init__(self, double: float, double2: float, double3: float, frame: org.orekit.frames.Frame): ...
    def getAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                acceleration vector
        
        
        """
        ...
    _getFieldAcceleration__T = typing.TypeVar('_getFieldAcceleration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldAcceleration__T], tArray: typing.Union[typing.List[_getFieldAcceleration__T], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldAcceleration__T]:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getFieldAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
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
    def getPositionAdjointContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to position adjoint derivatives.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to position adjoint derivatives
        
        
        """
        ...
    _getPositionAdjointFieldContribution__T = typing.TypeVar('_getPositionAdjointFieldContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPositionAdjointFieldContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPositionAdjointFieldContribution__T], tArray: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getPositionAdjointFieldContribution__T]:
        """
            Computes the contribution to position adjoint derivatives.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointFieldContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
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
    public abstract class AbstractCartesianAdjointNonCentralBodyTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointNewtonianTerm`
    
        Abstract class defining the contributions of a point-mass, single body gravity in the adjoint equations for Cartesian
        coordinates.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`
    """
    def getPositionAdjointContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to position adjoint derivatives.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to position adjoint derivatives
        
        
        """
        ...
    _getPositionAdjointFieldContribution__T = typing.TypeVar('_getPositionAdjointFieldContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPositionAdjointFieldContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPositionAdjointFieldContribution__T], tArray: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getPositionAdjointFieldContribution__T]:
        """
            Computes the contribution to position adjoint derivatives.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointFieldContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to position adjoint derivatives
        
        
        """
        ...

class CartesianAdjointKeplerianTerm(AbstractCartesianAdjointNewtonianTerm):
    """
    public class CartesianAdjointKeplerianTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointNewtonianTerm`
    
        Class defining the Keplerian contributions in the adjoint equations for Cartesian coordinates. If present, then the
        propagator should also include the Newtonian attraction of a central body.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`,
            :class:`~org.orekit.forces.gravity.NewtonianAttraction`
    """
    def __init__(self, double: float): ...
    def getPositionAdjointContribution(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[float]:
        """
            Computes the contribution to position adjoint derivatives.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                adjointVariables (double[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to position adjoint derivatives
        
        
        """
        ...
    _getPositionAdjointFieldContribution__T = typing.TypeVar('_getPositionAdjointFieldContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getPositionAdjointFieldContribution(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getPositionAdjointFieldContribution__T], tArray: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], tArray2: typing.Union[typing.List[_getPositionAdjointFieldContribution__T], jpype.JArray], frame: org.orekit.frames.Frame) -> typing.MutableSequence[_getPositionAdjointFieldContribution__T]:
        """
            Computes the contribution to position adjoint derivatives.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm.getPositionAdjointFieldContribution` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointGravitationalTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                adjointVariables (T[]): adjoint variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                contribution to position adjoint derivatives
        
        
        """
        ...

class CartesianAdjointSingleBodyTerm(AbstractCartesianAdjointNonCentralBodyTerm):
    """
    public class CartesianAdjointSingleBodyTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointNonCentralBodyTerm`
    
        Class defining the contributions of a point-mass, single body gravity in the adjoint equations for Cartesian
        coordinates. If present, then the propagator should also include the Newtonian attraction of a body. This is similar to
        :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointKeplerianTerm` but with the body not necessarily a central
        one.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`,
            :class:`~org.orekit.forces.gravity.SingleBodyAbsoluteAttraction`
    """
    def __init__(self, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]): ...
    def getAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                acceleration vector
        
        
        """
        ...
    _getFieldAcceleration__T = typing.TypeVar('_getFieldAcceleration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldAcceleration__T], tArray: typing.Union[typing.List[_getFieldAcceleration__T], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldAcceleration__T]:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getFieldAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                acceleration vector
        
        
        """
        ...

class CartesianAdjointThirdBodyTerm(AbstractCartesianAdjointNonCentralBodyTerm):
    """
    public class CartesianAdjointThirdBodyTerm extends :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointNonCentralBodyTerm`
    
        Class defining the contributions of a point-mass, third body in the adjoint equations for Cartesian coordinates. If
        present, then the propagator should also include a :class:`~org.orekit.forces.gravity.ThirdBodyAttraction`.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`,
            :class:`~org.orekit.forces.gravity.ThirdBodyAttraction`
    """
    def __init__(self, double: float, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]): ...
    def getAcceleration(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.Union[typing.List[float], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date
                stateVariables (double[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
            Returns:
                acceleration vector
        
        
        """
        ...
    _getFieldAcceleration__T = typing.TypeVar('_getFieldAcceleration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldAcceleration(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getFieldAcceleration__T], tArray: typing.Union[typing.List[_getFieldAcceleration__T], jpype.JArray], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldAcceleration__T]:
        """
            Compute the acceleration vector.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm.getFieldAcceleration` in
                class :class:`~org.orekit.control.indirect.adjoint.AbstractCartesianAdjointEquationTerm`
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): date
                stateVariables (T[]): state variables
                frame (:class:`~org.orekit.frames.Frame`): propagation frame
        
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
    cost: org.orekit.control.indirect.adjoint.cost.__module_protocol__
