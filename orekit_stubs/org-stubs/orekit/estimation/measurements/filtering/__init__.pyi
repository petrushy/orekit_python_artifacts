
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org
import org.orekit.estimation.measurements
import org.orekit.files.rinex.observation
import org.orekit.gnss
import org.orekit.propagation
import typing



class DualFrequencySmoother:
    """
    Handler to perform pseudo-range smoothing using Divergence-Free phase combinations.
    
    Since:
        11.2
    """
    def __init__(self, threshold: float, N: int):
        """
        Simple constructor.
        
        Parameters:
            threshold (double): threshold for loss of lock detection (represents the maximum difference between smoothed and measured values for loss of
                lock detection)
            N (int): window size of the Hatch Filter
        
        
        """
        ...
    def copyObservationData(self, obsData: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
        Copy an ObservationData object.
        
        Parameters:
            obsData (ObservationData): observation data to copy
        
        Returns:
            a copy of the input observation data
        
        
        """
        ...
    def createFilter(self, codeData: org.orekit.files.rinex.observation.ObservationData, phaseDataF1: org.orekit.files.rinex.observation.ObservationData, phaseDataF2: org.orekit.files.rinex.observation.ObservationData, satSystem: org.orekit.gnss.SatelliteSystem) -> 'DualFrequencyHatchFilter':
        """
        Creates an Hatch filter given initial data.
        
        Parameters:
            codeData (ObservationData): input code observation data
            phaseDataF1 (ObservationData): input phase observation data for the first frequency
            phaseDataF2 (ObservationData): input phase observation data for the second frequency
            satSystem (SatelliteSystem): satellite system corresponding to the observations
        
        Returns:
            an Hatch filter for the input data
        
        
        """
        ...
    def filterDataSet(self, listODS: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet], satSystem: org.orekit.gnss.SatelliteSystem, prnNumber: int, obsTypeF1: org.orekit.gnss.ObservationType, obsTypeF2: org.orekit.gnss.ObservationType) -> None:
        """
        Applies a Dual Frequency Hatch filter to a list of ObservationDataSet.
        
        Parameters:
            listODS (List<ObservationDataSet> listODS): input observation data sets
            satSystem (SatelliteSystem): satellite System from which to filter the pseudo-range values
            prnNumber (int): PRN identifier to identify the satellite from which to filter the pseudo-range values
            obsTypeF1 (ObservationType): observation type to be used as the first frequency for filtering
            obsTypeF2 (ObservationType): observation type to be used as the second frequency for filtering
        
        
        """
        ...
    def getFilteredDataMap(self) -> java.util.Map[org.orekit.gnss.ObservationType, java.util.List['SmoothedObservationDataSet']]:
        """
        Get the map of the filtered data.
        
        Returns:
            a map containing the filtered data.
        
        
        """
        ...
    def getMapFilters(self) -> java.util.Map[org.orekit.gnss.ObservationType, 'DualFrequencyHatchFilter']:
        """
        Get the map storing the filters for each observation type.
        
        Returns:
            the map storing the filters for each observation type
        
        
        """
        ...

_MeasurementFilter__T = typing.TypeVar('_MeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class MeasurementFilter(typing.Generic[_MeasurementFilter__T]):
    """
    Interface for measurement pre-processing filter.
    
    Pre-processing filters are used to disabled measurements before they are used during an orbit determination process. Example of pre-processing filters are:
    
      - Minimum satellite elevation
      - Minimum value of the signal-to-noise ratio
      - Measurement residual
    
    
    Since:
        10.2
    """
    def filter(self, measurement: org.orekit.estimation.measurements.ObservedMeasurement[_MeasurementFilter__T], state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Apply a filter to an observed measurement.
        
        If the observed measurement is rejected by the filter, the method isEnabled will return false.
        
        Parameters:
            measurement (ObservedMeasurement<MeasurementFilter> measurement): observed measurement
            state (SpacecraftState): current spacecraft state.
        
        
        """
        ...

class SingleFrequencySmoother:
    """
    Handler to perform pseudo-range smoothing using single frequency measurements.
    
    Since:
        11.2
    """
    def __init__(self, type: org.orekit.gnss.MeasurementType, threshold: float, N: int, integrationTime: float):
        """
        Simple constructor.
        
        Parameters:
            type (MeasurementType): type of the smoothing measurements
            threshold (double): threshold for loss of lock detection (represents the maximum difference between smoothed and measured values for loss of
                lock detection)
            N (int): window size of the Hatch Filter
            integrationTime (double): time interval between two measurements (s)
        
        
        """
        ...
    def copyObservationData(self, obsData: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
        Copy an ObservationData object.
        
        Parameters:
            obsData (ObservationData): observation data to copy
        
        Returns:
            a copy of the input observation data
        
        
        """
        ...
    def createFilter(self, codeData: org.orekit.files.rinex.observation.ObservationData, smoothingData: org.orekit.files.rinex.observation.ObservationData, system: org.orekit.gnss.SatelliteSystem) -> 'SingleFrequencyHatchFilter':
        """
        Creates an Hatch filter given initial data.
        
        Parameters:
            codeData (ObservationData): input code observation data
            smoothingData (ObservationData): input smoothing observation data
            system (SatelliteSystem): satellite system corresponding to the observations
        
        Returns:
            an Hatch filter for the input data
        
        
        """
        ...
    def filterDataSet(self, listODS: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet], satSystem: org.orekit.gnss.SatelliteSystem, prnNumber: int, obsType: org.orekit.gnss.ObservationType) -> None:
        """
        Applies a Single Frequency Hatch filter to a list of ObservationDataSet.
        
        Parameters:
            listODS (List<ObservationDataSet> listODS): input observation data sets
            satSystem (SatelliteSystem): satellite System from which to filter the pseudo-range values
            prnNumber (int): PRN identifier to identify the satellite from which to filter the pseudo-range values
            obsType (ObservationType): observation type to use for filtering
        
        
        """
        ...
    def getFilteredDataMap(self) -> java.util.Map[org.orekit.gnss.ObservationType, java.util.List['SmoothedObservationDataSet']]:
        """
        Get the map of the filtered data.
        
        Returns:
            a map containing the filtered data.
        
        
        """
        ...
    def getMapFilters(self) -> java.util.Map[org.orekit.gnss.ObservationType, 'SingleFrequencyHatchFilter']:
        """
        Get the map storing the filters for each observation type.
        
        Returns:
            the map storing the filters for each observation type
        
        
        """
        ...

class SmoothedObservationDataSet:
    """
    Container used to store smoothed observation data along with the original data set it originates from.
    
    Since:
        11.2
    """
    def __init__(self, smoothedObsData: org.orekit.files.rinex.observation.ObservationData, obsDataSet: org.orekit.files.rinex.observation.ObservationDataSet):
        """
        Simple constructor.
        
        Parameters:
            smoothedObsData (ObservationData): smoothed observation data
            obsDataSet (ObservationDataSet): original observation data set used to compute the smoothed observation data
        
        
        """
        ...
    def getDataSet(self) -> org.orekit.files.rinex.observation.ObservationDataSet:
        """
        Get the original observation data set used to compute the smoothed observation data.
        
        Returns:
            the original observation data set used to compute the smoothed observation data
        
        
        """
        ...
    def getSmoothedData(self) -> org.orekit.files.rinex.observation.ObservationData:
        """
        Get the smoothed observation data.
        
        Returns:
            the smoothed observation data
        
        
        """
        ...

_ElevationFilter__T = typing.TypeVar('_ElevationFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ElevationFilter(MeasurementFilter[_ElevationFilter__T], typing.Generic[_ElevationFilter__T]):
    """
    Elevation pre-processing filter.
    
    Since:
        10.2
    """
    def __init__(self, station: org.orekit.estimation.measurements.GroundStation, threshold: float):
        """
        Constructor.
        
        Parameters:
            station (GroundStation): considered by the filter
            threshold (double): minimum elevation for a measurements to be accepted, in radians
        
        
        """
        ...
    def filter(self, measurement: org.orekit.estimation.measurements.ObservedMeasurement[_ElevationFilter__T], state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Apply a filter to an observed measurement.
        
        If the observed measurement is rejected by the filter, the method isEnabled will return false.
        
        Specified by: filter in interface MeasurementFilter
        
        Parameters:
            measurement (ObservedMeasurement<ElevationFilter> measurement): observed measurement
            state (SpacecraftState): current spacecraft state.
        
        
        """
        ...

_PythonMeasurementFilter__T = typing.TypeVar('_PythonMeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementFilter(MeasurementFilter[_PythonMeasurementFilter__T], typing.Generic[_PythonMeasurementFilter__T]):
    """
    Interface for measurement pre-processing filter.
    
    Pre-processing filters are used to disabled measurements before they are used during an orbit determination process. Example of pre-processing filters are:
    
      - Minimum satellite elevation
      - Minimum value of the signal-to-noise ratio
      - Measurement residual
    
    
    Since:
        10.2
    """
    def __init__(self): ...
    def filter(self, measurement: org.orekit.estimation.measurements.ObservedMeasurement[_PythonMeasurementFilter__T], state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Apply a filter to an observed measurement.
        
        If the observed measurement is rejected by the filter, the method isEnabled will return false.
        
        Specified by: filter in interface MeasurementFilter
        
        Parameters:
            measurement (ObservedMeasurement<PythonMeasurementFilter> measurement): observed measurement
            state (SpacecraftState): current spacecraft state.
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
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

_ResidualFilter__T = typing.TypeVar('_ResidualFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ResidualFilter(MeasurementFilter[_ResidualFilter__T], typing.Generic[_ResidualFilter__T]):
    """
    Residual pre-processing filter.
    
    The measurement residual is defined by the difference between the observed value and the estimated value of the measurement.
    
    Since:
        10.2
    """
    def __init__(self, threshold: float):
        """
        Constructor.
        
        Parameters:
            threshold (double): maximum value for the measurement residual
        
        
        """
        ...
    def filter(self, measurement: org.orekit.estimation.measurements.ObservedMeasurement[_ResidualFilter__T], state: org.orekit.propagation.SpacecraftState) -> None:
        """
        Apply a filter to an observed measurement.
        
        If the observed measurement is rejected by the filter, the method isEnabled will return false.
        
        Specified by: filter in interface MeasurementFilter
        
        Parameters:
            measurement (ObservedMeasurement<ResidualFilter> measurement): observed measurement
            state (SpacecraftState): current spacecraft state.
        
        
        """
        ...

class DualFrequencyHatchFilter(org.orekit.estimation.measurements.filtering.HatchFilter):
    """
    Hatch Filter using Carrier-Phase measurements taken at two different frequencies, to form a Divergence-Free phase combination.
    
    This filter uses a phase combination to mitigate the effects of the temporally varying ionospheric delays. Still, the spatial variation of the ionospheric delays are not compensated by this phase combination.
    
    Since:
        11.2
    
    Also see:
        "Subirana, J. S., Hernandez-Pajares, M., and José Miguel Juan Zornoza. (2013). GNSS Data Processing: Fundamentals and
        Algorithms. European Space Agency. Section 4.2.3.1.1"
    """
    def __init__(self, initCode: org.orekit.files.rinex.observation.ObservationData, initPhaseFreq1: org.orekit.files.rinex.observation.ObservationData, initPhaseFreq2: org.orekit.files.rinex.observation.ObservationData, wavelengthFreq1: float, wavelengthFreq2: float, threshold: float, N: int):
        """
        Constructor for the Dual Frequency Hatch Filter.
        
        The threshold parameter corresponds to the maximum difference between non-smoothed and smoothed pseudo range value, above which the filter is reset.
        
        Parameters:
            initCode (ObservationData): initial code measurement
            initPhaseFreq1 (ObservationData): initial phase measurement for the first chosen frequency
            initPhaseFreq2 (ObservationData): initial phase measurement for the second chosen frequency
            wavelengthFreq1 (double): initPhaseFreq1 observed value wavelength (m)
            wavelengthFreq2 (double): initPhaseFreq2 observed value wavelength (m)
            threshold (double): threshold for loss of lock detection (it represents the maximum difference between smoothed and measured values for loss
                of lock detection)
            N (int): window size of the Hatch Filter
        
        
        """
        ...
    def filterData(self, codeData: org.orekit.files.rinex.observation.ObservationData, phaseDataFreq1: org.orekit.files.rinex.observation.ObservationData, phaseDataFreq2: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
        This method filters the provided data given the state of the filter.
        
        Parameters:
            codeData (ObservationData): input code observation data
            phaseDataFreq1 (ObservationData): input phase observation data for the first frequency
            phaseDataFreq2 (ObservationData): input phase observation data for the second frequency
        
        Returns:
            the smoothed observation data
        
        
        """
        ...
    def getFirstFrequencyPhaseHistory(self) -> java.util.ArrayList[float]:
        """
        Get the history of phase values of the first frequency.
        
        Returns:
            the history of phase values of the first frequency
        
        
        """
        ...
    def getSecondFrequencyPhaseHistory(self) -> java.util.ArrayList[float]:
        """
        Get the history of phase values of the second frequency.
        
        Returns:
            the history of phase values of the second frequency
        
        
        """
        ...

class PythonHatchFilter(org.orekit.estimation.measurements.filtering.HatchFilter):
    def __init__(self, threshold: float, N: int):
        """
        Constructor for the Abstract Hatch Filter.
        
        Initialize the variables and set the initial pseudo-range state.
        
        Parameters:
            threshold (double): threshold for loss of lock detection (it represents the maximum difference between smoothed and measured values for loss
                of lock detection)
            N (int): window size of the Hatch Filter
        
        
        """
        ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: meth:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
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

class SingleFrequencyHatchFilter(org.orekit.estimation.measurements.filtering.HatchFilter):
    """
    Single frequency Hatch filter.
    
    The single frequency Hatch Filter is used to smooth the pseudo-range measurement using either a Doppler measurement or a carrier phase measurement.
    
    Since:
        11.2
    
    Also see:
        "Subirana, J. S., Hernandez-Pajares, M., and José Miguel Juan Zornoza. (2013). GNSS Data Processing: Fundamentals and
        Algorithms. European Space Agency.", "Zhou, Z., and Li, B. (2017). Optimal Doppler-aided smoothing strategy for GNSS
        navigation. GPS solutions, 21(1), 197-210."
    """
    def __init__(self, initCode: org.orekit.files.rinex.observation.ObservationData, initSmoothing: org.orekit.files.rinex.observation.ObservationData, type: org.orekit.gnss.MeasurementType, wavelength: float, threshold: float, N: int, integrationTime: float):
        """
        Constructor for the Single Frequency Hatch Filter.
        
        The threshold parameter corresponds to the maximum difference between non-smoothed and smoothed pseudo range value, above which the filter is reset.
        
        Parameters:
            initCode (ObservationData): initial code measurement
            initSmoothing (ObservationData): initial smoothing measurement
            type (MeasurementType): type of the smoothing measurement (CARRIER_PHASE or DOPPLER)
            wavelength (double): measurement value wavelength (m)
            threshold (double): threshold for loss of lock detection (represents the maximum difference between smoothed and measured values for loss of
                lock detection)
            N (int): window size of the Hatch Filter
            integrationTime (double): time interval between two measurements (s)
        
        
        """
        ...
    def filterData(self, codeData: org.orekit.files.rinex.observation.ObservationData, smoothingData: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
        This method filters the provided data given the state of the filter.
        
        Parameters:
            codeData (ObservationData): input code observation data
            smoothingData (ObservationData): input smoothing observation data
        
        Returns:
            the smoothed observation data
        
        
        """
        ...

class HatchFilter: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation.measurements.filtering")``.

    DualFrequencyHatchFilter: typing.Type[DualFrequencyHatchFilter]
    DualFrequencySmoother: typing.Type[DualFrequencySmoother]
    ElevationFilter: typing.Type[ElevationFilter]
    HatchFilter: typing.Type[HatchFilter]
    MeasurementFilter: typing.Type[MeasurementFilter]
    PythonHatchFilter: typing.Type[PythonHatchFilter]
    PythonMeasurementFilter: typing.Type[PythonMeasurementFilter]
    ResidualFilter: typing.Type[ResidualFilter]
    SingleFrequencyHatchFilter: typing.Type[SingleFrequencyHatchFilter]
    SingleFrequencySmoother: typing.Type[SingleFrequencySmoother]
    SmoothedObservationDataSet: typing.Type[SmoothedObservationDataSet]
