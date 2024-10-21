import org.hipparchus
import org.orekit.models.earth.weather.water.class-use
import typing



class WaterVaporPressureProvider:
    """
    public interface WaterVaporPressureProvider
    
        Interface for converting between relative humidity and water vapor pressure.
    
        Since:
            12.1
    """
    _relativeHumidity_1__T = typing.TypeVar('_relativeHumidity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def relativeHumidity(self, double: float, double2: float, double3: float) -> float:
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
    def relativeHumidity(self, t: _relativeHumidity_1__T, t2: _relativeHumidity_1__T, t3: _relativeHumidity_1__T) -> _relativeHumidity_1__T:
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
    def waterVaporPressure(self, double: float, double2: float, double3: float) -> float:
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
    def waterVaporPressure(self, t: _waterVaporPressure_1__T, t2: _waterVaporPressure_1__T, t3: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
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
    public class CIPM2007 extends :class:`~org.orekit.models.earth.weather.water.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
    
        Official model CIPM-2007 (identical to CIPM-1981/91) from Comité International des Poids et Mesures.
    
        This water vapor model is the one from Giacomo and Davis as indicated in IERS TN 32, chap. 9.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.models.earth.weather.water.https:.www.nist.gov.system.files.documents.calibrations.CIPM`
    """
    def __init__(self): ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, double: float, double2: float, double3: float) -> float:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
            Parameters:
                p (double): pressure (Pa)
                t (double): temperature (Kelvin)
                rh (double): relative humidity, as a ratio (50% → 0.5)
        
            Returns:
                water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, t: _waterVaporPressure_1__T, t2: _waterVaporPressure_1__T, t3: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
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
    public class NbsNrcSteamTable extends :class:`~org.orekit.models.earth.weather.water.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
    
        Steam table from US National Bureau of Standards (NBS) and National Research Council (NRC) of Canada.
    
        The table is an extract from table 1 in
        :class:`~org.orekit.models.earth.weather.water.https:.www.thermopedia.com.content.1150`, using only the pressure column
        and truncated to 99°C (the original table goes up to 373.976°C). According to
        :class:`~org.orekit.models.earth.weather.water.https:.www.thermopedia.com.access`, this data is available for free.
    
        Since:
            12.1
    
        Also see:
            :class:`~org.orekit.models.earth.weather.water.https:.dx.doi.org.10.1615.AtoZ.s.steam_tables`
    """
    def __init__(self): ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, double: float, double2: float, double3: float) -> float:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
            Parameters:
                p (double): pressure (Pa)
                t (double): temperature (Kelvin)
                rh (double): relative humidity, as a ratio (50% → 0.5)
        
            Returns:
                water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, t: _waterVaporPressure_1__T, t2: _waterVaporPressure_1__T, t3: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
            Parameters:
                p (T): pressure (Pa)
                t (T): temperature (Kelvin)
                rh (T): relative humidity, as a ratio (50% → 0.5)
        
            Returns:
                water vapor pressure (Pa)
        
        
        """
        ...

class PythonWaterVaporPressureProvider(WaterVaporPressureProvider):
    """
    public class PythonWaterVaporPressureProvider extends :class:`~org.orekit.models.earth.weather.water.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
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
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, double: float, double2: float, double3: float) -> float:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
            Parameters:
                p (double): pressure (Pa)
                t (double): temperature (Kelvin)
                rh (double): relative humidity, as a ratio (50% → 0.5)
        
            Returns:
                water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, t: _waterVaporPressure_1__T, t2: _waterVaporPressure_1__T, t3: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
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
    public class Wang1988 extends :class:`~org.orekit.models.earth.weather.water.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
    
        Conversion polynomial from "The Principle of the GPS Precise Positioning System", Wang et al, 1988.
    
        This corresponds to equation 5.96 in Guochang Xu, GPS - Theory, Algorithms and Applications, Springer, 2007.
    
        Since:
            12.1
    """
    def __init__(self): ...
    _waterVaporPressure_1__T = typing.TypeVar('_waterVaporPressure_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def waterVaporPressure(self, double: float, double2: float, double3: float) -> float:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
            Parameters:
                p (double): pressure (Pa)
                t (double): temperature (Kelvin)
                rh (double): relative humidity, as a ratio (50% → 0.5)
        
            Returns:
                water vapor pressure (Pa)
        
        """
        ...
    @typing.overload
    def waterVaporPressure(self, t: _waterVaporPressure_1__T, t2: _waterVaporPressure_1__T, t3: _waterVaporPressure_1__T) -> _waterVaporPressure_1__T:
        """
            Compute water vapor pressure.
        
            Specified by:
                :meth:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider.waterVaporPressure` in
                interface :class:`~org.orekit.models.earth.weather.water.WaterVaporPressureProvider`
        
            Parameters:
                p (T): pressure (Pa)
                t (T): temperature (Kelvin)
                rh (T): relative humidity, as a ratio (50% → 0.5)
        
            Returns:
                water vapor pressure (Pa)
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.weather.water")``.

    CIPM2007: typing.Type[CIPM2007]
    NbsNrcSteamTable: typing.Type[NbsNrcSteamTable]
    PythonWaterVaporPressureProvider: typing.Type[PythonWaterVaporPressureProvider]
    Wang1988: typing.Type[Wang1988]
    WaterVaporPressureProvider: typing.Type[WaterVaporPressureProvider]
    class-use: org.orekit.models.earth.weather.water.class-use.__module_protocol__
