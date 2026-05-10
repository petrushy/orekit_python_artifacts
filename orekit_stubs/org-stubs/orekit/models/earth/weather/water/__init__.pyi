
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import typing



class WaterVaporPressureProvider:
    """
    Interface for converting between relative humidity and water vapor pressure.
    
    Since:
        12.1
    """
    _relativeHumidity_1__T = typing.TypeVar('_relativeHumidity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def relativeHumidity(self, p: float, t: float, e: float) -> float:
        """
        Compute relative humidity.
        
        Parameters:
            p (double): pressure (Pa)
            t (double): temperature (Kelvin)
            e (double): water vapor pressure (Pa)
        
        Returns:
            relative humidity, as a ratio (50% → 0.5)
        
        """
        ...
    @typing.overload
    def relativeHumidity(self, p: _relativeHumidity_1__T, t: _relativeHumidity_1__T, e: _relativeHumidity_1__T) -> _relativeHumidity_1__T:
        """
        Compute relative humidity.
        
        Parameters:
            p (T): pressure (Pa)
            t (T): temperature (Kelvin)
            e (T): water vapor pressure (Pa)
        
        Returns:
            relative humidity, as a ratio (50% → 0.5)
        
        
        """
        ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, p: float, t: float, rh: float) -> float:
        """
        Compute water vapor pressure.
        
        Parameters:
            p (double): pressure (Pa)
            t (double): temperature (Kelvin)
            rh (double): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, p: _waterVaporPressure_1__T, t: _waterVaporPressure_1__T, rh: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
        Compute water vapor pressure.
        
        Parameters:
            p (T): pressure (Pa)
            t (T): temperature (Kelvin)
            rh (T): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        
        """
        ...

class CIPM2007(WaterVaporPressureProvider):
    """
    Official model CIPM-2007 (identical to CIPM-1981/91) from Comité International des Poids et Mesures.
    
    This water vapor model is the one from Giacomo and Davis as indicated in IERS TN 32, chap. 9.
    
    Since:
        12.1
    
    Also see:
        CIPM
    """
    def __init__(self): ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, p: float, t: float, rh: float) -> float:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (double): pressure (Pa)
            t (double): temperature (Kelvin)
            rh (double): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, p: _waterVaporPressure_1__T, t: _waterVaporPressure_1__T, rh: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (T): pressure (Pa)
            t (T): temperature (Kelvin)
            rh (T): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        
        """
        ...

class NbsNrcSteamTable(WaterVaporPressureProvider):
    """
    Steam table from US National Bureau of Standards (NBS) and National Research Council (NRC) of Canada.
    
    The table is an extract from table 1 in content, using only the pressure column and truncated to 99°C (the original table goes up to 373.976°C). According to access, this data is available for free.
    
    Since:
        12.1
    
    Also see:
        steam_tables
    """
    def __init__(self): ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, p: float, t: float, rh: float) -> float:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (double): pressure (Pa)
            t (double): temperature (Kelvin)
            rh (double): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, p: _waterVaporPressure_1__T, t: _waterVaporPressure_1__T, rh: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (T): pressure (Pa)
            t (T): temperature (Kelvin)
            rh (T): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        
        """
        ...

class PythonWaterVaporPressureProvider(WaterVaporPressureProvider):
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, p: float, t: float, rh: float) -> float:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (double): pressure (Pa)
            t (double): temperature (Kelvin)
            rh (double): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, p: _waterVaporPressure_1__T, t: _waterVaporPressure_1__T, rh: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (T): pressure (Pa)
            t (T): temperature (Kelvin)
            rh (T): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        
        """
        ...

class Wang1988(WaterVaporPressureProvider):
    """
    Conversion polynomial from "The Principle of the GPS Precise Positioning System", Wang et al, 1988.
    
    This corresponds to equation 5.96 in Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007.
    
    Since:
        12.1
    """
    def __init__(self): ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, p: float, t: float, rh: float) -> float:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (double): pressure (Pa)
            t (double): temperature (Kelvin)
            rh (double): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, p: _waterVaporPressure_1__T, t: _waterVaporPressure_1__T, rh: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
        Compute water vapor pressure.
        
        Specified by: waterVaporPressure in interface WaterVaporPressureProvider
        
        Parameters:
            p (T): pressure (Pa)
            t (T): temperature (Kelvin)
            rh (T): relative humidity, as a ratio (50% → 0.5)
        
        Returns:
            water vapor pressure (Pa)
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.weather.water")``.

    CIPM2007: typing.Type[CIPM2007]
    NbsNrcSteamTable: typing.Type[NbsNrcSteamTable]
    PythonWaterVaporPressureProvider: typing.Type[PythonWaterVaporPressureProvider]
    Wang1988: typing.Type[Wang1988]
    WaterVaporPressureProvider: typing.Type[WaterVaporPressureProvider]
