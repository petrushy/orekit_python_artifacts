
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.hipparchus
import org.orekit.attitudes
import org.orekit.control.indirect.adjoint
import org.orekit.forces
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.conversion
import org.orekit.propagation.events
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
    def getDimension(self) -> int:
        """
            Getter for adjoint dimension.
        
            Returns:
                dimension
        
        
        """
        ...

class CartesianAdjointDynamicsProviderFactory:
    """
    public class CartesianAdjointDynamicsProviderFactory extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory for common Cartesian adjoint dynamics providers.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
    """
    @staticmethod
    def buildBoundedEnergyProvider(string: str, double: float, double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with bounded Cartesian energy as cost.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                massFlowRateFactor (double): mass flow rate factor
                maximumThrustMagnitude (double): maximum thrust magnitude
                eventDetectionSettings (:class:`~org.orekit.propagation.events.EventDetectionSettings`): detection settings for adjoint-related events
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
        """
        ...
    @staticmethod
    def buildBoundedFuelCostProvider(string: str, double: float, double2: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with bounded Cartesian fuel as cost.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                massFlowRateFactor (double): mass flow rate factor
                maximumThrustMagnitude (double): maximum thrust magnitude
                eventDetectionSettings (:class:`~org.orekit.propagation.events.EventDetectionSettings`): detection settings for adjoint-related events
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
        """
        ...
    @staticmethod
    def buildFlightDurationProvider(string: str, double: float, double2: float, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with unbounded Cartesian energy and vanishing mass flow as cost.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                massFlowRateFactor (double): mass flow rate factor
                maximumThrustMagnitude (double): maximum thrust magnitude
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
        """
        ...
    @staticmethod
    def buildLogarithmicBarrierFuelCostProvider(string: str, double: float, double2: float, double3: float, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with bounded Cartesian fuel penalized with a logarithmic barrier.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                massFlowRateFactor (double): mass flow rate factor
                maximumThrustMagnitude (double): maximum thrust magnitude
                epsilon (double): penalty weight
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
        """
        ...
    @staticmethod
    def buildQuadraticPenaltyFuelCostProvider(string: str, double: float, double2: float, double3: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with bounded Cartesian fuel penalized with a quadratic term.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                massFlowRateFactor (double): mass flow rate factor
                maximumThrustMagnitude (double): maximum thrust magnitude
                epsilon (double): penalty weight
                eventDetectionSettings (:class:`~org.orekit.propagation.events.EventDetectionSettings`): detection settings for adjoint-related events
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
        """
        ...
    @staticmethod
    def buildUnboundedEnergyProvider(string: str, double: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with unbounded Cartesian energy as cost.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                massFlowRateFactor (double): mass flow rate factor
                eventDetectionSettings (:class:`~org.orekit.propagation.events.EventDetectionSettings`): detection settings for adjoint-related events
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
        """
        ...
    @staticmethod
    def buildUnboundedEnergyProviderNeglectingMass(string: str, *cartesianAdjointEquationTerm: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
            Method building a provider with unbounded Cartesian energy and vanishing mass flow as cost.
        
            Parameters:
                adjointName (:class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): adjoint name
                cartesianAdjointEquationTerms (:class:`~org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm`...): Cartesian adjoint equation terms
        
            Returns:
                provider
        
        
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
            :class:`~org.orekit.propagation.conversion.ExplicitRungeKuttaIntegratorBuilder`,
            :class:`~org.orekit.propagation.conversion.FieldExplicitRungeKuttaIntegratorBuilder`
    """
    _getFieldIntegratorBuilder__T = typing.TypeVar('_getFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldIntegratorBuilder(self, field: org.hipparchus.Field[_getFieldIntegratorBuilder__T]) -> org.orekit.propagation.conversion.FieldExplicitRungeKuttaIntegratorBuilder[_getFieldIntegratorBuilder__T]:
        """
            Returns a Field ODE integrator builder based on an explicit Runge Kutta scheme.
        
            Parameters:
                field (:class:`~org.orekit.control.indirect.shooting.propagation.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field for builder
        
            Returns:
                builder
        
        
        """
        ...
    def getIntegratorBuilder(self) -> org.orekit.propagation.conversion.ExplicitRungeKuttaIntegratorBuilder:
        """
            Returns an ODE integrator builder based on an explicit Runge Kutta scheme.
        
            Returns:
                builder
        
        
        """
        ...

class ShootingIntegrationSettingsFactory:
    """
    public class ShootingIntegrationSettingsFactory extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Factory for some common schemes.
    
        Since:
            13.0
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.propagation.ShootingPropagationSettings`
    """
    @staticmethod
    def getClassicalRungeKuttaIntegratorSettings(double: float) -> ShootingIntegrationSettings:
        """
            Returns shooting integration settings according to the classical Runge Kutta scheme.
        
            Parameters:
                step (double): default step-size
        
            Returns:
                integration settings
        
        
        """
        ...
    @staticmethod
    def getDormandPrince54IntegratorSettings(double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider) -> ShootingIntegrationSettings:
        """
            Returns shooting integration settings according to the Dormand Prince 5(4) scheme.
        
            Parameters:
                minStep (double): minimum step-size
                maxStep (double): maximum step-size
                toleranceProvider (:class:`~org.orekit.propagation.ToleranceProvider`): tolerance provider
        
            Returns:
                integration settings
        
        
        """
        ...
    @staticmethod
    def getDormandPrince853IntegratorSettings(double: float, double2: float, toleranceProvider: org.orekit.propagation.ToleranceProvider) -> ShootingIntegrationSettings:
        """
            Returns shooting integration settings according to the Dormand Prince 8(53) scheme.
        
            Parameters:
                minStep (double): minimum step-size
                maxStep (double): maximum step-size
                toleranceProvider (:class:`~org.orekit.propagation.ToleranceProvider`): tolerance provider
        
            Returns:
                integration settings
        
        
        """
        ...
    @staticmethod
    def getLutherIntegratorSettings(double: float) -> ShootingIntegrationSettings:
        """
            Returns shooting integration settings according to the Luther Runge Kutta scheme.
        
            Parameters:
                step (double): default step-size
        
            Returns:
                integration settings
        
        
        """
        ...
    @staticmethod
    def getMidpointIntegratorSettings(double: float) -> ShootingIntegrationSettings:
        """
            Returns shooting integration settings according to the midpoint Runge Kutta scheme.
        
            Parameters:
                step (double): default step-size
        
            Returns:
                integration settings
        
        
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
    def __init__(self, list: java.util.List[org.orekit.forces.ForceModel], adjointDynamicsProvider: AdjointDynamicsProvider, shootingIntegrationSettings: typing.Union[ShootingIntegrationSettings, typing.Callable]): ...
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.forces.ForceModel], adjointDynamicsProvider: AdjointDynamicsProvider, frame: org.orekit.frames.Frame, shootingIntegrationSettings: typing.Union[ShootingIntegrationSettings, typing.Callable], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
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
    public abstract class CartesianAdjointDynamicsProvider extends :class:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
    
        Abstract class for Cartesian adjoint derivatives provider.
    
        Since:
            12.2
    
        Also see:
            :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
    """
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
    def buildFieldAdditionalDerivativesProvider(self, field: org.hipparchus.Field[_buildFieldAdditionalDerivativesProvider__T]) -> org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider[_buildFieldAdditionalDerivativesProvider__T]: ...
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
    def getDimension(self) -> int:
        """
            Getter for adjoint dimension.
        
            Specified by:
                :meth:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider.getDimension` in
                interface :class:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider`
        
            Returns:
                dimension
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.shooting.propagation")``.

    AdjointDynamicsProvider: typing.Type[AdjointDynamicsProvider]
    CartesianAdjointDynamicsProvider: typing.Type[CartesianAdjointDynamicsProvider]
    CartesianAdjointDynamicsProviderFactory: typing.Type[CartesianAdjointDynamicsProviderFactory]
    ShootingIntegrationSettings: typing.Type[ShootingIntegrationSettings]
    ShootingIntegrationSettingsFactory: typing.Type[ShootingIntegrationSettingsFactory]
    ShootingPropagationSettings: typing.Type[ShootingPropagationSettings]
