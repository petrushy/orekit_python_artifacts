
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import jpype
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.models.earth.atmosphere.data
import org.orekit.time
import org.orekit.utils
import typing



class Atmosphere:
    """
    Interface for atmospheric models.
    """
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T:
        """
        Get the local density.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Returns:
            frame of the central body.
        
        Since:
            6.0
        
        
        """
        ...
    _getVelocity_0__T = typing.TypeVar('_getVelocity_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getVelocity(self, date: org.orekit.time.FieldAbsoluteDate[_getVelocity_0__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T]:
        """
        Get the inertial velocity of atmosphere molecules.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            velocity (m/s) (defined in the same frame as the position)
        
        
        """
        ...
    @typing.overload
    def getVelocity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the inertial velocity of atmosphere molecules.
        
        By default, atmosphere is supposed to have a null velocity in the central body frame.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            velocity (m/s) (defined in the same frame as the position)
        
        """
        ...

class DTM2000InputParameters(java.io.Serializable):
    """
    Container for solar activity data, compatible with DTM2000 Atmosphere model. This model needs mean and instantaneous solar flux and geomagnetic incides to compute the local density. Mean solar flux is (for the moment) represented by the F10.7 indices. Instantaneous flux can be set to the mean value if the data is not available. Geomagnetic acivity is represented by the Kp indice, which goes from 1 (very low activity) to 9 (high activity).
    
    All needed solar activity data can be found on the gov
    """
    def get24HoursKp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the last 24H mean geomagnetic index.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 24H geomagnetic index
        
        
        """
        ...
    def getInstantFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous solar flux
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMeanFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Returns:
            the minimum date.
        
        
        """
        ...
    def getThreeHourlyKP(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using: delay=6-abs(lat)*0.033 (lat in deg.)
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 3H geomagnetic index
        
        
        """
        ...

class JB2006InputParameters(java.io.Serializable):
    """
    Interface for solar activity and magnetic activity data.
    """
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the Geomagnetic planetary 3-hour index A :sub:`p` . Tabular time 6.7 hours earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the A :sub:`p` index
        
        
        """
        ...
    def getF10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux index (1e :sup:`-22` Watt/(m²Hertz)). Tabular time 1.0 day earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous F10.7 index
        
        
        """
        ...
    def getF10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux. Averaged 81-day centered F10.7 B index on the input time.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux F10.7B index
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Returns:
            the minimum date.
        
        
        """
        ...
    def getS10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV index (26-34 nm) scaled to F10. Tabular time 1 day earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the EUV S10 index
        
        
        """
        ...
    def getS10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV 81-day averaged centered index.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean EUV S10B index
        
        
        """
        ...
    def getXM10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 index scaled to F10.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the EUV S10 index
        
        
        """
        ...
    def getXM10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 81-day average centered index. Tabular time 5.0 days earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean EUV S10B index
        
        
        """
        ...

class JB2008InputParameters(java.io.Serializable):
    """
    Interface for solar activity and magnetic activity data.
    
    Those data are needed by the JB2008 atmosphere model.
    """
    def getDSTDTC(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the temperature change computed from Dst index.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the temperature change computed from Dst index
        
        
        """
        ...
    def getF10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux index (1e :sup:`-22` Watt/(m²Hertz)).
        
        Tabular time 1.0 day earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous F10.7 index
        
        
        """
        ...
    def getF10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux. Averaged 81-day centered F10.7 B index on the input time.
        
        Tabular time 1.0 day earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux F10.7B index
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Returns:
            the minimum date.
        
        
        """
        ...
    def getS10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV index (26-34 nm) scaled to F10.
        
        Tabular time 1.0 day earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the EUV S10 index
        
        
        """
        ...
    def getS10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV 81-day averaged centered index.
        
        Tabular time 1.0 day earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean EUV S10B index
        
        
        """
        ...
    def getXM10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 index scaled to F10.
        
        Tabular time 2.0 days earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the MG2 index
        
        
        """
        ...
    def getXM10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 81-day average centered index.
        
        Tabular time 2.0 days earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean MG2 index
        
        
        """
        ...
    def getY10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the Solar X-Ray & Lya index scaled to F10.
        
        Tabular time 5.0 days earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the Solar X-Ray & Lya index scaled to F10
        
        
        """
        ...
    def getY10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the Solar X-Ray & Lya 81-day ave. centered index.
        
        Tabular time 5.0 days earlier.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the Solar X-Ray & Lya 81-day ave. centered index
        
        
        """
        ...

class NRLMSISE00InputParameters(java.io.Serializable):
    """
    Container for solar activity data, compatible with NRLMSISE-00 atmosphere model.
    
    This model needs daily and average F10.7 solar fluxes and A :sub:`p` geomagnetic indices to compute the local density.
    """
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Get the A :sub:`p` geomagnetic indices.
        
        A :sub:`p` indices are provided as an array such as:
        
          - 0 → daily A :sub:`p`
          - 1 → 3 hr A :sub:`p` index for current time
          - 2 → 3 hr A :sub:`p` index for 3 hrs before current time
          - 3 → 3 hr A :sub:`p` index for 6 hrs before current time
          - 4 → 3 hr A :sub:`p` index for 9 hrs before current time
          - 5 → Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
          - 6 → Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the daily F10.7 solar flux for previous day.
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the daily F10.7 flux for previous day
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Returns:
            the minimum date.
        
        
        """
        ...

class AbstractSunInfluencedAtmosphere(Atmosphere):
    """
    Abstract class for atmospheric models using the Sun's position.
    
    Since:
        13.0
    """
    ...

class PythonAtmosphere(Atmosphere):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Specified by: getDensity in interface Atmosphere
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T:
        """
        Get the local density.
        
        Specified by: getDensity in interface Atmosphere
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Specified by: getFrame in interface Atmosphere
        
        Returns:
            frame of the central body.
        
        
        """
        ...
    _getVelocity_0__T = typing.TypeVar('_getVelocity_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getVelocity(self, date: org.orekit.time.FieldAbsoluteDate[_getVelocity_0__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getVelocity_0__T]:
        """
        Get the inertial velocity of atmosphere molecules.
        
        Specified by: getVelocity in interface Atmosphere
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            velocity (m/s) (defined in the same frame as the position)
        
        
        """
        ...
    @typing.overload
    def getVelocity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the inertial velocity of atmosphere molecules.
        
        By default, atmosphere is supposed to have a null velocity in the central body frame.
        
        Specified by: getVelocity in interface Atmosphere
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            velocity (m/s) (defined in the same frame as the position)
        
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

class PythonDTM2000InputParameters(DTM2000InputParameters):
    """
    Also see:
        serialized
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def get24HoursKp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the last 24H mean geomagnetic index.
        
        Specified by: get24HoursKp in interface DTM2000InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 24H geomagnetic index
        
        
        """
        ...
    def getInstantFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux.
        
        Specified by: getInstantFlux in interface DTM2000InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous solar flux
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Specified by: getMaxDate in interface DTM2000InputParameters
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMeanFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux.
        
        Specified by: getMeanFlux in interface DTM2000InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Specified by: getMinDate in interface DTM2000InputParameters
        
        Returns:
            the minimum date.
        
        
        """
        ...
    def getThreeHourlyKP(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 3 hours geomagnetic index. With a delay of 3 hours at pole to 6 hours at equator using: delay=6-abs(lat)*0.033 (lat in deg.)
        
        Specified by: getThreeHourlyKP in interface DTM2000InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 3H geomagnetic index
        
        
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

class PythonJB2006InputParameters(JB2006InputParameters):
    """
    Python implementation of the JB2006InputParameters interface. This class is part of the JCC Python interface and exposes all methods natively.
    
    Also see:
        serialized
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the Geomagnetic planetary 3-hour index A :sub:`p` . Tabular time 6.7 hours earlier.
        
        Specified by: getAp in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the A :sub:`p` index
        
        
        """
        ...
    def getF10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the instantaneous solar flux index (1e :sup:`-22` Watt/(m²Hertz)). Tabular time 1.0 day earlier.
        
        Specified by: getF10 in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the instantaneous F10.7 index
        
        
        """
        ...
    def getF10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the mean solar flux. Averaged 81-day centered F10.7 B index on the input time.
        
        Specified by: getF10B in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the mean solar flux F10.7B index
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Specified by: getMaxDate in interface JB2006InputParameters
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Specified by: getMinDate in interface JB2006InputParameters
        
        Returns:
            the minimum date.
        
        
        """
        ...
    def getS10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV index (26-34 nm) scaled to F10. Tabular time 1 day earlier.
        
        Specified by: getS10 in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the EUV S10 index
        
        
        """
        ...
    def getS10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the EUV 81-day averaged centered index.
        
        Specified by: getS10B in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean EUV S10B index
        
        
        """
        ...
    def getXM10(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 index scaled to F10.
        
        Specified by: getXM10 in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the EUV S10 index
        
        
        """
        ...
    def getXM10B(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the MG2 81-day average centered index. Tabular time 5.0 days earlier.
        
        Specified by: getXM10B in interface JB2006InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the the mean EUV S10B index
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonJB2008InputParameters(JB2008InputParameters):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDSTDTC(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getF10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getF10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate: ...
    def getS10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getS10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getXM10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getXM10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getY10(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getY10B(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonNRLMSISE00InputParameters(NRLMSISE00InputParameters):
    """
    Also see:
        serialized
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getAp(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Get the A :sub:`p` geomagnetic indices.
        
        A :sub:`p` indices are provided as an array such as:
        
          - 0 -> daily A :sub:`p`
          - 1 -> 3 hr A :sub:`p` index for current time
          - 2 -> 3 hr A :sub:`p` index for 3 hrs before current time
          - 3 -> 3 hr A :sub:`p` index for 6 hrs before current time
          - 4 -> 3 hr A :sub:`p` index for 9 hrs before current time
          - 5 -> Average of eight 3 hr A :sub:`p` indices from 12 to 33 hrs prior to current time
          - 6 -> Average of eight 3 hr A :sub:`p` indices from 36 to 57 hrs prior to current time
        
        Specified by: getAp in interface NRLMSISE00InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the array of A :sub:`p` indices
        
        
        """
        ...
    def getAverageFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the 81 day average of F10.7 solar flux centered on current day.
        
        Specified by: getAverageFlux in interface NRLMSISE00InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the 81 day average of F10.7 solar flux centered on current day
        
        
        """
        ...
    def getDailyFlux(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the value of the daily F10.7 solar flux for previous day.
        
        Specified by: getDailyFlux in interface NRLMSISE00InputParameters
        
        Parameters:
            date (AbsoluteDate): the current date
        
        Returns:
            the daily F10.7 flux for previous day
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range maximum date.
        
        Specified by: getMaxDate in interface NRLMSISE00InputParameters
        
        Returns:
            the maximum date.
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Gets the available data range minimum date.
        
        Specified by: getMinDate in interface NRLMSISE00InputParameters
        
        Returns:
            the minimum date.
        
        
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

class SimpleExponentialAtmosphere(Atmosphere):
    """
    Simple exponential atmospheric model.
    
    This model represents a simple atmosphere with an exponential density and rigidly bound to the underlying rotating body.
    """
    def __init__(self, shape: org.orekit.bodies.BodyShape, rho0: float, h0: float, hscale: float):
        """
        Create an exponential atmosphere.
        
        Parameters:
            shape (BodyShape): body shape model
            rho0 (double): Density at the altitude h0
            h0 (double): Altitude of reference (m)
            hscale (double): Scale factor
        
        
        """
        ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Specified by: getDensity in interface Atmosphere
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T:
        """
        Description copied from interface: getDensity Get the local density.
        
        Specified by: getDensity in interface Atmosphere
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Specified by: getFrame in interface Atmosphere
        
        Returns:
            frame of the central body.
        
        
        """
        ...

class AbstractJacchiaBowmanModel(AbstractSunInfluencedAtmosphere):
    """
    Base class for Jacchia-Bowman atmospheric models.
    
    Since:
        13.1
    
    Also see:
        JB2006, JB2008
    """
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T:
        """
        Get the local density.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getEarth(self) -> org.orekit.bodies.BodyShape:
        """
        Get the Earth body shape.
        
        Returns:
            the Earth body shape
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Returns:
            frame of the central body.
        
        
        """
        ...
    def getUtc(self) -> org.orekit.time.TimeScale:
        """
        Get the UTC time scale.
        
        Returns:
            UTC time scale
        
        
        """
        ...

class DTM2000(AbstractSunInfluencedAtmosphere):
    """
    This atmosphere model is the realization of the DTM-2000 model.
    
    It is described in the paper:
    
    The DTM-2000 empirical thermosphere model with new data assimilation and constraints at lower boundary: accuracy and properties
    
    S. Bruinsma, G. Thuillier and F. Barlier
    
    Journal of Atmospheric and Solar-Terrestrial Physics 65 (2003) 1053–1070
    
    
    
    This model provides dense output for altitudes beyond 120 km.
    
    The model needs geographical and time information to compute general values, but also needs space weather data : mean and instantaneous solar flux and geomagnetic indices.
    
    Mean solar flux is (for the moment) represented by the F10.7 indices. Instantaneous flux can be set to the mean value if the data is not available. Geomagnetic activity is represented by the Kp index, which goes from 1 (very low activity) to 9 (high activity).
    
    All these data can be found on the gov
    """
    @typing.overload
    def __init__(self, parameters: DTM2000InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, parameters: DTM2000InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape, utc: org.orekit.time.TimeScale): ...
    _getDensity_2__T = typing.TypeVar('_getDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getDensity_3__T = typing.TypeVar('_getDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, day: int, alti: float, lon: float, lat: float, hl: float, f: float, fbar: float, akp3: float, akp24: float) -> float:
        """
        Get the local density with initial entries.
        
        Parameters:
            day (int): day of year
            alti (double): altitude in meters
            lon (double): local longitude (rad)
            lat (double): local latitude (rad)
            hl (double): local solar time in rad (O hr = 0 rad)
            f (double): instantaneous solar flux (F10.7)
            fbar (double): mean solar flux (F10.7)
            akp3 (double): 3 hrs geomagnetic activity index (1-9)
            akp24 (double): Mean of last 24 hrs geomagnetic activity index (1-9)
        
        Returns:
            the local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, day: int, alti: _getDensity_2__T, lon: _getDensity_2__T, lat: _getDensity_2__T, hl: _getDensity_2__T, f: float, fbar: float, akp3: float, akp24: float) -> _getDensity_2__T:
        """
        Get the local density with initial entries.
        
        Parameters:
            day (int): day of year
            alti (T): altitude in meters
            lon (T): local longitude (rad)
            lat (T): local latitude (rad)
            hl (T): local solar time in rad (O hr = 0 rad)
            f (double): instantaneous solar flux (F10.7)
            fbar (double): mean solar flux (F10.7)
            akp3 (double): 3 hrs geomagnetic activity index (1-9)
            akp24 (double): Mean of last 24 hrs geomagnetic activity index (1-9)
        
        Returns:
            the local density (kg/m³)
        
        Since:
            9.0
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_3__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_3__T], frame: org.orekit.frames.Frame) -> _getDensity_3__T:
        """
        Get the local density.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Returns:
            frame of the central body.
        
        
        """
        ...

class HarrisPriester(AbstractSunInfluencedAtmosphere):
    """
    This atmosphere model is the realization of the Modified Harris-Priester model.
    
    This model is a static one that takes into account the diurnal density bulge. It doesn't need any space weather data but a density vs. altitude table, which depends on solar activity.
    
    The implementation relies on the book:
    
    Satellite Orbits
    
    Oliver Montenbruck, Eberhard Gill
    
    Springer 2005
    """
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, double: float): ...
    @typing.overload
    def __init__(self, extendedPositionProvider: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.OneAxisEllipsoid, tabAltRho: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], n: float): ...
    _getDensity_2__T = typing.TypeVar('_getDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getDensity_3__T = typing.TypeVar('_getDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, sunInEarth: org.hipparchus.geometry.euclidean.threed.Vector3D, posInEarth: org.hipparchus.geometry.euclidean.threed.Vector3D) -> float:
        """
        Get the local density.
        
        Parameters:
            sunInEarth (Vector3D): position of the Sun in Earth frame (m)
            posInEarth (Vector3D): target position in Earth frame (m)
        
        Returns:
            the local density (kg/m³)
        
        Get the local density at some position.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³) or if altitude is below the model minimal altitude
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float: ...
    @typing.overload
    def getDensity(self, sunInEarth: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_2__T], posInEarth: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_2__T]) -> _getDensity_2__T:
        """
        Get the local density.
        
        Parameters:
            sunInEarth (FieldVector3D<T> sunInEarth): position of the Sun in Earth frame (m)
            posInEarth (FieldVector3D<T> posInEarth): target position in Earth frame (m)
        
        Returns:
            the local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_3__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_3__T], frame: org.orekit.frames.Frame) -> _getDensity_3__T:
        """
        Get the local density at some position.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³) or if altitude is below the model minimal altitude
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Returns:
            frame of the central body.
        
        
        """
        ...
    def getMaxAlt(self) -> float:
        """
        Get the maximal altitude for the model.
        
        Above this altitude, density is assumed to be zero.
        
        Returns:
            the maximal altitude (m)
        
        
        """
        ...
    def getMinAlt(self) -> float:
        """
        Get the minimal altitude for the model.
        
        No computation is possible below this altitude.
        
        Returns:
            the minimal altitude (m)
        
        
        """
        ...
    def getTabDensity(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get the current density table.
        
        The density table is an array such as:
        
          - tabAltRho[][0] = altitude (m)
          - tabAltRho[][1] = min density (kg/m³)
          - tabAltRho[][2] = max density (kg/m³)
        
        The altitude must be increasing without limitation in range.
        
        The returned density table is a copy of the current one.
        
        Returns:
            density vs. altitude table
        
        
        """
        ...

_NRLMSISE00__FieldOutput__T = typing.TypeVar('_NRLMSISE00__FieldOutput__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class NRLMSISE00(AbstractSunInfluencedAtmosphere):
    """
    This class implements the mathematical representation of the 2001 Naval Research Laboratory Mass Spectrometer and Incoherent Scatter Radar Exosphere (NRLMSISE-00) of the MSIS® class model.
    
    NRLMSISE-00 calculates the neutral atmosphere empirical model from the surface to lower exosphere (0 to 1000 km) and provides:
    
      - Exospheric Temperature above Input Position (K)
      - Local Temperature at Input Position (K)
      - Total Mass-Density at Input Position (kg/m³)
      - Partial Densities at Input Position (1/m³) for:
    
          - He,
          - H,
          - N,
          - O,
          - Ar,
          - N2,
          - O2,
          - anomalous oxygen.
    
    
    
    The model needs geographical and time information to compute general values, but also needs space weather data:
    
      - mean and daily solar flux,
      - geomagnetic indices.
    
    Switches can be used to turn on and off particular variations:
    
    0 is off, 1 is on, and 2 is main effects off but cross terms on.
    
    The standard value is 1 for all the 23 available switches.
    
    Function of each switch according to its number:
    
      - #1 - F10.7 effect on mean
      - #2 - Independent of time
      - #3 - Symmetrical annual
      - #4 - Symmetrical semiannual
      - #5 - Asymmetrical annual
      - #6 - Asymmetrical semiannual
      - #7 - Diurnal
      - #8 - Semidiurnal
      - #9 - Daily Ap []
      - #10 - All UT, longitudinal effects
      - #11 - Longitudinal
      - #12 - UT and mixed UT, longitudinal
      - #13 - Mixed AP, UT, longitudinal
      - #14 - Terdiurnal
      - #15 - Departures from diffusive equilibrium
      - #16 - All exospheric temperature variations
      - #17 - All variations from 120 km temperature (TLB)
      - #18 - All lower thermosphere (TN1) temperature variations
      - #19 - All 120 km gradient (S) variations
      - #20 - All upper stratosphere (TN2) temperature variations
      - #21 - All variations from 120 km values (ZLB)
      - #22 - All lower mesosphere temperature (TN3) variations
      - #23 - Turbopause scale height variations
    
    [] Switch #9 is a bit specific:
    
      - set to 1, the daily Ap only is used (first element of ap array),
      - set to -1, the entire array of ap is used, including 3 hr ap indices.
    
    The NRLMSISE-00 model was developed by Mike Picone, Alan Hedin, and Doug Drob.
    
    They also wrote a NRLMSISE-00 distribution package in FORTRAN available at:
    
    ftp://hanna.ccmc.gsfc.nasa.gov/pub/modelweb/atmospheric/msis/nrlmsise00/
    
    
    
    Dominik Brodowski implemented a C version of the NRLMSISE-00 model available at:
    
    https://www.brodo.de/space/nrlmsise/index.html
    
    Instances of this class are immutable.
    
    Since:
        8.1
    """
    @typing.overload
    def __init__(self, parameters: NRLMSISE00InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, parameters: NRLMSISE00InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape, ut: org.orekit.time.TimeScale): ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T:
        """
        Get the local density.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Returns:
            frame of the central body.
        
        
        """
        ...
    def withSwitch(self, number: int, value: int) -> 'NRLMSISE00':
        """
        Change a switch.
        
        This method creates a new instance, the current instance is not changed at all!
        
        Parameters:
            number (int): switch number between 1 and 23
            value (int): switch value
        
        Returns:
            a new instance, with switch changed
        
        
        """
        ...
    class FieldOutput(typing.Generic[_NRLMSISE00__FieldOutput__T]):
        def getDensity(self, int: int) -> _NRLMSISE00__FieldOutput__T: ...

class PythonAbstractSunInfluencedAtmosphere(AbstractSunInfluencedAtmosphere):
    def __init__(self, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable]):
        """
        Constructor.
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getDensity_1__T = typing.TypeVar('_getDensity_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, date: org.orekit.time.AbsoluteDate, position: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density.
        
        Parameters:
            date (AbsoluteDate): current date
            position (Vector3D): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, date: org.orekit.time.FieldAbsoluteDate[_getDensity_1__T], position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_1__T], frame: org.orekit.frames.Frame) -> _getDensity_1__T:
        """
        Get the local density.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            position (FieldVector3D<T> position): current position in frame
            frame (Frame): the frame in which is defined the position
        
        Returns:
            local density (kg/m³)
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
        Get the frame of the central body.
        
        Returns:
            frame of the central body.
        
        
        """
        ...
    def getSun(self) -> org.orekit.utils.ExtendedPositionProvider:
        """
        Getter for Sun's position provider.
        
        Overrides: getSun in class AbstractSunInfluencedAtmosphere
        
        Returns:
            position provider
        
        
        """
        ...
    _getSunPosition_0__T = typing.TypeVar('_getSunPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getSunPosition(self, date: org.orekit.time.FieldAbsoluteDate[_getSunPosition_0__T], frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getSunPosition_0__T]:
        """
        Overrides: getSunPosition in class AbstractSunInfluencedAtmosphere
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date of output position
            frame (Frame): frame of output position
        
        Returns:
            Sun's position
        
        
        """
        ...
    @typing.overload
    def getSunPosition(self, date: org.orekit.time.AbsoluteDate, frame: org.orekit.frames.Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Method returning the Sun's position vector.
        
        Overrides: getSunPosition in class AbstractSunInfluencedAtmosphere
        
        Parameters:
            date (AbsoluteDate): date of output position
            frame (Frame): frame of output position
        
        Returns:
            Sun's position
        
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

class JB2006(AbstractJacchiaBowmanModel):
    """
    This is the realization of the Jacchia-Bowman 2006 atmospheric model.
    
    It is described in the paper:
    
    `A New Empirical Thermospheric Density Model JB2006 Using New Solar Indices <http://sol.spacenvironment.net/~JB2006/pubs/JB2006_AIAA-6166_model.pdf>`
    
    Bruce R. Bowman, W. Kent Tobiska and Frank A. Marcos
    
    
    
    AIAA 2006-6166
    
    
    
    This model provides dense output for all altitudes and positions. Output data are :
    
      - Exospheric Temperature above Input Position (deg K)
      - Temperature at Input Position (deg K)
      - Total Mass-Density at Input Position (kg/m³)
    
    The model needs geographical and time information to compute general values, but also needs space weather data : mean and daily solar flux, retrieved threw different indices, and planetary geomagnetic indices.
    
    More information on these indices can be found on the ` official JB2006 website. <http://sol.spacenvironment.net/~JB2006/JB2006_index.html>`
    
    Since:
        13.1
    """
    @typing.overload
    def __init__(self, parameters: JB2006InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, parameters: JB2006InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape, utc: org.orekit.time.TimeScale): ...

class JB2008(AbstractJacchiaBowmanModel):
    """
    This is the realization of the Jacchia-Bowman 2008 atmospheric model.
    
    It is described in the paper:
    
    
    
    class:`~org.orekit.models.earth.atmosphere.https:.www.researchgate.net.publication.228621668_A_New_Empirical_Thermospheric_Density_Model_JB2008_Using_New_Solar_and_Geomagnetic_Indices`
    
    Bruce R. Bowman & al.
    
    AIAA 2008-6438
    
    
    
    Two computation methods are proposed to the user:
    
      - one OREKIT independent and compliant with initial FORTRAN routine entry values:
        getDensity.
      -         one compliant with OREKIT Atmosphere interface, necessary to the DragForce computation.
    
    This model provides dense output for all altitudes and positions. Output data are :
    
      - Exospheric Temperature above Input Position (deg K)
      - Temperature at Input Position (deg K)
      - Total Mass-Density at Input Position (kg/m³)
    
    The model needs geographical and time information to compute general values, but also needs space weather data : mean and daily solar flux, retrieved through different indices, and planetary geomagnetic indices.
    
    More information on these indices can be found on the ` official JB2008 website. <http://sol.spacenvironment.net/~JB2008/indices.html>`
    """
    @typing.overload
    def __init__(self, parameters: JB2008InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape): ...
    @typing.overload
    def __init__(self, parameters: JB2008InputParameters, sun: typing.Union[org.orekit.utils.ExtendedPositionProvider, typing.Callable], earth: org.orekit.bodies.BodyShape, utc: org.orekit.time.TimeScale): ...
    _getDensity_2__T = typing.TypeVar('_getDensity_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _getDensity_3__T = typing.TypeVar('_getDensity_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getDensity(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: org.orekit.frames.Frame) -> float:
        """
        Get the local density with initial entries.
        
        The method creates a new instance of JB2008 model and set the input solar activity data equal to the provided one. These data are then available form PAST_INFINITY to FUTURE_INFINITY.
        
        Parameters:
            dateMJD (double): date and time, in modified julian days and fraction
            sunRA (double): Right Ascension of Sun (radians).
            sunDecli (double): Declination of Sun (radians).
            satLon (double): Right Ascension of position (radians)
            satLat (double): Geocentric latitude of position (radians)
            satAlt (double): Height of position (m)
            f10 (double): 10.7-cm Solar flux (1e :sup:`-22` Watt/(m²Hertz))
        
        (Tabular time 1.0 day earlier) f10B (double): 10.7-cm Solar Flux, averaged 81-day centered on the input time
        
        (Tabular time 1.0 day earlier) s10 (double): EUV index (26-34 nm) scaled to F10
        
        (Tabular time 1 day earlier) s10B (double): UV 81-day averaged centered index (Tabular time 1 day earlier) xm10 (double): MG2 index scaled to F10
        
        (Tabular time 2.0 days earlier) xm10B (double): MG2 81-day ave. centered index
        
        (Tabular time 2.0 days earlier) y10 (double): Solar X-Ray & Lya index scaled to F10
        
        (Tabular time 5.0 days earlier) y10B (double): Solar X-Ray & Lya 81-day ave. centered index
        
        (Tabular time 5.0 days earlier) dstdtc (double): Temperature change computed from Dst index
        
        Returns:
            total mass-Density at input position (kg/m³)
        
        """
        ...
    @typing.overload
    def getDensity(self, dateMJD: float, sunRA: float, sunDecli: float, satLon: float, satLat: float, satAlt: float, f10: float, f10B: float, s10: float, s10B: float, xm10: float, xm10B: float, y10: float, y10B: float, dstdtc: float) -> float: ...
    @typing.overload
    def getDensity(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getDensity_2__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getDensity_2__T], frame: org.orekit.frames.Frame) -> _getDensity_2__T:
        """
        Get the local density with initial entries.
        
        The method creates a new instance of JB2008 model and set the input solar activity data equal to the provided one. These data are then available form PAST_INFINITY to FUTURE_INFINITY.
        
        Parameters:
            dateMJD (T): date and time, in modified julian days and fraction
            sunRA (T): Right Ascension of Sun (radians).
            sunDecli (T): Declination of Sun (radians).
            satLon (T): Right Ascension of position (radians)
            satLat (T): Geocentric latitude of position (radians)
            satAlt (T): Height of position (m)
            f10 (double): 10.7-cm Solar flux (1e :sup:`-22` Watt/(m²Hertz))
        
        (Tabular time 1.0 day earlier) f10B (double): 10.7-cm Solar Flux, averaged 81-day centered on the input time
        
        (Tabular time 1.0 day earlier) s10 (double): EUV index (26-34 nm) scaled to F10
        
        (Tabular time 1 day earlier) s10B (double): UV 81-day averaged centered index (Tabular time 1 day earlier) xm10 (double): MG2 index scaled to F10
        
        (Tabular time 2.0 days earlier) xm10B (double): MG2 81-day ave. centered index
        
        (Tabular time 2.0 days earlier) y10 (double): Solar X-Ray & Lya index scaled to F10
        
        (Tabular time 5.0 days earlier) y10B (double): Solar X-Ray & Lya 81-day ave. centered index
        
        (Tabular time 5.0 days earlier) dstdtc (double): Temperature change computed from Dst index
        
        Returns:
            total mass-Density at input position (kg/m³)
        
        
        """
        ...
    @typing.overload
    def getDensity(self, dateMJD: _getDensity_3__T, sunRA: _getDensity_3__T, sunDecli: _getDensity_3__T, satLon: _getDensity_3__T, satLat: _getDensity_3__T, satAlt: _getDensity_3__T, f10: float, f10B: float, s10: float, s10B: float, xm10: float, xm10B: float, y10: float, y10B: float, dstdtc: float) -> _getDensity_3__T: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models.earth.atmosphere")``.

    AbstractJacchiaBowmanModel: typing.Type[AbstractJacchiaBowmanModel]
    AbstractSunInfluencedAtmosphere: typing.Type[AbstractSunInfluencedAtmosphere]
    Atmosphere: typing.Type[Atmosphere]
    DTM2000: typing.Type[DTM2000]
    DTM2000InputParameters: typing.Type[DTM2000InputParameters]
    HarrisPriester: typing.Type[HarrisPriester]
    JB2006: typing.Type[JB2006]
    JB2006InputParameters: typing.Type[JB2006InputParameters]
    JB2008: typing.Type[JB2008]
    JB2008InputParameters: typing.Type[JB2008InputParameters]
    NRLMSISE00: typing.Type[NRLMSISE00]
    NRLMSISE00InputParameters: typing.Type[NRLMSISE00InputParameters]
    PythonAbstractSunInfluencedAtmosphere: typing.Type[PythonAbstractSunInfluencedAtmosphere]
    PythonAtmosphere: typing.Type[PythonAtmosphere]
    PythonDTM2000InputParameters: typing.Type[PythonDTM2000InputParameters]
    PythonJB2006InputParameters: typing.Type[PythonJB2006InputParameters]
    PythonJB2008InputParameters: typing.Type[PythonJB2008InputParameters]
    PythonNRLMSISE00InputParameters: typing.Type[PythonNRLMSISE00InputParameters]
    SimpleExponentialAtmosphere: typing.Type[SimpleExponentialAtmosphere]
    data: org.orekit.models.earth.atmosphere.data.__module_protocol__
