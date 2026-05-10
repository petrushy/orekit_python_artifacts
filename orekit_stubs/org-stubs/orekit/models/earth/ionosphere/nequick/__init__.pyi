
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
    Fourier time series for the NeQuick model.
    
    Since:
        13.0.1
    
    Also see:
        computeFourierTimeSeries
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
    Fourier time series for the NeQuick model.
    
    Since:
        13.0.1
    
    Also see:
        computeFourierTimeSeries
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

class NeQuickModel(org.orekit.models.earth.ionosphere.IonosphericModel, org.orekit.models.earth.ionosphere.IonosphericDelayModel):
    """
    NeQuick ionospheric delay model.
    
    Since:
        10.1
    
    Also see:
        "European Union (2016). European GNSS (Galileo) Open Service-Ionospheric Correction Algorithm for Galileo Single
        Frequency Users. 1.2.", R
    """
    RE: typing.ClassVar[float] = ...
    """
    Mean Earth radius in m (Ref Table 2.5.2).
    
    Also see:
        constant
    
    
    """
    _computeFourierTimeSeries_0__T = typing.TypeVar('_computeFourierTimeSeries_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def computeFourierTimeSeries(self, dateTime: org.orekit.time.DateTimeComponents, az: _computeFourierTimeSeries_0__T) -> FieldFourierTimeSeries[_computeFourierTimeSeries_0__T]:
        """
        Compute Fourier time series.
        
        Parameters:
            dateTime (DateTimeComponents): current date time components
            az (T): effective ionisation level
        
        Returns:
            Fourier time series
        
        Since:
            13.0.1
        
        
        """
        ...
    @typing.overload
    def computeFourierTimeSeries(self, dateTime: org.orekit.time.DateTimeComponents, az: float) -> FourierTimeSeries:
        """
        Compute Fourier time series.
        
        Parameters:
            dateTime (DateTimeComponents): current date time components
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
    def electronDensity(self, fourierTimeSeries: FourierTimeSeries, latitude: float, longitude: float, h: float) -> float:
        """
        Computes the electron density at a given height.
        
        Parameters:
            dateTime (DateTimeComponents): date
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
            fourierTimeSeries (FourierTimeSeries): Fourier time series for foF2 and M(3000)F2 layer (flatten array)
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
    def electronDensity(self, dateTime: org.orekit.time.DateTimeComponents, az: float, latitude: float, longitude: float, h: float) -> float: ...
    @typing.overload
    def electronDensity(self, fourierTimeSeries: FieldFourierTimeSeries[_electronDensity_2__T], latitude: _electronDensity_2__T, longitude: _electronDensity_2__T, h: _electronDensity_2__T) -> _electronDensity_2__T:
        """
        Computes the electron density at a given height.
        
        Parameters:
            dateTime (DateTimeComponents): date
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
            fourierTimeSeries (FieldFourierTimeSeries<T> fourierTimeSeries): Fourier time series for foF2 and M(3000)F2 layer (flatten array)
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
    def electronDensity(self, dateTime: org.orekit.time.DateTimeComponents, az: _electronDensity_3__T, latitude: _electronDensity_3__T, longitude: _electronDensity_3__T, h: _electronDensity_3__T) -> _electronDensity_3__T: ...
    def getParametersDrivers(self) -> java.util.List[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for parameters.
        
        Specified by: getParametersDrivers in interface ParameterDriversProvider
        
        Returns:
            drivers for parameters
        
        
        """
        ...
    def getUtc(self) -> org.orekit.time.TimeScale:
        """
        Get UTC time scale.
        
        Returns:
            UTC time scale
        
        Since:
            13.0
        
        
        """
        ...
    _pathDelay_2__T = typing.TypeVar('_pathDelay_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pathDelay_3__T = typing.TypeVar('_pathDelay_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pathDelay(self, state: org.orekit.propagation.SpacecraftState, baseFrame: org.orekit.frames.TopocentricFrame, frequency: float, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float:
        """
        Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
        This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0° the path delay will be equal to zero.
        
        For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be implemented to compute the path delay for any elevation angle.
        
        Specified by: pathDelay in interface IonosphericModel
        
        Parameters:
            state (SpacecraftState): spacecraft state
            baseFrame (TopocentricFrame): base frame associated with the station
            frequency (double): frequency of the signal in Hz
            parameters (double[]): ionospheric model parameters at state date
        
        Returns:
            the path delay due to the ionosphere in m
        
        Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
        This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0° the path delay will be equal to zero.
        
        For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be implemented to compute the path delay for any elevation angle.
        
        Specified by: pathDelay in interface IonosphericDelayModel
        
        Parameters:
            state (SpacecraftState): spacecraft state
            baseFrame (TopocentricFrame): base frame associated with the station
            receptionDate (AbsoluteDate): date at signal reception
            frequency (double): frequency of the signal in Hz
            parameters (double[]): ionospheric model parameters at state date
        
        Returns:
            the path delay due to the ionosphere in m
        
        """
        ...
    @typing.overload
    def pathDelay(self, state: org.orekit.propagation.SpacecraftState, baseFrame: org.orekit.frames.TopocentricFrame, receptionDate: org.orekit.time.AbsoluteDate, frequency: float, parameters: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def pathDelay(self, state: org.orekit.propagation.FieldSpacecraftState[_pathDelay_2__T], baseFrame: org.orekit.frames.TopocentricFrame, frequency: float, parameters: typing.Union[typing.List[_pathDelay_2__T], jpype.JArray]) -> _pathDelay_2__T:
        """
        Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
        This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0° the path delay will be equal to zero.
        
        For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be implemented to compute the path delay for any elevation angle.
        
        Specified by: pathDelay in interface IonosphericModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            baseFrame (TopocentricFrame): base frame associated with the station
            frequency (double): frequency of the signal in Hz
            parameters (T[]): ionospheric model parameters at state date
        
        Returns:
            the path delay due to the ionosphere in m
        
        Calculates the ionospheric path delay for the signal path from a ground station to a satellite.
        
        This method is intended to be used for orbit determination issues. In that respect, if the elevation is below 0° the path delay will be equal to zero.
        
        For individual use of the ionospheric model (i.e. not for orbit determination), another method signature can be implemented to compute the path delay for any elevation angle.
        
        Specified by: pathDelay in interface IonosphericDelayModel
        
        Parameters:
            state (FieldSpacecraftState<T> state): spacecraft state
            baseFrame (TopocentricFrame): base frame associated with the station
            receptionDate (FieldAbsoluteDate<T> receptionDate): date at signal reception
            frequency (double): frequency of the signal in Hz
            parameters (T[]): ionospheric model parameters at state date
        
        Returns:
            the path delay due to the ionosphere in m
        
        
        """
        ...
    @typing.overload
    def pathDelay(self, state: org.orekit.propagation.FieldSpacecraftState[_pathDelay_3__T], baseFrame: org.orekit.frames.TopocentricFrame, receptionDate: org.orekit.time.FieldAbsoluteDate[_pathDelay_3__T], frequency: float, parameters: typing.Union[typing.List[_pathDelay_3__T], jpype.JArray]) -> _pathDelay_3__T: ...
    _stec_1__T = typing.TypeVar('_stec_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def stec(self, date: org.orekit.time.AbsoluteDate, recP: org.orekit.bodies.GeodeticPoint, satP: org.orekit.bodies.GeodeticPoint) -> float:
        """
        Parameters:
            date (AbsoluteDate): current date
            recP (GeodeticPoint): receiver position
            satP (GeodeticPoint): satellite position
        
        Returns:
            the STEC in TECUnits
        
        """
        ...
    @typing.overload
    def stec(self, date: org.orekit.time.FieldAbsoluteDate[_stec_1__T], recP: org.orekit.bodies.FieldGeodeticPoint[_stec_1__T], satP: org.orekit.bodies.FieldGeodeticPoint[_stec_1__T]) -> _stec_1__T:
        """
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            recP (FieldGeodeticPoint<T> recP): receiver position
            satP (FieldGeodeticPoint<T> satP): satellite position
        
        Returns:
            the STEC in TECUnits
        
        
        """
        ...

class NeQuickParameters:
    """
    This class performs the computation of the parameters used by the NeQuick model.
    
    Since:
        10.1
    
    Also see:
        "European Union (2016). European GNSS (Galileo) Open Service-Ionospheric Correction Algorithm for Galileo Single
        Frequency Users. 1.2.", R
    """
    @typing.overload
    def __init__(self, fourierTimeSeries: FourierTimeSeries, latitude: float, longitude: float, modip: float): ...
    @typing.overload
    def __init__(self, dateTime: org.orekit.time.DateTimeComponents, flattenF2: typing.Union[typing.List[float], jpype.JArray], flattenFm3: typing.Union[typing.List[float], jpype.JArray], latitude: float, longitude: float, az: float, modip: float): ...
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
    def getBE(self, h: float) -> float:
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
    def getBF1(self, h: float) -> float:
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
            in km
        
        
        """
        ...
    def getHmF1(self) -> float:
        """
        Get the F1 layer maximum density height.
        
        Returns:
            in km
        
        
        """
        ...
    def getHmF2(self) -> float:
        """
        Get the F2 layer maximum density height.
        
        Returns:
            in km
        
        
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
    Container for ray-perigee parameters.
    
    By convention, point 1 is at lower height.
    
    Since:
        13.0
    """
    def __init__(self, recP: org.orekit.bodies.GeodeticPoint, satP: org.orekit.bodies.GeodeticPoint):
        """
        Constructor.
        
        Parameters:
            recP (GeodeticPoint): receiver position
            satP (GeodeticPoint): satellite position
        
        
        """
        ...
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
    Performs the computation of the coordinates along the integration path.
    
    Since:
        13.0
    """
    def __init__(self, n: int, ray: Ray, s1: float, s2: float):
        """
        Constructor.
        
        Parameters:
            n (int): number of intervals for integration (2 points per interval, hence 2n points will be generated)
            ray (Ray): ray-perigee parameters
            s1 (double): lower boundary of integration
            s2 (double): upper boundary for integration
        
        
        """
        ...
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
        
        Note there are 2 points per interval, so index must be between 0 (included) and 2n (excluded) for a segment built with n intervals
        
        Returns:
            number of points
        
        
        """
        ...
    def getPoint(self, index: int) -> org.orekit.bodies.GeodeticPoint:
        """
        Get point along the ray.
        
        Parameters:
            index (int): point index (between O included and getNbPoints excluded)
        
        Returns:
            point on ray
        
        Since:
            13.0
        
        
        """
        ...

class NeQuickGalileo(NeQuickModel):
    """
    Galileo-specific version of NeQuick engine.
    
    Since:
        13.0
    """
    @typing.overload
    def __init__(self, alpha: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, alpha: typing.Union[typing.List[float], jpype.JArray], utc: org.orekit.time.TimeScale): ...
    def getAlpha(self) -> typing.MutableSequence[float]:
        """
        Get effective ionisation level coefficients.
        
        Returns:
            effective ionisation level coefficients
        
        
        """
        ...

class NeQuickItu(NeQuickModel):
    """
    Original model from Aeronomy and Radiopropagation Laboratory of the Abdus Salam International Centre for Theoretical Physics Trieste, Italy.
    
    None of the code from Abdus Salam International Centre for Theoretical Physics Trieste has been used, the models have been reimplemented from scratch by the Orekit team.
    
    Since:
        13.0
    """
    def __init__(self, f107: float, utc: org.orekit.time.TimeScale):
        """
        Build a new instance.
        
        Parameters:
            f107 (double): solar flux
            utc (TimeScale): UTC time scale
        
        
        """
        ...
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
