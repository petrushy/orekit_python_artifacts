import java.io
import java.lang
import java.lang.annotation
import java.security
import typing



class AnnotatedElement:
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = typing.TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: typing.Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = typing.TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: typing.Type[_getDeclaredAnnotationsByType__T]) -> typing.List[_getDeclaredAnnotationsByType__T]: ...
    def isAnnotationPresent(self, class_: typing.Type[java.lang.annotation.Annotation]) -> bool: ...

class Array:
    @staticmethod
    def get(object: typing.Any, int: int) -> typing.Any: ...
    @staticmethod
    def getBoolean(object: typing.Any, int: int) -> bool: ...
    @staticmethod
    def getByte(object: typing.Any, int: int) -> int: ...
    @staticmethod
    def getChar(object: typing.Any, int: int) -> str: ...
    @staticmethod
    def getDouble(object: typing.Any, int: int) -> float: ...
    @staticmethod
    def getFloat(object: typing.Any, int: int) -> float: ...
    @staticmethod
    def getInt(object: typing.Any, int: int) -> int: ...
    @staticmethod
    def getLength(object: typing.Any) -> int: ...
    @staticmethod
    def getLong(object: typing.Any, int: int) -> int: ...
    @staticmethod
    def getShort(object: typing.Any, int: int) -> int: ...
    @typing.overload
    @staticmethod
    def newInstance(class_: typing.Type[typing.Any], int: int) -> typing.Any: ...
    @typing.overload
    @staticmethod
    def newInstance(class_: typing.Type[typing.Any], *int: int) -> typing.Any: ...
    @staticmethod
    def set(object: typing.Any, int: int, object2: typing.Any) -> None: ...
    @staticmethod
    def setBoolean(object: typing.Any, int: int, boolean: bool) -> None: ...
    @staticmethod
    def setByte(object: typing.Any, int: int, byte: int) -> None: ...
    @staticmethod
    def setChar(object: typing.Any, int: int, char: str) -> None: ...
    @staticmethod
    def setDouble(object: typing.Any, int: int, double: float) -> None: ...
    @staticmethod
    def setFloat(object: typing.Any, int: int, float: float) -> None: ...
    @staticmethod
    def setInt(object: typing.Any, int: int, int2: int) -> None: ...
    @staticmethod
    def setLong(object: typing.Any, int: int, long: int) -> None: ...
    @staticmethod
    def setShort(object: typing.Any, int: int, short: int) -> None: ...

class GenericSignatureFormatError(java.lang.ClassFormatError):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class InaccessibleObjectException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class InvocationHandler:
    def invoke(self, object: typing.Any, method: 'Method', objectArray: typing.List[typing.Any]) -> typing.Any: ...

class InvocationTargetException(java.lang.ReflectiveOperationException):
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, string: str): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getTargetException(self) -> java.lang.Throwable: ...

class MalformedParameterizedTypeException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class MalformedParametersException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str): ...

class Member:
    PUBLIC: typing.ClassVar[int] = ...
    DECLARED: typing.ClassVar[int] = ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def isSynthetic(self) -> bool: ...

class Modifier:
    PUBLIC: typing.ClassVar[int] = ...
    PRIVATE: typing.ClassVar[int] = ...
    PROTECTED: typing.ClassVar[int] = ...
    STATIC: typing.ClassVar[int] = ...
    FINAL: typing.ClassVar[int] = ...
    SYNCHRONIZED: typing.ClassVar[int] = ...
    VOLATILE: typing.ClassVar[int] = ...
    TRANSIENT: typing.ClassVar[int] = ...
    NATIVE: typing.ClassVar[int] = ...
    INTERFACE: typing.ClassVar[int] = ...
    ABSTRACT: typing.ClassVar[int] = ...
    STRICT: typing.ClassVar[int] = ...
    def __init__(self): ...
    @staticmethod
    def classModifiers() -> int: ...
    @staticmethod
    def constructorModifiers() -> int: ...
    @staticmethod
    def fieldModifiers() -> int: ...
    @staticmethod
    def interfaceModifiers() -> int: ...
    @staticmethod
    def isAbstract(int: int) -> bool: ...
    @staticmethod
    def isFinal(int: int) -> bool: ...
    @staticmethod
    def isInterface(int: int) -> bool: ...
    @staticmethod
    def isNative(int: int) -> bool: ...
    @staticmethod
    def isPrivate(int: int) -> bool: ...
    @staticmethod
    def isProtected(int: int) -> bool: ...
    @staticmethod
    def isPublic(int: int) -> bool: ...
    @staticmethod
    def isStatic(int: int) -> bool: ...
    @staticmethod
    def isStrict(int: int) -> bool: ...
    @staticmethod
    def isSynchronized(int: int) -> bool: ...
    @staticmethod
    def isTransient(int: int) -> bool: ...
    @staticmethod
    def isVolatile(int: int) -> bool: ...
    @staticmethod
    def methodModifiers() -> int: ...
    @staticmethod
    def parameterModifiers() -> int: ...
    @typing.overload
    def toString(self) -> str: ...
    @typing.overload
    @staticmethod
    def toString(int: int) -> str: ...

class Proxy(java.io.Serializable):
    @staticmethod
    def getInvocationHandler(object: typing.Any) -> InvocationHandler: ...
    @staticmethod
    def getProxyClass(classLoader: java.lang.ClassLoader, *class2: typing.Type[typing.Any]) -> typing.Type[typing.Any]: ...
    @staticmethod
    def isProxyClass(class_: typing.Type[typing.Any]) -> bool: ...
    @staticmethod
    def newProxyInstance(classLoader: java.lang.ClassLoader, classArray: typing.List[typing.Type[typing.Any]], invocationHandler: InvocationHandler) -> typing.Any: ...

class ReflectPermission(java.security.BasicPermission):
    @typing.overload
    def __init__(self, string: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str): ...

class Type:
    def getTypeName(self) -> str: ...

class UndeclaredThrowableException(java.lang.RuntimeException):
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable): ...
    @typing.overload
    def __init__(self, throwable: java.lang.Throwable, string: str): ...
    def getCause(self) -> java.lang.Throwable: ...
    def getUndeclaredThrowable(self) -> java.lang.Throwable: ...

class AccessibleObject(AnnotatedElement):
    def canAccess(self, object: typing.Any) -> bool: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = typing.TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: typing.Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = typing.TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: typing.Type[_getDeclaredAnnotationsByType__T]) -> typing.List[_getDeclaredAnnotationsByType__T]: ...
    def isAccessible(self) -> bool: ...
    def isAnnotationPresent(self, class_: typing.Type[java.lang.annotation.Annotation]) -> bool: ...
    @typing.overload
    @staticmethod
    def setAccessible(accessibleObjectArray: typing.List['AccessibleObject'], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def trySetAccessible(self) -> bool: ...

class AnnotatedType(AnnotatedElement):
    def getAnnotatedOwnerType(self) -> 'AnnotatedType': ...
    def getType(self) -> Type: ...

class GenericArrayType(Type):
    def getGenericComponentType(self) -> Type: ...

class GenericDeclaration(AnnotatedElement):
    def getTypeParameters(self) -> typing.List['TypeVariable'[typing.Any]]: ...

class Parameter(AnnotatedElement):
    def equals(self, object: typing.Any) -> bool: ...
    def getAnnotatedType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    _getDeclaredAnnotation__T = typing.TypeVar('_getDeclaredAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotation(self, class_: typing.Type[_getDeclaredAnnotation__T]) -> _getDeclaredAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    _getDeclaredAnnotationsByType__T = typing.TypeVar('_getDeclaredAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getDeclaredAnnotationsByType(self, class_: typing.Type[_getDeclaredAnnotationsByType__T]) -> typing.List[_getDeclaredAnnotationsByType__T]: ...
    def getDeclaringExecutable(self) -> 'Executable': ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterizedType(self) -> Type: ...
    def getType(self) -> typing.Type[typing.Any]: ...
    def hashCode(self) -> int: ...
    def isImplicit(self) -> bool: ...
    def isNamePresent(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toString(self) -> str: ...

class ParameterizedType(Type):
    def getActualTypeArguments(self) -> typing.List[Type]: ...
    def getOwnerType(self) -> Type: ...
    def getRawType(self) -> Type: ...

_TypeVariable__D = typing.TypeVar('_TypeVariable__D', bound=GenericDeclaration)  # <D>
class TypeVariable(Type, AnnotatedElement, typing.Generic[_TypeVariable__D]):
    def getAnnotatedBounds(self) -> typing.List[AnnotatedType]: ...
    def getBounds(self) -> typing.List[Type]: ...
    def getGenericDeclaration(self) -> _TypeVariable__D: ...
    def getName(self) -> str: ...

class WildcardType(Type):
    def getLowerBounds(self) -> typing.List[Type]: ...
    def getUpperBounds(self) -> typing.List[Type]: ...

class AnnotatedArrayType(AnnotatedType):
    def getAnnotatedGenericComponentType(self) -> AnnotatedType: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...

class AnnotatedParameterizedType(AnnotatedType):
    def getAnnotatedActualTypeArguments(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...

class AnnotatedTypeVariable(AnnotatedType):
    def getAnnotatedBounds(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...

class AnnotatedWildcardType(AnnotatedType):
    def getAnnotatedLowerBounds(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedOwnerType(self) -> AnnotatedType: ...
    def getAnnotatedUpperBounds(self) -> typing.List[AnnotatedType]: ...

class Executable(AccessibleObject, Member, GenericDeclaration):
    def getAnnotatedExceptionTypes(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedParameterTypes(self) -> typing.List[AnnotatedType]: ...
    def getAnnotatedReceiverType(self) -> AnnotatedType: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getExceptionTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getGenericExceptionTypes(self) -> typing.List[Type]: ...
    def getGenericParameterTypes(self) -> typing.List[Type]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterAnnotations(self) -> typing.List[typing.List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getParameters(self) -> typing.List[Parameter]: ...
    def getTypeParameters(self) -> typing.List[TypeVariable[typing.Any]]: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def toGenericString(self) -> str: ...

class Field(AccessibleObject, Member):
    def equals(self, object: typing.Any) -> bool: ...
    def get(self, object: typing.Any) -> typing.Any: ...
    def getAnnotatedType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    _getAnnotationsByType__T = typing.TypeVar('_getAnnotationsByType__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotationsByType(self, class_: typing.Type[_getAnnotationsByType__T]) -> typing.List[_getAnnotationsByType__T]: ...
    def getBoolean(self, object: typing.Any) -> bool: ...
    def getByte(self, object: typing.Any) -> int: ...
    def getChar(self, object: typing.Any) -> str: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getDouble(self, object: typing.Any) -> float: ...
    def getFloat(self, object: typing.Any) -> float: ...
    def getGenericType(self) -> Type: ...
    def getInt(self, object: typing.Any) -> int: ...
    def getLong(self, object: typing.Any) -> int: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getShort(self, object: typing.Any) -> int: ...
    def getType(self) -> typing.Type[typing.Any]: ...
    def hashCode(self) -> int: ...
    def isEnumConstant(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def set(self, object: typing.Any, object2: typing.Any) -> None: ...
    @typing.overload
    @staticmethod
    def setAccessible(accessibleObjectArray: typing.List[AccessibleObject], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def setBoolean(self, object: typing.Any, boolean: bool) -> None: ...
    def setByte(self, object: typing.Any, byte: int) -> None: ...
    def setChar(self, object: typing.Any, char: str) -> None: ...
    def setDouble(self, object: typing.Any, double: float) -> None: ...
    def setFloat(self, object: typing.Any, float: float) -> None: ...
    def setInt(self, object: typing.Any, int: int) -> None: ...
    def setLong(self, object: typing.Any, long: int) -> None: ...
    def setShort(self, object: typing.Any, short: int) -> None: ...
    def toGenericString(self) -> str: ...
    def toString(self) -> str: ...

_Constructor__T = typing.TypeVar('_Constructor__T')  # <T>
class Constructor(Executable, typing.Generic[_Constructor__T]):
    def equals(self, object: typing.Any) -> bool: ...
    def getAnnotatedReceiverType(self) -> AnnotatedType: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[java.lang.annotation.Annotation]) -> java.lang.annotation.Annotation: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[_Constructor__T]: ...
    def getExceptionTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getGenericExceptionTypes(self) -> typing.List[Type]: ...
    def getGenericParameterTypes(self) -> typing.List[Type]: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterAnnotations(self) -> typing.List[typing.List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getTypeParameters(self) -> typing.List[TypeVariable['Constructor'[_Constructor__T]]]: ...
    def hashCode(self) -> int: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    def newInstance(self, *object: typing.Any) -> _Constructor__T: ...
    @typing.overload
    @staticmethod
    def setAccessible(accessibleObjectArray: typing.List[AccessibleObject], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def toGenericString(self) -> str: ...
    def toString(self) -> str: ...

class Method(Executable):
    def equals(self, object: typing.Any) -> bool: ...
    def getAnnotatedReturnType(self) -> AnnotatedType: ...
    _getAnnotation__T = typing.TypeVar('_getAnnotation__T', bound=java.lang.annotation.Annotation)  # <T>
    def getAnnotation(self, class_: typing.Type[_getAnnotation__T]) -> _getAnnotation__T: ...
    def getDeclaredAnnotations(self) -> typing.List[java.lang.annotation.Annotation]: ...
    def getDeclaringClass(self) -> typing.Type[typing.Any]: ...
    def getDefaultValue(self) -> typing.Any: ...
    def getExceptionTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getGenericExceptionTypes(self) -> typing.List[Type]: ...
    def getGenericParameterTypes(self) -> typing.List[Type]: ...
    def getGenericReturnType(self) -> Type: ...
    def getModifiers(self) -> int: ...
    def getName(self) -> str: ...
    def getParameterAnnotations(self) -> typing.List[typing.List[java.lang.annotation.Annotation]]: ...
    def getParameterCount(self) -> int: ...
    def getParameterTypes(self) -> typing.List[typing.Type[typing.Any]]: ...
    def getReturnType(self) -> typing.Type[typing.Any]: ...
    def getTypeParameters(self) -> typing.List[TypeVariable['Method']]: ...
    def hashCode(self) -> int: ...
    def invoke(self, object: typing.Any, *object2: typing.Any) -> typing.Any: ...
    def isBridge(self) -> bool: ...
    def isDefault(self) -> bool: ...
    def isSynthetic(self) -> bool: ...
    def isVarArgs(self) -> bool: ...
    @typing.overload
    @staticmethod
    def setAccessible(accessibleObjectArray: typing.List[AccessibleObject], boolean: bool) -> None: ...
    @typing.overload
    def setAccessible(self, boolean: bool) -> None: ...
    def toGenericString(self) -> str: ...
    def toString(self) -> str: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.lang.reflect")``.

    AccessibleObject: typing.Type[AccessibleObject]
    AnnotatedArrayType: typing.Type[AnnotatedArrayType]
    AnnotatedElement: typing.Type[AnnotatedElement]
    AnnotatedParameterizedType: typing.Type[AnnotatedParameterizedType]
    AnnotatedType: typing.Type[AnnotatedType]
    AnnotatedTypeVariable: typing.Type[AnnotatedTypeVariable]
    AnnotatedWildcardType: typing.Type[AnnotatedWildcardType]
    Array: typing.Type[Array]
    Constructor: typing.Type[Constructor]
    Executable: typing.Type[Executable]
    Field: typing.Type[Field]
    GenericArrayType: typing.Type[GenericArrayType]
    GenericDeclaration: typing.Type[GenericDeclaration]
    GenericSignatureFormatError: typing.Type[GenericSignatureFormatError]
    InaccessibleObjectException: typing.Type[InaccessibleObjectException]
    InvocationHandler: typing.Type[InvocationHandler]
    InvocationTargetException: typing.Type[InvocationTargetException]
    MalformedParameterizedTypeException: typing.Type[MalformedParameterizedTypeException]
    MalformedParametersException: typing.Type[MalformedParametersException]
    Member: typing.Type[Member]
    Method: typing.Type[Method]
    Modifier: typing.Type[Modifier]
    Parameter: typing.Type[Parameter]
    ParameterizedType: typing.Type[ParameterizedType]
    Proxy: typing.Type[Proxy]
    ReflectPermission: typing.Type[ReflectPermission]
    Type: typing.Type[Type]
    TypeVariable: typing.Type[TypeVariable]
    UndeclaredThrowableException: typing.Type[UndeclaredThrowableException]
    WildcardType: typing.Type[WildcardType]
