
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
    Interface to definite cost function in the frame of Pontryagin's Maximum Principle using Cartesian coordinates. It provides the link between the optimal control and the adjoint variables. This relationship is obtained by maximizing the Hamiltonian. The choice of control vector impacts on it. Both standard (double type) and (Calculus)Field versions are to be implemented by inheritors.
    
    Since:
        12.2
    
    Also see:
        CartesianAdjointDerivativesProvider
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
    def getCostDerivativeProvider(self, name: str) -> org.orekit.propagation.integration.AdditionalDerivativesProvider:
        """
        Get the derivatives provider to be able to integrate the cost function.
        
        Parameters:
            name (String): name of cost as additional state variable
        
        Returns:
            derivatives provider
        
        Since:
            13.0
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]:
        """
        Get the detectors needed for propagation.
        
        Returns:
            event detectors
        
        
        """
        ...
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
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
        Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
        Returns:
            mass flow rate factor
        
        
        """
        ...
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    Abstract event detector for singularities in adjoint dynamics.
    
    Since:
        13.0
    """
    def getDetectionSettings(self) -> org.orekit.propagation.events.EventDetectionSettings:
        """
        Description copied from interface: getDetectionSettings Getter for the settings.
        
        Specified by: getDetectionSettings in interface EventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.EventHandler:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface EventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...

_FieldCartesianCost__T = typing.TypeVar('_FieldCartesianCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianCost(typing.Generic[_FieldCartesianCost__T]):
    """
    Interface to definite cost function in the frame of Pontryagin's Maximum Principle using Cartesian coordinates. It provides the link between the optimal control and the adjoint variables. This relationship is obtained by maximizing the Hamiltonian. The choice of control vector impacts on it.
    
    Since:
        13.0
    
    Also see:
        CartesianAdjointDerivativesProvider
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
    def getCostDerivativeProvider(self, name: str) -> org.orekit.propagation.integration.FieldAdditionalDerivativesProvider[_FieldCartesianCost__T]:
        """
        Get the derivatives provider to be able to integrate the cost function.
        
        Parameters:
            name (String): name of cost as additional state variable
        
        Returns:
            derivatives provider
        
        Since:
            13.0
        
        
        """
        ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldCartesianCost__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldCartesianCost__T]]:
        """
        Get the detectors needed for propagation.
        
        Parameters:
            field (Field<FieldCartesianCost> field): field
        
        Returns:
            event detectors
        
        
        """
        ...
    def getFieldHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray], mass: _FieldCartesianCost__T) -> _FieldCartesianCost__T:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Parameters:
            adjointVariables (FieldCartesianCost[]): adjoint vector
            mass (FieldCartesianCost): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray], mass: _FieldCartesianCost__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldCartesianCost__T]:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (FieldCartesianCost[]): adjoint vector
            mass (FieldCartesianCost): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> _FieldCartesianCost__T:
        """
        Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
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
    def updateFieldAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray], mass: _FieldCartesianCost__T, adjointDerivatives: typing.Union[typing.List[_FieldCartesianCost__T], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Parameters:
            adjointVariables (FieldCartesianCost[]): adjoint vector
            mass (FieldCartesianCost): mass
            adjointDerivatives (FieldCartesianCost[]): derivatives to update
        
        
        """
        ...

_FieldControlSwitchDetector__T = typing.TypeVar('_FieldControlSwitchDetector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldControlSwitchDetector(org.orekit.propagation.events.FieldEventDetector[_FieldControlSwitchDetector__T], typing.Generic[_FieldControlSwitchDetector__T]):
    """
    Abstract event detector for singularities in adjoint dynamics.
    
    Since:
        13.0
    """
    def getDetectionSettings(self) -> org.orekit.propagation.events.FieldEventDetectionSettings[_FieldControlSwitchDetector__T]:
        """
        Description copied from interface: getDetectionSettings Getter for the settings.
        
        Specified by: getDetectionSettings in interface FieldEventDetector
        
        Returns:
            detection settings
        
        
        """
        ...
    def getHandler(self) -> org.orekit.propagation.events.handlers.FieldEventHandler[_FieldControlSwitchDetector__T]:
        """
        Description copied from interface: getHandler Get the handler.
        
        Specified by: getHandler in interface FieldEventDetector
        
        Returns:
            event handler to call at event occurrences
        
        
        """
        ...

class AbstractCartesianCost(CartesianCost):
    """
    Abstract class for cost with Cartesian coordinates.
    
    Since:
        13.0
    
    Also see:
        CartesianCost
    """
    def getAdjointDimension(self) -> int:
        """
        Getter for adjoint vector dimension.
        
        Specified by: getAdjointDimension in interface CartesianCost
        
        Returns:
            adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
        Getter for adjoint vector name.
        
        Specified by: getAdjointName in interface CartesianCost
        
        Returns:
            name
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> float:
        """
        Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
        Specified by: getMassFlowRateFactor in interface CartesianCost
        
        Returns:
            mass flow rate factor
        
        
        """
        ...

_FieldAbstractCartesianCost__T = typing.TypeVar('_FieldAbstractCartesianCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractCartesianCost(FieldCartesianCost[_FieldAbstractCartesianCost__T], typing.Generic[_FieldAbstractCartesianCost__T]):
    """
    Abstract class for cost with Cartesian coordinates.
    
    Since:
        13.0
    
    Also see:
        CartesianCost
    """
    def getAdjointDimension(self) -> int:
        """
        Getter for adjoint vector dimension.
        
        Specified by: getAdjointDimension in interface FieldCartesianCost
        
        Returns:
            adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
        Getter for adjoint vector name.
        
        Specified by: getAdjointName in interface FieldCartesianCost
        
        Returns:
            name
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> _FieldAbstractCartesianCost__T:
        """
        Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
        Specified by: getMassFlowRateFactor in interface FieldCartesianCost
        
        Returns:
            mass flow rate factor
        
        
        """
        ...

_FieldUnboundedCartesianEnergyNeglectingMass__T = typing.TypeVar('_FieldUnboundedCartesianEnergyNeglectingMass__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnboundedCartesianEnergyNeglectingMass(FieldCartesianCost[_FieldUnboundedCartesianEnergyNeglectingMass__T], typing.Generic[_FieldUnboundedCartesianEnergyNeglectingMass__T]):
    """
    Class for unbounded energy cost with Cartesian coordinates neglecting the mass consumption. Under this assumption, the mass is constant and there is no need to consider the corresponding adjoint variable. Here, the control vector is chosen as the acceleration given by thrusting, expressed in the propagation frame. This leads to the optimal thrust force being equal to the adjoint velocity vector times the mass.
    
    Since:
        13.0
    """
    def __init__(self, name: str, field: org.hipparchus.Field[_FieldUnboundedCartesianEnergyNeglectingMass__T]):
        """
        Constructor.
        
        Parameters:
            name (String): name
            field (Field<FieldUnboundedCartesianEnergyNeglectingMass> field): field
        
        
        """
        ...
    def getAdjointDimension(self) -> int:
        """
        Getter for adjoint vector dimension.
        
        Specified by: getAdjointDimension in interface FieldCartesianCost
        
        Returns:
            adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
        Getter for adjoint vector name.
        
        Specified by: getAdjointName in interface FieldCartesianCost
        
        Returns:
            name
        
        
        """
        ...
    def getFieldHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray], mass: _FieldUnboundedCartesianEnergyNeglectingMass__T) -> _FieldUnboundedCartesianEnergyNeglectingMass__T:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Specified by: getFieldHamiltonianContribution in interface FieldCartesianCost
        
        Parameters:
            adjointVariables (FieldUnboundedCartesianEnergyNeglectingMass[]): adjoint vector
            mass (FieldUnboundedCartesianEnergyNeglectingMass): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray], mass: _FieldUnboundedCartesianEnergyNeglectingMass__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldUnboundedCartesianEnergyNeglectingMass__T]:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Specified by: getFieldThrustAccelerationVector in interface FieldCartesianCost
        
        Parameters:
            adjointVariables (FieldUnboundedCartesianEnergyNeglectingMass[]): adjoint vector
            mass (FieldUnboundedCartesianEnergyNeglectingMass): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> _FieldUnboundedCartesianEnergyNeglectingMass__T:
        """
        Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
        Specified by: getMassFlowRateFactor in interface FieldCartesianCost
        
        Returns:
            mass flow rate factor
        
        
        """
        ...
    def toCartesianCost(self) -> 'UnboundedCartesianEnergyNeglectingMass':
        """
        Method returning equivalent in non-Field.
        
        Specified by: toCartesianCost in interface FieldCartesianCost
        
        Returns:
            cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray], mass: _FieldUnboundedCartesianEnergyNeglectingMass__T, adjointDerivatives: typing.Union[typing.List[_FieldUnboundedCartesianEnergyNeglectingMass__T], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Specified by: updateFieldAdjointDerivatives in interface FieldCartesianCost
        
        Parameters:
            adjointVariables (FieldUnboundedCartesianEnergyNeglectingMass[]): adjoint vector
            mass (FieldUnboundedCartesianEnergyNeglectingMass): mass
            adjointDerivatives (FieldUnboundedCartesianEnergyNeglectingMass[]): derivatives to update
        
        
        """
        ...

class PythonCartesianCost(CartesianCost):
    """
    Python implementation of the CartesianCost interface. This class is part of the JCC Python interface and exposes all methods natively.
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
    def getAdjointDimension(self) -> int:
        """
        Getter for adjoint vector dimension.
        
        Specified by: getAdjointDimension in interface CartesianCost
        
        Returns:
            adjoint dimension
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
        Getter for adjoint vector name.
        
        Specified by: getAdjointName in interface CartesianCost
        
        Returns:
            adjoint vector name
        
        
        """
        ...
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Specified by: getHamiltonianContribution in interface CartesianCost
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getMassFlowRateFactor(self) -> float:
        """
        Getter for mass flow rate factor. It is negated and multiplied by the thrust force magnitude to obtain the mass time derivative. The fact that it is a constant means that the exhaust speed is assumed to be independent of time.
        
        Specified by: getMassFlowRateFactor in interface CartesianCost
        
        Returns:
            mass flow rate factor
        
        
        """
        ...
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Specified by: getThrustAccelerationVector in interface CartesianCost
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Specified by: updateAdjointDerivatives in interface CartesianCost
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
            adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

class CartesianFlightDurationCost(AbstractCartesianCost):
    """
    Class for minimizing the flight duration (a.k.a. time of flight) with Cartesian coordinates. It is the integral over time of the constant one. The control is assumed to be bounded. It also assumes that no external acceleration depends on mass. If the mass flow rate factor is zero, then there is no adjoint for the mass.
    
    Since:
        13.0
    
    Also see:
        CartesianCost
    """
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float):
        """
        Constructor.
        
        Parameters:
            name (String): name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
        
        
        """
        ...
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
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
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    Class for fuel cost with Cartesian coordinates. It is the integral over time of the Euclidean norm of the thrust vector.
    
    Since:
        13.0
    
    Also see:
        CartesianCost
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.EventDetectionSettings:
        """
        Getter for event detection settings.
        
        Returns:
            detection settings.
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]:
        """
        Get the detectors needed for propagation.
        
        Returns:
            event detectors
        
        
        """
        ...
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
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
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    Class for minimizing the flight duration (a.k.a. time of flight) with Cartesian coordinates. It is the integral over time of the constant one. The control is assumed to be bounded. It also assumes that no external acceleration depends on mass. If the mass flow rate factor is zero, then there is no adjoint for the mass.
    
    Since:
        13.0
    
    Also see:
        CartesianCost,
        CartesianFlightDurationCost
    """
    def __init__(self, name: str, massFlowRateFactor: _FieldCartesianFlightDurationCost__T, maximumThrustMagnitude: _FieldCartesianFlightDurationCost__T):
        """
        Constructor.
        
        Parameters:
            name (String): name
            massFlowRateFactor (FieldCartesianFlightDurationCost): mass flow rate factor
            maximumThrustMagnitude (FieldCartesianFlightDurationCost): maximum thrust magnitude
        
        
        """
        ...
    def getFieldHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray], mass: _FieldCartesianFlightDurationCost__T) -> _FieldCartesianFlightDurationCost__T:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Parameters:
            adjointVariables (FieldCartesianFlightDurationCost[]): adjoint vector
            mass (FieldCartesianFlightDurationCost): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray], mass: _FieldCartesianFlightDurationCost__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldCartesianFlightDurationCost__T]:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (FieldCartesianFlightDurationCost[]): adjoint vector
            mass (FieldCartesianFlightDurationCost): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
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
    def updateFieldAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray], mass: _FieldCartesianFlightDurationCost__T, adjointDerivatives: typing.Union[typing.List[_FieldCartesianFlightDurationCost__T], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Parameters:
            adjointVariables (FieldCartesianFlightDurationCost[]): adjoint vector
            mass (FieldCartesianFlightDurationCost): mass
            adjointDerivatives (FieldCartesianFlightDurationCost[]): derivatives to update
        
        
        """
        ...

_FieldCartesianFuelCost__T = typing.TypeVar('_FieldCartesianFuelCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCartesianFuelCost(FieldAbstractCartesianCost[_FieldCartesianFuelCost__T], typing.Generic[_FieldCartesianFuelCost__T]):
    """
    Class for fuel cost with Cartesian coordinates. It is the integral over time of the Euclidean norm of the thrust vector.
    
    Since:
        13.0
    
    Also see:
        CartesianCost
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldCartesianFuelCost__T, maximumThrustMagnitude: _FieldCartesianFuelCost__T): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldCartesianFuelCost__T, maximumThrustMagnitude: _FieldCartesianFuelCost__T, eventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldCartesianFuelCost__T]): ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.FieldEventDetectionSettings[_FieldCartesianFuelCost__T]:
        """
        Getter for event detection settings.
        
        Returns:
            detection settings.
        
        
        """
        ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldCartesianFuelCost__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldCartesianFuelCost__T]]:
        """
        Get the detectors needed for propagation.
        
        Parameters:
            field (Field<FieldCartesianFuelCost> field): field
        
        Returns:
            event detectors
        
        
        """
        ...
    def getFieldHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray], mass: _FieldCartesianFuelCost__T) -> _FieldCartesianFuelCost__T:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Parameters:
            adjointVariables (FieldCartesianFuelCost[]): adjoint vector
            mass (FieldCartesianFuelCost): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray], mass: _FieldCartesianFuelCost__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldCartesianFuelCost__T]:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (FieldCartesianFuelCost[]): adjoint vector
            mass (FieldCartesianFuelCost): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def getMaximumThrustMagnitude(self) -> _FieldCartesianFuelCost__T:
        """
        Getter for maximum thrust magnitude.
        
        Returns:
            maximum thrust
        
        
        """
        ...
    def toCartesianCost(self) -> CartesianFuelCost:
        """
        Description copied from interface: toCartesianCost Method returning equivalent in non-Field.
        
        Returns:
            cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray], mass: _FieldCartesianFuelCost__T, adjointDerivatives: typing.Union[typing.List[_FieldCartesianFuelCost__T], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Parameters:
            adjointVariables (FieldCartesianFuelCost[]): adjoint vector
            mass (FieldCartesianFuelCost): mass
            adjointDerivatives (FieldCartesianFuelCost[]): derivatives to update
        
        
        """
        ...

_FieldPenalizedCartesianFuelCost__T = typing.TypeVar('_FieldPenalizedCartesianFuelCost__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPenalizedCartesianFuelCost(FieldAbstractCartesianCost[_FieldPenalizedCartesianFuelCost__T], typing.Generic[_FieldPenalizedCartesianFuelCost__T]):
    """
    Abstract class for fuel cost with a penalty term proportional to a weight parameter epsilon. This is typically used in a continuation method, starting from epsilon equal to 1 and going towards 0 where the fuel cost is recovered. The point is to enhance convergence. The control vector is the normalized (by the upper bound on magnitude) thrust force in propagation frame. See the following reference: BERTRAND, Régis et EPENOY, Richard. New smoothing techniques for solving bang–bang optimal control problems—numerical results and statistical interpretation. Optimal Control Applications and Methods, 2002, vol. 23, no 4, p. 171-197.
    
    Since:
        13.0
    
    Also see:
        FieldCartesianFuelCost,
        PenalizedCartesianFuelCost
    """
    def evaluateFieldPenaltyFunction(self, controlNorm: _FieldPenalizedCartesianFuelCost__T) -> _FieldPenalizedCartesianFuelCost__T:
        """
        Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
        Parameters:
            controlNorm (FieldPenalizedCartesianFuelCost): Euclidean norm of control vector
        
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
    def getFieldHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[_FieldPenalizedCartesianFuelCost__T], jpype.JArray], mass: _FieldPenalizedCartesianFuelCost__T) -> _FieldPenalizedCartesianFuelCost__T:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Parameters:
            adjointVariables (FieldPenalizedCartesianFuelCost[]): adjoint vector
            mass (FieldPenalizedCartesianFuelCost): mass
        
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
    Abstract class for fuel cost with a penalty term proportional to a weight parameter epsilon. This is typically used in a continuation method, starting from epsilon equal to 1 and going towards 0 where the fuel cost is recovered. The point is to enhance convergence. The control vector is the normalized (by the upper bound on magnitude) thrust force in propagation frame. See the following reference: BERTRAND, Régis et EPENOY, Richard. New smoothing techniques for solving bang–bang optimal control problems—numerical results and statistical interpretation. Optimal Control Applications and Methods, 2002, vol. 23, no 4, p. 171-197.
    
    Since:
        13.0
    
    Also see:
        CartesianFuelCost
    """
    def evaluatePenaltyFunction(self, controlNorm: float) -> float:
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
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
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
    """
    Python implementation of the AbstractCartesianCost class. This class is part of the JCC Python interface and exposes abstract methods natively.
    """
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
            adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...

class UnboundedCartesianEnergyNeglectingMass(AbstractCartesianCost):
    """
    Class for unbounded energy cost with Cartesian coordinates neglecting the mass consumption. Under this assumption, the mass is constant and there is no need to consider the corresponding adjoint variable. Here, the control vector is chosen as the acceleration given by thrusting, expressed in the propagation frame. This leads to the optimal thrust force being equal to the adjoint velocity vector times the mass.
    
    Since:
        12.2
    """
    def __init__(self, name: str):
        """
        Constructor.
        
        Parameters:
            name (String): name
        
        
        """
        ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]:
        """
        Get the detectors needed for propagation.
        
        Returns:
            event detectors
        
        
        """
        ...
    def getHamiltonianContribution(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> float:
        """
        Computes the Hamiltonian contribution to the cost function. It equals the Lagrange-form integrand multiplied by -1.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            contribution to Hamiltonian
        
        
        """
        ...
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    Fuel cost penalized with a logarithmic term, which is a barrier so is not defined for epsilon equal to 0 or 1.
    
    Since:
        13.0
    """
    def __init__(self, name: str, massFlowRateFactor: _FieldLogarithmicBarrierCartesianFuel__T, maximumThrustMagnitude: _FieldLogarithmicBarrierCartesianFuel__T, epsilon: _FieldLogarithmicBarrierCartesianFuel__T):
        """
        Constructor.
        
        Parameters:
            name (String): adjoint name
            massFlowRateFactor (FieldLogarithmicBarrierCartesianFuel): mass flow rate factor
            maximumThrustMagnitude (FieldLogarithmicBarrierCartesianFuel): maximum thrust magnitude
            epsilon (FieldLogarithmicBarrierCartesianFuel): penalty weight
        
        
        """
        ...
    def evaluateFieldPenaltyFunction(self, controlNorm: _FieldLogarithmicBarrierCartesianFuel__T) -> _FieldLogarithmicBarrierCartesianFuel__T:
        """
        Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
        Specified by: evaluateFieldPenaltyFunction in class FieldPenalizedCartesianFuelCost
        
        Parameters:
            controlNorm (FieldLogarithmicBarrierCartesianFuel): Euclidean norm of control vector
        
        Returns:
            penalty function
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[_FieldLogarithmicBarrierCartesianFuel__T], jpype.JArray], mass: _FieldLogarithmicBarrierCartesianFuel__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldLogarithmicBarrierCartesianFuel__T]:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (FieldLogarithmicBarrierCartesianFuel[]): adjoint vector
            mass (FieldLogarithmicBarrierCartesianFuel): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def toCartesianCost(self) -> 'LogarithmicBarrierCartesianFuel':
        """
        Method returning equivalent in non-Field.
        
        Returns:
            cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[_FieldLogarithmicBarrierCartesianFuel__T], jpype.JArray], mass: _FieldLogarithmicBarrierCartesianFuel__T, adjointDerivatives: typing.Union[typing.List[_FieldLogarithmicBarrierCartesianFuel__T], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Parameters:
            adjointVariables (FieldLogarithmicBarrierCartesianFuel[]): adjoint vector
            mass (FieldLogarithmicBarrierCartesianFuel): mass
            adjointDerivatives (FieldLogarithmicBarrierCartesianFuel[]): derivatives to update
        
        
        """
        ...

_FieldQuadraticPenaltyCartesianFuel__T = typing.TypeVar('_FieldQuadraticPenaltyCartesianFuel__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQuadraticPenaltyCartesianFuel(FieldPenalizedCartesianFuelCost[_FieldQuadraticPenaltyCartesianFuel__T], typing.Generic[_FieldQuadraticPenaltyCartesianFuel__T]):
    """
    Fuel cost penalized with a quadratic term. For epsilon equal to 1, one gets the bounded energy cost.
    
    Since:
        13.0
    
    Also see:
        BoundedCartesianEnergy
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldQuadraticPenaltyCartesianFuel__T, maximumThrustMagnitude: _FieldQuadraticPenaltyCartesianFuel__T, epsilon: _FieldQuadraticPenaltyCartesianFuel__T): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldQuadraticPenaltyCartesianFuel__T, maximumThrustMagnitude: _FieldQuadraticPenaltyCartesianFuel__T, epsilon: _FieldQuadraticPenaltyCartesianFuel__T, eventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldQuadraticPenaltyCartesianFuel__T]): ...
    def evaluateFieldPenaltyFunction(self, controlNorm: _FieldQuadraticPenaltyCartesianFuel__T) -> _FieldQuadraticPenaltyCartesianFuel__T:
        """
        Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
        Specified by: evaluateFieldPenaltyFunction in class FieldPenalizedCartesianFuelCost
        
        Parameters:
            controlNorm (FieldQuadraticPenaltyCartesianFuel): Euclidean norm of control vector
        
        Returns:
            penalty function
        
        
        """
        ...
    def getEventDetectionSettings(self) -> org.orekit.propagation.events.FieldEventDetectionSettings[_FieldQuadraticPenaltyCartesianFuel__T]:
        """
        Getter for the event detection settings.
        
        Returns:
            detection settings
        
        
        """
        ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldQuadraticPenaltyCartesianFuel__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldQuadraticPenaltyCartesianFuel__T]]:
        """
        Get the detectors needed for propagation.
        
        Parameters:
            field (Field<FieldQuadraticPenaltyCartesianFuel> field): field
        
        Returns:
            event detectors
        
        
        """
        ...
    def getFieldThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[_FieldQuadraticPenaltyCartesianFuel__T], jpype.JArray], mass: _FieldQuadraticPenaltyCartesianFuel__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldQuadraticPenaltyCartesianFuel__T]:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (FieldQuadraticPenaltyCartesianFuel[]): adjoint vector
            mass (FieldQuadraticPenaltyCartesianFuel): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def toCartesianCost(self) -> 'QuadraticPenaltyCartesianFuel':
        """
        Method returning equivalent in non-Field.
        
        Returns:
            cost function for non-Field applications
        
        
        """
        ...
    def updateFieldAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[_FieldQuadraticPenaltyCartesianFuel__T], jpype.JArray], mass: _FieldQuadraticPenaltyCartesianFuel__T, adjointDerivatives: typing.Union[typing.List[_FieldQuadraticPenaltyCartesianFuel__T], jpype.JArray]) -> None:
        """
        Update the adjoint derivatives if necessary.
        
        Parameters:
            adjointVariables (FieldQuadraticPenaltyCartesianFuel[]): adjoint vector
            mass (FieldQuadraticPenaltyCartesianFuel): mass
            adjointDerivatives (FieldQuadraticPenaltyCartesianFuel[]): derivatives to update
        
        
        """
        ...

class LogarithmicBarrierCartesianFuel(PenalizedCartesianFuelCost):
    """
    Fuel cost penalized with a logarithmic term, which is a barrier so is not defined for epsilon equal to 0 or 1.
    
    Since:
        13.0
    """
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float, epsilon: float):
        """
        Constructor.
        
        Parameters:
            name (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
            epsilon (double): penalty weight
        
        
        """
        ...
    def evaluatePenaltyFunction(self, controlNorm: float) -> float:
        """
        Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
        Specified by: evaluatePenaltyFunction in class PenalizedCartesianFuelCost
        
        Parameters:
            controlNorm (double): Euclidean norm of control vector
        
        Returns:
            penalty function
        
        
        """
        ...
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    Fuel cost penalized with a quadratic term. For epsilon equal to 1, one gets the bounded energy cost.
    
    Since:
        13.0
    
    Also see:
        BoundedCartesianEnergy
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float, epsilon: float): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float, epsilon: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def evaluatePenaltyFunction(self, controlNorm: float) -> float:
        """
        Evaluate the penalty term (without the weight), assumed to be a function of the control norm.
        
        Specified by: evaluatePenaltyFunction in class PenalizedCartesianFuelCost
        
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
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]:
        """
        Get the detectors needed for propagation.
        
        Returns:
            event detectors
        
        
        """
        ...
    def getThrustAccelerationVector(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
        Parameters:
            adjointVariables (double[]): adjoint vector
            mass (double): mass
        
        Returns:
            thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, adjointVariables: typing.Union[typing.List[float], jpype.JArray], mass: float, adjointDerivatives: typing.Union[typing.List[float], jpype.JArray]) -> None:
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
    Class for bounded energy cost with Cartesian coordinates. An energy cost is proportional to the integral over time of the squared Euclidean norm of the control vector, often scaled with 1/2. This type of cost is not optimal in terms of mass consumption, however its solutions showcase a smoother behavior favorable for convergence in shooting techniques. Here, the control vector is chosen as the thrust force divided by the maximum thrust magnitude and expressed in the propagation frame.
    
    Since:
        12.2
    
    Also see:
        UnboundedCartesianEnergy
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, maximumThrustMagnitude: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]:
        """
        Get the detectors needed for propagation.
        
        Returns:
            event detectors
        
        
        """
        ...
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
    Class for bounded energy cost with Cartesian coordinates. An energy cost is proportional to the integral over time of the squared Euclidean norm of the control vector, often scaled with 1/2. This type of cost is not optimal in terms of mass consumption, however its solutions showcase a smoother behavior favorable for convergence in shooting techniques. Here, the control vector is chosen as the thrust force divided by the maximum thrust magnitude and expressed in the propagation frame.
    
    Since:
        13.0
    
    Also see:
        FieldUnboundedCartesianEnergy,
        BoundedCartesianEnergy
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldBoundedCartesianEnergy__T, maximumThrustMagnitude: _FieldBoundedCartesianEnergy__T): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldBoundedCartesianEnergy__T, maximumThrustMagnitude: _FieldBoundedCartesianEnergy__T, eventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldBoundedCartesianEnergy__T]): ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldBoundedCartesianEnergy__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldBoundedCartesianEnergy__T]]:
        """
        Get the detectors needed for propagation.
        
        Parameters:
            field (Field<FieldBoundedCartesianEnergy> field): field
        
        Returns:
            event detectors
        
        
        """
        ...
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
    Class for unbounded energy cost with Cartesian coordinates. Here, the control vector is chosen as the thrust force, expressed in the propagation frame. This leads to the optimal thrust being in the same direction as the adjoint velocity.
    
    Since:
        13.0
    
    Also see:
        FieldUnboundedCartesianEnergyNeglectingMass,
        UnboundedCartesianEnergy
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldUnboundedCartesianEnergy__T): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: _FieldUnboundedCartesianEnergy__T, eventDetectionSettings: org.orekit.propagation.events.FieldEventDetectionSettings[_FieldUnboundedCartesianEnergy__T]): ...
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_FieldUnboundedCartesianEnergy__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_FieldUnboundedCartesianEnergy__T]]:
        """
        Get the detectors needed for propagation.
        
        Parameters:
            field (Field<FieldUnboundedCartesianEnergy> field): field
        
        Returns:
            event detectors
        
        
        """
        ...
    def toCartesianCost(self) -> 'UnboundedCartesianEnergy':
        """
        Method returning equivalent in non-Field.
        
        Returns:
            cost function for non-Field applications
        
        
        """
        ...

class UnboundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.CartesianEnergyConsideringMass):
    """
    Class for unbounded energy cost with Cartesian coordinates. Here, the control vector is chosen as the thrust force, expressed in the propagation frame. This leads to the optimal thrust being in the same direction as the adjoint velocity.
    
    Since:
        12.2
    
    Also see:
        UnboundedCartesianEnergyNeglectingMass
    """
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float): ...
    @typing.overload
    def __init__(self, name: str, massFlowRateFactor: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]:
        """
        Get the detectors needed for propagation.
        
        Returns:
            event detectors
        
        
        """
        ...

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
