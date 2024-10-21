import java.io
import org.hipparchus.linear
import org.hipparchus.stat.regression.class-use
import typing



class MultipleLinearRegression:
    def estimateRegressandVariance(self) -> float: ...
    def estimateRegressionParameters(self) -> typing.List[float]: ...
    def estimateRegressionParametersStandardErrors(self) -> typing.List[float]: ...
    def estimateRegressionParametersVariance(self) -> typing.List[typing.List[float]]: ...
    def estimateResiduals(self) -> typing.List[float]: ...

class RegressionResults(java.io.Serializable):
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], boolean: bool, long: int, int: int, double3: float, double4: float, double5: float, boolean2: bool, boolean3: bool): ...
    def getAdjustedRSquared(self) -> float: ...
    def getCovarianceOfParameters(self, int: int, int2: int) -> float: ...
    def getErrorSumSquares(self) -> float: ...
    def getMeanSquareError(self) -> float: ...
    def getN(self) -> int: ...
    def getNumberOfParameters(self) -> int: ...
    def getParameterEstimate(self, int: int) -> float: ...
    def getParameterEstimates(self) -> typing.List[float]: ...
    def getRSquared(self) -> float: ...
    def getRegressionSumSquares(self) -> float: ...
    def getStdErrorOfEstimate(self, int: int) -> float: ...
    def getStdErrorOfEstimates(self) -> typing.List[float]: ...
    def getTotalSumSquares(self) -> float: ...
    def hasIntercept(self) -> bool: ...

class UpdatingMultipleLinearRegression:
    def addObservation(self, doubleArray: typing.List[float], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> None: ...
    def clear(self) -> None: ...
    def getN(self) -> int: ...
    def hasIntercept(self) -> bool: ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.List[int]) -> RegressionResults: ...

class AbstractMultipleLinearRegression(MultipleLinearRegression):
    def __init__(self): ...
    def estimateErrorVariance(self) -> float: ...
    def estimateRegressandVariance(self) -> float: ...
    def estimateRegressionParameters(self) -> typing.List[float]: ...
    def estimateRegressionParametersStandardErrors(self) -> typing.List[float]: ...
    def estimateRegressionParametersVariance(self) -> typing.List[typing.List[float]]: ...
    def estimateRegressionStandardError(self) -> float: ...
    def estimateResiduals(self) -> typing.List[float]: ...
    def isNoIntercept(self) -> bool: ...
    def newSampleData(self, doubleArray: typing.List[float], int: int, int2: int) -> None: ...
    def setNoIntercept(self, boolean: bool) -> None: ...

class MillerUpdatingRegression(UpdatingMultipleLinearRegression):
    @typing.overload
    def __init__(self, int: int, boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool, double: float): ...
    def addObservation(self, doubleArray: typing.List[float], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> None: ...
    def clear(self) -> None: ...
    def getDiagonalOfHatMatrix(self, doubleArray: typing.List[float]) -> float: ...
    def getN(self) -> int: ...
    def getOrderOfRegressors(self) -> typing.List[int]: ...
    def getPartialCorrelations(self, int: int) -> typing.List[float]: ...
    def hasIntercept(self) -> bool: ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, int: int) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.List[int]) -> RegressionResults: ...

class SimpleRegression(java.io.Serializable, UpdatingMultipleLinearRegression):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, boolean: bool): ...
    @typing.overload
    def addData(self, double: float, double2: float) -> None: ...
    @typing.overload
    def addData(self, doubleArray: typing.List[typing.List[float]]) -> None: ...
    def addObservation(self, doubleArray: typing.List[float], double2: float) -> None: ...
    def addObservations(self, doubleArray: typing.List[typing.List[float]], doubleArray2: typing.List[float]) -> None: ...
    def append(self, simpleRegression: 'SimpleRegression') -> None: ...
    def clear(self) -> None: ...
    def getIntercept(self) -> float: ...
    def getInterceptStdErr(self) -> float: ...
    def getMeanSquareError(self) -> float: ...
    def getN(self) -> int: ...
    def getR(self) -> float: ...
    def getRSquare(self) -> float: ...
    def getRegressionSumSquares(self) -> float: ...
    def getSignificance(self) -> float: ...
    def getSlope(self) -> float: ...
    @typing.overload
    def getSlopeConfidenceInterval(self) -> float: ...
    @typing.overload
    def getSlopeConfidenceInterval(self, double: float) -> float: ...
    def getSlopeStdErr(self) -> float: ...
    def getSumOfCrossProducts(self) -> float: ...
    def getSumSquaredErrors(self) -> float: ...
    def getTotalSumSquares(self) -> float: ...
    def getXSumSquares(self) -> float: ...
    def hasIntercept(self) -> bool: ...
    def predict(self, double: float) -> float: ...
    @typing.overload
    def regress(self) -> RegressionResults: ...
    @typing.overload
    def regress(self, intArray: typing.List[int]) -> RegressionResults: ...
    @typing.overload
    def removeData(self, double: float, double2: float) -> None: ...
    @typing.overload
    def removeData(self, doubleArray: typing.List[typing.List[float]]) -> None: ...

class GLSMultipleLinearRegression(AbstractMultipleLinearRegression):
    def __init__(self): ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], int: int, int2: int) -> None: ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]], doubleArray3: typing.List[typing.List[float]]) -> None: ...

class OLSMultipleLinearRegression(AbstractMultipleLinearRegression):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, double: float): ...
    def calculateAdjustedRSquared(self) -> float: ...
    def calculateHat(self) -> org.hipparchus.linear.RealMatrix: ...
    def calculateRSquared(self) -> float: ...
    def calculateResidualSumOfSquares(self) -> float: ...
    def calculateTotalSumOfSquares(self) -> float: ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], doubleArray2: typing.List[typing.List[float]]) -> None: ...
    @typing.overload
    def newSampleData(self, doubleArray: typing.List[float], int: int, int2: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.regression")``.

    AbstractMultipleLinearRegression: typing.Type[AbstractMultipleLinearRegression]
    GLSMultipleLinearRegression: typing.Type[GLSMultipleLinearRegression]
    MillerUpdatingRegression: typing.Type[MillerUpdatingRegression]
    MultipleLinearRegression: typing.Type[MultipleLinearRegression]
    OLSMultipleLinearRegression: typing.Type[OLSMultipleLinearRegression]
    RegressionResults: typing.Type[RegressionResults]
    SimpleRegression: typing.Type[SimpleRegression]
    UpdatingMultipleLinearRegression: typing.Type[UpdatingMultipleLinearRegression]
    class-use: org.hipparchus.stat.regression.class-use.__module_protocol__
