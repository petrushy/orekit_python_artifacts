
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.net
import java.util
import jpype.protocol
import typing



class AboutHandler:
    def handleAbout(self, aboutEvent: 'AboutEvent') -> None: ...

class AppEvent(java.util.EventObject): ...

class OpenFilesHandler:
    def openFiles(self, openFilesEvent: 'OpenFilesEvent') -> None: ...

class OpenURIHandler:
    def openURI(self, openURIEvent: 'OpenURIEvent') -> None: ...

class PreferencesHandler:
    def handlePreferences(self, preferencesEvent: 'PreferencesEvent') -> None: ...

class PrintFilesHandler:
    def printFiles(self, printFilesEvent: 'PrintFilesEvent') -> None: ...

class QuitHandler:
    def handleQuitRequestWith(self, quitEvent: 'QuitEvent', quitResponse: 'QuitResponse') -> None: ...

class QuitResponse:
    def cancelQuit(self) -> None: ...
    def performQuit(self) -> None: ...

class QuitStrategy(java.lang.Enum['QuitStrategy']):
    NORMAL_EXIT: typing.ClassVar['QuitStrategy'] = ...
    CLOSE_ALL_WINDOWS: typing.ClassVar['QuitStrategy'] = ...
    _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'QuitStrategy': ...
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
    @staticmethod
    def values() -> typing.MutableSequence['QuitStrategy']: ...

class SystemEventListener(java.util.EventListener): ...

class AboutEvent(AppEvent):
    def __init__(self): ...

class AppForegroundEvent(AppEvent):
    def __init__(self): ...

class AppForegroundListener(SystemEventListener):
    def appMovedToBackground(self, appForegroundEvent: AppForegroundEvent) -> None: ...
    def appRaisedToForeground(self, appForegroundEvent: AppForegroundEvent) -> None: ...

class AppHiddenEvent(AppEvent):
    def __init__(self): ...

class AppHiddenListener(SystemEventListener):
    def appHidden(self, appHiddenEvent: AppHiddenEvent) -> None: ...
    def appUnhidden(self, appHiddenEvent: AppHiddenEvent) -> None: ...

class AppReopenedEvent(AppEvent):
    def __init__(self): ...

class AppReopenedListener(SystemEventListener):
    def appReopened(self, appReopenedEvent: AppReopenedEvent) -> None: ...

class FilesEvent(AppEvent):
    def getFiles(self) -> java.util.List[java.io.File]: ...

class OpenURIEvent(AppEvent):
    def __init__(self, uRI: java.net.URI): ...
    def getURI(self) -> java.net.URI: ...

class PreferencesEvent(AppEvent):
    def __init__(self): ...

class QuitEvent(AppEvent):
    def __init__(self): ...

class ScreenSleepEvent(AppEvent):
    def __init__(self): ...

class ScreenSleepListener(SystemEventListener):
    def screenAboutToSleep(self, screenSleepEvent: ScreenSleepEvent) -> None: ...
    def screenAwoke(self, screenSleepEvent: ScreenSleepEvent) -> None: ...

class SystemSleepEvent(AppEvent):
    def __init__(self): ...

class SystemSleepListener(SystemEventListener):
    def systemAboutToSleep(self, systemSleepEvent: SystemSleepEvent) -> None: ...
    def systemAwoke(self, systemSleepEvent: SystemSleepEvent) -> None: ...

class UserSessionEvent(AppEvent):
    def __init__(self, reason: 'UserSessionEvent.Reason'): ...
    def getReason(self) -> 'UserSessionEvent.Reason': ...
    class Reason(java.lang.Enum['UserSessionEvent.Reason']):
        UNSPECIFIED: typing.ClassVar['UserSessionEvent.Reason'] = ...
        CONSOLE: typing.ClassVar['UserSessionEvent.Reason'] = ...
        REMOTE: typing.ClassVar['UserSessionEvent.Reason'] = ...
        LOCK: typing.ClassVar['UserSessionEvent.Reason'] = ...
        _valueOf_1__T = typing.TypeVar('_valueOf_1__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'UserSessionEvent.Reason': ...
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_1__T], string: str) -> _valueOf_1__T: ...
        @staticmethod
        def values() -> typing.MutableSequence['UserSessionEvent.Reason']: ...

class UserSessionListener(SystemEventListener):
    def userSessionActivated(self, userSessionEvent: UserSessionEvent) -> None: ...
    def userSessionDeactivated(self, userSessionEvent: UserSessionEvent) -> None: ...

class OpenFilesEvent(FilesEvent):
    def __init__(self, list: java.util.List[typing.Union[java.io.File, jpype.protocol.SupportsPath]], string: str): ...
    def getSearchTerm(self) -> str: ...

class PrintFilesEvent(FilesEvent):
    def __init__(self, list: java.util.List[typing.Union[java.io.File, jpype.protocol.SupportsPath]]): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.awt.desktop")``.

    AboutEvent: typing.Type[AboutEvent]
    AboutHandler: typing.Type[AboutHandler]
    AppEvent: typing.Type[AppEvent]
    AppForegroundEvent: typing.Type[AppForegroundEvent]
    AppForegroundListener: typing.Type[AppForegroundListener]
    AppHiddenEvent: typing.Type[AppHiddenEvent]
    AppHiddenListener: typing.Type[AppHiddenListener]
    AppReopenedEvent: typing.Type[AppReopenedEvent]
    AppReopenedListener: typing.Type[AppReopenedListener]
    FilesEvent: typing.Type[FilesEvent]
    OpenFilesEvent: typing.Type[OpenFilesEvent]
    OpenFilesHandler: typing.Type[OpenFilesHandler]
    OpenURIEvent: typing.Type[OpenURIEvent]
    OpenURIHandler: typing.Type[OpenURIHandler]
    PreferencesEvent: typing.Type[PreferencesEvent]
    PreferencesHandler: typing.Type[PreferencesHandler]
    PrintFilesEvent: typing.Type[PrintFilesEvent]
    PrintFilesHandler: typing.Type[PrintFilesHandler]
    QuitEvent: typing.Type[QuitEvent]
    QuitHandler: typing.Type[QuitHandler]
    QuitResponse: typing.Type[QuitResponse]
    QuitStrategy: typing.Type[QuitStrategy]
    ScreenSleepEvent: typing.Type[ScreenSleepEvent]
    ScreenSleepListener: typing.Type[ScreenSleepListener]
    SystemEventListener: typing.Type[SystemEventListener]
    SystemSleepEvent: typing.Type[SystemSleepEvent]
    SystemSleepListener: typing.Type[SystemSleepListener]
    UserSessionEvent: typing.Type[UserSessionEvent]
    UserSessionListener: typing.Type[UserSessionListener]
