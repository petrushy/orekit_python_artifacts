
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
    Class for measurements generation.
    
    Since:
        2.0
    
    Also see:
        SensorToSensorMapping,
        SensorToGroundMapping
    """
    def __init__(self, nbModels: int):
        """
        Build a new instance.
        
        Parameters:
            nbModels (int): number of viewing models to map
        
        
        """
        ...
    def addGroundMapping(self, groundMapping: 'SensorToGroundMapping') -> None:
        """
        Add a ground mapping.
        
        A ground mapping is defined by a set of GCPs.
        
        Parameters:
            groundMapping (SensorToGroundMapping): sensor to ground mapping
        
        
        """
        ...
    def addInterMapping(self, interMapping: 'SensorToSensorMapping') -> None:
        """
        Add a mapping between two viewing models.
        
        Parameters:
            interMapping (SensorToSensorMapping): sensor to sensor mapping
        
        
        """
        ...
    def getGroundMapping(self, ruggedName: str, sensorName: str) -> 'SensorToGroundMapping':
        """
        Get a ground Mapping for a sensor.
        
        Parameters:
            ruggedName (String): Rugged name
            sensorName (String): sensor name
        
        Returns:
            selected ground mapping or null if sensor is not found
        
        
        """
        ...
    def getGroundMappings(self) -> java.util.Collection['SensorToGroundMapping']:
        """
        Get all the ground mapping entries.
        
        Returns:
            an unmodifiable view of all mapping entries
        
        
        """
        ...
    def getInterMapping(self, ruggedNameA: str, sensorNameA: str, ruggedNameB: str, sensorNameB: str) -> 'SensorToSensorMapping':
        """
        Get a sensor mapping for a sensor.
        
        returns sensor to sensor mapping associated with specific sensors and related rugged instance.
        
        Parameters:
            ruggedNameA (String): Rugged name A
            sensorNameA (String): sensor name A
            ruggedNameB (String): Rugged name B
            sensorNameB (String): sensor name B
        
        Returns:
            selected ground mapping or null if a sensor is not found
        
        
        """
        ...
    def getInterMappings(self) -> java.util.Collection['SensorToSensorMapping']:
        """
        Get the sensor to sensor values.
        
        Returns:
            the inter-mappings
        
        
        """
        ...
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
    Container for mapping sensor pixels with sensor pixels or ground points.
    
    Since:
        2.0
    """
    @typing.overload
    def __init__(self, sensorName: str): ...
    @typing.overload
    def __init__(self, sensorName: str, ruggedName: str): ...
    def addMapping(self, pixel: org.orekit.rugged.linesensor.SensorPixel, point: _SensorMapping__T) -> None:
        """
        Add a mapping between a sensor pixel and another point (sensor pixel or ground point).
        
        Parameters:
            pixel (SensorPixel): sensor pixel
            point (SensorMapping): sensor pixel or ground point corresponding to the sensor pixel
        
        
        """
        ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, _SensorMapping__T]]:
        """
        Get all the mapping entries.
        
        Returns:
            an unmodifiable view of all mapping entries
        
        
        """
        ...
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
    Container for mapping between sensor pixels and ground points.
    
    Since:
        2.0
    
    Also see:
        SensorMapping
    """
    @typing.overload
    def __init__(self, sensorName: str): ...
    @typing.overload
    def __init__(self, ruggedName: str, sensorName: str): ...
    def addMapping(self, pixel: org.orekit.rugged.linesensor.SensorPixel, groundPoint: org.orekit.bodies.GeodeticPoint) -> None:
        """
        Add a mapping between one sensor pixel and one ground point.
        
        Parameters:
            pixel (SensorPixel): sensor pixel
            groundPoint (org.orekit.bodies.GeodeticPoint): ground point corresponding to the sensor pixel
        
        
        """
        ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, org.orekit.bodies.GeodeticPoint]]:
        """
        Get all the mapping entries.
        
        Returns:
            an unmodifiable view of all mapping entries
        
        
        """
        ...
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
    Container for mapping sensors pixels of two viewing models. Store the distance between both lines of sight computed with distanceBetweenLOS
    
    Constraints in relation to central body distance can be added.
    
    Since:
        2.0
    
    Also see:
        SensorMapping
    """
    @typing.overload
    def __init__(self, sensorNameA: str, sensorNameB: str): ...
    @typing.overload
    def __init__(self, sensorNameA: str, sensorNameB: str, bodyConstraintWeight: float): ...
    @typing.overload
    def __init__(self, sensorNameA: str, ruggedNameA: str, sensorNameB: str, ruggedNameB: str): ...
    @typing.overload
    def __init__(self, sensorNameA: str, ruggedNameA: str, sensorNameB: str, ruggedNameB: str, bodyConstraintWeight: float): ...
    @typing.overload
    def addMapping(self, pixelA: org.orekit.rugged.linesensor.SensorPixel, pixelB: org.orekit.rugged.linesensor.SensorPixel, losDistance: float) -> None:
        """
        Parameters:
            pixelA (SensorPixel): sensor pixel A
            pixelB (SensorPixel): sensor pixel B corresponding to the sensor pixel A (by direct then inverse location)
            losDistance (Double): distance between the two lines of sight
        
        Add a mapping between two sensor pixels (A and B) and corresponding distance between the LOS and the central body distance constraint associated with pixel A.
        
        Parameters:
            pixelA (SensorPixel): sensor pixel A
            pixelB (SensorPixel): sensor pixel B corresponding to the sensor pixel A (by direct then inverse location)
            losDistance (Double): distance between the two lines of sight
            bodyDistance (Double): elevation to central body
        
        
        """
        ...
    @typing.overload
    def addMapping(self, pixelA: org.orekit.rugged.linesensor.SensorPixel, pixelB: org.orekit.rugged.linesensor.SensorPixel, losDistance: float, bodyDistance: float) -> None: ...
    def getBodyConstraintWeight(self) -> float:
        """
        Get the weight given to the central body distance constraint with respect to the LOS distance.
        
        Returns:
            the central body constraint weight
        
        
        """
        ...
    def getBodyDistance(self, idx: int) -> float:
        """
        Get distance between central body and pixel A, corresponding to the inter-mapping index.
        
        Parameters:
            idx (int): inter-mapping index
        
        Returns:
            the central body distances at index idx
        
        
        """
        ...
    def getBodyDistances(self) -> java.util.List[float]:
        """
        Get distances between central body and pixel A (mapping with constraints).
        
        Returns:
            the central body distances
        
        
        """
        ...
    def getLosDistance(self, idx: int) -> float:
        """
        Get distance between LOS, corresponding to the inter-mapping index.
        
        Parameters:
            idx (int): inter-mapping index
        
        Returns:
            the LOS distance at index idx
        
        
        """
        ...
    def getLosDistances(self) -> java.util.List[float]:
        """
        Get distances between lines of sight (from both view).
        
        Returns:
            the LOS distances
        
        
        """
        ...
    def getMapping(self) -> java.util.Set[java.util.Map.Entry[org.orekit.rugged.linesensor.SensorPixel, org.orekit.rugged.linesensor.SensorPixel]]:
        """
        Get all the inter-mapping entries.
        
        Returns:
            an unmodifiable view of all mapping entries
        
        
        """
        ...
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
    def setBodyConstraintWeight(self, bodyConstraintWeight: float) -> None:
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
