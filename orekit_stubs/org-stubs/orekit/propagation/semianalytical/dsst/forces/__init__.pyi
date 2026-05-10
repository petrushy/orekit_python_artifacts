
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.orekit.attitudes
import org.orekit.bodies
import org.orekit.forces
import org.orekit.forces.drag
import org.orekit.forces.gravity.potential
import org.orekit.forces.radiation
import org.orekit.frames
import org.orekit.models.earth.atmosphere
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.semianalytical.dsst.utilities
import org.orekit.time
import org.orekit.utils
import typing



class DSSTForceModel(org.orekit.utils.ParameterDriversProvider, org.orekit.propagation.events.EventDetectorsProvider):
    """
    This interface represents a force modifying spacecraft motion for a DSSTPropagator.
    
    Objects implementing this interface are intended to be added to a DSSTPropagator before the propagation is started.
    
    The propagator will call at the very beginning of a propagation the initializeShortPeriodTerms method allowing preliminary computation such as truncation if needed.
    
    Then the propagator will call at each step:
    
      1.  the getMeanElementRate method. The force model instance will extract all the state data needed to compute the mean element rates that contribute to the mean state derivative. 2.  the updateShortPeriodTerms method, if osculating parameters are desired, on a sample of points within the last step.
    """
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, parameters: typing.Union[typing.List[float], jpype.JArray], date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Extract the proper parameter drivers' values from the array in input of the updateShortPeriodTerms method. Parameters are filtered given an input date.
        
        Parameters:
            parameters (double[]): the input parameters array containing all span values of all drivers from which the parameter values at date date wants
                to be extracted
            date (AbsoluteDate): the date
        
        Returns:
            the parameters given the date
        
        """
        ...
    @typing.overload
    def extractParameters(self, parameters: typing.Union[typing.List[_extractParameters_1__T], jpype.JArray], date: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.MutableSequence[_extractParameters_1__T]:
        """
        Extract the proper parameter drivers' values from the array in input of the updateShortPeriodTerms method. Parameters are filtered given an input date.
        
        Parameters:
            parameters (T[]): the input parameters array containing all span values of all drivers from which the parameter values at date date wants
                to be extracted
            date (FieldAbsoluteDate<T> date): the date
        
        Returns:
            the parameters given the date
        
        
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
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialize the force model at the start of propagation.
        
        The default implementation of this method does nothing.
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): spacecraft state at the start of propagation.
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        Since:
            11.1
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the force model at the start of propagation.
        
        The default implementation of this method does nothing.
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        Since:
            11.0
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List['ShortPeriodTerms']: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List['FieldShortPeriodTerms'[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, provider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Parameters:
            provider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

_FieldForceModelContext__T = typing.TypeVar('_FieldForceModelContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldForceModelContext(typing.Generic[_FieldForceModelContext__T]):
    """
    Base class for dsst force models parameter containers.
    
    Since:
        10.0
    """
    def getFieldAuxiliaryElements(self) -> org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_FieldForceModelContext__T]:
        """
        Method to get the auxiliary elementsrelated to the ForceModelContext.
        
        Returns:
            field auxiliary elements
        
        
        """
        ...

_FieldShortPeriodTerms__T = typing.TypeVar('_FieldShortPeriodTerms__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldShortPeriodTerms(typing.Generic[_FieldShortPeriodTerms__T]):
    """
    Additive short period terms contributing to the mean to osculating orbit mapping.
    
    Each instance contains a set of several terms that are computed together.
    
    Also see:
        DSSTForceModel
    """
    def getCoefficients(self, date: org.orekit.time.FieldAbsoluteDate[_FieldShortPeriodTerms__T], selected: java.util.Set[str]) -> java.util.Map[str, typing.MutableSequence[_FieldShortPeriodTerms__T]]:
        """
        Computes the coefficients involved in the contributions.
        
        This method is intended mainly for validation purposes. Its output is highly dependent on the implementation details in each force model and may change from version to version. It is not recommended to use it for any operational purposes.
        
        Parameters:
            date (FieldAbsoluteDate<FieldShortPeriodTerms> date): current date
            selected (Set<String> selected): set of coefficients that should be put in the map (empty set means all coefficients are selected)
        
        Returns:
            the selected coefficients of the short periodic variations, in a map where all keys start with
            getCoefficientsKeyPrefix
        
        
        """
        ...
    def getCoefficientsKeyPrefix(self) -> str:
        """
        Get the prefix for short period coefficients keys.
        
        This prefix is used to identify the coefficients of the current force model from the coefficients pertaining to other force models. All the keys in the map returned by getCoefficients start with this prefix, which must be unique among all providers.
        
        Returns:
            the prefix for short periodic coefficients keys
        
        Also see:
            getCoefficients
        
        
        """
        ...
    def value(self, meanOrbit: org.orekit.orbits.FieldOrbit[_FieldShortPeriodTerms__T]) -> typing.MutableSequence[_FieldShortPeriodTerms__T]:
        """
        Evaluate the contributions of the short period terms.
        
        Parameters:
            meanOrbit (FieldOrbit<FieldShortPeriodTerms> meanOrbit): mean orbit to which the short period contribution applies
        
        Returns:
            short period terms contributions
        
        
        """
        ...

class ForceModelContext:
    """
    Base class for dsst force models attributes containers.
    
    Since:
        10.0
    """
    def getAuxiliaryElements(self) -> org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements:
        """
        Method to get the auxiliary elements related to the ForceModelContext.
        
        Returns:
            auxiliary elements
        
        
        """
        ...

class J2SquaredModel:
    """
    Semi-analytical J2-squared model.
    
    This interface is implemented by models providing J2-squared second-order terms in equinoctial elements. These terms are used in the computation of the closed-form J2-squared perturbation in semi-analytical satellite theory.
    
    Since:
        12.0
    
    Also see:
        ZeisModel
    """
    _computeMeanEquinoctialSecondOrderTerms_1__T = typing.TypeVar('_computeMeanEquinoctialSecondOrderTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeMeanEquinoctialSecondOrderTerms(self, context: 'DSSTJ2SquaredClosedFormContext') -> typing.MutableSequence[float]:
        """
        Compute the J2-squared second-order terms in equinoctial elements.
        
        Parameters:
            context (DSSTJ2SquaredClosedFormContext): model context
        
        Returns:
            the J2-squared second-order terms in equinoctial elements. Order must follow: [A, K, H, Q, P, M]
        
        """
        ...
    @typing.overload
    def computeMeanEquinoctialSecondOrderTerms(self, context: 'FieldDSSTJ2SquaredClosedFormContext'[_computeMeanEquinoctialSecondOrderTerms_1__T]) -> typing.MutableSequence[_computeMeanEquinoctialSecondOrderTerms_1__T]:
        """
        Compute the J2-squared second-order terms in equinoctial elements.
        
        Parameters:
            context (FieldDSSTJ2SquaredClosedFormContext<T> context): model context
        
        Returns:
            the J2-squared second-order terms in equinoctial elements. Order must follow: [A, K, H, Q, P, M]
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List['ShortPeriodTerms']: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the J2-squared short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Parameters:
            parameters (double[]): force model parameters
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        Since:
            12.2
        
        default <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the J2-squared short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Parameters:
            parameters (T[]): force model parameters
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        Since:
            12.2
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

class ShortPeriodTerms:
    """
    Additive short period terms contributing to the mean to osculating orbit mapping.
    
    Each instance contains a set of several terms that are computed together.
    
    Since:
        7.1
    
    Also see:
        DSSTForceModel
    """
    def getCoefficients(self, date: org.orekit.time.AbsoluteDate, selected: java.util.Set[str]) -> java.util.Map[str, typing.MutableSequence[float]]:
        """
        Computes the coefficients involved in the contributions.
        
        This method is intended mainly for validation purposes. Its output is highly dependent on the implementation details in each force model and may change from version to version. It is not recommended to use it for any operational purposes.
        
        Parameters:
            date (AbsoluteDate): current date
            selected (Set<String> selected): set of coefficients that should be put in the map (empty set means all coefficients are selected)
        
        Returns:
            the selected coefficients of the short periodic variations, in a map where all keys start with
            getCoefficientsKeyPrefix
        
        
        """
        ...
    def getCoefficientsKeyPrefix(self) -> str:
        """
        Get the prefix for short period coefficients keys.
        
        This prefix is used to identify the coefficients of the current force model from the coefficients pertaining to other force models. All the keys in the map returned by getCoefficients start with this prefix, which must be unique among all providers.
        
        Returns:
            the prefix for short periodic coefficients keys
        
        Also see:
            getCoefficients
        
        
        """
        ...
    def value(self, meanOrbit: org.orekit.orbits.Orbit) -> typing.MutableSequence[float]:
        """
        Evaluate the contributions of the short period terms.
        
        Parameters:
            meanOrbit (Orbit): mean orbit to which the short period contribution applies
        
        Returns:
            short period terms contributions
        
        
        """
        ...

class AbstractGaussianContribution(DSSTForceModel):
    """
    Common handling of DSSTForceModel methods for Gaussian contributions to DSST propagation.
    
    This abstract class allows to provide easily a subset of DSSTForceModel methods for specific Gaussian contributions.
    
    This class implements the notion of numerical averaging of the DSST theory. Numerical averaging is mainly used for non-conservative disturbing forces such as atmospheric drag and solar radiation pressure.
    
    Gaussian contributions can be expressed as: da :sub:`i` /dt = δa :sub:`i` /δv . q
    
    where:
    
      - a :sub:`i` are the six equinoctial elements
      - v is the velocity vector
      - q is the perturbing acceleration due to the considered force
    
    The averaging process and other considerations lead to integrate this contribution over the true longitude L possibly taking into account some limits.
    
    To create a numerically averaged contribution, one needs only to provide a ForceModel and to implement in the derived class the methods: getLLimits and getParametersDriversWithoutMu.
    """
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Parameters:
            state (SpacecraftState): current state
            gauss (GaussQuadrature): Gauss quadrature
            low (double): lower bound of the integral interval
            high (double): upper bound of the integral interval
            context (AbstractGaussianContributionContext): container for attributes
            parameters (double[]): values of the force model parameters at state date (1 values for each parameters)
        
        Returns:
            the mean element rates
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            gauss (GaussQuadrature): Gauss quadrature
            low (T): lower bound of the integral interval
            high (T): upper bound of the integral interval
            context (FieldAbstractGaussianContributionContext<T> context): container for attributes
            parameters (T[]): values of the force model parameters(1 values for each parameters)
        
        Returns:
            the mean element rates
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, initialState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], target: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None:
        """
        Initialize the force model at the start of propagation.
        
        The default implementation of this method does nothing.
        
        Specified by: init in interface DSSTForceModel
        
        Parameters:
            initialState (FieldSpacecraftState<T> initialState): spacecraft state at the start of propagation.
            target (FieldAbsoluteDate<T> target): date of propagation. Not equal to getDate().
        
        
        """
        ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the force model at the start of propagation.
        
        The default implementation of this method does nothing.
        
        Specified by: init in interface DSSTForceModel
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, provider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            provider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

class AbstractGaussianContributionContext(ForceModelContext):
    """
    This class is a container for the common parameters used in AbstractGaussianContribution.
    
    It performs parameters initialization at each integration step for the Gaussian contributions
    
    Since:
        10.0
    """
    def getCo2AB(self) -> float:
        """
        Get co2AB = C / 2AB.
        
        Returns:
            co2AB
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
        Get the Keplerian mean motion.
        
        The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMu(self) -> float:
        """
        Get central attraction coefficient.
        
        Returns:
            mu
        
        
        """
        ...
    def getOOA(self) -> float:
        """
        Get ooA = 1 / A.
        
        Returns:
            ooA
        
        
        """
        ...
    def getOOAB(self) -> float:
        """
        Get ooAB = 1 / (A * B).
        
        Returns:
            ooAB
        
        
        """
        ...
    def getOoBpo(self) -> float:
        """
        Get ooBpo = 1 / (B + 1).
        
        Returns:
            ooBpo
        
        
        """
        ...
    def getOoMU(self) -> float:
        """
        Get ooMu = 1 / mu.
        
        Returns:
            ooMu
        
        
        """
        ...
    def getTon2a(self) -> float:
        """
        Get ton2a = 2 / (n² * a).
        
        Returns:
            ton2a
        
        
        """
        ...

class DSSTGravityContext(ForceModelContext):
    """
    This class is a container for the common parameters used in DSSTTesseral and DSSTZonal.
    
    It performs parameters initialization at each integration step for the Tesseral and Zonal contribution to the central body gravitational perturbation.
    
    Since:
        12.2
    """
    def getA(self) -> float:
        """
        Getter for the a.
        
        Returns:
            the a
        
        
        """
        ...
    def getAlpha(self) -> float:
        """
        Get direction cosine α for central body.
        
        Returns:
            α
        
        
        """
        ...
    def getAx2oA(self) -> float:
        """
        Getter for the ax2oA.
        
        Returns:
            the ax2oA
        
        
        """
        ...
    def getBeta(self) -> float:
        """
        Get direction cosine β for central body.
        
        Returns:
            β
        
        
        """
        ...
    def getBoA(self) -> float:
        """
        Get B / A.
        
        Returns:
            the boA
        
        
        """
        ...
    def getBoABpo(self) -> float:
        """
        Get BoABpo = B / A(1 + B).
        
        Returns:
            the boABpo
        
        
        """
        ...
    def getBodyFixedToInertialTransform(self) -> org.orekit.frames.StaticTransform:
        """
        Getter for the bodyFixedToInertialTransform.
        
        Returns:
            the bodyFixedToInertialTransform
        
        
        """
        ...
    def getChi(self) -> float:
        """
        Getter for the chi.
        
        Returns:
            the chi
        
        
        """
        ...
    def getChi2(self) -> float:
        """
        Getter for the chi2.
        
        Returns:
            the chi2
        
        
        """
        ...
    def getCo2AB(self) -> float:
        """
        Get Co2AB = C / 2AB.
        
        Returns:
            the co2AB
        
        
        """
        ...
    def getGamma(self) -> float:
        """
        Get direction cosine γ for central body.
        
        Returns:
            γ
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
        Get the Keplerian mean motion.
        
        The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMuoa(self) -> float:
        """
        Get μ / a.
        
        Returns:
            the muoa
        
        
        """
        ...
    def getOoAB(self) -> float:
        """
        ooAB = 1 / (A * B).
        
        Returns:
            the ooAB
        
        
        """
        ...
    def getRoa(self) -> float:
        """
        Get roa = R / a.
        
        Returns:
            the roa
        
        
        """
        ...

class DSSTJ2SquaredClosedForm(DSSTForceModel):
    """
    Second order J2-squared force model.
    
    The force model implements a closed-form of the J2-squared perturbation. The full realization of the model is based on a gaussian quadrature. Even if it is very accurate, a gaussian quadrature is usually time consuming. A closed-form is less accurate than a gaussian quadrature, but faster.
    
    Since:
        12.0
    """
    def __init__(self, j2SquaredModel: J2SquaredModel, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Constructor.
        
        Parameters:
            j2SquaredModel (J2SquaredModel): model for second order terms
            provider (UnnormalizedSphericalHarmonicsProvider): gravity field to use
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt..
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt..
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters..
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model. .
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            attitudeProvider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms. .
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms. .
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

class DSSTJ2SquaredClosedFormContext(ForceModelContext):
    """
    This class is a container for the common parameters used in DSSTJ2SquaredClosedForm.
    
    It performs parameters initialization at each integration step for the second-order J2-squared contribution to the central body gravitational perturbation.
    
    Since:
        12.0
    """
    def __init__(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Simple constructor.
        
        Parameters:
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            provider (UnnormalizedSphericalHarmonicsProvider): provider for spherical harmonics
        
        
        """
        ...
    def getA4(self) -> float:
        """
        Get the semi major axis to the power 4.
        
        Returns:
            the semi major axis to the power 4
        
        
        """
        ...
    def getAlpha4(self) -> float:
        """
        Get the equatorial radius of the central body to the power 4.
        
        Returns:
            the equatorial radius of the central body to the power 4
        
        
        """
        ...
    def getC(self) -> float:
        """
        Get the cosine of the inclination.
        
        Returns:
            the cosine of the inclination
        
        
        """
        ...
    def getEta(self) -> float:
        """
        Get the eta value.
        
        Returns:
            sqrt(1 - e * e)
        
        
        """
        ...
    def getS2(self) -> float:
        """
        Get the sine of the inclination to the power 2.
        
        Returns:
            the sine of the inclination to the power 2
        
        
        """
        ...

class DSSTNewtonianAttraction(DSSTForceModel):
    """
    Force model for Newtonian central body attraction for the DSSTPropagator.
    
    Since:
        10.0
    """
    CENTRAL_ATTRACTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Name of the single parameter of this model: the central attraction coefficient.
    
    Also see:
        constant
    
    
    """
    def __init__(self, mu: float):
        """
        Simple constructor.
        
        Parameters:
            mu (double): central attraction coefficient (m^3/s^2)
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    def getMu(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the central attraction coefficient μ at specific date.
        
        Parameters:
            date (AbsoluteDate): date at which mu wants to be known
        
        Returns:
            mu central attraction coefficient (m³/s²)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, provider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            provider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

class DSSTNewtonianAttractionContext(ForceModelContext):
    """
    This class is a container for the common parameters used in DSSTNewtonianAttraction.
    
    It performs parameters initialization at each integration step for the central body attraction.
    
    Since:
        10.0
    """
    def __init__(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]):
        """
        Simple constructor.
        
        Parameters:
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters
        
        
        """
        ...
    def getGM(self) -> float:
        """
        Get standard gravitational parameter μ for the body in m³/s².
        
        Returns:
            gm
        
        
        """
        ...

class DSSTTesseral(DSSTForceModel):
    """
    Tesseral contribution to the central body gravitational perturbation.
    
    Only resonant tesserals are considered.
    """
    SHORT_PERIOD_PREFIX: typing.ClassVar[str] = ...
    """
    Name of the prefix for short period coefficients keys.
    
    Also see:
        constant
    
    
    """
    CM_COEFFICIENTS: typing.ClassVar[str] = ...
    """
    Identifier for cMm coefficients.
    
    Also see:
        constant
    
    
    """
    SM_COEFFICIENTS: typing.ClassVar[str] = ...
    """
    Identifier for sMm coefficients.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, centralBodyFrame: org.orekit.frames.Frame, centralBodyRotationRate: float, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, centralBodyFrame: org.orekit.frames.Frame, centralBodyRotationRate: float, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, maxDegreeTesseralSP: int, maxOrderTesseralSP: int, maxEccPowTesseralSP: int, maxFrequencyShortPeriodics: int, maxDegreeMdailyTesseralSP: int, maxOrderMdailyTesseralSP: int, maxEccPowMdailyTesseralSP: int): ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            spacecraftState (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            spacecraftState (FieldSpacecraftState<T> spacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            attitudeProvider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

class DSSTThirdBody(DSSTForceModel):
    """
    Third body attraction perturbation to the DSSTPropagator.
    """
    SHORT_PERIOD_PREFIX: typing.ClassVar[str] = ...
    """
    Name of the prefix for short period coefficients keys.
    
    Also see:
        constant
    
    
    """
    ATTRACTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Name of the single parameter of this model: the attraction coefficient.
    
    Also see:
        constant
    
    
    """
    MAX_POWER: typing.ClassVar[int] = ...
    """
    Max power for summation.
    
    Also see:
        constant
    
    
    """
    BIG_TRUNCATION_TOLERANCE: typing.ClassVar[float] = ...
    """
    Truncation tolerance for big, eccentric orbits.
    
    Also see:
        constant
    
    
    """
    SMALL_TRUNCATION_TOLERANCE: typing.ClassVar[float] = ...
    """
    Truncation tolerance for small orbits.
    
    Also see:
        constant
    
    
    """
    def __init__(self, body: org.orekit.bodies.CelestialBody, mu: float):
        """
        Complete constructor.
        
        Parameters:
            body (CelestialBody): the 3rd body to consider
            mu (double): central attraction coefficient (i.e., attraction coefficient of the central body, not the one of the 3rd body)
        
        Also see:
            CelestialBodies
        
        
        """
        ...
    def getBody(self) -> org.orekit.bodies.CelestialBody:
        """
        Get third body.
        
        Returns:
            third body
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, currentState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            currentState (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, currentState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            currentState (FieldSpacecraftState<T> currentState): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, provider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            provider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

class DSSTThirdBodyDynamicContext(ForceModelContext):
    """
    This class is a container for the common parameters used in DSSTThirdBody.
    
    It performs parameters initialization at each integration step for the third body attraction perturbation. These parameters change for each integration step.
    
    Since:
        11.3.3
    """
    def __init__(self, aux: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, body: org.orekit.bodies.CelestialBody, parameters: typing.Union[typing.List[float], jpype.JArray]):
        """
        Constructor.
        
        Parameters:
            aux (AuxiliaryElements): auxiliary elements related to the current orbit
            body (CelestialBody): body the 3rd body to consider
            parameters (double[]): values of the force model parameters
        
        
        """
        ...
    def getA(self) -> float:
        """
        Get A = sqrt(μ * a).
        
        Returns:
            A
        
        
        """
        ...
    def getAlpha(self) -> float:
        """
        Get direction cosine α for central body.
        
        Returns:
            α
        
        
        """
        ...
    def getBB(self) -> float:
        """
        Get B².
        
        Returns:
            B²
        
        
        """
        ...
    def getBBB(self) -> float:
        """
        Get B³.
        
        Returns:
            B³
        
        
        """
        ...
    def getBeta(self) -> float:
        """
        Get direction cosine β for central body.
        
        Returns:
            β
        
        
        """
        ...
    def getBoA(self) -> float:
        """
        Get B / A.
        
        Returns:
            BoA
        
        
        """
        ...
    def getBoABpo(self) -> float:
        """
        Get BoABpo = B / A(1 + B).
        
        Returns:
            BoABpo
        
        
        """
        ...
    def getGamma(self) -> float:
        """
        Get direction cosine γ for central body.
        
        Returns:
            γ
        
        
        """
        ...
    def getHXXX(self) -> float:
        """
        Get hXXX = h * Χ³.
        
        Returns:
            hXXX
        
        
        """
        ...
    def getKXXX(self) -> float:
        """
        Get kXXX = h * Χ³.
        
        Returns:
            kXXX
        
        
        """
        ...
    def getM2aoA(self) -> float:
        """
        Get m2aoA = -2 * a / A.
        
        Returns:
            m2aoA
        
        
        """
        ...
    def getMCo2AB(self) -> float:
        """
        Get mCo2AB = -C / 2AB.
        
        Returns:
            mCo2AB
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
        Get the Keplerian mean motion.
        
        The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMuoR3(self) -> float:
        """
        Get muoR3 = mu3 / R3.
        
        Returns:
            muoR3
        
        
        """
        ...
    def getOoAB(self) -> float:
        """
        Get ooAB = 1 / (A * B).
        
        Returns:
            ooAB
        
        
        """
        ...
    def getR3(self) -> float:
        """
        Get the distance from center of mass of the central body to the 3rd body.
        
        Returns:
            the distance from center of mass of the central body to the 3rd body
        
        
        """
        ...
    def getX(self) -> float:
        """
        Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
        Returns:
            Χ
        
        
        """
        ...
    def getXX(self) -> float:
        """
        Get Χ².
        
        Returns:
            Χ²
        
        
        """
        ...
    def getb(self) -> float:
        """
        Get b = 1 / (1 + sqrt(1 - e²)) = 1 / (1 + B).
        
        Returns:
            b
        
        
        """
        ...

class DSSTThirdBodyStaticContext(ForceModelContext):
    """
    This class is a container for the common parameters used in DSSTThirdBody.
    
    It performs parameters initialization at each integration step for the third body attraction perturbation. These parameters are initialize as soon as possible. In fact, they are initialized once with short period terms and don't evolve during propagation.
    
    Since:
        11.3.3
    """
    def __init__(self, aux: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, x: float, r3: float, parameters: typing.Union[typing.List[float], jpype.JArray]):
        """
        Constructor.
        
        Parameters:
            aux (AuxiliaryElements): auxiliary elements
            x (double): DSST Chi element
            r3 (double): distance from center of mass of the central body to the 3rd body
            parameters (double[]): force model parameters
        
        
        """
        ...
    def getMaxAR3Pow(self) -> int:
        """
        Get the value of max power for a/R3 in the serie expansion.
        
        Returns:
            maxAR3Pow
        
        
        """
        ...
    def getMaxEccPow(self) -> int:
        """
        Get the value of max power for e in the serie expansion.
        
        Returns:
            maxEccPow
        
        
        """
        ...
    def getMaxFreqF(self) -> int:
        """
        Get the value of max frequency of F.
        
        Returns:
            maxFreqF
        
        
        """
        ...

class DSSTZonal(DSSTForceModel):
    """
    Zonal contribution to the central body gravitational perturbation.
    """
    SHORT_PERIOD_PREFIX: typing.ClassVar[str] = ...
    """
    Name of the prefix for short period coefficients keys.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, maxDegreeShortPeriodics: int, maxEccPowShortPeriodics: int, maxFrequencyShortPeriodics: int): ...
    @typing.overload
    def __init__(self, bodyFixedFrame: org.orekit.frames.Frame, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, bodyFixedFrame: org.orekit.frames.Frame, provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, maxDegreeShortPeriodics: int, maxEccPowShortPeriodics: int, maxFrequencyShortPeriodics: int): ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            spacecraftState (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            spacecraftState (FieldSpacecraftState<T> spacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getProvider(self) -> org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider:
        """
        Get the spherical harmonics provider.
        
        Returns:
            the spherical harmonics provider
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            attitudeProvider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

_FieldAbstractGaussianContributionContext__T = typing.TypeVar('_FieldAbstractGaussianContributionContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractGaussianContributionContext(FieldForceModelContext[_FieldAbstractGaussianContributionContext__T], typing.Generic[_FieldAbstractGaussianContributionContext__T]):
    """
    This class is a container for the common "field" parameters used in AbstractGaussianContribution.
    
    It performs parameters initialization at each integration step for the Gaussian contributions
    
    Since:
        10.0
    """
    def getA(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get A = sqrt(μ * a).
        
        Returns:
            A
        
        
        """
        ...
    def getCo2AB(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get co2AB = C / 2AB.
        
        Returns:
            co2AB
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get the Keplerian mean motion.
        
        The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMu(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get central attraction coefficient.
        
        Returns:
            mu
        
        
        """
        ...
    def getOOA(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get ooA = 1 / A.
        
        Returns:
            ooA
        
        
        """
        ...
    def getOOAB(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get ooAB = 1 / (A * B).
        
        Returns:
            ooAB
        
        
        """
        ...
    def getOoBpo(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get ooBpo = 1 / (B + 1).
        
        Returns:
            ooBpo
        
        
        """
        ...
    def getOoMU(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get ooMu = 1 / mu.
        
        Returns:
            ooMu
        
        
        """
        ...
    def getTon2a(self) -> _FieldAbstractGaussianContributionContext__T:
        """
        Get ton2a = 2 / (n² * a).
        
        Returns:
            ton2a
        
        
        """
        ...

_FieldDSSTGravityContext__T = typing.TypeVar('_FieldDSSTGravityContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTGravityContext(FieldForceModelContext[_FieldDSSTGravityContext__T], typing.Generic[_FieldDSSTGravityContext__T]):
    """
    This class is a container for the common parameters used in DSSTTesseral and DSSTZonal.
    
    It performs parameters initialization at each integration step for the Tesseral and Zonal contribution to the central body gravitational perturbation.
    
    Since:
        12.2
    """
    def getA(self) -> _FieldDSSTGravityContext__T:
        """
        A = sqrt(μ * a).
        
        Returns:
            A
        
        
        """
        ...
    def getAlpha(self) -> _FieldDSSTGravityContext__T:
        """
        Get direction cosine α for central body.
        
        Returns:
            α
        
        
        """
        ...
    def getAx2oA(self) -> _FieldDSSTGravityContext__T:
        """
        Getter for the ax2oA.
        
        Returns:
            the ax2oA
        
        
        """
        ...
    def getBeta(self) -> _FieldDSSTGravityContext__T:
        """
        Get direction cosine β for central body.
        
        Returns:
            β
        
        
        """
        ...
    def getBoA(self) -> _FieldDSSTGravityContext__T:
        """
        Get B / A.
        
        Returns:
            BoA
        
        
        """
        ...
    def getBoABpo(self) -> _FieldDSSTGravityContext__T:
        """
        Get BoABpo = B / A(1 + B).
        
        Returns:
            BoABpo
        
        
        """
        ...
    def getBodyFixedToInertialTransform(self) -> org.orekit.frames.FieldStaticTransform[_FieldDSSTGravityContext__T]:
        """
        Getter for the bodyFixedToInertialTransform.
        
        Returns:
            the bodyFixedToInertialTransform
        
        
        """
        ...
    def getChi(self) -> _FieldDSSTGravityContext__T:
        """
        Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
        Returns:
            chi
        
        
        """
        ...
    def getChi2(self) -> _FieldDSSTGravityContext__T:
        """
        Get Χ².
        
        Returns:
            chi2
        
        
        """
        ...
    def getCo2AB(self) -> _FieldDSSTGravityContext__T:
        """
        Get Co2AB = C / 2AB.
        
        Returns:
            Co2AB
        
        
        """
        ...
    def getGamma(self) -> _FieldDSSTGravityContext__T:
        """
        Get direction cosine γ for central body.
        
        Returns:
            the γ
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldDSSTGravityContext__T:
        """
        Get the Keplerian mean motion.
        
        The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMuoa(self) -> _FieldDSSTGravityContext__T:
        """
        Get muoa = μ / a.
        
        Returns:
            the muoa
        
        
        """
        ...
    def getOoAB(self) -> _FieldDSSTGravityContext__T:
        """
        Get ooAB = 1 / (A * B).
        
        Returns:
            ooAB
        
        
        """
        ...
    def getRoa(self) -> _FieldDSSTGravityContext__T:
        """
        Get roa = R / a.
        
        Returns:
            roa
        
        
        """
        ...

_FieldDSSTJ2SquaredClosedFormContext__T = typing.TypeVar('_FieldDSSTJ2SquaredClosedFormContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTJ2SquaredClosedFormContext(FieldForceModelContext[_FieldDSSTJ2SquaredClosedFormContext__T], typing.Generic[_FieldDSSTJ2SquaredClosedFormContext__T]):
    """
    This class is a container for the common parameters used in DSSTJ2SquaredClosedForm.
    
    It performs parameters initialization at each integration step for the second-order J2-squared contribution to the central body gravitational perturbation.
    
    Since:
        12.0
    """
    def __init__(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_FieldDSSTJ2SquaredClosedFormContext__T], provider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider):
        """
        Simple constructor.
        
        Parameters:
            auxiliaryElements (FieldAuxiliaryElements<FieldDSSTJ2SquaredClosedFormContext> auxiliaryElements): auxiliary elements related to the current orbit
            provider (UnnormalizedSphericalHarmonicsProvider): provider for spherical harmonics
        
        
        """
        ...
    def getA4(self) -> _FieldDSSTJ2SquaredClosedFormContext__T:
        """
        Get the semi major axis to the power 4.
        
        Returns:
            the semi major axis to the power 4
        
        
        """
        ...
    def getAlpha4(self) -> float:
        """
        Get the equatorial radius of the central body to the power 4.
        
        Returns:
            the equatorial radius of the central body to the power 4
        
        
        """
        ...
    def getC(self) -> _FieldDSSTJ2SquaredClosedFormContext__T:
        """
        Get the cosine of the inclination.
        
        Returns:
            the cosine of the inclination
        
        
        """
        ...
    def getEta(self) -> _FieldDSSTJ2SquaredClosedFormContext__T:
        """
        Get the eta value.
        
        Returns:
            sqrt(1 - e * e)
        
        
        """
        ...
    def getS2(self) -> _FieldDSSTJ2SquaredClosedFormContext__T:
        """
        Get the sine of the inclination to the power 2.
        
        Returns:
            the sine of the inclination to the power 2
        
        
        """
        ...

_FieldDSSTNewtonianAttractionContext__T = typing.TypeVar('_FieldDSSTNewtonianAttractionContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTNewtonianAttractionContext(FieldForceModelContext[_FieldDSSTNewtonianAttractionContext__T], typing.Generic[_FieldDSSTNewtonianAttractionContext__T]):
    """
    This class is a container for the common "field" parameters used in DSSTNewtonianAttraction.
    
    It performs parameters initialization at each integration step for the central body attraction.
    
    Since:
        10.0
    """
    def getGM(self) -> _FieldDSSTNewtonianAttractionContext__T:
        """
        Get standard gravitational parameter μ for the body in m³/s².
        
        Returns:
            gm
        
        
        """
        ...

_FieldDSSTThirdBodyDynamicContext__T = typing.TypeVar('_FieldDSSTThirdBodyDynamicContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTThirdBodyDynamicContext(FieldForceModelContext[_FieldDSSTThirdBodyDynamicContext__T], typing.Generic[_FieldDSSTThirdBodyDynamicContext__T]):
    """
    This class is a container for the common "field" parameters used in DSSTThirdBody.
    
    It performs parameters initialization at each integration step for the third body attraction perturbation. These parameters change for each integration step.
    
    Since:
        12.0
    """
    def __init__(self, aux: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_FieldDSSTThirdBodyDynamicContext__T], body: org.orekit.bodies.CelestialBody, parameters: typing.Union[typing.List[_FieldDSSTThirdBodyDynamicContext__T], jpype.JArray]):
        """
        Constructor.
        
        Parameters:
            aux (FieldAuxiliaryElements<FieldDSSTThirdBodyDynamicContext> aux): auxiliary elements related to the current orbit
            body (CelestialBody): body the 3rd body to consider
            parameters (FieldDSSTThirdBodyDynamicContext[]): values of the force model parameters
        
        
        """
        ...
    def getA(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get A = sqrt(μ * a).
        
        Returns:
            A
        
        
        """
        ...
    def getAlpha(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get direction cosine α for central body.
        
        Returns:
            α
        
        
        """
        ...
    def getBB(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get B².
        
        Returns:
            B²
        
        
        """
        ...
    def getBBB(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get B³.
        
        Returns:
            B³
        
        
        """
        ...
    def getBeta(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get direction cosine β for central body.
        
        Returns:
            β
        
        
        """
        ...
    def getBoA(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get B / A.
        
        Returns:
            BoA
        
        
        """
        ...
    def getBoABpo(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get BoABpo = B / A(1 + B).
        
        Returns:
            BoABpo
        
        
        """
        ...
    def getGamma(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get direction cosine γ for central body.
        
        Returns:
            γ
        
        
        """
        ...
    def getHXXX(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get hXXX = h * Χ³.
        
        Returns:
            hXXX
        
        
        """
        ...
    def getKXXX(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get kXXX = h * Χ³.
        
        Returns:
            kXXX
        
        
        """
        ...
    def getM2aoA(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get m2aoA = -2 * a / A.
        
        Returns:
            m2aoA
        
        
        """
        ...
    def getMCo2AB(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get mCo2AB = -C / 2AB.
        
        Returns:
            mCo2AB
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get the Keplerian mean motion.
        
        The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMuoR3(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get muoR3 = mu3 / R3.
        
        Returns:
            muoR3
        
        
        """
        ...
    def getOoAB(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get ooAB = 1 / (A * B).
        
        Returns:
            ooAB
        
        
        """
        ...
    def getR3(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get the distance from center of mass of the central body to the 3rd body.
        
        Returns:
            the distance from center of mass of the central body to the 3rd body
        
        
        """
        ...
    def getX(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
        Returns:
            Χ
        
        
        """
        ...
    def getXX(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get Χ².
        
        Returns:
            Χ²
        
        
        """
        ...
    def getb(self) -> _FieldDSSTThirdBodyDynamicContext__T:
        """
        Get b = 1 / (1 + sqrt(1 - e²)) = 1 / (1 + B).
        
        Returns:
            b
        
        
        """
        ...

class PythonDSSTForceModel(DSSTForceModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, parameters: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
            parameters (double[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model.
        
        Returns:
            the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, state: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], parameters: typing.Union[typing.List[_getMeanElementRate_1__T], jpype.JArray]) -> typing.MutableSequence[_getMeanElementRate_1__T]:
        """
        Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
        Specified by: getMeanElementRate in interface DSSTForceModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
            parameters (T[]): values of the force model parameters at state date (only 1 span for each parameter driver) obtained for example by
                calling getParameters on force model or
                getParametersAtStateDate on gradient converter.
        
        Returns:
            the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[float], jpype.JArray]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], type: org.orekit.propagation.PropagationType, parameters: typing.Union[typing.List[_initializeShortPeriodTerms_1__T], jpype.JArray]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
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
    def registerAttitudeProvider(self, provider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
        Register an attitude provider.
        
        Register an attitude provider that can be used by the force model.
        
        Specified by: registerAttitudeProvider in interface DSSTForceModel
        
        Parameters:
            provider (AttitudeProvider): the AttitudeProvider
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[float], jpype.JArray], *meanStates: org.orekit.propagation.SpacecraftState) -> None:
        """
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (double[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model. The extract parameter method
                extractParameters is called in the method to
                select the right parameter corresponding to the mean state date.
            meanStates (SpacecraftState...): mean states information: date, kinematics, attitude
        
        public <T extends CalculusFieldElement<T>> void updateShortPeriodTerms (T[] parameters, FieldSpacecraftState<T>... meanStates)
        
        Update the short period terms.
        
        The ShortPeriodTerms that will be updated are the ones that were returned during the call to initializeShortPeriodTerms.
        
        Specified by: updateShortPeriodTerms in interface DSSTForceModel
        
        Parameters:
            parameters (T[]): values of the force model parameters (all span values for each parameters) obtained for example by calling
                getParametersAllValues on force model or
                getParameters on gradient converter. The extract
                parameter method extractParameters is called
                in the method to select the right parameter.
            meanStates (FieldSpacecraftState<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, parameters: typing.Union[typing.List[_updateShortPeriodTerms_1__T], jpype.JArray], *meanStates: org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]) -> None: ...

_PythonFieldShortPeriodTerms__T = typing.TypeVar('_PythonFieldShortPeriodTerms__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldShortPeriodTerms(FieldShortPeriodTerms[_PythonFieldShortPeriodTerms__T], typing.Generic[_PythonFieldShortPeriodTerms__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCoefficients(self, date: org.orekit.time.FieldAbsoluteDate[_PythonFieldShortPeriodTerms__T], selected: java.util.Set[str]) -> java.util.Map[str, typing.MutableSequence[_PythonFieldShortPeriodTerms__T]]:
        """
        Computes the coefficients involved in the contributions.
        
        This method is intended mainly for validation purposes. Its output is highly dependent on the implementation details in each force model and may change from version to version. It is not recommended to use it for any operational purposes.
        
        Specified by: getCoefficients in interface FieldShortPeriodTerms
        
        Parameters:
            date (FieldAbsoluteDate<PythonFieldShortPeriodTerms> date): current date
            selected (Set<String> selected): set of coefficients that should be put in the map (empty set means all coefficients are selected)
        
        Returns:
            the selected coefficients of the short periodic variations, in a map where all keys start with
            getCoefficientsKeyPrefix
        
        
        """
        ...
    def getCoefficientsKeyPrefix(self) -> str:
        """
        Get the prefix for short period coefficients keys.
        
        This prefix is used to identify the coefficients of the current force model from the coefficients pertaining to other force models. All the keys in the map returned by getCoefficients start with this prefix, which must be unique among all providers.
        
        Specified by: getCoefficientsKeyPrefix in interface FieldShortPeriodTerms
        
        Returns:
            the prefix for short periodic coefficients keys
        
        Also see:
            getCoefficients
        
        
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
    def value(self, meanOrbit: org.orekit.orbits.FieldOrbit[_PythonFieldShortPeriodTerms__T]) -> typing.MutableSequence[_PythonFieldShortPeriodTerms__T]:
        """
        Evaluate the contributions of the short period terms.
        
        Specified by: value in interface FieldShortPeriodTerms
        
        Parameters:
            meanOrbit (FieldOrbit<PythonFieldShortPeriodTerms> meanOrbit): mean orbit to which the short period contribution applies
        
        Returns:
            short period terms contributions
        
        
        """
        ...

class PythonForceModelContext(ForceModelContext):
    def __init__(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements):
        """
        Simple constructor.
        
        Parameters:
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonJ2SquaredModel(J2SquaredModel):
    def __init__(self): ...
    _computeMeanEquinoctialSecondOrderTerms_1__T = typing.TypeVar('_computeMeanEquinoctialSecondOrderTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeMeanEquinoctialSecondOrderTerms(self, context: DSSTJ2SquaredClosedFormContext) -> typing.MutableSequence[float]:
        """
        Description copied from interface: computeMeanEquinoctialSecondOrderTerms Compute the J2-squared second-order terms in equinoctial elements.
        
        Specified by: computeMeanEquinoctialSecondOrderTerms in interface J2SquaredModel
        
        Parameters:
            context (DSSTJ2SquaredClosedFormContext): model context
        
        Returns:
            the J2-squared second-order terms in equinoctial elements. Order must follow: [A, K, H, Q, P, M]
        
        """
        ...
    @typing.overload
    def computeMeanEquinoctialSecondOrderTerms(self, context: FieldDSSTJ2SquaredClosedFormContext[_computeMeanEquinoctialSecondOrderTerms_1__T]) -> typing.MutableSequence[_computeMeanEquinoctialSecondOrderTerms_1__T]:
        """
        Description copied from interface: computeMeanEquinoctialSecondOrderTerms Compute the J2-squared second-order terms in equinoctial elements.
        
        Specified by: computeMeanEquinoctialSecondOrderTerms in interface J2SquaredModel
        
        Parameters:
            context (FieldDSSTJ2SquaredClosedFormContext<T> context): model context
        
        Returns:
            the J2-squared second-order terms in equinoctial elements. Order must follow: [A, K, H, Q, P, M]
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonShortPeriodTerms(ShortPeriodTerms):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getCoefficients(self, date: org.orekit.time.AbsoluteDate, selected: java.util.Set[str]) -> java.util.Map[str, typing.MutableSequence[float]]:
        """
        Computes the coefficients involved in the contributions.
        
        This method is intended mainly for validation purposes. Its output is highly dependent on the implementation details in each force model and may change from version to version. It is not recommended to use it for any operational purposes.
        
        Specified by: getCoefficients in interface ShortPeriodTerms
        
        Parameters:
            date (AbsoluteDate): current date
            selected (Set<String> selected): set of coefficients that should be put in the map (empty set means all coefficients are selected)
        
        Returns:
            the selected coefficients of the short periodic variations, in a map where all keys start with
            getCoefficientsKeyPrefix
        
        
        """
        ...
    def getCoefficientsKeyPrefix(self) -> str:
        """
        Get the prefix for short period coefficients keys.
        
        This prefix is used to identify the coefficients of the current force model from the coefficients pertaining to other force models. All the keys in the map returned by getCoefficients start with this prefix, which must be unique among all providers.
        
        Specified by: getCoefficientsKeyPrefix in interface ShortPeriodTerms
        
        Returns:
            the prefix for short periodic coefficients keys
        
        Also see:
            getCoefficients
        
        
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
    def value(self, meanOrbit: org.orekit.orbits.Orbit) -> typing.MutableSequence[float]:
        """
        Evaluate the contributions of the short period terms.
        
        Specified by: value in interface ShortPeriodTerms
        
        Parameters:
            meanOrbit (Orbit): mean orbit to which the short period contribution applies
        
        Returns:
            short period terms contributions
        
        
        """
        ...

class ZeisModel(J2SquaredModel):
    """
    Zeis model for J2-squared second-order terms.
    
    Since:
        12.0
    
    Also see:
        "ZEIS, Eric and CEFOLA, P. Computerized algebraic utilities for the construction of nonsingular satellite theories.
        Journal of Guidance and Control, 1980, vol. 3, no 1, p. 48-54.", "SAN-JUAN, Juan F., LÓPEZ, Rosario, et CEFOLA, Paul J.
        A Second-Order Closed-Form $$ J_2 $$ Model for the Draper Semi-Analytical Satellite Theory. The Journal of the
        Astronautical Sciences, 2022, p. 1-27."
    """
    def __init__(self):
        """
        Constructor.
        """
        ...
    _computeC2Z_1__T = typing.TypeVar('_computeC2Z_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeC2Z(self, context: DSSTJ2SquaredClosedFormContext) -> float:
        """
        Get the value of the Zeis constant.
        
        Parameters:
            context (DSSTJ2SquaredClosedFormContext): model context
        
        Returns:
            the value of the Zeis constant
        
        """
        ...
    @typing.overload
    def computeC2Z(self, context: FieldDSSTJ2SquaredClosedFormContext[_computeC2Z_1__T]) -> _computeC2Z_1__T:
        """
        Get the value of the Zeis constant.
        
        Parameters:
            context (FieldDSSTJ2SquaredClosedFormContext<T> context): model context
        
        Returns:
            the value of the Zeis constant
        
        
        """
        ...
    _computeMeanEquinoctialSecondOrderTerms_1__T = typing.TypeVar('_computeMeanEquinoctialSecondOrderTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeMeanEquinoctialSecondOrderTerms(self, context: DSSTJ2SquaredClosedFormContext) -> typing.MutableSequence[float]:
        """
        Compute the J2-squared second-order terms in equinoctial elements..
        
        Specified by: computeMeanEquinoctialSecondOrderTerms in interface J2SquaredModel
        
        Parameters:
            context (DSSTJ2SquaredClosedFormContext): model context
        
        Returns:
            the J2-squared second-order terms in equinoctial elements. Order must follow: [A, K, H, Q, P, M]
        
        """
        ...
    @typing.overload
    def computeMeanEquinoctialSecondOrderTerms(self, context: FieldDSSTJ2SquaredClosedFormContext[_computeMeanEquinoctialSecondOrderTerms_1__T]) -> typing.MutableSequence[_computeMeanEquinoctialSecondOrderTerms_1__T]:
        """
        Compute the J2-squared second-order terms in equinoctial elements..
        
        Specified by: computeMeanEquinoctialSecondOrderTerms in interface J2SquaredModel
        
        Parameters:
            context (FieldDSSTJ2SquaredClosedFormContext<T> context): model context
        
        Returns:
            the J2-squared second-order terms in equinoctial elements. Order must follow: [A, K, H, Q, P, M]
        
        
        """
        ...

class DSSTAtmosphericDrag(AbstractGaussianContribution):
    """
    Atmospheric drag contribution to the DSSTPropagator.
    
    The drag acceleration is computed through the acceleration model of DragForce.
    """
    @typing.overload
    def __init__(self, force: org.orekit.forces.drag.DragForce, mu: float): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, cd: float, area: float, mu: float): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, spacecraft: org.orekit.forces.drag.DragSensitive, mu: float): ...
    def getAtmosphere(self) -> org.orekit.models.earth.atmosphere.Atmosphere:
        """
        Get the atmospheric model.
        
        Returns:
            atmosphere model
        
        
        """
        ...
    def getDrag(self) -> org.orekit.forces.drag.DragForce:
        """
        Get drag force.
        
        Returns:
            drag force
        
        
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
    def getRbar(self) -> float:
        """
        Get the critical distance.
        
        The critical distance from the center of the central body aims at defining the atmosphere entry/exit.
        
        Returns:
            the critical distance from the center of the central body (m)
        
        
        """
        ...
    def getSpacecraft(self) -> org.orekit.forces.drag.DragSensitive:
        """
        Get spacecraft shape.
        
        Returns:
            spacecraft shape
        
        
        """
        ...
    def setRbar(self, rbar: float) -> None:
        """
        Set the critical distance from the center of the central body at which the atmosphere is considered to end, i.e. beyond this distance atmospheric drag is not considered.
        
        Parameters:
            rbar (double): the critical distance from the center of the central body (m)
        
        
        """
        ...

class DSSTSolarRadiationPressure(AbstractGaussianContribution):
    """
    Solar radiation pressure contribution to the DSSTPropagator.
    
    The solar radiation pressure acceleration is computed through the acceleration model of SolarRadiationPressure.
    """
    @typing.overload
    def __init__(self, dRef: float, pRef: float, cr: float, area: float, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], centralBody: org.orekit.bodies.OneAxisEllipsoid, mu: float): ...
    @typing.overload
    def __init__(self, cr: float, area: float, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], centralBody: org.orekit.bodies.OneAxisEllipsoid, mu: float): ...
    @typing.overload
    def __init__(self, dRef: float, pRef: float, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], centralBody: org.orekit.bodies.OneAxisEllipsoid, spacecraft: org.orekit.forces.radiation.RadiationSensitive, mu: float): ...
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], centralBody: org.orekit.bodies.OneAxisEllipsoid, spacecraft: org.orekit.forces.radiation.RadiationSensitive, mu: float): ...
    def getEquatorialRadius(self) -> float:
        """
        Get the central body equatorial radius.
        
        Returns:
            central body equatorial radius (m)
        
        
        """
        ...
    def getSpacecraft(self) -> org.orekit.forces.radiation.RadiationSensitive:
        """
        Get spacecraft shape.
        
        Returns:
            the spacecraft shape.
        
        
        """
        ...

class DSSTTesseralContext(DSSTGravityContext):
    """
    This class is a container for the common parameters used in DSSTTesseral.
    
    It performs parameters initialization at each integration step for the Tesseral contribution to the central body gravitational perturbation.
    
    Since:
        10.0
    """
    def getE2(self) -> float:
        """
        Get ecc².
        
        Returns:
            e2
        
        
        """
        ...
    def getOrbitPeriod(self) -> float:
        """
        Get the Keplerian period.
        
        The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian period in seconds, or positive infinity for hyperbolic orbits
        
        
        """
        ...
    def getRatio(self) -> float:
        """
        Get the ratio of satellite period to central body rotation period.
        
        Returns:
            ratio
        
        
        """
        ...
    def getTheta(self) -> float:
        """
        Get Central body rotation angle θ.
        
        Returns:
            theta
        
        
        """
        ...

class DSSTZonalContext(DSSTGravityContext):
    """
    This class is a container for the common parameters used in DSSTZonal.
    
    It performs parameters initialization at each integration step for the Zonal contribution to the central body gravitational perturbation.
    
    Since:
        10.0
    """
    def getBB(self) -> float:
        """
        Get B * B.
        
        Returns:
            BB
        
        
        """
        ...
    def getCXO2N2A2(self) -> float:
        """
        Get (C * χ) / ( 2 * n² * a² ).
        
        Returns:
            cxo2n2a2
        
        
        """
        ...
    def getChi3(self) -> float:
        """
        Getter for the Χ³.
        
        Returns:
            the Χ³
        
        
        """
        ...
    def getHK(self) -> float:
        """
        Get h * k.
        
        Returns:
            hk
        
        
        """
        ...
    def getK2MH2(self) -> float:
        """
        Get k² - h².
        
        Returns:
            k2mh2
        
        
        """
        ...
    def getK2MH2O2(self) -> float:
        """
        Get (k² - h²) / 2.
        
        Returns:
            k2mh2o2
        
        
        """
        ...
    def getOON2A2(self) -> float:
        """
        Get 1 / (n² * a²).
        
        Returns:
            oon2a2
        
        
        """
        ...
    def getX2ON2A2XP1(self) -> float:
        """
        Get (χ²) / (n² * a² * (χ + 1 ) ).
        
        Returns:
            x2on2a2xp1
        
        
        """
        ...
    def getX3ON2A(self) -> float:
        """
        Get χ³ / (n² * a).
        
        Returns:
            x3on2a
        
        
        """
        ...
    def getXON2A2(self) -> float:
        """
        Get χ / (n² * a²).
        
        Returns:
            xon2a2
        
        
        """
        ...

_FieldDSSTTesseralContext__T = typing.TypeVar('_FieldDSSTTesseralContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTTesseralContext(FieldDSSTGravityContext[_FieldDSSTTesseralContext__T], typing.Generic[_FieldDSSTTesseralContext__T]):
    """
    This class is a container for the common "field" parameters used in DSSTTesseral.
    
    It performs parameters initialization at each integration step for the Tesseral contribution to the central body gravitational perturbation.
    
    Since:
        10.0
    """
    def getE2(self) -> _FieldDSSTTesseralContext__T:
        """
        Get ecc².
        
        Returns:
            e2
        
        
        """
        ...
    def getMoa(self) -> _FieldDSSTTesseralContext__T:
        """
        Deprecated. since 12.2 Use getMuoa() instead Get μ / a .
        
        Returns:
            moa
        
        
        """
        ...
    def getOrbitPeriod(self) -> _FieldDSSTTesseralContext__T:
        """
        Get the Keplerian period.
        
        The Keplerian period is computed directly from semi major axis and central acceleration constant.
        
        Returns:
            Keplerian period in seconds, or positive infinity for hyperbolic orbits
        
        
        """
        ...
    def getRatio(self) -> _FieldDSSTTesseralContext__T:
        """
        Get the ratio of satellite period to central body rotation period.
        
        Returns:
            ratio
        
        
        """
        ...
    def getTheta(self) -> _FieldDSSTTesseralContext__T:
        """
        Get Central body rotation angle θ.
        
        Returns:
            theta
        
        
        """
        ...

_FieldDSSTZonalContext__T = typing.TypeVar('_FieldDSSTZonalContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTZonalContext(FieldDSSTGravityContext[_FieldDSSTZonalContext__T], typing.Generic[_FieldDSSTZonalContext__T]):
    """
    This class is a container for the common "field" parameters used in DSSTZonal.
    
    It performs parameters initialization at each integration step for the Zonal contribution to the central body gravitational perturbation.
    
    Since:
        10.0
    """
    def getBB(self) -> _FieldDSSTZonalContext__T:
        """
        Get B * B.
        
        Returns:
            BB
        
        
        """
        ...
    def getCXO2N2A2(self) -> _FieldDSSTZonalContext__T:
        """
        Get (C * χ) / ( 2 * n² * a² ).
        
        Returns:
            cxo2n2a2
        
        
        """
        ...
    def getChi3(self) -> _FieldDSSTZonalContext__T:
        """
        Getter for the Χ³.
        
        Returns:
            the Χ³
        
        
        """
        ...
    def getHK(self) -> _FieldDSSTZonalContext__T:
        """
        Get h * k.
        
        Returns:
            hk
        
        
        """
        ...
    def getK2MH2(self) -> _FieldDSSTZonalContext__T:
        """
        Get k² - h².
        
        Returns:
            k2mh2
        
        
        """
        ...
    def getK2MH2O2(self) -> _FieldDSSTZonalContext__T:
        """
        Get (k² - h²) / 2.
        
        Returns:
            k2mh2o2
        
        
        """
        ...
    def getOON2A2(self) -> _FieldDSSTZonalContext__T:
        """
        Get 1 / (n² * a²).
        
        Returns:
            oon2a2
        
        
        """
        ...
    def getX2ON2A2XP1(self) -> _FieldDSSTZonalContext__T:
        """
        Get (χ²) / (n² * a² * (χ + 1 ) ).
        
        Returns:
            x2on2a2xp1
        
        
        """
        ...
    def getX3ON2A(self) -> _FieldDSSTZonalContext__T:
        """
        Get χ³ / (n² * a).
        
        Returns:
            x3on2a
        
        
        """
        ...
    def getXON2A2(self) -> _FieldDSSTZonalContext__T:
        """
        Get χ / (n² * a²).
        
        Returns:
            xon2a2
        
        
        """
        ...

class PythonAbstractGaussianContribution(AbstractGaussianContribution):
    def __init__(self, coefficientsKeyPrefix: str, threshold: float, contribution: org.orekit.forces.ForceModel, mu: float):
        """
        Build a new instance.
        
        Parameters:
            coefficientsKeyPrefix (String): prefix for coefficients keys
            threshold (double): tolerance for the choice of the Gauss quadrature order
            contribution (ForceModel): the ForceModel to be numerically averaged
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getLLimits_1__T = typing.TypeVar('_getLLimits_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLLimits(self, state: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements) -> typing.MutableSequence[float]:
        """
        Compute the limits in L, the true longitude, for integration.
        
        Specified by: getLLimits in class AbstractGaussianContribution
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            auxiliaryElements (AuxiliaryElements): auxiliary elements related to the current orbit
        
        Returns:
            the integration limits in L
        
        """
        ...
    @typing.overload
    def getLLimits(self, state: org.orekit.propagation.FieldSpacecraftState[_getLLimits_1__T], auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getLLimits_1__T]) -> typing.MutableSequence[_getLLimits_1__T]:
        """
        Compute the limits in L, the true longitude, for integration.
        
        Specified by: getLLimits in class AbstractGaussianContribution
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            auxiliaryElements (FieldAuxiliaryElements<T> auxiliaryElements): auxiliary elements related to the current orbit
        
        Returns:
            the integration limits in L
        
        
        """
        ...
    def getParametersDriversWithoutMu(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for force model parameters except the one for the central attraction coefficient.
        
        The driver for central attraction coefficient is automatically added at the last element of the ParameterDriver array into getParametersDrivers method.
        
        Specified by: meth:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution.getParametersDriversWithoutMu` in class AbstractGaussianContribution
        
        Returns:
            drivers for force model parameters
        
        
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
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst.forces")``.

    AbstractGaussianContribution: typing.Type[AbstractGaussianContribution]
    AbstractGaussianContributionContext: typing.Type[AbstractGaussianContributionContext]
    DSSTAtmosphericDrag: typing.Type[DSSTAtmosphericDrag]
    DSSTForceModel: typing.Type[DSSTForceModel]
    DSSTGravityContext: typing.Type[DSSTGravityContext]
    DSSTJ2SquaredClosedForm: typing.Type[DSSTJ2SquaredClosedForm]
    DSSTJ2SquaredClosedFormContext: typing.Type[DSSTJ2SquaredClosedFormContext]
    DSSTNewtonianAttraction: typing.Type[DSSTNewtonianAttraction]
    DSSTNewtonianAttractionContext: typing.Type[DSSTNewtonianAttractionContext]
    DSSTSolarRadiationPressure: typing.Type[DSSTSolarRadiationPressure]
    DSSTTesseral: typing.Type[DSSTTesseral]
    DSSTTesseralContext: typing.Type[DSSTTesseralContext]
    DSSTThirdBody: typing.Type[DSSTThirdBody]
    DSSTThirdBodyDynamicContext: typing.Type[DSSTThirdBodyDynamicContext]
    DSSTThirdBodyStaticContext: typing.Type[DSSTThirdBodyStaticContext]
    DSSTZonal: typing.Type[DSSTZonal]
    DSSTZonalContext: typing.Type[DSSTZonalContext]
    FieldAbstractGaussianContributionContext: typing.Type[FieldAbstractGaussianContributionContext]
    FieldDSSTGravityContext: typing.Type[FieldDSSTGravityContext]
    FieldDSSTJ2SquaredClosedFormContext: typing.Type[FieldDSSTJ2SquaredClosedFormContext]
    FieldDSSTNewtonianAttractionContext: typing.Type[FieldDSSTNewtonianAttractionContext]
    FieldDSSTTesseralContext: typing.Type[FieldDSSTTesseralContext]
    FieldDSSTThirdBodyDynamicContext: typing.Type[FieldDSSTThirdBodyDynamicContext]
    FieldDSSTZonalContext: typing.Type[FieldDSSTZonalContext]
    FieldForceModelContext: typing.Type[FieldForceModelContext]
    FieldShortPeriodTerms: typing.Type[FieldShortPeriodTerms]
    ForceModelContext: typing.Type[ForceModelContext]
    J2SquaredModel: typing.Type[J2SquaredModel]
    PythonAbstractGaussianContribution: typing.Type[PythonAbstractGaussianContribution]
    PythonDSSTForceModel: typing.Type[PythonDSSTForceModel]
    PythonFieldShortPeriodTerms: typing.Type[PythonFieldShortPeriodTerms]
    PythonForceModelContext: typing.Type[PythonForceModelContext]
    PythonJ2SquaredModel: typing.Type[PythonJ2SquaredModel]
    PythonShortPeriodTerms: typing.Type[PythonShortPeriodTerms]
    ShortPeriodTerms: typing.Type[ShortPeriodTerms]
    ZeisModel: typing.Type[ZeisModel]
