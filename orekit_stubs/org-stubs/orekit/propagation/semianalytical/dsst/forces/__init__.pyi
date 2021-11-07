import java.util
import org.hipparchus
import org.orekit.attitudes
import org.orekit.bodies
import org.orekit.forces.drag
import org.orekit.forces.gravity.potential
import org.orekit.forces.radiation
import org.orekit.frames
import org.orekit.models.earth.atmosphere
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.propagation.semianalytical.dsst.forces.class-use
import org.orekit.propagation.semianalytical.dsst.utilities
import org.orekit.time
import org.orekit.utils
import typing



class DSSTForceModel:
    """
    public interface DSSTForceModel
    
        This interface represents a force modifying spacecraft motion for a
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        Objects implementing this interface are intended to be added to a
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator` before the propagation is started.
    
        The propagator will call at the very beginning of a propagation the
        :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms` method allowing
        preliminary computation such as truncation if needed.
    
        Then the propagator will call at each step:
    
          1.  the :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` method. The force model
            instance will extract all the state data needed to compute the mean element rates that contribute to the mean state
            derivative.
          2.  the :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` method, if
            osculating parameters are desired, on a sample of points within the last step.
    """
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements`): auxiliary elements related to the current orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], tArray: typing.List[_getMeanElementRate_1__T]) -> typing.List[_getMeanElementRate_1__T]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements`<T> auxiliaryElements): auxiliary elements related to the current orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        
        """
        ...
    _getParameters_1__T = typing.TypeVar('_getParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getParameters(self) -> typing.List[float]:
        """
            Get force model parameters.
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        """
        ...
    @typing.overload
    def getParameters(self, field: org.hipparchus.Field[_getParameters_1__T]) -> typing.List[_getParameters_1__T]:
        """
            Get force model parameters.
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field to which the elements belong
        
            Returns:
                force model parameters
        
            Since:
                9.0
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation.
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
            Since:
                11.0
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, propagationType: org.orekit.propagation.PropagationType, doubleArray: typing.List[float]) -> java.util.List['ShortPeriodTerms']: ...
    @typing.overload
    def initializeShortPeriodTerms(self, fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], propagationType: org.orekit.propagation.PropagationType, tArray: typing.List[_initializeShortPeriodTerms_1__T]) -> java.util.List['FieldShortPeriodTerms'[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Register an attitude provider.
        
            Register an attitude provider that can be used by the force model.
        
            Parameters:
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): the :class:`~org.orekit.attitudes.AttitudeProvider`
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, doubleArray: typing.List[float], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Parameters:
                parameters (double[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.SpacecraftState`...): mean states information: date, kinematics, attitude
        
        <T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void updateShortPeriodTerms(T[] parameters, :class:`~org.orekit.propagation.FieldSpacecraftState`<T>... meanStates)
        
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Parameters:
                parameters (T[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.FieldSpacecraftState`<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, tArray: typing.List[_updateShortPeriodTerms_1__T], fieldSpacecraftStateArray: typing.List[org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]]) -> None: ...

_FieldForceModelContext__T = typing.TypeVar('_FieldForceModelContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldForceModelContext(typing.Generic[_FieldForceModelContext__T]):
    """
    public abstract class FieldForceModelContext<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for dsst force models parameter containers.
    
        Since:
            10.0
    """
    def getFieldAuxiliaryElements(self) -> org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_FieldForceModelContext__T]: ...

_FieldShortPeriodTerms__T = typing.TypeVar('_FieldShortPeriodTerms__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldShortPeriodTerms(typing.Generic[_FieldShortPeriodTerms__T]):
    """
    public interface FieldShortPeriodTerms<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        Additive short period terms contributing to the mean to osculating orbit mapping.
    
        Each instance contains a set of several terms that are computed together.
    
        Also see:
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    """
    def getCoefficients(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldShortPeriodTerms__T], set: java.util.Set[str]) -> java.util.Map[str, typing.List[_FieldShortPeriodTerms__T]]: ...
    def getCoefficientsKeyPrefix(self) -> str:
        """
            Get the prefix for short period coefficients keys.
        
            This prefix is used to identify the coefficients of the current force model from the coefficients pertaining to other
            force models. All the keys in the map returned by
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.FieldShortPeriodTerms.getCoefficients` start with this prefix,
            which must be unique among all providers.
        
            Returns:
                the prefix for short periodic coefficients keys
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.FieldShortPeriodTerms.getCoefficients`
        
        
        """
        ...
    def value(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldShortPeriodTerms__T]) -> typing.List[_FieldShortPeriodTerms__T]: ...

class ForceModelContext:
    """
    public abstract class ForceModelContext extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Base class for dsst force models attributes containers.
    
        Since:
            10.0
    """
    def getAuxiliaryElements(self) -> org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements:
        """
            Method to get the auxiliary elements related to the
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.ForceModelContext`.
        
            Returns:
                auxiliary elements
        
        
        """
        ...

class ShortPeriodTerms:
    """
    public interface ShortPeriodTerms
    
        Additive short period terms contributing to the mean to osculating orbit mapping.
    
        Each instance contains a set of several terms that are computed together.
    
        Since:
            7.1
    
        Also see:
            :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    """
    def getCoefficients(self, absoluteDate: org.orekit.time.AbsoluteDate, set: java.util.Set[str]) -> java.util.Map[str, typing.List[float]]: ...
    def getCoefficientsKeyPrefix(self) -> str:
        """
            Get the prefix for short period coefficients keys.
        
            This prefix is used to identify the coefficients of the current force model from the coefficients pertaining to other
            force models. All the keys in the map returned by
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms.getCoefficients` start with this prefix,
            which must be unique among all providers.
        
            Returns:
                the prefix for short periodic coefficients keys
        
            Also see:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms.getCoefficients`
        
        
        """
        ...
    def value(self, orbit: org.orekit.orbits.Orbit) -> typing.List[float]:
        """
            Evaluate the contributions of the short period terms.
        
            Parameters:
                meanOrbit (:class:`~org.orekit.orbits.Orbit`): mean orbit to which the short period contribution applies
        
            Returns:
                short period terms contributions
        
        
        """
        ...

class AbstractGaussianContribution(DSSTForceModel):
    """
    public abstract class AbstractGaussianContribution extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    
        Common handling of :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel` methods for Gaussian
        contributions to DSST propagation.
    
        This abstract class allows to provide easily a subset of
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel` methods for specific Gaussian contributions.
    
        This class implements the notion of numerical averaging of the DSST theory. Numerical averaging is mainly used for
        non-conservative disturbing forces such as atmospheric drag and solar radiation pressure.
    
        Gaussian contributions can be expressed as: da :sub:`i` /dt = δa :sub:`i` /δv . q
    
    
        where:
    
          - a :sub:`i` are the six equinoctial elements
          - v is the velocity vector
          - q is the perturbing acceleration due to the considered force
    
    
        The averaging process and other considerations lead to integrate this contribution over the true longitude L possibly
        taking into account some limits.
    
        To create a numerically averaged contribution, one needs only to provide a :class:`~org.orekit.forces.ForceModel` and to
        implement in the derived class the methods:
        :meth:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution.getLLimits` and
        :meth:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution.getParametersDriversWithoutMu`.
    """
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements`): auxiliary elements related to the current orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state
                gauss (:class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution.GaussQuadrature`): Gauss quadrature
                low (double): lower bound of the integral interval
                high (double): upper bound of the integral interval
                context (:class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContributionContext`): container for attributes
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], tArray: typing.List[_getMeanElementRate_1__T]) -> typing.List[_getMeanElementRate_1__T]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements`<T> auxiliaryElements): auxiliary elements related to the current orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state
                gauss (:class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution.GaussQuadrature`): Gauss quadrature
                low (T): lower bound of the integral interval
                high (T): upper bound of the integral interval
                context (:class:`~org.orekit.propagation.semianalytical.dsst.forces.FieldAbstractGaussianContributionContext`<T> context): container for attributes
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation.
        
            The default implementation of this method does nothing.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.init` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, propagationType: org.orekit.propagation.PropagationType, doubleArray: typing.List[float]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], propagationType: org.orekit.propagation.PropagationType, tArray: typing.List[_initializeShortPeriodTerms_1__T]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Register an attitude provider.
        
            Register an attitude provider that can be used by the force model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.registerAttitudeProvider` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): the :class:`~org.orekit.attitudes.AttitudeProvider`
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, doubleArray: typing.List[float], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (double[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.SpacecraftState`...): mean states information: date, kinematics, attitude
        
        public <T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void updateShortPeriodTerms(T[] parameters, :class:`~org.orekit.propagation.FieldSpacecraftState`<T>... meanStates)
        
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (T[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.FieldSpacecraftState`<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, tArray: typing.List[_updateShortPeriodTerms_1__T], fieldSpacecraftStateArray: typing.List[org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]]) -> None: ...

class AbstractGaussianContributionContext(ForceModelContext):
    """
    public class AbstractGaussianContributionContext extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.ForceModelContext`
    
        This class is a container for the common parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution`.
    
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

class DSSTNewtonianAttraction(DSSTForceModel):
    """
    public class DSSTNewtonianAttraction extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    
        Force model for Newtonian central body attraction for the
        :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        Since:
            10.0
    """
    CENTRAL_ATTRACTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CENTRAL_ATTRACTION_COEFFICIENT
    
        Name of the single parameter of this model: the central attraction coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, double: float): ...
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getFieldEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements`): auxiliary elements related to the current orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], tArray: typing.List[_getMeanElementRate_1__T]) -> typing.List[_getMeanElementRate_1__T]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements`<T> auxiliaryElements): auxiliary elements related to the current orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        
        """
        ...
    def getMu(self) -> float:
        """
            Get the central attraction coefficient μ.
        
            Returns:
                mu central attraction coefficient (m³/s²)
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, propagationType: org.orekit.propagation.PropagationType, doubleArray: typing.List[float]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], propagationType: org.orekit.propagation.PropagationType, tArray: typing.List[_initializeShortPeriodTerms_1__T]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Register an attitude provider.
        
            Register an attitude provider that can be used by the force model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.registerAttitudeProvider` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): the :class:`~org.orekit.attitudes.AttitudeProvider`
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, doubleArray: typing.List[float], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (double[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.SpacecraftState`...): mean states information: date, kinematics, attitude
        
        public <T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void updateShortPeriodTerms(T[] parameters, :class:`~org.orekit.propagation.FieldSpacecraftState`<T>... meanStates)
        
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (T[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.FieldSpacecraftState`<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, tArray: typing.List[_updateShortPeriodTerms_1__T], fieldSpacecraftStateArray: typing.List[org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]]) -> None: ...

class DSSTNewtonianAttractionContext(ForceModelContext):
    """
    public class DSSTNewtonianAttractionContext extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.ForceModelContext`
    
        This class is a container for the common parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTNewtonianAttraction`.
    
        It performs parameters initialization at each integration step for the central body attraction.
    
    
        Since:
            10.0
    """
    def __init__(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]): ...
    def getGM(self) -> float:
        """
            Get standard gravitational parameter μ for the body in m³/s².
        
            Returns:
                gm
        
        
        """
        ...

class DSSTTesseral(DSSTForceModel):
    """
    public class DSSTTesseral extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    
        Tesseral contribution to the central body gravitational perturbation.
    
        Only resonant tesserals are considered.
    """
    SHORT_PERIOD_PREFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SHORT_PERIOD_PREFIX
    
        Name of the prefix for short period coefficients keys.
    
        Also see:
            :meth:`~constant`
    
    
    """
    CM_COEFFICIENTS: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` CM_COEFFICIENTS
    
        Identifier for cMm coefficients.
    
        Also see:
            :meth:`~constant`
    
    
    """
    SM_COEFFICIENTS: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SM_COEFFICIENTS
    
        Identifier for sMm coefficients.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, double: float, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, int: int, int2: int, int3: int, int4: int, int5: int, int6: int, int7: int): ...
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getFieldEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                spacecraftState (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements`): auxiliary elements related to the current orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], tArray: typing.List[_getMeanElementRate_1__T]) -> typing.List[_getMeanElementRate_1__T]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                spacecraftState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> spacecraftState): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements`<T> auxiliaryElements): auxiliary elements related to the current orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, propagationType: org.orekit.propagation.PropagationType, doubleArray: typing.List[float]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], propagationType: org.orekit.propagation.PropagationType, tArray: typing.List[_initializeShortPeriodTerms_1__T]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Register an attitude provider.
        
            Register an attitude provider that can be used by the force model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.registerAttitudeProvider` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the :class:`~org.orekit.attitudes.AttitudeProvider`
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, doubleArray: typing.List[float], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (double[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.SpacecraftState`...): mean states information: date, kinematics, attitude
        
        public <T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void updateShortPeriodTerms(T[] parameters, :class:`~org.orekit.propagation.FieldSpacecraftState`<T>... meanStates)
        
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (T[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.FieldSpacecraftState`<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, tArray: typing.List[_updateShortPeriodTerms_1__T], fieldSpacecraftStateArray: typing.List[org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]]) -> None: ...

class DSSTTesseralContext(ForceModelContext):
    """
    public class DSSTTesseralContext extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.ForceModelContext`
    
        This class is a container for the common parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTTesseral`.
    
        It performs parameters initialization at each integration step for the Tesseral contribution to the central body
        gravitational perturbation.
    
    
        Since:
            10.0
    """
    def getAx2oA(self) -> float:
        """
            Get ax2oA = 2 * a / A .
        
            Returns:
                ax2oA
        
        
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
    def getChi(self) -> float:
        """
            Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
            Returns:
                chi
        
        
        """
        ...
    def getChi2(self) -> float:
        """
            Get Χ².
        
            Returns:
                chi2
        
        
        """
        ...
    def getCo2AB(self) -> float:
        """
            Get Co2AB = C / 2AB.
        
            Returns:
                Co2AB
        
        
        """
        ...
    def getE2(self) -> float:
        """
            Get ecc².
        
            Returns:
                e2
        
        
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
    def getMoa(self) -> float:
        """
            Get μ / a .
        
            Returns:
                moa
        
        
        """
        ...
    def getOoAB(self) -> float:
        """
            Get ooAB = 1 / (A * B).
        
            Returns:
                ooAB
        
        
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
    def getRoa(self) -> float:
        """
            Get roa = R / a.
        
            Returns:
                roa
        
        
        """
        ...
    def getTheta(self) -> float:
        """
            Get Central body rotation angle θ.
        
            Returns:
                theta
        
        
        """
        ...

class DSSTThirdBody(DSSTForceModel):
    """
    public class DSSTThirdBody extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    
        Third body attraction perturbation to the :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    """
    SHORT_PERIOD_PREFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SHORT_PERIOD_PREFIX
    
        Name of the prefix for short period coefficients keys.
    
        Also see:
            :meth:`~constant`
    
    
    """
    ATTRACTION_COEFFICIENT: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` ATTRACTION_COEFFICIENT
    
        Name of the single parameter of this model: the attraction coefficient.
    
        Also see:
            :meth:`~constant`
    
    
    """
    def __init__(self, celestialBody: org.orekit.bodies.CelestialBody, double: float): ...
    def getBody(self) -> org.orekit.bodies.CelestialBody:
        """
            Get third body.
        
            Returns:
                third body
        
        
        """
        ...
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getFieldEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                currentState (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements`): auxiliary elements related to the current orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], tArray: typing.List[_getMeanElementRate_1__T]) -> typing.List[_getMeanElementRate_1__T]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                currentState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> currentState): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements`<T> auxiliaryElements): auxiliary elements related to the current orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, propagationType: org.orekit.propagation.PropagationType, doubleArray: typing.List[float]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], propagationType: org.orekit.propagation.PropagationType, tArray: typing.List[_initializeShortPeriodTerms_1__T]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Register an attitude provider.
        
            Register an attitude provider that can be used by the force model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.registerAttitudeProvider` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                provider (:class:`~org.orekit.attitudes.AttitudeProvider`): the :class:`~org.orekit.attitudes.AttitudeProvider`
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, doubleArray: typing.List[float], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (double[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.SpacecraftState`...): mean states information: date, kinematics, attitude
        
        public <T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void updateShortPeriodTerms(T[] parameters, :class:`~org.orekit.propagation.FieldSpacecraftState`<T>... meanStates)
        
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (T[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.FieldSpacecraftState`<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, tArray: typing.List[_updateShortPeriodTerms_1__T], fieldSpacecraftStateArray: typing.List[org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]]) -> None: ...

class DSSTThirdBodyContext(ForceModelContext):
    """
    public class DSSTThirdBodyContext extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.ForceModelContext`
    
        This class is a container for the common parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTThirdBody`.
    
        It performs parameters initialization at each integration step for the third body attraction perturbation.
    
    
        Since:
            10.0
    """
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
    def getAoR3Pow(self) -> typing.List[float]:
        """
            Get the value of a / R3 up to power maxAR3Pow.
        
            Returns:
                aoR3Pow
        
        
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
    def getQns(self) -> typing.List[typing.List[float]]:
        """
            Get the value of Qns coefficients.
        
            Returns:
                Qns
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
            Returns:
                Χ
        
        
        """
        ...
    def getb(self) -> float:
        """
            Get b = 1 / (1 + sqrt(1 - e²)) = 1 / (1 + B).
        
            Returns:
                b
        
        
        """
        ...

class DSSTZonal(DSSTForceModel):
    """
    public class DSSTZonal extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
    
        Zonal contribution to the central body gravitational perturbation.
    """
    SHORT_PERIOD_PREFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is` SHORT_PERIOD_PREFIX
    
        Name of the prefix for short period coefficients keys.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider, int: int, int2: int, int3: int): ...
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getFieldEventsDetectors` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getMeanElementRate_1__T = typing.TypeVar('_getMeanElementRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getMeanElementRate(self, spacecraftState: org.orekit.propagation.SpacecraftState, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                spacecraftState (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements`): auxiliary elements related to the current orbit
                parameters (double[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        """
        ...
    @typing.overload
    def getMeanElementRate(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getMeanElementRate_1__T], fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_getMeanElementRate_1__T], tArray: typing.List[_getMeanElementRate_1__T]) -> typing.List[_getMeanElementRate_1__T]:
        """
            Computes the mean equinoctial elements rates da :sub:`i` / dt.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.getMeanElementRate` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                spacecraftState (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> spacecraftState): current state information: date, kinematics, attitude
                auxiliaryElements (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements`<T> auxiliaryElements): auxiliary elements related to the current orbit
                parameters (T[]): values of the force model parameters
        
            Returns:
                the mean element rates dai/dt
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getProvider(self) -> org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider:
        """
            Get the spherical harmonics provider.
        
            Returns:
                the spherical harmonics provider
        
        
        """
        ...
    _initializeShortPeriodTerms_1__T = typing.TypeVar('_initializeShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def initializeShortPeriodTerms(self, auxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.AuxiliaryElements, propagationType: org.orekit.propagation.PropagationType, doubleArray: typing.List[float]) -> java.util.List[ShortPeriodTerms]: ...
    @typing.overload
    def initializeShortPeriodTerms(self, fieldAuxiliaryElements: org.orekit.propagation.semianalytical.dsst.utilities.FieldAuxiliaryElements[_initializeShortPeriodTerms_1__T], propagationType: org.orekit.propagation.PropagationType, tArray: typing.List[_initializeShortPeriodTerms_1__T]) -> java.util.List[FieldShortPeriodTerms[_initializeShortPeriodTerms_1__T]]: ...
    def registerAttitudeProvider(self, attitudeProvider: org.orekit.attitudes.AttitudeProvider) -> None:
        """
            Register an attitude provider.
        
            Register an attitude provider that can be used by the force model.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.registerAttitudeProvider` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                attitudeProvider (:class:`~org.orekit.attitudes.AttitudeProvider`): the :class:`~org.orekit.attitudes.AttitudeProvider`
        
        
        """
        ...
    _updateShortPeriodTerms_1__T = typing.TypeVar('_updateShortPeriodTerms_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def updateShortPeriodTerms(self, doubleArray: typing.List[float], spacecraftStateArray: typing.List[org.orekit.propagation.SpacecraftState]) -> None:
        """
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (double[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.SpacecraftState`...): mean states information: date, kinematics, attitude
        
        public <T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> void updateShortPeriodTerms(T[] parameters, :class:`~org.orekit.propagation.FieldSpacecraftState`<T>... meanStates)
        
            Update the short period terms.
        
            The :class:`~org.orekit.propagation.semianalytical.dsst.forces.ShortPeriodTerms` that will be updated are the ones that
            were returned during the call to
            :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.initializeShortPeriodTerms`.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel.updateShortPeriodTerms` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTForceModel`
        
            Parameters:
                parameters (T[]): values of the force model parameters
                meanStates (:class:`~org.orekit.propagation.FieldSpacecraftState`<T>...): mean states information: date, kinematics, attitude
        
        
        """
        ...
    @typing.overload
    def updateShortPeriodTerms(self, tArray: typing.List[_updateShortPeriodTerms_1__T], fieldSpacecraftStateArray: typing.List[org.orekit.propagation.FieldSpacecraftState[_updateShortPeriodTerms_1__T]]) -> None: ...

class DSSTZonalContext(ForceModelContext):
    """
    public class DSSTZonalContext extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.ForceModelContext`
    
        This class is a container for the common parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTZonal`.
    
        It performs parameters initialization at each integration step for the Zonal contribution to the central body
        gravitational perturbation.
    
    
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
    def getCXO2N2A2(self) -> float:
        """
            Get (C * χ) / ( 2 * n² * a² ).
        
            Returns:
                cxo2n2a2
        
        
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
    def getMuoa(self) -> float:
        """
            Get μ / a .
        
            Returns:
                muoa
        
        
        """
        ...
    def getOON2A2(self) -> float:
        """
            Get 1 / (n² * a²).
        
            Returns:
                oon2a2
        
        
        """
        ...
    def getOoAB(self) -> float:
        """
            Get ooAB = 1 / (A * B).
        
            Returns:
                ooAB
        
        
        """
        ...
    def getRoa(self) -> float:
        """
            Get roa = R / a.
        
            Returns:
                roa
        
        
        """
        ...
    def getX(self) -> float:
        """
            Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
            Returns:
                Χ
        
        
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
    def getXX(self) -> float:
        """
            Get Χ².
        
            Returns:
                Χ².
        
        
        """
        ...
    def getXXX(self) -> float:
        """
            Get Χ³.
        
            Returns:
                Χ³
        
        
        """
        ...

_FieldAbstractGaussianContributionContext__T = typing.TypeVar('_FieldAbstractGaussianContributionContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAbstractGaussianContributionContext(FieldForceModelContext[_FieldAbstractGaussianContributionContext__T], typing.Generic[_FieldAbstractGaussianContributionContext__T]):
    """
    public class FieldAbstractGaussianContributionContext<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.FieldForceModelContext`<T>
    
        This class is a container for the common "field" parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution`.
    
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

_FieldDSSTNewtonianAttractionContext__T = typing.TypeVar('_FieldDSSTNewtonianAttractionContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTNewtonianAttractionContext(FieldForceModelContext[_FieldDSSTNewtonianAttractionContext__T], typing.Generic[_FieldDSSTNewtonianAttractionContext__T]):
    """
    public class FieldDSSTNewtonianAttractionContext<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.FieldForceModelContext`<T>
    
        This class is a container for the common "field" parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTNewtonianAttraction`.
    
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

_FieldDSSTTesseralContext__T = typing.TypeVar('_FieldDSSTTesseralContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTTesseralContext(FieldForceModelContext[_FieldDSSTTesseralContext__T], typing.Generic[_FieldDSSTTesseralContext__T]):
    """
    public class FieldDSSTTesseralContext<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.FieldForceModelContext`<T>
    
        This class is a container for the common "field" parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTTesseral`.
    
        It performs parameters initialization at each integration step for the Tesseral contribution to the central body
        gravitational perturbation.
    
    
        Since:
            10.0
    """
    def getAx2oA(self) -> _FieldDSSTTesseralContext__T:
        """
            Get ax2oA = 2 * a / A .
        
            Returns:
                ax2oA
        
        
        """
        ...
    def getBoA(self) -> _FieldDSSTTesseralContext__T:
        """
            Get B / A.
        
            Returns:
                BoA
        
        
        """
        ...
    def getBoABpo(self) -> _FieldDSSTTesseralContext__T:
        """
            Get BoABpo = B / A(1 + B).
        
            Returns:
                BoABpo
        
        
        """
        ...
    def getChi(self) -> _FieldDSSTTesseralContext__T:
        """
            Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
            Returns:
                chi
        
        
        """
        ...
    def getChi2(self) -> _FieldDSSTTesseralContext__T:
        """
            Get Χ².
        
            Returns:
                chi2
        
        
        """
        ...
    def getCo2AB(self) -> _FieldDSSTTesseralContext__T:
        """
            Get Co2AB = C / 2AB.
        
            Returns:
                Co2AB
        
        
        """
        ...
    def getE2(self) -> _FieldDSSTTesseralContext__T:
        """
            Get ecc².
        
            Returns:
                e2
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldDSSTTesseralContext__T:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMoa(self) -> _FieldDSSTTesseralContext__T:
        """
            Get μ / a .
        
            Returns:
                moa
        
        
        """
        ...
    def getOoAB(self) -> _FieldDSSTTesseralContext__T:
        """
            Get ooAB = 1 / (A * B).
        
            Returns:
                ooAB
        
        
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
    def getRoa(self) -> _FieldDSSTTesseralContext__T:
        """
            Get roa = R / a.
        
            Returns:
                roa
        
        
        """
        ...
    def getTheta(self) -> _FieldDSSTTesseralContext__T:
        """
            Get Central body rotation angle θ.
        
            Returns:
                theta
        
        
        """
        ...

_FieldDSSTThirdBodyContext__T = typing.TypeVar('_FieldDSSTThirdBodyContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTThirdBodyContext(FieldForceModelContext[_FieldDSSTThirdBodyContext__T], typing.Generic[_FieldDSSTThirdBodyContext__T]):
    """
    public class FieldDSSTThirdBodyContext<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.FieldForceModelContext`<T>
    
        This class is a container for the common "field" parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTThirdBody`.
    
        It performs parameters initialization at each integration step for the third body attraction perturbation.
    
    
        Since:
            10.0
    """
    def getA(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get A = sqrt(μ * a).
        
            Returns:
                A
        
        
        """
        ...
    def getAlpha(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get direction cosine α for central body.
        
            Returns:
                α
        
        
        """
        ...
    def getAoR3Pow(self) -> typing.List[_FieldDSSTThirdBodyContext__T]:
        """
            Get the value of a / R3 up to power maxAR3Pow.
        
            Returns:
                aoR3Pow
        
        
        """
        ...
    def getBB(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get B².
        
            Returns:
                B²
        
        
        """
        ...
    def getBBB(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get B³.
        
            Returns:
                B³
        
        
        """
        ...
    def getBeta(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get direction cosine β for central body.
        
            Returns:
                β
        
        
        """
        ...
    def getBoA(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get B / A.
        
            Returns:
                BoA
        
        
        """
        ...
    def getBoABpo(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get BoABpo = B / A(1 + B).
        
            Returns:
                BoABpo
        
        
        """
        ...
    def getGamma(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get direction cosine γ for central body.
        
            Returns:
                γ
        
        
        """
        ...
    def getHXXX(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get hXXX = h * Χ³.
        
            Returns:
                hXXX
        
        
        """
        ...
    def getKXXX(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get kXXX = h * Χ³.
        
            Returns:
                kXXX
        
        
        """
        ...
    def getM2aoA(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get m2aoA = -2 * a / A.
        
            Returns:
                m2aoA
        
        
        """
        ...
    def getMCo2AB(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get mCo2AB = -C / 2AB.
        
            Returns:
                mCo2AB
        
        
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
    def getMeanMotion(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMuoR3(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get muoR3 = mu3 / R3.
        
            Returns:
                muoR3
        
        
        """
        ...
    def getOoAB(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get ooAB = 1 / (A * B).
        
            Returns:
                ooAB
        
        
        """
        ...
    def getQns(self) -> typing.List[typing.List[_FieldDSSTThirdBodyContext__T]]:
        """
            Get the value of Qns coefficients.
        
            Returns:
                Qns
        
        
        """
        ...
    def getX(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
            Returns:
                Χ
        
        
        """
        ...
    def getb(self) -> _FieldDSSTThirdBodyContext__T:
        """
            Get b = 1 / (1 + sqrt(1 - e²)) = 1 / (1 + B).
        
            Returns:
                b
        
        
        """
        ...

_FieldDSSTZonalContext__T = typing.TypeVar('_FieldDSSTZonalContext__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDSSTZonalContext(FieldForceModelContext[_FieldDSSTZonalContext__T], typing.Generic[_FieldDSSTZonalContext__T]):
    """
    public class FieldDSSTZonalContext<T extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.FieldForceModelContext`<T>
    
        This class is a container for the common "field" parameters used in
        :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTZonal`.
    
        It performs parameters initialization at each integration step for the Zonal contribution to the central body
        gravitational perturbation.
    
    
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
    def getBoA(self) -> _FieldDSSTZonalContext__T:
        """
            Get B / A.
        
            Returns:
                BoA
        
        
        """
        ...
    def getBoABpo(self) -> _FieldDSSTZonalContext__T:
        """
            Get BoABpo = B / A(1 + B).
        
            Returns:
                BoABpo
        
        
        """
        ...
    def getCXO2N2A2(self) -> _FieldDSSTZonalContext__T:
        """
            Get (C * χ) / ( 2 * n² * a² ).
        
            Returns:
                cxo2n2a2
        
        
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
    def getM2aoA(self) -> _FieldDSSTZonalContext__T:
        """
            Get m2aoA = -2 * a / A.
        
            Returns:
                m2aoA
        
        
        """
        ...
    def getMCo2AB(self) -> _FieldDSSTZonalContext__T:
        """
            Get mCo2AB = -C / 2AB.
        
            Returns:
                mCo2AB
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldDSSTZonalContext__T:
        """
            Get the Keplerian mean motion.
        
            The Keplerian mean motion is computed directly from semi major axis and central acceleration constant.
        
            Returns:
                Keplerian mean motion in radians per second
        
        
        """
        ...
    def getMuoa(self) -> _FieldDSSTZonalContext__T:
        """
            Get μ / a .
        
            Returns:
                muoa
        
        
        """
        ...
    def getOON2A2(self) -> _FieldDSSTZonalContext__T:
        """
            Get 1 / (n² * a²).
        
            Returns:
                oon2a2
        
        
        """
        ...
    def getOoAB(self) -> _FieldDSSTZonalContext__T:
        """
            Get ooAB = 1 / (A * B).
        
            Returns:
                ooAB
        
        
        """
        ...
    def getRoa(self) -> _FieldDSSTZonalContext__T:
        """
            Get roa = R / a.
        
            Returns:
                roa
        
        
        """
        ...
    def getX(self) -> _FieldDSSTZonalContext__T:
        """
            Get Χ = 1 / sqrt(1 - e²) = 1 / B.
        
            Returns:
                Χ
        
        
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
    def getXX(self) -> _FieldDSSTZonalContext__T:
        """
            Get Χ².
        
            Returns:
                Χ².
        
        
        """
        ...
    def getXXX(self) -> _FieldDSSTZonalContext__T:
        """
            Get Χ³.
        
            Returns:
                Χ³
        
        
        """
        ...

class DSSTAtmosphericDrag(AbstractGaussianContribution):
    """
    public class DSSTAtmosphericDrag extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution`
    
        Atmospheric drag contribution to the :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        The drag acceleration is computed through the acceleration model of :class:`~org.orekit.forces.drag.DragForce`.
    """
    @typing.overload
    def __init__(self, dragForce: org.orekit.forces.drag.DragForce, double: float): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, dragSensitive: org.orekit.forces.drag.DragSensitive, double: float): ...
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
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
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

class DSSTSolarRadiationPressure(AbstractGaussianContribution):
    """
    public class DSSTSolarRadiationPressure extends :class:`~org.orekit.propagation.semianalytical.dsst.forces.AbstractGaussianContribution`
    
        Solar radiation pressure contribution to the :class:`~org.orekit.propagation.semianalytical.dsst.DSSTPropagator`.
    
        The solar radiation pressure acceleration is computed through the acceleration model of
        :class:`~org.orekit.forces.radiation.SolarRadiationPressure`.
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float, double4: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double5: float, double6: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double3: float, double4: float): ...
    @typing.overload
    def __init__(self, double: float, double2: float, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double3: float, radiationSensitive: org.orekit.forces.radiation.RadiationSensitive, double4: float): ...
    @typing.overload
    def __init__(self, extendedPVCoordinatesProvider: org.orekit.utils.ExtendedPVCoordinatesProvider, double: float, radiationSensitive: org.orekit.forces.radiation.RadiationSensitive, double2: float): ...
    def getEquatorialRadius(self) -> float:
        """
            Get the central body equatorial radius.
        
            Returns:
                central body equatorial radius (m)
        
        
        """
        ...
    def getEventsDetectors(self) -> typing.List[org.orekit.propagation.events.EventDetector]:
        """
            Get the discrete events related to the model.
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> typing.List[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]:
        """
            Get the discrete events related to the model.
        
            Parameters:
                field (:class:`~org.orekit.propagation.semianalytical.dsst.forces.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field used by default
        
            Returns:
                array of events detectors or null if the model is not related to any discrete events
        
        
        """
        ...
    def getSpacecraft(self) -> org.orekit.forces.radiation.RadiationSensitive:
        """
            Get spacecraft shape.
        
            Returns:
                the spacecraft shape.
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst.forces")``.

    AbstractGaussianContribution: typing.Type[AbstractGaussianContribution]
    AbstractGaussianContributionContext: typing.Type[AbstractGaussianContributionContext]
    DSSTAtmosphericDrag: typing.Type[DSSTAtmosphericDrag]
    DSSTForceModel: typing.Type[DSSTForceModel]
    DSSTNewtonianAttraction: typing.Type[DSSTNewtonianAttraction]
    DSSTNewtonianAttractionContext: typing.Type[DSSTNewtonianAttractionContext]
    DSSTSolarRadiationPressure: typing.Type[DSSTSolarRadiationPressure]
    DSSTTesseral: typing.Type[DSSTTesseral]
    DSSTTesseralContext: typing.Type[DSSTTesseralContext]
    DSSTThirdBody: typing.Type[DSSTThirdBody]
    DSSTThirdBodyContext: typing.Type[DSSTThirdBodyContext]
    DSSTZonal: typing.Type[DSSTZonal]
    DSSTZonalContext: typing.Type[DSSTZonalContext]
    FieldAbstractGaussianContributionContext: typing.Type[FieldAbstractGaussianContributionContext]
    FieldDSSTNewtonianAttractionContext: typing.Type[FieldDSSTNewtonianAttractionContext]
    FieldDSSTTesseralContext: typing.Type[FieldDSSTTesseralContext]
    FieldDSSTThirdBodyContext: typing.Type[FieldDSSTThirdBodyContext]
    FieldDSSTZonalContext: typing.Type[FieldDSSTZonalContext]
    FieldForceModelContext: typing.Type[FieldForceModelContext]
    FieldShortPeriodTerms: typing.Type[FieldShortPeriodTerms]
    ForceModelContext: typing.Type[ForceModelContext]
    ShortPeriodTerms: typing.Type[ShortPeriodTerms]
    class-use: org.orekit.propagation.semianalytical.dsst.forces.class-use.__module_protocol__
