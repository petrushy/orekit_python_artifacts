
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.hipparchus
import org.hipparchus.util
import org.orekit.bodies
import org.orekit.frames
import org.orekit.models.earth.ionosphere
import org.orekit.propagation
import org.orekit.time
import org.orekit.utils
import typing



_FieldFourierTimeSeries__T = typing.TypeVar('_FieldFourierTimeSeries__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldFourierTimeSeries(typing.Generic[_FieldFourierTimeSeries__T]):
    """
    public class FieldFourierTimeSeries<T extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Fourier time series for the NeQuick model.
    
        Since:
            13.0.1
    
        Also see:
            :meth:`~org.orekit.models.earth.ionosphere.nequick.NeQuickModel.computeFourierTimeSeries`
    """
    def getAz(self) -> _FieldFourierTimeSeries__T:
        """
            Get effective ionisation level.
        
            Returns:
                effective ionisation level
        
        
        """
        ...
    def getAzr(self) -> _FieldFourierTimeSeries__T:
        """
            Get effective sunspot number.
        
            Returns:
                effective sunspot number
        
        
        """
        ...
    def getDateTime(self) -> org.orekit.time.DateTimeComponents:
        """
            Get date time components.
        
            Returns:
                date time components
        
        
        """
        ...

class FourierTimeSeries:
    """
    public class FourierTimeSeries extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Fourier time series for the NeQuick model.
    
        Since:
            13.0.1
    
        Also see:
            :meth:`~org.orekit.models.earth.ionosphere.nequick.NeQuickModel.computeFourierTimeSeries`
    """
    def getAz(self) -> float:
        """
            Get effective ionisation level.
        
            Returns:
                effective ionisation level
        
        
        """
        ...
    def getAzr(self) -> float:
        """
            Get effective sunspot number.
        
            Returns:
                effective sunspot number
        
        
        """
        ...
    def getDateTime(self) -> org.orekit.time.DateTimeComponents:
        """
            Get date time components.
        
            Returns:
                date time components
        
        
        """
        ...

class NeQuickModel(org.orekit.models.earth.ionosphere.IonosphericModel):
    """
    public abstract class NeQuickModel extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
    
        NeQuick ionospheric delay model.
    
        Since:
            10.1
    
        Also see:
            "European Union (2016). European GNSS (Galileo) Open Service-Ionospheric Correction Algorithm for Galileo Single
            Frequency Users. 1.2.", :class:`~org.orekit.models.earth.ionosphere.nequick.https:.www.itu.int.rec.R`
    """
    RE: typing.ClassVar[float] = ...
    """
    public static final double RE
    
        Mean Earth radius in m (Ref Table 2.5.2).
    
        Also see:
            :meth:`~constant`
    
    
    """
    _computeFourierTimeSeries_0__T = typing.TypeVar('_computeFourierTimeSeries_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeFourierTimeSeries(self, dateTimeComponents: org.orekit.time.DateTimeComponents, t: _computeFourierTimeSeries_0__T) -> FieldFourierTimeSeries[_computeFourierTimeSeries_0__T]:
        """
            Compute Fourier time series.
        
            Parameters:
                dateTime (:class:`~org.orekit.time.DateTimeComponents`): current date time components
                az (T): effective ionisation level
        
            Returns:
                Fourier time series
        
            Since:
                13.0.1
        
        
        """
        ...
    @typing.overload
    def computeFourierTimeSeries(self, dateTimeComponents: org.orekit.time.DateTimeComponents, double: float) -> FourierTimeSeries:
        """
            Compute Fourier time series.
        
            Parameters:
                dateTime (:class:`~org.orekit.time.DateTimeComponents`): current date time components
                az (double): effective ionisation level
        
            Returns:
                Fourier time series
        
            Since:
                13.0.1
        
        """
        ...
    _electronDensity_2__T = typing.TypeVar('_electronDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _electronDensity_3__T = typing.TypeVar('_electronDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def electronDensity(self, fourierTimeSeries: FourierTimeSeries, double: float, double2: float, double3: float) -> float:
        """
            Computes the electron density at a given height.
        
            Parameters:
                dateTime (:class:`~org.orekit.time.DateTimeComponents`): date
                az (double): effective ionization level
                latitude (double): latitude along the integration path
                longitude (double): longitude along the integration path
                h (double): height along the integration path in m
        
            Returns:
                electron density [m⁻³]
        
            Since:
                13.0
        
            Computes the electron density at a given height.
        
            Parameters:
                fourierTimeSeries (:class:`~org.orekit.models.earth.ionosphere.nequick.FourierTimeSeries`): Fourier time series for foF2 and M(3000)F2 layer (flatten array)
                latitude (double): latitude along the integration path
                longitude (double): longitude along the integration path
                h (double): height along the integration path in m
        
            Returns:
                electron density [m⁻³]
        
            Since:
                13.0.1
        
        """
        ...
    @typing.overload
    def electronDensity(self, dateTimeComponents: org.orekit.time.DateTimeComponents, double: float, double2: float, double3: float, double4: float) -> float: ...
    @typing.overload
    def electronDensity(self, fieldFourierTimeSeries: FieldFourierTimeSeries[_electronDensity_2__T], t: _electronDensity_2__T, t2: _electronDensity_2__T, t3: _electronDensity_2__T) -> _electronDensity_2__T:
        """
            Computes the electron density at a given height.
        
            Parameters:
                dateTime (:class:`~org.orekit.time.DateTimeComponents`): date
                az (T): effective ionization level
                latitude (T): latitude along the integration path
                longitude (T): longitude along the integration path
                h (T): height along the integration path in m
        
            Returns:
                electron density [m⁻³]
        
            Since:
                13.0 CalculusFieldElement, CalculusFieldElement, CalculusFieldElement)}
        
            Computes the electron density at a given height.
        
            Parameters:
                fourierTimeSeries (:class:`~org.orekit.models.earth.ionosphere.nequick.FieldFourierTimeSeries`<T> fourierTimeSeries): Fourier time series for foF2 and M(3000)F2 layer (flatten array)
                latitude (T): latitude along the integration path
                longitude (T): longitude along the integration path
                h (T): height along the integration path in m
        
            Returns:
                electron density [m⁻³]
        
            Since:
                13.0.1
        
        
        """
        ...
    @typing.overload
    def electronDensity(self, dateTimeComponents: org.orekit.time.DateTimeComponents, t: _electronDensity_3__T, t2: _electronDensity_3__T, t3: _electronDensity_3__T, t4: _electronDensity_3__T) -> _electronDensity_3__T: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]: ...
    def getUtc(self) -> org.orekit.time.TimeScale:
        """
            Get UTC time scale.
        
            Returns:
                UTC time scale
        
            Since:
                13.0
        
        
        """
        ...
    _pathDelay_1__T = typing.TypeVar('_pathDelay_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, spacecraftState: org.orekit.propagation.SpacecraftState, topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.SpacecraftState`): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (double[]): ionospheric model parameters at state date
        
            Returns:
                the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, fieldSpacecraftState: org.orekit.propagation.FieldSpacecraftState[_pathDelay_1__T], topocentricFrame: org.orekit.frames.TopocentricFrame, double: float, tArray: typing.Union[typing.List[_pathDelay_1__T], jpype.JArray]) -> _pathDelay_1__T:
        """
            Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
            This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0° the
            path delay will be equal to zero.
        
            For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be
            implemented to compute the path delay for any elevation angle.
        
            Specified by:
                :meth:`~org.orekit.models.earth.ionosphere.IonosphericModel.pathDelay` in
                interface :class:`~org.orekit.models.earth.ionosphere.IonosphericModel`
        
            Parameters:
                state (:class:`~org.orekit.propagation.FieldSpacecraftState`<T> state): spacecraft state
                baseFrame (:class:`~org.orekit.frames.TopocentricFrame`): base frame associated with the station
                frequency (double): frequency of the signal in Hz
                parameters (T[]): ionospheric model parameters at state date
        
            Returns:
                the path delay due to the ionosphere in m
        
        
        """
        ...
    _stec_1__T = typing.TypeVar('_stec_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def stec(self, absoluteDate: org.orekit.time.AbsoluteDate, geodeticPoint: org.orekit.bodies.GeodeticPoint, geodeticPoint2: org.orekit.bodies.GeodeticPoint) -> float:
        """
            This method allows the computation of the Slant Total Electron Content (STEC).
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): current date
                recP (:class:`~org.orekit.bodies.GeodeticPoint`): receiver position
                satP (:class:`~org.orekit.bodies.GeodeticPoint`): satellite position
        
            Returns:
                the STEC in TECUnits
        
        """
        ...
    @typing.overload
    def stec(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_stec_1__T], fieldGeodeticPoint: org.orekit.bodies.FieldGeodeticPoint[_stec_1__T], fieldGeodeticPoint2: org.orekit.bodies.FieldGeodeticPoint[_stec_1__T]) -> _stec_1__T:
        """
            This method allows the computation of the Slant Total Electron Content (STEC).
        
            Parameters:
                date (:class:`~org.orekit.time.FieldAbsoluteDate`<T> date): current date
                recP (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> recP): receiver position
                satP (:class:`~org.orekit.bodies.FieldGeodeticPoint`<T> satP): satellite position
        
            Returns:
                the STEC in TECUnits
        
        
        """
        ...

class NeQuickParameters:
    """
    public class NeQuickParameters extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class performs the computation of the parameters used by the NeQuick model.
    
        Since:
            10.1
    
        Also see:
            "European Union (2016). European GNSS (Galileo) Open Service-Ionospheric Correction Algorithm for Galileo Single
            Frequency Users. 1.2.", :class:`~org.orekit.models.earth.ionosphere.nequick.https:.www.itu.int.rec.R`
    """
    @typing.overload
    def __init__(self, fourierTimeSeries: FourierTimeSeries, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, dateTimeComponents: org.orekit.time.DateTimeComponents, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float, double4: float, double5: float, double6: float): ...
    def getAzr(self) -> float:
        """
            Get effective sunspot number.
        
            Returns:
                effective sunspot number
        
            Since:
                13.0
        
        
        """
        ...
    def getB2Bot(self) -> float:
        """
            Get the F2 layer thickness parameter (bottom).
        
            Returns:
                B2Bot in km
        
        
        """
        ...
    def getBE(self, double: float) -> float:
        """
            Get the E layer thickness parameter.
        
            Parameters:
                h (double): current height (km)
        
            Returns:
                Be in km
        
            Since:
                13.0
        
        
        """
        ...
    def getBF1(self, double: float) -> float:
        """
            Get the F1 layer thickness parameter.
        
            Parameters:
                h (double): current height (km)
        
            Returns:
                B1 in km
        
            Since:
                13.0
        
        
        """
        ...
    def getDateTime(self) -> org.orekit.time.DateTimeComponents:
        """
            Get current date time components.
        
            Returns:
                current date time components
        
            Since:
                13.0
        
        
        """
        ...
    def getFoF2(self) -> float:
        """
            Get F2 layer critical frequency.
        
            Returns:
                F2 layer critical frequency
        
            Since:
                13.0
        
        
        """
        ...
    def getHmE(self) -> float:
        """
            Get the E layer maximum density height.
        
            Returns:
                hmE in km
        
        
        """
        ...
    def getHmF1(self) -> float:
        """
            Get the F1 layer maximum density height.
        
            Returns:
                hmF1 in km
        
        
        """
        ...
    def getHmF2(self) -> float:
        """
            Get the F2 layer maximum density height.
        
            Returns:
                hmF2 in km
        
        
        """
        ...
    def getLayerAmplitudes(self) -> typing.MutableSequence[float]:
        """
            Get the F2, F1 and E layer amplitudes.
        
            The resulting element is an array having the following form:
        
              - double[0] = A1 → F2 layer amplitude
              - double[1] = A2 → F1 layer amplitude
              - double[2] = A3 → E layer amplitude
        
        
            Returns:
                layer amplitudes
        
        
        """
        ...
    def getNmF2(self) -> float:
        """
            Get the F2 layer maximum density.
        
            Returns:
                nmF2
        
        
        """
        ...

class Ray:
    """
    public class Ray extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container for ray-perigee parameters.
    
        By convention, point 1 is at lower height.
    
        Since:
            13.0
    """
    def __init__(self, geodeticPoint: org.orekit.bodies.GeodeticPoint, geodeticPoint2: org.orekit.bodies.GeodeticPoint): ...
    def getCosineAz(self) -> float:
        """
            Get the cosine of azimuth of satellite as seen from ray-perigee.
        
            Returns:
                the cosine of azimuth
        
        
        """
        ...
    def getLatitude(self) -> float:
        """
            Get the ray-perigee latitude.
        
            Returns:
                the ray-perigee latitude in radians
        
        
        """
        ...
    def getLongitude(self) -> float:
        """
            Get the ray-perigee longitude.
        
            Returns:
                the ray-perigee longitude in radians
        
        
        """
        ...
    def getRadius(self) -> float:
        """
            Get the ray-perigee radius.
        
            Returns:
                the ray-perigee radius in meters
        
        
        """
        ...
    def getRecH(self) -> float:
        """
            Get receiver altitude.
        
            Returns:
                receiver altitude
        
            Since:
                13.0
        
        
        """
        ...
    def getS1(self) -> float:
        """
            Get the distance of the first point from the ray perigee.
        
            Returns:
                s1 in meters
        
        
        """
        ...
    def getS2(self) -> float:
        """
            Get the distance of the second point from the ray perigee.
        
            Returns:
                s2 in meters
        
        
        """
        ...
    def getSatH(self) -> float:
        """
            Get satellite altitude.
        
            Returns:
                satellite altitude
        
            Since:
                13.0
        
        
        """
        ...
    def getScLat(self) -> org.hipparchus.util.SinCos:
        """
            Get the ray-perigee latitude sin/cos.
        
            Returns:
                the ray-perigee latitude sin/cos
        
            Since:
                13.0
        
        
        """
        ...
    def getSineAz(self) -> float:
        """
            Get the sine of azimuth of satellite as seen from ray-perigee.
        
            Returns:
                the sine of azimuth
        
        
        """
        ...

class Segment:
    """
    public class Segment extends :class:`~org.orekit.models.earth.ionosphere.nequick.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Performs the computation of the coordinates along the integration path.
    
        Since:
            13.0
    """
    def __init__(self, int: int, ray: Ray, double: float, double2: float): ...
    def getInterval(self) -> float:
        """
            Get the integration step.
        
            Returns:
                the integration step in meters
        
        
        """
        ...
    def getNbPoints(self) -> int:
        """
            Get number of points.
        
            Note there are 2 points per interval, so :code:`index` must be between 0 (included) and 2n (excluded) for a segment
            built with :code:`n` intervals
        
            Returns:
                number of points
        
        
        """
        ...
    def getPoint(self, int: int) -> org.orekit.bodies.GeodeticPoint:
        """
            Get point along the ray.
        
            Parameters:
                index (int): point index (between O included and :meth:`~org.orekit.models.earth.ionosphere.nequick.Segment.getNbPoints` excluded)
        
            Returns:
                point on ray
        
            Since:
                13.0
        
        
        """
        ...

class NeQuickGalileo(NeQuickModel):
    """
    public class NeQuickGalileo extends :class:`~org.orekit.models.earth.ionosphere.nequick.NeQuickModel`
    
        Galileo-specific version of NeQuick engine.
    
        Since:
            13.0
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], timeScale: org.orekit.time.TimeScale): ...
    def getAlpha(self) -> typing.MutableSequence[float]:
        """
            Get effective ionisation level coefficients.
        
            Returns:
                effective ionisation level coefficients
        
        
        """
        ...

class NeQuickItu(NeQuickModel):
    """
    public class NeQuickItu extends :class:`~org.orekit.models.earth.ionosphere.nequick.NeQuickModel`
    
        Original model from Aeronomy and Radiopropagation Laboratory of the Abdus Salam International Centre for Theoretical
        Physics Trieste, Italy.
    
        None of the code from Abdus Salam International Centre for Theoretical Physics Trieste has been used, the models have
        been reimplemented from scratch by the Orekit team.
    
        Since:
            13.0
    """
    def __init__(self, double: float, timeScale: org.orekit.time.TimeScale): ...
    def getF107(self) -> float:
        """
            Get solar flux.
        
            Returns:
                solar flux
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.ionosphere.nequick")``.

    FieldFourierTimeSeries: typing.Type[FieldFourierTimeSeries]
    FourierTimeSeries: typing.Type[FourierTimeSeries]
    NeQuickGalileo: typing.Type[NeQuickGalileo]
    NeQuickItu: typing.Type[NeQuickItu]
    NeQuickModel: typing.Type[NeQuickModel]
    NeQuickParameters: typing.Type[NeQuickParameters]
    Ray: typing.Type[Ray]
    Segment: typing.Type[Segment]
