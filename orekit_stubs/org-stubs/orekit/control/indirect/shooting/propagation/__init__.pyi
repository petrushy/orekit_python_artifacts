import java.util
import org.hipparchus
import org.orekit.attitudes
import org.orekit.control.indirect.adjoint
import org.orekit.control.indirect.adjoint.cost
import org.orekit.control.indirect.shooting.propagation.class-use
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation.conversion
import org.orekit.propagation.integration
import typing



class AdjointDynamicsProvider:
    """
    public interface AdjointDynamicsProvider
    
        Interface for adjoint derivatives provider (both standard and Field).
    
        Since:
            12.2
    """
    def buildAdditionalDerivativesProvider(self) -> org.orekit.propagation.integration.AdditionalDerivativesProvider:
        """
            Builds adjoint derivatives provider.
        
            Returns:
                derivatives provider
        
        
        """
        ...
    _buildFieldAdditionalDerivativesProvider__T = typing.TypeVar('_buildFieldAdditionalDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def buildFieldAdditionalDerivativesProvider(self, field: org.hipparchus.Field[_buildFieldAdditionalDerivativesProvider__T]) -> org.orekit.propagation.integration.FieldAdditionalDerivativesProvider[_buildFieldAdditionalDerivativesProvider__T]:
        """
            Builds Field adjoint derivatives provider.
        
            Parameters:
                field (:class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): input field
        
            Returns:
                derivatives provider
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Returns:
                name
        
        
        """
        ...

class ShootingIntegrationSettings:
    """
    public interface ShootingIntegrationSettings
    
        Defines integration settings for indirect shooting methods. Gives standard and Field integrator builders.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings`,
            :class:`~org.orekit.propagation.conversion.ODEIntegratorBuilder`,
            :class:`~org.orekit.propagation.conversion.FieldODEIntegratorBuilder`
    """
    _getFieldIntegratorBuilder__T = typing.TypeVar('_getFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldIntegratorBuilder(self, field: org.hipparchus.Field[_getFieldIntegratorBuilder__T]) -> org.orekit.propagation.conversion.FieldODEIntegratorBuilder[_getFieldIntegratorBuilder__T]:
        """
            Returns a Field ODE integrator builder.
        
            Parameters:
                field (:class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field for builder
        
            Returns:
                builder
        
        
        """
        ...
    def getIntegratorBuilder(self) -> org.orekit.propagation.conversion.ODEIntegratorBuilder:
        """
            Returns an ODE integrator builder.
        
            Returns:
                builder
        
        
        """
        ...

class ShootingPropagationSettings:
    """
    public class ShootingPropagationSettings extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Defines propagation settings for indirect shooting methods. The provided list of :class:`~org.orekit.forces.ForceModel`
        should have their counterpart in the provided adjoint equations encapsulated in
        :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`. Note that in case of orbit-based
        propagation (with a central body), the Newtonian term still needs to be passed explicitly (with its adjoint equivalent).
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.propagation.numerical.NumericalPropagator`,
            :class:`~org.orekit.propagation.numerical.FieldNumericalPropagator`
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.forces.ForceModel], adjointDynamicsProvider: AdjointDynamicsProvider, shootingIntegrationSettings: ShootingIntegrationSettings): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.forces.ForceModel], adjointDynamicsProvider: AdjointDynamicsProvider, frame: org.orekit.frames.Frame, shootingIntegrationSettings: ShootingIntegrationSettings, attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
    def getAdjointDynamicsProvider(self) -> AdjointDynamicsProvider:
        """
            Getter for adjoint dynamics provider.
        
            Returns:
                adjoint dynamics
        
        
        """
        ...
    def getAttitudeProvider(self) -> org.orekit.attitudes.AttitudeProvider:
        """
            Getter for the attitude provider.
        
            Returns:
                attitude provider.
        
        
        """
        ...
    def getForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]: ...
    def getIntegrationSettings(self) -> ShootingIntegrationSettings:
        """
            Getter for the integration settings.
        
            Returns:
                integration settings
        
        
        """
        ...
    def getPropagationFrame(self) -> org.orekit.frames.Frame:
        """
            Getter for the propagation frame.
        
            Returns:
                propagation frame
        
        
        """
        ...

class CartesianAdjointDynamicsProvider(AdjointDynamicsProvider):
    """
    public class CartesianAdjointDynamicsProvider extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
    
        Class for Cartesian adjoint derivatives provider (both standard and Field).
    
        Since:
            12.2
    """
    def __init__(self, cartesianCost: org.orekit.control.indirect.adjoint.cost.CartesianCost, cartesianAdjointEquationTermArray: typing.List[org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm]): ...
    def buildAdditionalDerivativesProvider(self) -> org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider:
        """
            Builds adjoint derivatives provider.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider.buildAdditionalDerivativesProvider` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
        
            Returns:
                derivatives provider
        
        
        """
        ...
    _buildFieldAdditionalDerivativesProvider__T = typing.TypeVar('_buildFieldAdditionalDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def buildFieldAdditionalDerivativesProvider(self, field: org.hipparchus.Field[_buildFieldAdditionalDerivativesProvider__T]) -> org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider[_buildFieldAdditionalDerivativesProvider__T]:
        """
            Builds Field adjoint derivatives provider.
        
            Specified by:
                
                meth:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider.buildFieldAdditionalDerivativesProvider` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
        
            Parameters:
                field (:class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): input field
        
            Returns:
                derivatives provider
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
            Getter for adjoint vector name.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider.getAdjointName` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
        
            Returns:
                name
        
        
        """
        ...

class ClassicalRungeKuttaIntegrationSettings(ShootingIntegrationSettings):
    """
    public class ClassicalRungeKuttaIntegrationSettings extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings`
    
        Integration settings using the classical Runge-Kutta 4 scheme.
    
        Since:
            12.2
    
        Also see:
            
            class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator?is`
    """
    def __init__(self, double: float): ...
    _getFieldIntegratorBuilder__T = typing.TypeVar('_getFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldIntegratorBuilder(self, field: org.hipparchus.Field[_getFieldIntegratorBuilder__T]) -> org.orekit.propagation.conversion.ClassicalRungeKuttaFieldIntegratorBuilder[_getFieldIntegratorBuilder__T]:
        """
            Returns a Field ODE integrator builder.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings.getFieldIntegratorBuilder` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings`
        
            Parameters:
                field (:class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field for builder
        
            Returns:
                builder
        
        
        """
        ...
    def getIntegratorBuilder(self) -> org.orekit.propagation.conversion.ClassicalRungeKuttaIntegratorBuilder:
        """
            Returns an ODE integrator builder.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings.getIntegratorBuilder` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings`
        
            Returns:
                builder
        
        
        """
        ...

class DormandPrince54IntegrationSettings(ShootingIntegrationSettings):
    """
    public class DormandPrince54IntegrationSettings extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings`
    
        Integration settings using the Dormand-Prince 5(4) scheme.
    
        Since:
            12.2
    
        Also see:
            
            class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.ode.nonstiff.ClassicalRungeKuttaIntegrator?is`
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    _getFieldIntegratorBuilder__T = typing.TypeVar('_getFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldIntegratorBuilder(self, field: org.hipparchus.Field[_getFieldIntegratorBuilder__T]) -> org.orekit.propagation.conversion.DormandPrince54FieldIntegratorBuilder[_getFieldIntegratorBuilder__T]:
        """
            Returns a Field ODE integrator builder.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings.getFieldIntegratorBuilder` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings`
        
            Parameters:
                field (:class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field for builder
        
            Returns:
                builder
        
        
        """
        ...
    def getIntegratorBuilder(self) -> org.orekit.propagation.conversion.DormandPrince54IntegratorBuilder:
        """
            Returns an ODE integrator builder.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings.getIntegratorBuilder` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.ShootingIntegrationSettings`
        
            Returns:
                builder
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.shooting.propagation")``.

    AdjointDynamicsProvider: typing.Type[AdjointDynamicsProvider]
    CartesianAdjointDynamicsProvider: typing.Type[CartesianAdjointDynamicsProvider]
    ClassicalRungeKuttaIntegrationSettings: typing.Type[ClassicalRungeKuttaIntegrationSettings]
    DormandPrince54IntegrationSettings: typing.Type[DormandPrince54IntegrationSettings]
    ShootingIntegrationSettings: typing.Type[ShootingIntegrationSettings]
    ShootingPropagationSettings: typing.Type[ShootingPropagationSettings]
    class-use: org.orekit.control.indirect.shooting.propagation.class-use.__module_protocol__
