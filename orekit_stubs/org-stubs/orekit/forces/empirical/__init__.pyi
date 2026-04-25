
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import jpype
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.attitudes
import org.orekit.forces
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AbstractParametricAcceleration(org.orekit.forces.ForceModel):
    """
    Abstract class for parametric acceleration.
    
    Since:
        13.0
    """
    def dependsOnPositionOnly(self) -> bool:
        """
        Check if force model depends on position only at a given, fixed date.
        
        Specified by: dependsOnPositionOnly in interface ForceModel
        
        Returns:
            true if force model depends on position only, false if it depends on mass or velocity, either directly or due to a
            dependency on attitude
        
        
        """
        ...
    def getAttitudeOverride(self) -> org.orekit.attitudes.AttitudeProvider:
        """
        Getter for attitude override.
        
        Returns:
            attitude override
        
        
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

class AccelerationModel(org.orekit.utils.ParameterDriversProvider):
    """
    Acceleration model used by empirical force.
    
    Since:
        10.3
    """
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the acceleration model at the start of the propagation.
        
        The default implementation of this method does nothing
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], parameters: typing.Union[typing.List[_signedAmplitude_1__T], jpype.JArray]) -> _signedAmplitude_1__T:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        
        """
        ...

class HarmonicAccelerationModel(AccelerationModel):
    """
    Harmonic acceleration model.
    
    Since:
        10.3
    """
    def __init__(self, prefix: str, referenceDate: org.orekit.time.AbsoluteDate, fundamentalPeriod: float, harmonicMultiplier: int):
        """
        Simple constructor.
        
        Parameters:
            prefix (String): prefix to use for parameter drivers
            referenceDate (AbsoluteDate): reference date for computing polynomials, if null the reference date will be automatically set at propagation start
            fundamentalPeriod (double): fundamental period (typically set to initial orbit getKeplerianPeriod)
            harmonicMultiplier (int): multiplier to compute harmonic period from fundamental period)
        
        
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
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the acceleration model at the start of the propagation.
        
        The default implementation of this method does nothing
        
        Specified by: init in interface AccelerationModel
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Specified by: signedAmplitude in interface AccelerationModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], parameters: typing.Union[typing.List[_signedAmplitude_1__T], jpype.JArray]) -> _signedAmplitude_1__T:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Specified by: signedAmplitude in interface AccelerationModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        
        """
        ...

class ParametricAcceleration(AbstractParametricAcceleration):
    """
    This class implements a parametric acceleration.
    
    Parametric accelerations are intended to model lesser-known forces, estimating a few defining parameters from a parametric function using orbit determination. Typical parametric functions are polynomial (often limited to a constant term) and harmonic (often with either orbital period or half orbital period).
    
    An important operational example is the infamous GPS Y-bias, which is thought to be related to a radiator thermal radiation. Other examples could be to model leaks that produce roughly constant trust in some spacecraft-related direction.
    
    The acceleration direction is considered constant in either:
    
      - inertial frame
      - spacecraft frame
      - a dedicated attitude frame overriding spacecraft attitude (this could for example be used to model solar arrays
        orientation if the force is related to solar arrays)
    
    If the direction of the acceleration is unknown, then three instances of this class should be used, one along the X axis, one along the Y axis and one along the Z axis and their parameters estimated as usual.
    
    Since:
        10.3
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, boolean: bool, accelerationModel: AccelerationModel): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider, accelerationModel: AccelerationModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the force model at the start of propagation. This method will be called before any calls to addContribution, addContribution, acceleration or acceleration
        
        The default implementation of this method does nothing.
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...

class PolynomialAccelerationModel(AccelerationModel):
    """
    Polynomial acceleration model.
    
    Since:
        10.3
    """
    def __init__(self, prefix: str, referenceDate: org.orekit.time.AbsoluteDate, degree: int):
        """
        Simple constructor.
        
        Parameters:
            prefix (String): prefix to use for parameter drivers
            referenceDate (AbsoluteDate): reference date for computing polynomials, if null the reference date will be automatically set at propagation start
            degree (int): polynomial degree (i.e. a value of 0 corresponds to a constant acceleration)
        
        
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
    def init(self, initialState: org.orekit.propagation.SpacecraftState, target: org.orekit.time.AbsoluteDate) -> None:
        """
        Initialize the acceleration model at the start of the propagation.
        
        The default implementation of this method does nothing
        
        Specified by: init in interface AccelerationModel
        
        Parameters:
            initialState (SpacecraftState): spacecraft state at the start of propagation.
            target (AbsoluteDate): date of propagation. Not equal to getDate().
        
        
        """
        ...
    _signedAmplitude_1__T = typing.TypeVar('_signedAmplitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Specified by: signedAmplitude in interface AccelerationModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], parameters: typing.Union[typing.List[_signedAmplitude_1__T], jpype.JArray]) -> _signedAmplitude_1__T:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Specified by: signedAmplitude in interface AccelerationModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        
        """
        ...

class PythonAccelerationModel(AccelerationModel):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def signedAmplitude(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Specified by: signedAmplitude in interface AccelerationModel
        
        Parameters:
            state (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        """
        ...
    @typing.overload
    def signedAmplitude(self, state: org.orekit.propagation.FieldSpacecraftState[_signedAmplitude_1__T], parameters: typing.Union[typing.List[_signedAmplitude_1__T], jpype.JArray]) -> _signedAmplitude_1__T:
        """
        Compute the signed amplitude of the acceleration.
        
        The acceleration is the direction multiplied by the signed amplitude. So if signed amplitude is negative, the acceleratin is towards the opposite of the direction specified at construction.
        
        Specified by: signedAmplitude in interface AccelerationModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters
        
        Returns:
            norm of the acceleration
        
        
        """
        ...

class TimeSpanParametricAcceleration(AbstractParametricAcceleration):
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, boolean: bool, accelerationModel: AccelerationModel): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, attitudeProvider: org.orekit.attitudes.AttitudeProvider, accelerationModel: AccelerationModel): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def addAccelerationModelValidAfter(self, accelerationModel: AccelerationModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addAccelerationModelValidBefore(self, accelerationModel: AccelerationModel, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def extractAccelerationModelRange(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap[AccelerationModel]: ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    @typing.overload
    def extractParameters(self, tArray: typing.Union[typing.List[_extractParameters_1__T], jpype.JArray], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.MutableSequence[_extractParameters_1__T]: ...
    def getAccelerationModel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> AccelerationModel: ...
    def getAccelerationModelSpan(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap.Span[AccelerationModel]: ...
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[AccelerationModel]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    _init_0__T = typing.TypeVar('_init_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def init(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_init_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_init_0__T]) -> None: ...
    @typing.overload
    def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.empirical")``.

    AbstractParametricAcceleration: typing.Type[AbstractParametricAcceleration]
    AccelerationModel: typing.Type[AccelerationModel]
    HarmonicAccelerationModel: typing.Type[HarmonicAccelerationModel]
    ParametricAcceleration: typing.Type[ParametricAcceleration]
    PolynomialAccelerationModel: typing.Type[PolynomialAccelerationModel]
    PythonAccelerationModel: typing.Type[PythonAccelerationModel]
    TimeSpanParametricAcceleration: typing.Type[TimeSpanParametricAcceleration]
