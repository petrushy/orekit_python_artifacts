import java.lang
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.analysis.solvers
import org.hipparchus.ode
import org.hipparchus.ode.sampling
import typing



class Action(java.lang.Enum['Action']):
    STOP: typing.ClassVar['Action'] = ...
    RESET_STATE: typing.ClassVar['Action'] = ...
    RESET_DERIVATIVES: typing.ClassVar['Action'] = ...
    CONTINUE: typing.ClassVar['Action'] = ...
    RESET_EVENTS: typing.ClassVar['Action'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'Action': ...
    @staticmethod
    def values() -> typing.List['Action']: ...

class EventHandlerConfiguration:
    def getConvergence(self) -> float: ...
    def getEventHandler(self) -> 'ODEEventHandler': ...
    def getMaxCheckInterval(self) -> float: ...
    def getMaxIterationCount(self) -> int: ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]: ...

_FieldEventHandlerConfiguration__T = typing.TypeVar('_FieldEventHandlerConfiguration__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventHandlerConfiguration(typing.Generic[_FieldEventHandlerConfiguration__T]):
    def getConvergence(self) -> _FieldEventHandlerConfiguration__T: ...
    def getEventHandler(self) -> 'FieldODEEventHandler'[_FieldEventHandlerConfiguration__T]: ...
    def getMaxCheckInterval(self) -> float: ...
    def getMaxIterationCount(self) -> int: ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldEventHandlerConfiguration__T]: ...

_FieldODEEventHandler__T = typing.TypeVar('_FieldODEEventHandler__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldODEEventHandler(typing.Generic[_FieldODEEventHandler__T]):
    def eventOccurred(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], boolean: bool) -> Action: ...
    def g(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T]) -> _FieldODEEventHandler__T: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T], t: _FieldODEEventHandler__T) -> None: ...
    def resetState(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldODEEventHandler__T]) -> org.hipparchus.ode.FieldODEState[_FieldODEEventHandler__T]: ...

class FilterType(java.lang.Enum['FilterType']):
    TRIGGER_ONLY_DECREASING_EVENTS: typing.ClassVar['FilterType'] = ...
    TRIGGER_ONLY_INCREASING_EVENTS: typing.ClassVar['FilterType'] = ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'FilterType': ...
    @staticmethod
    def values() -> typing.List['FilterType']: ...

class ODEEventHandler:
    def eventOccurred(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> Action: ...
    def g(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> float: ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None: ...
    def resetState(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> org.hipparchus.ode.ODEState: ...

class EventFilter(ODEEventHandler):
    def __init__(self, oDEEventHandler: ODEEventHandler, filterType: FilterType): ...
    def eventOccurred(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, boolean: bool) -> Action: ...
    def g(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> float: ...
    def init(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, double: float) -> None: ...
    def resetState(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> org.hipparchus.ode.ODEState: ...

class EventState(EventHandlerConfiguration):
    def __init__(self, oDEEventHandler: ODEEventHandler, double: float, double2: float, int: int, bracketedUnivariateSolver: org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]): ...
    def doEvent(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative) -> 'EventState.EventOccurrence': ...
    def evaluateStep(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool: ...
    def getConvergence(self) -> float: ...
    def getEventHandler(self) -> ODEEventHandler: ...
    def getEventTime(self) -> float: ...
    def getMaxCheckInterval(self) -> float: ...
    def getMaxIterationCount(self) -> int: ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedUnivariateSolver[org.hipparchus.analysis.UnivariateFunction]: ...
    def reinitializeBegin(self, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> None: ...
    def tryAdvance(self, oDEStateAndDerivative: org.hipparchus.ode.ODEStateAndDerivative, oDEStateInterpolator: org.hipparchus.ode.sampling.ODEStateInterpolator) -> bool: ...
    class EventOccurrence:
        def getAction(self) -> Action: ...
        def getNewState(self) -> org.hipparchus.ode.ODEState: ...
        def getStopTime(self) -> float: ...

_FieldEventFilter__T = typing.TypeVar('_FieldEventFilter__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventFilter(FieldODEEventHandler[_FieldEventFilter__T], typing.Generic[_FieldEventFilter__T]):
    def __init__(self, field: org.hipparchus.Field[_FieldEventFilter__T], fieldODEEventHandler: FieldODEEventHandler[_FieldEventFilter__T], filterType: FilterType): ...
    def eventOccurred(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T], boolean: bool) -> Action: ...
    def g(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T]) -> _FieldEventFilter__T: ...
    def init(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T], t: _FieldEventFilter__T) -> None: ...
    def resetState(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventFilter__T]) -> org.hipparchus.ode.FieldODEState[_FieldEventFilter__T]: ...

_FieldEventState__EventOccurrence__T = typing.TypeVar('_FieldEventState__EventOccurrence__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FieldEventState__T = typing.TypeVar('_FieldEventState__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldEventState(FieldEventHandlerConfiguration[_FieldEventState__T], typing.Generic[_FieldEventState__T]):
    def __init__(self, fieldODEEventHandler: FieldODEEventHandler[_FieldEventState__T], double: float, t: _FieldEventState__T, int: int, bracketedRealFieldUnivariateSolver: org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldEventState__T]): ...
    def doEvent(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T]) -> 'FieldEventState.EventOccurrence'[_FieldEventState__T]: ...
    def evaluateStep(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> bool: ...
    def getConvergence(self) -> _FieldEventState__T: ...
    def getEventHandler(self) -> FieldODEEventHandler[_FieldEventState__T]: ...
    def getEventTime(self) -> _FieldEventState__T: ...
    def getMaxCheckInterval(self) -> float: ...
    def getMaxIterationCount(self) -> int: ...
    def getSolver(self) -> org.hipparchus.analysis.solvers.BracketedRealFieldUnivariateSolver[_FieldEventState__T]: ...
    def reinitializeBegin(self, fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> None: ...
    def tryAdvance(self, fieldODEStateAndDerivative: org.hipparchus.ode.FieldODEStateAndDerivative[_FieldEventState__T], fieldODEStateInterpolator: org.hipparchus.ode.sampling.FieldODEStateInterpolator[_FieldEventState__T]) -> bool: ...
    class EventOccurrence(typing.Generic[_FieldEventState__EventOccurrence__T]):
        def getAction(self) -> Action: ...
        def getNewState(self) -> org.hipparchus.ode.FieldODEState[_FieldEventState__EventOccurrence__T]: ...
        def getStopTime(self) -> _FieldEventState__EventOccurrence__T: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.ode.events")``.

    Action: typing.Type[Action]
    EventFilter: typing.Type[EventFilter]
    EventHandlerConfiguration: typing.Type[EventHandlerConfiguration]
    EventState: typing.Type[EventState]
    FieldEventFilter: typing.Type[FieldEventFilter]
    FieldEventHandlerConfiguration: typing.Type[FieldEventHandlerConfiguration]
    FieldEventState: typing.Type[FieldEventState]
    FieldODEEventHandler: typing.Type[FieldODEEventHandler]
    FilterType: typing.Type[FilterType]
    ODEEventHandler: typing.Type[ODEEventHandler]
