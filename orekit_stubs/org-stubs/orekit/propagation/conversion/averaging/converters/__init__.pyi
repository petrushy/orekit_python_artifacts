
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.data
import org.orekit.forces.gravity.potential
import org.orekit.orbits
import org.orekit.propagation.conversion.averaging
import typing



_OsculatingToAveragedConverter__T = typing.TypeVar('_OsculatingToAveragedConverter__T', bound=org.orekit.propagation.conversion.averaging.AveragedOrbitalState)  # <T>
class OsculatingToAveragedConverter(typing.Generic[_OsculatingToAveragedConverter__T]):
    """
    Interface for osculating-to-averaged converters.
    
    Since:
        12.1
    
    Also see:
        AveragedOrbitalState
    """
    def convertToAveraged(self, osculatingOrbit: org.orekit.orbits.Orbit) -> _OsculatingToAveragedConverter__T:
        """
        Convert osculating orbit to averaged orbital state according to underlying theory.
        
        Parameters:
            osculatingOrbit (Orbit): osculating orbit
        
        Returns:
            averaged orbital state
        
        
        """
        ...

_FixedPointOsculatingToAveragedConverter__T = typing.TypeVar('_FixedPointOsculatingToAveragedConverter__T', bound=org.orekit.propagation.conversion.averaging.AveragedOrbitalState)  # <T>
class FixedPointOsculatingToAveragedConverter(OsculatingToAveragedConverter[_FixedPointOsculatingToAveragedConverter__T], typing.Generic[_FixedPointOsculatingToAveragedConverter__T]):
    """
    Abstract class for osculating-to-averaged converters based on a fixed-point algorithm.
    
    Since:
        12.1
    
    Also see:
        OsculatingToAveragedConverter
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default convergence threshold.
    
    Also see:
        constant
    
    
    """
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    """
    Default maximum number of iterations.
    
    Also see:
        constant
    
    
    """
    def getEpsilon(self) -> float:
        """
        Getter for the convergence threshold.
        
        Returns:
            convergence threshold
        
        
        """
        ...
    def getMaxIterations(self) -> int:
        """
        Getter for the maximum number of iterations.
        
        Returns:
            maximum number of iterations
        
        
        """
        ...
    def setEpsilon(self, epsilon: float) -> None:
        """
        Setter for epsilon.
        
        Parameters:
            epsilon (double): convergence threshold.
        
        
        """
        ...
    def setMaxIterations(self, maxIterations: int) -> None:
        """
        Setter for maximum number of iterations.
        
        Parameters:
            maxIterations (int): maximum iterations
        
        
        """
        ...

class OsculatingToBrouwerLyddaneConverter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.BrouwerLyddaneOrbitalState]):
    """
    Class for osculating-to-averaged conversion according to Brouwer-Lyddane theory. Value of M2 parameter is set to zero.
    
    Since:
        12.1
    
    Also see:
        BrouwerLyddanePropagator,
        BrouwerLyddaneOrbitalState
    """
    @typing.overload
    def __init__(self, double: float, int: int, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def convertToAveraged(self, osculatingOrbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.BrouwerLyddaneOrbitalState:
        """
        Convert osculating orbit to averaged orbital state according to underlying theory.
        
        Parameters:
            osculatingOrbit (Orbit): osculating orbit
        
        Returns:
            averaged orbital state
        
        
        """
        ...

class OsculatingToDSST6X0Converter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.DSST6X0OrbitalState]):
    """
    Class for osculating-to-averaged conversion according to DSST theory, using 6 zonal harmonics as the only perturbations.
    
    Since:
        12.1
    
    Also see:
        DSSTPropagator,
        DSST6X0OrbitalState
    """
    @typing.overload
    def __init__(self, double: float, int: int, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def convertToAveraged(self, osculatingOrbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.DSST6X0OrbitalState:
        """
        Convert osculating orbit to averaged orbital state according to underlying theory.
        
        Parameters:
            osculatingOrbit (Orbit): osculating orbit
        
        Returns:
            averaged orbital state
        
        
        """
        ...

class OsculatingToEcksteinHechlerConverter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.EcksteinHechlerOrbitalState]):
    """
    Class for osculating-to-averaged conversion according to Eckstein-Hechler theory.
    
    Since:
        12.1
    
    Also see:
        EcksteinHechlerPropagator,
        EcksteinHechlerOrbitalState
    """
    @typing.overload
    def __init__(self, double: float, int: int, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    @typing.overload
    def __init__(self, unnormalizedSphericalHarmonicsProvider: org.orekit.forces.gravity.potential.UnnormalizedSphericalHarmonicsProvider): ...
    def convertToAveraged(self, osculatingOrbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.EcksteinHechlerOrbitalState:
        """
        Convert osculating orbit to averaged orbital state according to underlying theory.
        
        Parameters:
            osculatingOrbit (Orbit): osculating orbit
        
        Returns:
            averaged orbital state
        
        
        """
        ...

class OsculatingToSGP4Converter(FixedPointOsculatingToAveragedConverter[org.orekit.propagation.conversion.averaging.SGP4OrbitalState]):
    """
    Class for osculating-to-averaged conversion according to "SGP4" theory, meant as the set of models associated to Two-Line Elements.
    
    Since:
        12.1
    
    Also see:
        TLEPropagator,
        SGP4OrbitalState
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float, dataContext: org.orekit.data.DataContext): ...
    @typing.overload
    def __init__(self, dataContext: org.orekit.data.DataContext): ...
    def convertToAveraged(self, osculatingOrbit: org.orekit.orbits.Orbit) -> org.orekit.propagation.conversion.averaging.SGP4OrbitalState:
        """
        Convert osculating orbit to averaged orbital state according to underlying theory.
        
        Parameters:
            osculatingOrbit (Orbit): osculating orbit
        
        Returns:
            averaged orbital state
        
        
        """
        ...

_PythonFixedPointOsculatingToAveragedConverter__T = typing.TypeVar('_PythonFixedPointOsculatingToAveragedConverter__T', bound=org.orekit.propagation.conversion.averaging.AveragedOrbitalState)  # <T>
class PythonFixedPointOsculatingToAveragedConverter(FixedPointOsculatingToAveragedConverter[_PythonFixedPointOsculatingToAveragedConverter__T], typing.Generic[_PythonFixedPointOsculatingToAveragedConverter__T]):
    def __init__(self, epsilon: float, maxIterations: int):
        """
        Protected constructor.
        
        Parameters:
            epsilon (double): tolerance for convergence
            maxIterations (int): maximum number of iterations
        
        
        """
        ...
    def convertToAveraged(self, osculatingOrbit: org.orekit.orbits.Orbit) -> _PythonFixedPointOsculatingToAveragedConverter__T:
        """
        Convert osculating orbit to averaged orbital state according to underlying theory.
        
        Parameters:
            osculatingOrbit (Orbit): osculating orbit
        
        Returns:
            averaged orbital state
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.propagation.conversion.averaging.converters.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
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


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.conversion.averaging.converters")``.

    FixedPointOsculatingToAveragedConverter: typing.Type[FixedPointOsculatingToAveragedConverter]
    OsculatingToAveragedConverter: typing.Type[OsculatingToAveragedConverter]
    OsculatingToBrouwerLyddaneConverter: typing.Type[OsculatingToBrouwerLyddaneConverter]
    OsculatingToDSST6X0Converter: typing.Type[OsculatingToDSST6X0Converter]
    OsculatingToEcksteinHechlerConverter: typing.Type[OsculatingToEcksteinHechlerConverter]
    OsculatingToSGP4Converter: typing.Type[OsculatingToSGP4Converter]
    PythonFixedPointOsculatingToAveragedConverter: typing.Type[PythonFixedPointOsculatingToAveragedConverter]
