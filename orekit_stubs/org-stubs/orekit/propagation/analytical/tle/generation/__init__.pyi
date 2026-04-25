
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation
import org.orekit.propagation.analytical.tle
import org.orekit.propagation.conversion.osc2mean
import org.orekit.time
import typing



class TleGenerationAlgorithm:
    """
    This interface provides a way to generate a TLE from a spacecraft state.
    
    Since:
        12.0
    """
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, state: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], templateTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            templateTLE (FieldTLE<T> templateTLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, state: org.orekit.propagation.SpacecraftState, templateTLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Parameters:
            state (SpacecraftState): spacecraft state
            templateTLE (TLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        """
        ...

class TleGenerationUtil:
    """
    Utility class for TLE generation algorithm.
    """
    _newTLE_0__T = typing.TypeVar('_newTLE_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def newTLE(keplerianOrbit: org.orekit.orbits.FieldKeplerianOrbit[_newTLE_0__T], templateTLE: org.orekit.propagation.analytical.tle.FieldTLE[_newTLE_0__T], bStar: _newTLE_0__T, utc: org.orekit.time.TimeScale) -> org.orekit.propagation.analytical.tle.FieldTLE[_newTLE_0__T]:
        """
        Builds a new TLE from Keplerian parameters and a template for TLE data.
        
        Parameters:
            keplerianOrbit (FieldKeplerianOrbit<T> keplerianOrbit): the Keplerian parameters to build the TLE from
            templateTLE (FieldTLE<T> templateTLE): TLE used to get object identification
            bStar (T): TLE B* parameter
            utc (TimeScale): UTC scale
        
        Returns:
            TLE with template identification and new orbital parameters
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def newTLE(keplerianOrbit: org.orekit.orbits.KeplerianOrbit, templateTLE: org.orekit.propagation.analytical.tle.TLE, bStar: float, utc: org.orekit.time.TimeScale) -> org.orekit.propagation.analytical.tle.TLE:
        """
        Builds a new TLE from Keplerian parameters and a template for TLE data.
        
        Parameters:
            keplerianOrbit (KeplerianOrbit): the Keplerian parameters to build the TLE from
            templateTLE (TLE): TLE used to get object identification
            bStar (double): TLE B* parameter
            utc (TimeScale): UTC scale
        
        Returns:
            TLE with template identification and new orbital parameters
        
        """
        ...

class FixedPointTleGenerationAlgorithm(TleGenerationAlgorithm):
    """
    Fixed Point method to reverse SGP4 and SDP4 propagation algorithm and generate a usable TLE from a spacecraft state.
    
    Using this algorithm, the B* value is not computed. In other words, the B* value from the template TLE is set to the generated one.
    
    Since:
        12.0
    """
    EPSILON_DEFAULT: typing.ClassVar[float] = ...
    """
    Default value for epsilon.
    
    Also see:
        constant
    
    
    """
    MAX_ITERATIONS_DEFAULT: typing.ClassVar[int] = ...
    """
    Default value for maxIterations.
    
    Also see:
        constant
    
    
    """
    SCALE_DEFAULT: typing.ClassVar[float] = ...
    """
    Default value for scale.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float): ...
    @typing.overload
    def __init__(self, double: float, int: int, double2: float, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, state: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], templateTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Specified by: generate in interface TleGenerationAlgorithm
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            templateTLE (FieldTLE<T> templateTLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, state: org.orekit.propagation.SpacecraftState, templateTLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Specified by: generate in interface TleGenerationAlgorithm
        
        Parameters:
            state (SpacecraftState): spacecraft state
            templateTLE (TLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        """
        ...

class LeastSquaresTleGenerationAlgorithm(TleGenerationAlgorithm):
    """
    Least squares method to generate a usable TLE from a spacecraft state.
    
    Since:
        12.0
    """
    DEFAULT_MAX_ITERATIONS: typing.ClassVar[int] = ...
    """
    Default value for maximum number of iterations.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame): ...
    @typing.overload
    def __init__(self, timeScale: org.orekit.time.TimeScale, frame: org.orekit.frames.Frame, leastSquaresConverter: org.orekit.propagation.conversion.osc2mean.LeastSquaresConverter): ...
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, state: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], templateTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Specified by: generate in interface TleGenerationAlgorithm
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            templateTLE (FieldTLE<T> templateTLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, state: org.orekit.propagation.SpacecraftState, templateTLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Specified by: generate in interface TleGenerationAlgorithm
        
        Parameters:
            state (SpacecraftState): spacecraft state
            templateTLE (TLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        """
        ...
    def getRms(self) -> float:
        """
        Get the Root Mean Square of the TLE estimation.
        
        Be careful that the RMS is updated each time the generate method is called.
        
        Returns:
            the RMS
        
        
        """
        ...

class PythonTleGenerationAlgorithm(TleGenerationAlgorithm):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.propagation.analytical.tle.generation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _generate_0__T = typing.TypeVar('_generate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def generate(self, state: org.orekit.propagation.FieldSpacecraftState[_generate_0__T], templateTLE: org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]) -> org.orekit.propagation.analytical.tle.FieldTLE[_generate_0__T]:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Specified by: generate in interface TleGenerationAlgorithm
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            templateTLE (FieldTLE<T> templateTLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        
        """
        ...
    @typing.overload
    def generate(self, state: org.orekit.propagation.SpacecraftState, templateTLE: org.orekit.propagation.analytical.tle.TLE) -> org.orekit.propagation.analytical.tle.TLE:
        """
        Generate a TLE from a given spacecraft state and a template TLE.
        
        The template TLE is only used to get identifiers like satellite number, launch year, etc. In other words, the keplerian elements contained in the generated TLE are based on the provided state and not the template TLE.
        
        Specified by: generate in interface TleGenerationAlgorithm
        
        Parameters:
            state (SpacecraftState): spacecraft state
            templateTLE (TLE): template TLE
        
        Returns:
            a TLE corresponding to the given state
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.analytical.tle.generation")``.

    FixedPointTleGenerationAlgorithm: typing.Type[FixedPointTleGenerationAlgorithm]
    LeastSquaresTleGenerationAlgorithm: typing.Type[LeastSquaresTleGenerationAlgorithm]
    PythonTleGenerationAlgorithm: typing.Type[PythonTleGenerationAlgorithm]
    TleGenerationAlgorithm: typing.Type[TleGenerationAlgorithm]
    TleGenerationUtil: typing.Type[TleGenerationUtil]
