
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
            field (Field<T> field): input field
        
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
    Factory for common Cartesian adjoint dynamics providers.
    
    Since:
        13.0
    
    Also see:
        AdjointDynamicsProvider
    """
    @staticmethod
    def buildBoundedEnergyProvider(adjointName: str, massFlowRateFactor: float, maximumThrustMagnitude: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with bounded Cartesian energy as cost.
        
        Parameters:
            adjointName (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
            eventDetectionSettings (EventDetectionSettings): detection settings for adjoint-related events
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...
    @staticmethod
    def buildBoundedFuelCostProvider(adjointName: str, massFlowRateFactor: float, maximumThrustMagnitude: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with bounded Cartesian fuel as cost.
        
        Parameters:
            adjointName (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
            eventDetectionSettings (EventDetectionSettings): detection settings for adjoint-related events
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...
    @staticmethod
    def buildFlightDurationProvider(adjointName: str, massFlowRateFactor: float, maximumThrustMagnitude: float, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with unbounded Cartesian energy and vanishing mass flow as cost.
        
        Parameters:
            adjointName (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...
    @staticmethod
    def buildLogarithmicBarrierFuelCostProvider(adjointName: str, massFlowRateFactor: float, maximumThrustMagnitude: float, epsilon: float, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with bounded Cartesian fuel penalized with a logarithmic barrier.
        
        Parameters:
            adjointName (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
            epsilon (double): penalty weight
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...
    @staticmethod
    def buildQuadraticPenaltyFuelCostProvider(adjointName: str, massFlowRateFactor: float, maximumThrustMagnitude: float, epsilon: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with bounded Cartesian fuel penalized with a quadratic term.
        
        Parameters:
            adjointName (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            maximumThrustMagnitude (double): maximum thrust magnitude
            epsilon (double): penalty weight
            eventDetectionSettings (EventDetectionSettings): detection settings for adjoint-related events
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...
    @staticmethod
    def buildUnboundedEnergyProvider(adjointName: str, massFlowRateFactor: float, eventDetectionSettings: org.orekit.propagation.events.EventDetectionSettings, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with unbounded Cartesian energy as cost.
        
        Parameters:
            adjointName (String): adjoint name
            massFlowRateFactor (double): mass flow rate factor
            eventDetectionSettings (EventDetectionSettings): detection settings for adjoint-related events
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...
    @staticmethod
    def buildUnboundedEnergyProviderNeglectingMass(adjointName: str, *cartesianAdjointEquationTerms: org.orekit.control.indirect.adjoint.CartesianAdjointEquationTerm) -> 'CartesianAdjointDynamicsProvider':
        """
        Method building a provider with unbounded Cartesian energy and vanishing mass flow as cost.
        
        Parameters:
            adjointName (String): adjoint name
            cartesianAdjointEquationTerms (CartesianAdjointEquationTerm...): Cartesian adjoint equation terms
        
        Returns:
            provider
        
        
        """
        ...

class ShootingIntegrationSettings:
    """
    Defines integration settings for indirect shooting methods. Gives standard and Field integrator builders.
    
    Since:
        12.2
    
    Also see:
        ShootingPropagationSettings,
        ExplicitRungeKuttaIntegratorBuilder,
        FieldExplicitRungeKuttaIntegratorBuilder
    """
    _getFieldIntegratorBuilder__T = typing.TypeVar('_getFieldIntegratorBuilder__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldIntegratorBuilder(self, field: org.hipparchus.Field[_getFieldIntegratorBuilder__T]) -> org.orekit.propagation.conversion.FieldExplicitRungeKuttaIntegratorBuilder[_getFieldIntegratorBuilder__T]:
        """
        Returns a Field ODE integrator builder based on an explicit Runge Kutta scheme.
        
        Parameters:
            field (Field<T> field): field for builder
        
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
    Factory for some common schemes.
    
    Since:
        13.0
    
    Also see:
        ShootingPropagationSettings
    """
    @staticmethod
    def getClassicalRungeKuttaIntegratorSettings(step: float) -> ShootingIntegrationSettings:
        """
        Returns shooting integration settings according to the classical Runge Kutta scheme.
        
        Parameters:
            step (double): default step-size
        
        Returns:
            integration settings
        
        
        """
        ...
    @staticmethod
    def getDormandPrince54IntegratorSettings(minStep: float, maxStep: float, toleranceProvider: org.orekit.propagation.ToleranceProvider) -> ShootingIntegrationSettings:
        """
        Returns shooting integration settings according to the Dormand Prince 5(4) scheme.
        
        Parameters:
            minStep (double): minimum step-size
            maxStep (double): maximum step-size
            toleranceProvider (ToleranceProvider): tolerance provider
        
        Returns:
            integration settings
        
        
        """
        ...
    @staticmethod
    def getDormandPrince853IntegratorSettings(minStep: float, maxStep: float, toleranceProvider: org.orekit.propagation.ToleranceProvider) -> ShootingIntegrationSettings:
        """
        Returns shooting integration settings according to the Dormand Prince 8(53) scheme.
        
        Parameters:
            minStep (double): minimum step-size
            maxStep (double): maximum step-size
            toleranceProvider (ToleranceProvider): tolerance provider
        
        Returns:
            integration settings
        
        
        """
        ...
    @staticmethod
    def getLutherIntegratorSettings(step: float) -> ShootingIntegrationSettings:
        """
        Returns shooting integration settings according to the Luther Runge Kutta scheme.
        
        Parameters:
            step (double): default step-size
        
        Returns:
            integration settings
        
        
        """
        ...
    @staticmethod
    def getMidpointIntegratorSettings(step: float) -> ShootingIntegrationSettings:
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
    Defines propagation settings for indirect shooting methods. The provided list of ForceModel should have their counterpart in the provided adjoint equations encapsulated in AdjointDynamicsProvider. Note that in case of orbit-based propagation (with a central body), the Newtonian term still needs to be passed explicitly (with its adjoint equivalent).
    
    Since:
        12.2
    
    Also see:
        NumericalPropagator,
        FieldNumericalPropagator
    """
    @typing.overload
    def __init__(self, forceModels: java.util.List[org.orekit.forces.ForceModel], adjointDynamicsProvider: AdjointDynamicsProvider, integrationSettings: typing.Union[ShootingIntegrationSettings, typing.Callable]): ...
    @typing.overload
    def __init__(self, forceModels: java.util.List[org.orekit.forces.ForceModel], adjointDynamicsProvider: AdjointDynamicsProvider, propagationFrame: org.orekit.frames.Frame, integrationSettings: typing.Union[ShootingIntegrationSettings, typing.Callable], attitudeProvider: org.orekit.attitudes.AttitudeProvider): ...
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
    def getForceModels(self) -> java.util.List[org.orekit.forces.ForceModel]:
        """
        Getter for the force models.
        
        Returns:
            forces
        
        
        """
        ...
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
    Abstract class for Cartesian adjoint derivatives provider.
    
    Since:
        12.2
    
    Also see:
        AdjointDynamicsProvider
    """
    def buildAdditionalDerivativesProvider(self) -> org.orekit.control.indirect.adjoint.CartesianAdjointDerivativesProvider:
        """
        Builds adjoint derivatives provider.
        
        Specified by: buildAdditionalDerivativesProvider in interface AdjointDynamicsProvider
        
        Returns:
            derivatives provider
        
        
        """
        ...
    _buildFieldAdditionalDerivativesProvider__T = typing.TypeVar('_buildFieldAdditionalDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def buildFieldAdditionalDerivativesProvider(self, field: org.hipparchus.Field[_buildFieldAdditionalDerivativesProvider__T]) -> org.orekit.control.indirect.adjoint.FieldCartesianAdjointDerivativesProvider[_buildFieldAdditionalDerivativesProvider__T]:
        """
        Builds Field adjoint derivatives provider.
        
        Specified by: meth:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider.buildFieldAdditionalDerivativesProvider` in interface AdjointDynamicsProvider
        
        Parameters:
            field (Field<T> field): input field
        
        Returns:
            derivatives provider
        
        
        """
        ...
    def getAdjointName(self) -> str:
        """
        Getter for adjoint vector name.
        
        Specified by: getAdjointName in interface AdjointDynamicsProvider
        
        Returns:
            name
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Getter for adjoint dimension.
        
        Specified by: getDimension in interface AdjointDynamicsProvider
        
        Returns:
            dimension
        
        
        """
        ...

class PythonAdjointDynamicsProvider(AdjointDynamicsProvider):
    """
    Python implementation of the AdjointDynamicsProvider interface. This class is part of the JCC Python interface and exposes all methods natively.
    """
    def __init__(self): ...
    def buildAdditionalDerivativesProvider(self) -> org.orekit.propagation.integration.AdditionalDerivativesProvider:
        """
        Builds adjoint derivatives provider.
        
        Specified by: buildAdditionalDerivativesProvider in interface AdjointDynamicsProvider
        
        Returns:
            derivatives provider
        
        
        """
        ...
    _buildFieldAdditionalDerivativesProvider__T = typing.TypeVar('_buildFieldAdditionalDerivativesProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def buildFieldAdditionalDerivativesProvider(self, field: org.hipparchus.Field[_buildFieldAdditionalDerivativesProvider__T]) -> org.orekit.propagation.integration.FieldAdditionalDerivativesProvider[_buildFieldAdditionalDerivativesProvider__T]:
        """
        Builds Field adjoint derivatives provider.
        
        Specified by: meth:`~org.orekit.control.indirect.shooting.propagation.AdjointDynamicsProvider.buildFieldAdditionalDerivativesProvider` in interface AdjointDynamicsProvider
        
        Parameters:
            field (Field<T> field): input field
        
        Returns:
            derivatives provider
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.control.indirect.shooting.propagation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAdjointName(self) -> str:
        """
        Getter for adjoint vector name.
        
        Specified by: getAdjointName in interface AdjointDynamicsProvider
        
        Returns:
            name
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Getter for adjoint dimension.
        
        Specified by: getDimension in interface AdjointDynamicsProvider
        
        Returns:
            dimension
        
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect.shooting.propagation")``.

    AdjointDynamicsProvider: typing.Type[AdjointDynamicsProvider]
    CartesianAdjointDynamicsProvider: typing.Type[CartesianAdjointDynamicsProvider]
    CartesianAdjointDynamicsProviderFactory: typing.Type[CartesianAdjointDynamicsProviderFactory]
    PythonAdjointDynamicsProvider: typing.Type[PythonAdjointDynamicsProvider]
    ShootingIntegrationSettings: typing.Type[ShootingIntegrationSettings]
    ShootingIntegrationSettingsFactory: typing.Type[ShootingIntegrationSettingsFactory]
    ShootingPropagationSettings: typing.Type[ShootingPropagationSettings]
