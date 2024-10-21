import java.util
import org
import org.orekit.estimation.measurements
import org.orekit.estimation.measurements.filtering.class-use
import org.orekit.files.rinex.observation
import org.orekit.gnss
import org.orekit.propagation
import typing



class DualFrequencySmoother:
    """
    public class DualFrequencySmoother extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Handler to perform pseudo-range smoothing using Divergence-Free phase combinations.
    
        Since:
            11.2
    """
    def __init__(self, double: float, int: int): ...
    def copyObservationData(self, observationData: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
            Copy an ObservationData object.
        
            Parameters:
                obsData (:class:`~org.orekit.files.rinex.observation.ObservationData`): observation data to copy
        
            Returns:
                a copy of the input observation data
        
        
        """
        ...
    def createFilter(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData, observationData3: org.orekit.files.rinex.observation.ObservationData, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'DualFrequencyHatchFilter':
        """
            Creates an Hatch filter given initial data.
        
            Parameters:
                codeData (:class:`~org.orekit.files.rinex.observation.ObservationData`): input code observation data
                phaseDataF1 (:class:`~org.orekit.files.rinex.observation.ObservationData`): input phase observation data for the first frequency
                phaseDataF2 (:class:`~org.orekit.files.rinex.observation.ObservationData`): input phase observation data for the second frequency
                satSystem (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system corresponding to the observations
        
            Returns:
                an Hatch filter for the input data
        
        
        """
        ...
    def filterDataSet(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet], satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, observationType: org.orekit.gnss.ObservationType, observationType2: org.orekit.gnss.ObservationType) -> None: ...
    def getFilteredDataMap(self) -> java.util.HashMap[org.orekit.gnss.ObservationType, java.util.List['SmoothedObservationDataSet']]: ...
    def getMapFilters(self) -> java.util.HashMap[org.orekit.gnss.ObservationType, 'DualFrequencyHatchFilter']: ...

_MeasurementFilter__T = typing.TypeVar('_MeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class MeasurementFilter(typing.Generic[_MeasurementFilter__T]):
    """
    public interface MeasurementFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>>
    
        Interface for measurement pre-processing filter.
    
        Pre-processing filters are used to disabled measurements before they are used during an orbit determination process.
        Example of pre-processing filters are:
    
          - Minimum satellite elevation
          - Minimum value of the signal-to-noise ratio
          - Measurement residual
    
    
        Since:
            10.2
    """
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_MeasurementFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

class SingleFrequencySmoother:
    """
    public class SingleFrequencySmoother extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Handler to perform pseudo-range smoothing using single frequency measurements.
    
        Since:
            11.2
    """
    def __init__(self, measurementType: org.orekit.gnss.MeasurementType, double: float, int: int, double2: float): ...
    def copyObservationData(self, observationData: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
            Copy an ObservationData object.
        
            Parameters:
                obsData (:class:`~org.orekit.files.rinex.observation.ObservationData`): observation data to copy
        
            Returns:
                a copy of the input observation data
        
        
        """
        ...
    def createFilter(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData, satelliteSystem: org.orekit.gnss.SatelliteSystem) -> 'SingleFrequencyHatchFilter':
        """
            Creates an Hatch filter given initial data.
        
            Parameters:
                codeData (:class:`~org.orekit.files.rinex.observation.ObservationData`): input code observation data
                smoothingData (:class:`~org.orekit.files.rinex.observation.ObservationData`): input smoothing observation data
                system (:class:`~org.orekit.gnss.SatelliteSystem`): satellite system corresponding to the observations
        
            Returns:
                an Hatch filter for the input data
        
        
        """
        ...
    def filterDataSet(self, list: java.util.List[org.orekit.files.rinex.observation.ObservationDataSet], satelliteSystem: org.orekit.gnss.SatelliteSystem, int: int, observationType: org.orekit.gnss.ObservationType) -> None: ...
    def getFilteredDataMap(self) -> java.util.HashMap[org.orekit.gnss.ObservationType, java.util.List['SmoothedObservationDataSet']]: ...
    def getMapFilters(self) -> java.util.HashMap[org.orekit.gnss.ObservationType, 'SingleFrequencyHatchFilter']: ...

class SmoothedObservationDataSet:
    """
    public class SmoothedObservationDataSet extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container used to store smoothed observation data along with the original data set it originates from.
    
        Since:
            11.2
    """
    def __init__(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationDataSet: org.orekit.files.rinex.observation.ObservationDataSet): ...
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
    public class ElevationFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Elevation pre-processing filter.
    
        Since:
            10.2
    """
    def __init__(self, groundStation: org.orekit.estimation.measurements.GroundStation, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ElevationFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

_PythonMeasurementFilter__T = typing.TypeVar('_PythonMeasurementFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class PythonMeasurementFilter(MeasurementFilter[_PythonMeasurementFilter__T], typing.Generic[_PythonMeasurementFilter__T]):
    """
    public class PythonMeasurementFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Interface for measurement pre-processing filter.
    
        Pre-processing filters are used to disabled measurements before they are used during an orbit determination process.
        Example of pre-processing filters are:
    
          - Minimum satellite elevation
          - Minimum value of the signal-to-noise ratio
          - Measurement residual
    
    
        Since:
            10.2
    """
    def __init__(self): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_PythonMeasurementFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...
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

_ResidualFilter__T = typing.TypeVar('_ResidualFilter__T', bound=org.orekit.estimation.measurements.ObservedMeasurement)  # <T>
class ResidualFilter(MeasurementFilter[_ResidualFilter__T], typing.Generic[_ResidualFilter__T]):
    """
    public class ResidualFilter<T extends :class:`~org.orekit.estimation.measurements.ObservedMeasurement`<T>> extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.estimation.measurements.filtering.MeasurementFilter`<T>
    
        Residual pre-processing filter.
    
        The measurement residual is defined by the difference between the observed value and the estimated value of the
        measurement.
    
        Since:
            10.2
    """
    def __init__(self, double: float): ...
    def filter(self, observedMeasurement: org.orekit.estimation.measurements.ObservedMeasurement[_ResidualFilter__T], spacecraftState: org.orekit.propagation.SpacecraftState) -> None: ...

class DualFrequencyHatchFilter(org.orekit.estimation.measurements.filtering.HatchFilter):
    """
    public class DualFrequencyHatchFilter extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Hatch Filter using Carrier-Phase measurements taken at two different frequencies, to form a Divergence-Free phase
        combination.
    
        This filter uses a phase combination to mitigate the effects of the temporally varying ionospheric delays. Still, the
        spatial variation of the ionospheric delays are not compensated by this phase combination.
    
        Since:
            11.2
    
        Also see:
            "Subirana, J. S., Hernandez-Pajares, M., and José Miguel Juan Zornoza. (2013). GNSS Data Processing: Fundamentals and
            Algorithms. European Space Agency. Section 4.2.3.1.1"
    """
    def __init__(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData, observationData3: org.orekit.files.rinex.observation.ObservationData, double: float, double2: float, double3: float, int: int): ...
    def filterData(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData, observationData3: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
            This method filters the provided data given the state of the filter.
        
            Parameters:
                codeData (:class:`~org.orekit.files.rinex.observation.ObservationData`): input code observation data
                phaseDataFreq1 (:class:`~org.orekit.files.rinex.observation.ObservationData`): input phase observation data for the first frequency
                phaseDataFreq2 (:class:`~org.orekit.files.rinex.observation.ObservationData`): input phase observation data for the second frequency
        
            Returns:
                the smoothed observation data
        
        
        """
        ...
    def getFirstFrequencyPhaseHistory(self) -> java.util.ArrayList[float]: ...
    def getSecondFrequencyPhaseHistory(self) -> java.util.ArrayList[float]: ...

class PythonHatchFilter(org.orekit.estimation.measurements.filtering.HatchFilter):
    """
    public class PythonHatchFilter extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    """
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

class SingleFrequencyHatchFilter(org.orekit.estimation.measurements.filtering.HatchFilter):
    """
    public class SingleFrequencyHatchFilter extends :class:`~org.orekit.estimation.measurements.filtering.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Single frequency Hatch filter.
    
        The single frequency Hatch Filter is used to smooth the pseudo-range measurement using either a Doppler measurement or a
        carrier phase measurement.
    
        Since:
            11.2
    
        Also see:
            "Subirana, J. S., Hernandez-Pajares, M., and José Miguel Juan Zornoza. (2013). GNSS Data Processing: Fundamentals and
            Algorithms. European Space Agency.", "Zhou, Z., and Li, B. (2017). Optimal Doppler-aided smoothing strategy for GNSS
            navigation. GPS solutions, 21(1), 197-210."
    """
    def __init__(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData, measurementType: org.orekit.gnss.MeasurementType, double: float, double2: float, int: int, double3: float): ...
    def filterData(self, observationData: org.orekit.files.rinex.observation.ObservationData, observationData2: org.orekit.files.rinex.observation.ObservationData) -> org.orekit.files.rinex.observation.ObservationData:
        """
            This method filters the provided data given the state of the filter.
        
            Parameters:
                codeData (:class:`~org.orekit.files.rinex.observation.ObservationData`): input code observation data
                smoothingData (:class:`~org.orekit.files.rinex.observation.ObservationData`): input smoothing observation data
        
            Returns:
                the smoothed observation data
        
        
        """
        ...

class HatchFilter: ...


class __module_protocol__(typing.Protocol):
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
    class-use: org.orekit.estimation.measurements.filtering.class-use.__module_protocol__
