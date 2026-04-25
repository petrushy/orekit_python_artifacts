
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import java.util.stream
import jpype
import org
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.ode.events
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class Attitude(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['Attitude']):
    """
    This class handles attitude definition at a given date.
    
    This class represents the rotation between a reference frame and the satellite frame, as well as the spin of the satellite (axis and rotation rate).
    
    The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the spin rate into account. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
    The instance Attitude is guaranteed to be immutable.
    
    Also see:
        Orbit, AttitudeProvider
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, angularCoordinates: org.orekit.utils.AngularCoordinates): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date of attitude parameters.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date of the attitude parameters
        
        
        """
        ...
    def getOrientation(self) -> org.orekit.utils.TimeStampedAngularCoordinates:
        """
        Get the complete orientation including spin.
        
        Returns:
            complete orientation including spin
        
        Also see:
            getRotation, getSpin
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame.
        
        Returns:
            reference frame from which attitude is defined.
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the attitude rotation.
        
        Returns:
            attitude satellite rotation from reference frame.
        
        Also see:
            getOrientation, getSpin
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the satellite rotation acceleration.
        
        The rotation acceleration. vector is defined in satellite frame.
        
        Returns:
            rotation acceleration
        
        Also see:
            getOrientation, getRotation
        
        
        """
        ...
    def getSpin(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the satellite spin.
        
        The spin vector is defined in satellite frame.
        
        Returns:
            spin satellite spin (axis and velocity).
        
        Also see:
            getOrientation, getRotation
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'Attitude':
        """
        Get a time-shifted attitude.
        
        The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the spin rate into account. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new attitude, shifted with respect to the instance (which is immutable)
        
        Get a time-shifted attitude.
        
        The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the spin rate into account. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new attitude, shifted with respect to the instance (which is immutable)
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'Attitude': ...
    def withReferenceFrame(self, newReferenceFrame: org.orekit.frames.Frame) -> 'Attitude':
        """
        Get a similar attitude with a specific reference frame.
        
        If the instance reference frame is already the specified one, the instance itself is returned without any object creation. Otherwise, a new instance will be created with the specified reference frame. In this case, the required intermediate rotation and spin between the specified and the original reference frame will be inserted.
        
        Parameters:
            newReferenceFrame (Frame): desired reference frame for attitude
        
        Returns:
            an attitude that has the same orientation and motion as the instance, but guaranteed to have the specified reference
            frame
        
        
        """
        ...

class AttitudeBuilder:
    """
    This interface represents a builder for attitude.
    
    It is intended to modify raw angular coordinates when build attitudes, for example if these coordinates are not defined from the desired reference frame.
    
    Since:
        11.0
    """
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], rawAttitude: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude:
        """
        Build a filtered attitude.
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (PVCoordinatesProvider): provider for spacecraft position and velocity
            rawAttitude (TimeStampedAngularCoordinates): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], rawAttitude: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> 'FieldAttitude'[_build_1__T]:
        """
        Build a filtered attitude.
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for spacecraft position and velocity
            rawAttitude (TimeStampedFieldAngularCoordinates<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        
        """
        ...

class AttitudeInterpolator(org.orekit.time.AbstractTimeInterpolator[Attitude]):
    """
    Class for attitude interpolation.
    
    The type of interpolation used is defined by given time stamped angular coordinates interpolator at construction.
    
    Also see:
        TimeStampedAngularCoordinates, TimeInterpolator
    """
    def __init__(self, referenceFrame: org.orekit.frames.Frame, interpolator: org.orekit.time.TimeInterpolator[org.orekit.utils.TimeStampedAngularCoordinates]):
        """
        Constructor.
        
        Parameters:
            referenceFrame (Frame): reference frame from which attitude is defined
            interpolator (TimeInterpolator<TimeStampedAngularCoordinates> interpolator): time stamped angular coordinates interpolator
        
        
        """
        ...
    def getAngularInterpolator(self) -> org.orekit.time.TimeInterpolator[org.orekit.utils.TimeStampedAngularCoordinates]:
        """
        Get time stamped angular coordinates interpolator.
        
        Returns:
            time stamped angular coordinates interpolator
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get reference frame from which attitude is defined.
        
        Returns:
            reference frame from which attitude is defined
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.TimeInterpolator[org.orekit.time.TimeStamped]]: ...

class AttitudeRotationModel(org.orekit.utils.ParameterDriversProvider):
    """
    Interface for (attitude) rotation models taking as inputs a spacecraft state and model parameters. The rotation is defined between a reference frame and the satellite one.
    
    Since:
        13.0
    
    Also see:
        SpacecraftState, FieldSpacecraftState,
        Rotation,
        FieldRotation,
        Attitude, FieldAttitude,
        Maneuver
    """
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, state: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], parameters: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
        Computed the rotation given the input state and parameters' values.
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            parameters (T[]): values for parameter drivers
        
        Returns:
            attitude's rotation
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Computed the rotation given the input state and parameters' values.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            parameters (double[]): values for parameter drivers
        
        Returns:
            attitude's rotation
        
        """
        ...

class AttitudeSwitchHandler:
    """
    Interface for attitude switch notifications.
    
    This interface is intended to be implemented by users who want to be notified when an attitude switch occurs.
    
    Since:
        13.0
    
    Also see:
        AbstractSwitchingAttitudeProvider
    """
    def switchOccurred(self, preceding: 'AttitudeProvider', following: 'AttitudeProvider', state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Method called when attitude is switched from one law to another law.
        
        Parameters:
            preceding (AttitudeProvider): attitude law used preceding the switch (i.e. in the past of the switch event for a forward propagation, or in the future
                of the switch event for a backward propagation)
            following (AttitudeProvider): attitude law used following the switch (i.e. in the future of the switch event for a forward propagation, or in the past
                of the switch event for a backward propagation)
            state (SpacecraftState): state at switch time (with attitude computed using the past law)
        
        
        """
        ...

_FieldAttitude__T = typing.TypeVar('_FieldAttitude__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAttitude(org.orekit.time.FieldTimeStamped[_FieldAttitude__T], org.orekit.time.FieldTimeShiftable['FieldAttitude'[_FieldAttitude__T], _FieldAttitude__T], typing.Generic[_FieldAttitude__T]):
    """
    This class handles attitude definition at a given date.
    
    This class represents the rotation between a reference frame and the satellite frame, as well as the spin of the satellite (axis and rotation rate).
    
    The state can be slightly shifted to close dates. This shift is based on a linear extrapolation for attitude taking the spin rate into account. It is not intended as a replacement for proper attitude propagation but should be sufficient for either small time shifts or coarse accuracy.
    
    The instance Attitude is guaranteed to be immutable.
    
    Also see:
        Orbit, AttitudeProvider
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldAttitude__T], attitude: Attitude): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitude__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], frame: org.orekit.frames.Frame, fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAttitude__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], frame: org.orekit.frames.Frame, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, field2: org.hipparchus.Field[_FieldAttitude__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], frame: org.orekit.frames.Frame, fieldAngularCoordinates: org.orekit.utils.FieldAngularCoordinates[_FieldAttitude__T]): ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T]:
        """
        Get the date of attitude parameters.
        
        Specified by: getDate in interface FieldTimeStamped
        
        Returns:
            date of the attitude parameters
        
        
        """
        ...
    def getOrientation(self) -> org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitude__T]:
        """
        Get the complete orientation including spin.
        
        Returns:
            complete orientation including spin
        
        Also see:
            getRotation, getSpin
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get the reference frame.
        
        Returns:
            reference frame from which attitude is defined.
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAttitude__T]:
        """
        Get the attitude rotation.
        
        Returns:
            attitude satellite rotation from reference frame.
        
        Also see:
            getOrientation, getSpin
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]:
        """
        Get the satellite rotation acceleration.
        
        The rotation acceleration. vector is defined in satellite frame.
        
        Returns:
            rotation acceleration
        
        Also see:
            getOrientation, getRotation
        
        
        """
        ...
    def getSpin(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]:
        """
        Get the satellite spin.
        
        The spin vector is defined in satellite frame.
        
        Returns:
            spin satellite spin (axis and velocity).
        
        Also see:
            getOrientation, getRotation
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldAttitude__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAttitude__T) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    def toAttitude(self) -> Attitude:
        """
        Converts to an Attitude instance.
        
        Returns:
            Attitude with same properties
        
        
        """
        ...
    def withReferenceFrame(self, newReferenceFrame: org.orekit.frames.Frame) -> 'FieldAttitude'[_FieldAttitude__T]:
        """
        Get a similar attitude with a specific reference frame.
        
        If the instance reference frame is already the specified one, the instance itself is returned without any object creation. Otherwise, a new instance will be created with the specified reference frame. In this case, the required intermediate rotation and spin between the specified and the original reference frame will be inserted.
        
        Parameters:
            newReferenceFrame (Frame): desired reference frame for attitude
        
        Returns:
            an attitude that has the same orientation and motion as the instance, but guaranteed to have the specified reference
            frame
        
        
        """
        ...

_FieldAttitudeInterpolator__KK = typing.TypeVar('_FieldAttitudeInterpolator__KK', bound=org.hipparchus.CalculusFieldElement)  # <KK>
class FieldAttitudeInterpolator(org.orekit.time.AbstractFieldTimeInterpolator[FieldAttitude[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK], typing.Generic[_FieldAttitudeInterpolator__KK]):
    """
    Class for attitude interpolation.
    
    The type of interpolation used is defined by given time stamped angular coordinates interpolator at construction.
    
    Also see:
        TimeStampedFieldAngularCoordinates, FieldTimeInterpolator
    """
    def __init__(self, referenceFrame: org.orekit.frames.Frame, interpolator: org.orekit.time.FieldTimeInterpolator[org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK]):
        """
        Constructor.
        
        Parameters:
            referenceFrame (Frame): reference frame from which attitude is defined
            interpolator (FieldTimeInterpolator<TimeStampedFieldAngularCoordinates<FieldAttitudeInterpolator>, FieldAttitudeInterpolator> interpolator): time stamped angular coordinates interpolator
        
        
        """
        ...
    def getAngularInterpolator(self) -> org.orekit.time.FieldTimeInterpolator[org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK]:
        """
        Get time stamped angular coordinates interpolator.
        
        Returns:
            time stamped angular coordinates interpolator
        
        
        """
        ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame:
        """
        Get reference frame from which attitude is defined.
        
        Returns:
            reference frame from which attitude is defined
        
        
        """
        ...
    def getSubInterpolators(self) -> java.util.List[org.orekit.time.FieldTimeInterpolator[org.orekit.time.FieldTimeStamped[_FieldAttitudeInterpolator__KK], _FieldAttitudeInterpolator__KK]]: ...

_FieldInertia__T = typing.TypeVar('_FieldInertia__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldInertia(typing.Generic[_FieldInertia__T]):
    """
    Container for inertia of a 3D object.
    
    Instances of this class are immutable
    
    Since:
        12.0
    """
    def getInertiaAxis1(self) -> 'FieldInertiaAxis'[_FieldInertia__T]:
        """
        Get inertia along first axis.
        
        Returns:
            inertia along first axis
        
        
        """
        ...
    def getInertiaAxis2(self) -> 'FieldInertiaAxis'[_FieldInertia__T]:
        """
        Get inertia along second axis.
        
        Returns:
            inertia along second axis
        
        
        """
        ...
    def getInertiaAxis3(self) -> 'FieldInertiaAxis'[_FieldInertia__T]:
        """
        Get inertia along third axis.
        
        Returns:
            inertia along third axis
        
        
        """
        ...
    def momentum(self, rotationRate: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertia__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertia__T]:
        """
        Compute angular momentum.
        
        Parameters:
            rotationRate (FieldVector3D<FieldInertia> rotationRate): rotation rate in body frame.
        
        Returns:
            angular momentum in body frame
        
        
        """
        ...
    def swap12(self) -> 'FieldInertia'[_FieldInertia__T]:
        """
        Swap axes 1 and 2.
        
        The instance is unchanged.
        
        Returns:
            inertia with swapped axes
        
        
        """
        ...
    def swap13(self) -> 'FieldInertia'[_FieldInertia__T]:
        """
        Swap axes 1 and 3.
        
        The instance is unchanged.
        
        Returns:
            inertia with swapped axes
        
        
        """
        ...
    def swap23(self) -> 'FieldInertia'[_FieldInertia__T]:
        """
        Swap axes 2 and 3.
        
        The instance is unchanged.
        
        Returns:
            inertia with swapped axes
        
        
        """
        ...

_FieldInertiaAxis__T = typing.TypeVar('_FieldInertiaAxis__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldInertiaAxis(typing.Generic[_FieldInertiaAxis__T]):
    """
    Container for inertial axis.
    
    Instances of this class are immutable
    
    Since:
        12.0
    """
    def __init__(self, i: _FieldInertiaAxis__T, a: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertiaAxis__T]):
        """
        Simple constructor to pair a moment of inertia with its associated axis.
        
        Parameters:
            i (FieldInertiaAxis): moment of inertia
            a (FieldVector3D<FieldInertiaAxis> a): inertia axis
        
        
        """
        ...
    def getA(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldInertiaAxis__T]:
        """
        Get the inertia axis.
        
        Returns:
            inertia axis
        
        
        """
        ...
    def getI(self) -> _FieldInertiaAxis__T:
        """
        Get the moment of inertia.
        
        Returns:
            moment of inertia
        
        
        """
        ...
    def negate(self) -> 'FieldInertiaAxis'[_FieldInertiaAxis__T]:
        """
        Reverse the inertia axis.
        
        Returns:
            new container with reversed axis
        
        
        """
        ...

class Inertia:
    """
    Container for inertia of a 3D object.
    
    Instances of this class are immutable
    
    Since:
        12.0
    """
    def __init__(self, iA1: 'InertiaAxis', iA2: 'InertiaAxis', iA3: 'InertiaAxis'):
        """
        Simple constructor from principal axes.
        
        Parameters:
            iA1 (InertiaAxis): inertia along first axis
            iA2 (InertiaAxis): inertia along second axis
            iA3 (InertiaAxis): inertia along third axis
        
        
        """
        ...
    def getInertiaAxis1(self) -> 'InertiaAxis':
        """
        Get inertia along first axis.
        
        Returns:
            inertia along first axis
        
        
        """
        ...
    def getInertiaAxis2(self) -> 'InertiaAxis':
        """
        Get inertia along second axis.
        
        Returns:
            inertia along second axis
        
        
        """
        ...
    def getInertiaAxis3(self) -> 'InertiaAxis':
        """
        Get inertia along third axis.
        
        Returns:
            inertia along third axis
        
        
        """
        ...
    def momentum(self, rotationRate: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute angular momentum.
        
        Parameters:
            rotationRate (Vector3D): rotation rate in body frame.
        
        Returns:
            angular momentum in body frame
        
        
        """
        ...
    def swap12(self) -> 'Inertia':
        """
        Swap axes 1 and 2.
        
        The instance is unchanged.
        
        Returns:
            inertia with swapped axes
        
        
        """
        ...
    def swap13(self) -> 'Inertia':
        """
        Swap axes 1 and 3.
        
        The instance is unchanged.
        
        Returns:
            inertia with swapped axes
        
        
        """
        ...
    def swap23(self) -> 'Inertia':
        """
        Swap axes 2 and 3.
        
        The instance is unchanged.
        
        Returns:
            inertia with swapped axes
        
        
        """
        ...

class InertiaAxis:
    """
    Container for inertial axis.
    
    Instances of this class are immutable
    
    Since:
        12.0
    """
    def __init__(self, i: float, a: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Simple constructor to pair a moment of inertia with its associated axis.
        
        Parameters:
            i (double): moment of inertia
            a (Vector3D): inertia axis
        
        
        """
        ...
    def getA(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the inertia axis.
        
        Returns:
            inertia axis
        
        
        """
        ...
    def getI(self) -> float:
        """
        Get the moment of inertia.
        
        Returns:
            moment of inertia
        
        
        """
        ...
    def negate(self) -> 'InertiaAxis':
        """
        Reverse the inertia axis.
        
        Returns:
            new container with reversed axis
        
        
        """
        ...

class TargetProvider:
    """
    Provider for target vector.
    
    Since:
        12.2
    """
    _getDerivative2TargetDirection_0__T = typing.TypeVar('_getDerivative2TargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_getDerivative2TargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_getDerivative2TargetDirection_0__T]]: ...
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative2]: ...
    _getTargetDirection_0__T = typing.TypeVar('_getTargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetDirection(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid, pv: org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTargetDirection_0__T]:
        """
        Get a target vector.
        
        Parameters:
            sun (ExtendedPositionProvider): Sun model
            earth (OneAxisEllipsoid): Earth model
            pv (TimeStampedFieldPVCoordinates<T> pv): spacecraft position and velocity
            frame (Frame): inertial frame
        
        Returns:
            target direction in the spacecraft state frame
        
        
        """
        ...
    @typing.overload
    def getTargetDirection(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid, pv: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get a target vector.
        
        Parameters:
            sun (ExtendedPositionProvider): Sun model
            earth (OneAxisEllipsoid): Earth model
            pv (TimeStampedPVCoordinates): spacecraft position and velocity
            frame (Frame): inertial frame
        
        Returns:
            target direction in the spacecraft state frame
        
        """
        ...

class AttitudeProvider(org.orekit.propagation.events.EventDetectorsProvider, AttitudeRotationModel):
    """
    This interface represents an attitude provider model set.
    
    An attitude provider provides a way to compute an Attitude from an date and position-velocity local provider.
    """
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        Since:
            9.0
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_1__T = typing.TypeVar('_getAttitudeRotation_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, state: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], parameters: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
        input parameters as by default there is no driver. Users wanting to use them must override this.
        
        Specified by: getAttitudeRotation in interface AttitudeRotationModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            parameters (T[]): values for parameter drivers
        
        Returns:
            attitude's rotation
        
        Since:
            13.0
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_1__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_1__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        Since:
            12.0
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        Since:
            12.0
        
        Computed the rotation given the input state and parameters' values. The default implementation is independent of the input parameters as by default there is no driver. Users wanting to use them must override this.
        
        Specified by: getAttitudeRotation in interface AttitudeRotationModel
        
        Parameters:
            state (SpacecraftState): spacecraft state
            parameters (double[]): values for parameter drivers
        
        Returns:
            attitude's rotation
        
        Since:
            13.0
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        Since:
            13.0
        
        
        """
        ...

class FixedFrameBuilder(AttitudeBuilder):
    """
    Builder that assumes angular coordinates are given in a fixed frame.
    
    Since:
        11.0
    """
    def __init__(self, referenceFrame: org.orekit.frames.Frame):
        """
        Creates new instance.
        
        Parameters:
            referenceFrame (Frame): reference frame for raw attitudes
        
        
        """
        ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], rawAttitude: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude:
        """
        Build a filtered attitude.
        
        Specified by: build in interface AttitudeBuilder
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (PVCoordinatesProvider): provider for spacecraft position and velocity
            rawAttitude (TimeStampedAngularCoordinates): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], rawAttitude: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> FieldAttitude[_build_1__T]:
        """
        Build a filtered attitude.
        
        Specified by: build in interface AttitudeBuilder
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for spacecraft position and velocity
            rawAttitude (TimeStampedFieldAngularCoordinates<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        
        """
        ...

class GroundPointTarget(TargetProvider):
    """
    Ground point target for AlignedAndConstrained.
    
    Since:
        12.2
    """
    def __init__(self, location: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Simple constructor.
        
        Parameters:
            location (Vector3D): location of the target in Earth frame
        
        
        """
        ...
    _getDerivative2TargetDirection_0__T = typing.TypeVar('_getDerivative2TargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_getDerivative2TargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2[_getDerivative2TargetDirection_0__T]]: ...
    @typing.overload
    def getDerivative2TargetDirection(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[org.hipparchus.analysis.differentiation.UnivariateDerivative2]: ...
    _getTargetDirection_0__T = typing.TypeVar('_getTargetDirection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetDirection(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid, pv: org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetDirection_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTargetDirection_0__T]:
        """
        Get a target vector.
        
        Specified by: getTargetDirection in interface TargetProvider
        
        Parameters:
            sun (ExtendedPositionProvider): Sun model
            earth (OneAxisEllipsoid): Earth model
            pv (TimeStampedFieldPVCoordinates<T> pv): spacecraft position and velocity
            frame (Frame): inertial frame
        
        Returns:
            target direction in the spacecraft state frame
        
        
        """
        ...
    @typing.overload
    def getTargetDirection(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid, pv: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get a target vector.
        
        Specified by: getTargetDirection in interface TargetProvider
        
        Parameters:
            sun (ExtendedPositionProvider): Sun model
            earth (OneAxisEllipsoid): Earth model
            pv (TimeStampedPVCoordinates): spacecraft position and velocity
            frame (Frame): inertial frame
        
        Returns:
            target direction in the spacecraft state frame
        
        """
        ...

class PredefinedTarget(java.lang.Enum['PredefinedTarget'], TargetProvider):
    """
    Predefined targets for AlignedAndConstrained.
    
    Since:
        12.2
    """
    SUN: typing.ClassVar['PredefinedTarget'] = ...
    EARTH: typing.ClassVar['PredefinedTarget'] = ...
    NADIR: typing.ClassVar['PredefinedTarget'] = ...
    NORTH: typing.ClassVar['PredefinedTarget'] = ...
    EAST: typing.ClassVar['PredefinedTarget'] = ...
    VELOCITY: typing.ClassVar['PredefinedTarget'] = ...
    MOMENTUM: typing.ClassVar['PredefinedTarget'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'PredefinedTarget':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['PredefinedTarget']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (PredefinedTarget c : PredefinedTarget.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class PythonAttitudeBuilder(AttitudeBuilder):
    def __init__(self): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], rawAttitude: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude:
        """
        Build a filtered attitude.
        
        Specified by: build in interface AttitudeBuilder
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (PVCoordinatesProvider): provider for spacecraft position and velocity
            rawAttitude (TimeStampedAngularCoordinates): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        """
        ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], rawAttitude: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> FieldAttitude[_build_1__T]:
        """
        Build a filtered attitude.
        
        Specified by: build in interface AttitudeBuilder
        
        Parameters:
            frame (Frame): reference frame with respect to which attitude must be defined
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for spacecraft position and velocity
            rawAttitude (TimeStampedFieldAngularCoordinates<T> rawAttitude): raw rotation/rotation rate/rotation acceleration
        
        Returns:
            filtered attitude
        
        
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

class PythonAttitudeRotationModel(AttitudeRotationModel):
    """
    Python implementation of the AttitudeRotationModel interface. This class is part of the JCC Python interface and exposes all methods natively.
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
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, state: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], parameters: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]:
        """
        Computed the rotation given the input state and parameters' values.
        
        Specified by: getAttitudeRotation in interface AttitudeRotationModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            parameters (T[]): values for parameter drivers
        
        Returns:
            attitude's rotation
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, state: org.orekit.propagation.SpacecraftState, parameters: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Computed the rotation given the input state and parameters' values.
        
        Specified by: getAttitudeRotation in interface AttitudeRotationModel
        
        Parameters:
            state (SpacecraftState): spacecraft state
            parameters (double[]): values for parameter drivers
        
        Returns:
            attitude's rotation
        
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

class PythonAttitudeSwitchHandler(AttitudeSwitchHandler):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
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
    def switchOccurred(self, preceding: AttitudeProvider, following: AttitudeProvider, state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Description copied from interface: switchOccurred Method called when attitude is switched from one law to another law.
        
        Specified by: switchOccurred in interface AttitudeSwitchHandler
        
        Parameters:
            preceding (AttitudeProvider): attitude law used preceding the switch (i.e. in the past of the switch event for a forward propagation, or in the future
                of the switch event for a backward propagation)
            following (AttitudeProvider): attitude law used following the switch (i.e. in the future of the switch event for a forward propagation, or in the past
                of the switch event for a backward propagation)
            state (SpacecraftState): state at switch time (with attitude computed using the past law)
        
        
        """
        ...

class PythonTargetProvider(TargetProvider):
    """
    Python implementation of the TargetProvider interface. This class is part of the JCC Python interface and exposes all methods natively.
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
    _getTargetDirection_1__T = typing.TypeVar('_getTargetDirection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetDirection(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def getTargetDirection(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid, pv: org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetDirection_1__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTargetDirection_1__T]:
        """
        Get a target vector.
        
        Specified by: getTargetDirection in interface TargetProvider
        
        Parameters:
            sun (ExtendedPositionProvider): Sun model
            earth (OneAxisEllipsoid): Earth model
            pv (TimeStampedFieldPVCoordinates<T> pv): spacecraft position and velocity
            frame (Frame): inertial frame
        
        Returns:
            target direction in the spacecraft state frame
        
        
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

class AlignedAndConstrained(AttitudeProvider):
    """
    Attitude provider with one satellite vector aligned and another one constrained to two targets.
    
    Since:
        12.2
    """
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, targetProvider: typing.Union[TargetProvider, typing.Callable], vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, targetProvider2: typing.Union[TargetProvider, typing.Callable], frame: org.orekit.frames.Frame, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, targetProvider: typing.Union[TargetProvider, typing.Callable], vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, targetProvider2: typing.Union[TargetProvider, typing.Callable], extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class AttitudeProviderModifier(AttitudeProvider):
    """
    This interface represents an attitude provider that modifies/wraps another underlying provider.
    
    Since:
        5.1
    """
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getEventDetectors(self) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    @typing.overload
    def getEventDetectors(self, list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.EventDetector]: ...
    _getFieldEventDetectors_0__T = typing.TypeVar('_getFieldEventDetectors_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getFieldEventDetectors_1__T = typing.TypeVar('_getFieldEventDetectors_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_0__T]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_0__T]]: ...
    @typing.overload
    def getFieldEventDetectors(self, field: org.hipparchus.Field[_getFieldEventDetectors_1__T], list: java.util.List[org.orekit.utils.ParameterDriver]) -> java.util.stream.Stream[org.orekit.propagation.events.FieldEventDetector[_getFieldEventDetectors_1__T]]: ...
    @staticmethod
    def getFrozenAttitudeProvider(attitudeProvider: AttitudeProvider) -> 'AttitudeProviderModifier':
        """
        Wrap the input provider with a new one always returning attitudes with zero rotation rate and acceleration. It is not physically sound, but remains useful for performance when a full, physical attitude with time derivatives is not needed.
        
        Parameters:
            attitudeProvider (AttitudeProvider): provider to wrap
        
        Returns:
            wrapping provider
        
        Since:
            12.1
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface AttitudeProvider
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider:
        """
        Get the underlying attitude provider.
        
        Returns:
            underlying attitude provider
        
        
        """
        ...

class BoundedAttitudeProvider(AttitudeProvider):
    """
    This interface is intended for attitude ephemerides valid only during a time range.
    
    This interface provides a mean to retrieve an attitude at any time within a given range. It should be implemented by attitude readers based on external data files.
    
    Since:
        10.3
    """
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Returns:
            the first date of the range
        
        
        """
        ...
    @staticmethod
    def of(attitudeProvider: AttitudeProvider, interval: org.orekit.time.TimeInterval) -> 'BoundedAttitudeProvider':
        """
        Creates a bounded provider given a time interval and a standard attitude provider, with the same outputs.
        
        Parameters:
            attitudeProvider (AttitudeProvider): provider to be bounded
            interval (TimeInterval): time interval
        
        Returns:
            an instance of the interface
        
        Since:
            13.1
        
        
        """
        ...

class CelestialBodyPointed(AttitudeProvider):
    """
    This class handles a celestial body pointed attitude provider.
    
    The celestial body pointed law is defined by two main elements:
    
      - a celestial body towards which some satellite axis is exactly aimed
      - a phasing reference defining the rotation around the pointing axis
    
    The celestial body implicitly defines two of the three degrees of freedom and the phasing reference defines the remaining degree of freedom. This definition can be represented as first aligning exactly the satellite pointing axis to the current direction of the celestial body, and then to find the rotation around this axis such that the satellite phasing axis is in the half-plane defined by a cut line on the pointing axis and containing the celestial phasing reference.
    
    In order for this definition to work, the user must ensure that the phasing reference is never aligned with the pointing reference. Since the pointed body moves as the date changes, this should be ensured regardless of the date. A simple way to do this for Sun, Moon or any planet pointing is to choose a phasing reference far from the ecliptic plane. Using PLUS_K, the equatorial pole, is perfect in these cases.
    
    Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, celestialFrame: org.orekit.frames.Frame, pointedBody: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], phasingCel: org.hipparchus.geometry.euclidean.threed.Vector3D, pointingSat: org.hipparchus.geometry.euclidean.threed.Vector3D, phasingSat: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Creates new instance.
        
        Parameters:
            celestialFrame (Frame): frame in which phasingCel is defined
            pointedBody (ExtendedPositionProvider): celestial body to point at
            phasingCel (Vector3D): phasing reference, in celestial frame
            pointingSat (Vector3D): satellite vector defining the pointing direction
            phasingSat (Vector3D): phasing reference, in satellite frame
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...

class FixedRate(AttitudeProvider):
    """
    This class handles a simple attitude provider at constant rate around a fixed axis.
    
    This attitude provider is a simple linear extrapolation from an initial orientation, a rotation axis and a rotation rate. All this elements can be specified as a simple Attitude.
    
    Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, referenceAttitude: Attitude):
        """
        Creates a new instance.
        
        Parameters:
            referenceAttitude (Attitude): attitude at reference date
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    def getReferenceAttitude(self) -> Attitude:
        """
        Get the reference attitude.
        
        Returns:
            reference attitude
        
        
        """
        ...

class FrameAlignedProvider(AttitudeProvider):
    """
    This class handles an attitude provider aligned with a frame or a fixed offset to it.
    
    Instances of this class are guaranteed to be immutable.
    """
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @staticmethod
    def of(satelliteFrame: org.orekit.frames.Frame) -> AttitudeProvider:
        """
        Creates an attitude provider aligned with the given frame.
        
        This attitude provider returned by this method is designed to be as fast as possible for when attitude is irrelevant while still being a valid implementation of AttitudeProvider. To ensure good performance the specified attitude reference frame should be the same frame used for propagation so that computing the frame transformation is trivial.
        
        Parameters:
            satelliteFrame (Frame): with which the satellite is aligned.
        
        Returns:
            new attitude provider aligned with the given frame.
        
        Since:
            11.0
        
        
        """
        ...

class GroundPointing(AttitudeProvider):
    """
    Base class for ground pointing attitude providers.
    
    This class is a basic model for different kind of ground pointing attitude providers, such as : body center pointing, nadir pointing, target pointing, etc...
    
    The object GroundPointing is guaranteed to be immutable.
    
    Also see:
        AttitudeProvider
    """
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    def getBodyFrame(self) -> org.orekit.frames.Frame:
        """
        Get the body frame.
        
        Returns:
            body frame
        
        
        """
        ...

class LofOffset(AttitudeProvider):
    """
    Attitude law defined by fixed Roll, Pitch and Yaw angles (in any order) with respect to a local orbital frame.
    
    The attitude provider is defined as a rotation offset from some local orbital frame.
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, double: float, double2: float, double3: float): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
        Get the inertial frame.
        
        Returns:
            the inertial frame.
        
        
        """
        ...
    def getLof(self) -> org.orekit.frames.LOF:
        """
        Get the local orbital frame.
        
        Returns:
            the local orbital frame.
        
        
        """
        ...
    def getOffset(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotational offset.
        
        Returns:
            the rotational offset.
        
        
        """
        ...

class PythonAttitudeProvider(AttitudeProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
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

class TorqueFree(AttitudeProvider):
    """
    This class handles torque-free motion of a general (non-symmetrical) body.
    
    This attitude model is analytical, it can be called at any arbitrary date before or after the date of the initial attitude. Despite being an analytical model, it is not an approximation. It provides the attitude exactly in O(1) time.
    
    The equations are based on Landau and Lifchitz Course of Theoretical Physics, Mechanics vol 1, chapter 37. Some adaptations have been made to Landau and Lifchitz equations:
    
      - inertia can be in any order
      - initial conditions can be arbitrary
      - signs of several equations have been fixed to work for all initial conditions
      - equations have been rewritten to work in all octants
      - the φ angle model is based on a precomputed quadrature over one period computed at construction (the Landau and
        Lifchitz equations 37.17 to 37.20 seem to be wrong)
    
    The precomputed quadrature is performed numerically, but as it is performed only once at construction and the full integrated model over one period is saved, it can be applied analytically later on for any number of periods, hence we consider this attitude mode to be analytical.
    
    Since:
        12.0
    """
    def __init__(self, initialAttitude: Attitude, inertia: Inertia):
        """
        Simple constructor.
        
        Parameters:
            initialAttitude (Attitude): initial attitude
            inertia (Inertia): spacecraft inertia
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getInertia(self) -> Inertia:
        """
        Get the spacecraft inertia.
        
        Returns:
            spacecraft inertia
        
        
        """
        ...
    def getInitialAttitude(self) -> Attitude:
        """
        Get the initial attitude.
        
        Returns:
            initial attitude
        
        
        """
        ...

class AggregateBoundedAttitudeProvider(BoundedAttitudeProvider):
    """
    A BoundedAttitudeProvider that covers a larger time span from several constituent attitude providers that cover shorter time spans.
    
    Since:
        10.3
    """
    def __init__(self, providers: typing.Union[java.util.Collection[BoundedAttitudeProvider], typing.Sequence[BoundedAttitudeProvider], typing.Set[BoundedAttitudeProvider]]):
        """
        Constructor.
        
        Parameters:
            providers (Collection<? extends BoundedAttitudeProvider> providers): attitude providers that provide the backing data for this instance. There must be at least one attitude provider in the
                collection. If there are gaps between the getMaxDate of one
                attitude provider and the getMinDate of the next attitude provider
                an exception may be thrown by any method of this class at any time. If there are overlaps between the the
                getMaxDate of one attitude provider and the
                getMinDate of the next attitude provider then the attitude
                provider with the latest getMinDate is used.
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
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
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedAttitudeProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getMinDate Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedAttitudeProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface AttitudeProvider
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...

class BodyCenterPointing(GroundPointing):
    """
    This class handles body center pointing attitude provider.
    
    This class represents the attitude provider where the satellite z axis is pointing to the body frame center.
    
    The object BodyCenterPointing is guaranteed to be immutable.
    
    Also see:
        GroundPointing
    """
    def __init__(self, inertialFrame: org.orekit.frames.Frame, shape: org.orekit.bodies.Ellipsoid):
        """
        Creates new instance.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            shape (Ellipsoid): Body shape
        
        Since:
            7.1
        
        
        """
        ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...

class GroundPointingAttitudeModifier(GroundPointing, AttitudeProviderModifier):
    """
    Abstract class for attitude provider modifiers using an underlying ground pointing law.
    
    Since:
        12.1
    
    Also see:
        GroundPointing, AttitudeProviderModifier
    """
    _getBaseState_1__T = typing.TypeVar('_getBaseState_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getBaseState(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the base system state at given date, without modifications.
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which state is requested
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            satellite base attitude state.
        
        """
        ...
    @typing.overload
    def getBaseState(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getBaseState_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getBaseState_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getBaseState_1__T]:
        """
        Compute the base system state at given date, without modifications.
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which state is requested
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            satellite base attitude state.
        
        
        """
        ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> GroundPointing:
        """
        Getter for underlying ground pointing law.
        
        Specified by: getUnderlyingAttitudeProvider in interface AttitudeProviderModifier
        
        Returns:
            underlying attitude provider, which in this case is a GroundPointing instance
        
        
        """
        ...

class LofOffsetPointing(GroundPointing):
    """
    This class provides a default attitude provider.
    
    The attitude pointing law is defined by an attitude provider and the satellite axis vector chosen for pointing.
    """
    def __init__(self, inertialFrame: org.orekit.frames.Frame, shape: org.orekit.bodies.BodyShape, attLaw: AttitudeProvider, satPointingVector: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Creates new instance.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            shape (BodyShape): Body shape
            attLaw (AttitudeProvider): Attitude law
            satPointingVector (Vector3D): satellite vector defining the pointing direction
        
        Since:
            7.1
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Overrides: getAttitude in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Overrides: getAttitude in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Overrides: getAttitudeRotation in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Overrides: getAttitudeRotation in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...

class NadirPointing(GroundPointing):
    """
    This class handles nadir pointing attitude provider.
    
    This class represents the attitude provider where the satellite z axis is pointing to the vertical of the ground point under satellite.
    
    The object NadirPointing is guaranteed to be immutable.
    
    Also see:
        GroundPointing
    """
    def __init__(self, inertialFrame: org.orekit.frames.Frame, shape: org.orekit.bodies.BodyShape):
        """
        Creates new instance.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            shape (BodyShape): Body shape
        
        Since:
            7.1
        
        
        """
        ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...
    _getTargetPVViaInterpolation_0__T = typing.TypeVar('_getTargetPVViaInterpolation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPVViaInterpolation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPVViaInterpolation_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPVViaInterpolation_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPVViaInterpolation_0__T]:
        """
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): PV provider
            date (FieldAbsoluteDate<T> date): date
            frame (Frame): frame
        
        Returns:
            target position-velocity-acceleration
        
        
        """
        ...
    @typing.overload
    def getTargetPVViaInterpolation(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute target position-velocity-acceleration vector via interpolation.
        
        Parameters:
            pvProv (PVCoordinatesProvider): PV provider
            date (AbsoluteDate): date
            frame (Frame): frame
        
        Returns:
            target position-velocity-acceleration
        
        """
        ...

class PythonAttitudeProviderModifier(AttitudeProviderModifier):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider:
        """
        Get the underlying attitude provider.
        
        Specified by: getUnderlyingAttitudeProvider in interface AttitudeProviderModifier
        
        Returns:
            underlying attitude provider
        
        
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

class PythonBoundedAttitudeProvider(BoundedAttitudeProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedAttitudeProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedAttitudeProvider
        
        Returns:
            the first date of the range
        
        
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

class PythonGroundPointing(GroundPointing):
    def __init__(self, inertialFrame: org.orekit.frames.Frame, bodyFrame: org.orekit.frames.Frame):
        """
        Default constructor. Build a new instance with arbitrary default elements.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            bodyFrame (Frame): the frame that rotates with the body
        
        Since:
            7.1
        
        
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
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
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

class SpinStabilized(AttitudeProviderModifier):
    """
    This class handles a spin stabilized attitude provider.
    
    Spin stabilized laws are handled as wrappers for an underlying non-rotating law. This underlying law is typically an instance of CelestialBodyPointed with the pointing axis equal to the rotation axis, but can in fact be anything.
    
    Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, nonRotatingLaw: AttitudeProvider, start: org.orekit.time.AbsoluteDate, axis: org.hipparchus.geometry.euclidean.threed.Vector3D, rate: float):
        """
        Creates a new instance.
        
        Parameters:
            nonRotatingLaw (AttitudeProvider): underlying non-rotating attitude provider
            start (AbsoluteDate): start date of the rotation
            axis (Vector3D): rotation axis in satellite frame
            rate (double): spin rate in radians per seconds
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider:
        """
        Get the underlying attitude provider.
        
        Specified by: getUnderlyingAttitudeProvider in interface AttitudeProviderModifier
        
        Returns:
            underlying attitude provider
        
        
        """
        ...

class TabulatedLofOffset(BoundedAttitudeProvider):
    """
    This class handles an attitude provider interpolating from a predefined table containing offsets from a Local Orbital Frame.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        7.1
    
    Also see:
        LofOffset, TabulatedProvider
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOF: org.orekit.frames.LOF, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedAttitudeProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedAttitudeProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...
    def getTable(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]:
        """
        Get an unmodifiable view of the tabulated attitudes.
        
        Returns:
            unmodifiable view of the tabulated attitudes
        
        
        """
        ...

class TabulatedProvider(BoundedAttitudeProvider):
    """
    This class handles an attitude provider interpolating from a predefined table.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        6.1
    
    Also see:
        TabulatedLofOffset
    """
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, attitudeBuilder: AttitudeBuilder): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the last date of the range.
        
        Specified by: getMaxDate in interface BoundedAttitudeProvider
        
        Returns:
            the last date of the range
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the first date of the range.
        
        Specified by: getMinDate in interface BoundedAttitudeProvider
        
        Returns:
            the first date of the range
        
        
        """
        ...

class TargetPointing(GroundPointing):
    """
    This class handles target pointing attitude provider.
    
    This class represents the attitude provider where the satellite z axis is pointing to a ground point target.
    
    The target position is defined in a body frame specified by the user. It is important to make sure this frame is consistent.
    
    The object TargetPointing is guaranteed to be immutable.
    
    Also see:
        GroundPointing
    """
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, geodeticPoint: org.orekit.bodies.GeodeticPoint, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        
        """
        ...
    @typing.overload
    def getTargetPV(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Compute the target point position/velocity in specified frame.
        
        Specified by: getTargetPV in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which target point is requested
            frame (Frame): frame in which observed ground point should be provided
        
        Returns:
            observed ground point position (element 0) and velocity (at index 1) in specified frame
        
        """
        ...

class PythonGroundPointingAttitudeModifier(GroundPointingAttitudeModifier):
    """
    Python implementation of the GroundPointingAttitudeModifier abstract class. This class is part of the JCC Python interface.
    """
    def __init__(self, inertialFrame: org.orekit.frames.Frame, bodyFrame: org.orekit.frames.Frame, groundPointingLaw: GroundPointing):
        """
        Constructor.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            bodyFrame (Frame): the frame that rotates with the body
            groundPointingLaw (GroundPointing): underlying ground pointing attitude law
        
        
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

class YawCompensation(GroundPointingAttitudeModifier, AttitudeProviderModifier):
    """
    This class handles yaw compensation attitude provider.
    
    Yaw compensation is mainly used for Earth observation satellites. As a satellites moves along its track, the image of ground points move on the focal point of the optical sensor. This motion is a combination of the satellite motion, but also on the Earth rotation and on the current attitude (in particular if the pointing includes Roll or Pitch offset). In order to reduce geometrical distortion, the yaw angle is changed a little from the simple ground pointing attitude such that the apparent motion of ground points is along a prescribed axis (orthogonal to the optical sensors rows), taking into account all effects.
    
    This attitude is implemented as a wrapper on top of an underlying ground pointing law that defines the roll and pitch angles.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        GroundPointing
    """
    def __init__(self, inertialFrame: org.orekit.frames.Frame, groundPointingLaw: GroundPointing):
        """
        Creates a new instance.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            groundPointingLaw (GroundPointing): ground pointing attitude provider without yaw compensation
        
        Since:
            7.1
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Overrides: getAttitude in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Overrides: getAttitude in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...
    _getYawAngle_1__T = typing.TypeVar('_getYawAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getYawAngle(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> float:
        """
        Compute the yaw compensation angle at date.
        
        Parameters:
            pvProv (PVCoordinatesProvider): provider for PV coordinates
            date (AbsoluteDate): date at which compensation is requested
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            yaw compensation angle for orbit.
        
        """
        ...
    @typing.overload
    def getYawAngle(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getYawAngle_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getYawAngle_1__T], frame: org.orekit.frames.Frame) -> _getYawAngle_1__T:
        """
        Compute the yaw compensation angle at date.
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): provider for PV coordinates
            date (FieldAbsoluteDate<T> date): date at which compensation is requested
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            yaw compensation angle for orbit.
        
        Since:
            9.0
        
        
        """
        ...

class YawSteering(GroundPointingAttitudeModifier, AttitudeProviderModifier):
    """
    This class handles yaw steering law.
    
    Yaw steering is mainly used for low Earth orbiting satellites with no missions-related constraints on yaw angle. It sets the yaw angle in such a way the solar arrays have maximal lighting without changing the roll and pitch.
    
    The motion in yaw is smooth when the Sun is far from the orbital plane, but gets more and more square like as the Sun gets closer to the orbital plane. The degenerate extreme case with the Sun in the orbital plane leads to a yaw angle switching between two steady states, with instantaneous π radians rotations at each switch, two times per orbit. This degenerate case is clearly not operationally sound so another pointing mode is chosen when Sun comes closer than some predefined threshold to the orbital plane.
    
    This class can handle (for now) only a theoretically perfect yaw steering (i.e. the yaw angle is exactly the optimal angle). Smoothed yaw steering with a few sine waves approaching the optimal angle will be added in the future if needed.
    
    This attitude is implemented as a wrapper on top of an underlying ground pointing law that defines the roll and pitch angles.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        GroundPointing
    """
    def __init__(self, inertialFrame: org.orekit.frames.Frame, groundPointingLaw: GroundPointing, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], phasingAxis: org.hipparchus.geometry.euclidean.threed.Vector3D):
        """
        Creates a new instance.
        
        Parameters:
            inertialFrame (Frame): frame in which orbital velocities are computed
            groundPointingLaw (GroundPointing): ground pointing attitude provider without yaw compensation
            sun (ExtendedPositionProvider): sun motion model
            phasingAxis (Vector3D): satellite axis that must be roughly in Sun direction (if solar arrays rotation axis is Y, then this axis should be
                either +X or -X)
        
        Since:
            7.1
        
        
        """
        ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Overrides: getAttitude in class GroundPointing
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitude(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]:
        """
        Compute the attitude corresponding to an orbital state.
        
        Specified by: getAttitude in interface AttitudeProvider
        
        Specified by: getAttitude in interface AttitudeProviderModifier
        
        Overrides: getAttitude in class GroundPointing
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude on the specified date and position-velocity state
        
        
        """
        ...

class AttitudesSequence(org.orekit.attitudes.AbstractSwitchingAttitudeProvider):
    """
    This classes manages a sequence of different attitude providers that are activated in turn according to switching events. It includes non-zero transition durations between subsequent modes.
    
    Since:
        5.1
    
    Also see:
        AttitudesSwitcher
    """
    def __init__(self):
        """
        Constructor for an initially empty sequence.
        """
        ...
    _addSwitchingCondition__T = typing.TypeVar('_addSwitchingCondition__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addSwitchingCondition(self, past: AttitudeProvider, future: AttitudeProvider, switchEvent: _addSwitchingCondition__T, switchOnIncrease: bool, switchOnDecrease: bool, transitionTime: float, transitionFilter: org.orekit.utils.AngularDerivativesFilter, switchHandler: typing.Union[AttitudeSwitchHandler, typing.Callable]) -> None:
        """
        Add a switching condition between two attitude providers.
        
        The past and future attitude providers are defined with regard to the natural flow of time. This means that if the propagation is forward, the propagator will switch from past provider to future provider at event occurrence, but if the propagation is backward, the propagator will switch from future provider to past provider at event occurrence. The transition between the two attitude laws is not instantaneous, the switch event defines the start of the transition (i.e. when leaving the past attitude law and entering the interpolated transition law). The end of the transition (i.e. when leaving the interpolating transition law and entering the future attitude law) occurs at switch time plus transitionTime.
        
        An attitude provider may have several different switch events associated to it. Depending on which event is triggered, the appropriate provider is switched to.
        
        If the underlying detector has an event handler associated to it, this handler will be triggered (i.e. its eventOccurred method will be called), regardless of the event really triggering an attitude switch or not. As an example, if an eclipse detector is used to switch from day to night attitude mode when entering eclipse, with switchOnIncrease set to false and switchOnDecrease set to true. Then a handler set directly at eclipse detector level would be triggered at both eclipse entry and eclipse exit, but attitude switch would occur only at eclipse entry. Note that for the sake of symmetry, the transition start and end dates should match for both forward and backward propagation. This implies that for backward propagation, we have to compensate for the transitionTime when looking for the event. An unfortunate consequence is that the eventOccurred method may appear to be called out of sync with respect to the propagation (it will be called when propagator reaches transition end, despite it refers to transition start, as per transitionTime compensation), and if the method returns Action, it will stop at the end of the transition instead of at the start. For these reasons, it is not recommended to set up an event handler for events that are used to switch attitude. If an event handler is needed for other purposes, a second handler should be registered to the propagator rather than relying on the side effects of attitude switches.
        
        The smoothness of the transition between past and future attitude laws can be tuned using the transitionTime and transitionFilter parameters. The transitionTime parameter specifies how much time is spent to switch from one law to the other law. It should be larger than the event getThreshold in order to ensure attitude continuity. The transitionFilter parameter specifies the attitude time derivatives that should match at the boundaries between past attitude law and transition law on one side, and between transition law and future law on the other side. USE_R means only the rotation should be identical, USE_RR means both rotation and rotation rate should be identical, USE_RRA means both rotation, rotation rate and rotation acceleration should be identical. During the transition, the attitude law is computed by interpolating between past attitude law at switch time and future attitude law at current intermediate time.
        
        Parameters:
            past (AttitudeProvider): attitude provider applicable for times in the switch event occurrence past
            future (AttitudeProvider): attitude provider applicable for times in the switch event occurrence future
            switchEvent (T): event triggering the attitude providers switch
            switchOnIncrease (boolean): if true, switch is triggered on increasing event
            switchOnDecrease (boolean): if true, switch is triggered on decreasing event
            transitionTime (double): duration of the transition between the past and future attitude laws
            transitionFilter (AngularDerivativesFilter): specification of transition law time derivatives that should match past and future attitude laws
            switchHandler (AttitudeSwitchHandler): handler to call for notifying when switch occurs (may be null)
        
        Since:
            13.0
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        public <T extends CalculusFieldElement<T>> FieldRotation<T> getAttitudeRotation (FieldPVCoordinatesProvider<T> pvProv, FieldAbsoluteDate<T> date, Frame frame)
        
        Description copied from interface: getAttitudeRotation Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
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
    def getSwitches(self) -> java.util.List['AttitudesSequence.Switch']:
        """
        Gets a deep copy of the switches stored in this instance.
        
        Returns:
            deep copy of the switches stored in this instance
        
        
        """
        ...
    class Switch(org.orekit.attitudes.AbstractSwitchingAttitudeProvider.AbstractAttitudeSwitch):
        def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action: ...
        def g(self, spacecraftState: org.orekit.propagation.SpacecraftState) -> float: ...
        @typing.overload
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None: ...
        @typing.overload
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class AttitudesSwitcher(org.orekit.attitudes.AbstractSwitchingAttitudeProvider):
    """
    This classes manages a sequence of different attitude providers that are activated in turn according to switching events. Changes in attitude mode are instantaneous, so state derivatives need to be reset and the Action returned by the event handler is ignored.
    
    Since:
        13.0
    
    Also see:
        AttitudesSequence
    """
    def __init__(self):
        """
        Constructor for an initially empty sequence.
        """
        ...
    _addSwitchingCondition__T = typing.TypeVar('_addSwitchingCondition__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addSwitchingCondition(self, past: AttitudeProvider, future: AttitudeProvider, switchEvent: _addSwitchingCondition__T, switchOnIncrease: bool, switchOnDecrease: bool, switchHandler: typing.Union[AttitudeSwitchHandler, typing.Callable]) -> None:
        """
        Add a switching condition between two attitude providers.
        
        The past and future attitude providers are defined with regard to the natural flow of time. This means that if the propagation is forward, the propagator will switch from past provider to future provider at event occurrence, but if the propagation is backward, the propagator will switch from future provider to past provider at event occurrence.
        
        An attitude provider may have several different switch events associated to it. Depending on which event is triggered, the appropriate provider is switched to.
        
        If the underlying detector has an event handler associated to it, this handler will be triggered (i.e. its eventOccurred method will be called), regardless of the event really triggering an attitude switch or not. As an example, if an eclipse detector is used to switch from day to night attitude mode when entering eclipse, with switchOnIncrease set to false and switchOnDecrease set to true. Then a handler set directly at eclipse detector level would be triggered at both eclipse entry and eclipse exit, but attitude switch would occur only at eclipse entry.
        
        Parameters:
            past (AttitudeProvider): attitude provider applicable for times in the switch event occurrence past
            future (AttitudeProvider): attitude provider applicable for times in the switch event occurrence future
            switchEvent (T): event triggering the attitude providers switch
            switchOnIncrease (boolean): if true, switch is triggered on increasing event
            switchOnDecrease (boolean): if true, switch is triggered on decreasing event
            switchHandler (AttitudeSwitchHandler): handler to call for notifying when switch occurs (may be null)
        
        Since:
            13.0
        
        
        """
        ...
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        public <T extends CalculusFieldElement<T>> FieldRotation<T> getAttitudeRotation (FieldPVCoordinatesProvider<T> pvProv, FieldAbsoluteDate<T> date, Frame frame)
        
        Description copied from interface: getAttitudeRotation Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
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
    class InstantaneousSwitch(org.orekit.attitudes.AbstractSwitchingAttitudeProvider.AbstractAttitudeSwitch):
        def eventOccurred(self, spacecraftState: org.orekit.propagation.SpacecraftState, eventDetector: org.orekit.propagation.events.EventDetector, boolean: bool) -> org.hipparchus.ode.events.Action: ...
        @typing.overload
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate, eventDetector: org.orekit.propagation.events.EventDetector) -> None: ...
        @typing.overload
        def init(self, spacecraftState: org.orekit.propagation.SpacecraftState, absoluteDate: org.orekit.time.AbsoluteDate) -> None: ...

class PythonAbstractSwitchingAttitudeProvider(org.orekit.attitudes.AbstractSwitchingAttitudeProvider):
    """
    Python implementation of the AbstractSwitchingAttitudeProvider class. This class is part of the JCC Python interface and exposes abstract methods natively.
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
    _getAttitudeRotation_0__T = typing.TypeVar('_getAttitudeRotation_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getAttitudeRotation_2__T = typing.TypeVar('_getAttitudeRotation_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitudeRotation(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_getAttitudeRotation_0__T], tArray: typing.Union[typing.List[_getAttitudeRotation_0__T], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_0__T]: ...
    @typing.overload
    def getAttitudeRotation(self, spacecraftState: org.orekit.propagation.SpacecraftState, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (PVCoordinatesProvider): local position-velocity provider around current date
            date (AbsoluteDate): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            attitude-related rotation on the specified date and position-velocity state
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pvProv: typing.Union[org.orekit.utils.FieldPVCoordinatesProvider[_getAttitudeRotation_2__T], typing.Callable[[org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], org.orekit.frames.Frame], org.orekit.utils.TimeStampedFieldPVCoordinates[org.hipparchus.CalculusFieldElement]]], date: org.orekit.time.FieldAbsoluteDate[_getAttitudeRotation_2__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_getAttitudeRotation_2__T]:
        """
        Compute the attitude-related rotation corresponding to an orbital state.
        
        Specified by: getAttitudeRotation in interface AttitudeProvider
        
        Parameters:
            pvProv (FieldPVCoordinatesProvider<T> pvProv): local position-velocity provider around current date
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): reference frame from which attitude is computed
        
        Returns:
            rotation on the specified date and position-velocity state
        
        
        """
        ...
    @typing.overload
    def getAttitudeRotation(self, pVCoordinatesProvider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
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

class AbstractSwitchingAttitudeProvider: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.attitudes")``.

    AbstractSwitchingAttitudeProvider: typing.Type[AbstractSwitchingAttitudeProvider]
    AggregateBoundedAttitudeProvider: typing.Type[AggregateBoundedAttitudeProvider]
    AlignedAndConstrained: typing.Type[AlignedAndConstrained]
    Attitude: typing.Type[Attitude]
    AttitudeBuilder: typing.Type[AttitudeBuilder]
    AttitudeInterpolator: typing.Type[AttitudeInterpolator]
    AttitudeProvider: typing.Type[AttitudeProvider]
    AttitudeProviderModifier: typing.Type[AttitudeProviderModifier]
    AttitudeRotationModel: typing.Type[AttitudeRotationModel]
    AttitudeSwitchHandler: typing.Type[AttitudeSwitchHandler]
    AttitudesSequence: typing.Type[AttitudesSequence]
    AttitudesSwitcher: typing.Type[AttitudesSwitcher]
    BodyCenterPointing: typing.Type[BodyCenterPointing]
    BoundedAttitudeProvider: typing.Type[BoundedAttitudeProvider]
    CelestialBodyPointed: typing.Type[CelestialBodyPointed]
    FieldAttitude: typing.Type[FieldAttitude]
    FieldAttitudeInterpolator: typing.Type[FieldAttitudeInterpolator]
    FieldInertia: typing.Type[FieldInertia]
    FieldInertiaAxis: typing.Type[FieldInertiaAxis]
    FixedFrameBuilder: typing.Type[FixedFrameBuilder]
    FixedRate: typing.Type[FixedRate]
    FrameAlignedProvider: typing.Type[FrameAlignedProvider]
    GroundPointTarget: typing.Type[GroundPointTarget]
    GroundPointing: typing.Type[GroundPointing]
    GroundPointingAttitudeModifier: typing.Type[GroundPointingAttitudeModifier]
    Inertia: typing.Type[Inertia]
    InertiaAxis: typing.Type[InertiaAxis]
    LofOffset: typing.Type[LofOffset]
    LofOffsetPointing: typing.Type[LofOffsetPointing]
    NadirPointing: typing.Type[NadirPointing]
    PredefinedTarget: typing.Type[PredefinedTarget]
    PythonAbstractSwitchingAttitudeProvider: typing.Type[PythonAbstractSwitchingAttitudeProvider]
    PythonAttitudeBuilder: typing.Type[PythonAttitudeBuilder]
    PythonAttitudeProvider: typing.Type[PythonAttitudeProvider]
    PythonAttitudeProviderModifier: typing.Type[PythonAttitudeProviderModifier]
    PythonAttitudeRotationModel: typing.Type[PythonAttitudeRotationModel]
    PythonAttitudeSwitchHandler: typing.Type[PythonAttitudeSwitchHandler]
    PythonBoundedAttitudeProvider: typing.Type[PythonBoundedAttitudeProvider]
    PythonGroundPointing: typing.Type[PythonGroundPointing]
    PythonGroundPointingAttitudeModifier: typing.Type[PythonGroundPointingAttitudeModifier]
    PythonTargetProvider: typing.Type[PythonTargetProvider]
    SpinStabilized: typing.Type[SpinStabilized]
    TabulatedLofOffset: typing.Type[TabulatedLofOffset]
    TabulatedProvider: typing.Type[TabulatedProvider]
    TargetPointing: typing.Type[TargetPointing]
    TargetProvider: typing.Type[TargetProvider]
    TorqueFree: typing.Type[TorqueFree]
    YawCompensation: typing.Type[YawCompensation]
    YawSteering: typing.Type[YawSteering]
