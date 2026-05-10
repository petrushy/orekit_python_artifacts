
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
import org.orekit.forces
import org.orekit.models.earth.atmosphere
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class AbstractDragForceModel(org.orekit.forces.ForceModel):
    """
    Base class for drag force models.
    
    Since:
        10.2
    
    Also see:
        DragForce
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
    def getAtmosphere(self) -> org.orekit.models.earth.atmosphere.Atmosphere:
        """
        Get the atmospheric model.
        
        Returns:
            atmosphere model
        
        Since:
            12.1
        
        
        """
        ...

class DragSensitive:
    """
    Interface for spacecraft that are sensitive to atmospheric drag forces.
    
    Also see:
        DragForce
    """
    GLOBAL_DRAG_FACTOR: typing.ClassVar[str] = ...
    """
    Parameter name for global multiplicative factor.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    DRAG_COEFFICIENT: typing.ClassVar[str] = ...
    """
    Parameter name for drag coefficient.
    
    Also see:
        constant
    
    
    """
    LIFT_RATIO: typing.ClassVar[str] = ...
    """
    Parameter name for lift ration enabling Jacobian processing.
    
    The lift ratio is the proportion of atmosphere modecules that will experience specular reflection when hitting spacecraft instead of experiencing diffuse reflection. The ratio is between 0 and 1, 0 meaning there are no specular reflection, only diffuse reflection, and hence no lift effect.
    
    Since:
        9.0
    
    Also see:
        constant
    
    
    """
    def dependsOnAttitudeRate(self) -> bool:
        """
        Check if model depends on attitude's rotation rate or acceleration at a given, fixed date. If false, it essentially means that at most the attitude's rotation is used when computing the acceleration vector. The default implementation returns false as common models for orbital mechanics do not.
        
        Returns:
            true if force model depends on attitude derivatives
        
        Since:
            12.1
        
        
        """
        ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_dragAcceleration_0__T], density: _dragAcceleration_0__T, relativeVelocity: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], parameters: typing.Union[typing.List[_dragAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            density (T): atmospheric density at spacecraft position
            relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.SpacecraftState, density: float, relativeVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Parameters:
            state (SpacecraftState): current state
            density (double): atmospheric density at spacecraft position
            relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        Since:
            12.0
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Returns:
            parameters drivers
        
        Since:
            8.0
        
        
        """
        ...

class DragForce(AbstractDragForceModel):
    """
    Atmospheric drag force model. The drag acceleration is computed as follows : γ = (1/2 * ρ * V² * S / Mass) * DragCoefVector With DragCoefVector = {C :sub:`x` , C :sub:`y` , C :sub:`z` } and S given by the user through the interface DragSensitive
    """
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, spacecraft: DragSensitive): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, spacecraft: DragSensitive, useFiniteDifferencesOnDensityWrtPosition: bool): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
    def dependsOnAttitudeRate(self) -> bool:
        """
        Check if force model depends on attitude's rotation rate or acceleration at a given, fixed date. If false, it essentially means that at most the attitude's rotation is used when computing the acceleration vector. The default implementation returns false as common forces do not.
        
        Returns:
            true if force model depends on attitude derivatives
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getSpacecraft(self) -> DragSensitive:
        """
        Get spacecraft that are sensitive to atmospheric drag forces.
        
        Returns:
            drag sensitive spacecraft model
        
        
        """
        ...

class IsotropicDrag(DragSensitive):
    """
    This class models isotropic drag effects.
    
    The model of this spacecraft is a simple spherical model, this means that all coefficients are constant and do not depend on the direction.
    
    Since:
        7.1
    
    Also see:
        BoxAndSolarArraySpacecraft,
        IsotropicRadiationCNES95Convention
    """
    @typing.overload
    def __init__(self, crossSection: float, dragCoeff: float): ...
    @typing.overload
    def __init__(self, crossSection: float, dragCoeff: float, dragCoeffMin: float, dragCoeffMax: float): ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_dragAcceleration_0__T], density: _dragAcceleration_0__T, relativeVelocity: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], parameters: typing.Union[typing.List[_dragAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Specified by: dragAcceleration in interface DragSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            density (T): atmospheric density at spacecraft position
            relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.SpacecraftState, density: float, relativeVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Specified by: dragAcceleration in interface DragSensitive
        
        Parameters:
            state (SpacecraftState): current state
            density (double): atmospheric density at spacecraft position
            relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getDragParametersDrivers in interface DragSensitive
        
        Returns:
            parameters drivers
        
        
        """
        ...

class PythonAbstractDragForceModel(AbstractDragForceModel):
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, useFiniteDifferencesOnDensityWrtPosition: bool): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], parameters: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]:
        """
        Compute acceleration.
        
        Parameters:
            s (FieldSpacecraftState<T> s): current state information: date, kinematics, attitude
            parameters (T[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        
        """
        ...
    @typing.overload
    def acceleration(self, s: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute acceleration.
        
        Parameters:
            s (SpacecraftState): current state information: date, kinematics, attitude
            parameters (double[]): values of the force model parameters at state date, only 1 value for each parameterDriver
        
        Returns:
            acceleration in same frame as state
        
        """
        ...
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...

class PythonDragSensitive(DragSensitive):
    def __init__(self): ...
    _dragAcceleration_0__T = typing.TypeVar('_dragAcceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.FieldSpacecraftState[_dragAcceleration_0__T], density: _dragAcceleration_0__T, relativeVelocity: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T], parameters: typing.Union[typing.List[_dragAcceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_dragAcceleration_0__T]:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Specified by: dragAcceleration in interface DragSensitive
        
        Parameters:
            state (FieldSpacecraftState<T> state): current state
            density (T): atmospheric density at spacecraft position
            relativeVelocity (FieldVector3D<T> relativeVelocity): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (T[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        
        """
        ...
    @typing.overload
    def dragAcceleration(self, state: org.orekit.propagation.SpacecraftState, density: float, relativeVelocity: org.hipparchus.geometry.euclidean.threed.Vector3D, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute the acceleration due to drag.
        
        The computation includes all spacecraft specific characteristics like shape, area and coefficients.
        
        Specified by: dragAcceleration in interface DragSensitive
        
        Parameters:
            state (SpacecraftState): current state
            density (double): atmospheric density at spacecraft position
            relativeVelocity (Vector3D): relative velocity of atmosphere with respect to spacecraft, in the same inertial frame as spacecraft orbit (m/s)
            parameters (double[]): values of the force model parameters
        
        Returns:
            spacecraft acceleration in the same inertial frame as spacecraft orbit (m/s²)
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDragParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for supported parameters.
        
        Specified by: getDragParametersDrivers in interface DragSensitive
        
        Returns:
            parameters drivers
        
        
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

class TimeSpanDragForce(AbstractDragForceModel):
    DATE_BEFORE: typing.ClassVar[str] = ...
    DATE_AFTER: typing.ClassVar[str] = ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, dragSensitive: DragSensitive): ...
    @typing.overload
    def __init__(self, atmosphere: org.orekit.models.earth.atmosphere.Atmosphere, dragSensitive: DragSensitive, timeScale: org.orekit.time.TimeScale): ...
    _acceleration_0__T = typing.TypeVar('_acceleration_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acceleration(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_acceleration_0__T], tArray: typing.Union[typing.List[_acceleration_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_acceleration_0__T]: ...
    @typing.overload
    def acceleration(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def addDragSensitiveValidAfter(self, dragSensitive: DragSensitive, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def addDragSensitiveValidBefore(self, dragSensitive: DragSensitive, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...
    def extractDragSensitiveRange(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap[DragSensitive]: ...
    _extractParameters_1__T = typing.TypeVar('_extractParameters_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def extractParameters(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], absoluteDate: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]: ...
    @typing.overload
    def extractParameters(self, tArray: typing.Union[typing.List[_extractParameters_1__T], jpype.JArray], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_extractParameters_1__T]) -> typing.MutableSequence[_extractParameters_1__T]: ...
    def getDragSensitive(self, absoluteDate: org.orekit.time.AbsoluteDate) -> DragSensitive: ...
    def getDragSensitiveSpan(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TimeSpanMap.Span[DragSensitive]: ...
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
    def getFirstSpan(self) -> org.orekit.utils.TimeSpanMap.Span[DragSensitive]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.forces.drag")``.

    AbstractDragForceModel: typing.Type[AbstractDragForceModel]
    DragForce: typing.Type[DragForce]
    DragSensitive: typing.Type[DragSensitive]
    IsotropicDrag: typing.Type[IsotropicDrag]
    PythonAbstractDragForceModel: typing.Type[PythonAbstractDragForceModel]
    PythonDragSensitive: typing.Type[PythonDragSensitive]
    TimeSpanDragForce: typing.Type[TimeSpanDragForce]
