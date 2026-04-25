
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import java.util.function
import java.util.stream
import jpype
import org
import org.hipparchus
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.data
import org.orekit.files.ccsds.definitions
import org.orekit.frames.encounter
import org.orekit.models.earth
import org.orekit.time
import org.orekit.utils
import typing



class AbstractEopLoader(org.orekit.data.AbstractSelfFeedingLoader):
    """
    Base class for EOP loaders.
    """
    def __init__(self, supportedNames: str, manager: org.orekit.data.DataProvidersManager, utcSupplier: typing.Union[java.util.function.Supplier[org.orekit.time.TimeScale], typing.Callable[[], org.orekit.time.TimeScale]]):
        """
        Simple constructor.
        
        Parameters:
            supportedNames (String): regular expression for supported files names.
            manager (DataProvidersManager): provides access to the EOP files.
            utcSupplier (Supplier<TimeScale> utcSupplier): UTC time scale.
        
        
        """
        ...

class CachedTransformProvider:
    """
    Thread-safe cached provider for frame transforms.
    
    This provider is based on a thread-safe Least Recently Used cache using date as it access key, hence saving computation time on transform building.
    
    This class is thread-safe.
    
    Since:
        13.0.3
    """
    def __init__(self, origin: 'Frame', destination: 'Frame', fullGenerator: typing.Union[java.util.function.Function[org.orekit.time.AbsoluteDate, 'Transform'], typing.Callable[[org.orekit.time.AbsoluteDate], 'Transform']], kinematicGenerator: typing.Union[java.util.function.Function[org.orekit.time.AbsoluteDate, 'KinematicTransform'], typing.Callable[[org.orekit.time.AbsoluteDate], 'KinematicTransform']], staticGenerator: typing.Union[java.util.function.Function[org.orekit.time.AbsoluteDate, 'StaticTransform'], typing.Callable[[org.orekit.time.AbsoluteDate], 'StaticTransform']], cacheSize: int):
        """
        Simple constructor.
        
        Parameters:
            origin (Frame): origin frame
            destination (Frame): destination frame
            fullGenerator (Function<AbsoluteDate, Transform> fullGenerator): generator for full transforms
            kinematicGenerator (Function<AbsoluteDate, KinematicTransform> kinematicGenerator): generator for kinematic transforms
            staticGenerator (Function<AbsoluteDate, StaticTransform> staticGenerator): generator for static transforms
            cacheSize (int): number of transforms kept in the date-based cache
        
        
        """
        ...
    def getCacheSize(self) -> int:
        """
        Get the nmber of transforms kept in the date-based cache.
        
        Returns:
            nmber of transforms kept in the date-based cache
        
        
        """
        ...
    def getDestination(self) -> 'Frame':
        """
        Get destination frame.
        
        Returns:
            destination frame
        
        
        """
        ...
    def getKinematicTransform(self, date: org.orekit.time.AbsoluteDate) -> 'KinematicTransform':
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    def getOrigin(self) -> 'Frame':
        """
        Get origin frame.
        
        Returns:
            origin frame
        
        
        """
        ...
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> 'StaticTransform':
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...

class EOPEntry(org.orekit.time.TimeStamped, java.io.Serializable):
    """
    This class holds an Earth Orientation Parameters entry.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, iTRFVersion: 'ITRFVersion', absoluteDate: org.orekit.time.AbsoluteDate): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float, double4: float, double5: float, double6: float, double7: float, double8: float, double9: float, double10: float, iTRFVersion: 'ITRFVersion', absoluteDate: org.orekit.time.AbsoluteDate, eopDataType: 'EopDataType'): ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getDdEps(self) -> float:
        """
        Get the correction for nutation in obliquity δΔε.
        
        Returns:
            correction for nutation in obliquity δΔε
        
        
        """
        ...
    def getDdPsi(self) -> float:
        """
        Get the correction for nutation in longitude δΔΨ.
        
        Returns:
            correction for nutation in longitude δΔΨ
        
        
        """
        ...
    def getDx(self) -> float:
        """
        Get the correction for Celestial Intermediate Pole (CIP) coordinates.
        
        Returns:
            correction for Celestial Intermediate Pole (CIP) coordinates
        
        
        """
        ...
    def getDy(self) -> float:
        """
        Get the correction for Celestial Intermediate Pole (CIP) coordinates.
        
        Returns:
            correction for Celestial Intermediate Pole (CIP) coordinates
        
        
        """
        ...
    def getEopDataType(self) -> 'EopDataType': ...
    def getITRFType(self) -> 'ITRFVersion':
        """
        Get the ITRF version this entry defines.
        
        Returns:
            ITRF version this entry defines
        
        Since:
            9.2
        
        
        """
        ...
    def getLOD(self) -> float:
        """
        Get the LoD (Length of Day) value.
        
        Returns:
            LoD in seconds
        
        
        """
        ...
    def getMjd(self) -> int:
        """
        Get the entry date (modified julian day, 00h00 UTC scale).
        
        Returns:
            entry date
        
        Also see:
            getDate
        
        
        """
        ...
    def getUT1MinusUTC(self) -> float:
        """
        Get the UT1-UTC value.
        
        Returns:
            UT1-UTC in seconds
        
        
        """
        ...
    def getX(self) -> float:
        """
        Get the X component of the pole motion.
        
        Returns:
            X component of pole motion
        
        
        """
        ...
    def getXRate(self) -> float:
        """
        Get the X component of the pole motion rate.
        
        Returns:
            X component of pole motion rate
        
        Since:
            12.0
        
        
        """
        ...
    def getY(self) -> float:
        """
        Get the Y component of the pole motion.
        
        Returns:
            Y component of pole motion
        
        
        """
        ...
    def getYRate(self) -> float:
        """
        Get the Y component of the pole motion rate.
        
        Returns:
            Y component of pole motion rate
        
        Since:
            12.0
        
        
        """
        ...

class EOPFittedModel:
    """
    Container for fitted model for Earth Orientation Parameters.
    
    Since:
        12.0
    
    Also see:
        PredictedEOPHistory, EOPFitter
    """
    def __init__(self, dut1: org.orekit.utils.SecularAndHarmonic, xP: org.orekit.utils.SecularAndHarmonic, yP: org.orekit.utils.SecularAndHarmonic, dx: org.orekit.utils.SecularAndHarmonic, dy: org.orekit.utils.SecularAndHarmonic):
        """
        Simple constructor.
        
        Parameters:
            dut1 (SecularAndHarmonic): fitted model for dut1 and LOD
            xP (SecularAndHarmonic): fitted model for pole x component
            yP (SecularAndHarmonic): fitted model for pole y component
            dx (SecularAndHarmonic): fitted model for nutation x component
            dy (SecularAndHarmonic): fitted model for nutation y component
        
        
        """
        ...
    def getDUT1(self) -> org.orekit.utils.SecularAndHarmonic:
        """
        Get the fitted secular and harmonics model for DUT1/LOD.
        
        LOD can be computed from DUT1 as osculatingDerivative(date)
        
        Returns:
            fitted secular and harmonics model for DUT1/LOD
        
        
        """
        ...
    def getDx(self) -> org.orekit.utils.SecularAndHarmonic:
        """
        Get the fitted secular and harmonics model for nutation x component.
        
        Returns:
            fitted secular and harmonics model for nutation x component
        
        
        """
        ...
    def getDy(self) -> org.orekit.utils.SecularAndHarmonic:
        """
        Get the fitted secular and harmonics model for nutation y component.
        
        Returns:
            fitted secular and harmonics model for nutation y component
        
        
        """
        ...
    def getXp(self) -> org.orekit.utils.SecularAndHarmonic:
        """
        Get the fitted secular and harmonics model for pole x component.
        
        Returns:
            fitted secular and harmonics model for pole x component
        
        
        """
        ...
    def getYp(self) -> org.orekit.utils.SecularAndHarmonic:
        """
        Get the fitted secular and harmonics model for pole y component.
        
        Returns:
            fitted secular and harmonics model for pole y component
        
        
        """
        ...

class EOPFitter(java.io.Serializable):
    """
    Earth Orientation Parameters fitter for PredictedEOPHistory.
    
    Since:
        12.0
    
    Also see:
        PredictedEOPHistory, SingleParameterFitter, serialized
    """
    def __init__(self, dut1Fitter: 'SingleParameterFitter', xPFitter: 'SingleParameterFitter', yPFitter: 'SingleParameterFitter', dxFitter: 'SingleParameterFitter', dyFitter: 'SingleParameterFitter'):
        """
        Simple constructor.
        
        Parameters:
            dut1Fitter (SingleParameterFitter): fitter for dut1 and LOD
            xPFitter (SingleParameterFitter): fitter for pole x component
            yPFitter (SingleParameterFitter): fitter for pole y component
            dxFitter (SingleParameterFitter): fitter for nutation x component
            dyFitter (SingleParameterFitter): fitter for nutation y component
        
        
        """
        ...
    def fit(self, rawHistory: 'EOPHistory') -> EOPFittedModel:
        """
        Fit raw history.
        
        Parameters:
            rawHistory (EOPHistory): raw EOP history to fit.
        
        Returns:
            fitted model
        
        
        """
        ...

class EOPHistory:
    """
    This class loads any kind of Earth Orientation Parameter data throughout a large time range.
    """
    DEFAULT_INTERPOLATION_DEGREE: typing.ClassVar[int] = ...
    """
    Default interpolation degree.
    
    Since:
        12.0
    
    Also see:
        constant
    
    
    """
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, int: int, collection: typing.Union[java.util.Collection[EOPEntry], typing.Sequence[EOPEntry], typing.Set[EOPEntry]], boolean: bool, timeScales: org.orekit.time.TimeScales):
        """
        Simple constructor.
        
        This method uses the getDefault.
        
        Parameters:
            conventions (IERSConventions): IERS conventions to which EOP refers
            interpolationDegree (int): interpolation degree (must be of the form 4k-1)
            data (Collection<? extends EOPEntry> data): the EOP data to use
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        public EOPHistory (IERSConventions conventions, int interpolationDegree, Collection<? extends EOPEntry> data, boolean simpleEOP, TimeScales timeScales)
        
        Simple constructor.
        
        Parameters:
            conventions (IERSConventions): IERS conventions to which EOP refers
            interpolationDegree (int): interpolation degree (must be of the form 4k-1)
            data (Collection<? extends EOPEntry> data): the EOP data to use
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
            timeScales (TimeScales): to use when computing EOP corrections.
        
        Since:
            10.1
        
        
        """
        ...
    def cachesTidalCorrection(self) -> bool:
        """
        Check if the instance caches tidal corrections.
        
        Returns:
            true if the instance caches tidal corrections
        
        Since:
            12.0
        
        
        """
        ...
    def checkEOPContinuity(self, maxGap: float) -> None:
        """
        Check Earth orientation parameters continuity.
        
        Parameters:
            maxGap (double): maximal allowed gap between entries (in seconds)
        
        
        """
        ...
    def getConventions(self) -> org.orekit.utils.IERSConventions:
        """
        Get the IERS conventions to which these EOP apply.
        
        Returns:
            IERS conventions to which these EOP apply
        
        
        """
        ...
    def getEOPHistoryWithoutCachedTidalCorrection(self) -> 'EOPHistory':
        """
        Get version of the instance that does not cache tidal correction.
        
        Returns:
            version of the instance that does not cache tidal correction
        
        Since:
            12.0
        
        
        """
        ...
    def getEndDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date of the last available Earth Orientation Parameters.
        
        Returns:
            the end date of the available data
        
        
        """
        ...
    def getEntries(self) -> java.util.List[EOPEntry]:
        """
        Get a non-modifiable view of the EOP entries.
        
        Returns:
            non-modifiable view of the EOP entries
        
        
        """
        ...
    def getEopDataType(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'EopDataType': ...
    _getEquinoxNutationCorrection_1__T = typing.TypeVar('_getEquinoxNutationCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getEquinoxNutationCorrection(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Get the correction to the nutation parameters for equinox-based paradigm.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (AbsoluteDate): date at which the correction is desired
        
        Returns:
            nutation correction in longitude ΔΨ and in obliquity Δε (zero if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getEquinoxNutationCorrection(self, date: org.orekit.time.FieldAbsoluteDate[_getEquinoxNutationCorrection_1__T]) -> typing.MutableSequence[_getEquinoxNutationCorrection_1__T]:
        """
        Get the correction to the nutation parameters for equinox-based paradigm.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which the correction is desired
        
        Returns:
            nutation correction in longitude ΔΨ and in obliquity Δε (zero if date is outside covered range)
        
        
        """
        ...
    def getITRFVersion(self, date: org.orekit.time.AbsoluteDate) -> 'ITRFVersion':
        """
        Get the ITRF version.
        
        Parameters:
            date (AbsoluteDate): date at which the value is desired
        
        Returns:
            ITRF version of the EOP covering the specified date
        
        Since:
            9.2
        
        
        """
        ...
    def getInterpolationDegree(self) -> int:
        """
        Get interpolation degree.
        
        Returns:
            interpolation degree
        
        Since:
            12.0
        
        
        """
        ...
    _getLOD_1__T = typing.TypeVar('_getLOD_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getLOD(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (AbsoluteDate): date at which the value is desired
        
        Returns:
            LoD in seconds (0 if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getLOD(self, date: org.orekit.time.FieldAbsoluteDate[_getLOD_1__T]) -> _getLOD_1__T:
        """
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which the value is desired
        
        Returns:
            LoD in seconds (0 if date is outside covered range)
        
        Since:
            9.0
        
        
        """
        ...
    _getNonRotatinOriginNutationCorrection_1__T = typing.TypeVar('_getNonRotatinOriginNutationCorrection_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getNonRotatinOriginNutationCorrection(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Get the correction to the nutation parameters for Non-Rotating Origin paradigm.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (AbsoluteDate): date at which the correction is desired
        
        Returns:
            nutation correction in Celestial Intermediate Pole coordinates δX and δY (zero if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getNonRotatinOriginNutationCorrection(self, date: org.orekit.time.FieldAbsoluteDate[_getNonRotatinOriginNutationCorrection_1__T]) -> typing.MutableSequence[_getNonRotatinOriginNutationCorrection_1__T]:
        """
        Get the correction to the nutation parameters for Non-Rotating Origin paradigm.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which the correction is desired
        
        Returns:
            nutation correction in Celestial Intermediate Pole coordinates δX and δY (zero if date is outside covered range)
        
        
        """
        ...
    _getPoleCorrection_0__T = typing.TypeVar('_getPoleCorrection_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPoleCorrection(self, date: org.orekit.time.FieldAbsoluteDate[_getPoleCorrection_0__T]) -> 'FieldPoleCorrection'[_getPoleCorrection_0__T]:
        """
        Get the pole IERS Reference Pole correction.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which the correction is desired
        
        Returns:
            pole correction (NULL_CORRECTION if date is outside covered range)
        
        
        """
        ...
    @typing.overload
    def getPoleCorrection(self, date: org.orekit.time.AbsoluteDate) -> 'PoleCorrection':
        """
        Get the pole IERS Reference Pole correction.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (AbsoluteDate): date at which the correction is desired
        
        Returns:
            pole correction (NULL_CORRECTION if date is outside covered range)
        
        """
        ...
    def getStartDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date of the first available Earth Orientation Parameters.
        
        Returns:
            the start date of the available data
        
        
        """
        ...
    def getTimeScales(self) -> org.orekit.time.TimeScales:
        """
        Get the time scales used in computing EOP corrections.
        
        Returns:
            set of time scales.
        
        Since:
            10.1
        
        
        """
        ...
    _getUT1MinusUTC_1__T = typing.TypeVar('_getUT1MinusUTC_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getUT1MinusUTC(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the UT1-UTC value.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (AbsoluteDate): date at which the value is desired
        
        Returns:
            UT1-UTC in seconds (0 if date is outside covered range)
        
        """
        ...
    @typing.overload
    def getUT1MinusUTC(self, date: org.orekit.time.FieldAbsoluteDate[_getUT1MinusUTC_1__T]) -> _getUT1MinusUTC_1__T:
        """
        Get the UT1-UTC value.
        
        The data provided comes from the IERS files. It is smoothed data.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date at which the value is desired
        
        Returns:
            UT1-UTC in seconds (0 if date is outside covered range)
        
        Since:
            9.0
        
        
        """
        ...
    def isSimpleEop(self) -> bool:
        """
        Determine if this history uses simplified EOP corrections.
        
        Returns:
            true if tidal corrections are ignored, false otherwise.
        
        
        """
        ...

class EopDataType(java.lang.Enum['EopDataType']):
    """
    EOP data types.
    
    Since:
        13.1.1
    """
    UNKNOWN: typing.ClassVar['EopDataType'] = ...
    FINAL: typing.ClassVar['EopDataType'] = ...
    RAPID: typing.ClassVar['EopDataType'] = ...
    PREDICTED: typing.ClassVar['EopDataType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'EopDataType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['EopDataType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (EopDataType c : EopDataType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class EopHistoryLoader:
    """
    Interface for loading Earth Orientation Parameters history.
    
    Since:
        6.1
    """
    def fillHistory(self, converter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, history: java.util.SortedSet[EOPEntry]) -> None:
        """
        Load celestial body.
        
        Parameters:
            converter (NutationCorrectionConverter): converter to use for nutation corrections
            history (SortedSet<EOPEntry> history): history to fill up
        
        
        """
        ...
    class Parser:
        @staticmethod
        def newBulletinBParser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: typing.Union['ItrfVersionProvider', typing.Callable], timeScales: org.orekit.time.TimeScales) -> 'EopHistoryLoader.Parser': ...
        @staticmethod
        def newEopC04Parser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: typing.Union['ItrfVersionProvider', typing.Callable], timeScales: org.orekit.time.TimeScales) -> 'EopHistoryLoader.Parser': ...
        @staticmethod
        def newFinalsColumnsParser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: typing.Union['ItrfVersionProvider', typing.Callable], timeScales: org.orekit.time.TimeScales, boolean: bool) -> 'EopHistoryLoader.Parser': ...
        @staticmethod
        def newFinalsXmlParser(iERSConventions: org.orekit.utils.IERSConventions, itrfVersionProvider: typing.Union['ItrfVersionProvider', typing.Callable], timeScales: org.orekit.time.TimeScales) -> 'EopHistoryLoader.Parser': ...
        def parse(self, inputStream: java.io.InputStream, string: str) -> java.util.Collection[EOPEntry]: ...

_FieldCachedTransformProvider__T = typing.TypeVar('_FieldCachedTransformProvider__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCachedTransformProvider(typing.Generic[_FieldCachedTransformProvider__T]):
    """
    Thread-safe cached provider for frame transforms.
    
    This provider is based on a thread-safe Least Recently Used cache using date as it access key, hence saving computation time on transform building.
    
    This class is thread-safe.
    
    Since:
        13.0.3
    """
    def __init__(self, origin: 'Frame', destination: 'Frame', fullGenerator: typing.Union[java.util.function.Function[org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T], 'FieldTransform'[_FieldCachedTransformProvider__T]], typing.Callable[[org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T]], 'FieldTransform'[_FieldCachedTransformProvider__T]]], kinematicGenerator: typing.Union[java.util.function.Function[org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T], 'FieldKinematicTransform'[_FieldCachedTransformProvider__T]], typing.Callable[[org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T]], 'FieldKinematicTransform'[_FieldCachedTransformProvider__T]]], staticGenerator: typing.Union[java.util.function.Function[org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T], 'FieldStaticTransform'[_FieldCachedTransformProvider__T]], typing.Callable[[org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T]], 'FieldStaticTransform'[_FieldCachedTransformProvider__T]]], cacheSize: int):
        """
        Simple constructor.
        
        Parameters:
            origin (Frame): origin frame
            destination (Frame): destination frame
            fullGenerator (Function<FieldAbsoluteDate<FieldCachedTransformProvider>, FieldTransform<FieldCachedTransformProvider>>): generator for full transforms
            kinematicGenerator (Function<FieldAbsoluteDate<FieldCachedTransformProvider>, FieldKinematicTransform<FieldCachedTransformProvider>>): generator for kinematic transforms
            staticGenerator (Function<FieldAbsoluteDate<FieldCachedTransformProvider>, FieldStaticTransform<FieldCachedTransformProvider>>): generator for static transforms
            cacheSize (int): number of transforms kept in the date-based cache
        
        
        """
        ...
    def getCacheSize(self) -> int:
        """
        Get the nmber of transforms kept in the date-based cache.
        
        Returns:
            nmber of transforms kept in the date-based cache
        
        
        """
        ...
    def getDestination(self) -> 'Frame':
        """
        Get destination frame.
        
        Returns:
            destination frame
        
        
        """
        ...
    def getKinematicTransform(self, date: org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T]) -> 'FieldKinematicTransform'[_FieldCachedTransformProvider__T]:
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (FieldAbsoluteDate<FieldCachedTransformProvider> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    def getOrigin(self) -> 'Frame':
        """
        Get origin frame.
        
        Returns:
            origin frame
        
        
        """
        ...
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T]) -> 'FieldStaticTransform'[_FieldCachedTransformProvider__T]:
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (FieldAbsoluteDate<FieldCachedTransformProvider> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_FieldCachedTransformProvider__T]) -> 'FieldTransform'[_FieldCachedTransformProvider__T]:
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (FieldAbsoluteDate<FieldCachedTransformProvider> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...

_FieldPoleCorrection__T = typing.TypeVar('_FieldPoleCorrection__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldPoleCorrection(typing.Generic[_FieldPoleCorrection__T]):
    """
    Simple container class for pole correction parameters.
    
    This class is a simple container, it does not provide any processing method.
    
    Since:
        9.0
    """
    def __init__(self, xp: _FieldPoleCorrection__T, yp: _FieldPoleCorrection__T):
        """
        Simple constructor.
        
        Parameters:
            xp (FieldPoleCorrection): x :sub:`p` parameter (radians)
            yp (FieldPoleCorrection): y :sub:`p` parameter (radians)
        
        
        """
        ...
    def getXp(self) -> _FieldPoleCorrection__T:
        """
        Get the x :sub:`p` parameter.
        
        Returns:
            x :sub:`p` parameter
        
        
        """
        ...
    def getYp(self) -> _FieldPoleCorrection__T:
        """
        Get the y :sub:`p` parameter.
        
        Returns:
            y :sub:`p` parameter
        
        
        """
        ...

_FieldStaticTransform__T = typing.TypeVar('_FieldStaticTransform__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldStaticTransform(org.orekit.time.TimeStamped, typing.Generic[_FieldStaticTransform__T]):
    """
    A transform that only includes translation and rotation. It is static in the sense that no rates thereof are included.
    
    Since:
        12.0
    
    Also see:
        FieldTransform
    """
    _compose__T = typing.TypeVar('_compose__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def compose(date: org.orekit.time.FieldAbsoluteDate[_compose__T], first: 'FieldStaticTransform'[_compose__T], second: 'FieldStaticTransform'[_compose__T]) -> 'FieldStaticTransform'[_compose__T]:
        """
        Build a transform by combining two existing ones.
        
        Note that the dates of the two existing transformed are ignored, and the combined transform date is set to the date supplied in this constructor without any attempt to shift the raw transforms. This is a design choice allowing user full control of the combination.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date of the transform
            first (FieldStaticTransform<T> first): first transform applied
            second (FieldStaticTransform<T> second): second transform applied
        
        Returns:
            the newly created static transform that has the same effect as applying first, then second.
        
        Also see:
            of
        
        
        """
        ...
    _compositeRotation__T = typing.TypeVar('_compositeRotation__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def compositeRotation(first: 'FieldStaticTransform'[_compositeRotation__T], second: 'FieldStaticTransform'[_compositeRotation__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_compositeRotation__T]:
        """
        Compute a composite rotation.
        
        Parameters:
            first (FieldStaticTransform<T> first): first applied transform
            second (FieldStaticTransform<T> second): second applied transform
        
        Returns:
            rotation part of the composite transform
        
        
        """
        ...
    _compositeTranslation__T = typing.TypeVar('_compositeTranslation__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def compositeTranslation(first: 'FieldStaticTransform'[_compositeTranslation__T], second: 'FieldStaticTransform'[_compositeTranslation__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_compositeTranslation__T]:
        """
        Compute a composite translation.
        
        Parameters:
            first (FieldStaticTransform<T> first): first applied transform
            second (FieldStaticTransform<T> second): second applied transform
        
        Returns:
            translation part of the composite transform
        
        
        """
        ...
    def getFieldDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldStaticTransform__T]:
        """
        Get the Field date. This default implementation is there so that no API is broken by a minor release. It is overloaded by native inheritors and shall be removed in the next major release.
        
        Returns:
            Field date attached to the object
        
        Since:
            12.1
        
        
        """
        ...
    _getIdentity__T = typing.TypeVar('_getIdentity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getIdentity(field: org.hipparchus.Field[_getIdentity__T]) -> 'FieldStaticTransform'[_getIdentity__T]:
        """
        Get the identity static transform. Override methods for speed.
        
        Parameters:
            field (Field<T> field): field used by default
        
        Returns:
            identity transform.
        
        
        """
        ...
    def getInverse(self) -> 'FieldStaticTransform'[_FieldStaticTransform__T]:
        """
        Get the inverse transform of the instance.
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldStaticTransform__T]:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Returns:
            underlying elementary rotation
        
        
        """
        ...
    def getStaticInverse(self) -> 'FieldStaticTransform'[_FieldStaticTransform__T]:
        """
        Get the inverse transform of the instance in static form (without rates). This enables to create a purely static inverse, as inheritors such as FieldTransform may have a relatively computationally-heavy #getInverse() method.
        
        Returns:
            inverse static transform of the instance
        
        Since:
            12.1
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Returns:
            underlying elementary translation
        
        
        """
        ...
    _of_0__T = typing.TypeVar('_of_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_1__T = typing.TypeVar('_of_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_2__T = typing.TypeVar('_of_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_3__T = typing.TypeVar('_of_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def of(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_of_0__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_of_0__T]) -> 'FieldStaticTransform'[_of_0__T]:
        """
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            rotation (FieldRotation<T> rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
        
        Returns:
            the newly created static transform.
        
        Also see:
            of
        
        Create a new static transform from a translation and rotation.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            translation (FieldVector3D<T> translation): to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin in the old frame.
        
        Returns:
            the newly created static transform.
        
        Also see:
            of
        
        Create a new static transform from an FieldAbsoluteDate and a StaticTransform.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            staticTransform (StaticTransform): to apply
        
        Returns:
            the newly created static transform.
        
        Also see:
            of
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_of_1__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_of_1__T]) -> 'FieldStaticTransform'[_of_1__T]: ...
    @typing.overload
    @staticmethod
    def of(date: org.orekit.time.FieldAbsoluteDate[_of_2__T], translation: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_of_2__T], rotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_of_2__T]) -> 'FieldStaticTransform'[_of_2__T]:
        """
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            translation (FieldVector3D<T> translation): to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin in the old frame.
            rotation (FieldRotation<T> rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
        
        Returns:
            the newly created static transform.
        
        Also see:
            compose, of,
            of
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_of_3__T], staticTransform: 'StaticTransform') -> 'FieldStaticTransform'[_of_3__T]: ...
    @typing.overload
    def transformLine(self, fieldLine: org.hipparchus.geometry.euclidean.threed.FieldLine[_FieldStaticTransform__T]) -> org.hipparchus.geometry.euclidean.threed.FieldLine[_FieldStaticTransform__T]: ...
    @typing.overload
    def transformLine(self, line: org.hipparchus.geometry.euclidean.threed.Line) -> org.hipparchus.geometry.euclidean.threed.FieldLine[_FieldStaticTransform__T]: ...
    @typing.overload
    def transformPosition(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]: ...
    @typing.overload
    def transformPosition(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]: ...
    @typing.overload
    def transformVector(self, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]: ...
    @typing.overload
    def transformVector(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldStaticTransform__T]: ...

_FieldTransformGenerator__T = typing.TypeVar('_FieldTransformGenerator__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTransformGenerator(org.orekit.utils.TimeStampedGenerator['FieldTransform'[_FieldTransformGenerator__T]], typing.Generic[_FieldTransformGenerator__T]):
    """
    Generator to use field transforms in GenericTimeStampedCache.
    
    Since:
        9.0
    
    Also see:
        GenericTimeStampedCache
    """
    def __init__(self, field: org.hipparchus.Field[_FieldTransformGenerator__T], neighborsSize: int, provider: 'TransformProvider', step: float):
        """
        simple constructor.
        
        Parameters:
            field (Field<FieldTransformGenerator> field): field to which the elements belong
            neighborsSize (int): number of neighbors
            provider (TransformProvider): underlying provider
            step (double): step size
        
        
        """
        ...
    def generate(self, existingDate: org.orekit.time.AbsoluteDate, date: org.orekit.time.AbsoluteDate) -> java.util.List['FieldTransform'[_FieldTransformGenerator__T]]:
        """
        Generate a chronologically sorted list of entries to be cached.
        
        If existingDate is earlier than date, the range covered by generated entries must cover at least from existingDate (excluded) to date (included). If existingDate is later than date, the range covered by generated entries must cover at least from date (included) to existingDate (excluded).
        
        The generated entries may cover a range larger than the minimum specified above if the generator prefers to generate large chunks of data at once. It may generate again entries already generated by an earlier call (typically at existingDate), these extra entries will be silently ignored by the cache.
        
        Non-coverage of the minimum range may lead to a loss of data, as the gap will not be filled by the GenericTimeStampedCache in subsequent calls.
        
        The generated entries must be chronologically sorted.
        
        Specified by: generate in interface TimeStampedGenerator
        
        Parameters:
            existingDate (AbsoluteDate): date of the closest already existing entry (may be null)
            date (AbsoluteDate): date that must be covered by the range of the generated array
        
        Returns:
            chronologically sorted list of generated entries
        
        
        """
        ...

class Frame:
    """
    Tridimensional references frames class.
    
    Frame Presentation --------------------
    
    This class is the base class for all frames in OREKIT. The frames are linked together in a tree with some specific frame chosen as the root of the tree. Each frame is defined by Transform combining any number of translations and rotations from a reference frame which is its parent frame in the tree structure.
    
    When we say a Transform t is from frame :sub:`A` to frame :sub:`B`, we mean that if the coordinates of some absolute vector (say the direction of a distant star for example) has coordinates u :sub:`A` in frame :sub:`A` and u :sub:`B` in frame :sub:`B` , then u :sub:`B` =transformVector.
    
    The transforms may be constant or varying, depending on the implementation of the TransformProvider used to define the frame. For simple fixed transforms, using FixedTransformProvider is sufficient. For varying transforms (time-dependent or telemetry-based for example), it may be useful to define specific implementations of TransformProvider.
    """
    @typing.overload
    def __init__(self, frame: 'Frame', transform: 'Transform', string: str): ...
    @typing.overload
    def __init__(self, frame: 'Frame', transform: 'Transform', string: str, boolean: bool): ...
    @typing.overload
    def __init__(self, frame: 'Frame', transformProvider: 'TransformProvider', string: str): ...
    @typing.overload
    def __init__(self, frame: 'Frame', transformProvider: 'TransformProvider', string: str, boolean: bool): ...
    def getAncestor(self, n: int) -> 'Frame':
        """
        Get the n :sup:`th` ancestor of the frame.
        
        Parameters:
            n (int): index of the ancestor (0 is the instance, 1 is its parent, 2 is the parent of its parent...)
        
        Returns:
            n :sup:`th` ancestor of the frame (must be between 0 and the depth of the frame)
        
        Raises:
            IllegalArgumentException: if n is larger than the depth of the instance
        
        
        """
        ...
    def getDepth(self) -> int:
        """
        Get the depth of the frame.
        
        The depth of a frame is the number of parents frame between it and the frames tree root. It is 0 for the root frame, and the depth of a frame is the depth of its parent frame plus one.
        
        Returns:
            depth of the frame
        
        
        """
        ...
    def getFrozenFrame(self, reference: 'Frame', freezingDate: org.orekit.time.AbsoluteDate, frozenName: str) -> 'Frame':
        """
        Get a new version of the instance, frozen with respect to a reference frame.
        
        Freezing a frame consist in computing its position and orientation with respect to another frame at some freezing date and fixing them so they do not depend on time anymore. This means the frozen frame is fixed with respect to the reference frame.
        
        One typical use of this method is to compute an inertial launch reference frame by freezing a TopocentricFrame at launch date with respect to an inertial frame. Another use is to freeze an equinox-related celestial frame at a reference epoch date.
        
        Only the frame returned by this method is frozen, the instance by itself is not affected by calling this method and still moves freely.
        
        Parameters:
            reference (Frame): frame with respect to which the instance will be frozen
            freezingDate (AbsoluteDate): freezing date
            frozenName (String): name of the frozen frame
        
        Returns:
            a frozen version of the instance
        
        
        """
        ...
    _getKinematicTransformTo_0__T = typing.TypeVar('_getKinematicTransformTo_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getKinematicTransformTo(self, destination: 'Frame', date: org.orekit.time.FieldAbsoluteDate[_getKinematicTransformTo_0__T]) -> 'FieldKinematicTransform'[_getKinematicTransformTo_0__T]:
        """
        Get the kinematic portion of the transform from the instance to another frame. The returned transform is kinematic in the sense that it includes translations and rotations, with rates, but cannot transform an acceleration vector.
        
        This method is often more performant than getTransformTo when accelerations are not needed.
        
        Parameters:
            destination (Frame): destination frame to which we want to transform vectors
            date (FieldAbsoluteDate<T> date): the date (must be non-null, which is a more stringent condition * than in
                getKinematicTransformTo)
        
        Returns:
            kinematic transform from the instance to the destination frame
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def getKinematicTransformTo(self, destination: 'Frame', date: org.orekit.time.AbsoluteDate) -> 'KinematicTransform':
        """
        Get the kinematic portion of the transform from the instance to another frame. The returned transform is kinematic in the sense that it includes translations and rotations, with rates, but cannot transform an acceleration vector.
        
        This method is often more performant than getTransformTo when accelerations are not needed.
        
        Parameters:
            destination (Frame): destination frame to which we want to transform vectors
            date (AbsoluteDate): the date (can be null if it is sure than no date dependent frame is used)
        
        Returns:
            kinematic transform from the instance to the destination frame
        
        Since:
            12.1
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name.
        
        Returns:
            the name
        
        
        """
        ...
    def getParent(self) -> 'Frame':
        """
        Get the parent frame.
        
        Returns:
            parent frame
        
        
        """
        ...
    def getPeer(self) -> 'Frame':
        """
        Get the peer associated to this frame.
        
        Returns:
            peer associated with this frame, null if not peered at all
        
        Since:
            13.0.3
        
        
        """
        ...
    @staticmethod
    def getRoot() -> 'Frame':
        """
        Get the unique root frame.
        
        Returns:
            the unique instance of the root frame
        
        
        """
        ...
    _getStaticTransformTo_0__T = typing.TypeVar('_getStaticTransformTo_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransformTo(self, destination: 'Frame', date: org.orekit.time.FieldAbsoluteDate[_getStaticTransformTo_0__T]) -> FieldStaticTransform[_getStaticTransformTo_0__T]:
        """
        sense that it includes translations and rotations, but not rates.
        
        This method is often more performant than getTransformTo when rates are not needed.
        
        A first check is made on the FieldAbsoluteDate because "fielded" transforms have low-performance.
        
        The date field is checked with FieldElement.
        
        If true, the un-fielded version of the transform computation is used.
        
        Parameters:
            destination (Frame): destination frame to which we want to transform vectors
            date (FieldAbsoluteDate<T> date): the date (must be non-null, which is a more stringent condition than in
                getStaticTransformTo)
        
        Returns:
            static transform from the instance to the destination frame
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def getStaticTransformTo(self, destination: 'Frame', date: org.orekit.time.AbsoluteDate) -> 'StaticTransform':
        """
        sense that it includes translations and rotations, but not rates.
        
        This method is often more performant than getTransformTo when rates are not needed.
        
        Parameters:
            destination (Frame): destination frame to which we want to transform vectors
            date (AbsoluteDate): the date (can be null if it is sure than no date dependent frame is used)
        
        Returns:
            static transform from the instance to the destination frame
        
        Since:
            11.2
        
        """
        ...
    def getTransformProvider(self) -> 'TransformProvider':
        """
        Get the provider for transform from parent frame to instance.
        
        Returns:
            provider for transform from parent frame to instance
        
        
        """
        ...
    _getTransformTo_0__T = typing.TypeVar('_getTransformTo_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransformTo(self, destination: 'Frame', date: org.orekit.time.FieldAbsoluteDate[_getTransformTo_0__T]) -> 'FieldTransform'[_getTransformTo_0__T]:
        """
        Get the transform from the instance to another frame.
        
        Parameters:
            destination (Frame): destination frame to which we want to transform vectors
            date (FieldAbsoluteDate<T> date): the date (must be non-null, which is a more stringent condition than in
                getTransformTo)
        
        Returns:
            transform from the instance to the destination frame
        
        
        """
        ...
    @typing.overload
    def getTransformTo(self, destination: 'Frame', date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the transform from the instance to another frame.
        
        Parameters:
            destination (Frame): destination frame to which we want to transform vectors
            date (AbsoluteDate): the date (can be null if it is certain that no date dependent frame is used)
        
        Returns:
            transform from the instance to the destination frame
        
        """
        ...
    def isChildOf(self, potentialAncestor: 'Frame') -> bool:
        """
        Determine if a Frame is a child of another one.
        
        Parameters:
            potentialAncestor (Frame): supposed ancestor frame
        
        Returns:
            true if the potentialAncestor belongs to the path from instance to the root frame, excluding itself
        
        
        """
        ...
    def isPseudoInertial(self) -> bool:
        """
        Check if the frame is pseudo-inertial.
        
        Pseudo-inertial frames are frames that do have a linear motion and either do not rotate or rotate at a very low rate resulting in neglectible inertial forces. This means they are suitable for orbit definition and propagation using Newtonian mechanics. Frames that are not pseudo-inertial are not suitable for orbit definition and propagation.
        
        Returns:
            true if frame is pseudo-inertial
        
        
        """
        ...
    def setPeerCaching(self, peer: 'Frame', cacheSize: int) -> None:
        """
        Associate this frame to a peer, caching transforms.
        
        The cache is a LRU cache (Least Recently Used), so entries remain in the cache if they are used frequently, and only older entries that have not been accessed for a while will be expunged.
        
        Setting up a peer is mainly intended when there is a real need to speed up conversions in a context when the same frames (origin and destination) are used over and over again at the same date. One typical use case is to peer topocentric frames to the inertial frame when dealing with ground links as the conversion between a ground station (topocentric frame) and inertial frame will be needed for relative position computation, tropospheric effect computation, ionospheric effect computation, on all signal types and for all observables (code, phase, Doppler, signal strength…).
        
        Setting up peer caching does not change the result of the various getTransformTo methods, it just speeds up the computation in the case the same date is used over and over again between the instance and its peer. The computation is just fully performed the first time a date is used and the result is put in the cache before being returned. If a later call uses the same date again and there is a cache hit, then it will return the cached transform without any computation.
        
        The peer frame doesn't need to be close to the initial frame in the hierarchical frames tree, and there is no transitivity involved: peering is a point-to-point relationship. It is for example possible to peer a topocentric frame to the EME2000 frame despite there are several intermediate frames involved when computing the transform (topocentric → ITRF → TIRF → CIRF → GCRF → EME2000), the link will be a direct one and what will be cached at each date is the transform resulting from the combination of all transforms between the intermediate frames at this date. We could have at the same time the intermediate ITRF frame peered to another frame not belonging to this list, it won't have any influence, peering is really point-to-point.
        
        Peering is unidirectional, i.e. if frameA is peered to frameB, it means the transforms that will be cached are the transforms from frameA (the instance when this method or the getTransformTo method are called) to frameB (the argument when this method or the getTransformTo method are called). It is therefore possible to have frameA peered to frameB and frameB peered to another frameC or no frames at all. This allows several frames to be peered to a shared pivot one (typically Earth frame and many topocentric frames all peered to one inertial frame). The side effect of this choice is that peering improves efficiency only in one direction, i.e. if frameA is peered to frameB, then computing the transform from frameB to frameA should be done by computing transform from frameA to frameB and then inverting rather than directly computing the transform from frameB to frameA. It is of course possible to peer frameA to frameB and also frameB to frameA, but this prevents using a shared pivot frame.
        
        Peering is generally set up at the start of the application and kept unchanged throughout its operation, but nothing prevents to change it on the fly, even from different threads. Peering is thread-safe, but shared among all threads (there are internal locks to ensure thread safety), so peering is often set up on a main thread and then used on several other threads, like for example in parallel propagation contexts.
        
        Peering is optional; when a frame is first created, it is not peered to any other frames.
        
        When peering has been set up, caching is enabled for all transforms computed from the instance to its peer, i.e. getTransformTo, getTransformTo, getKinematicTransformTo, getKinematicTransformTo, getStaticTransformTo, getStaticTransformTo. It is not possible to set different cached for different transforms types.
        
        If a peer was already associated to this frame, it will be overridden. This can be used to clear peering by setting the peer to null and avoid keeping a reference to a frame that is not used anymore, hence allowing it to be garbage collected.
        
        Parameters:
            peer (Frame): peer frame (null to clear the cache)
            cacheSize (int): number of transforms kept in the date-based cache
        
        Since:
            13.0.3
        
        
        """
        ...
    def toString(self) -> str:
        """
        New definition of the java.util toString() method.
        
        Overrides: Object in class Object
        
        Returns:
            the name
        
        
        """
        ...

class Frames:
    def buildUncachedITRF(self, uT1Scale: org.orekit.time.UT1Scale) -> Frame: ...
    def getCIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getEME2000(self) -> 'FactoryManagedFrame': ...
    def getEOPHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory: ...
    def getEcliptic(self, iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    def getFrame(self, predefined: 'Predefined') -> Frame: ...
    def getGCRF(self) -> Frame: ...
    @typing.overload
    def getGTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getGTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getICRF(self) -> Frame: ...
    @typing.overload
    def getITRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getITRF(self, iTRFVersion: 'ITRFVersion', iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    def getITRFEquinox(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    def getPZ9011(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getTEME(self) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getVeis1950(self) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def of(timeScales: org.orekit.time.TimeScales, supplier: typing.Union[java.util.function.Supplier[Frame], typing.Callable[[], Frame]]) -> 'Frames': ...
    @typing.overload
    @staticmethod
    def of(timeScales: org.orekit.time.TimeScales, celestialBodies: org.orekit.bodies.CelestialBodies) -> 'Frames': ...

class FramesFactory:
    RAPID_DATA_PREDICTION_COLUMNS_1980_FILENAME: typing.ClassVar[str] = ...
    XML_1980_FILENAME: typing.ClassVar[str] = ...
    EOPC04_1980_FILENAME: typing.ClassVar[str] = ...
    BULLETINB_1980_FILENAME: typing.ClassVar[str] = ...
    RAPID_DATA_PREDICTION_COLUMNS_2000_FILENAME: typing.ClassVar[str] = ...
    XML_2000_FILENAME: typing.ClassVar[str] = ...
    EOPC04_2000_FILENAME: typing.ClassVar[str] = ...
    BULLETINB_2000_FILENAME: typing.ClassVar[str] = ...
    BULLETINA_FILENAME: typing.ClassVar[str] = ...
    CSV_FILENAME: typing.ClassVar[str] = ...
    @staticmethod
    def addDefaultEOP1980HistoryLoaders(string: str, string2: str, string3: str, string4: str, string5: str, string6: str) -> None: ...
    @staticmethod
    def addDefaultEOP2000HistoryLoaders(string: str, string2: str, string3: str, string4: str, string5: str, string6: str) -> None: ...
    @staticmethod
    def addEOPHistoryLoader(iERSConventions: org.orekit.utils.IERSConventions, eopHistoryLoader: typing.Union[EopHistoryLoader, typing.Callable]) -> None: ...
    @staticmethod
    def buildUncachedITRF(eOPHistory: EOPHistory, uTCScale: org.orekit.time.UTCScale) -> Frame: ...
    @staticmethod
    def clearEOPHistoryLoaders() -> None: ...
    @staticmethod
    def findEOP(frame: Frame) -> EOPHistory: ...
    @staticmethod
    def getCIRF(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getEME2000() -> 'FactoryManagedFrame': ...
    @staticmethod
    def getEOPHistory(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory: ...
    @staticmethod
    def getEcliptic(iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    @staticmethod
    def getFrame(predefined: 'Predefined') -> Frame: ...
    @staticmethod
    def getFrames() -> 'LazyLoadedFrames': ...
    @staticmethod
    def getGCRF() -> Frame: ...
    @typing.overload
    @staticmethod
    def getGTOD(boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getGTOD(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getICRF() -> Frame: ...
    @typing.overload
    @staticmethod
    def getITRF(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getITRF(iTRFVersion: 'ITRFVersion', iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    @staticmethod
    def getITRFEquinox(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getMOD(boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getMOD(iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    _getNonInterpolatingTransform_0__T = typing.TypeVar('_getNonInterpolatingTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getNonInterpolatingTransform(frame: Frame, frame2: Frame, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getNonInterpolatingTransform_0__T]) -> 'FieldTransform'[_getNonInterpolatingTransform_0__T]: ...
    @typing.overload
    @staticmethod
    def getNonInterpolatingTransform(frame: Frame, frame2: Frame, absoluteDate: org.orekit.time.AbsoluteDate) -> 'Transform': ...
    @staticmethod
    def getPZ9011(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getTEME() -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTIRF(iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTIRF(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTOD(boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    @staticmethod
    def getTOD(iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @staticmethod
    def getVeis1950() -> 'FactoryManagedFrame': ...
    @staticmethod
    def setEOPContinuityThreshold(double: float) -> None: ...

class ItrfVersionProvider:
    """
    Interface for retrieving the ITRF version for a given set of EOP data.
    
    Since:
        10.1
    
    Also see:
        ITRFVersionLoader
    """
    def getConfiguration(self, name: str, mjd: int) -> 'ITRFVersionLoader.ITRFVersionConfiguration':
        """
        Get the ITRF version configuration defined by a given file at specified date.
        
        Parameters:
            name (String): EOP file name
            mjd (int): date of the EOP in modified Julian day
        
        Returns:
            configuration valid around specified date in the file
        
        
        """
        ...

class LOF:
    """
    Interface for local orbital frame.
    """
    def getName(self) -> str:
        """
        Get name of the local orbital frame.
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    def isQuasiInertial(self) -> bool:
        """
        Get flag that indicates if current local orbital frame shall be treated as pseudo-inertial.
        
        Returns:
            flag that indicates if current local orbital frame shall be treated as pseudo-inertial
        
        
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], date: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], pv: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        Since:
            9.0
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        
        """
        ...
    _rotationFromLOF_0__T = typing.TypeVar('_rotationFromLOF_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromLOF(self, field: org.hipparchus.Field[_rotationFromLOF_0__T], fromLOF: 'LOF', date: org.orekit.time.FieldAbsoluteDate[_rotationFromLOF_0__T], pv: org.orekit.utils.FieldPVCoordinates[_rotationFromLOF_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromLOF_0__T]:
        """
        Get the rotation from input LOF to the instance.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromLOF method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            fromLOF (LOF): input local orbital frame
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input local orbital frame to the instance
        
        Since:
            11.3
        
        """
        ...
    @typing.overload
    def rotationFromLOF(self, fromLOF: 'LOF', date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from input LOF to the instance.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromLOF method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            fromLOF (LOF): input local orbital frame
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input local orbital frame to the instance
        
        Since:
            11.3
        
        
        """
        ...
    _rotationFromLOFInToLOFOut_0__T = typing.TypeVar('_rotationFromLOFInToLOFOut_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def rotationFromLOFInToLOFOut(field: org.hipparchus.Field[_rotationFromLOFInToLOFOut_0__T], in_: 'LOF', out: 'LOF', date: org.orekit.time.FieldAbsoluteDate[_rotationFromLOFInToLOFOut_0__T], pv: org.orekit.utils.FieldPVCoordinates[_rotationFromLOFInToLOFOut_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromLOFInToLOFOut_0__T]:
        """
        Get the rotation from input to output LOF.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromLOFInToLOFOut method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            in (LOF): input commonly used local orbital frame
            out (LOF): output commonly used local orbital frame
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input to output local orbital frame
        
        Since:
            11.3
        
        """
        ...
    @typing.overload
    @staticmethod
    def rotationFromLOFInToLOFOut(in_: 'LOF', out: 'LOF', date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from input to output LOF.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromLOFInToLOFOut method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            in (LOF): input commonly used local orbital frame
            out (LOF): output commonly used local orbital frame
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input to output local orbital frame.
        
        Since:
            11.3
        
        
        """
        ...
    _transformFromInertial_0__T = typing.TypeVar('_transformFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformFromInertial(self, date: org.orekit.time.FieldAbsoluteDate[_transformFromInertial_0__T], pv: org.orekit.utils.FieldPVCoordinates[_transformFromInertial_0__T]) -> 'FieldTransform'[_transformFromInertial_0__T]:
        """
        Get the transform from an inertial frame defining position-velocity and the local orbital frame.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            transform from the frame where position-velocity are defined to local orbital frame
        
        Since:
            9.0
        
        """
        ...
    @typing.overload
    def transformFromInertial(self, date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> 'Transform':
        """
        Get the transform from an inertial frame defining position-velocity and the local orbital frame.
        
        Parameters:
            date (AbsoluteDate): current date
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            transform from the frame where position-velocity are defined to local orbital frame
        
        
        """
        ...
    _transformFromLOF_0__T = typing.TypeVar('_transformFromLOF_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformFromLOF(self, fromLOF: 'LOF', date: org.orekit.time.FieldAbsoluteDate[_transformFromLOF_0__T], pv: org.orekit.utils.FieldPVCoordinates[_transformFromLOF_0__T]) -> 'FieldTransform'[_transformFromLOF_0__T]:
        """
        Get the rotation from input LOF to the instance.
        
        Parameters:
            fromLOF (LOF): input local orbital frame
            date (FieldAbsoluteDate<T> date): date of the transform
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input local orbital frame to the instance
        
        Since:
            11.3
        
        """
        ...
    @typing.overload
    def transformFromLOF(self, fromLOF: 'LOF', date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> 'Transform':
        """
        Get the rotation from input LOF to the instance.
        
        Parameters:
            fromLOF (LOF): input local orbital frame
            date (AbsoluteDate): date of the transform
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input local orbital frame to the instance
        
        Since:
            11.3
        
        
        """
        ...
    _transformFromLOFInToLOFOut_0__T = typing.TypeVar('_transformFromLOFInToLOFOut_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def transformFromLOFInToLOFOut(in_: 'LOF', out: 'LOF', date: org.orekit.time.FieldAbsoluteDate[_transformFromLOFInToLOFOut_0__T], pv: org.orekit.utils.FieldPVCoordinates[_transformFromLOFInToLOFOut_0__T]) -> 'FieldTransform'[_transformFromLOFInToLOFOut_0__T]:
        """
        Get the transform from input to output LOF.
        
        Parameters:
            in (LOF): input commonly used local orbital frame
            out (LOF): output commonly used local orbital frame
            date (FieldAbsoluteDate<T> date): date of the transform
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input to output local orbital frame.
        
        Since:
            11.3
        
        """
        ...
    @typing.overload
    @staticmethod
    def transformFromLOFInToLOFOut(in_: 'LOF', out: 'LOF', date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> 'Transform':
        """
        Get the transform from input to output LOF.
        
        Parameters:
            in (LOF): input commonly used local orbital frame
            out (LOF): output commonly used local orbital frame
            date (AbsoluteDate): date of the transform
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input to output local orbital frame
        
        Since:
            11.3
        
        
        """
        ...

class LazyLoadedEop:
    """
    Loads Earth Orientation Parameters (EOP) from a configured set of EopHistoryLoaders on demand. Methods are synchronized so it is safe for access from multiple threads.
    
    Since:
        10.1
    
    Also see:
        LazyLoadedFrames, FramesFactory
    """
    def __init__(self, dataProvidersManager: org.orekit.data.DataProvidersManager):
        """
        Create a new instance for loading EOP data from multiple EopHistoryLoaders.
        
        Parameters:
            dataProvidersManager (DataProvidersManager): provides access to the needed EOP data files.
        
        
        """
        ...
    def addDefaultEOP1980HistoryLoaders(self, rapidDataColumnsSupportedNames: str, xmlSupportedNames: str, eopC04SupportedNames: str, bulletinBSupportedNames: str, bulletinASupportedNames: str, csvSupportedNames: str, utcSupplier: typing.Union[java.util.function.Supplier[org.orekit.time.TimeScale], typing.Callable[[], org.orekit.time.TimeScale]]) -> None:
        """
        Add the default loaders EOP history (IAU 1980 precession/nutation).
        
        The default loaders look for IERS EOP C04 and bulletins B files. They correspond to IERS_1996 conventions.
        
        Parameters:
            rapidDataColumnsSupportedNames (String): regular expression for supported rapid data columns EOP files names (may be null if the default IERS file names are
                used)
            xmlSupportedNames (String): regular expression for supported XML EOP files names (may be null if the default IERS file names are used)
            eopC04SupportedNames (String): regular expression for supported EOP C04 files names (may be null if the default IERS file names are used)
            bulletinBSupportedNames (String): regular expression for supported bulletin B files names (may be null if the default IERS file names are used)
            bulletinASupportedNames (String): regular expression for supported bulletin A files names (may be null if the default IERS file names are used)
            csvSupportedNames (String): regular expression for supported csv files names (may be null if the default IERS file names are used)
            utcSupplier (Supplier<TimeScale> utcSupplier): UTC time scale supplier. Value is not accessed until attempting to load EOP.
        
        Since:
            12.0
        
        Also see:
            eop,
            addEOPHistoryLoader,
            clearEOPHistoryLoaders,
            addDefaultEOP2000HistoryLoaders
        
        
        """
        ...
    def addDefaultEOP2000HistoryLoaders(self, rapidDataColumnsSupportedNames: str, xmlSupportedNames: str, eopC04SupportedNames: str, bulletinBSupportedNames: str, bulletinASupportedNames: str, csvSupportedNames: str, utcSupplier: typing.Union[java.util.function.Supplier[org.orekit.time.TimeScale], typing.Callable[[], org.orekit.time.TimeScale]]) -> None:
        """
        Add the default loaders for EOP history (IAU 2000/2006 precession/nutation).
        
        The default loaders look for IERS EOP C04 and bulletins B files. They correspond to both IERS_2003 and IERS_2010 conventions.
        
        Parameters:
            rapidDataColumnsSupportedNames (String): regular expression for supported rapid data columns EOP files names (may be null if the default IERS file names are
                used)
            xmlSupportedNames (String): regular expression for supported XML EOP files names (may be null if the default IERS file names are used)
            eopC04SupportedNames (String): regular expression for supported EOP C04 files names (may be null if the default IERS file names are used)
            bulletinBSupportedNames (String): regular expression for supported bulletin B files names (may be null if the default IERS file names are used)
            bulletinASupportedNames (String): regular expression for supported bulletin A files names (may be null if the default IERS file names are used)
            csvSupportedNames (String): regular expression for supported csv files names (may be null if the default IERS file names are used)
            utcSupplier (Supplier<TimeScale> utcSupplier): UTC time scale supplier. Value is not accessed until attempting to load EOP.
        
        Since:
            12.0
        
        Also see:
            eop,
            addEOPHistoryLoader,
            clearEOPHistoryLoaders,
            addDefaultEOP1980HistoryLoaders
        
        
        """
        ...
    def addEOPHistoryLoader(self, conventions: org.orekit.utils.IERSConventions, loader: typing.Union[EopHistoryLoader, typing.Callable]) -> None:
        """
        Add a loader for Earth Orientation Parameters history.
        
        Parameters:
            conventions (IERSConventions): IERS conventions to which EOP history applies
            loader (EopHistoryLoader): custom loader to add for the EOP history
        
        Also see:
            addDefaultEOP1980HistoryLoaders,
            clearEOPHistoryLoaders
        
        
        """
        ...
    def clearEOPHistoryLoaders(self) -> None:
        """
        Clear loaders for Earth Orientation Parameters history.
        
        Also see:
            addEOPHistoryLoader,
            addDefaultEOP1980HistoryLoaders
        
        
        """
        ...
    def getDataProvidersManager(self) -> org.orekit.data.DataProvidersManager:
        """
        Get the data providers manager for this instance.
        
        Returns:
            the provider of EOP data files.
        
        
        """
        ...
    def getEOPHistory(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool, timeScales: org.orekit.time.TimeScales) -> EOPHistory:
        """
        Get Earth Orientation Parameters history.
        
        If no EopHistoryLoader has been added by calling addEOPHistoryLoader or if clearEOPHistoryLoaders has been called afterwards, the addDefaultEOP1980HistoryLoaders and addDefaultEOP2000HistoryLoaders methods will be called automatically with supported file names parameters all set to null, in order to get the default loaders configuration.
        
        Parameters:
            conventions (IERSConventions): conventions for which EOP history is requested
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
            timeScales (TimeScales): to use when loading EOP and computing corrections.
        
        Returns:
            Earth Orientation Parameters history
        
        
        """
        ...
    def setEOPContinuityThreshold(self, threshold: float) -> None:
        """
        Set the threshold to check EOP continuity.
        
        The default threshold (used if this method is never called) is 5 Julian days. If after loading EOP entries some holes between entries exceed this threshold, an exception will be triggered.
        
        One case when calling this method is really useful is for applications that use a single Bulletin A, as these bulletins have a roughly one month wide hole for the first bulletin of each month, which contains older final data in addition to the rapid data and the predicted data.
        
        Parameters:
            threshold (double): threshold to use for checking EOP continuity (in seconds)
        
        
        """
        ...
    def setInterpolationDegree(self, interpolationDegree: int) -> None:
        """
        Set the degree for interpolation degree.
        
        The default threshold (used if this method is never called) is DEFAULT_INTERPOLATION_DEGREE.
        
        Parameters:
            interpolationDegree (int): interpolation degree, must be of the form 4k-1
        
        Since:
            12.0
        
        
        """
        ...

class OrphanFrame:
    """
    Prototype frame that can be built from leaf to roots and later attached to a tree.
    
    Regular Frame instances can be built only from a parent frame, i.e. the frames tree can be built only from root to leafs. In some cases, it may desirable to build a subset tree and attach it to the main tree after build time, which means the tree is built from leafs to root. This class allows building this subtree.
    
    During the build process, the Frame associated with each OrphanFrame is not available. It becomes available only once the OrphanFrame has been attached to the main tree, and at this time it can be used to compute Transform.
    
    Since:
        6.0
    """
    def __init__(self, name: str):
        """
        Simple constructor.
        
        Parameters:
            name (String): name of the frame
        
        
        """
        ...
    @typing.overload
    def addChild(self, orphanFrame: 'OrphanFrame', transform: 'Transform', boolean: bool) -> None:
        """
        Add a child.
        
        If a child is added after the instance has been attached, the child and all its tree will be attached immediately too.
        
        Parameters:
            child (OrphanFrame): child to add
            transform (Transform): transform from instance to child
            isPseudoInertial (boolean): true if child is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
        Add a child.
        
        If a child is added after the instance has been attached, the child and all its tree will be attached immediately too.
        
        Parameters:
            child (OrphanFrame): child to add
            transformProvider (TransformProvider): provider for transform from instance to child
            isPseudoInertial (boolean): true if child is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
        
        """
        ...
    @typing.overload
    def addChild(self, orphanFrame: 'OrphanFrame', transformProvider: 'TransformProvider', boolean: bool) -> None: ...
    @typing.overload
    def attachTo(self, frame: Frame, transform: 'Transform', boolean: bool) -> None:
        """
        Parameters:
            parent (Frame): parent frame to attach to
            transform (Transform): transform from parent frame to instance
            isPseudoInertial (boolean): true if frame is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
        Attach the instance (and all its children down to leafs) to the main tree.
        
        Parameters:
            parent (Frame): parent frame to attach to
            transformProvider (TransformProvider): provider for transform from parent frame to instance
            isPseudoInertial (boolean): true if frame is considered pseudo-inertial (i.e. suitable for propagating orbit)
        
        
        """
        ...
    @typing.overload
    def attachTo(self, frame: Frame, transformProvider: 'TransformProvider', boolean: bool) -> None: ...
    def getChildren(self) -> java.util.List['OrphanFrame']:
        """
        Get all children of the instance.
        
        Returns:
            unmodifiable list of children
        
        
        """
        ...
    def getFrame(self) -> Frame:
        """
        Get the associated Frame.
        
        Returns:
            associated frame
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class PoleCorrection(java.io.Serializable):
    """
    Simple container class for pole correction parameters.
    
    This class is a simple container, it does not provide any processing method.
    
    Also see:
        serialized
    """
    NULL_CORRECTION: typing.ClassVar['PoleCorrection'] = ...
    """
    Null correction (xp = 0, yp = 0).
    """
    def __init__(self, xp: float, yp: float):
        """
        Simple constructor.
        
        Parameters:
            xp (double): x :sub:`p` parameter (radians)
            yp (double): y :sub:`p` parameter (radians)
        
        
        """
        ...
    def getXp(self) -> float:
        """
        Get the x :sub:`p` parameter.
        
        Returns:
            x :sub:`p` parameter
        
        
        """
        ...
    def getYp(self) -> float:
        """
        Get the y :sub:`p` parameter.
        
        Returns:
            y :sub:`p` parameter
        
        
        """
        ...

class Predefined(java.lang.Enum['Predefined']):
    """
    Predefined frames provided by Frames.
    """
    GCRF: typing.ClassVar['Predefined'] = ...
    ICRF: typing.ClassVar['Predefined'] = ...
    ECLIPTIC_CONVENTIONS_1996: typing.ClassVar['Predefined'] = ...
    ECLIPTIC_CONVENTIONS_2003: typing.ClassVar['Predefined'] = ...
    ECLIPTIC_CONVENTIONS_2010: typing.ClassVar['Predefined'] = ...
    EME2000: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_CIO_CONV_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    ITRF_EQUINOX_CONV_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TIRF_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    CIRF_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    VEIS_1950: typing.ClassVar['Predefined'] = ...
    GTOD_WITHOUT_EOP_CORRECTIONS: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    GTOD_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_WITHOUT_EOP_CORRECTIONS: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2010_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2010_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2003_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_2003_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_1996_ACCURATE_EOP: typing.ClassVar['Predefined'] = ...
    TOD_CONVENTIONS_1996_SIMPLE_EOP: typing.ClassVar['Predefined'] = ...
    MOD_WITHOUT_EOP_CORRECTIONS: typing.ClassVar['Predefined'] = ...
    MOD_CONVENTIONS_2010: typing.ClassVar['Predefined'] = ...
    MOD_CONVENTIONS_2003: typing.ClassVar['Predefined'] = ...
    MOD_CONVENTIONS_1996: typing.ClassVar['Predefined'] = ...
    TEME: typing.ClassVar['Predefined'] = ...
    PZ90_11: typing.ClassVar['Predefined'] = ...
    def getName(self) -> str:
        """
        Get the name of the frame.
        
        Returns:
            name of the frame
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'Predefined':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['Predefined']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (Predefined c : Predefined.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class SingleParameterFitter(java.io.Serializable):
    """
    Fitter for one Earth Orientation Parameter.
    
    Since:
        12.0
    
    Also see:
        PredictedEOPHistory, EOPFitter,
        SecularAndHarmonic, serialized
    """
    SUN_PULSATION: typing.ClassVar[float] = ...
    """
    Sun pulsation, one year period.
    
    Also see:
        constant
    
    
    """
    MOON_DRACONIC_PULSATION: typing.ClassVar[float] = ...
    """
    Moon pulsation (one Moon draconic period).
    
    Also see:
        constant
    
    
    """
    def __init__(self, timeConstant: float, convergence: float, degree: int, *pulsations: float):
        """
        Simple constructor.
        
        Parameters:
            timeConstant (double): time constant \(\tau\) of the exponential decay weight, point weight is \(e^{\frac{t-t_0}{\tau}}\), i.e. points far in
                the past before \(t_0\) have smaller weights
            convergence (double): convergence on fitted parameter
            degree (int): degree of the polynomial model
            pulsations (double...): pulsations of harmonic part (rad/s)
        
        Since:
            12.0.1
        
        Also see:
            createDefaultDut1FitterShortTermPrediction,
            createDefaultDut1FitterLongTermPrediction,
            createDefaultPoleFitterShortTermPrediction,
            createDefaultPoleFitterLongTermPrediction,
            createDefaultNutationFitterShortTermPrediction,
            createDefaultNutationFitterLongTermPrediction,
            SecularAndHarmonic
        
        
        """
        ...
    @staticmethod
    def createDefaultDut1FitterLongTermPrediction() -> 'SingleParameterFitter':
        """
        Create fitter with default parameters adapted for fitting orientation parameters dUT1 and LOD for long term prediction.
        
        The main difference between these settings and createDefaultDut1FitterShortTermPrediction is the much larger \(\tau\). This means weight is spread throughout history, hence forcing the fitted prediction model to be remain very stable on the long term. On the other hand, this implies that the model will start with already a much larger error just after raw history end. These settings are intended when prediction is used for 5 days after raw EOP end or more.
        
          - time constant \(\tau\) of the exponential decay set to 60 JULIAN_DAY
          - convergence set to 10⁻¹² s
          - polynomial part set to degree 3
          - one harmonic term at SUN_PULSATION}
          - one harmonic term at 2 times SUN_PULSATION}
          - one harmonic term at 3 times SUN_PULSATION}
          - one harmonic term at MOON_DRACONIC_PULSATION}
          - one harmonic term at 2 times MOON_DRACONIC_PULSATION}
          - one harmonic term at 3 times MOON_DRACONIC_PULSATION}
        
        
        Returns:
            fitter with default configuration for orientation parameters dUT1 and LOD
        
        Also see:
            createDefaultDut1FitterShortTermPrediction
        
        
        """
        ...
    @staticmethod
    def createDefaultDut1FitterShortTermPrediction() -> 'SingleParameterFitter':
        """
        Create fitter with default parameters adapted for fitting orientation parameters dUT1 and LOD for short term prediction.
        
        The main difference between these settings and createDefaultDut1FitterLongTermPrediction is the much smaller \(\tau\). This means more weight is set to the points at the end of the history, hence forcing the fitted prediction model to be closer to these points, hence the prediction error to be smaller just after raw history end. On the other hand, this implies that the model will diverge on long term. These settings are intended when prediction is used for at most 5 days after raw EOP end.
        
          - time constant \(\tau\) of the exponential decay set to 6 JULIAN_DAY
          - convergence set to 10⁻¹² s
          - polynomial part set to degree 3
          - one harmonic term at SUN_PULSATION}
          - one harmonic term at 2 times SUN_PULSATION}
          - one harmonic term at 3 times SUN_PULSATION}
          - one harmonic term at MOON_DRACONIC_PULSATION}
          - one harmonic term at 2 times MOON_DRACONIC_PULSATION}
          - one harmonic term at 3 times MOON_DRACONIC_PULSATION}
        
        
        Returns:
            fitter with default configuration for orientation parameters dUT1 and LOD
        
        Also see:
            createDefaultDut1FitterShortTermPrediction
        
        
        """
        ...
    @staticmethod
    def createDefaultNutationFitterLongTermPrediction() -> 'SingleParameterFitter':
        """
        Create fitter with default parameters adapted for fitting nutation parameters dx and dy for long term prediction.
        
        The main difference between these settings and createDefaultNutationFitterShortTermPrediction is the much larger \(\tau\). This means weight is spread throughout history, hence forcing the fitted prediction model to be remain very stable on the long term. On the other hand, this implies that the model will start with already a much larger error just after raw history end. These settings are intended when prediction is used for 5 days after raw EOP end or more.
        
          - time constant \(\tau\) of the exponential decay set to 60 JULIAN_DAY
          - convergence set to 10⁻¹² s
          - polynomial part set to degree 3
          - one harmonic term at SUN_PULSATION}
          - one harmonic term at 2 times SUN_PULSATION}
          - one harmonic term at 3 times SUN_PULSATION}
          - one harmonic term at MOON_DRACONIC_PULSATION}
          - one harmonic term at 2 times MOON_DRACONIC_PULSATION}
          - one harmonic term at 3 times MOON_DRACONIC_PULSATION}
        
        
        Returns:
            fitter with default configuration for pole nutation parameters dx and dy
        
        
        """
        ...
    @staticmethod
    def createDefaultNutationFitterShortTermPrediction() -> 'SingleParameterFitter':
        """
        Create fitter with default parameters adapted for fitting nutation parameters dx and dy for long term prediction.
        
        The main difference between these settings and createDefaultNutationFitterLongTermPrediction is the much smaller \(\tau\). This means more weight is set to the points at the end of the history, hence forcing the fitted prediction model to be closer to these points, hence the prediction error to be smaller just after raw history end. On the other hand, this implies that the model will diverge on long term. These settings are intended when prediction is used for at most 5 days after raw EOP end.
        
          - time constant \(\tau\) of the exponential decay set to 12 JULIAN_DAY
          - convergence set to 10⁻¹² s
          - polynomial part set to degree 3
          - one harmonic term at SUN_PULSATION}
          - one harmonic term at 2 times SUN_PULSATION}
          - one harmonic term at 3 times SUN_PULSATION}
          - one harmonic term at MOON_DRACONIC_PULSATION}
          - one harmonic term at 2 times MOON_DRACONIC_PULSATION}
          - one harmonic term at 3 times MOON_DRACONIC_PULSATION}
        
        
        Returns:
            fitter with default configuration for pole nutation parameters dx and dy
        
        
        """
        ...
    @staticmethod
    def createDefaultPoleFitterLongTermPrediction() -> 'SingleParameterFitter':
        """
        Create fitter with default parameters adapted for fitting pole parameters Xp and Yp for long term prediction.
        
        The main difference between these settings and createDefaultPoleFitterShortTermPrediction is the much larger \(\tau\). This means weight is spread throughout history, hence forcing the fitted prediction model to be remain very stable on the long term. On the other hand, this implies that the model will start with already a much larger error just after raw history end. These settings are intended when prediction is used for 5 days after raw EOP end or more.
        
          - time constant \(\tau\) of the exponential decay set to 60 JULIAN_DAY
          - convergence set to 10⁻¹² rad
          - polynomial part set to degree 3
          - one harmonic term at SUN_PULSATION}
          - one harmonic term at 2 times SUN_PULSATION}
          - one harmonic term at 3 times SUN_PULSATION}
          - one harmonic term at MOON_DRACONIC_PULSATION}
          - one harmonic term at 2 times MOON_DRACONIC_PULSATION}
          - one harmonic term at 3 times MOON_DRACONIC_PULSATION}
        
        
        Returns:
            fitter with default configuration for pole parameters Xp and Yp
        
        
        """
        ...
    @staticmethod
    def createDefaultPoleFitterShortTermPrediction() -> 'SingleParameterFitter':
        """
        Create fitter with default parameters adapted for fitting pole parameters Xp and Yp for long term prediction.
        
        The main difference between these settings and createDefaultPoleFitterLongTermPrediction is the much smaller \(\tau\). This means more weight is set to the points at the end of the history, hence forcing the fitted prediction model to be closer to these points, hence the prediction error to be smaller just after raw history end. On the other hand, this implies that the model will diverge on long term. These settings are intended when prediction is used for at most 5 days after raw EOP end.
        
          - time constant \(\tau\) of the exponential decay set to 12 JULIAN_DAY
          - convergence set to 10⁻¹² rad
          - polynomial part set to degree 3
          - one harmonic term at SUN_PULSATION}
          - one harmonic term at 2 times SUN_PULSATION}
          - one harmonic term at 3 times SUN_PULSATION}
          - one harmonic term at MOON_DRACONIC_PULSATION}
          - one harmonic term at 2 times MOON_DRACONIC_PULSATION}
          - one harmonic term at 3 times MOON_DRACONIC_PULSATION}
        
        
        Returns:
            fitter with default configuration for pole parameters Xp and Yp
        
        
        """
        ...
    def fit(self, rawHistory: EOPHistory, extractor: typing.Union[java.util.function.ToDoubleFunction[EOPEntry], typing.Callable[[EOPEntry], float]]) -> org.orekit.utils.SecularAndHarmonic:
        """
        Perform secular and harmonic fitting.
        
        Parameters:
            rawHistory (EOPHistory): EOP history to fit
            extractor (ToDoubleFunction<EOPEntry> extractor): extractor for Earth Orientation Parameter
        
        Returns:
            configured fitter
        
        
        """
        ...

class StaticTransform(org.orekit.time.TimeStamped):
    """
    A transform that only includes translation and rotation. It is static in the sense that no rates thereof are included.
    
    Since:
        11.2
    
    Also see:
        Transform
    """
    @staticmethod
    def compose(date: org.orekit.time.AbsoluteDate, first: 'StaticTransform', second: 'StaticTransform') -> 'StaticTransform':
        """
        Build a transform by combining two existing ones.
        
        Note that the dates of the two existing transformed are ignored, and the combined transform date is set to the date supplied in this constructor without any attempt to shift the raw transforms. This is a design choice allowing user full control of the combination.
        
        Parameters:
            date (AbsoluteDate): date of the transform
            first (StaticTransform): first transform applied
            second (StaticTransform): second transform applied
        
        Returns:
            the newly created static transform that has the same effect as applying first, then second.
        
        Also see:
            of
        
        
        """
        ...
    @staticmethod
    def compositeRotation(first: 'StaticTransform', second: 'StaticTransform') -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Compute a composite rotation.
        
        Parameters:
            first (StaticTransform): first applied transform
            second (StaticTransform): second applied transform
        
        Returns:
            rotation part of the composite transform
        
        
        """
        ...
    @staticmethod
    def compositeTranslation(first: 'StaticTransform', second: 'StaticTransform') -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute a composite translation.
        
        Parameters:
            first (StaticTransform): first applied transform
            second (StaticTransform): second applied transform
        
        Returns:
            translation part of the composite transform
        
        
        """
        ...
    @staticmethod
    def getIdentity() -> 'StaticTransform':
        """
        Get the identity static transform. It overrides most methods for speed.
        
        Returns:
            identity transform.
        
        
        """
        ...
    def getInverse(self) -> 'StaticTransform':
        """
        Get the inverse transform of the instance.
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Returns:
            underlying elementary rotation
        
        
        """
        ...
    def getStaticInverse(self) -> 'StaticTransform':
        """
        Get the inverse transform of the instance in static form (without rates). This enables to create a purely static inverse, as inheritors such as Transform may have a relatively computationally-heavy #getInverse() method.
        
        Returns:
            inverse static transform of the instance
        
        Since:
            12.1
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Returns:
            underlying elementary translation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation) -> 'StaticTransform':
        """
        Parameters:
            date (AbsoluteDate): of translation.
            rotation (Rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
        
        Returns:
            the newly created static transform.
        
        Also see:
            of
        
        Create a new static transform from a translation and rotation.
        
        Parameters:
            date (AbsoluteDate): of translation.
            translation (Vector3D): to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin in the old frame.
        
        Returns:
            the newly created static transform.
        
        Also see:
            of
        
        Create a new static transform from a translation and rotation.
        
        Parameters:
            date (AbsoluteDate): of translation.
            translation (Vector3D): to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin in the old frame.
            rotation (Rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
        
        Returns:
            the newly created static transform.
        
        Also see:
            compose, of,
            of
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'StaticTransform': ...
    @typing.overload
    @staticmethod
    def of(absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation) -> 'StaticTransform': ...
    def transformLine(self, line: org.hipparchus.geometry.euclidean.threed.Line) -> org.hipparchus.geometry.euclidean.threed.Line:
        """
        Transform a line.
        
        Parameters:
            line (Line): to transform
        
        Returns:
            transformed line
        
        
        """
        ...
    _transformPosition_0__T = typing.TypeVar('_transformPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformPosition(self, position: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformPosition_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformPosition_0__T]:
        """
        Parameters:
            position (FieldVector3D<T> position): vector to transform
        
        Returns:
            transformed position
        
        
        """
        ...
    @typing.overload
    def transformPosition(self, position: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Parameters:
            position (Vector3D): vector to transform
        
        Returns:
            transformed position
        
        """
        ...
    _transformVector_0__T = typing.TypeVar('_transformVector_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformVector(self, vector: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformVector_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformVector_0__T]:
        """
        Parameters:
            vector (FieldVector3D<T> vector): vector to transform
        
        Returns:
            transformed vector
        
        
        """
        ...
    @typing.overload
    def transformVector(self, vector: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Parameters:
            vector (Vector3D): vector to transform
        
        Returns:
            transformed vector
        
        """
        ...

class TransformGenerator(org.orekit.utils.TimeStampedGenerator['Transform']):
    """
    Generator to use transforms in GenericTimeStampedCache.
    
    Since:
        9.0
    
    Also see:
        GenericTimeStampedCache
    """
    def __init__(self, neighborsSize: int, provider: 'TransformProvider', step: float):
        """
        simple constructor.
        
        Parameters:
            neighborsSize (int): number of neighbors
            provider (TransformProvider): underlying provider
            step (double): step size
        
        
        """
        ...
    def generate(self, existingDate: org.orekit.time.AbsoluteDate, date: org.orekit.time.AbsoluteDate) -> java.util.List['Transform']:
        """
        Generate a chronologically sorted list of entries to be cached.
        
        If existingDate is earlier than date, the range covered by generated entries must cover at least from existingDate (excluded) to date (included). If existingDate is later than date, the range covered by generated entries must cover at least from date (included) to existingDate (excluded).
        
        The generated entries may cover a range larger than the minimum specified above if the generator prefers to generate large chunks of data at once. It may generate again entries already generated by an earlier call (typically at existingDate), these extra entries will be silently ignored by the cache.
        
        Non-coverage of the minimum range may lead to a loss of data, as the gap will not be filled by the GenericTimeStampedCache in subsequent calls.
        
        The generated entries must be chronologically sorted.
        
        Specified by: generate in interface TimeStampedGenerator
        
        Parameters:
            existingDate (AbsoluteDate): date of the closest already existing entry (may be null)
            date (AbsoluteDate): date that must be covered by the range of the generated array
        
        Returns:
            chronologically sorted list of generated entries
        
        
        """
        ...

class TransformProvider:
    """
    Interface for Transform providers.
    
    The transform provider interface is mainly used to define the transform between a frame and its parent frame.
    """
    _getKinematicTransform_0__T = typing.TypeVar('_getKinematicTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getKinematicTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getKinematicTransform_0__T]) -> 'FieldKinematicTransform'[_getKinematicTransform_0__T]:
        """
        Get a transform for position and velocity, not acceleration.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the kinematic transform.
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    def getKinematicTransform(self, date: org.orekit.time.AbsoluteDate) -> 'KinematicTransform':
        """
        Get a transform for position and velocity, not acceleration.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the kinematic transform.
        
        Since:
            12.1
        
        """
        ...
    _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> FieldStaticTransform[_getStaticTransform_0__T]:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the static transform.
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> StaticTransform:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation calls getTransform but implementations may override it for better performance.
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the static transform.
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        Since:
            9.0
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class TransformProviderUtils:
    """
    Utility for Transform providers.
    
    Since:
        9.2
    """
    IDENTITY_PROVIDER: typing.ClassVar[TransformProvider] = ...
    """
    Identity provider.
    
    The transforms generated by this providers are always IDENTITY.
    """
    @staticmethod
    def getCombinedProvider(first: TransformProvider, second: TransformProvider) -> TransformProvider:
        """
        Combine two transform providers.
        
        Parameters:
            first (TransformProvider): first provider to apply
            second (TransformProvider): second provider to apply
        
        Returns:
            a new provider which provide a transform similar to getTransform(date))
        
        
        """
        ...
    @staticmethod
    def getReversedProvider(provider: TransformProvider) -> TransformProvider:
        """
        Reverse a transform provider.
        
        Parameters:
            provider (TransformProvider): provider to reverse
        
        Returns:
            a new provider which provide a transform similar to getInverse()
        
        
        """
        ...

class AbstractFrames(Frames):
    def __init__(self, timeScales: org.orekit.time.TimeScales, supplier: typing.Union[java.util.function.Supplier[Frame], typing.Callable[[], Frame]]): ...
    def buildUncachedITRF(self, uT1Scale: org.orekit.time.UT1Scale) -> Frame: ...
    def getCIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getEME2000(self) -> 'FactoryManagedFrame': ...
    def getEcliptic(self, iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    def getFrame(self, predefined: Predefined) -> Frame: ...
    def getGCRF(self) -> Frame: ...
    @typing.overload
    def getGTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getGTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getICRF(self) -> Frame: ...
    @typing.overload
    def getITRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getITRF(self, iTRFVersion: 'ITRFVersion', iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    def getITRFEquinox(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getMOD(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    def getPZ9011(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getTEME(self) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, boolean: bool) -> 'FactoryManagedFrame': ...
    @typing.overload
    def getTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'FactoryManagedFrame': ...
    def getVeis1950(self) -> 'FactoryManagedFrame': ...

class CR3BPRotatingFrame(Frame):
    """
    Class creating the rotating frame centered on the barycenter of the CR3BP System.
    
    Since:
        10.2
    """
    def __init__(self, mu: float, primaryBody: org.orekit.bodies.CelestialBody, secondaryBody: org.orekit.bodies.CelestialBody):
        """
        Simple constructor.
        
        Parameters:
            mu (double): Mass ratio
            primaryBody (CelestialBody): Primary body.
            secondaryBody (CelestialBody): Secondary body.
        
        
        """
        ...

class EOPBasedTransformProvider(TransformProvider):
    """
    Interface for Transform providers that use EOPHistory.
    
    Since:
        7.1
    """
    def getEOPHistory(self) -> EOPHistory:
        """
        Get the EOP history.
        
        Returns:
            EOP history
        
        
        """
        ...
    def getNonInterpolatingProvider(self) -> 'EOPBasedTransformProvider':
        """
        Get a version of the provider that does not cache tidal corrections.
        
        This method removes the performance enhancing interpolation features that are used by default in EOP-based provider, in order to focus on accuracy. The interpolation features are intended to save processing time by avoiding doing tidal correction evaluation at each time step and caching some results. This method can be used to avoid this (it is automatically called by getNonInterpolatingTransform, when very high accuracy is desired, or for testing purposes. It should be used with care, as doing the full computation is really costly.
        
        Returns:
            version of the provider that does not cache tidal corrections
        
        Also see:
            getNonInterpolatingTransform
        
        
        """
        ...

class EclipticProvider(TransformProvider):
    """
    An inertial frame aligned with the ecliptic.
    
    The IAU defines the ecliptic as "the plane perpendicular to the mean heliocentric orbital angular momentum vector of the Earth-Moon barycentre in the BCRS (IAU 2006 Resolution B1)." The +z axis is aligned with the angular momentum vector, and the +x axis is aligned with +x axis of getMOD.
    
    This implementation agrees with the JPL 406 ephemerides to within 0.5 arc seconds.
    
    Since:
        7.0
    """
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions): ...
    @typing.overload
    def __init__(self, iERSConventions: org.orekit.utils.IERSConventions, timeScales: org.orekit.time.TimeScales): ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Description copied from interface: getTransform Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Description copied from interface: getTransform Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class FactoryManagedFrame(Frame):
    """
    Base class for the predefined frames that are managed by Frames.
    """
    def __init__(self, parent: Frame, transformProvider: TransformProvider, pseudoInertial: bool, factoryKey: Predefined):
        """
        Simple constructor.
        
        Parameters:
            parent (Frame): parent frame (must be non-null)
            transformProvider (TransformProvider): provider for transform from parent frame to instance
            pseudoInertial (boolean): true if frame is considered pseudo-inertial (i.e. suitable for propagating orbit)
            factoryKey (Predefined): key of the frame within the factory
        
        
        """
        ...
    def getFactoryKey(self) -> Predefined:
        """
        Get the key of the frame within the factory.
        
        Returns:
            key of the frame within the factory
        
        
        """
        ...

_FieldKinematicTransform__T = typing.TypeVar('_FieldKinematicTransform__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldKinematicTransform(FieldStaticTransform[_FieldKinematicTransform__T], typing.Generic[_FieldKinematicTransform__T]):
    """
    A transform that only includes translation and rotation as well as their respective rates. It is kinematic in the sense that it cannot transform an acceleration vector.
    
    Since:
        12.1
    
    Also see:
        FieldStaticTransform, FieldTransform,
        KinematicTransform
    """
    _compose__T = typing.TypeVar('_compose__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def compose(date: org.orekit.time.FieldAbsoluteDate[_compose__T], first: 'FieldKinematicTransform'[_compose__T], second: 'FieldKinematicTransform'[_compose__T]) -> 'FieldKinematicTransform'[_compose__T]:
        """
        Build a transform by combining two existing ones.
        
        Note that the dates of the two existing transformed are ignored, and the combined transform date is set to the date supplied in this constructor without any attempt to shift the raw transforms. This is a design choice allowing user full control of the combination.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): date of the transform
            first (FieldKinematicTransform<T> first): first transform applied
            second (FieldKinematicTransform<T> second): second transform applied
        
        Returns:
            the newly created kinematic transform that has the same effect as applying first, then second.
        
        Also see:
            of
        
        
        """
        ...
    _compositeRotationRate__T = typing.TypeVar('_compositeRotationRate__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def compositeRotationRate(first: 'FieldKinematicTransform'[_compositeRotationRate__T], second: 'FieldKinematicTransform'[_compositeRotationRate__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_compositeRotationRate__T]:
        """
        Compute a composite rotation rate.
        
        Parameters:
            first (FieldKinematicTransform<T> first): first applied transform
            second (FieldKinematicTransform<T> second): second applied transform
        
        Returns:
            rotation rate part of the composite transform
        
        
        """
        ...
    _compositeVelocity__T = typing.TypeVar('_compositeVelocity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def compositeVelocity(first: 'FieldKinematicTransform'[_compositeVelocity__T], second: 'FieldKinematicTransform'[_compositeVelocity__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_compositeVelocity__T]:
        """
        Compute a composite velocity.
        
        Parameters:
            first (FieldKinematicTransform<T> first): first applied transform
            second (FieldKinematicTransform<T> second): second applied transform
        
        Returns:
            velocity part of the composite transform
        
        
        """
        ...
    _getIdentity__T = typing.TypeVar('_getIdentity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getIdentity(field: org.hipparchus.Field[_getIdentity__T]) -> 'FieldKinematicTransform'[_getIdentity__T]:
        """
        Get the identity kinematic transform.
        
        Parameters:
            field (Field<T> field): field used by default
        
        Returns:
            identity transform.
        
        
        """
        ...
    def getInverse(self) -> 'FieldKinematicTransform'[_FieldKinematicTransform__T]:
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface FieldStaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getPVJacobian(self) -> typing.MutableSequence[typing.MutableSequence[_FieldKinematicTransform__T]]:
        """
        Compute the Jacobian of the transformOnlyPV (FieldPVCoordinates)} method of the transform.
        
        Element jacobian[i][j] is the derivative of Cartesian coordinate i of the transformed FieldPVCoordinates with respect to Cartesian coordinate j of the input FieldPVCoordinates in method transformOnlyPV.
        
        This definition implies that if we define position-velocity coordinates
        
         PV₁ = transform.transformPVCoordinates(PV₀), then
        
        their differentials dPV₁ and dPV₀ will obey the following relation where J is the matrix computed by this method:
        
         dPV₁ = J × dPV₀
        
        Returns:
            Jacobian matrix
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldKinematicTransform__T]:
        """
        Get the first time derivative of the rotation.
        
        The norm represents the angular rate.
        
        Returns:
            First time derivative of the rotation
        
        Also see:
            getRotation
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldKinematicTransform__T]:
        """
        Get the first time derivative of the translation.
        
        Returns:
            first time derivative of the translation
        
        Also see:
            getTranslation
        
        
        """
        ...
    _of_0__T = typing.TypeVar('_of_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_1__T = typing.TypeVar('_of_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_2__T = typing.TypeVar('_of_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _of_3__T = typing.TypeVar('_of_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def of(field: org.hipparchus.Field[_of_0__T], kinematicTransform: 'KinematicTransform') -> 'FieldKinematicTransform'[_of_0__T]:
        """
        Create a new kinematic transform from a translation and its rate.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            pvCoordinates (FieldPVCoordinates<T> pvCoordinates): translation (with rate) to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin
                in the old frame.
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            of
        
        Create a new kinematic transform from a non-Field version.
        
        Parameters:
            field (Field<T> field): field.
            kinematicTransform (KinematicTransform): non-Field kinematic transform
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            of
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(date: org.orekit.time.FieldAbsoluteDate[_of_1__T], rotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_of_1__T], rotationRate: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_of_1__T]) -> 'FieldKinematicTransform'[_of_1__T]:
        """
        Create a new kinematic transform from a rotation and zero, constant translation.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            rotation (FieldRotation<T> rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
            rotationRate (FieldVector3D<T> rotationRate): rate of rotation
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            of
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_of_2__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_of_2__T]) -> 'FieldKinematicTransform'[_of_2__T]: ...
    @typing.overload
    @staticmethod
    def of(date: org.orekit.time.FieldAbsoluteDate[_of_3__T], pvCoordinates: org.orekit.utils.FieldPVCoordinates[_of_3__T], rotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_of_3__T], rotationRate: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_of_3__T]) -> 'FieldKinematicTransform'[_of_3__T]:
        """
        Create a new kinematic transform from a translation and rotation.
        
        Parameters:
            date (FieldAbsoluteDate<T> date): of translation.
            pvCoordinates (FieldPVCoordinates<T> pvCoordinates): translation (with rate) to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin
                in the old frame.
            rotation (FieldRotation<T> rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
            rotationRate (FieldVector3D<T> rotationRate): rate of rotation
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            compose, of,
            of
        
        
        """
        ...
    @typing.overload
    def transformOnlyPV(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldKinematicTransform__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldKinematicTransform__T]: ...
    @typing.overload
    def transformOnlyPV(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldKinematicTransform__T]) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldKinematicTransform__T]: ...

class FixedTransformProvider(TransformProvider):
    """
    Transform provider using fixed transform.
    """
    def __init__(self, transform: 'Transform'):
        """
        Simple constructor.
        
        Parameters:
            transform (Transform): fixed transform
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class HelmertTransformation(TransformProvider):
    """
    Transformation class for geodetic systems.
    
    The Helmert transformation is mainly used to convert between various realizations of geodetic frames, for example in the ITRF family.
    
    The original Helmert transformation is a 14 parameters transform that includes translation, velocity, rotation, rotation rate and scale factor. The scale factor is useful for coordinates near Earth surface, but it cannot be extended to outer space as it would correspond to a non-unitary transform. Therefore, the scale factor is not used here.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        5.1
    """
    def __init__(self, epoch: org.orekit.time.AbsoluteDate, t1: float, t2: float, t3: float, r1: float, r2: float, r3: float, t1Dot: float, t2Dot: float, t3Dot: float, r1Dot: float, r2Dot: float, r3Dot: float):
        """
        Build a transform from its primitive operations.
        
        Parameters:
            epoch (AbsoluteDate): reference epoch of the transform
            t1 (double): translation parameter along X axis (BEWARE, this is in mm)
            t2 (double): translation parameter along Y axis (BEWARE, this is in mm)
            t3 (double): translation parameter along Z axis (BEWARE, this is in mm)
            r1 (double): rotation parameter around X axis (BEWARE, this is in mas)
            r2 (double): rotation parameter around Y axis (BEWARE, this is in mas)
            r3 (double): rotation parameter around Z axis (BEWARE, this is in mas)
            t1Dot (double): rate of translation parameter along X axis (BEWARE, this is in mm/y)
            t2Dot (double): rate of translation parameter along Y axis (BEWARE, this is in mm/y)
            t3Dot (double): rate of translation parameter along Z axis (BEWARE, this is in mm/y)
            r1Dot (double): rate of rotation parameter around X axis (BEWARE, this is in mas/y)
            r2Dot (double): rate of rotation parameter around Y axis (BEWARE, this is in mas/y)
            r3Dot (double): rate of rotation parameter around Z axis (BEWARE, this is in mas/y)
        
        
        """
        ...
    def getEpoch(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the reference epoch of the transform.
        
        Returns:
            reference epoch of the transform
        
        
        """
        ...
    _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> FieldStaticTransform[_getStaticTransform_0__T]:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the static transform.
        
        
        """
        ...
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> StaticTransform:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation calls getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the static transform.
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...
    class Predefined(java.lang.Enum['HelmertTransformation.Predefined']):
        ITRF_2020_TO_ITRF_2014: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_2008: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_2005: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_2000: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1997: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1996: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1994: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1993: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1992: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1991: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1990: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1989: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2020_TO_ITRF_1988: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_2008: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_2005: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_2000: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1997: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1996: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1994: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1993: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1992: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1991: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1990: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1989: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2014_TO_ITRF_1988: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_2005: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_2000: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1997: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1996: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1994: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1993: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1992: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1991: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1990: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1989: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        ITRF_2008_TO_ITRF_1988: typing.ClassVar['HelmertTransformation.Predefined'] = ...
        @typing.overload
        def createTransformedITRF(self, frame: Frame, string: str) -> Frame: ...
        @typing.overload
        def createTransformedITRF(self, frame: Frame, string: str, timeScale: org.orekit.time.TimeScale) -> Frame: ...
        def getDestination(self) -> 'ITRFVersion': ...
        def getOrigin(self) -> 'ITRFVersion': ...
        @typing.overload
        def getTransformation(self) -> 'HelmertTransformation': ...
        @typing.overload
        def getTransformation(self, timeScale: org.orekit.time.TimeScale) -> 'HelmertTransformation': ...
        @staticmethod
        def selectPredefined(int: int, int2: int) -> 'HelmertTransformation.Predefined': ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'HelmertTransformation.Predefined': ...
        @staticmethod
        def values() -> typing.MutableSequence['HelmertTransformation.Predefined']: ...

class ITRFVersion(java.lang.Enum['ITRFVersion']):
    """
    Enumerate for ITRF versions.
    
    Since:
        9.2
    
    Also see:
        EOPEntry, HelmertTransformation
    """
    ITRF_2020: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2014: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2008: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2005: typing.ClassVar['ITRFVersion'] = ...
    ITRF_2000: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1997: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1996: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1994: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1993: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1992: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1991: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1990: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1989: typing.ClassVar['ITRFVersion'] = ...
    ITRF_1988: typing.ClassVar['ITRFVersion'] = ...
    @typing.overload
    @staticmethod
    def getConverter(iTRFVersion: 'ITRFVersion', iTRFVersion2: 'ITRFVersion') -> 'ITRFVersion.Converter':
        """
        Find a converter between specified ITRF frames.
        
        Parameters:
            origin (ITRFVersion): origin ITRF
            destination (ITRFVersion): destination ITRF
            tt (TimeScale): TT time scale.
        
        Returns:
            transform from origin to destination
        
        Since:
            10.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getConverter(iTRFVersion: 'ITRFVersion', iTRFVersion2: 'ITRFVersion', timeScale: org.orekit.time.TimeScale) -> 'ITRFVersion.Converter': ...
    @typing.overload
    @staticmethod
    def getITRFVersion(int: int) -> 'ITRFVersion':
        """
        Find an ITRF version from its reference year.
        
        Parameters:
            year (int): reference year of the frame version
        
        Returns:
            ITRF version for specified year
        
        Find an ITRF version from its name.
        
        Parameters:
            name (String): name of the frame version (case is ignored)
        
        Returns:
            ITRF version
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getITRFVersion(string: str) -> 'ITRFVersion': ...
    @staticmethod
    def getLast() -> 'ITRFVersion':
        """
        Get last supported ITRF version.
        
        Returns:
            last supported ITRF version
        
        Since:
            11.2
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get the name the frame version.
        
        Returns:
            name of the frame version
        
        
        """
        ...
    def getYear(self) -> int:
        """
        Get the reference year of the frame version.
        
        Returns:
            reference year of the frame version
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'ITRFVersion':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['ITRFVersion']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (ITRFVersion c : ITRFVersion.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class Converter(TransformProvider):
        def getDestination(self) -> 'ITRFVersion': ...
        _getKinematicTransform_0__T = typing.TypeVar('_getKinematicTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getKinematicTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getKinematicTransform_0__T]) -> FieldKinematicTransform[_getKinematicTransform_0__T]: ...
        @typing.overload
        def getKinematicTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'KinematicTransform': ...
        def getOrigin(self) -> 'ITRFVersion': ...
        _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getStaticTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> FieldStaticTransform[_getStaticTransform_0__T]: ...
        @typing.overload
        def getStaticTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> StaticTransform: ...
        _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
        @typing.overload
        def getTransform(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]: ...
        @typing.overload
        def getTransform(self, absoluteDate: org.orekit.time.AbsoluteDate) -> 'Transform': ...

class ITRFVersionLoader(ItrfVersionProvider):
    """
    Loader for ITRF version configuration file.
    
    The ITRF version configuration file specifies the ITRFVersion that each type of Earth Orientation Parameter file contains for each date. This configuration file is used to interpret EOP C04 files, Bulletin A files, Bulletin B files, rapid data and prediction files in columns format files, rapid data and prediction files in XML format files...
    
    This file is an Orekit-specific configuration file.
    
    This class is immutable and hence thread-safe
    
    Since:
        9.2
    
    Also see:
        EopC04FilesLoader, BulletinAFilesLoader, BulletinBFilesLoader,
        RapidDataAndPredictionColumnsLoader, EopXmlLoader
    """
    SUPPORTED_NAMES: typing.ClassVar[str] = ...
    """
    Regular expression for supported files names.
    
    Also see:
        constant
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, dataProvidersManager: org.orekit.data.DataProvidersManager): ...
    def getConfiguration(self, name: str, mjd: int) -> 'ITRFVersionLoader.ITRFVersionConfiguration':
        """
        Description copied from interface: getConfiguration Get the ITRF version configuration defined by a given file at specified date.
        
        Specified by: getConfiguration in interface ItrfVersionProvider
        
        Parameters:
            name (String): EOP file name
            mjd (int): date of the EOP in modified Julian day
        
        Returns:
            configuration valid around specified date in the file
        
        
        """
        ...
    class ITRFVersionConfiguration:
        def __init__(self, string: str, iTRFVersion: ITRFVersion, int: int, int2: int): ...
        def appliesTo(self, string: str) -> bool: ...
        def getVersion(self) -> ITRFVersion: ...
        def isValid(self, int: int) -> bool: ...

class InterpolatingTransformProvider(TransformProvider):
    """
    Transform provider using thread-safe interpolation on transforms sample.
    
    The interpolation is a polynomial Hermite interpolation, which can either use or ignore the derivatives provided by the raw provider. This means that simple raw providers that do not compute derivatives can be used, the derivatives will be added appropriately by the interpolation process.
    
    Also see:
        GenericTimeStampedCache, ShiftingTransformProvider
    """
    def __init__(self, rawProvider: TransformProvider, cFilter: org.orekit.utils.CartesianDerivativesFilter, aFilter: org.orekit.utils.AngularDerivativesFilter, gridPoints: int, step: float, maxSlots: int, maxSpan: float, newSlotInterval: float):
        """
        Simple constructor.
        
        Parameters:
            rawProvider (TransformProvider): provider for raw (non-interpolated) transforms
            cFilter (CartesianDerivativesFilter): filter for derivatives from the sample to use in interpolation
            aFilter (AngularDerivativesFilter): filter for derivatives from the sample to use in interpolation
            gridPoints (int): number of interpolation grid points
            step (double): grid points time step
            maxSlots (int): maximum number of independent cached time slots in the GenericTimeStampedCache
            maxSpan (double): maximum duration span in seconds of one slot in the GenericTimeStampedCache
            newSlotInterval (double): time interval above which a new slot is created in the GenericTimeStampedCache
        
        Since:
            9.1
        
        
        """
        ...
    def getGridPoints(self) -> int:
        """
        Get the number of interpolation grid points.
        
        Returns:
            number of interpolation grid points
        
        
        """
        ...
    def getRawProvider(self) -> TransformProvider:
        """
        Get the underlying provider for raw (non-interpolated) transforms.
        
        Returns:
            provider for raw (non-interpolated) transforms
        
        
        """
        ...
    def getStep(self) -> float:
        """
        Get the grid points time step.
        
        Returns:
            grid points time step
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class KinematicTransform(StaticTransform):
    """
    A transform that only includes translation and rotation as well as their respective rates. It is kinematic in the sense that it cannot transform an acceleration vector.
    
    Since:
        12.1
    
    Also see:
        StaticTransform, Transform
    """
    @staticmethod
    def compose(date: org.orekit.time.AbsoluteDate, first: 'KinematicTransform', second: 'KinematicTransform') -> 'KinematicTransform':
        """
        Build a transform by combining two existing ones.
        
        Note that the dates of the two existing transformed are ignored, and the combined transform date is set to the date supplied in this constructor without any attempt to shift the raw transforms. This is a design choice allowing user full control of the combination.
        
        Parameters:
            date (AbsoluteDate): date of the transform
            first (KinematicTransform): first transform applied
            second (KinematicTransform): second transform applied
        
        Returns:
            the newly created kinematic transform that has the same effect as applying first, then second.
        
        Also see:
            of
        
        
        """
        ...
    @staticmethod
    def compositeRotationRate(first: 'KinematicTransform', second: 'KinematicTransform') -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute a composite rotation rate.
        
        Parameters:
            first (KinematicTransform): first applied transform
            second (KinematicTransform): second applied transform
        
        Returns:
            rotation rate part of the composite transform
        
        
        """
        ...
    @staticmethod
    def compositeVelocity(first: 'KinematicTransform', second: 'KinematicTransform') -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Compute a composite velocity.
        
        Parameters:
            first (KinematicTransform): first applied transform
            second (KinematicTransform): second applied transform
        
        Returns:
            velocity part of the composite transform
        
        
        """
        ...
    @staticmethod
    def getIdentity() -> 'KinematicTransform':
        """
        Get the identity kinematic transform.
        
        Returns:
            identity transform.
        
        
        """
        ...
    def getInverse(self) -> 'KinematicTransform':
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface StaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getPVJacobian(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the Jacobian of the transformOnlyPV (PVCoordinates)} method of the transform.
        
        Element jacobian[i][j] is the derivative of Cartesian coordinate i of the transformed PVCoordinates with respect to Cartesian coordinate j of the input PVCoordinates in method transformOnlyPV.
        
        This definition implies that if we define position-velocity coordinates
        
         PV₁ = transform.transformPVCoordinates(PV₀), then
        
        their differentials dPV₁ and dPV₀ will obey the following relation where J is the matrix computed by this method:
        
         dPV₁ = J × dPV₀
        
        Returns:
            Jacobian matrix
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the first time derivative of the rotation.
        
        The norm represents the angular rate.
        
        Returns:
            First time derivative of the rotation
        
        Also see:
            getRotation
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the first time derivative of the translation.
        
        Returns:
            first time derivative of the translation
        
        Also see:
            getTranslation
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'KinematicTransform':
        """
        Create a new kinematic transform from a rotation and zero, constant translation.
        
        Parameters:
            date (AbsoluteDate): of translation.
            rotation (Rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
            rotationRate (Vector3D): rate of rotation
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            of
        
        Create a new kinematic transform from a translation and rotation.
        
        Parameters:
            date (AbsoluteDate): of translation.
            pvCoordinates (PVCoordinates): translation (with rate) to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin
                in the old frame.
            rotation (Rotation): to apply after the translation. That is after translating applying this rotation produces positions expressed in the new
                frame.
            rotationRate (Vector3D): rate of rotation
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            compose, of,
            of
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(date: org.orekit.time.AbsoluteDate, pvCoordinates: org.orekit.utils.PVCoordinates) -> 'KinematicTransform':
        """
        Create a new kinematic transform from a translation and its rate.
        
        Parameters:
            date (AbsoluteDate): of translation.
            pvCoordinates (PVCoordinates): translation (with rate) to apply, expressed in the old frame. That is, the opposite of the coordinates of the new origin
                in the old frame.
        
        Returns:
            the newly created kinematic transform.
        
        Also see:
            of
        
        """
        ...
    @typing.overload
    @staticmethod
    def of(absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'KinematicTransform': ...
    @typing.overload
    def transformOnlyPV(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.orekit.utils.PVCoordinates:
        """
        Transform PVCoordinates, without the acceleration vector.
        
        Parameters:
            pv (PVCoordinates): the position-velocity couple to transform.
        
        Returns:
            transformed position-velocity
        
        Transform TimeStampedPVCoordinates, without the acceleration vector.
        
        In order to allow the user more flexibility, this method does not check for consistency between the transform getDate and the time-stamped position-velocity getDate. The returned value will always have the same getDate as the input argument, regardless of the instance getDate.
        
        Parameters:
            pv (TimeStampedPVCoordinates): the position-velocity couple to transform.
        
        Returns:
            transformed position-velocity
        
        
        """
        ...
    @typing.overload
    def transformOnlyPV(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class L1Frame(Frame):
    """
    Class to create a L1 centered frame with L1TransformProvider. Parent frame is always set as primaryBody.getInertiallyOrientedFrame()
    """
    def __init__(self, primaryBody: org.orekit.bodies.CelestialBody, secondaryBody: org.orekit.bodies.CelestialBody):
        """
        Simple constructor.
        
        Parameters:
            primaryBody (CelestialBody): Celestial body with bigger mass, m1.
            secondaryBody (CelestialBody): Celestial body with smaller mass, m2.
        
        
        """
        ...

class L1TransformProvider(TransformProvider):
    """
    L1 Transform provider for a frame on the L1 Lagrange point of two celestial bodies.
    """
    def __init__(self, primaryBody: org.orekit.bodies.CelestialBody, secondaryBody: org.orekit.bodies.CelestialBody):
        """
        Simple constructor.
        
        Parameters:
            primaryBody (CelestialBody): Primary body.
            secondaryBody (CelestialBody): Secondary body.
        
        
        """
        ...
    _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> FieldStaticTransform[_getStaticTransform_0__T]:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the static transform.
        
        
        """
        ...
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> StaticTransform:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation calls getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the static transform.
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class L2Frame(Frame):
    """
    Class to create a L2 centered frame with L2TransformProvider. Parent frame is always set as primaryBody.getInertiallyOrientedFrame()
    """
    def __init__(self, primaryBody: org.orekit.bodies.CelestialBody, secondaryBody: org.orekit.bodies.CelestialBody):
        """
        Simple constructor.
        
        Parameters:
            primaryBody (CelestialBody): Celestial body with bigger mass, m1.
            secondaryBody (CelestialBody): Celestial body with smaller mass, m2.
        
        
        """
        ...

class LOFType(java.lang.Enum['LOFType'], LOF):
    """
    Enumerate for different types of Local Orbital Frames.
    """
    TNW: typing.ClassVar['LOFType'] = ...
    TNW_INERTIAL: typing.ClassVar['LOFType'] = ...
    QSW: typing.ClassVar['LOFType'] = ...
    QSW_INERTIAL: typing.ClassVar['LOFType'] = ...
    LVLH: typing.ClassVar['LOFType'] = ...
    LVLH_INERTIAL: typing.ClassVar['LOFType'] = ...
    LVLH_CCSDS: typing.ClassVar['LOFType'] = ...
    LVLH_CCSDS_INERTIAL: typing.ClassVar['LOFType'] = ...
    VVLH: typing.ClassVar['LOFType'] = ...
    VVLH_INERTIAL: typing.ClassVar['LOFType'] = ...
    VNC: typing.ClassVar['LOFType'] = ...
    VNC_INERTIAL: typing.ClassVar['LOFType'] = ...
    EQW: typing.ClassVar['LOFType'] = ...
    NTW: typing.ClassVar['LOFType'] = ...
    NTW_INERTIAL: typing.ClassVar['LOFType'] = ...
    ENU: typing.ClassVar['LOFType'] = ...
    NED: typing.ClassVar['LOFType'] = ...
    def getName(self) -> str:
        """
        Get name of the local orbital frame.
        
        Specified by: getName in interface LOF
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromInertial_2__T = typing.TypeVar('_rotationFromInertial_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]: ...
    @typing.overload
    def rotationFromInertial(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it. It is unnecessary to use this method when dealing with LOFType, use rotationFromInertial instead.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_2__T], fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_2__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_2__T]:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it. It is unnecessary to use this method when dealing with LOFType, use rotationFromInertial instead.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        public abstract <T extends CalculusFieldElement<T>> FieldRotation<T> rotationFromInertial (Field<T> field, FieldPVCoordinates<T> pv)
        
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    _rotationFromLOF_0__T = typing.TypeVar('_rotationFromLOF_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _rotationFromLOF_2__T = typing.TypeVar('_rotationFromLOF_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromLOF(self, field: org.hipparchus.Field[_rotationFromLOF_0__T], lOF: LOF, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_rotationFromLOF_0__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_rotationFromLOF_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromLOF_0__T]: ...
    @typing.overload
    def rotationFromLOF(self, lOF: LOF, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation: ...
    @typing.overload
    def rotationFromLOF(self, field: org.hipparchus.Field[_rotationFromLOF_2__T], fromLOF: 'LOFType', pv: org.orekit.utils.FieldPVCoordinates[_rotationFromLOF_2__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromLOF_2__T]:
        """
        Get the rotation from input LOFType to the instance.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromLOF method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            fromLOF (LOFType): input local orbital frame
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input local orbital frame to the instance
        
        
        """
        ...
    @typing.overload
    def rotationFromLOF(self, fromLOF: 'LOFType', pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from input LOF to the instance.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromLOF method must be called and the complete rotation transform must be extracted from it.
        
        Parameters:
            fromLOF (LOFType): input local orbital frame
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from input local orbital frame to the instance
        
        """
        ...
    def toOrbitRelativeFrame(self) -> org.orekit.files.ccsds.definitions.OrbitRelativeFrame:
        """
        Convert current local orbital frame to CCSDS equivalent orbit relative frame when possible, null otherwise.
        
        Returns:
            CCSDS equivalent orbit relative frame when possible, null otherwise
        
        Also see:
            OrbitRelativeFrame
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'LOFType':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['LOFType']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (LOFType c : LOFType.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class LocalMagneticFieldFrame(LOF):
    """
    This class handles a magnetic field variation attitude provider.
    
    It was designed to be used as a Bdot attitude pointing law which align a specific body axis with Earth magnetic field vector.
    
    Attitude control thought the magnetic field is called Bdot as it follows the sinusoidal variation of the Earth magnetic field vector, along the orbit. Magnetorquers are used on board to align the instrument, as so the satellite, with the planet magnetic field, producing a sinusoidal torque along the orbit.
    """
    @typing.overload
    def __init__(self, frame: Frame, geoMagneticField: org.orekit.models.earth.GeoMagneticField, frame2: Frame): ...
    @typing.overload
    def __init__(self, frame: Frame, geoMagneticField: org.orekit.models.earth.GeoMagneticField, lOFBuilderVector: 'LocalMagneticFieldFrame.LOFBuilderVector', frame2: Frame): ...
    def getInertialFrame(self) -> Frame:
        """
        Get interlai frame.
        
        Returns:
            inertial frame
        
        
        """
        ...
    def getMagneticField(self) -> org.orekit.models.earth.GeoMagneticField:
        """
        Get geomagnetid field.
        
        Returns:
            geo magnetic field
        
        
        """
        ...
    def getName(self) -> str:
        """
        Get name of the local orbital frame.
        
        Specified by: getName in interface LOF
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], date: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], pv: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it. Direction as X axis aligned with magnetic field vector, Y axis aligned with the cross product of the magnetic field vector with chosen LOFBuilderVector.
        
        BEWARE: In this implementation, the method simply fieldify the normal rotation with given field. Hence all derivatives are lost.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it. Direction as X axis aligned with magnetic field vector, Z axis aligned with the cross product of the magnetic field vector with chosen LOFBuilderVector.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        
        """
        ...
    class LOFBuilderVector(java.lang.Enum['LocalMagneticFieldFrame.LOFBuilderVector']):
        PLUS_POSITION: typing.ClassVar['LocalMagneticFieldFrame.LOFBuilderVector'] = ...
        PLUS_VELOCITY: typing.ClassVar['LocalMagneticFieldFrame.LOFBuilderVector'] = ...
        PLUS_MOMENTUM: typing.ClassVar['LocalMagneticFieldFrame.LOFBuilderVector'] = ...
        MINUS_POSITION: typing.ClassVar['LocalMagneticFieldFrame.LOFBuilderVector'] = ...
        MINUS_VELOCITY: typing.ClassVar['LocalMagneticFieldFrame.LOFBuilderVector'] = ...
        MINUS_MOMENTUM: typing.ClassVar['LocalMagneticFieldFrame.LOFBuilderVector'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'LocalMagneticFieldFrame.LOFBuilderVector': ...
        @staticmethod
        def values() -> typing.MutableSequence['LocalMagneticFieldFrame.LOFBuilderVector']: ...

class LocalOrbitalFrame(Frame):
    """
    Class for frames moving with an orbiting satellite.
    
    There are several local orbital frames available. They are specified by the LOFType enumerate.
    
    Do not use the getTransformTo method as it is not implemented.
    
    Also see:
        toTransform
    """
    def __init__(self, parent: Frame, lof: LOF, provider: typing.Union[org.orekit.utils.PVCoordinatesProvider, typing.Callable], name: str):
        """
        Build a new instance.
        
        It is highly recommended that provider use an analytic formulation and not numerical integration as large integration errors may result from many short propagations.
        
        Parameters:
            parent (Frame): parent frame (must be non-null)
            lof (LOF): local orbital frame
            provider (PVCoordinatesProvider): provider used to compute frame motion.
            name (String): name of the frame
        
        Raises:
            IllegalArgumentException: if the parent frame is null
        
        
        """
        ...

class PredictedEOPHistory(EOPHistory):
    """
    This class extends an EOPHistory for some weeks using fitting.
    
    The goal of this class is to provide a reasonable prediction of Earth Orientation Parameters past the last date available in regular EOPHistory, which just generated corrections set to 0 when they have no data.
    
    The prediction is based on fitting of last data, with both SecularAndHarmonic terms. The extended entries are generated at one point per day and are continuous (i.e. no leap seconds are introduced)
    
    After construction, the history contains both the initial raw history and an extension part appended after it.
    
    Since:
        12.0
    
    Also see:
        EOPFitter, SecularAndHarmonic
    """
    def __init__(self, rawHistory: EOPHistory, extensionDuration: float, fitter: EOPFitter):
        """
        Simple constructor.
        
        Parameters:
            rawHistory (EOPHistory): raw EOP history to extend.
            extensionDuration (double): duration of the extension period (s)
            fitter (EOPFitter): fitter for all Earth Orientation Parameters
        
        
        """
        ...

class PythonEOPHistoryLoader(EopHistoryLoader):
    def __init__(self): ...
    def fillHistory(self, converter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, history: java.util.SortedSet[EOPEntry]) -> None:
        """
        Load celestial body.
        
        Specified by: fillHistory in interface EopHistoryLoader
        
        Parameters:
            converter (NutationCorrectionConverter): converter to use for nutation corrections
            history (SortedSet<EOPEntry> history): history to fill up
        
        
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

_PythonFieldStaticTransform__T = typing.TypeVar('_PythonFieldStaticTransform__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldStaticTransform(FieldStaticTransform[_PythonFieldStaticTransform__T], typing.Generic[_PythonFieldStaticTransform__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Description copied from interface: getDate Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getInverse(self) -> FieldStaticTransform[_PythonFieldStaticTransform__T]:
        """
        Description copied from interface: getInverse Get the inverse transform of the instance.
        
        Specified by: getInverse in interface FieldStaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_PythonFieldStaticTransform__T]:
        """
        Description copied from interface: getRotation Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Specified by: getRotation in interface FieldStaticTransform
        
        Returns:
            underlying elementary rotation
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_PythonFieldStaticTransform__T]:
        """
        Description copied from interface: getTranslation Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Specified by: getTranslation in interface FieldStaticTransform
        
        Returns:
            underlying elementary translation
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonFrames(Frames):
    def __init__(self): ...
    def buildUncachedITRF(self, uT1Scale: org.orekit.time.UT1Scale) -> Frame: ...
    def finalize(self) -> None: ...
    def getCIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    def getEME2000(self) -> FactoryManagedFrame: ...
    def getEOPHistory(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> EOPHistory: ...
    def getEcliptic(self, iERSConventions: org.orekit.utils.IERSConventions) -> Frame: ...
    def getFrame(self, predefined: Predefined) -> Frame: ...
    def getGCRF(self) -> Frame: ...
    @typing.overload
    def getGTOD(self, boolean: bool) -> FactoryManagedFrame: ...
    @typing.overload
    def getGTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    def getICRF(self) -> Frame: ...
    @typing.overload
    def getITRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    @typing.overload
    def getITRF(self, iTRFVersion: ITRFVersion, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> 'VersionedITRF': ...
    def getITRFEquinox(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    @typing.overload
    def getMOD(self, boolean: bool) -> FactoryManagedFrame: ...
    @typing.overload
    def getMOD(self, iERSConventions: org.orekit.utils.IERSConventions) -> FactoryManagedFrame: ...
    def getPZ9011(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    def getTEME(self) -> FactoryManagedFrame: ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions) -> FactoryManagedFrame: ...
    @typing.overload
    def getTIRF(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    @typing.overload
    def getTOD(self, boolean: bool) -> FactoryManagedFrame: ...
    @typing.overload
    def getTOD(self, iERSConventions: org.orekit.utils.IERSConventions, boolean: bool) -> FactoryManagedFrame: ...
    def getVeis1950(self) -> FactoryManagedFrame: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonItrfVersionProvider(ItrfVersionProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getConfiguration(self, name: str, mjd: int) -> ITRFVersionLoader.ITRFVersionConfiguration:
        """
        Get the ITRF version configuration defined by a given file at specified date.
        
        Specified by: getConfiguration in interface ItrfVersionProvider
        
        Parameters:
            name (String): EOP file name
            mjd (int): date of the EOP in modified Julian day
        
        Returns:
            configuration valid around specified date in the file
        
        
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

class PythonLOF(LOF):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getName(self) -> str:
        """
        Description copied from interface: getName Get name of the local orbital frame.
        
        Specified by: getName in interface LOF
        
        Returns:
            name of the local orbital frame
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    _rotationFromInertial_0__T = typing.TypeVar('_rotationFromInertial_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rotationFromInertial(self, field: org.hipparchus.Field[_rotationFromInertial_0__T], date: org.orekit.time.FieldAbsoluteDate[_rotationFromInertial_0__T], pv: org.orekit.utils.FieldPVCoordinates[_rotationFromInertial_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_rotationFromInertial_0__T]:
        """
        Description copied from interface: rotationFromInertial Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            date (FieldAbsoluteDate<T> date): date of the rotation
            pv (FieldPVCoordinates<T> pv): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        """
        ...
    @typing.overload
    def rotationFromInertial(self, date: org.orekit.time.AbsoluteDate, pv: org.orekit.utils.PVCoordinates) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Description copied from interface: rotationFromInertial Get the rotation from inertial frame to local orbital frame.
        
        This rotation does not include any time derivatives. If first time derivatives (i.e. rotation rate) is needed as well, the full transformFromInertial method must be called and the complete rotation transform must be extracted from it.
        
        Specified by: rotationFromInertial in interface LOF
        
        Parameters:
            date (AbsoluteDate): date of the rotation
            pv (PVCoordinates): position-velocity of the spacecraft in some inertial frame
        
        Returns:
            rotation from inertial frame to local orbital frame
        
        
        """
        ...

class PythonStaticTransform(StaticTransform):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getInverse(self) -> StaticTransform:
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface StaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Specified by: getRotation in interface StaticTransform
        
        Returns:
            underlying elementary rotation
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Specified by: getTranslation in interface StaticTransform
        
        Returns:
            underlying elementary translation
        
        
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

class PythonTransformProvider(TransformProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
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

class ShiftingTransformProvider(TransformProvider):
    """
    Transform provider using thread-safe shifts on transforms sample.
    
    The shifts take derivatives into account, up to user specified order.
    
    Since:
        7.1
    
    Also see:
        GenericTimeStampedCache, InterpolatingTransformProvider
    """
    def __init__(self, rawProvider: TransformProvider, cFilter: org.orekit.utils.CartesianDerivativesFilter, aFilter: org.orekit.utils.AngularDerivativesFilter, gridPoints: int, step: float, maxSlots: int, maxSpan: float, newSlotInterval: float):
        """
        Simple constructor.
        
        Parameters:
            rawProvider (TransformProvider): provider for raw (non-interpolated) transforms
            cFilter (CartesianDerivativesFilter): filter for derivatives from the sample to use in interpolation
            aFilter (AngularDerivativesFilter): filter for derivatives from the sample to use in interpolation
            gridPoints (int): number of interpolation grid points
            step (double): grid points time step
            maxSlots (int): maximum number of independent cached time slots in the GenericTimeStampedCache
            maxSpan (double): maximum duration span in seconds of one slot in the GenericTimeStampedCache
            newSlotInterval (double): time interval above which a new slot is created in the GenericTimeStampedCache
        
        Since:
            9.1
        
        
        """
        ...
    def getGridPoints(self) -> int:
        """
        Get the number of interpolation grid points.
        
        Returns:
            number of interpolation grid points
        
        
        """
        ...
    def getRawProvider(self) -> TransformProvider:
        """
        Get the underlying provider for raw (non-interpolated) transforms.
        
        Returns:
            provider for raw (non-interpolated) transforms
        
        
        """
        ...
    _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> FieldStaticTransform[_getStaticTransform_0__T]:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the static transform.
        
        
        """
        ...
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> StaticTransform:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation calls getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the static transform.
        
        """
        ...
    def getStep(self) -> float:
        """
        Get the grid points time step.
        
        Returns:
            grid points time step
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> 'FieldTransform'[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class TopocentricFrame(Frame, org.orekit.utils.ExtendedPositionProvider):
    """
    Topocentric frame.
    
    Frame associated to a position near the surface of a body shape.
    
    The origin of the frame is at the defining GeodeticPoint location, and the right-handed canonical trihedra is:
    
      - X axis in the local horizontal plane (normal to zenith direction) and following the local parallel towards East
      - Y axis in the horizontal plane (normal to zenith direction) and following the local meridian towards North
      - Z axis towards Zenith direction
    """
    def __init__(self, parentShape: org.orekit.bodies.BodyShape, point: org.orekit.bodies.GeodeticPoint, name: str):
        """
        Simple constructor.
        
        Parameters:
            parentShape (BodyShape): body shape on which the local point is defined
            point (GeodeticPoint): local surface point where topocentric frame is defined
            name (String): the string representation
        
        
        """
        ...
    def computeLimitVisibilityPoint(self, radius: float, azimuth: float, elevation: float) -> org.orekit.bodies.GeodeticPoint:
        """
        Compute the limit visibility point for a satellite in a given direction.
        
        This method can be used to compute visibility circles around ground stations for example, using a simple loop on azimuth, with either a fixed elevation or an elevation that depends on azimuth to take ground masks into account.
        
        Parameters:
            radius (double): satellite distance to Earth center
            azimuth (double): pointing azimuth from station
            elevation (double): pointing elevation from station
        
        Returns:
            limit visibility point for the satellite
        
        
        """
        ...
    _getAzimuth_1__T = typing.TypeVar('_getAzimuth_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getAzimuth(self, extPoint: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the azimuth of a point with regards to the topocentric frame center point.
        
        The azimuth is the angle between the North direction at local point and the projection in local horizontal plane of the direction from local point to given point. Azimuth angles are counted clockwise, i.e positive towards the East.
        
        Parameters:
            extPoint (Vector3D): point for which elevation shall be computed
            frame (Frame): frame in which the point is defined
            date (AbsoluteDate): computation date
        
        Returns:
            azimuth of the point
        
        """
        ...
    @typing.overload
    def getAzimuth(self, extPoint: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getAzimuth_1__T], frame: Frame, date: org.orekit.time.FieldAbsoluteDate[_getAzimuth_1__T]) -> _getAzimuth_1__T:
        """
        Get the azimuth of a point with regards to the topocentric frame center point.
        
        The azimuth is the angle between the North direction at local point and the projection in local horizontal plane of the direction from local point to given point. Azimuth angles are counted clockwise, i.e positive towards the East.
        
        Parameters:
            extPoint (FieldVector3D<T> extPoint): point for which elevation shall be computed
            frame (Frame): frame in which the point is defined
            date (FieldAbsoluteDate<T> date): computation date
        
        Returns:
            azimuth of the point
        
        Since:
            9.3
        
        
        """
        ...
    def getCartesianPoint(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the surface point defining the origin of the frame.
        
        Returns:
            surface point defining the origin of the frame in body frame
        
        Since:
            12.0
        
        
        """
        ...
    def getEast(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the east direction of topocentric frame, expressed in parent shape frame.
        
        The east direction is defined in the horizontal plane in order to complete direct triangle (east, north, zenith).
        
        Returns:
            unit vector in the east direction
        
        Also see:
            getWest
        
        
        """
        ...
    _getElevation_1__T = typing.TypeVar('_getElevation_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getElevation(self, extPoint: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the elevation of a point with regards to the local point.
        
        The elevation is the angle between the local horizontal and the direction from local point to given point.
        
        Parameters:
            extPoint (Vector3D): point for which elevation shall be computed
            frame (Frame): frame in which the point is defined
            date (AbsoluteDate): computation date
        
        Returns:
            elevation of the point
        
        """
        ...
    @typing.overload
    def getElevation(self, extPoint: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getElevation_1__T], frame: Frame, date: org.orekit.time.FieldAbsoluteDate[_getElevation_1__T]) -> _getElevation_1__T:
        """
        Get the elevation of a point with regards to the local point.
        
        The elevation is the angle between the local horizontal and the direction from local point to given point.
        
        Parameters:
            extPoint (FieldVector3D<T> extPoint): point for which elevation shall be computed
            frame (Frame): frame in which the point is defined
            date (FieldAbsoluteDate<T> date): computation date
        
        Returns:
            elevation of the point
        
        Since:
            9.3
        
        
        """
        ...
    def getNadir(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the nadir direction of topocentric frame, expressed in parent shape frame.
        
        The nadir direction is the opposite of zenith direction.
        
        Returns:
            unit vector in the nadir direction
        
        Also see:
            getZenith
        
        
        """
        ...
    def getNorth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the north direction of topocentric frame, expressed in parent shape frame.
        
        The north direction is defined in the horizontal plane (normal to zenith direction) and following the local meridian.
        
        Returns:
            unit vector in the north direction
        
        Also see:
            getSouth
        
        
        """
        ...
    _getPVCoordinates_0__T = typing.TypeVar('_getPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.FieldAbsoluteDate[_getPVCoordinates_0__T], frame: Frame) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_getPVCoordinates_0__T]:
        """
        Get the position-velocity-acceleration in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position-velocity-acceleration vector
        
        
        """
        ...
    @typing.overload
    def getPVCoordinates(self, date: org.orekit.time.AbsoluteDate, frame: Frame) -> org.orekit.utils.TimeStampedPVCoordinates:
        """
        Get the PVCoordinates of the body in the selected frame.
        
        Specified by: getPVCoordinates in interface ExtendedPositionProvider
        
        Specified by: getPVCoordinates in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            time-stamped position/velocity of the body (m and m/s)
        
        """
        ...
    def getParentShape(self) -> org.orekit.bodies.BodyShape:
        """
        Get the body shape on which the local point is defined.
        
        Returns:
            body shape on which the local point is defined
        
        
        """
        ...
    _getPoint_0__T = typing.TypeVar('_getPoint_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPoint(self, field: org.hipparchus.Field[_getPoint_0__T]) -> org.orekit.bodies.FieldGeodeticPoint[_getPoint_0__T]:
        """
        Get the surface point defining the origin of the frame.
        
        Parameters:
            field (Field<T> field): of the elements
        
        Returns:
            surface point defining the origin of the frame
        
        Since:
            9.3
        
        
        """
        ...
    @typing.overload
    def getPoint(self) -> org.orekit.bodies.GeodeticPoint:
        """
        Get the surface point defining the origin of the frame.
        
        Returns:
            surface point defining the origin of the frame
        
        """
        ...
    _getPosition_0__T = typing.TypeVar('_getPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getPosition(self, date: org.orekit.time.FieldAbsoluteDate[_getPosition_0__T], frame: Frame) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getPosition_0__T]:
        """
        Get the position in the selected frame.
        
        Specified by: getPosition in interface ExtendedPositionProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position
        
        
        """
        ...
    @typing.overload
    def getPosition(self, date: org.orekit.time.AbsoluteDate, frame: Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the position of the body in the selected frame.
        
        Specified by: getPosition in interface PVCoordinatesProvider
        
        Parameters:
            date (AbsoluteDate): current date
            frame (Frame): the frame where to define the position
        
        Returns:
            position of the body (m and)
        
        """
        ...
    _getRange_1__T = typing.TypeVar('_getRange_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getRange(self, extPoint: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the range of a point with regards to the topocentric frame center point.
        
        Parameters:
            extPoint (Vector3D): point for which range shall be computed
            frame (Frame): frame in which the point is defined
            date (AbsoluteDate): computation date
        
        Returns:
            range (distance) of the point
        
        """
        ...
    @typing.overload
    def getRange(self, extPoint: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getRange_1__T], frame: Frame, date: org.orekit.time.FieldAbsoluteDate[_getRange_1__T]) -> _getRange_1__T:
        """
        Get the range of a point with regards to the topocentric frame center point.
        
        Parameters:
            extPoint (FieldVector3D<T> extPoint): point for which range shall be computed
            frame (Frame): frame in which the point is defined
            date (FieldAbsoluteDate<T> date): computation date
        
        Returns:
            range (distance) of the point
        
        Since:
            9.3
        
        
        """
        ...
    _getRangeRate_1__T = typing.TypeVar('_getRangeRate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getRangeRate(self, extPV: org.orekit.utils.PVCoordinates, frame: Frame, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the range rate of a point with regards to the topocentric frame center point.
        
        Parameters:
            extPV (PVCoordinates): point/velocity for which range rate shall be computed
            frame (Frame): frame in which the point is defined
            date (AbsoluteDate): computation date
        
        Returns:
            range rate of the point (positive if point departs from frame)
        
        """
        ...
    @typing.overload
    def getRangeRate(self, extPV: org.orekit.utils.FieldPVCoordinates[_getRangeRate_1__T], frame: Frame, date: org.orekit.time.FieldAbsoluteDate[_getRangeRate_1__T]) -> _getRangeRate_1__T:
        """
        Get the range rate of a point with regards to the topocentric frame center point.
        
        Parameters:
            extPV (FieldPVCoordinates<T> extPV): point/velocity for which range rate shall be computed
            frame (Frame): frame in which the point is defined
            date (FieldAbsoluteDate<T> date): computation date
        
        Returns:
            range rate of the point (positive if point departs from frame)
        
        Since:
            9.3
        
        
        """
        ...
    def getSouth(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the south direction of topocentric frame, expressed in parent shape frame.
        
        The south direction is the opposite of north direction.
        
        Returns:
            unit vector in the south direction
        
        Also see:
            getNorth
        
        
        """
        ...
    _getTopocentricPosition_0__T = typing.TypeVar('_getTopocentricPosition_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getTopocentricPosition(coords: org.orekit.utils.FieldTrackingCoordinates[_getTopocentricPosition_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTopocentricPosition_0__T]:
        """
        Get the topocentric position from FieldTrackingCoordinates.
        
        Parameters:
            coords (FieldTrackingCoordinates<T> coords): The coordinates that are to be converted.
        
        Returns:
            The topocentric coordinates.
        
        Since:
            12.1
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getTopocentricPosition(coords: org.orekit.utils.TrackingCoordinates) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the topocentric position from TrackingCoordinates.
        
        Parameters:
            coords (TrackingCoordinates): The coordinates that are to be converted.
        
        Returns:
            The topocentric coordinates.
        
        Since:
            12.1
        
        """
        ...
    _getTrackingCoordinates_0__T = typing.TypeVar('_getTrackingCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTrackingCoordinates(self, extPoint: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getTrackingCoordinates_0__T], frame: Frame, date: org.orekit.time.FieldAbsoluteDate[_getTrackingCoordinates_0__T]) -> org.orekit.utils.FieldTrackingCoordinates[_getTrackingCoordinates_0__T]:
        """
        Get the tracking coordinates of a point with regards to the local point.
        
        Parameters:
            extPoint (FieldVector3D<T> extPoint): point for which elevation shall be computed
            frame (Frame): frame in which the point is defined
            date (FieldAbsoluteDate<T> date): computation date
        
        Returns:
            tracking coordinates of the point
        
        Since:
            12.0
        
        
        """
        ...
    @typing.overload
    def getTrackingCoordinates(self, extPoint: org.hipparchus.geometry.euclidean.threed.Vector3D, frame: Frame, date: org.orekit.time.AbsoluteDate) -> org.orekit.utils.TrackingCoordinates:
        """
        Get the tracking coordinates of a point with regards to the local point.
        
        Parameters:
            extPoint (Vector3D): point for which elevation shall be computed
            frame (Frame): frame in which the point is defined
            date (AbsoluteDate): computation date
        
        Returns:
            tracking coordinates of the point
        
        Since:
            12.0
        
        """
        ...
    def getVelocity(self, absoluteDate: org.orekit.time.AbsoluteDate, frame: Frame) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    def getWest(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the west direction of topocentric frame, expressed in parent shape frame.
        
        The west direction is the opposite of east direction.
        
        Returns:
            unit vector in the west direction
        
        Also see:
            getEast
        
        
        """
        ...
    def getZenith(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the zenith direction of topocentric frame, expressed in parent shape frame.
        
        The zenith direction is defined as the normal to local horizontal plane.
        
        Returns:
            unit vector in the zenith direction
        
        Also see:
            getNadir
        
        
        """
        ...
    def pointAtDistance(self, azimuth: float, elevation: float, distance: float) -> org.orekit.bodies.GeodeticPoint:
        """
        Compute the point observed from the station at some specified distance.
        
        Parameters:
            azimuth (double): pointing azimuth from station
            elevation (double): pointing elevation from station
            distance (double): distance to station
        
        Returns:
            observed point
        
        
        """
        ...

class TwoBodiesBaryFrame(Frame):
    """
    Class creating the inertial barycenter frame from two bodies.
    
    Since:
        10.2
    """
    def __init__(self, primaryBody: org.orekit.bodies.CelestialBody, secondaryBody: org.orekit.bodies.CelestialBody):
        """
        Simple constructor.
        
        Parameters:
            primaryBody (CelestialBody): Primary body.
            secondaryBody (CelestialBody): Secondary body.
        
        
        """
        ...

class UpdatableFrame(Frame):
    """
    Frame whose transform from its parent can be updated.
    
    This class allows to control the relative position of two parts of the global frames tree using any two frames in each part as control handles. Consider the following simplified frames tree as an example:
    
                  GCRF | -------------------------------- |             |                | Sun        satellite          Earth |                | on-board antenna   ground station | tracking antenna
    
    Tracking measurements really correspond to the link between the ground and on-board antennas. This is tightly linked to the transform between these two frames, however neither frame is the direct parent frame of the other one: the path involves four intermediate frames. When we process a measurement, what we really want to update is the transform that defines the satellite frame with respect to its parent GCRF frame.
    
    In order to implement the above case, the satellite frame is defined as an instance of this class and its updateTransform would be called each time we want to adjust the frame, i.e. each time we get a new measurement between the two antennas.
    """
    @typing.overload
    def __init__(self, frame: Frame, transform: 'Transform', string: str): ...
    @typing.overload
    def __init__(self, frame: Frame, transform: 'Transform', string: str, boolean: bool): ...
    def updateTransform(self, f1: Frame, f2: Frame, f1Tof2: 'Transform', date: org.orekit.time.AbsoluteDate) -> None:
        """
        Update the transform from parent frame implicitly according to two other frames.
        
        This method allows to control the relative position of two parts of the global frames tree using any two frames in each part as control handles. Consider the following simplified frames tree as an example:
        
                      GCRF | -------------------------------- |             |                | Sun        satellite          Earth |                | on-board antenna   ground station | tracking antenna
        
        Tracking measurements really correspond to the link between the ground and on-board antennas. This is tightly linked to the transform between these two frames, however neither frame is the direct parent frame of the other one: the path involves four intermediate frames. When we process a measurement, what we really want to update is the transform that defines the satellite frame with respect to its parent GCRF frame. This is the purpose of this method. This update is done by the following call, where measurementTransform represents the measurement as a simple translation transform between the two antenna frames:
        
        
         satellite.updateTransform(onBoardAntenna, trackingAntenna,
                                   measurementTransform, date);
         
        
        One way to represent the behavior of the method is to consider the sub-tree rooted at the instance on one hand (satellite and on-board antenna in the example above) and the tree containing all the other frames on the other hand (GCRF, Sun, Earth, ground station, tracking antenna). Both tree are considered as two solid sets linked together by a flexible spring, which is the transform we want to update. The method stretches the spring to make sure the transform between the two specified frames (one in each tree part) matches the specified transform.
        
        Parameters:
            f1 (Frame): first control frame (may be the instance itself)
            f2 (Frame): second control frame (may be the instance itself)
            f1Tof2 (Transform): desired transform from first to second control frame
            date (AbsoluteDate): date of the transform
        
        
        """
        ...

class VersionedITRF(Frame):
    """
    Specific version of International Terrestrial Reference Frame.
    
    This class represents an ITRF with a specific version, regardless of the version of the underlying EOPEntry.
    
    Since:
        9.2
    """
    def getITRFVersion(self) -> ITRFVersion:
        """
        Get the ITRF version.
        
        Returns:
            ITRF version
        
        
        """
        ...

_FieldTransform__T = typing.TypeVar('_FieldTransform__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTransform(org.orekit.time.FieldTimeShiftable['FieldTransform'[_FieldTransform__T], _FieldTransform__T], FieldKinematicTransform[_FieldTransform__T], typing.Generic[_FieldTransform__T]):
    """
    Transformation class in three-dimensional space.
    
    This class represents the transformation engine between Frame. It is used both to define the relationship between each frame and its parent frame and to gather all individual transforms into one operation when converting between frames far away from each other.
    
    The convention used in OREKIT is vectorial transformation. It means that a transformation is defined as a transform to apply to the coordinates of a vector expressed in the old frame to obtain the same vector expressed in the new frame.
    
    Instances of this class are guaranteed to be immutable.
    
    Examples
    ----------
    
    Example of translation from R :sub:`A` to R :sub:`B` ------------------------------------------------------
    
    We want to transform the FieldPVCoordinates PV :sub:`A` to PV :sub:`B` with :
    
    PV :sub:`A` = ({1, 0, 0}, {2, 0, 0}, {3, 0, 0});
    
    
    PV :sub:`B` = ({0, 0, 0}, {0, 0, 0}, {0, 0, 0});
    
    The transform to apply then is defined as follows :
    
    
     Vector3D translation  = new Vector3D(-1, 0, 0);
     Vector3D velocity     = new Vector3D(-2, 0, 0);
     Vector3D acceleration = new Vector3D(-3, 0, 0);
    
     Transform R1toR2 = new Transform(date, translation, velocity, acceleration);
    
     PVB = R1toR2.transformPVCoordinate(PVA);
     
    
    Example of rotation from R :sub:`A` to R :sub:`B` ---------------------------------------------------
    
    We want to transform the FieldPVCoordinates PV :sub:`A` to PV :sub:`B` with
    
    PV :sub:`A` = ({1, 0, 0}, { 1, 0, 0});
    
    
    PV :sub:`B` = ({0, 1, 0}, {-2, 1, 0});
    
    The transform to apply then is defined as follows :
    
    
     Rotation rotation = new Rotation(Vector3D.PLUS_K, FastMath.PI / 2);
     Vector3D rotationRate = new Vector3D(0, 0, -2);
    
     Transform R1toR2 = new Transform(rotation, rotationRate);
    
     PVB = R1toR2.transformPVCoordinates(PVA);
     
    
    Since:
        9.0
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_FieldTransform__T], transform: 'Transform'): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldRotation: org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D2: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T], fieldVector3D3: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldTransform: 'FieldTransform'[_FieldTransform__T], fieldTransform2: 'FieldTransform'[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldAngularCoordinates: org.orekit.utils.FieldAngularCoordinates[_FieldTransform__T]): ...
    @typing.overload
    def __init__(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldTransform__T], fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]): ...
    def freeze(self) -> 'FieldTransform'[_FieldTransform__T]:
        """
        Get a frozen transform.
        
        This method creates a copy of the instance but frozen in time, i.e. with velocity, acceleration and rotation rate forced to zero.
        
        Returns:
            a new transform, without any time-dependent parts
        
        
        """
        ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]:
        """
        Get the second time derivative of the translation.
        
        Returns:
            second time derivative of the translation
        
        Also see:
            getCartesian, getTranslation,
            getVelocity
        
        
        """
        ...
    def getAngular(self) -> org.orekit.utils.FieldAngularCoordinates[_FieldTransform__T]:
        """
        Get the underlying elementary angular part.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation with its derivative.
        
        Returns:
            underlying elementary angular part
        
        Also see:
            getRotation, getRotationRate,
            getRotationAcceleration
        
        
        """
        ...
    def getCartesian(self) -> org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]:
        """
        Get the underlying elementary Cartesian part.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation with its derivative.
        
        Returns:
            underlying elementary Cartesian part
        
        Also see:
            getTranslation, getVelocity
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getFieldDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldTransform__T]:
        """
        Get the date.
        
        Specified by: getFieldDate in interface FieldStaticTransform
        
        Returns:
            date attached to the object
        
        
        """
        ...
    _getIdentity__T = typing.TypeVar('_getIdentity__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getIdentity(field: org.hipparchus.Field[_getIdentity__T]) -> 'FieldTransform'[_getIdentity__T]:
        """
        Get the identity transform.
        
        Parameters:
            field (Field<T> field): field for the components
        
        Returns:
            identity transform
        
        
        """
        ...
    def getInverse(self) -> 'FieldTransform'[_FieldTransform__T]:
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface FieldKinematicTransform
        
        Specified by: getInverse in interface FieldStaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getJacobian(self, selector: org.orekit.utils.CartesianDerivativesFilter, jacobian: typing.Union[typing.List[typing.MutableSequence[_FieldTransform__T]], jpype.JArray]) -> None:
        """
        Compute the Jacobian of the transformPVCoordinates method of the transform.
        
        Element jacobian[i][j] is the derivative of Cartesian coordinate i of the transformed FieldPVCoordinates with respect to Cartesian coordinate j of the input FieldPVCoordinates in method transformPVCoordinates.
        
        This definition implies that if we define position-velocity coordinates transformPVCoordinates(PV₀) then their differentials dPV₁ and dPV₀ will obey the following relation where J is the matrix computed by this method: dPV₁ = J × dPV₀
        
        Parameters:
            selector (CartesianDerivativesFilter): selector specifying the size of the upper left corner that must be filled (either 3x3 for positions only, 6x6 for
                positions and velocities, 9x9 for positions, velocities and accelerations)
            jacobian (FieldTransform[][]):             placeholder matrix whose upper-left corner is to be filled with the Jacobian, the rest of the matrix remaining untouched
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_FieldTransform__T]:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Specified by: getRotation in interface FieldStaticTransform
        
        Returns:
            underlying elementary rotation
        
        Also see:
            getAngular, getRotationRate,
            getRotationAcceleration
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]:
        """
        Get the second time derivative of the rotation.
        
        Returns:
            Second time derivative of the rotation
        
        Also see:
            getAngular, getRotation,
            getRotationRate
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]:
        """
        Get the first time derivative of the rotation.
        
        The norm represents the angular rate.
        
        Specified by: getRotationRate in interface FieldKinematicTransform
        
        Returns:
            First time derivative of the rotation
        
        Also see:
            getAngular, getRotation,
            getRotationAcceleration
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Specified by: getTranslation in interface FieldStaticTransform
        
        Returns:
            underlying elementary translation
        
        Also see:
            getCartesian, getVelocity,
            getAcceleration
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldTransform__T]:
        """
        Get the first time derivative of the translation.
        
        Specified by: getVelocity in interface FieldKinematicTransform
        
        Returns:
            first time derivative of the translation
        
        Also see:
            getCartesian, getTranslation,
            getAcceleration
        
        
        """
        ...
    _interpolate_0__T = typing.TypeVar('_interpolate_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_1__T = typing.TypeVar('_interpolate_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _interpolate_2__T = typing.TypeVar('_interpolate_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_0__T], collection: typing.Union[java.util.Collection['FieldTransform'[_interpolate_0__T]], typing.Sequence['FieldTransform'[_interpolate_0__T]], typing.Set['FieldTransform'[_interpolate_0__T]]]) -> 'FieldTransform'[_interpolate_0__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_1__T], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, collection: typing.Union[java.util.Collection['FieldTransform'[_interpolate_1__T]], typing.Sequence['FieldTransform'[_interpolate_1__T]], typing.Set['FieldTransform'[_interpolate_1__T]]]) -> 'FieldTransform'[_interpolate_1__T]: ...
    @typing.overload
    @staticmethod
    def interpolate(fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_interpolate_2__T], cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, stream: java.util.stream.Stream['FieldTransform'[_interpolate_2__T]]) -> 'FieldTransform'[_interpolate_2__T]: ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> _FieldTransform__T: ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'FieldTransform'[_FieldTransform__T]: ...
    @typing.overload
    def shiftedBy(self, t: _FieldTransform__T) -> 'FieldTransform'[_FieldTransform__T]: ...
    def staticShiftedBy(self, dt: _FieldTransform__T) -> FieldStaticTransform[_FieldTransform__T]:
        """
        Shift the transform in time considering all rates, then return only the translation and rotation portion of the transform.
        
        Parameters:
            dt (FieldTransform): time shift in seconds.
        
        Returns:
            shifted transform as a static transform. It is static in the sense that it can only be used to transform directions and
            positions, but not velocities or accelerations.
        
        Also see:
            shiftedBy
        
        
        """
        ...
    def toStaticTransform(self) -> FieldStaticTransform[_FieldTransform__T]:
        """
        Create a so-called static transform from the instance.
        
        Returns:
            static part of the transform. It is static in the sense that it can only be used to transform directions and positions,
            but not velocities or accelerations.
        
        Also see:
            FieldStaticTransform
        
        
        """
        ...
    @typing.overload
    def transformPVCoordinates(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]) -> org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.orekit.utils.FieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTransform__T]) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTransform__T]: ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_FieldTransform__T]: ...

class GTODProvider(EOPBasedTransformProvider):
    """
    Greenwich True Of Date Frame, also known as True of Date Rotating frame (TDR) or Greenwich Rotating Coordinate frame (GCR).
    
    This frame handles the sidereal time according to IAU-82 model.
    
    Its parent frame is the TODProvider.
    
    The pole motion is not applied here.
    """
    def getEOPHistory(self) -> EOPHistory:
        """
        Get the EOP history.
        
        Specified by: getEOPHistory in interface EOPBasedTransformProvider
        
        Returns:
            EOP history
        
        
        """
        ...
    _getKinematicTransform_0__T = typing.TypeVar('_getKinematicTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getKinematicTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getKinematicTransform_0__T]) -> FieldKinematicTransform[_getKinematicTransform_0__T]:
        """
        Get a transform for position and velocity, not acceleration.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getKinematicTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the kinematic transform.
        
        
        """
        ...
    @typing.overload
    def getKinematicTransform(self, date: org.orekit.time.AbsoluteDate) -> KinematicTransform:
        """
        Get a transform for position and velocity, not acceleration.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getKinematicTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the kinematic transform.
        
        """
        ...
    def getNonInterpolatingProvider(self) -> 'GTODProvider':
        """
        Get a version of the provider that does not cache tidal corrections.
        
        This method removes the performance enhancing interpolation features that are used by default in EOP-based provider, in order to focus on accuracy. The interpolation features are intended to save processing time by avoiding doing tidal correction evaluation at each time step and caching some results. This method can be used to avoid this (it is automatically called by getNonInterpolatingTransform, when very high accuracy is desired, or for testing purposes. It should be used with care, as doing the full computation is really costly.
        
        Specified by: getNonInterpolatingProvider in interface EOPBasedTransformProvider
        
        Returns:
            version of the provider that does not cache tidal corrections
        
        Also see:
            getNonInterpolatingTransform
        
        
        """
        ...
    _getStaticTransform_0__T = typing.TypeVar('_getStaticTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getStaticTransform_0__T]) -> FieldStaticTransform[_getStaticTransform_0__T]:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation returns getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date.
        
        Returns:
            the static transform.
        
        
        """
        ...
    @typing.overload
    def getStaticTransform(self, date: org.orekit.time.AbsoluteDate) -> StaticTransform:
        """
        Get a transform for only rotations and translations on the specified date.
        
        The default implementation calls getTransform but implementations may override it for better performance.
        
        Specified by: getStaticTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date.
        
        Returns:
            the static transform.
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
        """
        ...

class LazyLoadedFrames(AbstractFrames):
    """
    This class lazily loads auxiliary data when it is needed by a requested frame. It is designed to match the behavior of FramesFactory in Orekit 10.0.
    
    Since:
        10.1
    
    Also see:
        LazyLoadedEop
    """
    def __init__(self, lazyLoadedEop: LazyLoadedEop, timeScales: org.orekit.time.TimeScales, celestialBodies: org.orekit.bodies.CelestialBodies):
        """
        Create a collection of frames from the given auxiliary data.
        
        Parameters:
            lazyLoadedEop (LazyLoadedEop): loads Earth Orientation Parameters.
            timeScales (TimeScales): defines the time scales used when computing frame transformations. For example, the TT time scale needed for
                getPZ9011.
            celestialBodies (CelestialBodies): defines the celestial bodies which, for example, are used in getICRF.
        
        
        """
        ...
    def addDefaultEOP1980HistoryLoaders(self, rapidDataColumnsSupportedNames: str, xmlSupportedNames: str, eopC04SupportedNames: str, bulletinBSupportedNames: str, bulletinASupportedNames: str, csvSupportedNames: str) -> None:
        """
        Add the default loaders EOP history (IAU 1980 precession/nutation).
        
        The default loaders look for IERS EOP C04 and bulletins B files. They correspond to IERS_1996 conventions.
        
        Parameters:
            rapidDataColumnsSupportedNames (String): regular expression for supported rapid data columns EOP files names (may be null if the default IERS file names are
                used)
            xmlSupportedNames (String): regular expression for supported XML EOP files names (may be null if the default IERS file names are used)
            eopC04SupportedNames (String): regular expression for supported EOP C04 files names (may be null if the default IERS file names are used)
            bulletinBSupportedNames (String): regular expression for supported bulletin B files names (may be null if the default IERS file names are used)
            bulletinASupportedNames (String): regular expression for supported bulletin A files names (may be null if the default IERS file names are used)
            csvSupportedNames (String): regular expression for supported csv files names (may be null if the default IERS file names are used)
        
        Since:
            12.0
        
        Also see:
            eop,
            addEOPHistoryLoader,
            clearEOPHistoryLoaders,
            addDefaultEOP2000HistoryLoaders
        
        
        """
        ...
    def addDefaultEOP2000HistoryLoaders(self, rapidDataColumnsSupportedNames: str, xmlSupportedNames: str, eopC04SupportedNames: str, bulletinBSupportedNames: str, bulletinASupportedNames: str, csvSupportedNames: str) -> None:
        """
        Add the default loaders for EOP history (IAU 2000/2006 precession/nutation).
        
        The default loaders look for IERS EOP C04 and bulletins B files. They correspond to both IERS_2003 and IERS_2010 conventions.
        
        Parameters:
            rapidDataColumnsSupportedNames (String): regular expression for supported rapid data columns EOP files names (may be null if the default IERS file names are
                used)
            xmlSupportedNames (String): regular expression for supported XML EOP files names (may be null if the default IERS file names are used)
            eopC04SupportedNames (String): regular expression for supported EOP C04 files names (may be null if the default IERS file names are used)
            bulletinBSupportedNames (String): regular expression for supported bulletin B files names (may be null if the default IERS file names are used)
            bulletinASupportedNames (String): regular expression for supported bulletin A files names (may be null if the default IERS file names are used)
            csvSupportedNames (String): regular expression for supported csv files names (may be null if the default IERS file names are used)
        
        Since:
            12.0
        
        Also see:
            eop,
            addEOPHistoryLoader,
            clearEOPHistoryLoaders,
            addDefaultEOP1980HistoryLoaders
        
        
        """
        ...
    def addEOPHistoryLoader(self, conventions: org.orekit.utils.IERSConventions, loader: typing.Union[EopHistoryLoader, typing.Callable]) -> None:
        """
        Add a loader for Earth Orientation Parameters history.
        
        Parameters:
            conventions (IERSConventions): IERS conventions to which EOP history applies
            loader (EopHistoryLoader): custom loader to add for the EOP history
        
        Also see:
            addDefaultEOP1980HistoryLoaders,
            clearEOPHistoryLoaders
        
        
        """
        ...
    def clearEOPHistoryLoaders(self) -> None:
        """
        Clear loaders for Earth Orientation Parameters history.
        
        Also see:
            addEOPHistoryLoader,
            addDefaultEOP1980HistoryLoaders
        
        
        """
        ...
    def getEOPHistory(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> EOPHistory:
        """
        Get Earth Orientation Parameters history.
        
        If no EopHistoryLoader has been added by calling addEOPHistoryLoader or if clearEOPHistoryLoaders has been called afterwards, the addDefaultEOP1980HistoryLoaders and addDefaultEOP2000HistoryLoaders methods will be called automatically with supported file names parameters all set to null, in order to get the default loaders configuration.
        
        Parameters:
            conventions (IERSConventions): conventions for which EOP history is requested
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Earth Orientation Parameters history
        
        
        """
        ...
    def setEOPContinuityThreshold(self, threshold: float) -> None:
        """
        Set the threshold to check EOP continuity.
        
        The default threshold (used if this method is never called) is 5 Julian days. If after loading EOP entries some holes between entries exceed this threshold, an exception will be triggered.
        
        One case when calling this method is really useful is for applications that use a single Bulletin A, as these bulletins have a roughly one month wide hole for the first bulletin of each month, which contains older final data in addition to the rapid data and the predicted data.
        
        Parameters:
            threshold (double): threshold to use for checking EOP continuity (in seconds)
        
        
        """
        ...

class PythonAbstractFrames(AbstractFrames):
    def __init__(self, timeScales: org.orekit.time.TimeScales, icrfSupplier: typing.Union[java.util.function.Supplier[Frame], typing.Callable[[], Frame]]):
        """
        Simple constructor.
        
        Parameters:
            timeScales (TimeScales): to use when creating frames.
            icrfSupplier (Supplier<Frame> icrfSupplier): used to implement getICRF;
        
        
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
    def getEOPHistory(self, conventions: org.orekit.utils.IERSConventions, simpleEOP: bool) -> EOPHistory:
        """
        Get Earth Orientation Parameters history.
        
        Parameters:
            conventions (IERSConventions): conventions for which EOP history is requested
            simpleEOP (boolean): if true, tidal effects are ignored when interpolating EOP
        
        Returns:
            Earth Orientation Parameters history
        
        
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

class PythonEOPBasedTransformProvider(EOPBasedTransformProvider):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getEOPHistory(self) -> EOPHistory:
        """
        Get the EOP history.
        
        Specified by: getEOPHistory in interface EOPBasedTransformProvider
        
        Returns:
            EOP history
        
        
        """
        ...
    def getNonInterpolatingProvider(self) -> EOPBasedTransformProvider:
        """
        Get a version of the provider that does not cache tidal corrections.
        
        This method removes the performance enhancing interpolation features that are used by default in EOP-based provider, in order to focus on accuracy. The interpolation features are intended to save processing time by avoiding doing tidal correction evaluation at each time step and caching some results. This method can be used to avoid this (it is automatically called by getNonInterpolatingTransform, when very high accuracy is desired, or for testing purposes. It should be used with care, as doing the full computation is really costly.
        
        Specified by: getNonInterpolatingProvider in interface EOPBasedTransformProvider
        
        Returns:
            version of the provider that does not cache tidal corrections
        
        Also see:
            getNonInterpolatingTransform
        
        
        """
        ...
    _getTransform_0__T = typing.TypeVar('_getTransform_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def getTransform(self, date: org.orekit.time.FieldAbsoluteDate[_getTransform_0__T]) -> FieldTransform[_getTransform_0__T]:
        """
        Get the FieldTransform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (FieldAbsoluteDate<T> date): current date
        
        Returns:
            transform at specified date
        
        
        """
        ...
    @typing.overload
    def getTransform(self, date: org.orekit.time.AbsoluteDate) -> 'Transform':
        """
        Get the Transform corresponding to specified date.
        
        Specified by: getTransform in interface TransformProvider
        
        Parameters:
            date (AbsoluteDate): current date
        
        Returns:
            transform at specified date
        
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

_PythonFieldKinematicTransform__T = typing.TypeVar('_PythonFieldKinematicTransform__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldKinematicTransform(FieldKinematicTransform[_PythonFieldKinematicTransform__T], typing.Generic[_PythonFieldKinematicTransform__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getInverse(self) -> FieldKinematicTransform[_PythonFieldKinematicTransform__T]:
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface FieldKinematicTransform
        
        Specified by: getInverse in interface FieldStaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.FieldRotation[_PythonFieldKinematicTransform__T]:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Specified by: getRotation in interface FieldStaticTransform
        
        Returns:
            underlying elementary rotation
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_PythonFieldKinematicTransform__T]:
        """
        Get the first time derivative of the rotation.
        
        The norm represents the angular rate.
        
        Specified by: getRotationRate in interface FieldKinematicTransform
        
        Returns:
            First time derivative of the rotation
        
        Also see:
            getRotation
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_PythonFieldKinematicTransform__T]:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Specified by: getTranslation in interface FieldStaticTransform
        
        Returns:
            underlying elementary translation
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_PythonFieldKinematicTransform__T]:
        """
        Get the first time derivative of the translation.
        
        Specified by: getVelocity in interface FieldKinematicTransform
        
        Returns:
            first time derivative of the translation
        
        Also see:
            getTranslation
        
        
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

class PythonKinematicTransform(KinematicTransform):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getInverse(self) -> KinematicTransform:
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface KinematicTransform
        
        Specified by: getInverse in interface StaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Specified by: getRotation in interface StaticTransform
        
        Returns:
            underlying elementary rotation
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the first time derivative of the rotation.
        
        The norm represents the angular rate.
        
        Specified by: getRotationRate in interface KinematicTransform
        
        Returns:
            First time derivative of the rotation
        
        Also see:
            getRotation
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Specified by: getTranslation in interface StaticTransform
        
        Returns:
            underlying elementary translation
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the first time derivative of the translation.
        
        Specified by: getVelocity in interface KinematicTransform
        
        Returns:
            first time derivative of the translation
        
        Also see:
            getTranslation
        
        
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

class Transform(org.orekit.time.TimeShiftable['Transform'], KinematicTransform):
    """
    Transformation class in three dimensional space.
    
    This class represents the transformation engine between Frame. It is used both to define the relationship between each frame and its parent frame and to gather all individual transforms into one operation when converting between frames far away from each other.
    
    The convention used in OREKIT is vectorial transformation. It means that a transformation is defined as a transform to apply to the coordinates of a vector expressed in the old frame to obtain the same vector expressed in the new frame.
    
    Instances of this class are guaranteed to be immutable.
    
    Examples
    ----------
    
    Example of translation from R :sub:`A` to R :sub:`B` ------------------------------------------------------
    
    We want to transform the PVCoordinates PV :sub:`A` to PV :sub:`B` with :
    
    PV :sub:`A` = ({1, 0, 0}, {2, 0, 0}, {3, 0, 0});
    
    
    PV :sub:`B` = ({0, 0, 0}, {0, 0, 0}, {0, 0, 0});
    
    The transform to apply then is defined as follows :
    
    
     Vector3D translation  = new Vector3D(-1, 0, 0);
     Vector3D velocity     = new Vector3D(-2, 0, 0);
     Vector3D acceleration = new Vector3D(-3, 0, 0);
    
     Transform R1toR2 = new Transform(date, translation, velocity, acceleration);
    
     PVB = R1toR2.transformPVCoordinates(PVA);
     
    
    Example of rotation from R :sub:`A` to R :sub:`B` ---------------------------------------------------
    
    We want to transform the PVCoordinates PV :sub:`A` to PV :sub:`B` with
    
    PV :sub:`A` = ({1, 0, 0}, { 1, 0, 0});
    
    
    PV :sub:`B` = ({0, 1, 0}, {-2, 1, 0});
    
    The transform to apply then is defined as follows :
    
    
     Rotation rotation = new Rotation(Vector3D.PLUS_K, FastMath.PI / 2);
     Vector3D rotationRate = new Vector3D(0, 0, -2);
    
     Transform R1toR2 = new Transform(rotation, rotationRate);
    
     PVB = R1toR2.transformPVCoordinates(PVA);
    """
    IDENTITY: typing.ClassVar['Transform'] = ...
    """
    Identity transform.
    """
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, rotation: org.hipparchus.geometry.euclidean.threed.Rotation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, rotation: org.hipparchus.geometry.euclidean.threed.Rotation): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, transform: 'Transform', transform2: 'Transform'): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, angularCoordinates: org.orekit.utils.AngularCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates): ...
    @typing.overload
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, pVCoordinates: org.orekit.utils.PVCoordinates, angularCoordinates: org.orekit.utils.AngularCoordinates): ...
    def freeze(self) -> 'Transform':
        """
        Get a frozen transform.
        
        This method creates a copy of the instance but frozen in time, i.e. with velocity, acceleration and rotation rate forced to zero.
        
        Returns:
            a new transform, without any time-dependent parts
        
        
        """
        ...
    def getAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the second time derivative of the translation.
        
        Returns:
            second time derivative of the translation
        
        Also see:
            getCartesian, getTranslation,
            getVelocity
        
        
        """
        ...
    def getAngular(self) -> org.orekit.utils.AngularCoordinates:
        """
        Get the underlying elementary angular part.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation with its derivative.
        
        Returns:
            underlying elementary angular part
        
        Also see:
            getRotation, getRotationRate,
            getRotationAcceleration
        
        
        """
        ...
    def getCartesian(self) -> org.orekit.utils.PVCoordinates:
        """
        Get the underlying elementary Cartesian part.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation with its derivative.
        
        Returns:
            underlying elementary Cartesian part
        
        Also see:
            getTranslation, getVelocity
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
        Get the date.
        
        Specified by: getDate in interface TimeStamped
        
        Returns:
            date attached to the object
        
        
        """
        ...
    def getInverse(self) -> 'Transform':
        """
        Get the inverse transform of the instance.
        
        Specified by: getInverse in interface KinematicTransform
        
        Specified by: getInverse in interface StaticTransform
        
        Returns:
            inverse transform of the instance
        
        
        """
        ...
    def getJacobian(self, selector: org.orekit.utils.CartesianDerivativesFilter, jacobian: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
        Compute the Jacobian of the transformPVCoordinates method of the transform.
        
        Element jacobian[i][j] is the derivative of Cartesian coordinate i of the transformed PVCoordinates with respect to Cartesian coordinate j of the input PVCoordinates in method transformPVCoordinates.
        
        This definition implies that if we define position-velocity coordinates
        
         PV₁ = transform.transformPVCoordinates(PV₀), then
        
        their differentials dPV₁ and dPV₀ will obey the following relation where J is the matrix computed by this method:
        
         dPV₁ = J × dPV₀
        
        Parameters:
            selector (CartesianDerivativesFilter): selector specifying the size of the upper left corner that must be filled (either 3x3 for positions only, 6x6 for
                positions and velocities, 9x9 for positions, velocities and accelerations)
            jacobian (double[][]):             placeholder matrix whose upper-left corner is to be filled with the Jacobian, the rest of the matrix remaining untouched
        
        
        """
        ...
    def getRotation(self) -> org.hipparchus.geometry.euclidean.threed.Rotation:
        """
        Get the underlying elementary rotation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary rotation.
        
        Specified by: getRotation in interface StaticTransform
        
        Returns:
            underlying elementary rotation
        
        Also see:
            getAngular, getRotationRate,
            getRotationAcceleration
        
        
        """
        ...
    def getRotationAcceleration(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the second time derivative of the rotation.
        
        Returns:
            Second time derivative of the rotation
        
        Also see:
            getAngular, getRotation,
            getRotationRate
        
        
        """
        ...
    def getRotationRate(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the first time derivative of the rotation.
        
        The norm represents the angular rate.
        
        Specified by: getRotationRate in interface KinematicTransform
        
        Returns:
            First time derivative of the rotation
        
        Also see:
            getAngular, getRotation,
            getRotationAcceleration
        
        
        """
        ...
    def getTranslation(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the underlying elementary translation.
        
        A transform can be uniquely represented as an elementary translation followed by an elementary rotation. This method returns this unique elementary translation.
        
        Specified by: getTranslation in interface StaticTransform
        
        Returns:
            underlying elementary translation
        
        Also see:
            getCartesian, getVelocity,
            getAcceleration
        
        
        """
        ...
    def getVelocity(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the first time derivative of the translation.
        
        Specified by: getVelocity in interface KinematicTransform
        
        Returns:
            first time derivative of the translation
        
        Also see:
            getCartesian, getTranslation,
            getAcceleration
        
        
        """
        ...
    @typing.overload
    def interpolate(self, absoluteDate: org.orekit.time.AbsoluteDate, stream: java.util.stream.Stream['Transform']) -> 'Transform': ...
    @typing.overload
    @staticmethod
    def interpolate(absoluteDate: org.orekit.time.AbsoluteDate, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, collection: typing.Union[java.util.Collection['Transform'], typing.Sequence['Transform'], typing.Set['Transform']]) -> 'Transform': ...
    @typing.overload
    def shiftedBy(self, double: float) -> 'Transform':
        """
        Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (double): time shift in seconds
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        Get a time-shifted instance.
        
        Specified by: shiftedBy in interface TimeShiftable
        
        Parameters:
            dt (TimeOffset): time shift
        
        Returns:
            a new instance, shifted with respect to instance (which is not changed)
        
        
        """
        ...
    @typing.overload
    def shiftedBy(self, timeOffset: org.orekit.time.TimeOffset) -> 'Transform': ...
    def staticShiftedBy(self, dt: float) -> StaticTransform:
        """
        Shift the transform in time considering all rates, then return only the translation and rotation portion of the transform.
        
        Parameters:
            dt (double): time shift in seconds.
        
        Returns:
            shifted transform as a static transform. It is static in the sense that it can only be used to transform directions and
            positions, but not velocities or accelerations.
        
        Also see:
            shiftedBy
        
        
        """
        ...
    def toStaticTransform(self) -> StaticTransform:
        """
        Create a so-called static transform from the instance.
        
        Returns:
            static part of the transform. It is static in the sense that it can only be used to transform directions and positions,
            but not velocities or accelerations.
        
        Also see:
            StaticTransform
        
        
        """
        ...
    _transformPVCoordinates_0__T = typing.TypeVar('_transformPVCoordinates_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _transformPVCoordinates_2__T = typing.TypeVar('_transformPVCoordinates_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def transformPVCoordinates(self, fieldPVCoordinates: org.orekit.utils.FieldPVCoordinates[_transformPVCoordinates_0__T]) -> org.orekit.utils.FieldPVCoordinates[_transformPVCoordinates_0__T]:
        """
        Transform FieldPVCoordinates including kinematic effects.
        
        Parameters:
            pv (FieldPVCoordinates<T> pv): position-velocity to transform.
        
        Returns:
            transformed position-velocity
        
        Transform TimeStampedFieldPVCoordinates including kinematic effects.
        
        In order to allow the user more flexibility, this method does not check for consistency between the transform getDate and the time-stamped position-velocity getDate. The returned value will always have the same getDate as the input argument, regardless of the instance getDate.
        
        Parameters:
            pv (TimeStampedFieldPVCoordinates<T> pv): time-stamped position-velocity to transform.
        
        Returns:
            transformed time-stamped position-velocity
        
        Since:
            7.0
        
        
        """
        ...
    @typing.overload
    def transformPVCoordinates(self, pVCoordinates: org.orekit.utils.PVCoordinates) -> org.orekit.utils.PVCoordinates:
        """
        Transform PVCoordinates including kinematic effects.
        
        Parameters:
            pva (PVCoordinates): the position-velocity-acceleration triplet to transform.
        
        Returns:
            transformed position-velocity-acceleration
        
        Transform TimeStampedPVCoordinates including kinematic effects.
        
        In order to allow the user more flexibility, this method does not check for consistency between the transform getDate and the time-stamped position-velocity getDate. The returned value will always have the same getDate as the input argument, regardless of the instance getDate.
        
        Parameters:
            pv (TimeStampedPVCoordinates): time-stamped position-velocity to transform.
        
        Returns:
            transformed time-stamped position-velocity
        
        Since:
            7.0
        
        """
        ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedFieldPVCoordinates: org.orekit.utils.TimeStampedFieldPVCoordinates[_transformPVCoordinates_2__T]) -> org.orekit.utils.TimeStampedFieldPVCoordinates[_transformPVCoordinates_2__T]: ...
    @typing.overload
    def transformPVCoordinates(self, timeStampedPVCoordinates: org.orekit.utils.TimeStampedPVCoordinates) -> org.orekit.utils.TimeStampedPVCoordinates: ...

class PythonAbstractEopParser(org.orekit.frames.AbstractEopParser):
    def __init__(self, converter: org.orekit.utils.IERSConventions.NutationCorrectionConverter, itrfVersionProvider: typing.Union[ItrfVersionProvider, typing.Callable], utc: org.orekit.time.TimeScale):
        """
        Simple constructor.
        
        Parameters:
            converter (NutationCorrectionConverter): converter to use
            itrfVersionProvider (ItrfVersionProvider): to use for determining the ITRF version of the EOP.
            utc (TimeScale): time scale for parsing dates.
        
        
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
    def parse(self, input: java.io.InputStream, name: str) -> java.util.Collection[EOPEntry]:
        """
        Parse EOP from the given input stream.
        
        Parameters:
            input (InputStream): stream to parse.
            name (String): of the stream for error messages.
        
        Returns:
            parsed EOP entries.
        
        Raises:
            IOException: if input throws one during parsing. TODO: Unclear what is reasonable to expose here.
        
        
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

class AbstractEopParser: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.frames")``.

    AbstractEopLoader: typing.Type[AbstractEopLoader]
    AbstractEopParser: typing.Type[AbstractEopParser]
    AbstractFrames: typing.Type[AbstractFrames]
    CR3BPRotatingFrame: typing.Type[CR3BPRotatingFrame]
    CachedTransformProvider: typing.Type[CachedTransformProvider]
    EOPBasedTransformProvider: typing.Type[EOPBasedTransformProvider]
    EOPEntry: typing.Type[EOPEntry]
    EOPFittedModel: typing.Type[EOPFittedModel]
    EOPFitter: typing.Type[EOPFitter]
    EOPHistory: typing.Type[EOPHistory]
    EclipticProvider: typing.Type[EclipticProvider]
    EopDataType: typing.Type[EopDataType]
    EopHistoryLoader: typing.Type[EopHistoryLoader]
    FactoryManagedFrame: typing.Type[FactoryManagedFrame]
    FieldCachedTransformProvider: typing.Type[FieldCachedTransformProvider]
    FieldKinematicTransform: typing.Type[FieldKinematicTransform]
    FieldPoleCorrection: typing.Type[FieldPoleCorrection]
    FieldStaticTransform: typing.Type[FieldStaticTransform]
    FieldTransform: typing.Type[FieldTransform]
    FieldTransformGenerator: typing.Type[FieldTransformGenerator]
    FixedTransformProvider: typing.Type[FixedTransformProvider]
    Frame: typing.Type[Frame]
    Frames: typing.Type[Frames]
    FramesFactory: typing.Type[FramesFactory]
    GTODProvider: typing.Type[GTODProvider]
    HelmertTransformation: typing.Type[HelmertTransformation]
    ITRFVersion: typing.Type[ITRFVersion]
    ITRFVersionLoader: typing.Type[ITRFVersionLoader]
    InterpolatingTransformProvider: typing.Type[InterpolatingTransformProvider]
    ItrfVersionProvider: typing.Type[ItrfVersionProvider]
    KinematicTransform: typing.Type[KinematicTransform]
    L1Frame: typing.Type[L1Frame]
    L1TransformProvider: typing.Type[L1TransformProvider]
    L2Frame: typing.Type[L2Frame]
    LOF: typing.Type[LOF]
    LOFType: typing.Type[LOFType]
    LazyLoadedEop: typing.Type[LazyLoadedEop]
    LazyLoadedFrames: typing.Type[LazyLoadedFrames]
    LocalMagneticFieldFrame: typing.Type[LocalMagneticFieldFrame]
    LocalOrbitalFrame: typing.Type[LocalOrbitalFrame]
    OrphanFrame: typing.Type[OrphanFrame]
    PoleCorrection: typing.Type[PoleCorrection]
    Predefined: typing.Type[Predefined]
    PredictedEOPHistory: typing.Type[PredictedEOPHistory]
    PythonAbstractEopParser: typing.Type[PythonAbstractEopParser]
    PythonAbstractFrames: typing.Type[PythonAbstractFrames]
    PythonEOPBasedTransformProvider: typing.Type[PythonEOPBasedTransformProvider]
    PythonEOPHistoryLoader: typing.Type[PythonEOPHistoryLoader]
    PythonFieldKinematicTransform: typing.Type[PythonFieldKinematicTransform]
    PythonFieldStaticTransform: typing.Type[PythonFieldStaticTransform]
    PythonFrames: typing.Type[PythonFrames]
    PythonItrfVersionProvider: typing.Type[PythonItrfVersionProvider]
    PythonKinematicTransform: typing.Type[PythonKinematicTransform]
    PythonLOF: typing.Type[PythonLOF]
    PythonStaticTransform: typing.Type[PythonStaticTransform]
    PythonTransformProvider: typing.Type[PythonTransformProvider]
    ShiftingTransformProvider: typing.Type[ShiftingTransformProvider]
    SingleParameterFitter: typing.Type[SingleParameterFitter]
    StaticTransform: typing.Type[StaticTransform]
    TopocentricFrame: typing.Type[TopocentricFrame]
    Transform: typing.Type[Transform]
    TransformGenerator: typing.Type[TransformGenerator]
    TransformProvider: typing.Type[TransformProvider]
    TransformProviderUtils: typing.Type[TransformProviderUtils]
    TwoBodiesBaryFrame: typing.Type[TwoBodiesBaryFrame]
    UpdatableFrame: typing.Type[UpdatableFrame]
    VersionedITRF: typing.Type[VersionedITRF]
    encounter: org.orekit.frames.encounter.__module_protocol__
