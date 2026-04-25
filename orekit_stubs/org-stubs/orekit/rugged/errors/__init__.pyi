
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import jpype.protocol
import org.hipparchus.exception
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.rugged.api
import org.orekit.rugged.linesensor
import org.orekit.rugged.raster
import org.orekit.rugged.utils
import org.orekit.time
import typing



class DumpManager:
    """
    Class managing debug dumps.
    
    WARNING: this class is public only for technical reasons, it is not considered to belong to the public API of the library and should not be called by user code. It is only intended to be called internally by the Rugged library itself. This class may be changed or even removed at any time, so user code should not rely on it.
    """
    @staticmethod
    def activate(file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None:
        """
        Activate debug dump.
        
        Parameters:
            file (File): dump file
        
        
        """
        ...
    @staticmethod
    def deactivate() -> None:
        """
        Deactivate debug dump.
        """
        ...
    @typing.overload
    @staticmethod
    def dumpAlgorithm(algorithmId: org.orekit.rugged.api.AlgorithmId) -> None:
        """
        Dump algorithm data.
        
        Parameters:
            algorithmId (AlgorithmId): algorithm ID
        
        Dump algorithm data.
        
        Parameters:
            algorithmId (AlgorithmId): algorithm ID
            specific (double): algorithm specific extra data
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def dumpAlgorithm(algorithmId: org.orekit.rugged.api.AlgorithmId, double: float) -> None: ...
    @staticmethod
    def dumpDirectLocation(date: org.orekit.time.AbsoluteDate, sensorPosition: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.hipparchus.geometry.euclidean.threed.Vector3D, lightTimeCorrection: bool, aberrationOfLightCorrection: bool, refractionCorrection: bool) -> None:
        """
        Dump a direct location computation.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date of the location
            sensorPosition (org.hipparchus.geometry.euclidean.threed.Vector3D): sensor position in spacecraft frame
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): normalized line-of-sight in spacecraft frame
            lightTimeCorrection (boolean): flag for light time correction
            aberrationOfLightCorrection (boolean): flag for aberration of light correction
            refractionCorrection (boolean): flag for refraction correction
        
        
        """
        ...
    @staticmethod
    def dumpDirectLocationResult(gp: org.orekit.bodies.GeodeticPoint) -> None:
        """
        Dump a direct location result.
        
        Parameters:
            gp (org.orekit.bodies.GeodeticPoint): resulting geodetic point
        
        
        """
        ...
    @staticmethod
    def dumpEllipsoid(ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid) -> None:
        """
        Dump ellipsoid data.
        
        Parameters:
            ellipsoid (ExtendedEllipsoid): ellipsoid to dump
        
        
        """
        ...
    @staticmethod
    def dumpInverseLocation(sensor: org.orekit.rugged.linesensor.LineSensor, point: org.orekit.bodies.GeodeticPoint, ellipsoid: org.orekit.rugged.utils.ExtendedEllipsoid, minLine: int, maxLine: int, lightTimeCorrection: bool, aberrationOfLightCorrection: bool, refractionCorrection: bool) -> None:
        """
        Dump an inverse location computation.
        
        Parameters:
            sensor (LineSensor): sensor
            point (org.orekit.bodies.GeodeticPoint): point to localize
            ellipsoid (ExtendedEllipsoid): the used ellipsoid
            minLine (int): minimum line number
            maxLine (int): maximum line number
            lightTimeCorrection (boolean): flag for light time correction
            aberrationOfLightCorrection (boolean): flag for aberration of light correction
            refractionCorrection (boolean): flag for refraction correction
        
        
        """
        ...
    @staticmethod
    def dumpInverseLocationResult(pixel: org.orekit.rugged.linesensor.SensorPixel) -> None:
        """
        Dump an inverse location result.
        
        Parameters:
            pixel (SensorPixel): resulting sensor pixel
        
        
        """
        ...
    @staticmethod
    def dumpSensorDatation(sensor: org.orekit.rugged.linesensor.LineSensor, lineNumber: float, date: org.orekit.time.AbsoluteDate) -> None:
        """
        Dump a sensor datation.
        
        Parameters:
            sensor (LineSensor): sensor
            lineNumber (double): line number
            date (org.orekit.time.AbsoluteDate): date
        
        
        """
        ...
    @staticmethod
    def dumpSensorLOS(sensor: org.orekit.rugged.linesensor.LineSensor, date: org.orekit.time.AbsoluteDate, i: int, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> None:
        """
        Dump a sensor LOS.
        
        Parameters:
            sensor (LineSensor): sensor
            date (org.orekit.time.AbsoluteDate): date
            i (int): pixel index
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): pixel normalized line-of-sight
        
        
        """
        ...
    @staticmethod
    def dumpSensorMeanPlane(meanPlane: org.orekit.rugged.linesensor.SensorMeanPlaneCrossing) -> None:
        """
        Dump a sensor mean plane.
        
        Parameters:
            meanPlane (SensorMeanPlaneCrossing): mean plane associated with sensor
        
        
        """
        ...
    @staticmethod
    def dumpSensorRate(sensor: org.orekit.rugged.linesensor.LineSensor, lineNumber: float, rate: float) -> None:
        """
        Dump a sensor rate.
        
        Parameters:
            sensor (LineSensor): sensor
            lineNumber (double): line number
            rate (double): lines rate
        
        
        """
        ...
    @staticmethod
    def dumpTileCell(tile: org.orekit.rugged.raster.Tile, latitudeIndex: int, longitudeIndex: int, elevation: float) -> None:
        """
        Dump DEM cell data.
        
        Parameters:
            tile (Tile): tile to which the cell belongs
            latitudeIndex (int): latitude index of the cell
            longitudeIndex (int): longitude index of the cell
            elevation (double): elevation of the cell
        
        
        """
        ...
    @staticmethod
    def dumpTransform(scToBody: org.orekit.rugged.utils.SpacecraftToObservedBody, index: int, bodyToInertial: org.orekit.frames.Transform, scToInertial: org.orekit.frames.Transform) -> None:
        """
        Dump an observation transform transform.
        
        Parameters:
            scToBody (SpacecraftToObservedBody): provider for observation
            index (int): index of the transform
            bodyToInertial (org.orekit.frames.Transform): transform from body frame to inertial frame
            scToInertial (org.orekit.frames.Transform): transfrom from spacecraft frame to inertial frame
        
        
        """
        ...
    @staticmethod
    def endNicely() -> None:
        """
        In case dump is suspended and an exception is thrown, allows the dump to end nicely.
        """
        ...
    @staticmethod
    def isActive() -> bool:
        """
        Check if dump is active for this thread.
        
        Returns:
            true if dump is active for this thread
        
        
        """
        ...
    @staticmethod
    def resume(wasSuspended: bool) -> None:
        """
        Resume the dump, only if it was not already suspended.
        
        Parameters:
            wasSuspended (Boolean): flag to tell if the dump was already suspended (true; false otherwise)
        
        
        """
        ...
    @staticmethod
    def suspend() -> bool:
        """
        Suspend the dump. In case the dump is already suspended, keep the previous status in order to correctly deal the resume stage.
        
        Returns:
            a flag to tell if the dump is already suspended (true; false otherwise)
        
        
        """
        ...

class DumpReplayer:
    """
    Replayer for Rugged debug dumps.
    
    Also see:
        DumpManager, Dump
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def createRugged(self) -> org.orekit.rugged.api.Rugged:
        """
        Create a Rugged instance from parsed data.
        
        Returns:
            rugged instance
        
        
        """
        ...
    def execute(self, rugged: org.orekit.rugged.api.Rugged) -> typing.MutableSequence['DumpReplayer.Result']:
        """
        Execute all dumped calls.
        
        The dumped calls correspond to computation methods like direct or inverse location.
        
        Parameters:
            rugged (Rugged): Rugged instance on which calls will be performed
        
        Returns:
            results of all dumped calls
        
        
        """
        ...
    def parse(self, file: typing.Union[java.io.File, jpype.protocol.SupportsPath]) -> None:
        """
        Parse a dump file.
        
        Parameters:
            file (File): dump file to parse
        
        
        """
        ...
    class Result:
        def getExpected(self) -> typing.Any: ...
        def getReplayed(self) -> typing.Any: ...

class RuggedException(java.lang.RuntimeException, org.hipparchus.exception.LocalizedException):
    """
    This class is the base class for all specific exceptions thrown by the rugged library classes.
    
    This class is heavily based on OrekitException, which is distributed under the terms of the Apache License V2.
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, localizable: org.hipparchus.exception.Localizable, *object: typing.Any): ...
    @typing.overload
    def __init__(self, localizable: org.hipparchus.exception.Localizable, *object: typing.Any): ...
    def getLocalizedMessage(self) -> str:
        """
        Overrides: Throwable in class Throwable
        
        
        """
        ...
    @typing.overload
    def getMessage(self) -> str:
        """
        Overrides: Throwable in class Throwable
        
        
        """
        ...
    @typing.overload
    def getMessage(self, locale: java.util.Locale) -> str:
        """
        Specified by: getMessage in interface LocalizedException
        """
        ...
    def getParts(self) -> typing.MutableSequence[typing.Any]:
        """
        Get the variable parts of the error message.
        
        Specified by: getParts in interface LocalizedException
        
        Returns:
            a copy of the variable parts of the error message
        
        
        """
        ...
    def getSpecifier(self) -> org.hipparchus.exception.Localizable:
        """
        Get the localizable specifier of the error message.
        
        Specified by: getSpecifier in interface LocalizedException
        
        Returns:
            localizable specifier of the error message
        
        
        """
        ...

class RuggedExceptionWrapper(java.lang.RuntimeException):
    """
    Deprecated. as of 2.1, this class is not used anymore, as RuggedException is now an unchecked exception This class allows to wrap RuggedException instances in RuntimeException.
    
    Wrapping RuggedException instances is useful when a low level method throws one such exception and this method must be called from another one which does not allow this exception. Typical examples are propagation methods that are used inside Hipparchus optimizers, integrators or solvers.
    
    This class is heavily based on OrekitException, which is distributed under the terms of the Apache License V2.
    
    Also see:
        serialized
    """
    def __init__(self, wrappedException: RuggedException):
        """
        Deprecated. Simple constructor.
        
        Parameters:
            wrappedException (RuggedException): Orekit exception to wrap
        
        
        """
        ...
    def getException(self) -> RuggedException:
        """
        Deprecated. Get the wrapped exception.
        
        Returns:
            wrapped exception
        
        
        """
        ...

class RuggedInternalError(java.lang.RuntimeException, org.hipparchus.exception.LocalizedException):
    """
    Extension of Runtime with localized message for internal errors only.
    
    Since:
        2.1
    
    Also see:
        serialized
    """
    def __init__(self, cause: java.lang.Throwable):
        """
        Create an exception with localized message.
        
        Parameters:
            cause (Throwable): underlying cause
        
        
        """
        ...
    def getLocalizedMessage(self) -> str:
        """
        Overrides: Throwable in class Throwable
        
        
        """
        ...
    @typing.overload
    def getMessage(self) -> str:
        """
        Overrides: Throwable in class Throwable
        
        
        """
        ...
    @typing.overload
    def getMessage(self, locale: java.util.Locale) -> str:
        """
        Specified by: getMessage in interface LocalizedException
        """
        ...
    def getParts(self) -> typing.MutableSequence[typing.Any]:
        """
        Specified by: getParts in interface LocalizedException
        
        
        """
        ...
    def getSpecifier(self) -> org.hipparchus.exception.Localizable:
        """
        Specified by: getSpecifier in interface LocalizedException
        
        
        """
        ...

class RuggedMessages(java.lang.Enum['RuggedMessages'], org.hipparchus.exception.Localizable):
    """
    Enumeration for localized messages formats.
    
    The constants in this enumeration represent the available formats as localized strings. These formats are intended to be localized using simple properties files, using the constant name as the key and the property value as the message format. The source English format is provided in the constants themselves to serve both as a reminder for developers to understand the parameters needed by each format, as a basis for translators to create localized properties files, and as a default format if some translation is missing.
    
    This class is heavily based on OrekitMessages, which is distributed under the terms of the Apache License V2.
    """
    INTERNAL_ERROR: typing.ClassVar['RuggedMessages'] = ...
    OUT_OF_TILE_INDICES: typing.ClassVar['RuggedMessages'] = ...
    OUT_OF_TILE_ANGLES: typing.ClassVar['RuggedMessages'] = ...
    NO_DEM_DATA: typing.ClassVar['RuggedMessages'] = ...
    TILE_WITHOUT_REQUIRED_NEIGHBORS_SELECTED: typing.ClassVar['RuggedMessages'] = ...
    OUT_OF_TIME_RANGE: typing.ClassVar['RuggedMessages'] = ...
    UNINITIALIZED_CONTEXT: typing.ClassVar['RuggedMessages'] = ...
    EMPTY_TILE: typing.ClassVar['RuggedMessages'] = ...
    UNKNOWN_SENSOR: typing.ClassVar['RuggedMessages'] = ...
    LINE_OF_SIGHT_DOES_NOT_REACH_GROUND: typing.ClassVar['RuggedMessages'] = ...
    LINE_OF_SIGHT_NEVER_CROSSES_LATITUDE: typing.ClassVar['RuggedMessages'] = ...
    LINE_OF_SIGHT_NEVER_CROSSES_LONGITUDE: typing.ClassVar['RuggedMessages'] = ...
    LINE_OF_SIGHT_NEVER_CROSSES_ALTITUDE: typing.ClassVar['RuggedMessages'] = ...
    DEM_ENTRY_POINT_IS_BEHIND_SPACECRAFT: typing.ClassVar['RuggedMessages'] = ...
    FRAMES_MISMATCH_WITH_INTERPOLATOR_DUMP: typing.ClassVar['RuggedMessages'] = ...
    NOT_INTERPOLATOR_DUMP_DATA: typing.ClassVar['RuggedMessages'] = ...
    DEBUG_DUMP_ALREADY_ACTIVE: typing.ClassVar['RuggedMessages'] = ...
    DEBUG_DUMP_ACTIVATION_ERROR: typing.ClassVar['RuggedMessages'] = ...
    DEBUG_DUMP_NOT_ACTIVE: typing.ClassVar['RuggedMessages'] = ...
    CANNOT_PARSE_LINE: typing.ClassVar['RuggedMessages'] = ...
    LIGHT_TIME_CORRECTION_REDEFINED: typing.ClassVar['RuggedMessages'] = ...
    ABERRATION_OF_LIGHT_CORRECTION_REDEFINED: typing.ClassVar['RuggedMessages'] = ...
    ATMOSPHERIC_REFRACTION_REDEFINED: typing.ClassVar['RuggedMessages'] = ...
    TILE_ALREADY_DEFINED: typing.ClassVar['RuggedMessages'] = ...
    UNKNOWN_TILE: typing.ClassVar['RuggedMessages'] = ...
    NO_PARAMETERS_SELECTED: typing.ClassVar['RuggedMessages'] = ...
    NO_REFERENCE_MAPPINGS: typing.ClassVar['RuggedMessages'] = ...
    DUPLICATED_PARAMETER_NAME: typing.ClassVar['RuggedMessages'] = ...
    INVALID_RUGGED_NAME: typing.ClassVar['RuggedMessages'] = ...
    UNSUPPORTED_REFINING_CONTEXT: typing.ClassVar['RuggedMessages'] = ...
    NO_LAYER_DATA: typing.ClassVar['RuggedMessages'] = ...
    INVALID_STEP: typing.ClassVar['RuggedMessages'] = ...
    INVALID_RANGE_FOR_LINES: typing.ClassVar['RuggedMessages'] = ...
    SENSOR_PIXEL_NOT_FOUND_IN_RANGE_LINES: typing.ClassVar['RuggedMessages'] = ...
    SENSOR_PIXEL_NOT_FOUND_IN_PIXELS_LINE: typing.ClassVar['RuggedMessages'] = ...
    @typing.overload
    def getLocalizedString(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    @typing.overload
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        Specified by: getLocalizedString in interface Localizable
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        Specified by: getSourceString in interface Localizable
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'RuggedMessages':
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
    def values() -> typing.MutableSequence['RuggedMessages']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows:
        
        
        for (RuggedMessages c : RuggedMessages.values())
            System.out.println(c);
        
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...
    class UTF8Control(java.util.ResourceBundle.Control):
        def __init__(self): ...
        def newBundle(self, string: str, locale: java.util.Locale, string2: str, classLoader: java.lang.ClassLoader, boolean: bool) -> java.util.ResourceBundle: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.errors")``.

    DumpManager: typing.Type[DumpManager]
    DumpReplayer: typing.Type[DumpReplayer]
    RuggedException: typing.Type[RuggedException]
    RuggedExceptionWrapper: typing.Type[RuggedExceptionWrapper]
    RuggedInternalError: typing.Type[RuggedInternalError]
    RuggedMessages: typing.Type[RuggedMessages]
