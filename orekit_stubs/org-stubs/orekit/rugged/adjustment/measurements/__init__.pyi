
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.orekit.bodies
import org.orekit.rugged.linesensor
import typing



class Observables:
    """
    public class Observables extends :class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class for measurements generation.
    
        Since:
            2.0
    
        Also see:
            :class:`~org.orekit.rugged.adjustment.measurements.SensorToSensorMapping`,
            :class:`~org.orekit.rugged.adjustment.measurements.SensorToGroundMapping`
    """
    def __init__(self, int: int): ...
    def addGroundMapping(self, sensorToGroundMapping: 'SensorToGroundMapping') -> None:
        """
            Add a ground mapping.
        
            A ground mapping is defined by a set of GCPs.
        
            Parameters:
                groundMapping (:class:`~org.orekit.rugged.adjustment.measurements.SensorToGroundMapping`): sensor to ground mapping
        
        
        """
        ...
    def addInterMapping(self, sensorToSensorMapping: 'SensorToSensorMapping') -> None:
        """
            Add a mapping between two viewing models.
        
            Parameters:
                interMapping (:class:`~org.orekit.rugged.adjustment.measurements.SensorToSensorMapping`): sensor to sensor mapping
        
        
        """
        ...
    def getGroundMapping(self, string: str, string2: str) -> 'SensorToGroundMapping':
        """
            Get a ground Mapping for a sensor.
        
            Parameters:
                ruggedName (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Rugged name
                sensorName (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): sensor name
        
            Returns:
                selected ground mapping or null if sensor is not found
        
        
        """
        ...
    def getGroundMappings(self) -> java.util.Collection['SensorToGroundMapping']: ...
    def getInterMapping(self, string: str, string2: str, string3: str, string4: str) -> 'SensorToSensorMapping':
        """
            Get a sensor mapping for a sensor.
        
            returns sensor to sensor mapping associated with specific sensors and related rugged instance.
        
            Parameters:
                ruggedNameA (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Rugged name A
                sensorNameA (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): sensor name A
                ruggedNameB (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): Rugged name B
                sensorNameB (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): sensor name B
        
            Returns:
                selected ground mapping or null if a sensor is not found
        
        
        """
        ...
    def getInterMappings(self) -> java.util.Collection['SensorToSensorMapping']: ...
    def getNbModels(self) -> int:
        """
            Get the number of viewing models to map.
        
            Returns:
                the number of viewing models to map
        
        
        """
        ...

_SensorMapping__T = typing.TypeVar('_SensorMapping__T')  # <T>
class SensorMapping(typing.Generic[_SensorMapping__T]):
    """
    public class SensorMapping<T> extends :class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for mapping sensor pixels with sensor pixels or ground points.
    
        Since:
            2.0
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, t: _SensorMapping__T) -> None:
        """
            Add a mapping between a sensor pixel and another point (sensor pixel or ground point).
        
            Parameters:
                pixel (:class:`~org.orekit.rugged.linesensor.SensorPixel`): sensor pixel
                point (:class:`~org.orekit.rugged.adjustment.measurements.SensorMapping`): sensor pixel or ground point corresponding to the sensor pixel
        
        
        """
        ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, _SensorMapping__T]]: ...
    def getRuggedName(self) -> str:
        """
            Get the name of the Rugged to which mapping applies.
        
            Returns:
                name of the Rugged to which mapping applies
        
        
        """
        ...
    def getSensorName(self) -> str:
        """
            Get the name of the sensor to which mapping applies.
        
            Returns:
                name of the sensor to which mapping applies
        
        
        """
        ...

class SensorToGroundMapping:
    """
    public class SensorToGroundMapping extends :class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for mapping between sensor pixels and ground points.
    
        Since:
            2.0
    
        Also see:
            :class:`~org.orekit.rugged.adjustment.measurements.SensorMapping`
    """
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, geodeticPoint: org.orekit.bodies.GeodeticPoint) -> None:
        """
            Add a mapping between one sensor pixel and one ground point.
        
            Parameters:
                pixel (:class:`~org.orekit.rugged.linesensor.SensorPixel`): sensor pixel
                groundPoint (org.orekit.bodies.GeodeticPoint): ground point corresponding to the sensor pixel
        
        
        """
        ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, org.orekit.bodies.GeodeticPoint]]: ...
    def getRuggedName(self) -> str:
        """
            Get the name of the Rugged to which mapping applies.
        
            Returns:
                name of the Rugged to which mapping applies
        
        
        """
        ...
    def getSensorName(self) -> str:
        """
            Get the name of the sensor to which mapping applies.
        
            Returns:
                name of the sensor to which mapping applies
        
        
        """
        ...

class SensorToSensorMapping:
    """
    public class SensorToSensorMapping extends :class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for mapping sensors pixels of two viewing models. Store the distance between both lines of sight computed with
        :meth:`~org.orekit.rugged.api.Rugged.distanceBetweenLOS`
    
        Constraints in relation to central body distance can be added.
    
        Since:
            2.0
    
        Also see:
            :class:`~org.orekit.rugged.adjustment.measurements.SensorMapping`
    """
    @typing.overload
    def __init__(self, string: str, string2: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, double: float): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, double: float): ...
    @typing.overload
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, sensorPixel2: org.orekit.rugged.linesensor.SensorPixel, double: float) -> None:
        """
            Add a mapping between two sensor pixels (A and B) and corresponding distance between the LOS.
        
            Parameters:
                pixelA (:class:`~org.orekit.rugged.linesensor.SensorPixel`): sensor pixel A
                pixelB (:class:`~org.orekit.rugged.linesensor.SensorPixel`): sensor pixel B corresponding to the sensor pixel A (by direct then inverse location)
                losDistance (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double?is`): distance between the two lines of sight
        
            Add a mapping between two sensor pixels (A and B) and corresponding distance between the LOS and the central body
            distance constraint associated with pixel A.
        
            Parameters:
                pixelA (:class:`~org.orekit.rugged.linesensor.SensorPixel`): sensor pixel A
                pixelB (:class:`~org.orekit.rugged.linesensor.SensorPixel`): sensor pixel B corresponding to the sensor pixel A (by direct then inverse location)
                losDistance (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double?is`): distance between the two lines of sight
                bodyDistance (:class:`~org.orekit.rugged.adjustment.measurements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Double?is`): elevation to central body
        
        
        """
        ...
    @typing.overload
    def addMapping(self, sensorPixel: org.orekit.rugged.linesensor.SensorPixel, sensorPixel2: org.orekit.rugged.linesensor.SensorPixel, double: float, double2: float) -> None: ...
    def getBodyConstraintWeight(self) -> float:
        """
            Get the weight given to the central body distance constraint with respect to the LOS distance.
        
            Returns:
                the central body constraint weight
        
        
        """
        ...
    def getBodyDistance(self, int: int) -> float:
        """
            Get distance between central body and pixel A, corresponding to the inter-mapping index.
        
            Parameters:
                idx (int): inter-mapping index
        
            Returns:
                the central body distances at index idx
        
        
        """
        ...
    def getBodyDistances(self) -> java.util.List[float]: ...
    def getLosDistance(self, int: int) -> float:
        """
            Get distance between LOS, corresponding to the inter-mapping index.
        
            Parameters:
                idx (int): inter-mapping index
        
            Returns:
                the LOS distance at index idx
        
        
        """
        ...
    def getLosDistances(self) -> java.util.List[float]: ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, org.orekit.rugged.linesensor.SensorPixel]]: ...
    def getRuggedNameA(self) -> str:
        """
            Get the name of the Rugged A to which mapping applies.
        
            Returns:
                name of the Rugged A to which mapping applies
        
        
        """
        ...
    def getRuggedNameB(self) -> str:
        """
            Get the name of the Rugged B to which mapping applies.
        
            Returns:
                name of the Rugged B to which mapping applies
        
        
        """
        ...
    def getSensorNameA(self) -> str:
        """
            Get the name of the sensor A to which mapping applies.
        
            Returns:
                name of the sensor A to which mapping applies
        
        
        """
        ...
    def getSensorNameB(self) -> str:
        """
            Get the name of the sensor B to which mapping applies.
        
            Returns:
                name of the sensor B to which mapping applies
        
        
        """
        ...
    def setBodyConstraintWeight(self, double: float) -> None:
        """
            Set the central body constraint weight.
        
            Parameters:
                bodyConstraintWeight (double): the central body constraint weight to set
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.adjustment.measurements")``.

    Observables: typing.Type[Observables]
    SensorMapping: typing.Type[SensorMapping]
    SensorToGroundMapping: typing.Type[SensorToGroundMapping]
    SensorToSensorMapping: typing.Type[SensorToSensorMapping]
