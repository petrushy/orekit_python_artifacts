
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util.stream
import jpype
import org
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.propagation.events
import org.orekit.propagation.events.handlers
import org.orekit.propagation.integration
import typing



class CartesianCost:
    """
    public interface CartesianCost
    
        Interface to definite cost function in the frame of Pontryagin's Maximum Principle using Cartesian coordinates. It
        provides the link between the optimal control and the adjoint variables. This relationship is obtained by maximizing the
        Hamiltonian. The choice of control vector impacts on it. Both standard (double type) and (Calculus)Field versions are to
        be implemented by inheritors.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`
    """
    def getAdjointDimension(self) -> int:
        """
            Getter for adjoint vector dimension.
        
            Returns:
                adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Returns:
                adjoint vector name
        
        
        """
        ...
    def getCostDerivativeProvider(self, string: str) -> org.orekit.propagation.integration.AdditionalDerivativesProvider:
        """
            Get the derivatives provider to be able to integrate the cost function.
        
            Parameters:
                name (:class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of cost as additional state variable
        
            Returns:
                derivatives provider
        
            Since:
                13.0
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> float:
        """
            Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time
            derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
            Returns:
                mass flow rate factor
        
        
        """
        ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

class ControlSwitchDetector(org.orekit.propagation.events.EventDetector):
    """
    public abstract class ControlSwitchDetector extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.EventDetector`
    
        Abstract event detector for singularities in adjoint dynamics.
    
        Since:
            13.0
    """
    def getDetectionSettings(self) -> org.orekit.propagation.events.EventDetectionSettings:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.EventDetector.getDetectionSettings`
            Getter for the settings.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getDetectionSettings` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
            Description copied from interface: :meth:`~org.orekit.propagation.events.EventDetector.getHandler`
            Get the handler.
        
            Specified by:
                :meth:`~org.orekit.propagation.events.EventDetector.getHandler` in
                interface :class:`~org.orekit.propagation.events.EventDetector`
        
            Returns:
                event handler to call at event occurrences
        
        
        """
        ...

_FieldCartesianCost__T = typing.TypeVar('_FieldCartesianCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianCost(typing.Generic[_FieldCartesianCost__T]):
    """
    public interface FieldCartesianCost<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        Interface to definite cost function in the frame of Pontryagin's Maximum Principle using Cartesian coordinates. It
        provides the link between the optimal control and the adjoint variables. This relationship is obtained by maximizing the
        Hamiltonian. The choice of control vector impacts on it.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider`
    """
    def getAdjointDimension(self) -> int:
        """
            Getter for adjoint vector dimension.
        
            Returns:
                adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Returns:
                adjoint vector name
        
        
        """
        ...
    def getCostDerivativeProvider(self, string: str) -> org.orekit.propagation.integration.FieldAdditionalDerivativesProvider[_FieldCartesianCost__T]: ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldCartesianCost__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldCartesianCost__T]]: ...
    def getFieldHamiltonianContribution(self, tArray: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray], t2: _FieldCartesianCost__T) -> _FieldCartesianCost__T:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, tArray: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray], t2: _FieldCartesianCost__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldCartesianCost__T]: ...
    def getMassFlowRateFactor(self) -> _FieldCartesianCost__T:
        """
            Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time
            derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
            Returns:
                mass flow rate factor
        
        
        """
        ...
    def toCartesianCost(self) -> CartesianCost:
        """
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, tArray: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray], t2: _FieldCartesianCost__T, tArray2: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`): mass
                adjointDerivatives (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`[]): derivatives to update
        
        
        """
        ...

_FieldControlSwitchDetector__T = typing.TypeVar('_FieldControlSwitchDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldControlSwitchDetector(org.orekit.propagation.events.FieldEventDetector[_FieldControlSwitchDetector__T], typing.Generic[_FieldControlSwitchDetector__T]):
    """
    public abstract class FieldControlSwitchDetector<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.events.FieldEventDetector`<T>
    
        Abstract event detector for singularities in adjoint dynamics.
    
        Since:
            13.0
    """
    def getDetectionSettings(self) -> org.orekit.propagation.events.FieldEventDetectionSettings[_FieldControlSwitchDetector__T]: ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldControlSwitchDetector__T]: ...

class AbstractCartesianCost(CartesianCost):
    """
    public abstract class AbstractCartesianCost extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    
        Abstract class for cost with Cartesian coordinates.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    """
    def getAdjointDimension(self) -> int:
        """
            Getter for adjoint vector dimension.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.CartesianCost.getAdjointDimension` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
        
            Returns:
                adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.CartesianCost.getAdjointName` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
        
            Returns:
                name
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> float:
        """
            Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time
            derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.CartesianCost.getMassFlowRateFactor` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
        
            Returns:
                mass flow rate factor
        
        
        """
        ...

_FieldAbstractCartesianCost__T = typing.TypeVar('_FieldAbstractCartesianCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractCartesianCost(FieldCartesianCost[_FieldAbstractCartesianCost__T], typing.Generic[_FieldAbstractCartesianCost__T]):
    """
    public abstract class FieldAbstractCartesianCost<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`<T>
    
        Abstract class for cost with Cartesian coordinates.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    """
    def getAdjointDimension(self) -> int:
        """
            Getter for adjoint vector dimension.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getAdjointDimension` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getAdjointName` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                name
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> _FieldAbstractCartesianCost__T:
        """
            Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time
            derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getMassFlowRateFactor` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                mass flow rate factor
        
        
        """
        ...

_FieldUnboundedCartesianEnergyNeglectingMass__T = typing.TypeVar('_FieldUnboundedCartesianEnergyNeglectingMass__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnboundedCartesianEnergyNeglectingMass(FieldCartesianCost[_FieldUnboundedCartesianEnergyNeglectingMass__T], typing.Generic[_FieldUnboundedCartesianEnergyNeglectingMass__T]):
    """
    public class FieldUnboundedCartesianEnergyNeglectingMass<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`<T>
    
        Class for unbounded energy cost with Cartesian coordinates neglecting the mass consumption. Under this assumption, the
        mass is constant and there is no need to consider the corresponding adjoint variable. Here, the control vector is chosen
        as the acceleration given by thrusting, expressed in the propagation frame. This leads to the optimal thrust force being
        equal to the adjoint velocity vector times the mass.
    
        Since:
            13.0
    """
    def __init__(self, string: str, field: org.hipparchus.Field[_FieldUnboundedCartesianEnergyNeglectingMass__T]): ...
    def getAdjointDimension(self) -> int:
        """
            Getter for adjoint vector dimension.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getAdjointDimension` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getAdjointName` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                name
        
        
        """
        ...
    def getFieldHamiltonianContribution(self, tArray: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray], t2: _FieldUnboundedCartesianEnergyNeglectingMass__T) -> _FieldUnboundedCartesianEnergyNeglectingMass__T:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getFieldHamiltonianContribution` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergyNeglectingMass`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergyNeglectingMass`): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, tArray: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray], t2: _FieldUnboundedCartesianEnergyNeglectingMass__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldUnboundedCartesianEnergyNeglectingMass__T]: ...
    def getMassFlowRateFactor(self) -> _FieldUnboundedCartesianEnergyNeglectingMass__T:
        """
            Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time
            derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.getMassFlowRateFactor` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                mass flow rate factor
        
        
        """
        ...
    def toCartesianCost(self) -> 'UnboundedCartesianEnergyNeglectingMass':
        """
            Method returning equivalent in non-Field.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.toCartesianCost` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, tArray: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray], t2: _FieldUnboundedCartesianEnergyNeglectingMass__T, tArray2: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.updateFieldAdjointDerivatives` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost`
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergyNeglectingMass`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergyNeglectingMass`): mass
                adjointDerivatives (:class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergyNeglectingMass`[]): derivatives to update
        
        
        """
        ...

class PythonCartesianCost(CartesianCost):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAdjointDimension(self) -> int: ...
    def getAdjointName(self) -> str: ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float: ...
    def getMassFlowRateFactor(self) -> float: ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...

class CartesianFlightDurationCost(AbstractCartesianCost):
    """
    public class CartesianFlightDurationCost extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianCost`
    
        Class for minimizing the flight duration (a.k.a. time of flight) with Cartesian coordinates. It is the integral over
        time of the constant one. The control is assumed to be bounded. It also assumes that no external acceleration depends on
        mass. If the mass flow rate factor is zero, then there is no adjoint for the mass.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    """
    def __init__(self, string: str, double: float, double2: float): ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getMaximumThrustMagnitude(self) -> float:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

class CartesianFuelCost(AbstractCartesianCost):
    """
    public class CartesianFuelCost extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianCost`
    
        Class for fuel cost with Cartesian coordinates. It is the integral over time of the Euclidean norm of the thrust vector.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    """
    @typing.overload
    def __init__(self, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.EventDetectionSettings:
        """
            Getter for event detection settings.
        
            Returns:
                detection settings.
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getMaximumThrustMagnitude(self) -> float:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

_FieldCartesianFlightDurationCost__T = typing.TypeVar('_FieldCartesianFlightDurationCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianFlightDurationCost(FieldAbstractCartesianCost[_FieldCartesianFlightDurationCost__T], typing.Generic[_FieldCartesianFlightDurationCost__T]):
    """
    public class FieldCartesianFlightDurationCost<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldAbstractCartesianCost`<T>
    
        Class for minimizing the flight duration (a.k.a. time of flight) with Cartesian coordinates. It is the integral over
        time of the constant one. The control is assumed to be bounded. It also assumes that no external acceleration depends on
        mass. If the mass flow rate factor is zero, then there is no adjoint for the mass.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`,
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianFlightDurationCost`
    """
    def __init__(self, string: str, t: _FieldCartesianFlightDurationCost__T, t2: _FieldCartesianFlightDurationCost__T): ...
    def getFieldHamiltonianContribution(self, tArray: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray], t2: _FieldCartesianFlightDurationCost__T) -> _FieldCartesianFlightDurationCost__T:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFlightDurationCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFlightDurationCost`): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, tArray: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray], t2: _FieldCartesianFlightDurationCost__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldCartesianFlightDurationCost__T]: ...
    def getMaximumThrustMagnitude(self) -> _FieldCartesianFlightDurationCost__T:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...
    def toCartesianCost(self) -> CartesianFlightDurationCost:
        """
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, tArray: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray], t2: _FieldCartesianFlightDurationCost__T, tArray2: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFlightDurationCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFlightDurationCost`): mass
                adjointDerivatives (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFlightDurationCost`[]): derivatives to update
        
        
        """
        ...

_FieldCartesianFuelCost__T = typing.TypeVar('_FieldCartesianFuelCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianFuelCost(FieldAbstractCartesianCost[_FieldCartesianFuelCost__T], typing.Generic[_FieldCartesianFuelCost__T]):
    """
    public class FieldCartesianFuelCost<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldAbstractCartesianCost`<T>
    
        Class for fuel cost with Cartesian coordinates. It is the integral over time of the Euclidean norm of the thrust vector.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    """
    @typing.overload
    def __init__(self, string: str, t: _FieldCartesianFuelCost__T, t2: _FieldCartesianFuelCost__T): ...
    @typing.overload
    def __init__(self, string: str, t: _FieldCartesianFuelCost__T, t2: _FieldCartesianFuelCost__T, fieldEventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldCartesianFuelCost__T]): ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.FieldEventDetectionSettings[_FieldCartesianFuelCost__T]: ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldCartesianFuelCost__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldCartesianFuelCost__T]]: ...
    def getFieldHamiltonianContribution(self, tArray: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray], t2: _FieldCartesianFuelCost__T) -> _FieldCartesianFuelCost__T:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFuelCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFuelCost`): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, tArray: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray], t2: _FieldCartesianFuelCost__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldCartesianFuelCost__T]: ...
    def getMaximumThrustMagnitude(self) -> _FieldCartesianFuelCost__T:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...
    def toCartesianCost(self) -> CartesianFuelCost:
        """
            Description copied from interface: :meth:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianCost.toCartesianCost`
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, tArray: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray], t2: _FieldCartesianFuelCost__T, tArray2: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFuelCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFuelCost`): mass
                adjointDerivatives (:class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFuelCost`[]): derivatives to update
        
        
        """
        ...

_FieldPenalizedCartesianFuelCost__T = typing.TypeVar('_FieldPenalizedCartesianFuelCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPenalizedCartesianFuelCost(FieldAbstractCartesianCost[_FieldPenalizedCartesianFuelCost__T], typing.Generic[_FieldPenalizedCartesianFuelCost__T]):
    """
    public abstract class FieldPenalizedCartesianFuelCost<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldAbstractCartesianCost`<T>
    
        Abstract class for fuel cost with a penalty term proportional to a weight parameter epsilon. This is typically used in a
        continuation method, starting from epsilon equal to 1 and going towards 0 where the fuel cost is recovered. The point is
        to enhance convergence. The control vector is the normalized (by the upper bound on magnitude) thrust force in
        propagation frame. See the following reference: BERTRAND, Régis et EPENOY, Richard. New smoothing techniques for
        solving bang–bang optimal control problems—numerical results and statistical interpretation. Optimal Control
        Applications and Methods, 2002, vol. 23, no 4, p. 171-197.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.FieldCartesianFuelCost`,
            :class:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost`
    """
    def evaluateFieldPenaltyFunction(self, t: _FieldPenalizedCartesianFuelCost__T) -> _FieldPenalizedCartesianFuelCost__T:
        """
            Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
            Parameters:
                controlNorm (:class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`): Euclidean norm of control vector
        
            Returns:
                penalty function
        
        
        """
        ...
    def getEpsilon(self) -> _FieldPenalizedCartesianFuelCost__T:
        """
            Getter for the penalty weight epsilon.
        
            Returns:
                epsilon
        
        
        """
        ...
    def getFieldHamiltonianContribution(self, tArray: typing.Union[typing.List[_FieldPenalizedCartesianFuelCost__T], jpype.JArray], t2: _FieldPenalizedCartesianFuelCost__T) -> _FieldPenalizedCartesianFuelCost__T:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getMaximumThrustMagnitude(self) -> _FieldPenalizedCartesianFuelCost__T:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...

class PenalizedCartesianFuelCost(AbstractCartesianCost):
    """
    public abstract class PenalizedCartesianFuelCost extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianCost`
    
        Abstract class for fuel cost with a penalty term proportional to a weight parameter epsilon. This is typically used in a
        continuation method, starting from epsilon equal to 1 and going towards 0 where the fuel cost is recovered. The point is
        to enhance convergence. The control vector is the normalized (by the upper bound on magnitude) thrust force in
        propagation frame. See the following reference: BERTRAND, Régis et EPENOY, Richard. New smoothing techniques for
        solving bang–bang optimal control problems—numerical results and statistical interpretation. Optimal Control
        Applications and Methods, 2002, vol. 23, no 4, p. 171-197.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianFuelCost`
    """
    def evaluatePenaltyFunction(self, double: float) -> float:
        """
            Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
            Parameters:
                controlNorm (double): Euclidean norm of control vector
        
            Returns:
                penalty function
        
        
        """
        ...
    def getEpsilon(self) -> float:
        """
            Getter for the penalty weight epsilon.
        
            Returns:
                epsilon
        
        
        """
        ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getMaximumThrustMagnitude(self) -> float:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...

class PythonAbstractCartesianCost(AbstractCartesianCost):
    def finalize(self) -> None: ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float: ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None: ...

class UnboundedCartesianEnergyNeglectingMass(AbstractCartesianCost):
    """
    public class UnboundedCartesianEnergyNeglectingMass extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianCost`
    
        Class for unbounded energy cost with Cartesian coordinates neglecting the mass consumption. Under this assumption, the
        mass is constant and there is no need to consider the corresponding adjoint variable. Here, the control vector is chosen
        as the acceleration given by thrusting, expressed in the propagation frame. This leads to the optimal thrust force being
        equal to the adjoint velocity vector times the mass.
    
        Since:
            12.2
    """
    def __init__(self, string: str): ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    def getHamiltonianContribution(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> float:
        """
            Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

_FieldLogarithmicBarrierCartesianFuel__T = typing.TypeVar('_FieldLogarithmicBarrierCartesianFuel__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLogarithmicBarrierCartesianFuel(FieldPenalizedCartesianFuelCost[_FieldLogarithmicBarrierCartesianFuel__T], typing.Generic[_FieldLogarithmicBarrierCartesianFuel__T]):
    """
    public class FieldLogarithmicBarrierCartesianFuel<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`<T>
    
        Fuel cost penalized with a logarithmic term, which is a barrier so is not defined for epsilon equal to 0 or 1.
    
        Since:
            13.0
    """
    def __init__(self, string: str, t: _FieldLogarithmicBarrierCartesianFuel__T, t2: _FieldLogarithmicBarrierCartesianFuel__T, t3: _FieldLogarithmicBarrierCartesianFuel__T): ...
    def evaluateFieldPenaltyFunction(self, t: _FieldLogarithmicBarrierCartesianFuel__T) -> _FieldLogarithmicBarrierCartesianFuel__T:
        """
            Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost.evaluateFieldPenaltyFunction` in
                class :class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`
        
            Parameters:
                controlNorm (:class:`~org.orekit.control.indirect.adjoint.cost.FieldLogarithmicBarrierCartesianFuel`): Euclidean norm of control vector
        
            Returns:
                penalty function
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, tArray: typing.Union[typing.List[_FieldLogarithmicBarrierCartesianFuel__T], jpype.JArray], t2: _FieldLogarithmicBarrierCartesianFuel__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldLogarithmicBarrierCartesianFuel__T]: ...
    def toCartesianCost(self) -> 'LogarithmicBarrierCartesianFuel':
        """
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, tArray: typing.Union[typing.List[_FieldLogarithmicBarrierCartesianFuel__T], jpype.JArray], t2: _FieldLogarithmicBarrierCartesianFuel__T, tArray2: typing.Union[typing.List[_FieldLogarithmicBarrierCartesianFuel__T], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldLogarithmicBarrierCartesianFuel`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldLogarithmicBarrierCartesianFuel`): mass
                adjointDerivatives (:class:`~org.orekit.control.indirect.adjoint.cost.FieldLogarithmicBarrierCartesianFuel`[]): derivatives to update
        
        
        """
        ...

_FieldQuadraticPenaltyCartesianFuel__T = typing.TypeVar('_FieldQuadraticPenaltyCartesianFuel__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQuadraticPenaltyCartesianFuel(FieldPenalizedCartesianFuelCost[_FieldQuadraticPenaltyCartesianFuel__T], typing.Generic[_FieldQuadraticPenaltyCartesianFuel__T]):
    """
    public class FieldQuadraticPenaltyCartesianFuel<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`<T>
    
        Fuel cost penalized with a quadratic term. For epsilon equal to 1, one gets the bounded energy cost.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.BoundedCartesianEnergy`
    """
    @typing.overload
    def __init__(self, string: str, t: _FieldQuadraticPenaltyCartesianFuel__T, t2: _FieldQuadraticPenaltyCartesianFuel__T, t3: _FieldQuadraticPenaltyCartesianFuel__T): ...
    @typing.overload
    def __init__(self, string: str, t: _FieldQuadraticPenaltyCartesianFuel__T, t2: _FieldQuadraticPenaltyCartesianFuel__T, t3: _FieldQuadraticPenaltyCartesianFuel__T, fieldEventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldQuadraticPenaltyCartesianFuel__T]): ...
    def evaluateFieldPenaltyFunction(self, t: _FieldQuadraticPenaltyCartesianFuel__T) -> _FieldQuadraticPenaltyCartesianFuel__T:
        """
            Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost.evaluateFieldPenaltyFunction` in
                class :class:`~org.orekit.control.indirect.adjoint.cost.FieldPenalizedCartesianFuelCost`
        
            Parameters:
                controlNorm (:class:`~org.orekit.control.indirect.adjoint.cost.FieldQuadraticPenaltyCartesianFuel`): Euclidean norm of control vector
        
            Returns:
                penalty function
        
        
        """
        ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.FieldEventDetectionSettings[_FieldQuadraticPenaltyCartesianFuel__T]: ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldQuadraticPenaltyCartesianFuel__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldQuadraticPenaltyCartesianFuel__T]]: ...
    def getFieldThrustAccelerationVector(self, tArray: typing.Union[typing.List[_FieldQuadraticPenaltyCartesianFuel__T], jpype.JArray], t2: _FieldQuadraticPenaltyCartesianFuel__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldQuadraticPenaltyCartesianFuel__T]: ...
    def toCartesianCost(self) -> 'QuadraticPenaltyCartesianFuel':
        """
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, tArray: typing.Union[typing.List[_FieldQuadraticPenaltyCartesianFuel__T], jpype.JArray], t2: _FieldQuadraticPenaltyCartesianFuel__T, tArray2: typing.Union[typing.List[_FieldQuadraticPenaltyCartesianFuel__T], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (:class:`~org.orekit.control.indirect.adjoint.cost.FieldQuadraticPenaltyCartesianFuel`[]): adjoint vector
                mass (:class:`~org.orekit.control.indirect.adjoint.cost.FieldQuadraticPenaltyCartesianFuel`): mass
                adjointDerivatives (:class:`~org.orekit.control.indirect.adjoint.cost.FieldQuadraticPenaltyCartesianFuel`[]): derivatives to update
        
        
        """
        ...

class LogarithmicBarrierCartesianFuel(PenalizedCartesianFuelCost):
    """
    public class LogarithmicBarrierCartesianFuel extends :class:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost`
    
        Fuel cost penalized with a logarithmic term, which is a barrier so is not defined for epsilon equal to 0 or 1.
    
        Since:
            13.0
    """
    def __init__(self, string: str, double: float, double2: float, double3: float): ...
    def evaluatePenaltyFunction(self, double: float) -> float:
        """
            Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost.evaluatePenaltyFunction` in
                class :class:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost`
        
            Parameters:
                controlNorm (double): Euclidean norm of control vector
        
            Returns:
                penalty function
        
        
        """
        ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

class QuadraticPenaltyCartesianFuel(PenalizedCartesianFuelCost):
    """
    public class QuadraticPenaltyCartesianFuel extends :class:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost`
    
        Fuel cost penalized with a quadratic term. For epsilon equal to 1, one gets the bounded energy cost.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.BoundedCartesianEnergy`
    """
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, double3: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def evaluatePenaltyFunction(self, double: float) -> float:
        """
            Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost.evaluatePenaltyFunction` in
                class :class:`~org.orekit.control.indirect.adjoint.cost.PenalizedCartesianFuelCost`
        
            Parameters:
                controlNorm (double): Euclidean norm of control vector
        
            Returns:
                penalty function
        
        
        """
        ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.EventDetectionSettings:
        """
            Getter for the event detection settings.
        
            Returns:
                detection settings
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    def getThrustAccelerationVector(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

class BoundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.CartesianEnergyConsideringMass):
    """
    public class BoundedCartesianEnergy extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianCost`
    
        Class for bounded energy cost with Cartesian coordinates. An energy cost is proportional to the integral over time of
        the squared Euclidean norm of the control vector, often scaled with 1/2. This type of cost is not optimal in terms of
        mass consumption, however its solutions showcase a smoother behavior favorable for convergence in shooting techniques.
        Here, the control vector is chosen as the thrust force divided by the maximum thrust magnitude and expressed in the
        propagation frame.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.UnboundedCartesianEnergy`
    """
    @typing.overload
    def __init__(self, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    def getMaximumThrustMagnitude(self) -> float:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
            Since:
                13.0
        
        
        """
        ...

_FieldBoundedCartesianEnergy__T = typing.TypeVar('_FieldBoundedCartesianEnergy__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldBoundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.FieldCartesianEnergyConsideringMass[_FieldBoundedCartesianEnergy__T], typing.Generic[_FieldBoundedCartesianEnergy__T]):
    """
    public class FieldBoundedCartesianEnergy<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldAbstractCartesianCost`<T>
    
        Class for bounded energy cost with Cartesian coordinates. An energy cost is proportional to the integral over time of
        the squared Euclidean norm of the control vector, often scaled with 1/2. This type of cost is not optimal in terms of
        mass consumption, however its solutions showcase a smoother behavior favorable for convergence in shooting techniques.
        Here, the control vector is chosen as the thrust force divided by the maximum thrust magnitude and expressed in the
        propagation frame.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergy`,
            :class:`~org.orekit.control.indirect.adjoint.cost.BoundedCartesianEnergy`
    """
    @typing.overload
    def __init__(self, string: str, t: _FieldBoundedCartesianEnergy__T, t2: _FieldBoundedCartesianEnergy__T): ...
    @typing.overload
    def __init__(self, string: str, t: _FieldBoundedCartesianEnergy__T, t2: _FieldBoundedCartesianEnergy__T, fieldEventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldBoundedCartesianEnergy__T]): ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldBoundedCartesianEnergy__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldBoundedCartesianEnergy__T]]: ...
    def getMaximumThrustMagnitude(self) -> _FieldBoundedCartesianEnergy__T:
        """
            Getter for maximum thrust magnitude.
        
            Returns:
                maximum thrust
        
        
        """
        ...
    def toCartesianCost(self) -> BoundedCartesianEnergy:
        """
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...

_FieldUnboundedCartesianEnergy__T = typing.TypeVar('_FieldUnboundedCartesianEnergy__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnboundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.FieldCartesianEnergyConsideringMass[_FieldUnboundedCartesianEnergy__T], typing.Generic[_FieldUnboundedCartesianEnergy__T]):
    """
    public class FieldUnboundedCartesianEnergy<T extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.control.indirect.adjoint.cost.FieldAbstractCartesianCost`<T>
    
        Class for unbounded energy cost with Cartesian coordinates. Here, the control vector is chosen as the thrust force,
        expressed in the propagation frame. This leads to the optimal thrust being in the same direction as the adjoint
        velocity.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.FieldUnboundedCartesianEnergyNeglectingMass`,
            :class:`~org.orekit.control.indirect.adjoint.cost.UnboundedCartesianEnergy`
    """
    @typing.overload
    def __init__(self, string: str, t: _FieldUnboundedCartesianEnergy__T): ...
    @typing.overload
    def __init__(self, string: str, t: _FieldUnboundedCartesianEnergy__T, fieldEventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldUnboundedCartesianEnergy__T]): ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldUnboundedCartesianEnergy__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldUnboundedCartesianEnergy__T]]: ...
    def toCartesianCost(self) -> 'UnboundedCartesianEnergy':
        """
            Method returning equivalent in non-Field.
        
            Returns:
                cost function for non-Field applications
        
        
        """
        ...

class UnboundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.CartesianEnergyConsideringMass):
    """
    public class UnboundedCartesianEnergy extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianCost`
    
        Class for unbounded energy cost with Cartesian coordinates. Here, the control vector is chosen as the thrust force,
        expressed in the propagation frame. This leads to the optimal thrust being in the same direction as the adjoint
        velocity.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.UnboundedCartesianEnergyNeglectingMass`
    """
    @typing.overload
    def __init__(self, string: str, double: float): ...
    @typing.overload
    def __init__(self, string: str, double: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...

class CartesianEnergyConsideringMass: ...

class FieldCartesianEnergyConsideringMass: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.adjoint.cost")``.

    AbstractCartesianCost: typing.Type[AbstractCartesianCost]
    BoundedCartesianEnergy: typing.Type[BoundedCartesianEnergy]
    CartesianCost: typing.Type[CartesianCost]
    CartesianEnergyConsideringMass: typing.Type[CartesianEnergyConsideringMass]
    CartesianFlightDurationCost: typing.Type[CartesianFlightDurationCost]
    CartesianFuelCost: typing.Type[CartesianFuelCost]
    ControlSwitchDetector: typing.Type[ControlSwitchDetector]
    FieldAbstractCartesianCost: typing.Type[FieldAbstractCartesianCost]
    FieldBoundedCartesianEnergy: typing.Type[FieldBoundedCartesianEnergy]
    FieldCartesianCost: typing.Type[FieldCartesianCost]
    FieldCartesianEnergyConsideringMass: typing.Type[FieldCartesianEnergyConsideringMass]
    FieldCartesianFlightDurationCost: typing.Type[FieldCartesianFlightDurationCost]
    FieldCartesianFuelCost: typing.Type[FieldCartesianFuelCost]
    FieldControlSwitchDetector: typing.Type[FieldControlSwitchDetector]
    FieldLogarithmicBarrierCartesianFuel: typing.Type[FieldLogarithmicBarrierCartesianFuel]
    FieldPenalizedCartesianFuelCost: typing.Type[FieldPenalizedCartesianFuelCost]
    FieldQuadraticPenaltyCartesianFuel: typing.Type[FieldQuadraticPenaltyCartesianFuel]
    FieldUnboundedCartesianEnergy: typing.Type[FieldUnboundedCartesianEnergy]
    FieldUnboundedCartesianEnergyNeglectingMass: typing.Type[FieldUnboundedCartesianEnergyNeglectingMass]
    LogarithmicBarrierCartesianFuel: typing.Type[LogarithmicBarrierCartesianFuel]
    PenalizedCartesianFuelCost: typing.Type[PenalizedCartesianFuelCost]
    PythonAbstractCartesianCost: typing.Type[PythonAbstractCartesianCost]
    PythonCartesianCost: typing.Type[PythonCartesianCost]
    QuadraticPenaltyCartesianFuel: typing.Type[QuadraticPenaltyCartesianFuel]
    UnboundedCartesianEnergy: typing.Type[UnboundedCartesianEnergy]
    UnboundedCartesianEnergyNeglectingMass: typing.Type[UnboundedCartesianEnergyNeglectingMass]
