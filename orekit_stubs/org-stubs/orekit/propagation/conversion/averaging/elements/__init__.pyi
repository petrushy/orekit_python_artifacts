import org.orekit.propagation.conversion.averaging.elements.class-use
import typing



class AveragedOrbitalElements:
    """
    public interface AveragedOrbitalElements
    
        Interface for storing averaged orbital elements.
    
        Since:
            12.1
    """
    def toArray(self) -> typing.List[float]:
        """
            Write values from instance into an array of doubles.
        
            Returns:
                array with values
        
        
        """
        ...

class AveragedCircularWithMeanAngle(AveragedOrbitalElements):
    """
    public class AveragedCircularWithMeanAngle extends :class:`~org.orekit.propagation.conversion.averaging.elements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    
        Immutable class containing values of averaged circular elements from any applicable theory (with MEAN as
        :class:`~org.orekit.orbits.PositionAngleType`).
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
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
    def toArray(self) -> typing.List[float]:
        """
            Write values from instance into an array of doubles.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements.toArray` in
                interface :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
        
            Returns:
                array with values
        
        
        """
        ...

class AveragedEquinoctialWithMeanAngle(AveragedOrbitalElements):
    """
    public class AveragedEquinoctialWithMeanAngle extends :class:`~org.orekit.propagation.conversion.averaging.elements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    
        Immutable class containing values of averaged equinoctial elements from any applicable theory (with MEAN as
        :class:`~org.orekit.orbits.PositionAngleType`).
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
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
    def toArray(self) -> typing.List[float]:
        """
            Write values from instance into an array of doubles.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements.toArray` in
                interface :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
        
            Returns:
                array with values
        
        
        """
        ...

class AveragedKeplerianWithMeanAngle(AveragedOrbitalElements):
    """
    public class AveragedKeplerianWithMeanAngle extends :class:`~org.orekit.propagation.conversion.averaging.elements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    
        Immutable class containing values of averaged Keplerian elements from any applicable theory (with MEAN as
        :class:`~org.orekit.orbits.PositionAngleType`).
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, double5: float, double6: float): ...
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
    def toArray(self) -> typing.List[float]:
        """
            Write values from instance into an array of doubles.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements.toArray` in
                interface :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
        
            Returns:
                array with values
        
        
        """
        ...

class PythonAveragedOrbitalElements(AveragedOrbitalElements):
    """
    public class PythonAveragedOrbitalElements extends :class:`~org.orekit.propagation.conversion.averaging.elements.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
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
    def toArray(self) -> typing.List[float]:
        """
            Write values from instance into an array of doubles.
        
            Specified by:
                :meth:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements.toArray` in
                interface :class:`~org.orekit.propagation.conversion.averaging.elements.AveragedOrbitalElements`
        
            Returns:
                array with values
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.averaging.elements")``.

    AveragedCircularWithMeanAngle: typing.Type[AveragedCircularWithMeanAngle]
    AveragedEquinoctialWithMeanAngle: typing.Type[AveragedEquinoctialWithMeanAngle]
    AveragedKeplerianWithMeanAngle: typing.Type[AveragedKeplerianWithMeanAngle]
    AveragedOrbitalElements: typing.Type[AveragedOrbitalElements]
    PythonAveragedOrbitalElements: typing.Type[PythonAveragedOrbitalElements]
    class-use: org.orekit.propagation.conversion.averaging.elements.class-use.__module_protocol__
