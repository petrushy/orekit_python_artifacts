import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.forces
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AccelerationModel:
    """
    public interface AccelerationModel
    
        Acceleration model used by empirical force.
    
        Since:
            10.3
    """
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the acceleration model at the start of the propagation.
        
            The default implementation of this method does nothing
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        
        """
        ...

class ParametricAcceleration(org.orekit.forces.AbstractForceModel):
    """
    public class ParametricAcceleration extends :class:`~org.orekit.forces.AbstractForceModel`
    
        This class implements a parametric acceleration.
    
        Parametric accelerations are intended to model lesser-known forces, estimating a few defining parameters from a
        parametric function using orbit determination. Typical parametric functions are polynomial (often limited to a constant
        term) and harmonic (often with either orbital period or half orbital period).
    
        An important operational example is the infamous GPS Y-bias, which is thought to be related to a radiator thermal
        radiation. Other examples could be to model leaks that produce roughly constant trust in some spacecraft-related
        direction.
    
        The acceleration direction is considered constant in either:
    
          - inertial frame
          - spacecraft frame
          - a dedicated attitude frame overriding spacecraft attitude (this could for example be used to model solar arrays
            orientation if the force is related to solar arrays)
    
    
        If the direction of the acceleration is unknown, then three instances of this class should be used, one along the X
        axis, one along the Y axis and one along the Z axis and their parameters estimated as usual.
    
        Since:
            10.3
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, boolean: bool, accelerationModel: AccelerationModel): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider, accelerationModel: AccelerationModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
            Compute acceleration.
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Compute acceleration.
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                acceleration in same frame as state
        
        """
        ...
    def dependsOnPositionOnly(self) -> bool:
        """
            Check if force models depends on position only.
        
            Returns:
                true if force model depends on position only, false if it depends on velocity, either directly or due to a dependency on
                attitude
        
        
        """
        ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the force model at the start of propagation. This method will be called before any calls to
            :meth:`~org.orekit.forces.ForceModel.addContribution`, :meth:`~org.orekit.forces.ForceModel.addContribution`, null or
            null
        
            The default implementation of this method does nothing.
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...

class TimeSpanParametricAcceleration(org.orekit.forces.AbstractForceModel):
    DATE_BEFORE: typing.ClassVar[str] = ...
    DATE_AFTER: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, boolean: bool, accelerationModel: AccelerationModel): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider, accelerationModel: AccelerationModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.List[_acceleration_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def addAccelerationModelValidAfter(self, accelerationModel: AccelerationModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addAccelerationModelValidBefore(self, accelerationModel: AccelerationModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def dependsOnPositionOnly(self) -> bool: ...
    def extractAccelerationModelRange(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap[AccelerationModel]: ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.List[float], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    @typing.overload
    def extractParameters(self, tArray: typing.List[_extractParameters_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.List[_extractParameters_1__T]: ...
    def getAccelerationModel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> AccelerationModel: ...
    def getAccelerationModelSpan(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap.Span[AccelerationModel]: ...
    def getEventsDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventsDetectors__T = typing.TypeVar('_getFieldEventsDetectors__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getFieldEventsDetectors(self, field: org.hipparchus.Field[_getFieldEventsDetectors__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventsDetectors__T]]: ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[AccelerationModel]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getTransitions(self) -> java.util.NavigableSet[org.orekit.utils.TimeSpanMap.Transition[AccelerationModel]]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class HarmonicAccelerationModel(AccelerationModel):
    """
    public class HarmonicAccelerationModel extends Object implements :class:`~org.orekit.forces.empirical.AccelerationModel`
    
        Harmonic acceleration model.
    
        Since:
            10.3
    """
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, double: float, int: int): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the acceleration model at the start of the propagation.
        
            The default implementation of this method does nothing
        
            Specified by:
                :meth:`~org.orekit.forces.empirical.AccelerationModel.init`Â in
                interfaceÂ :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        
        """
        ...

class PolynomialAccelerationModel(AccelerationModel):
    """
    public class PolynomialAccelerationModel extends Object implements :class:`~org.orekit.forces.empirical.AccelerationModel`
    
        Polynomial acceleration model.
    
        Since:
            10.3
    """
    def __init__(self, string: str, absoluteDate: org.orekit.time.AbsoluteDate, int: int): ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None:
        """
            Initialize the acceleration model at the start of the propagation.
        
            The default implementation of this method does nothing
        
            Specified by:
                :meth:`~org.orekit.forces.empirical.AccelerationModel.init`Â in
                interfaceÂ :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                initialState (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state at the start of propagation.
                target (:class:`~org.orekit.time.AbsoluteDate`): date of propagation. Not equal to :code:`initialState.getDate()`.
        
        
        """
        ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        
        """
        ...

class PythonAccelerationModel(AccelerationModel):
    """
    public class PythonAccelerationModel extends Object implements :class:`~org.orekit.forces.empirical.AccelerationModel`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
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
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.List[float]) -> float:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): current state information: date, kinematics, attitude
                parameters (double[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], tArray: typing.List[_signedAmplitude_1__T]) -> _signedAmplitude_1__T:
        """
            Compute the signed amplitude of the acceleration.
        
            The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the
            acceleratin is towards the opposite of the direction specified at construction.
        
            Specified by:
                 in interface :class:`~org.orekit.forces.empirical.AccelerationModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): current state information: date, kinematics, attitude
                parameters (T[]): values of the force model parameters
        
            Returns:
                norm of the acceleration
        
        
        """
        ...
    _signedAmplitude_FT__T = typing.TypeVar('_signedAmplitude_FT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def signedAmplitude_FT(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_FT__T], tArray: typing.List[_signedAmplitude_FT__T]) -> _signedAmplitude_FT__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.empirical")``.

    AccelerationModel: typing.Type[AccelerationModel]
    HarmonicAccelerationModel: typing.Type[HarmonicAccelerationModel]
    ParametricAcceleration: typing.Type[ParametricAcceleration]
    PolynomialAccelerationModel: typing.Type[PolynomialAccelerationModel]
    PythonAccelerationModel: typing.Type[PythonAccelerationModel]
    TimeSpanParametricAcceleration: typing.Type[TimeSpanParametricAcceleration]
