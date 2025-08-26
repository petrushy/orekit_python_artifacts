
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.bodies
import org.orekit.frames
import org.orekit.propagation
import org.orekit.rugged.intersection
import org.orekit.rugged.linesensor
import org.orekit.rugged.raster
import org.orekit.rugged.refraction
import org.orekit.rugged.utils
import org.orekit.time
import org.orekit.utils
import typing



class AlgorithmId(java.lang.Enum['AlgorithmId']):
    """
    public enum AlgorithmId extends :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.rugged.api.AlgorithmId`>
    
        Enumerate for Digital Elevation Model intersection.
    """
    DUVENHAGE: typing.ClassVar['AlgorithmId'] = ...
    DUVENHAGE_FLAT_BODY: typing.ClassVar['AlgorithmId'] = ...
    BASIC_SLOW_EXHAUSTIVE_SCAN_FOR_TESTS_ONLY: typing.ClassVar['AlgorithmId'] = ...
    CONSTANT_ELEVATION_OVER_ELLIPSOID: typing.ClassVar['AlgorithmId'] = ...
    IGNORE_DEM_USE_ELLIPSOID: typing.ClassVar['AlgorithmId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'AlgorithmId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['AlgorithmId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (AlgorithmId c : AlgorithmId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class BodyRotatingFrameId(java.lang.Enum['BodyRotatingFrameId']):
    """
    public enum BodyRotatingFrameId extends :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.rugged.api.BodyRotatingFrameId`>
    
        Enumerate for body rotating frames.
    """
    ITRF: typing.ClassVar['BodyRotatingFrameId'] = ...
    ITRF_EQUINOX: typing.ClassVar['BodyRotatingFrameId'] = ...
    GTOD: typing.ClassVar['BodyRotatingFrameId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'BodyRotatingFrameId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['BodyRotatingFrameId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (BodyRotatingFrameId c : BodyRotatingFrameId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class EllipsoidId(java.lang.Enum['EllipsoidId']):
    """
    public enum EllipsoidId extends :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.rugged.api.EllipsoidId`>
    
        Enumerate for ellipsoid.
    """
    GRS80: typing.ClassVar['EllipsoidId'] = ...
    WGS84: typing.ClassVar['EllipsoidId'] = ...
    IERS96: typing.ClassVar['EllipsoidId'] = ...
    IERS2003: typing.ClassVar['EllipsoidId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'EllipsoidId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['EllipsoidId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (EllipsoidId c : EllipsoidId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class InertialFrameId(java.lang.Enum['InertialFrameId']):
    """
    public enum InertialFrameId extends :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum?is`<:class:`~org.orekit.rugged.api.InertialFrameId`>
    
        Enumerate for inertial frames.
    """
    GCRF: typing.ClassVar['InertialFrameId'] = ...
    EME2000: typing.ClassVar['InertialFrameId'] = ...
    MOD: typing.ClassVar['InertialFrameId'] = ...
    TOD: typing.ClassVar['InertialFrameId'] = ...
    VEIS1950: typing.ClassVar['InertialFrameId'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'InertialFrameId':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException?is`: if this enum type has no constant with the specified name
                :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException?is`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['InertialFrameId']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (InertialFrameId c : InertialFrameId.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class Rugged:
    """
    public class Rugged extends :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Main class of Rugged library API.
    
        Also see:
            :class:`~org.orekit.rugged.api.RuggedBuilder`
    """
    @typing.overload
    def dateLocation(self, string: str, double: float, double2: float, int: int, int2: int) -> org.orekit.time.AbsoluteDate:
        """
            Find the date at which sensor sees a ground point.
        
            This method is a partial :meth:`~org.orekit.rugged.api.Rugged.inverseLocation` focusing only on date.
        
            The point is given only by its latitude and longitude, the elevation is computed from the Digital Elevation Model.
        
            Note that for each sensor name, the :code:`minLine` and :code:`maxLine` settings are cached, because they induce costly
            frames computation. So these settings should not be tuned very finely and changed at each call, but should rather be a
            few thousand lines wide and refreshed only when needed. If for example an inverse location is roughly estimated to occur
            near line 53764 (for example using :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`), :code:`minLine` and
            :code:`maxLine` could be set for example to 50000 and 60000, which would be OK also if next line inverse location is
            expected to occur near line 53780, and next one ... The setting could be changed for example to 55000 and 65000 when an
            inverse location is expected to occur after 55750. Of course, these values are only an example and should be adjusted
            depending on mission needs.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the line sensor
                latitude (double): ground point latitude (rad)
                longitude (double): ground point longitude (rad)
                minLine (int): minimum line number
                maxLine (int): maximum line number
        
            Returns:
                date at which ground point is seen by line sensor
        
            Also see:
                :meth:`~org.orekit.rugged.api.Rugged.inverseLocation`, :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`
        
        """
        ...
    @typing.overload
    def dateLocation(self, string: str, geodeticPoint: org.orekit.bodies.GeodeticPoint, int: int, int2: int) -> org.orekit.time.AbsoluteDate:
        """
            Find the date at which sensor sees a ground point.
        
            This method is a partial :meth:`~org.orekit.rugged.api.Rugged.inverseLocation` focusing only on date.
        
            Note that for each sensor name, the :code:`minLine` and :code:`maxLine` settings are cached, because they induce costly
            frames computation. So these settings should not be tuned very finely and changed at each call, but should rather be a
            few thousand lines wide and refreshed only when needed. If for example an inverse location is roughly estimated to occur
            near line 53764 (for example using :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`), :code:`minLine` and
            :code:`maxLine` could be set for example to 50000 and 60000, which would be OK also if next line inverse location is
            expected to occur near line 53780, and next one ... The setting could be changed for example to 55000 and 65000 when an
            inverse location is expected to occur after 55750. Of course, these values are only an example and should be adjusted
            depending on mission needs.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the line sensor
                point (org.orekit.bodies.GeodeticPoint): point to localize
                minLine (int): minimum line number
                maxLine (int): maximum line number
        
            Returns:
                date at which ground point is seen by line sensor
        
            Also see:
                :meth:`~org.orekit.rugged.api.Rugged.inverseLocation`, :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`
        
        
        """
        ...
    @typing.overload
    def directLocation(self, absoluteDate: org.orekit.time.AbsoluteDate, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.orekit.bodies.GeodeticPoint:
        """
            Direct location of a single line-of-sight.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date of the location
                sensorPosition (org.hipparchus.geometry.euclidean.threed.Vector3D): sensor position in spacecraft frame. For simplicity, due to the size of sensor, we consider each pixel to be at sensor
                    position
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): normalized line-of-sight in spacecraft frame
        
            Returns:
                ground position of intersection point between specified los and ground
        
        
        """
        ...
    @typing.overload
    def directLocation(self, string: str, double: float) -> typing.MutableSequence[org.orekit.bodies.GeodeticPoint]:
        """
            Direct location of a sensor line.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the line sensor
                lineNumber (double): number of the line to localize on ground
        
            Returns:
                ground position of all pixels of the specified sensor line
        
        """
        ...
    def distanceBetweenLOS(self, lineSensor: org.orekit.rugged.linesensor.LineSensor, absoluteDate: org.orekit.time.AbsoluteDate, double: float, spacecraftToObservedBody: org.orekit.rugged.utils.SpacecraftToObservedBody, lineSensor2: org.orekit.rugged.linesensor.LineSensor, absoluteDate2: org.orekit.time.AbsoluteDate, double2: float) -> typing.MutableSequence[float]:
        """
            Compute distances between two line sensors.
        
            Parameters:
                sensorA (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor A
                dateA (org.orekit.time.AbsoluteDate): current date for sensor A
                pixelA (double): pixel index for sensor A
                scToBodyA (:class:`~org.orekit.rugged.utils.SpacecraftToObservedBody`): spacecraft to body transform for sensor A
                sensorB (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor B
                dateB (org.orekit.time.AbsoluteDate): current date for sensor B
                pixelB (double): pixel index for sensor B
        
            Returns:
                distances computed between LOS and to the ground
        
            Since:
                2.0
        
        
        """
        ...
    _distanceBetweenLOSderivatives__T = typing.TypeVar('_distanceBetweenLOSderivatives__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    def distanceBetweenLOSderivatives(self, lineSensor: org.orekit.rugged.linesensor.LineSensor, absoluteDate: org.orekit.time.AbsoluteDate, double: float, spacecraftToObservedBody: org.orekit.rugged.utils.SpacecraftToObservedBody, lineSensor2: org.orekit.rugged.linesensor.LineSensor, absoluteDate2: org.orekit.time.AbsoluteDate, double2: float, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_distanceBetweenLOSderivatives__T]) -> typing.MutableSequence[_distanceBetweenLOSderivatives__T]:
        """
            Compute distances between two line sensors with derivatives.
        
            Parameters:
                sensorA (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor A
                dateA (org.orekit.time.AbsoluteDate): current date for sensor A
                pixelA (double): pixel index for sensor A
                scToBodyA (:class:`~org.orekit.rugged.utils.SpacecraftToObservedBody`): spacecraftToBody transform for sensor A
                sensorB (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor B
                dateB (org.orekit.time.AbsoluteDate): current date for sensor B
                pixelB (double): pixel index for sensor B
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`DerivativeStructure` instances
        
            Returns:
                distances computed, with derivatives, between LOS and to the ground
        
            Also see:
                :meth:`~org.orekit.rugged.api.Rugged.distanceBetweenLOS`
        
        
        """
        ...
    def getAlgorithm(self) -> org.orekit.rugged.intersection.IntersectionAlgorithm:
        """
            Get the DEM intersection algorithm.
        
            Returns:
                DEM intersection algorithm
        
        
        """
        ...
    def getAlgorithmId(self) -> AlgorithmId:
        """
            Get the DEM intersection algorithm identifier.
        
            Returns:
                DEM intersection algorithm Id
        
            Since:
                2.2
        
        
        """
        ...
    def getBodyToInertial(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
            Get transform from observed body frame to inertial frame.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date of the transform
        
            Returns:
                transform from observed body frame to inertial frame
        
        
        """
        ...
    def getEllipsoid(self) -> org.orekit.rugged.utils.ExtendedEllipsoid:
        """
            Get the observed body ellipsoid.
        
            Returns:
                observed body ellipsoid
        
        
        """
        ...
    def getInertialToBody(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
            Get transform from inertial frame to observed body frame.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date of the transform
        
            Returns:
                transform from inertial frame to observed body frame
        
        
        """
        ...
    def getLineSensor(self, string: str) -> org.orekit.rugged.linesensor.LineSensor:
        """
            Get a sensor.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): sensor name
        
            Returns:
                selected sensor
        
        
        """
        ...
    def getLineSensors(self) -> java.util.Collection[org.orekit.rugged.linesensor.LineSensor]: ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end of search time span.
        
            Returns:
                end of search time span
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start of search time span.
        
            Returns:
                start of search time span
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the Rugged name.
        
            Returns:
                Rugged name
        
            Since:
                2.0
        
        
        """
        ...
    def getRefractionCorrection(self) -> org.orekit.rugged.refraction.AtmosphericRefraction:
        """
            Get the atmospheric refraction model.
        
            Returns:
                atmospheric refraction model
        
            Since:
                2.0
        
        
        """
        ...
    def getScToBody(self) -> org.orekit.rugged.utils.SpacecraftToObservedBody:
        """
            Get converter between spacecraft and body.
        
            Returns:
                the scToBody
        
            Since:
                2.0
        
        
        """
        ...
    def getScToInertial(self, absoluteDate: org.orekit.time.AbsoluteDate) -> org.orekit.frames.Transform:
        """
            Get transform from spacecraft to inertial frame.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date of the transform
        
            Returns:
                transform from spacecraft to inertial frame
        
        
        """
        ...
    @typing.overload
    def inverseLocation(self, string: str, double: float, double2: float, int: int, int2: int) -> org.orekit.rugged.linesensor.SensorPixel:
        """
            Inverse location of a ground point.
        
            The point is given only by its latitude and longitude, the elevation is computed from the Digital Elevation Model.
        
            Note that for each sensor name, the :code:`minLine` and :code:`maxLine` settings are cached, because they induce costly
            frames computation. So these settings should not be tuned very finely and changed at each call, but should rather be a
            few thousand lines wide and refreshed only when needed. If for example an inverse location is roughly estimated to occur
            near line 53764 (for example using :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`), :code:`minLine` and
            :code:`maxLine` could be set for example to 50000 and 60000, which would be OK also if next line inverse location is
            expected to occur near line 53780, and next one ... The setting could be changed for example to 55000 and 65000 when an
            inverse location is expected to occur after 55750. Of course, these values are only an example and should be adjusted
            depending on mission needs.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the line sensor
                latitude (double): ground point latitude (rad)
                longitude (double): ground point longitude (rad)
                minLine (int): minimum line number
                maxLine (int): maximum line number
        
            Returns:
                sensor pixel seeing ground point, or null if ground point cannot be seen between the prescribed line numbers
        
            Also see:
                :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`
        
        """
        ...
    @typing.overload
    def inverseLocation(self, string: str, geodeticPoint: org.orekit.bodies.GeodeticPoint, int: int, int2: int) -> org.orekit.rugged.linesensor.SensorPixel:
        """
            Inverse location of a point.
        
            Note that for each sensor name, the :code:`minLine` and :code:`maxLine` settings are cached, because they induce costly
            frames computation. So these settings should not be tuned very finely and changed at each call, but should rather be a
            few thousand lines wide and refreshed only when needed. If for example an inverse location is roughly estimated to occur
            near line 53764 (for example using :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`), :code:`minLine` and
            :code:`maxLine` could be set for example to 50000 and 60000, which would be OK also if next line inverse location is
            expected to occur near line 53780, and next one ... The setting could be changed for example to 55000 and 65000 when an
            inverse location is expected to occur after 55750. Of course, these values are only an example and should be adjusted
            depending on mission needs.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the line sensor
                point (org.orekit.bodies.GeodeticPoint): geodetic point to localize
                minLine (int): minimum line number where the search will be performed
                maxLine (int): maximum line number where the search will be performed
        
            Returns:
                sensor pixel seeing point, or null if point cannot be seen between the prescribed line numbers
        
            Also see:
                :meth:`~org.orekit.rugged.api.Rugged.dateLocation`, :class:`~org.orekit.rugged.utils.RoughVisibilityEstimator`
        
        
        """
        ...
    _inverseLocationDerivatives__T = typing.TypeVar('_inverseLocationDerivatives__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    def inverseLocationDerivatives(self, string: str, geodeticPoint: org.orekit.bodies.GeodeticPoint, int: int, int2: int, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_inverseLocationDerivatives__T]) -> typing.MutableSequence[_inverseLocationDerivatives__T]:
        """
            Inverse location of a point with derivatives.
        
            Parameters:
                sensorName (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): name of the line sensor
                point (org.orekit.bodies.GeodeticPoint): point to localize
                minLine (int): minimum line number
                maxLine (int): maximum line number
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
            Returns:
                sensor pixel seeing point with derivatives, or null if point cannot be seen between the prescribed line numbers
        
            Since:
                2.0
        
            Also see:
                :meth:`~org.orekit.rugged.api.Rugged.inverseLocation`
        
        
        """
        ...
    def isAberrationOfLightCorrected(self) -> bool:
        """
            Get flag for aberration of light correction.
        
            Returns:
                true if the aberration of light time is corrected for more accurate location
        
        
        """
        ...
    def isInRange(self, absoluteDate: org.orekit.time.AbsoluteDate) -> bool:
        """
            Check if a date is in the supported range.
        
            The support range is given by the :code:`minDate` and :code:`maxDate` construction parameters, with an
            :code:`overshootTolerance` margin accepted (i.e. a date slightly before :code:`minDate` or slightly after
            :code:`maxDate` will be considered in range if the overshoot does not exceed the tolerance set at construction).
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date to check
        
            Returns:
                true if date is in the supported range
        
        
        """
        ...
    def isLightTimeCorrected(self) -> bool:
        """
            Get flag for light time correction.
        
            Returns:
                true if the light time between ground and spacecraft is compensated for more accurate location
        
        
        """
        ...

class RuggedBuilder:
    """
    public class RuggedBuilder extends :class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Builder for :class:`~org.orekit.rugged.api.Rugged` instances.
    
        This class implements the *builder pattern* to create :class:`~org.orekit.rugged.api.Rugged` instances. It does so by
        using a *fluent API* in order to clarify reading and allow later extensions with new configuration parameters.
    
        A typical use would be:
    
        .. code-block: java
        
           Rugged rugged = new RuggedBuilder().
                           setEllipsoid(EllipsoidId.WGS84, BodyRotatingFrameId.ITRF).
                           setAlgorithmID(AlgorithmId.Duvenhage).
                           setDigitalElevationModel(tileUpdater, maxCachedTiles).
                           setTimeSpan(minDate, maxDate, tStep, overshootTolerance).
                           setTrajectory(positionsVelocities, pvInterpolationNumber, pvFilter,
                                         quaternions, aInterpolationNumber, aFilter).
                           addLineSensor(sensor1).
                           addLineSensor(sensor2).
                           addLineSensor(sensor3).
                           build();
         
    
        If a configuration parameter has not been set prior to the call to {]link #build()}, then an exception will be triggered
        with an explicit error message.
    
        Also see:
            :class:`~org.orekit.rugged.api.https:.en.wikipedia.org.wiki.Builder_pattern`,
            :class:`~org.orekit.rugged.api.https:.en.wikipedia.org.wiki.Fluent_interface`
    """
    def __init__(self): ...
    def addLineSensor(self, lineSensor: org.orekit.rugged.linesensor.LineSensor) -> 'RuggedBuilder':
        """
            Set up line sensor model.
        
            Parameters:
                lineSensor (:class:`~org.orekit.rugged.linesensor.LineSensor`): line sensor model
        
            Returns:
                the builder instance
        
        
        """
        ...
    def build(self) -> Rugged:
        """
            Build a :class:`~org.orekit.rugged.api.Rugged` instance.
        
            Returns:
                built instance
        
        
        """
        ...
    def clearLineSensors(self) -> 'RuggedBuilder':
        """
            Remove all line sensors.
        
            Returns:
                the builder instance
        
        
        """
        ...
    def getAFilter(self) -> org.orekit.utils.AngularDerivativesFilter:
        """
            Get the filter for derivatives from the sample to use in attitude interpolation.
        
            Returns:
                filter for derivatives from the sample to use in attitude interpolation
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`
        
        
        """
        ...
    def getAInterpolationNumber(self) -> int:
        """
            Get the number of points to use for attitude interpolation.
        
            Returns:
                number of points to use for attitude interpolation
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`
        
        
        """
        ...
    def getAberrationOfLightCorrection(self) -> bool:
        """
            Get the aberration of light correction flag.
        
            Returns:
                aberration of light correction flag
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setAberrationOfLightCorrection`
        
        
        """
        ...
    def getAlgorithm(self) -> AlgorithmId:
        """
            Get the algorithm to use for Digital Elevation Model intersection.
        
            Returns:
                algorithm to use for Digital Elevation Model intersection
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm`
        
        
        """
        ...
    def getConstantElevation(self) -> float:
        """
            Get the constant elevation over ellipsoid to use with
            :meth:`~org.orekit.rugged.api.AlgorithmId.CONSTANT_ELEVATION_OVER_ELLIPSOID`.
        
            Returns:
                updater used to load Digital Elevation Model tiles
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setConstantElevation`
        
        
        """
        ...
    def getEllipsoid(self) -> org.orekit.rugged.utils.ExtendedEllipsoid:
        """
            Get the ellipsoid.
        
            Returns:
                the ellipsoid
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setEllipsoid`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setEllipsoid`
        
        
        """
        ...
    def getInertialFrame(self) -> org.orekit.frames.Frame:
        """
            Get the inertial frame.
        
            Returns:
                inertial frame
        
        
        """
        ...
    def getLightTimeCorrection(self) -> bool:
        """
            Get the light time correction flag.
        
            Returns:
                light time correction flag
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setLightTimeCorrection`
        
        
        """
        ...
    def getLineSensors(self) -> java.util.List[org.orekit.rugged.linesensor.LineSensor]: ...
    def getMaxCachedTiles(self) -> int:
        """
            Get the maximum number of tiles stored in the cache.
        
            Returns:
                maximum number of tiles stored in the cache
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getTileUpdater`
        
        
        """
        ...
    def getMaxDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the end of search time span.
        
            Returns:
                end of search time span
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan`
        
        
        """
        ...
    def getMinDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the start of search time span.
        
            Returns:
                start of search time span
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan`
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the Rugged name.
        
            Returns:
                the Rugged name
        
            Since:
                2.0
        
        
        """
        ...
    def getOvershootTolerance(self) -> float:
        """
            Get the tolerance in seconds allowed for :meth:`~org.orekit.rugged.api.RuggedBuilder.getMinDate` and
            :meth:`~org.orekit.rugged.api.RuggedBuilder.getMaxDate` overshooting.
        
            Returns:
                tolerance in seconds allowed for :meth:`~org.orekit.rugged.api.RuggedBuilder.getMinDate` and
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getMaxDate` overshooting
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan`
        
        
        """
        ...
    def getPVFilter(self) -> org.orekit.utils.CartesianDerivativesFilter:
        """
            Get the filter for derivatives from the sample to use in position/velocity interpolation.
        
            Returns:
                filter for derivatives from the sample to use in position/velocity interpolation
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`
        
        
        """
        ...
    def getPVInterpolationNumber(self) -> int:
        """
            Get the number of points to use for position/velocity interpolation.
        
            Returns:
                number of points to use for position/velocity interpolation
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`
        
        
        """
        ...
    def getPositionsVelocities(self) -> java.util.List[org.orekit.utils.TimeStampedPVCoordinates]:
        """
            Get the satellite position and velocity (m and m/s in inertial frame).
        
            Returns:
                satellite position and velocity (m and m/s in inertial frame)
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`
        
        
        """
        ...
    def getQuaternions(self) -> java.util.List[org.orekit.utils.TimeStampedAngularCoordinates]:
        """
            Get the satellite quaternions with respect to inertial frame.
        
            Returns:
                satellite quaternions with respect to inertial frame
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`
        
        
        """
        ...
    def getRefractionCorrection(self) -> org.orekit.rugged.refraction.AtmosphericRefraction:
        """
            Get the atmospheric refraction model.
        
            Returns:
                atmospheric refraction model
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setRefractionCorrection`
        
        
        """
        ...
    def getTStep(self) -> float:
        """
            Get the step to use for inertial frame to body frame transforms cache computations.
        
            Returns:
                step to use for inertial frame to body frame transforms cache computations
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan`
        
        
        """
        ...
    def getTileUpdater(self) -> org.orekit.rugged.raster.TileUpdater:
        """
            Get the updater used to load Digital Elevation Model tiles.
        
            Returns:
                updater used to load Digital Elevation Model tiles
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getMaxCachedTiles`
        
        
        """
        ...
    def isOverlappingTiles(self) -> bool:
        """
            Get the flag telling if the DEM tiles are overlapping.
        
            Returns:
                true if the Digital Elevation Model tiles are overlapping; false otherwise. Default = true.
        
            Since:
                4.0
        
        
        """
        ...
    def setAberrationOfLightCorrection(self, boolean: bool) -> 'RuggedBuilder':
        """
            Set flag for aberration of light correction.
        
            This methods set the flag for compensating or not aberration of light, which is velocity composition between light and
            spacecraft when the light from ground points reaches the sensor. Compensating this velocity composition improves
            location accuracy and is *enabled* by default (i.e. not calling this method before building is therefore equivalent to
            calling it with a parameter set to :code:`true`). Not compensating it is useful in two cases: for validation purposes
            against system that do not compensate it or when the pixels line of sight already include the correction.
        
            Parameters:
                newAberrationOfLightCorrection (boolean): if true, the aberration of light is corrected for more accurate location
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setLightTimeCorrection`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getAberrationOfLightCorrection`
        
        
        """
        ...
    def setAlgorithm(self, algorithmId: AlgorithmId) -> 'RuggedBuilder':
        """
            Set the algorithm to use for Digital Elevation Model intersection.
        
            Note that some algorithms require specific other methods to be called too:
        
              - :meth:`~org.orekit.rugged.api.AlgorithmId.DUVENHAGE`, :meth:`~org.orekit.rugged.api.AlgorithmId.DUVENHAGE_FLAT_BODY` and
                :meth:`~org.orekit.rugged.api.AlgorithmId.BASIC_SLOW_EXHAUSTIVE_SCAN_FOR_TESTS_ONLY` all require
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel` or
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel` to be called,
              - :meth:`~org.orekit.rugged.api.AlgorithmId.CONSTANT_ELEVATION_OVER_ELLIPSOID` requires
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setConstantElevation` to be called,
              - :meth:`~org.orekit.rugged.api.AlgorithmId.IGNORE_DEM_USE_ELLIPSOID` does not require any methods tobe called.
        
        
            Parameters:
                newAlgorithmId (:class:`~org.orekit.rugged.api.AlgorithmId`): identifier of algorithm to use for Digital Elevation Model intersection
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getAlgorithm`
        
        
        """
        ...
    def setConstantElevation(self, double: float) -> 'RuggedBuilder':
        """
            Set the user-provided constant elevation model.
        
            Note that this method is relevant *only* if the algorithm specified in
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm` is
            :meth:`~org.orekit.rugged.api.AlgorithmId.CONSTANT_ELEVATION_OVER_ELLIPSOID`. If it is called for another algorithm, the
            elevation set here will be ignored.
        
            Parameters:
                newConstantElevation (double): constant elevation to use (m)
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getConstantElevation`
        
        
        """
        ...
    @typing.overload
    def setDigitalElevationModel(self, tileUpdater: typing.Union[org.orekit.rugged.raster.TileUpdater, typing.Callable], int: int) -> 'RuggedBuilder':
        """
            Set the user-provided :class:`~org.orekit.rugged.raster.TileUpdater`.
        
            The DEM tiles must be overlapping, otherwise use :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`
            with flag set to false.
        
            Note that when the algorithm specified in :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm` is either
            :meth:`~org.orekit.rugged.api.AlgorithmId.CONSTANT_ELEVATION_OVER_ELLIPSOID` or
            :meth:`~org.orekit.rugged.api.AlgorithmId.IGNORE_DEM_USE_ELLIPSOID`, then this method becomes irrelevant and can either
            be not called at all, or it can be called with an updater set to :code:`null`. For all other algorithms, the updater
            must be properly configured.
        
            Parameters:
                newTileUpdater (:class:`~org.orekit.rugged.raster.TileUpdater`): updater used to load Digital Elevation Model tiles
                newMaxCachedTiles (int): maximum number of tiles stored in the cache
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm`, :meth:`~org.orekit.rugged.api.RuggedBuilder.getTileUpdater`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getMaxCachedTiles`
        
            Set the user-provided :class:`~org.orekit.rugged.raster.TileUpdater`.
        
            Note that when the algorithm specified in :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm` is either
            :meth:`~org.orekit.rugged.api.AlgorithmId.CONSTANT_ELEVATION_OVER_ELLIPSOID` or
            :meth:`~org.orekit.rugged.api.AlgorithmId.IGNORE_DEM_USE_ELLIPSOID`, then this method becomes irrelevant and can either
            be not called at all, or it can be called with an updater set to :code:`null`. For all other algorithms, the updater
            must be properly configured.
        
            Parameters:
                newTileUpdater (:class:`~org.orekit.rugged.raster.TileUpdater`): updater used to load Digital Elevation Model tiles
                newMaxCachedTiles (int): maximum number of tiles stored in the cache
                newIsOverlappingTiles (boolean): flag to tell if the DEM tiles are overlapping: true if overlapping; false otherwise.
        
            Returns:
                the builder instance
        
            Since:
                4.0
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setDigitalElevationModel`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setAlgorithm`, :meth:`~org.orekit.rugged.api.RuggedBuilder.getTileUpdater`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getMaxCachedTiles`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.isOverlappingTiles`
        
        
        """
        ...
    @typing.overload
    def setDigitalElevationModel(self, tileUpdater: typing.Union[org.orekit.rugged.raster.TileUpdater, typing.Callable], int: int, boolean: bool) -> 'RuggedBuilder': ...
    @typing.overload
    def setEllipsoid(self, oneAxisEllipsoid: org.orekit.bodies.OneAxisEllipsoid) -> 'RuggedBuilder':
        """
            Set the reference ellipsoid.
        
            Parameters:
                ellipsoidID (:class:`~org.orekit.rugged.api.EllipsoidId`): reference ellipsoid
                bodyRotatingFrameID (:class:`~org.orekit.rugged.api.BodyRotatingFrameId`): body rotating frame identifier from an earlier run and frames mismatch
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setEllipsoid`, :meth:`~org.orekit.rugged.api.RuggedBuilder.getEllipsoid`
        
            Set the reference ellipsoid.
        
            Parameters:
                newEllipsoid (org.orekit.bodies.OneAxisEllipsoid): reference ellipsoid
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setEllipsoid`, :meth:`~org.orekit.rugged.api.RuggedBuilder.getEllipsoid`
        
        
        """
        ...
    @typing.overload
    def setEllipsoid(self, ellipsoidId: EllipsoidId, bodyRotatingFrameId: BodyRotatingFrameId) -> 'RuggedBuilder': ...
    def setLightTimeCorrection(self, boolean: bool) -> 'RuggedBuilder':
        """
            Set flag for light time correction.
        
            This methods set the flag for compensating or not light time between ground and spacecraft. Compensating this delay
            improves location accuracy and is *enabled* by default (i.e. not calling this method before building is therefore
            equivalent to calling it with a parameter set to :code:`true`). Not compensating it is mainly useful for validation
            purposes against system that do not compensate it.
        
            Parameters:
                newLightTimeCorrection (boolean): if true, the light travel time between ground and spacecraft is compensated for more accurate location
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setAberrationOfLightCorrection`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getLightTimeCorrection`
        
        
        """
        ...
    def setName(self, string: str) -> None:
        """
            Set the Rugged name.
        
            Parameters:
                name (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.lang.String?is`): the Rugged name
        
            Since:
                2.0
        
        
        """
        ...
    def setOverlappingTiles(self, boolean: bool) -> None:
        """
            Set the DEM overlapping tiles flag.
        
            Parameters:
                newIsOverlappingTiles (boolean): flag to tell if the Digital Elevation Model tiles are overlapping: true if overlapping; false otherwise
        
            Since:
                4.0
        
        
        """
        ...
    def setRefractionCorrection(self, atmosphericRefraction: org.orekit.rugged.refraction.AtmosphericRefraction) -> 'RuggedBuilder':
        """
            Set atmospheric refraction for line of sight correction.
        
            This method sets an atmospheric refraction model to be used between spacecraft and ground for the correction of
            intersected points on ground. Compensating for the effect of atmospheric refraction improves location accuracy.
        
            Parameters:
                newAtmosphericRefraction (:class:`~org.orekit.rugged.refraction.AtmosphericRefraction`): the atmospheric refraction model to be used for more accurate location
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getRefractionCorrection`
        
        
        """
        ...
    def setTimeSpan(self, absoluteDate: org.orekit.time.AbsoluteDate, absoluteDate2: org.orekit.time.AbsoluteDate, double: float, double2: float) -> 'RuggedBuilder':
        """
            Set the time span to be covered for direct and inverse location calls.
        
            This method set only the time span and not the trajectory, therefore it *must* be used together with either
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
            or :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory` but should *not* be mixed with
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`.
        
            Parameters:
                newMinDate (org.orekit.time.AbsoluteDate): start of search time span
                newMaxDate (org.orekit.time.AbsoluteDate): end of search time span
                newTstep (double): step to use for inertial frame to body frame transforms cache computations (s)
                newOvershootTolerance (double): tolerance in seconds allowed for :code:`minDate` and :code:`maxDate` overshooting (s)
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getMinDate`, :meth:`~org.orekit.rugged.api.RuggedBuilder.getMaxDate`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getTStep`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getOvershootTolerance`
        
        
        """
        ...
    @typing.overload
    def setTrajectory(self, double: float, int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter, propagator: org.orekit.propagation.Propagator) -> 'RuggedBuilder':
        """
            Set the spacecraft trajectory.
        
            This method set only the trajectory and not the time span, therefore it *must* be used together with the
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan` but should *not* be mixed with
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`.
        
            Parameters:
                inertialFrameId (:class:`~org.orekit.rugged.api.InertialFrameId`): inertial frame Id used for spacecraft positions/velocities/quaternions
                positionsVelocities (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<org.orekit.utils.TimeStampedPVCoordinates> positionsVelocities): satellite position and velocity (m and m/s in inertial frame)
                pvInterpolationNumber (int): number of points to use for position/velocity interpolation
                pvFilter (org.orekit.utils.CartesianDerivativesFilter): filter for derivatives from the sample to use in position/velocity interpolation
                quaternions (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<org.orekit.utils.TimeStampedAngularCoordinates> quaternions): satellite quaternions with respect to inertial frame
                aInterpolationNumber (int): number of points to use for attitude interpolation
                aFilter (org.orekit.utils.AngularDerivativesFilter): filter for derivatives from the sample to use in attitude interpolation
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getInertialFrame`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getPositionsVelocities`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getPVInterpolationNumber`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getPVInterpolationNumber`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getQuaternions`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getAInterpolationNumber`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getAFilter`
        
            Set the spacecraft trajectory.
        
            This method set only the trajectory and not the time span, therefore it *must* be used together with the
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan` but should *not* be mixed with
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`.
        
            Parameters:
                inertialFrame (org.orekit.frames.Frame): inertial frame used for spacecraft positions/velocities/quaternions
                positionsVelocities (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<org.orekit.utils.TimeStampedPVCoordinates> positionsVelocities): satellite position and velocity (m and m/s in inertial frame)
                pvInterpolationNumber (int): number of points to use for position/velocity interpolation
                pvFilter (org.orekit.utils.CartesianDerivativesFilter): filter for derivatives from the sample to use in position/velocity interpolation
                quaternions (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.util.List?is`<org.orekit.utils.TimeStampedAngularCoordinates> quaternions): satellite quaternions with respect to inertial frame
                aInterpolationNumber (int): number of points to use for attitude interpolation
                aFilter (org.orekit.utils.AngularDerivativesFilter): filter for derivatives from the sample to use in attitude interpolation
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getPositionsVelocities`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getPVInterpolationNumber`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getPVInterpolationNumber`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getQuaternions`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getAInterpolationNumber`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.getAFilter`
        
            Set the spacecraft trajectory.
        
            This method set only the trajectory and not the time span, therefore it *must* be used together with the
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan` but should *not* be mixed with
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`.
        
            Parameters:
                interpolationStep (double): step to use for inertial/Earth/spacecraft transforms interpolations (s)
                interpolationNumber (int): number of points to use for inertial/Earth/spacecraft transforms interpolations
                pvFilter (org.orekit.utils.CartesianDerivativesFilter): filter for derivatives from the sample to use in position/velocity interpolation
                aFilter (org.orekit.utils.AngularDerivativesFilter): filter for derivatives from the sample to use in attitude interpolation
                propagator (org.orekit.propagation.Propagator): global propagator
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`
        
        
        """
        ...
    @typing.overload
    def setTrajectory(self, frame: org.orekit.frames.Frame, list: java.util.List[org.orekit.utils.TimeStampedPVCoordinates], int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, list2: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int2: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter) -> 'RuggedBuilder': ...
    @typing.overload
    def setTrajectory(self, inertialFrameId: InertialFrameId, list: java.util.List[org.orekit.utils.TimeStampedPVCoordinates], int: int, cartesianDerivativesFilter: org.orekit.utils.CartesianDerivativesFilter, list2: java.util.List[org.orekit.utils.TimeStampedAngularCoordinates], int2: int, angularDerivativesFilter: org.orekit.utils.AngularDerivativesFilter) -> 'RuggedBuilder': ...
    def setTrajectoryAndTimeSpan(self, inputStream: java.io.InputStream) -> 'RuggedBuilder':
        """
            Set both the spacecraft trajectory and the time span.
        
            This method set both the trajectory and the time span in a tightly coupled way, therefore it should *not* be mixed with
            the individual methods :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
            or :meth:`~org.orekit.rugged.api.RuggedBuilder.setTimeSpan`.
        
            Parameters:
                storageStream (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.io.InputStream?is`): stream from where to read previous instance :meth:`~org.orekit.rugged.api.RuggedBuilder.storeInterpolator` (caller
                    opened it and remains responsible for closing it)
        
            Returns:
                the builder instance
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.storeInterpolator`
        
        
        """
        ...
    def storeInterpolator(self, outputStream: java.io.OutputStream) -> None:
        """
            Store frames transform interpolator.
        
            This method allows to reuse the interpolator built in one instance, to build another instance by calling
            :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`. This reduces the builder initialization time as
            setting up the interpolator can be long, it is mainly intended to be used when several runs are done (for example in an
            image processing chain) with the same configuration.
        
            This method must be called *after* both the ellipsoid and trajectory have been set.
        
            Parameters:
                storageStream (:class:`~org.orekit.rugged.api.https:.docs.oracle.com.javase.8.docs.api.java.io.OutputStream?is`): stream where to store the interpolator (caller opened it and remains responsible for closing it)
        
            Also see:
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setEllipsoid`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setEllipsoid`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`, :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectory`,
                :meth:`~org.orekit.rugged.api.RuggedBuilder.setTrajectoryAndTimeSpan`
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.api")``.

    AlgorithmId: typing.Type[AlgorithmId]
    BodyRotatingFrameId: typing.Type[BodyRotatingFrameId]
    EllipsoidId: typing.Type[EllipsoidId]
    InertialFrameId: typing.Type[InertialFrameId]
    Rugged: typing.Type[Rugged]
    RuggedBuilder: typing.Type[RuggedBuilder]
