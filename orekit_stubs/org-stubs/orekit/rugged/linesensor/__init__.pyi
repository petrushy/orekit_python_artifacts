
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

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
    Interface representing line datation model.
    
    Also see:
        LinearLineDatation
    """
    def getDate(self, lineNumber: float) -> org.orekit.time.AbsoluteDate:
        """
        Get the date for a given line.
        
        Parameters:
            lineNumber (double): line number
        
        Returns:
            date at which line is acquired
        
        
        """
        ...
    def getLine(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the line for a given date.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date
        
        Returns:
            line number
        
        
        """
        ...
    def getRate(self, lineNumber: float) -> float:
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
    Line sensor model.
    """
    def __init__(self, name: str, datationModel: LineDatation, position: org.hipparchus.geometry.euclidean.threed.Vector3D, los: org.orekit.rugged.los.TimeDependentLOS):
        """
        Simple constructor.
        
        Parameters:
            name (String): name of the sensor
            datationModel (LineDatation): datation model
            position (org.hipparchus.geometry.euclidean.threed.Vector3D): sensor position in spacecraft frame
            los (TimeDependentLOS): pixels lines-of-sight in spacecraft frame
        
        Also see:
            LOSBuilder
        
        
        """
        ...
    def dumpRate(self, lineNumber: float) -> None:
        """
        Dump the rate for the current line number.
        
        Parameters:
            lineNumber (double): line number
        
        
        """
        ...
    def getDate(self, lineNumber: float) -> org.orekit.time.AbsoluteDate:
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
            i (int): pixel index (must be between 0 and getNbPixels - 1
        
        Returns:
            pixel normalized line-of-sight
        
        Get the pixel normalized interpolated line-of-sight at some date.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): current date
            i (double): pixel index (must be between 0 and getNbPixels - 1
        
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
            i (int): pixel index (must be between 0 and getNbPixels - 1
            generator (DerivativeGenerator<T> generator): generator to use for building Derivative instances
        
        Returns:
            pixel normalized line-of-sight
        
        Get the pixel normalized line-of-sight at some date, and their derivatives with respect to estimated parameters.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): current date
            i (double): pixel index (must be between 0 and getNbPixels - 1
            generator (DerivativeGenerator<T> generator): generator to use for building Derivative instances
        
        Returns:
            pixel normalized line-of-sight
        
        Since:
            2.0
        
        
        """
        ...
    @typing.overload
    def getLOSDerivatives(self, absoluteDate: org.orekit.time.AbsoluteDate, int: int, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives_1__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives_1__T]: ...
    def getLine(self, date: org.orekit.time.AbsoluteDate) -> float:
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
    def getRate(self, lineNumber: float) -> float:
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
    Class dedicated to find when ground point crosses mean sensor plane.
    
    This class is used in the first stage of inverse location.
    """
    @typing.overload
    def __init__(self, lineSensor: LineSensor, spacecraftToObservedBody: org.orekit.rugged.utils.SpacecraftToObservedBody, int: int, int2: int, boolean: bool, boolean2: bool, int3: int, double: float): ...
    @typing.overload
    def __init__(self, lineSensor: LineSensor, spacecraftToObservedBody: org.orekit.rugged.utils.SpacecraftToObservedBody, int: int, int2: int, boolean: bool, boolean2: bool, int3: int, double: float, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, stream: java.util.stream.Stream['SensorMeanPlaneCrossing.CrossingResult']): ...
    def find(self, target: org.hipparchus.geometry.euclidean.threed.Vector3D) -> 'SensorMeanPlaneCrossing.CrossingResult':
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
    def getCachedResults(self) -> java.util.stream.Stream['SensorMeanPlaneCrossing.CrossingResult']:
        """
        Get cached previous results.
        
        Returns:
            cached previous results
        
        
        """
        ...
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
        
        The normal is oriented such traversing pixels in increasing indices order corresponds is consistent with trigonometric order (i.e. counterclockwise).
        
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
    Container for sensor pixel.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        serialized
    """
    def __init__(self, lineNumber: float, pixelNumber: float):
        """
        Build a new instance.
        
        Parameters:
            lineNumber (double): line number
            pixelNumber (double): pixel number
        
        
        """
        ...
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
    Class devoted to locate where ground point crosses a sensor line.
    
    This class is used in the first stage of inverse location.
    """
    def __init__(self, sensor: LineSensor, meanNormal: org.hipparchus.geometry.euclidean.threed.Vector3D, targetDirection: org.hipparchus.geometry.euclidean.threed.Vector3D, maxEval: int, accuracy: float):
        """
        Simple constructor.
        
        Parameters:
            sensor (LineSensor): sensor to consider
            meanNormal (org.hipparchus.geometry.euclidean.threed.Vector3D): mean plane normal of the line sensor
            targetDirection (org.hipparchus.geometry.euclidean.threed.Vector3D): target direction in spacecraft frame
            maxEval (int): maximum number of evaluations
            accuracy (double): accuracy to use for finding crossing line number
        
        
        """
        ...
    def locatePixel(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Locate pixel along sensor line.
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): current date
        
        Returns:
            pixel location (NaN if the first and last pixels of the line do not bracket a location)
        
        
        """
        ...

class LinearLineDatation(LineDatation):
    """
    Linear model for LineDatation.
    
    Instances of this class are guaranteed to be immutable.
    """
    def __init__(self, referenceDate: org.orekit.time.AbsoluteDate, referenceLine: float, rate: float):
        """
        Simple constructor.
        
        Parameters:
            referenceDate (org.orekit.time.AbsoluteDate): reference date
            referenceLine (double): line number at reference date
            rate (double): rate of lines scanning (lines / seconds)
        
        
        """
        ...
    def getDate(self, lineNumber: float) -> org.orekit.time.AbsoluteDate:
        """
        Get the date for a given line.
        
        Specified by: getDate in interface LineDatation
        
        Parameters:
            lineNumber (double): line number
        
        Returns:
            date at which line is acquired
        
        
        """
        ...
    def getLine(self, date: org.orekit.time.AbsoluteDate) -> float:
        """
        Get the line for a given date.
        
        Specified by: getLine in interface LineDatation
        
        Parameters:
            date (org.orekit.time.AbsoluteDate): date
        
        Returns:
            line number
        
        
        """
        ...
    def getRate(self, lineNumber: float) -> float:
        """
        Get the rate of lines scanning.
        
        Specified by: getRate in interface LineDatation
        
        Parameters:
            lineNumber (double): line number
        
        Returns:
            rate of lines scanning (lines / seconds)
        
        
        """
        ...

class PythonLineDatation(LineDatation):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getDate(self, double: float) -> org.orekit.time.AbsoluteDate: ...
    def getLine(self, absoluteDate: org.orekit.time.AbsoluteDate) -> float: ...
    def getRate(self, double: float) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.linesensor")``.

    LineDatation: typing.Type[LineDatation]
    LineSensor: typing.Type[LineSensor]
    LinearLineDatation: typing.Type[LinearLineDatation]
    PythonLineDatation: typing.Type[PythonLineDatation]
    SensorMeanPlaneCrossing: typing.Type[SensorMeanPlaneCrossing]
    SensorPixel: typing.Type[SensorPixel]
    SensorPixelCrossing: typing.Type[SensorPixelCrossing]
