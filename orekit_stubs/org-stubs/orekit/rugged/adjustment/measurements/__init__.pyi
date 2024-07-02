import java.util
import org.orekit.bodies
import org.orekit.rugged.linesensor
import typing



class Observables:
    def __init__(self, int: int): ...
    def addGroundMapping(self, sensorToGroundMapping: 'SensorToGroundMapping') -> None: ...
    def addInterMapping(self, sensorToSensorMapping: 'SensorToSensorMapping') -> None: ...
    def getGroundMapping(self, string: str, string2: str) -> 'SensorToGroundMapping': ...
    def getGroundMappings(self) -> java.util.Collection['SensorToGroundMapping']: ...
    def getInterMapping(self, string: str, string2: str, string3: str, string4: str) -> 'SensorToSensorMapping': ...
    def getInterMappings(self) -> java.util.Collection['SensorToSensorMapping']: ...
    def getNbModels(self) -> int: ...

_SensorMapping__T = typing.TypeVar('_SensorMapping__T')  # <T>
class SensorMapping(typing.Generic[_SensorMapping__T]):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, t: _SensorMapping__T) -> None: ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, _SensorMapping__T]]: ...
    def getRuggedName(self) -> str: ...
    def getSensorName(self) -> str: ...

class SensorToGroundMapping:
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> None: ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, org.orekit.bodies.GeodeticPoint]]: ...
    def getRuggedName(self) -> str: ...
    def getSensorName(self) -> str: ...

class SensorToSensorMapping:
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, double: float): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, double: float): ...
    @typing.overload
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, sensorPixel2: org.orekit.rugged.linesensor.SensorPixel, double: float) -> None: ...
    @typing.overload
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, sensorPixel2: org.orekit.rugged.linesensor.SensorPixel, double: float, double2: float) -> None: ...
    def getBodyConstraintWeight(self) -> float: ...
    def getBodyDistance(self, int: int) -> float: ...
    def getBodyDistances(self) -> java.util.List[float]: ...
    def getLosDistance(self, int: int) -> float: ...
    def getLosDistances(self) -> java.util.List[float]: ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, org.orekit.rugged.linesensor.SensorPixel]]: ...
    def getRuggedNameA(self) -> str: ...
    def getRuggedNameB(self) -> str: ...
    def getSensorNameA(self) -> str: ...
    def getSensorNameB(self) -> str: ...
    def setBodyConstraintWeight(self, double: float) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.adjustment.measurements")``.

    Observables: typing.Type[Observables]
    SensorMapping: typing.Type[SensorMapping]
    SensorToGroundMapping: typing.Type[SensorToGroundMapping]
    SensorToSensorMapping: typing.Type[SensorToSensorMapping]
