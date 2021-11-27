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
import typing



class LocalizedGeometryFormats(java.lang.Enum['LocalizedGeometryFormats'], org.hipparchus.exception.Localizable):
    """
    public enum LocalizedGeometryFormats extends Enum<:class:`~org.hipparchus.geometry.LocalizedGeometryFormats`> implements Localizable
    
        Enumeration for localized messages formats used in exceptions messages.
    
        The constants in this enumeration represent the available formats as localized strings. These formats are intended to be
        localized using simple properties files, using the constant name as the key and the property value as the message
        format. The source English format is provided in the constants themselves to serve both as a reminder for developers to
        understand the parameters needed by each format, as a basis for translators to create localized properties files, and as
        a default format if some translation is missing.
    """
    CANNOT_NORMALIZE_A_ZERO_NORM_VECTOR: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CARDAN_ANGLES_SINGULARITY: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CLOSE_VERTICES: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CLOSEST_ORTHOGONAL_MATRIX_HAS_NEGATIVE_DETERMINANT: typing.ClassVar['LocalizedGeometryFormats'] = ...
    CROSSING_BOUNDARY_LOOPS: typing.ClassVar['LocalizedGeometryFormats'] = ...
    EDGE_CONNECTED_TO_ONE_FACET: typing.ClassVar['LocalizedGeometryFormats'] = ...
    EULER_ANGLES_SINGULARITY: typing.ClassVar['LocalizedGeometryFormats'] = ...
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
    def getLocalizedString(self, locale: java.util.Locale) -> str:
        """
        
            Specified by:
                 in interface 
        
        
        """
        ...
    def getSourceString(self) -> str:
        """
        
            Specified by:
                 in interface 
        
        
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
                name (String): the name of the enum constant to be returned.
        
            Returns:
                the enum constant with the specified name
        
            Raises:
                : if this enum type has no constant with the specified name
                : if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.List['LocalizedGeometryFormats']:
        """
            Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to
            iterate over the constants as follows:
        
            .. code-block: java
            
            for (LocalizedGeometryFormats c : LocalizedGeometryFormats.values())
                System.out.println(c);
            
        
            Returns:
                an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

_Point__S = typing.TypeVar('_Point__S', bound='Space')  # <S>
class Point(java.io.Serializable, typing.Generic[_Point__S]):
    """
    public interface Point<S extends :class:`~org.hipparchus.geometry.Space`> extends Serializable
    
        This interface represents a generic geometrical point.
    
        Also see:
            :class:`~org.hipparchus.geometry.Space`, :class:`~org.hipparchus.geometry.Vector`
    """
    def distance(self, point: 'Point'[_Point__S]) -> float: ...
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

class Space(java.io.Serializable):
    """
    public interface Space extends Serializable
    
        This interface represents a generic space, with affine and vectorial counterparts.
    
        Also see:
            :class:`~org.hipparchus.geometry.Vector`
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
class VectorFormat(typing.Generic[_VectorFormat__S]):
    """
    public abstract class VectorFormat<S extends :class:`~org.hipparchus.geometry.Space`> extends Object
    
        Formats a vector in components list format "{x; y; ...}".
    
        The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format
        for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1
        ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        **Note:** using "," as a separator may interfere with the grouping separator of the default null for the current locale.
        Thus it is advised to use a null instance with disabled grouping in such a case.
    """
    DEFAULT_PREFIX: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_PREFIX
    
        The default prefix: "{".
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_SUFFIX: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_SUFFIX
    
        The default suffix: "}".
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_SEPARATOR: typing.ClassVar[str] = ...
    """
    public static final String DEFAULT_SEPARATOR
    
        The default separator: ", ".
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def format(self, vector: 'Vector'[_VectorFormat__S], stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer:
        """
            Formats the coordinates of a :class:`~org.hipparchus.geometry.Vector` to produce a string.
        
            Parameters:
                toAppendTo (StringBuffer): where the text is to be appended
                pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
                coordinates (double...): coordinates of the object to format.
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    def format(self, vector: 'Vector'[_VectorFormat__S]) -> str: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]:
        """
            Get the set of locales for which point/vector formats are available.
        
            This is the same set as the null set.
        
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
    def parse(self, string: str) -> 'Vector'[_VectorFormat__S]: ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'Vector'[_VectorFormat__S]: ...

_Vector__S = typing.TypeVar('_Vector__S', bound=Space)  # <S>
class Vector(Point[_Vector__S], typing.Generic[_Vector__S]):
    """
    public interface Vector<S extends :class:`~org.hipparchus.geometry.Space`> extends :class:`~org.hipparchus.geometry.Point`<S>
    
        This interface represents a generic vector in a vectorial space or a point in an affine space.
    
        Also see:
            :class:`~org.hipparchus.geometry.Space`, :class:`~org.hipparchus.geometry.Point`
    """
    @typing.overload
    def add(self, double: float, vector: 'Vector'[_Vector__S]) -> 'Vector'[_Vector__S]: ...
    @typing.overload
    def add(self, vector: 'Vector'[_Vector__S]) -> 'Vector'[_Vector__S]: ...
    def distance1(self, vector: 'Vector'[_Vector__S]) -> float: ...
    def distanceInf(self, vector: 'Vector'[_Vector__S]) -> float: ...
    def distanceSq(self, vector: 'Vector'[_Vector__S]) -> float: ...
    def dotProduct(self, vector: 'Vector'[_Vector__S]) -> float: ...
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
    def getZero(self) -> 'Vector'[_Vector__S]: ...
    def isInfinite(self) -> bool:
        """
            Returns true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
            Returns:
                true if any coordinate of this vector is infinite and none are NaN; false otherwise
        
        
        """
        ...
    def negate(self) -> 'Vector'[_Vector__S]: ...
    def normalize(self) -> 'Vector'[_Vector__S]: ...
    def scalarMultiply(self, double: float) -> 'Vector'[_Vector__S]: ...
    @typing.overload
    def subtract(self, double: float, vector: 'Vector'[_Vector__S]) -> 'Vector'[_Vector__S]: ...
    @typing.overload
    def subtract(self, vector: 'Vector'[_Vector__S]) -> 'Vector'[_Vector__S]: ...
    def toString(self, numberFormat: java.text.NumberFormat) -> str:
        """
            Get a string representation of this vector.
        
            Parameters:
                format (NumberFormat): the custom format for components
        
            Returns:
                a string representation of this vector
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry")``.

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
