import java.io
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.models.earth.atmosphere.data
import org.orekit.time
import org.orekit.utils
import typing



class Atmosphere(java.io.Serializable):
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    _getVelocity_0__T = typing.TypeVar('_getVelocity_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getVelocity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getVelocity_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T]: ...
    @typing.overload
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class DTM2000InputParameters(java.io.Serializable):
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getInstantFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...

class JB2008InputParameters(java.io.Serializable):
    def getDSTDTC(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getF10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getF10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getS10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getS10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getXM10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getXM10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getY10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getY10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...

class NRLMSISE00InputParameters(java.io.Serializable):
    def getAp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...

class DTM2000(Atmosphere):
    @typing.overload
    def __init__(self, dTM2000InputParameters: DTM2000InputParameters, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, dTM2000InputParameters: DTM2000InputParameters, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, bodyShape: org.orekit.bodies.BodyShape, timeScale: org.orekit.time.TimeScale): ...
    _getDensity_2__T = typing.TypeVar('_getDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getDensity_3__T = typing.TypeVar('_getDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, int: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float) -> float: ...
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, int: int, t: _getDensity_2__T, t2: _getDensity_2__T, t3: _getDensity_2__T, t4: _getDensity_2__T, double: float, double2: float, double3: float, double4: float) -> _getDensity_2__T: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_3__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_3__T], frame: org.orekit.frames.Frame) -> _getDensity_3__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...

class HarrisPriester(Atmosphere):
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, doubleArray: typing.List[typing.List[float]], double2: float): ...
    _getDensity_2__T = typing.TypeVar('_getDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getDensity_3__T = typing.TypeVar('_getDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float: ...
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_2__T]) -> _getDensity_2__T: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_3__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_3__T], frame: org.orekit.frames.Frame) -> _getDensity_3__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def getMaxAlt(self) -> float: ...
    def getMinAlt(self) -> float: ...
    def getTabDensity(self) -> typing.List[typing.List[float]]: ...

class JB2008(Atmosphere):
    @typing.overload
    def __init__(self, jB2008InputParameters: JB2008InputParameters, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, jB2008InputParameters: JB2008InputParameters, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, bodyShape: org.orekit.bodies.BodyShape, timeScale: org.orekit.time.TimeScale): ...
    _getDensity_2__T = typing.TypeVar('_getDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getDensity_3__T = typing.TypeVar('_getDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, double11: float, double12: float, double13: float, double14: float, double15: float) -> float: ...
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, t: _getDensity_2__T, t2: _getDensity_2__T, t3: _getDensity_2__T, t4: _getDensity_2__T, t5: _getDensity_2__T, t6: _getDensity_2__T, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float) -> _getDensity_2__T: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_3__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_3__T], frame: org.orekit.frames.Frame) -> _getDensity_3__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...

_NRLMSISE00__FieldOutput__T = typing.TypeVar('_NRLMSISE00__FieldOutput__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class NRLMSISE00(Atmosphere):
    @typing.overload
    def __init__(self, nRLMSISE00InputParameters: NRLMSISE00InputParameters, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, bodyShape: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, nRLMSISE00InputParameters: NRLMSISE00InputParameters, pVCoordinatesProvider: org.orekit.utils.PVCoordinatesProvider, bodyShape: org.orekit.bodies.BodyShape, timeScale: org.orekit.time.TimeScale): ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    def withSwitch(self, int: int, int2: int) -> 'NRLMSISE00': ...
    class FieldOutput(typing.Generic[_NRLMSISE00__FieldOutput__T]):
        def getDensity(self, int: int) -> _NRLMSISE00__FieldOutput__T: ...

class PythonAtmosphere(Atmosphere):
    def __init__(self): ...
    def finalize(self) -> None: ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...
    _getVelocity_0__T = typing.TypeVar('_getVelocity_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getVelocity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getVelocity_0__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T]: ...
    @typing.overload
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonDTM2000InputParameters(DTM2000InputParameters):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def get24HoursKp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getInstantFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMeanFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getThreeHourlyKP(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonJB2008InputParameters(JB2008InputParameters):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDSTDTC(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getF10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getF10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getS10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getS10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getXM10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getXM10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getY10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getY10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonNRLMSISE00InputParameters(NRLMSISE00InputParameters):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getAp(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]: ...
    def getAverageFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getDailyFlux(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class SimpleExponentialAtmosphere(Atmosphere):
    def __init__(self, bodyShape: org.orekit.bodies.BodyShape, double: float, double2: float, double3: float): ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T: ...
    def getFrame(self) -> org.orekit.frames.Frame: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.atmosphere")``.

    Atmosphere: typing.Type[Atmosphere]
    DTM2000: typing.Type[DTM2000]
    DTM2000InputParameters: typing.Type[DTM2000InputParameters]
    HarrisPriester: typing.Type[HarrisPriester]
    JB2008: typing.Type[JB2008]
    JB2008InputParameters: typing.Type[JB2008InputParameters]
    NRLMSISE00: typing.Type[NRLMSISE00]
    NRLMSISE00InputParameters: typing.Type[NRLMSISE00InputParameters]
    PythonAtmosphere: typing.Type[PythonAtmosphere]
    PythonDTM2000InputParameters: typing.Type[PythonDTM2000InputParameters]
    PythonJB2008InputParameters: typing.Type[PythonJB2008InputParameters]
    PythonNRLMSISE00InputParameters: typing.Type[PythonNRLMSISE00InputParameters]
    SimpleExponentialAtmosphere: typing.Type[SimpleExponentialAtmosphere]
    data: org.orekit.models.earth.atmosphere.data.__module_protocol__
