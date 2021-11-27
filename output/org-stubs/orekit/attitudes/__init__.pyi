import java.io
import java.util
import java.util.stream
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation
import org.orekit.propagation.events
import org.orekit.time
import org.orekit.utils
import typing



class Attitude(org.orekit.time.TimeStamped, org.orekit.time.TimeShiftable['Attitude'], org.orekit.time.TimeInterpolable['Attitude'], java.io.Serializable):
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame, angularCoordinates: org.orekit.utils.AngularCoordinates): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getOrientation(self) -> org.orekit.utils.TimeStampedAngularCoordinates: ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame: ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def getSpin(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, collection: typing.Union[java.util.Collection[org.orekit.time.TimeInterpolable], typing.Sequence[org.orekit.time.TimeInterpolable], typing.Set[org.orekit.time.TimeInterpolable]]) -> org.orekit.time.TimeInterpolable: ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream['Attitude']) -> 'Attitude': ...
    def shiftedBy(self, double: float) -> 'Attitude': ...
    def withReferenceFrame(self, frame: org.orekit.frames.Frame) -> 'Attitude': ...

class AttitudeBuilder:
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude: ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> 'FieldAttitude'[_build_1__T]: ...

class AttitudeProvider:
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> 'FieldAttitude'[_getAttitude_1__T]: ...

_FieldAttitude__T = typing.TypeVar('_FieldAttitude__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAttitude(org.orekit.time.FieldTimeStamped[_FieldAttitude__T], org.orekit.time.FieldTimeShiftable['FieldAttitude'[_FieldAttitude__T], _FieldAttitude__T], org.orekit.time.FieldTimeInterpolable['FieldAttitude'[_FieldAttitude__T], _FieldAttitude__T], typing.Generic[_FieldAttitude__T]):
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
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T]: ...
    def getOrientation(self) -> org.orekit.utils.TimeStampedFieldAngularCoordinates[_FieldAttitude__T]: ...
    def getReferenceFrame(self) -> org.orekit.frames.Frame: ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldAttitude__T]: ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]: ...
    def getSpin(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAttitude__T]: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[org.hipparchus.CalculusFieldElement], collection: typing.Union[java.util.Collection[_FieldAttitude__T], typing.Sequence[_FieldAttitude__T], typing.Set[_FieldAttitude__T]]) -> _FieldAttitude__T: ...
    @typing.overload
    def interpolate(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldAttitude__T], stream: java.util.stream.Stream['FieldAttitude'[_FieldAttitude__T]]) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldAttitude__T) -> 'FieldAttitude'[_FieldAttitude__T]: ...
    def toAttitude(self) -> Attitude: ...
    def withReferenceFrame(self, frame: org.orekit.frames.Frame) -> 'FieldAttitude'[_FieldAttitude__T]: ...

class AttitudeProviderModifier(AttitudeProvider):
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider: ...

class AttitudesSequence(AttitudeProvider):
    def __init__(self): ...
    _addSwitchingCondition__T = typing.TypeVar('_addSwitchingCondition__T', bound=org.orekit.propagation.events.EventDetector)  # <T>
    def addSwitchingCondition(self, attitudeProvider: AttitudeProvider, attitudeProvider2: AttitudeProvider, t: _addSwitchingCondition__T, boolean: bool, boolean2: bool, double: float, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, switchHandler: 'AttitudesSequence.SwitchHandler') -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _registerSwitchEvents_0__T = typing.TypeVar('_registerSwitchEvents_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def registerSwitchEvents(self, field: org.hipparchus.Field[_registerSwitchEvents_0__T], fieldPropagator: org.orekit.propagation.FieldPropagator[_registerSwitchEvents_0__T]) -> None: ...
    @typing.overload
    def registerSwitchEvents(self, propagator: org.orekit.propagation.Propagator) -> None: ...
    def resetActiveProvider(self, attitudeProvider: AttitudeProvider) -> None: ...
    class SwitchHandler:
        def switchOccurred(self, attitudeProvider: AttitudeProvider, attitudeProvider2: AttitudeProvider, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

class BoundedAttitudeProvider(AttitudeProvider):
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...

class CelestialBodyPointed(AttitudeProvider):
    def __init__(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...

class FixedFrameBuilder(AttitudeBuilder):
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude: ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> FieldAttitude[_build_1__T]: ...

class FixedRate(AttitudeProvider):
    def __init__(self, attitude: Attitude): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    def getReferenceAttitude(self) -> Attitude: ...

class GroundPointing(AttitudeProvider):
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    def getBodyFrame(self) -> org.orekit.frames.Frame: ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class InertialProvider(AttitudeProvider):
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    @staticmethod
    def of(frame: org.orekit.frames.Frame) -> AttitudeProvider: ...

class LofOffset(AttitudeProvider):
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOFType: org.orekit.frames.LOFType): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOFType: org.orekit.frames.LOFType, rotationOrder: org.hipparchus.geometry.euclidean.threed.RotationOrder, double: float, double2: float, double3: float): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...

class PythonAttitudeBuilder(AttitudeBuilder):
    def __init__(self): ...
    _build_1__T = typing.TypeVar('_build_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, timeStampedAngularCoordinates: org.orekit.utils.TimeStampedAngularCoordinates) -> Attitude: ...
    @typing.overload
    def build(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_1__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_1__T]) -> FieldAttitude[_build_1__T]: ...
    _build_FFT__T = typing.TypeVar('_build_FFT__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def build_FFT(self, frame: org.orekit.frames.Frame, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_build_FFT__T], timeStampedFieldAngularCoordinates: org.orekit.utils.TimeStampedFieldAngularCoordinates[_build_FFT__T]) -> FieldAttitude[_build_FFT__T]: ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonAttitudeProvider(AttitudeProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _getAttitude_FFF__T = typing.TypeVar('_getAttitude_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getAttitude_FFF(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_FFF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_FFF__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_FFF__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class AggregateBoundedAttitudeProvider(BoundedAttitudeProvider):
    def __init__(self, collection: typing.Union[java.util.Collection[BoundedAttitudeProvider], typing.Sequence[BoundedAttitudeProvider], typing.Set[BoundedAttitudeProvider]]): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...

class BodyCenterPointing(GroundPointing):
    def __init__(self, frame: org.orekit.frames.Frame, ellipsoid: org.orekit.bodies.Ellipsoid): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class LofOffsetPointing(GroundPointing):
    def __init__(self, frame: org.orekit.frames.Frame, bodyShape: org.orekit.bodies.BodyShape, attitudeProvider: AttitudeProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class NadirPointing(GroundPointing):
    def __init__(self, frame: org.orekit.frames.Frame, bodyShape: org.orekit.bodies.BodyShape): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class PythonAttitudeProviderModifier(AttitudeProviderModifier):
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _getAttitude_FFF__T = typing.TypeVar('_getAttitude_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getAttitude_FFF(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_FFF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_FFF__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_FFF__T]: ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonBoundedAttitudeProvider(BoundedAttitudeProvider):
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _getAttitude_FFF__T = typing.TypeVar('_getAttitude_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getAttitude_FFF(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_FFF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_FFF__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_FFF__T]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonGroundPointing(GroundPointing):
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame): ...
    def finalize(self) -> None: ...
    _getTargetPV_1__T = typing.TypeVar('_getTargetPV_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_1__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_1__T]: ...
    _getTargetPV_FFF__T = typing.TypeVar('_getTargetPV_FFF__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    def getTargetPV_FFF(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_FFF__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_FFF__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_FFF__T]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonSwitchHandler(AttitudesSequence.SwitchHandler):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    def switchOccurred(self, attitudeProvider: AttitudeProvider, attitudeProvider2: AttitudeProvider, spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

class SpinStabilized(AttitudeProviderModifier):
    def __init__(self, attitudeProvider: AttitudeProvider, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider: ...

class TabulatedLofOffset(BoundedAttitudeProvider):
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOFType: org.orekit.frames.LOFType, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, lOFType: org.orekit.frames.LOFType, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getTable(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]: ...

class TabulatedProvider(BoundedAttitudeProvider):
    @typing.overload
    def __init__(self, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, attitudeBuilder: AttitudeBuilder): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, list: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...

class TargetPointing(GroundPointing):
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, geodeticPoint: org.orekit.bodies.GeodeticPoint, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, frame: org.orekit.frames.Frame, frame2: org.orekit.frames.Frame, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class YawCompensation(GroundPointing, AttitudeProviderModifier):
    def __init__(self, frame: org.orekit.frames.Frame, groundPointing: GroundPointing): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _getBaseState_1__T = typing.TypeVar('_getBaseState_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getBaseState(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getBaseState(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getBaseState_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getBaseState_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getBaseState_1__T]: ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider: ...
    _getYawAngle_1__T = typing.TypeVar('_getYawAngle_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getYawAngle(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getYawAngle(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getYawAngle_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getYawAngle_1__T], frame: org.orekit.frames.Frame) -> _getYawAngle_1__T: ...

class YawSteering(GroundPointing, AttitudeProviderModifier):
    def __init__(self, frame: org.orekit.frames.Frame, groundPointing: GroundPointing, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    _getAttitude_1__T = typing.TypeVar('_getAttitude_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAttitude(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getAttitude(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getAttitude_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getAttitude_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getAttitude_1__T]: ...
    _getBaseState_1__T = typing.TypeVar('_getBaseState_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getBaseState(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> Attitude: ...
    @typing.overload
    def getBaseState(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getBaseState_1__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getBaseState_1__T], frame: org.orekit.frames.Frame) -> FieldAttitude[_getBaseState_1__T]: ...
    _getTargetPV_0__T = typing.TypeVar('_getTargetPV_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTargetPV(self, fieldPVCoordinatesProvider: org.orekit.utils.FieldPVCoordinatesProvider[_getTargetPV_0__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTargetPV_0__T], frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getTargetPV_0__T]: ...
    @typing.overload
    def getTargetPV(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, absoluteDate: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.orekit.utils.TimeStampedPVCoordinates: ...
    def getUnderlyingAttitudeProvider(self) -> AttitudeProvider: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.attitudes")``.

    AggregateBoundedAttitudeProvider: typing.Type[AggregateBoundedAttitudeProvider]
    Attitude: typing.Type[Attitude]
    AttitudeBuilder: typing.Type[AttitudeBuilder]
    AttitudeProvider: typing.Type[AttitudeProvider]
    AttitudeProviderModifier: typing.Type[AttitudeProviderModifier]
    AttitudesSequence: typing.Type[AttitudesSequence]
    BodyCenterPointing: typing.Type[BodyCenterPointing]
    BoundedAttitudeProvider: typing.Type[BoundedAttitudeProvider]
    CelestialBodyPointed: typing.Type[CelestialBodyPointed]
    FieldAttitude: typing.Type[FieldAttitude]
    FixedFrameBuilder: typing.Type[FixedFrameBuilder]
    FixedRate: typing.Type[FixedRate]
    GroundPointing: typing.Type[GroundPointing]
    InertialProvider: typing.Type[InertialProvider]
    LofOffset: typing.Type[LofOffset]
    LofOffsetPointing: typing.Type[LofOffsetPointing]
    NadirPointing: typing.Type[NadirPointing]
    PythonAttitudeBuilder: typing.Type[PythonAttitudeBuilder]
    PythonAttitudeProvider: typing.Type[PythonAttitudeProvider]
    PythonAttitudeProviderModifier: typing.Type[PythonAttitudeProviderModifier]
    PythonBoundedAttitudeProvider: typing.Type[PythonBoundedAttitudeProvider]
    PythonGroundPointing: typing.Type[PythonGroundPointing]
    PythonSwitchHandler: typing.Type[PythonSwitchHandler]
    SpinStabilized: typing.Type[SpinStabilized]
    TabulatedLofOffset: typing.Type[TabulatedLofOffset]
    TabulatedProvider: typing.Type[TabulatedProvider]
    TargetPointing: typing.Type[TargetPointing]
    YawCompensation: typing.Type[YawCompensation]
    YawSteering: typing.Type[YawSteering]
