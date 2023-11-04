import java.io
import java.util.stream
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.los
import org.orekit.rugged.utils
import org.orekit.time
import org.orekit.utils
import typing



class LineDatation:
    """
    public interface LineDatation
    
        Interface representing line datation model.
    
        Also see:
            :class:`~org.orekit.rugged.linesensor.LinearLineDatation`
    """
    def getDate(self, double: float) -> org.orekit.time.AbsoluteDate:
        """
            Get the date for a given line.
        
            Parameters:
                lineNumber (double): line number
        
            Returns:
                date at which line is acquired
        
        
        """
        ...
    def getLine(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the line for a given date.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date
        
            Returns:
                line number
        
        
        """
        ...
    def getRate(self, double: float) -> float:
        """
            Get the rate of lines scanning.
        
            Parameters:
                lineNumber (double): line number
        
            Returns:
                rate of lines scanning (lines / seconds)
        
        
        """
        ...

class LineSensor:
    """
    public class LineSensor extends :class:`~org.orekit.rugged.linesensor.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Line sensor model.
    """
    def __init__(self, string: str, lineDatation: LineDatation, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, timeDependentLOS: org.orekit.rugged.los.TimeDependentLOS): ...
    def dumpRate(self, double: float) -> None:
        """
            Dump the rate for the current line number.
        
            Parameters:
                lineNumber (double): line number
        
        
        """
        ...
    def getDate(self, double: float) -> org.orekit.time.AbsoluteDate:
        """
            Get the date.
        
            Parameters:
                lineNumber (double): line number
        
            Returns:
                date corresponding to line number
        
        
        """
        ...
    @typing.overload
    def getLOS(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the pixel normalized line-of-sight at some date.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): current date
                i (int): pixel index (must be between 0 and :meth:`~org.orekit.rugged.linesensor.LineSensor.getNbPixels` - 1
        
            Returns:
                pixel normalized line-of-sight
        
            Get the pixel normalized interpolated line-of-sight at some date.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): current date
                i (double): pixel index (must be between 0 and :meth:`~org.orekit.rugged.linesensor.LineSensor.getNbPixels` - 1
        
            Returns:
                pixel normalized line-of-sight
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    def getLOS(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _getLOSDerivatives_0__T = typing.TypeVar('_getLOSDerivatives_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    _getLOSDerivatives_1__T = typing.TypeVar('_getLOSDerivatives_1__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def getLOSDerivatives(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives_0__T]:
        """
            Get the pixel normalized line-of-sight at some date, and their derivatives with respect to estimated parameters.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): current date
                i (int): pixel index (must be between 0 and :meth:`~org.orekit.rugged.linesensor.LineSensor.getNbPixels` - 1
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
            Returns:
                pixel normalized line-of-sight
        
            Get the pixel normalized line-of-sight at some date, and their derivatives with respect to estimated parameters.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): current date
                i (double): pixel index (must be between 0 and :meth:`~org.orekit.rugged.linesensor.LineSensor.getNbPixels` - 1
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
            Returns:
                pixel normalized line-of-sight
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    def getLOSDerivatives(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives_1__T]: ...
    def getLine(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the line number.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date
        
            Returns:
                line number corresponding to date
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the sensor.
        
            Returns:
                name of the sensor
        
        
        """
        ...
    def getNbPixels(self) -> int:
        """
            Get the number of pixels.
        
            Returns:
                number of pixels
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
            Get the drivers for LOS parameters.
        
            Returns:
                drivers for LOS parameters
        
            Since:
                2.0
        
        
        """
        ...
    def getPosition(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the sensor position.
        
            Returns:
                position
        
        
        """
        ...
    def getRate(self, double: float) -> float:
        """
            Get the rate of lines scanning.
        
            Parameters:
                lineNumber (double): line number
        
            Returns:
                rate of lines scanning (lines / seconds)
        
        
        """
        ...

class SensorMeanPlaneCrossing:
    """
    public class SensorMeanPlaneCrossing extends :class:`~org.orekit.rugged.linesensor.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class dedicated to find when ground point crosses mean sensor plane.
    
        This class is used in the first stage of inverse location.
    """
    @typing.overload
    def __init__(self, lineSensor: LineSensor, spacecraftToObservedBody: org.orekit.rugged.utils.SpacecraftToObservedBody, int: int, int2: int, boolean: bool, boolean2: bool, int3: int, double: float): ...
    @typing.overload
    def __init__(self, lineSensor: LineSensor, spacecraftToObservedBody: org.orekit.rugged.utils.SpacecraftToObservedBody, int: int, int2: int, boolean: bool, boolean2: bool, int3: int, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, stream: java.util.stream.Stream['SensorMeanPlaneCrossing.CrossingResult']): ...
    def find(self, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'SensorMeanPlaneCrossing.CrossingResult':
        """
            Find mean plane crossing.
        
            Parameters:
                target (org.hipparchus.geometry.euclidean.threed.Vector3D): target ground point
        
            Returns:
                line number and target direction at mean plane crossing, or null if search interval does not bracket a solution
        
        
        """
        ...
    def getAccuracy(self) -> float:
        """
            Get the accuracy to use for finding crossing line number.
        
            Returns:
                accuracy to use for finding crossing line number
        
        
        """
        ...
    def getCachedResults(self) -> java.util.stream.Stream['SensorMeanPlaneCrossing.CrossingResult']: ...
    def getMaxEval(self) -> int:
        """
            Get the maximum number of evaluations.
        
            Returns:
                maximum number of evaluations
        
        
        """
        ...
    def getMaxLine(self) -> int:
        """
            Get the maximum line number in the search interval.
        
            Returns:
                maximum line number in the search interval
        
        
        """
        ...
    def getMeanPlaneNormal(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get the mean plane normal.
        
            The normal is oriented such traversing pixels in increasing indices order corresponds is consistent with trigonometric
            order (i.e. counterclockwise).
        
            Returns:
                mean plane normal
        
        
        """
        ...
    def getMinLine(self) -> int:
        """
            Get the minimum line number in the search interval.
        
            Returns:
                minimum line number in the search interval
        
        
        """
        ...
    def getScToBody(self) -> org.orekit.rugged.utils.SpacecraftToObservedBody:
        """
            Get converter between spacecraft and body.
        
            Returns:
                converter between spacecraft and body
        
        
        """
        ...
    def getSensor(self) -> LineSensor:
        """
            Get the underlying sensor.
        
            Returns:
                underlying sensor
        
        
        """
        ...
    class CrossingResult:
        def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D3: org.hipparchus.geometry.euclidean.threed.Vector3D): ...
        def getDate(self) -> org.orekit.time.AbsoluteDate: ...
        def getLine(self) -> float: ...
        def getTarget(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
        def getTargetDirection(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
        def getTargetDirectionDerivative(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class SensorPixel(java.io.Serializable):
    """
    public class SensorPixel extends :class:`~org.orekit.rugged.linesensor.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.rugged.linesensor.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable?is`
    
        Container for sensor pixel.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, double: float, double2: float): ...
    def getLineNumber(self) -> float:
        """
            Get the line number.
        
            Returns:
                line number
        
        
        """
        ...
    def getPixelNumber(self) -> float:
        """
            Get the pixel number.
        
            Returns:
                pixel number
        
        
        """
        ...

class SensorPixelCrossing:
    """
    public class SensorPixelCrossing extends :class:`~org.orekit.rugged.linesensor.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Class devoted to locate where ground point crosses a sensor line.
    
        This class is used in the first stage of inverse location.
    """
    def __init__(self, lineSensor: LineSensor, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, vector3D2: org.hipparchus.geometry.euclidean.threed.Vector3D, int: int, double: float): ...
    def locatePixel(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Locate pixel along sensor line.
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): current date
        
            Returns:
                pixel location (:code:`Double.NaN` if the first and last pixels of the line do not bracket a location)
        
        
        """
        ...

class LinearLineDatation(LineDatation):
    """
    public class LinearLineDatation extends :class:`~org.orekit.rugged.linesensor.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.rugged.linesensor.LineDatation`
    
        Linear model for :class:`~org.orekit.rugged.linesensor.LineDatation`.
    
        Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, absoluteDate: org.orekit.time.AbsoluteDate, double: float, double2: float): ...
    def getDate(self, double: float) -> org.orekit.time.AbsoluteDate:
        """
            Get the date for a given line.
        
            Specified by:
                :meth:`~org.orekit.rugged.linesensor.LineDatation.getDate` in
                interface :class:`~org.orekit.rugged.linesensor.LineDatation`
        
            Parameters:
                lineNumber (double): line number
        
            Returns:
                date at which line is acquired
        
        
        """
        ...
    def getLine(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float:
        """
            Get the line for a given date.
        
            Specified by:
                :meth:`~org.orekit.rugged.linesensor.LineDatation.getLine` in
                interface :class:`~org.orekit.rugged.linesensor.LineDatation`
        
            Parameters:
                date (org.orekit.time.AbsoluteDate): date
        
            Returns:
                line number
        
        
        """
        ...
    def getRate(self, double: float) -> float:
        """
            Get the rate of lines scanning.
        
            Specified by:
                :meth:`~org.orekit.rugged.linesensor.LineDatation.getRate` in
                interface :class:`~org.orekit.rugged.linesensor.LineDatation`
        
            Parameters:
                lineNumber (double): line number
        
            Returns:
                rate of lines scanning (lines / seconds)
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.linesensor")``.

    LineDatation: typing.Type[LineDatation]
    LineSensor: typing.Type[LineSensor]
    LinearLineDatation: typing.Type[LinearLineDatation]
    SensorMeanPlaneCrossing: typing.Type[SensorMeanPlaneCrossing]
    SensorPixel: typing.Type[SensorPixel]
    SensorPixelCrossing: typing.Type[SensorPixelCrossing]
