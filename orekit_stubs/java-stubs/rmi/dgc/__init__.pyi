
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.rmi
import java.rmi.server
import jpype
import typing



class DGC(java.rmi.Remote):
    def clean(self, objIDArray: typing.Union[typing.List[java.rmi.server.ObjID], jpype.JArray], long: int, vMID: 'VMID', boolean: bool) -> None: ...
    def dirty(self, objIDArray: typing.Union[typing.List[java.rmi.server.ObjID], jpype.JArray], long: int, lease: 'Lease') -> 'Lease': ...

class Lease(java.io.Serializable):
    def __init__(self, vMID: 'VMID', long: int): ...
    def getVMID(self) -> 'VMID': ...
    def getValue(self) -> int: ...

class VMID(java.io.Serializable):
    def __init__(self): ...
    def equals(self, object: typing.Any) -> bool: ...
    def hashCode(self) -> int: ...
    @staticmethod
    def isUnique() -> bool: ...
    def toString(self) -> str: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.rmi.dgc")``.

    DGC: typing.Type[DGC]
    Lease: typing.Type[Lease]
    VMID: typing.Type[VMID]
