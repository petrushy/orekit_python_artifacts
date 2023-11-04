import java.lang.invoke
import typing



class ObjectMethods:
    @staticmethod
    def bootstrap(lookup: java.lang.invoke.MethodHandles.Lookup, string: str, typeDescriptor: java.lang.invoke.TypeDescriptor, class_: typing.Type[typing.Any], string2: str, *methodHandle: java.lang.invoke.MethodHandle) -> typing.Any: ...

class SwitchBootstraps:
    @staticmethod
    def enumSwitch(lookup: java.lang.invoke.MethodHandles.Lookup, string: str, methodType: java.lang.invoke.MethodType, *object: typing.Any) -> java.lang.invoke.CallSite: ...
    @staticmethod
    def typeSwitch(lookup: java.lang.invoke.MethodHandles.Lookup, string: str, methodType: java.lang.invoke.MethodType, *object: typing.Any) -> java.lang.invoke.CallSite: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.runtime")``.

    ObjectMethods: typing.Type[ObjectMethods]
    SwitchBootstraps: typing.Type[SwitchBootstraps]
