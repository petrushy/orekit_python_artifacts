import java.util
import java.util.stream
import org
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.control.indirect.adjoint.cost.class-use
import org.orekit.propagation.events
import org.orekit.utils
import typing



class CartesianCost(org.orekit.propagation.events.EventDetectorsProvider):
    """
    public interface CartesianCost extends :class:`~org.orekit.propagation.events.EventDetectorsProvider`
    
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
            Getter for adjoint vector dimension. Default is 7 (six for Cartesian coordinates and one for mass).
        
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
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, tArray: typing.List[_getFieldHamiltonianContribution__T], t2: _getFieldHamiltonianContribution__T) -> _getFieldHamiltonianContribution__T:
        """
            Computes the Hamiltonian contribution of the cost function.
        
            Parameters:
                adjointVariables (T[]): adjoint vector
                mass (T): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    _getFieldThrustAccelerationVector__T = typing.TypeVar('_getFieldThrustAccelerationVector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldThrustAccelerationVector(self, tArray: typing.List[_getFieldThrustAccelerationVector__T], t2: _getFieldThrustAccelerationVector__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldThrustAccelerationVector__T]:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (T[]): adjoint vector
                mass (T): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def getHamiltonianContribution(self, doubleArray: typing.List[float], double2: float) -> float:
        """
            Computes the Hamiltonian contribution of the cost function.
        
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
    def getThrustAccelerationVector(self, doubleArray: typing.List[float], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.List[float], double2: float, doubleArray2: typing.List[float]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...
    _updateFieldAdjointDerivatives__T = typing.TypeVar('_updateFieldAdjointDerivatives__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def updateFieldAdjointDerivatives(self, tArray: typing.List[_updateFieldAdjointDerivatives__T], t2: _updateFieldAdjointDerivatives__T, tArray2: typing.List[_updateFieldAdjointDerivatives__T]) -> None:
        """
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (T[]): adjoint vector
                mass (T): mass
                adjointDerivatives (T[]): derivatives to update
        
        
        """
        ...

class AbstractCartesianEnergy(CartesianCost):
    """
    public abstract class AbstractCartesianEnergy extends :class:`~org.orekit.control.indirect.adjoint.cost.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    
        Abstract class for energy cost with Cartesian coordinates. An energy cost is proportional to the integral over time of
        the Euclidean norm of the control vector, often scaled with 1/2. This type of cost is not optimal in terms of mass
        consumption, however its solutions showcase a smoother behavior favorable for convergence in shooting techniques.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
    """
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

class UnboundedCartesianEnergyNeglectingMass(AbstractCartesianEnergy):
    """
    public class UnboundedCartesianEnergyNeglectingMass extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianEnergy`
    
        Class for unbounded energy cost with Cartesian coordinates neglecting the mass consumption. Under this assumption, the
        mass is constant and there is no need to consider the corresponding adjoint variable. Here, the control vector is chosen
        as the acceleration given by thrusting, expressed in the propagation frame. This leads to the optimal thrust force being
        equal to the adjoint velocity vector times the mass.
    
        Since:
            12.2
    """
    def __init__(self, string: str): ...
    def getAdjointDimension(self) -> int:
        """
            Getter for adjoint vector dimension. Default is 7 (six for Cartesian coordinates and one for mass).
        
            Returns:
                adjoint dimension
        
        
        """
        ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    _getFieldHamiltonianContribution__T = typing.TypeVar('_getFieldHamiltonianContribution__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldHamiltonianContribution(self, tArray: typing.List[_getFieldHamiltonianContribution__T], t2: _getFieldHamiltonianContribution__T) -> _getFieldHamiltonianContribution__T:
        """
            Computes the Hamiltonian contribution of the cost function.
        
            Parameters:
                adjointVariables (T[]): adjoint vector
                mass (T): mass
        
            Returns:
                contribution to Hamiltonian
        
        
        """
        ...
    _getFieldThrustAccelerationVector__T = typing.TypeVar('_getFieldThrustAccelerationVector__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldThrustAccelerationVector(self, tArray: typing.List[_getFieldThrustAccelerationVector__T], t2: _getFieldThrustAccelerationVector__T) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getFieldThrustAccelerationVector__T]:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (T[]): adjoint vector
                mass (T): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def getHamiltonianContribution(self, doubleArray: typing.List[float], double2: float) -> float:
        """
            Computes the Hamiltonian contribution of the cost function.
        
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
        
            Specified by:
                :meth:`~org.orekit.control.indirect.adjoint.cost.CartesianCost.getMassFlowRateFactor` in
                interface :class:`~org.orekit.control.indirect.adjoint.cost.CartesianCost`
        
            Overrides:
                :meth:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianEnergy.getMassFlowRateFactor` in
                class :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianEnergy`
        
            Returns:
                mass flow rate factor
        
        
        """
        ...
    def getThrustAccelerationVector(self, doubleArray: typing.List[float], double2: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Computes the thrust acceleration vector in propagation frame from the adjoint variables and the mass.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
        
            Returns:
                thrust vector
        
        
        """
        ...
    def updateAdjointDerivatives(self, doubleArray: typing.List[float], double2: float, doubleArray2: typing.List[float]) -> None:
        """
            Description copied from
            interface: :meth:`~org.orekit.control.indirect.adjoint.cost.CartesianCost.updateAdjointDerivatives`
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (double[]): adjoint vector
                mass (double): mass
                adjointDerivatives (double[]): derivatives to update
        
        
        """
        ...
    _updateFieldAdjointDerivatives__T = typing.TypeVar('_updateFieldAdjointDerivatives__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def updateFieldAdjointDerivatives(self, tArray: typing.List[_updateFieldAdjointDerivatives__T], t2: _updateFieldAdjointDerivatives__T, tArray2: typing.List[_updateFieldAdjointDerivatives__T]) -> None:
        """
            Description copied from
            interface: :meth:`~org.orekit.control.indirect.adjoint.cost.CartesianCost.updateFieldAdjointDerivatives`
            Update the adjoint derivatives if necessary.
        
            Parameters:
                adjointVariables (T[]): adjoint vector
                mass (T): mass
                adjointDerivatives (T[]): derivatives to update
        
        
        """
        ...

class BoundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.CartesianEnergyConsideringMass):
    """
    public class BoundedCartesianEnergy extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianEnergy`
    
        Class for bounded energy cost with Cartesian coordinates. Here, the control vector is chosen as the thrust force divided
        by the maximum thrust magnitude and expressed in the propagation frame. It has a unit Euclidean norm.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.adjoint.cost.UnboundedCartesianEnergyNeglectingMass`
    """
    @typing.overload
    def __init__(self, string: str, double: float, double2: float): ...
    @typing.overload
    def __init__(self, string: str, double: float, double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings): ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...

class UnboundedCartesianEnergy(org.orekit.control.indirect.adjoint.cost.CartesianEnergyConsideringMass):
    """
    public class UnboundedCartesianEnergy extends :class:`~org.orekit.control.indirect.adjoint.cost.AbstractCartesianEnergy`
    
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
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...

class CartesianEnergyConsideringMass: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.adjoint.cost")``.

    AbstractCartesianEnergy: typing.Type[AbstractCartesianEnergy]
    BoundedCartesianEnergy: typing.Type[BoundedCartesianEnergy]
    CartesianCost: typing.Type[CartesianCost]
    CartesianEnergyConsideringMass: typing.Type[CartesianEnergyConsideringMass]
    UnboundedCartesianEnergy: typing.Type[UnboundedCartesianEnergy]
    UnboundedCartesianEnergyNeglectingMass: typing.Type[UnboundedCartesianEnergyNeglectingMass]
    class-use: org.orekit.control.indirect.adjoint.cost.class-use.__module_protocol__
