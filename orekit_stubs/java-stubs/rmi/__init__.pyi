import java.io
import java.lang
import java.rmi.activation
import java.rmi.dgc
import java.rmi.registry
import java.rmi.server
import typing



class AlreadyBoundException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

_MarshalledObject__T = typing.TypeVar('_MarshalledObject__T')  # <T>
class MarshalledObject(java.io.Serializable, typing.Generic[_MarshalledObject__T]):
    def __init__(self, t: _MarshalledObject__T): ...
    def equals(self, object: typing.Any) -> bool: ...
    def get(self) -> _MarshalledObject__T: ...
    def hashCode(self) -> int: ...

class Naming:
    @staticmethod
    def bind(string: str, remote: 'Remote') -> None: ...
    @staticmethod
    def list(string: str) -> typing.List[str]: ...
    @staticmethod
    def lookup(string: str) -> 'Remote': ...
    @staticmethod
    def rebind(string: str, remote: 'Remote') -> None: ...
    @staticmethod
    def unbind(string: str) -> None: ...

class NotBoundException(java.lang.Exception):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class RMISecurityException(java.lang.SecurityException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...

class RMISecurityManager(java.lang.SecurityManager):
    def __init__(self): ...

class Remote: ...

class RemoteException(java.io.IOException):
    detail: java.lang.Throwable = ...
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, throwable: java.lang.Throwable): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getMessage(self) -> str: ...

class AccessException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ConnectException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ConnectIOException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class MarshalException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class NoSuchObjectException(RemoteException):
    def __init__(self, string: str): ...

class ServerError(RemoteException):
    def __init__(self, string: str, error: java.lang.Error): ...

class ServerException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class ServerRuntimeException(RemoteException):
    def __init__(self, string: str, exception: java.lang.Exception): ...

class StubNotFoundException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnexpectedException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnknownHostException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...

class UnmarshalException(RemoteException):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, exception: java.lang.Exception): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi")``.

    AccessException: typing.Type[AccessException]
    AlreadyBoundException: typing.Type[AlreadyBoundException]
    ConnectException: typing.Type[ConnectException]
    ConnectIOException: typing.Type[ConnectIOException]
    MarshalException: typing.Type[MarshalException]
    MarshalledObject: typing.Type[MarshalledObject]
    Naming: typing.Type[Naming]
    NoSuchObjectException: typing.Type[NoSuchObjectException]
    NotBoundException: typing.Type[NotBoundException]
    RMISecurityException: typing.Type[RMISecurityException]
    RMISecurityManager: typing.Type[RMISecurityManager]
    Remote: typing.Type[Remote]
    RemoteException: typing.Type[RemoteException]
    ServerError: typing.Type[ServerError]
    ServerException: typing.Type[ServerException]
    ServerRuntimeException: typing.Type[ServerRuntimeException]
    StubNotFoundException: typing.Type[StubNotFoundException]
    UnexpectedException: typing.Type[UnexpectedException]
    UnknownHostException: typing.Type[UnknownHostException]
    UnmarshalException: typing.Type[UnmarshalException]
    activation: java.rmi.activation.__module_protocol__
    dgc: java.rmi.dgc.__module_protocol__
    registry: java.rmi.registry.__module_protocol__
    server: java.rmi.server.__module_protocol__
