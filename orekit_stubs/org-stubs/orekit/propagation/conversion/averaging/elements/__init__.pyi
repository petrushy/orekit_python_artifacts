
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import typing



class AveragedOrbitalElements:
    """
    Interface for storing averaged orbital elements.
    
    Since:
        12.1
    """
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Write values from instance into an array of doubles.
        
        Returns:
            array with values
        
        
        """
        ...

class AveragedCircularWithMeanAngle(AveragedOrbitalElements):
    """
    Immutable class containing values of averaged circular elements from any applicable theory (with MEAN as PositionAngleType).
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalElements
    """
    def __init__(self, averagedSemiMajorAxis: float, averagedCircularEx: float, averagedCircularEy: float, averagedInclination: float, averagedRightAscensionOfTheAscendingNode: float, averagedMeanLatitudeArgument: float):
        """
        Constructor.
        
        Parameters:
            averagedSemiMajorAxis (double): averaged semi-major axis
            averagedCircularEx (double): averaged circular ex
            averagedCircularEy (double): averaged circular ey
            averagedInclination (double): averaged inclination
            averagedRightAscensionOfTheAscendingNode (double): averaged RAAN
            averagedMeanLatitudeArgument (double): averaged mean latitude argument
        
        
        """
        ...
    def getAveragedCircularEx(self) -> float:
        """
        Getter for averaged circular ex.
        
        Returns:
            ex
        
        
        """
        ...
    def getAveragedCircularEy(self) -> float:
        """
        Getter for averaged circular ey.
        
        Returns:
            ey
        
        
        """
        ...
    def getAveragedInclination(self) -> float:
        """
        Getter for averaged inclination.
        
        Returns:
            inclination
        
        
        """
        ...
    def getAveragedMeanLatitudeArgument(self) -> float:
        """
        Getter for averaged mean latitude argument.
        
        Returns:
            mean latitude argument
        
        
        """
        ...
    def getAveragedRightAscensionOfTheAscendingNode(self) -> float:
        """
        Getter for averaged RAAN.
        
        Returns:
            RAAN
        
        
        """
        ...
    def getAveragedSemiMajorAxis(self) -> float:
        """
        Getter for averaged semi-major axis.
        
        Returns:
            semi-major axis.
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Write values from instance into an array of doubles.
        
        Specified by: toArray in interface AveragedOrbitalElements
        
        Returns:
            array with values
        
        
        """
        ...

class AveragedEquinoctialWithMeanAngle(AveragedOrbitalElements):
    """
    Immutable class containing values of averaged equinoctial elements from any applicable theory (with MEAN as PositionAngleType).
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalElements
    """
    def __init__(self, averagedSemiMajorAxis: float, averagedEquinoctialEx: float, averagedEquinoctialEy: float, averagedHx: float, averagedHy: float, averagedMeanLongitudeArgument: float):
        """
        Constructor.
        
        Parameters:
            averagedSemiMajorAxis (double): semi-major axis
            averagedEquinoctialEx (double): equinoctial ex
            averagedEquinoctialEy (double): equinoctial ey
            averagedHx (double): hx
            averagedHy (double): hy
            averagedMeanLongitudeArgument (double): mean longitude argument
        
        
        """
        ...
    def getAveragedEquinoctialEx(self) -> float:
        """
        Getter for the averaged equinoctial ex.
        
        Returns:
            ex
        
        
        """
        ...
    def getAveragedEquinoctialEy(self) -> float:
        """
        Getter for the averaged equinoctial ey.
        
        Returns:
            ey
        
        
        """
        ...
    def getAveragedHx(self) -> float:
        """
        Getter for the averaged hx.
        
        Returns:
            hx
        
        
        """
        ...
    def getAveragedHy(self) -> float:
        """
        Getter for the averaged hy.
        
        Returns:
            hy
        
        
        """
        ...
    def getAveragedMeanLongitudeArgument(self) -> float:
        """
        Getter for the averaged mean longitude argument.
        
        Returns:
            mean longitude argument
        
        
        """
        ...
    def getAveragedSemiMajorAxis(self) -> float:
        """
        Getter for the averaged semi-major axis.
        
        Returns:
            semi-major axis.
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Write values from instance into an array of doubles.
        
        Specified by: toArray in interface AveragedOrbitalElements
        
        Returns:
            array with values
        
        
        """
        ...

class AveragedKeplerianWithMeanAngle(AveragedOrbitalElements):
    """
    Immutable class containing values of averaged Keplerian elements from any applicable theory (with MEAN as PositionAngleType).
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalElements
    """
    def __init__(self, averagedSemiMajorAxis: float, averagedEccentricity: float, averagedInclination: float, averagedPerigeeArgument: float, averagedRightAscensionOfTheAscendingNode: float, averagedMeanAnomaly: float):
        """
        Constructor.
        
        Parameters:
            averagedSemiMajorAxis (double): averaged semi-major axis
            averagedEccentricity (double): averaged eccentricity
            averagedInclination (double): averaged inclination
            averagedPerigeeArgument (double): averaged perigee argument
            averagedRightAscensionOfTheAscendingNode (double): averaged RAAN
            averagedMeanAnomaly (double): averaged mean anomaly
        
        
        """
        ...
    def getAveragedEccentricity(self) -> float:
        """
        Getter for the averaged eccentricity.
        
        Returns:
            eccentricity
        
        
        """
        ...
    def getAveragedInclination(self) -> float:
        """
        Getter for the averaged inclination.
        
        Returns:
            inclination
        
        
        """
        ...
    def getAveragedMeanAnomaly(self) -> float:
        """
        Getter for the averaged mean anomaly.
        
        Returns:
            mean anomaly
        
        
        """
        ...
    def getAveragedPerigeeArgument(self) -> float:
        """
        Getter for the averaged perigee argument.
        
        Returns:
            perigee argument.
        
        
        """
        ...
    def getAveragedRightAscensionOfTheAscendingNode(self) -> float:
        """
        Getter for the averaged RAAN.
        
        Returns:
            RAAN
        
        
        """
        ...
    def getAveragedSemiMajorAxis(self) -> float:
        """
        Getter for the averaged semi-major axis.
        
        Returns:
            semi-major axis
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Write values from instance into an array of doubles.
        
        Specified by: toArray in interface AveragedOrbitalElements
        
        Returns:
            array with values
        
        
        """
        ...

class PythonAveragedOrbitalElements(AveragedOrbitalElements):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.conversion.averaging.elements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Write values from instance into an array of doubles.
        
        Specified by: toArray in interface AveragedOrbitalElements
        
        Returns:
            array with values
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.averaging.elements")``.

    AveragedCircularWithMeanAngle: typing.Type[AveragedCircularWithMeanAngle]
    AveragedEquinoctialWithMeanAngle: typing.Type[AveragedEquinoctialWithMeanAngle]
    AveragedKeplerianWithMeanAngle: typing.Type[AveragedKeplerianWithMeanAngle]
    AveragedOrbitalElements: typing.Type[AveragedOrbitalElements]
    PythonAveragedOrbitalElements: typing.Type[PythonAveragedOrbitalElements]
