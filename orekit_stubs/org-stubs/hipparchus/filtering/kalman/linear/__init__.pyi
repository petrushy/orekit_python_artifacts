import org.hipparchus.filtering.kalman
import org.hipparchus.linear
import typing



class LinearEvolution:
    def __init__(self, realMatrix: org.hipparchus.linear.RealMatrix, realMatrix2: org.hipparchus.linear.RealMatrix, realVector: org.hipparchus.linear.RealVector, realMatrix3: org.hipparchus.linear.RealMatrix, realMatrix4: org.hipparchus.linear.RealMatrix): ...
    def getCommand(self) -> org.hipparchus.linear.RealVector: ...
    def getControlMatrix(self) -> org.hipparchus.linear.RealMatrix: ...
    def getMeasurementJacobian(self) -> org.hipparchus.linear.RealMatrix: ...
    def getProcessNoiseMatrix(self) -> org.hipparchus.linear.RealMatrix: ...
    def getStateTransitionMatrix(self) -> org.hipparchus.linear.RealMatrix: ...

_LinearKalmanFilter__T = typing.TypeVar('_LinearKalmanFilter__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class LinearKalmanFilter(org.hipparchus.filtering.kalman.AbstractKalmanFilter[_LinearKalmanFilter__T], typing.Generic[_LinearKalmanFilter__T]):
    def __init__(self, matrixDecomposer: org.hipparchus.linear.MatrixDecomposer, linearProcess: 'LinearProcess'[_LinearKalmanFilter__T], processEstimate: org.hipparchus.filtering.kalman.ProcessEstimate): ...
    def estimationStep(self, t: _LinearKalmanFilter__T) -> org.hipparchus.filtering.kalman.ProcessEstimate: ...

_LinearProcess__T = typing.TypeVar('_LinearProcess__T', bound=org.hipparchus.filtering.kalman.Measurement)  # <T>
class LinearProcess(typing.Generic[_LinearProcess__T]):
    def getEvolution(self, t: _LinearProcess__T) -> LinearEvolution: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.filtering.kalman.linear")``.

    LinearEvolution: typing.Type[LinearEvolution]
    LinearKalmanFilter: typing.Type[LinearKalmanFilter]
    LinearProcess: typing.Type[LinearProcess]
