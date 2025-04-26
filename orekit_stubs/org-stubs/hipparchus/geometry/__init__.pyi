
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.text
import java.util
import org.hipparchus.exception
import org.hipparchus.geometry.enclosing
import org.hipparchus.geometry.euclidean
import org.hipparchus.geometry.hull
import org.hipparchus.geometry.partitioning
import org.hipparchus.geometry.spherical
import org.hipparchus.util
import typing



class Geometry:
    """
    public classGeometry extends :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Utilities for geometry.
    
        Since:
            4.0
    """
    _barycenter__S = typing.TypeVar('_barycenter__S', bound='Space')  # <S>
    _barycenter__P = typing.TypeVar('_barycenter__P', bound='Point')  # <P>
    @staticmethod
    def barycenter(list: java.util.List[_barycenter__P]) -> _barycenter__P:
        """
            Compute the barycenter of n points.
        
            Parameters:
                points (:class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.util.List`<P> points): points generating the barycenter
        
            Returns:
                barycenter of the points
        
        
        """
        ...

class LocalizedGeometryFormats(java.lang.Enum['LocalizedGeometryFormats'], org.hipparchus.exception.Localizable):
    """
    public enumLocalizedGeometryFormats extends :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.Enum`<:class:`~org.hipparchus.geometry.LocalizedGeometryFormats`>
    implements :class:`~org.hipparchus.geometry.https:.www.hipparchus.org.hipparchus`
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    CANNOT_NORMALIZE_A_ZERO_NORM_VECTOR: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CLOSE_VERTICES: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CLOSEST_ORTHOGONAL_MATRIX_HAS_NEGATIVE_DETERMINANT: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CROSSING_BOUNDARY_LOOPS: typing.ClassVar['LocalizedGeometryFormats'] = ...
    EDGE_CONNECTED_TO_ONE_FACET: typing.ClassVar['LocalizedGeometryFormats'] = ...
    FACET_ORIENTATION_MISMATCH: typing.ClassVar['LocalizedGeometryFormats'] = ...
    INCONSISTENT_STATE_AT_2_PI_WRAPPING: typing.ClassVar['LocalizedGeometryFormats'] = ...
    NON_INVERTIBLE_TRANSFORM: typing.ClassVar['LocalizedGeometryFormats'] = ...
    NOT_CONVEX: typing.ClassVar['LocalizedGeometryFormats'] = ...
    NOT_CONVEX_HYPERPLANES: typing.ClassVar['LocalizedGeometryFormats'] = ...
    NOT_SUPPORTED_IN_DIMENSION_N: typing.ClassVar['LocalizedGeometryFormats'] = ...
    OUTLINE_BOUNDARY_LOOP_OPEN: typing.ClassVar['LocalizedGeometryFormats'] = ...
    FACET_WITH_SEVERAL_BOUNDARY_LOOPS: typing.ClassVar['LocalizedGeometryFormats'] = ...
    OUT_OF_PLANE: typing.ClassVar['LocalizedGeometryFormats'] = ...
    ROTATION_MATRIX_DIMENSIONS: typing.ClassVar['LocalizedGeometryFormats'] = ...
    UNABLE_TO_ORTHOGONOLIZE_MATRIX: typing.ClassVar['LocalizedGeometryFormats'] = ...
    ZERO_NORM_FOR_ROTATION_AXIS: typing.ClassVar['LocalizedGeometryFormats'] = ...
    ZERO_NORM_FOR_ROTATION_DEFINING_VECTOR: typing.ClassVar['LocalizedGeometryFormats'] = ...
    TOO_SMALL_TOLERANCE: typing.ClassVar['LocalizedGeometryFormats'] = ...
    INVALID_ROTATION_ORDER_NAME: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CANNOT_FIND_INSIDE_POINT: typing.ClassVar['LocalizedGeometryFormats'] = ...
    @typing.overload
    def getLocalizedString(self, string: str, string2: str, locale: java.util.Locale) -> str: ...
    @typing.overload
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.geometry.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.geometry.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                :meth:`~org.hipparchus.geometry.https:.www.hipparchus.org.hipparchus` in
                interface :class:`~org.hipparchus.geometry.https:.www.hipparchus.org.hipparchus`
        
        
        """
        ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(string: str) -> 'LocalizedGeometryFormats':
        """
            Returns the enum constant of this type with the specified name. The string must match *exactly* an identifier used to
            declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
            Parameters:
                name (:class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.IllegalArgumentException`: if this enum type has no constant with the specified name
                :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.NullPointerException`: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['LocalizedGeometryFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared.
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_Point__S = typing.TypeVar('_Point__S', bound='Space')  # <S>
_Point__P = typing.TypeVar('_Point__P', bound='Point')  # <P>
class Point(java.io.Serializable, typing.Generic[_Point__S, _Point__P]):
    """
    public interfacePoint<S extends :class:`~org.hipparchus.geometry.Space`,P extends Point<S,P>>extends :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This interface represents a generic geometrical point.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.Space`
              - :class:`~org.hipparchus.geometry.Vector`
    """
    def distance(self, p: _Point__P) -> float:
        """
            Compute the distance between the instance and another point.
        
            Parameters:
                p (:class:`~org.hipparchus.geometry.Point`): second point
        
            Returns:
                the distance between the instance and p
        
        
        """
        ...
    def getSpace(self) -> 'Space':
        """
            Get the space to which the point belongs.
        
            Returns:
                containing space
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Returns true if any coordinate of this point is NaN; false otherwise
        
            Returns:
                true if any coordinate of this point is NaN; false otherwise
        
        
        """
        ...
    def moveTowards(self, p: _Point__P, double: float) -> _Point__P:
        """
            Move towards another point.
        
            Motion is linear (along space curvature) and based on a ratio where 0.0 stands for not moving at all, 0.5 stands for
            moving halfway towards other point, and 1.0 stands for moving fully to the other point.
        
            Parameters:
                other (:class:`~org.hipparchus.geometry.Point`): other point
                ratio (double): motion ratio,
        
            Returns:
                moved point
        
            Since:
                4.0
        
        
        """
        ...

class Space(java.io.Serializable):
    """
    public interfaceSpaceextends :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.io.Serializable`
    
        This interface represents a generic space, with affine and vectorial counterparts.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.Vector`
    """
    def getDimension(self) -> int:
        """
            Get the dimension of the space.
        
            Returns:
                dimension of the space
        
        
        """
        ...
    def getSubSpace(self) -> 'Space': ...

_VectorFormat__S = typing.TypeVar('_VectorFormat__S', bound=Space)  # <S>
_VectorFormat__V = typing.TypeVar('_VectorFormat__V', bound='Vector')  # <V>
class VectorFormat(typing.Generic[_VectorFormat__S, _VectorFormat__V]):
    """
    public abstract classVectorFormat<S extends :class:`~org.hipparchus.geometry.Space`,V extends :class:`~org.hipparchus.geometry.Vector`<S,V>> extends :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Formats a vector in components list format "{x; y; ...}".
    
        The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format
        for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1
        ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        **Note:** using "," as a separator may interfere with the grouping separator of the default
        :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` for the current
        locale. Thus it is advised to use a
        :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` instance with disabled
        grouping in such a case.
    """
    DEFAULT_PREFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.String` DEFAULT_PREFIX
    
        The default prefix: "{".
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.String` DEFAULT_SUFFIX
    
        The default suffix: "}".
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    DEFAULT_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.String` DEFAULT_SEPARATOR
    
        The default separator: ", ".
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    @typing.overload
    def format(self, vector: 'Vector'[_VectorFormat__S, _VectorFormat__V], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer:
        """
            Formats the coordinates of a :class:`~org.hipparchus.geometry.Vector` to produce a string.
        
            Parameters:
                toAppendTo (:class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.lang.StringBuffer`): where the text is to be appended
                pos (:class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.text.FieldPosition`): On input: an alignment field, if desired. On output: the offsets of the alignment field
                coordinates (double...): coordinates of the object to format.
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    def format(self, vector: 'Vector'[_VectorFormat__S, _VectorFormat__V]) -> str: ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
            Get the set of locales for which point/vector formats are available.
        
            This is the same set as the
            :class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat` set.
        
            Returns:
                available point/vector format locales.
        
        
        """
        ...
    def getFormat(self) -> java.text.NumberFormat:
        """
            Get the components format.
        
            Returns:
                components format.
        
        
        """
        ...
    def getPrefix(self) -> str:
        """
            Get the format prefix.
        
            Returns:
                format prefix.
        
        
        """
        ...
    def getSeparator(self) -> str:
        """
            Get the format separator between components.
        
            Returns:
                format separator.
        
        
        """
        ...
    def getSuffix(self) -> str:
        """
            Get the format suffix.
        
            Returns:
                format suffix.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str) -> 'Vector'[_VectorFormat__S, _VectorFormat__V]: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'Vector'[_VectorFormat__S, _VectorFormat__V]: ...

_Vector__S = typing.TypeVar('_Vector__S', bound=Space)  # <S>
_Vector__V = typing.TypeVar('_Vector__V', bound='Vector')  # <V>
class Vector(Point[_Vector__S, _Vector__V], org.hipparchus.util.Blendable[_Vector__V], typing.Generic[_Vector__S, _Vector__V]):
    """
    public interfaceVector<S extends :class:`~org.hipparchus.geometry.Space`,V extends Vector<S,V>>extends :class:`~org.hipparchus.geometry.Point`<S,V>, :class:`~org.hipparchus.geometry.https:.www.hipparchus.org.hipparchus`<V>
    
        This interface represents a generic vector in a vectorial space or a point in an affine space.
    
        Also see:
    
              - :class:`~org.hipparchus.geometry.Space`
              - :class:`~org.hipparchus.geometry.Point`
    """
    @typing.overload
    def add(self, double: float, v: _Vector__V) -> _Vector__V:
        """
            Add a scaled vector to the instance.
        
            Parameters:
                factor (double): scale factor to apply to v before adding it
                v (:class:`~org.hipparchus.geometry.Vector`): vector to add
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def add(self, v: _Vector__V) -> _Vector__V:
        """
            Add a vector to the instance.
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.Vector`): vector to add
        
            Returns:
                a new vector
        
        """
        ...
    def blendArithmeticallyWith(self, v: _Vector__V, double: float) -> _Vector__V: ...
    def distance1(self, v: _Vector__V) -> float:
        """
            Compute the distance between the instance and another vector according to the L :sub:`1` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNorm1()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.Vector`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`1` norm
        
        
        """
        ...
    def distanceInf(self, v: _Vector__V) -> float:
        """
            Compute the distance between the instance and another vector according to the L :sub:`∞` norm.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormInf()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.Vector`): second vector
        
            Returns:
                the distance between the instance and p according to the L :sub:`∞` norm
        
        
        """
        ...
    def distanceSq(self, v: _Vector__V) -> float:
        """
            Compute the square of the distance between the instance and another vector.
        
            Calling this method is equivalent to calling: :code:`q.subtract(p).getNormSq()` except that no intermediate vector is
            built
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.Vector`): second vector
        
            Returns:
                the square of the distance between the instance and p
        
        
        """
        ...
    def dotProduct(self, v: _Vector__V) -> float:
        """
            Compute the dot-product of the instance and another vector.
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.Vector`): second vector
        
            Returns:
                the dot product this.v
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Get the L :sub:`2` norm for the vector.
        
            Returns:
                Euclidean norm for the vector
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
            Get the L :sub:`1` norm for the vector.
        
            Returns:
                L :sub:`1` norm for the vector
        
        
        """
        ...
    def getNormInf(self) -> float:
        """
            Get the L :sub:`∞` norm for the vector.
        
            Returns:
                L :sub:`∞` norm for the vector
        
        
        """
        ...
    def getNormSq(self) -> float:
        """
            Get the square of the norm for the vector.
        
            Returns:
                square of the Euclidean norm for the vector
        
        
        """
        ...
    def getZero(self) -> _Vector__V:
        """
            Get the null vector of the vectorial space or origin point of the affine space.
        
            Returns:
                null vector of the vectorial space or origin point of the affine space
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
            Returns:
                true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
        """
        ...
    def negate(self) -> _Vector__V:
        """
            Get the opposite of the instance.
        
            Returns:
                a new vector which is opposite to the instance
        
        
        """
        ...
    def normalize(self) -> _Vector__V: ...
    def scalarMultiply(self, double: float) -> _Vector__V:
        """
            Multiply the instance by a scalar.
        
            Parameters:
                a (double): scalar
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float, v: _Vector__V) -> _Vector__V:
        """
            Subtract a scaled vector from the instance.
        
            Parameters:
                factor (double): scale factor to apply to v before subtracting it
                v (:class:`~org.hipparchus.geometry.Vector`): vector to subtract
        
            Returns:
                a new vector
        
        
        """
        ...
    @typing.overload
    def subtract(self, v: _Vector__V) -> _Vector__V:
        """
            Subtract a vector from the instance.
        
            Parameters:
                v (:class:`~org.hipparchus.geometry.Vector`): vector to subtract
        
            Returns:
                a new vector
        
        """
        ...
    def toString(self, numberFormat: java.text.NumberFormat) -> str:
        """
            Get a string representation of this vector.
        
            Parameters:
                format (:class:`~org.hipparchus.geometry.https:.docs.oracle.com.javase.8.docs.api.java.text.NumberFormat`): the custom format for components
        
            Returns:
                a string representation of this vector
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry")``.

    Geometry: typing.Type[Geometry]
    LocalizedGeometryFormats: typing.Type[LocalizedGeometryFormats]
    Point: typing.Type[Point]
    Space: typing.Type[Space]
    Vector: typing.Type[Vector]
    VectorFormat: typing.Type[VectorFormat]
    enclosing: org.hipparchus.geometry.enclosing.__module_protocol__
    euclidean: org.hipparchus.geometry.euclidean.__module_protocol__
    hull: org.hipparchus.geometry.hull.__module_protocol__
    partitioning: org.hipparchus.geometry.partitioning.__module_protocol__
    spherical: org.hipparchus.geometry.spherical.__module_protocol__
