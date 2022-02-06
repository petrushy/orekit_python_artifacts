import java.io
import java.lang
import java.util
import org.hipparchus.fraction
import typing



class Parser:
    """
    public class Parser extends Object
    
        Parser for units.
    
        This fairly basic parser uses recursive descent with the following grammar, where '*' can in fact be either '*',
        'Ãƒâ€”', '.', or 'Ã‚Â·', '/' can be either '/' or 'Ã¢ï¿½â€ž' and '^' can be either '^', "**" or implicit with switch to
        superscripts, and fraction are either unicode fractions like Ã‚Â½ or Ã¢â€¦Å¾ or the decimal value 0.5. The special cases
        "n/a" returns a null list. It is intended to manage the special unit :meth:`~org.orekit.utils.units.Unit.NONE`.
    
        .. code-block: java
        
        
           unit         ::=  "n/a" | chain
           chain        ::=  operand { ('*' | '/') operand }
           operand      ::=  integer | integer term | term
           term         ::=  'âˆš' base | base power
           power        ::=  '^' exponent | Îµ
           exponent     ::=  'fraction'   | integer | '(' integer denominator ')'
           denominator  ::=  '/' integer  | Îµ
           base         ::=  identifier | '(' chain ')'
         
    
        This parses correctly units like MHz, km/Ã¢Ë†Å¡d, kg.m.sÃ¢ï¿½Â»Ã‚Â¹, Ã‚Âµas^Ã¢â€¦â€“/(h**(2)Ãƒâ€”m)Ã‚Â³,
        km/Ã¢Ë†Å¡(kg.s), Ã¢Ë†Å¡kg*km** (3/2) /(Ã‚Âµs^2*ÃŽÂ©Ã¢ï¿½Â»Ã¢ï¿½Â·), km**0.5/s, #/y, 2rev/dÃ‚Â², 1/s.
    
        Note that we don't accept combining square roots and power on the same operand; km/Ã¢Ë†Å¡dÃ‚Â³ is refused (but
        km/Ã¢Ë†Å¡(dÃ‚Â³) is accepted). We also accept a single integer prefix and only at the start of the specification.
    
        Since:
            11.0
    """
    @staticmethod
    def buildTermsList(string: str) -> java.util.List['PowerTerm']: ...

class PowerTerm:
    """
    public class PowerTerm extends Object
    
        A container for a term with associated power.
    
        Since:
            11.0
    """
    def getBase(self) -> java.lang.CharSequence:
        """
            Get the base term.
        
            Returns:
                base term
        
        
        """
        ...
    def getExponent(self) -> org.hipparchus.fraction.Fraction:
        """
            Get the fractional exponent.
        
            Returns:
                fractional exponent
        
        
        """
        ...
    def getScale(self) -> float:
        """
            Get the scaling factor.
        
            Returns:
                scaling factor
        
        
        """
        ...

class Unit(java.io.Serializable):
    """
    public class Unit extends Object implements Serializable
    
        Basic handling of multiplicative units.
    
        This class is by no means a complete handling of units. For complete support, look at libraries like :code:`UOM`. This
        class handles only time, length, mass and current dimensions, as well as angles (which are dimensionless).
    
        Instances of this class are immutable.
    
        Since:
            11.0
    
        Also see:
            UOM, :meth:`~serialized`
    """
    NONE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` NONE
    
        No unit.
    
    """
    ONE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` ONE
    
        Dimensionless unit.
    
    """
    PERCENT: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` PERCENT
    
        Percentage unit.
    
    """
    SECOND: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` SECOND
    
        Second unit.
    
    """
    MINUTE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` MINUTE
    
        Minute unit.
    
    """
    HOUR: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` HOUR
    
        Hour unit.
    
    """
    DAY: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` DAY
    
        Day unit.
    
    """
    YEAR: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` YEAR
    
        Julian year unit.
    
        Also see:
            SI Units at IAU
    
    
    """
    HERTZ: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` HERTZ
    
        Hertz unit.
    
    """
    METRE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` METRE
    
        Metre unit.
    
    """
    KILOMETRE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KILOMETRE
    
        Kilometre unit.
    
    """
    KILOGRAM: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` KILOGRAM
    
        Kilogram unit.
    
    """
    GRAM: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` GRAM
    
        Gram unit.
    
    """
    AMPERE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` AMPERE
    
        Ampere unit.
    
    """
    RADIAN: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` RADIAN
    
        Radian unit.
    
    """
    DEGREE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` DEGREE
    
        Degree unit.
    
    """
    ARC_MINUTE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` ARC_MINUTE
    
        Arc minute unit.
    
    """
    ARC_SECOND: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` ARC_SECOND
    
        Arc second unit.
    
    """
    REVOLUTION: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` REVOLUTION
    
        Revolution unit.
    
    """
    NEWTON: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` NEWTON
    
        Newton unit.
    
    """
    PASCAL: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` PASCAL
    
        Pascal unit.
    
    """
    BAR: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` BAR
    
        Bar unit.
    
    """
    JOULE: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` JOULE
    
        Joule unit.
    
    """
    WATT: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` WATT
    
        Watt unit.
    
    """
    COULOMB: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` COULOMB
    
        Coulomb unit.
    
    """
    VOLT: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` VOLT
    
        Volt unit.
    
    """
    OHM: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` OHM
    
        Ohm unit.
    
    """
    TESLA: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` TESLA
    
        tesla unit.
    
    """
    SOLAR_FLUX_UNIT: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` SOLAR_FLUX_UNIT
    
        Solar Flux Unit.
    
    """
    TOTAL_ELECTRON_CONTENT_UNIT: typing.ClassVar['Unit'] = ...
    """
    public static final :class:`~org.orekit.utils.units.Unit` TOTAL_ELECTRON_CONTENT_UNIT
    
        Total Electron Content Unit.
    
    """
    def __init__(self, string: str, double: float, fraction: org.hipparchus.fraction.Fraction, fraction2: org.hipparchus.fraction.Fraction, fraction3: org.hipparchus.fraction.Fraction, fraction4: org.hipparchus.fraction.Fraction, fraction5: org.hipparchus.fraction.Fraction): ...
    def alias(self, string: str) -> 'Unit':
        """
            Create an alias for a unit.
        
            Parameters:
                newName (String): name of the new unit
        
            Returns:
                a new unit representing same unit as the instance but with a different name
        
        
        """
        ...
    def divide(self, string: str, unit: 'Unit') -> 'Unit':
        """
            Create quotient of units.
        
            Parameters:
                newName (String): name of the new unit
                other (:class:`~org.orekit.utils.units.Unit`): unit to divide with
        
            Returns:
                a new unit representing the this divided by the other unit
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Check if the instance represents the same unit as another instance.
        
            The name is not considered so aliases are considered equal.
        
            Overrides:
                 in class 
        
            Parameters:
                unit (Object): other unit
        
            Returns:
                true if the instance and the other unit refer to the same unit
        
        
        """
        ...
    @typing.overload
    def fromSI(self, double: float) -> float:
        """
            Convert a value from SI units.
        
            Parameters:
                value (double): value SI unit
        
            Returns:
                value in instance units
        
            Convert a value from SI units.
        
            Parameters:
                value (Double): value SI unit
        
            Returns:
                value in instance units
        
        
        """
        ...
    @typing.overload
    def fromSI(self, double: float) -> float: ...
    def getAngle(self) -> org.hipparchus.fraction.Fraction:
        """
            Get the angle exponent.
        
            Returns:
                angle exponent
        
        
        """
        ...
    def getCurrent(self) -> org.hipparchus.fraction.Fraction:
        """
            Get the current exponent.
        
            Returns:
                current exponent
        
        
        """
        ...
    def getLength(self) -> org.hipparchus.fraction.Fraction:
        """
            Get the length exponent.
        
            Returns:
                length exponent
        
        
        """
        ...
    def getMass(self) -> org.hipparchus.fraction.Fraction:
        """
            Get the mass exponent.
        
            Returns:
                mass exponent
        
        
        """
        ...
    def getName(self) -> str:
        """
            Get the name of the unit.
        
            Returns:
                name of the unit
        
        
        """
        ...
    def getScale(self) -> float:
        """
            Get the scaling factor to SI units.
        
            Returns:
                scaling factor to SI units
        
        
        """
        ...
    def getTime(self) -> org.hipparchus.fraction.Fraction:
        """
            Get the time exponent.
        
            Returns:
                time exponent
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashcode for this unit.
        
            Overrides:
                 in class 
        
            Returns:
                hashcode
        
        
        """
        ...
    def multiply(self, string: str, unit: 'Unit') -> 'Unit':
        """
            Create product of units.
        
            Parameters:
                newName (String): name of the new unit
                other (:class:`~org.orekit.utils.units.Unit`): unit to multiply with
        
            Returns:
                a new unit representing the this times the other unit
        
        
        """
        ...
    @staticmethod
    def parse(string: str) -> 'Unit':
        """
            Parse a unit.
        
            The grammar for unit specification allows chains units multiplication and division, as well as putting powers on units.
        
            The symbols used for units are the SI units with some extensions.
        
            year
              the accepted non-SI unit for Julian year is "a" but we also accept "yr"
        
            dimensionless
              both "1" and "#" (U+0023, NUMBER SIGN) are accepted
        
            mass
              "g" is the standard symbol, despite the unit is "kg" (its the only unit that has a prefix in its name, so all multiples
                must be based on "g")
        
            degrees
              the base symbol for degrees is "Â°" (U+00B0, DEGREE SIGN), but we also accept "â—¦" (U+25E6, WHITE BULLET) and "deg"
        
            arcminute
              The base symbol for is "â€²" (U+2032, PRIME) but we also accept "'" (U+0027, APOSTROPHE)
        
            arcsecond
              The base symbol for is "Ã¢â‚¬Â³" (U+2033, DOUBLE PRIME) but we also accept "''" (two occurrences of U+0027, APOSTROPHE),
                "\"" (U+0022, QUOTATION MARK) and "as"
        
        
            All the SI prefix (from "y", yocto, to "Y", Yotta) are accepted, as well as integer prefixes. The standard symbol for
            micro 10Ã¢ï¿½Â»Ã¢ï¿½Â¶ is "Ã‚Âµ" (U+00B5, MICRO SIGN), but we also accept "ÃŽÂ¼" (U+03BC, GREEK SMALL LETTER MU). Beware
            that some combinations are forbidden, for example "Pa" is Pascal, not peta-years, and "as" is arcsecond for this parser,
            not atto-seconds, because many people in the space field use mas for milliarcseconds and Ã‚Âµas for microarcseconds.
            Beware that prefixes are case-sensitive! Integer prefixes can be used to specify units like "30s", but only once at the
            beginning of the specification (i.e. "2rev/dÃ‚Â²" is accepted, but "rev/(2d)Ã‚Â²" is refused). Conforming with SI
            brochure "The International System of Units" (9th edition, 2019), each SI prefix is part of the unit and precedes the
            unit symbol without a separator (i.e. MHz is seen as one identifier).
        
            multiplication
              can specified with either "*" (U+002A, ASTERISK), "Ãƒâ€”" (U+00D7, MULTIPLICATION SIGN), "." (U+002E, FULL STOP) or
                "Ã‚Â·" (U+00B7, MIDDLE DOT) as the operator
        
            division
              can be specified with either "/" (U+002F, SOLIDUS) or "â�„" (U+2044, FRACTION SLASH) as the operator
        
            powers
              can be specified either by
        
                  - prefixing with the unicode "âˆš" (U+221A, SQUARE ROOT) character
                  - postfixing with "**", "^" or implicitly using unicode superscripts
        
        
        
            Exponents can be specified in different ways:
        
              - as an integer, as in "m^-2" or "mâ�»Â²"
              - directly as unicode characters for the few fractions that unicode supports, as in "Î©^â…ž"
              - as the special decimal value 0.5 which is used by CCSDS, as in "km**0.5"
              - as a pair of parentheses surrounding two integers separated by a solidus or fraction slash, as in "Pa^(11/12)"
        
            For integer exponents, the digits must be ASCII digits from the Basic Latin block from unicode if explicit exponent
            maker "**" or "^" was used, or using unicode superscript digits if implicit exponentiation (i.e. no markers at all) is
            used. Unicode superscripts are not allowed for fractional exponents because unicode does not provide a superscript
            solidus. Negative exponents can be used too.
        
            These rules mean all the following (silly) examples are parsed properly: MHz, km/Ã¢Ë†Å¡d, kg.m.sÃ¢ï¿½Â»Ã‚Â¹,
            Ã‚Âµas^Ã¢â€¦â€“/(h**(2)Ãƒâ€”m)Ã‚Â³, km/Ã¢Ë†Å¡(kg.s), km**0.5, 2rev/dÃ‚Â²
        
            Parameters:
                unitSpecification (String): unit specification to parse
        
            Returns:
                parsed unit
        
        
        """
        ...
    def power(self, string: str, fraction: org.hipparchus.fraction.Fraction) -> 'Unit':
        """
            Create power of unit.
        
            Parameters:
                newName (String): name of the new unit
                exponent (Fraction): exponent to apply
        
            Returns:
                a new unit representing the power of the instance
        
        
        """
        ...
    def sameDimension(self, unit: 'Unit') -> bool:
        """
            Check if a unit has the same dimension as another unit.
        
            Parameters:
                other (:class:`~org.orekit.utils.units.Unit`): other unit to check against
        
            Returns:
                true if unit has the same dimension as the other unit
        
        
        """
        ...
    def sameDimensionSI(self) -> 'Unit':
        """
            Create the SI unit with same dimension.
        
            Returns:
                a new unit, with same dimension as instance and scaling factor set to 1.0
        
        
        """
        ...
    def scale(self, string: str, double: float) -> 'Unit':
        """
            Scale a unit.
        
            Parameters:
                newName (String): name of the new unit
                factor (double): scaling factor
        
            Returns:
                a new unit representing scale times the instance
        
        
        """
        ...
    def sqrt(self, string: str) -> 'Unit':
        """
            Create root of unit.
        
            Parameters:
                newName (String): name of the new unit
        
            Returns:
                a new unit representing the square root of the instance
        
        
        """
        ...
    @typing.overload
    def toSI(self, double: float) -> float:
        """
            Convert a value to SI units.
        
            Parameters:
                value (double): value instance unit
        
            Returns:
                value in SI units
        
            Convert a value to SI units.
        
            Parameters:
                value (Double): value instance unit
        
            Returns:
                value in SI units
        
        
        """
        ...
    @typing.overload
    def toSI(self, double: float) -> float: ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UnitsCache:
    """
    public class UnitsCache extends Object
    
        Cache for parsed units.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getUnits(self, string: str) -> Unit:
        """
            Get units from a string specification.
        
            Parsing is performed only the first time a specification is encountered, so the cache speeds up cases where the same
            units is encountered many times (for example when parsing CCSDS messages with many entries).
        
            Parameters:
                specification (String): units specification (may be null)
        
            Returns:
                parsed units (:meth:`~org.orekit.utils.units.Unit.NONE` if specification is null)
        
        
        """
        ...

class UnitsConverter:
    """
    public class UnitsConverter extends Object
    
        Converter between units.
    
        Instances of this class are immutable.
    
        Since:
            11.0
    """
    IDENTITY: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` IDENTITY
    
        Identity converter.
    
    """
    PERCENTS_TO_UNIT: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` PERCENTS_TO_UNIT
    
        Percents to units converter.
    
    """
    ARC_SECONDS_TO_RADIANS: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` ARC_SECONDS_TO_RADIANS
    
        Arcseconds to radians converter.
    
    """
    MILLI_ARC_SECONDS_TO_RADIANS: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` MILLI_ARC_SECONDS_TO_RADIANS
    
        Milli arcseconds to radians converter.
    
    """
    MILLI_SECONDS_TO_SECONDS: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` MILLI_SECONDS_TO_SECONDS
    
        Milli seconds to seconds converter.
    
    """
    DAYS_TO_SECONDS: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` DAYS_TO_SECONDS
    
        Days to seconds converter.
    
    """
    KILOMETRES_TO_METRES: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` KILOMETRES_TO_METRES
    
        Kilometres to metres converter.
    
    """
    KILOMETRES_2_TO_METRES_2: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` KILOMETRES_2_TO_METRES_2
    
        Square kilometres to square metres converter.
    
    """
    KM3_P_S2_TO_M3_P_S2: typing.ClassVar['UnitsConverter'] = ...
    """
    public static final :class:`~org.orekit.utils.units.UnitsConverter` KM3_P_S2_TO_M3_P_S2
    
        kmÂ³/sÂ² to mÂ³/sÂ² converter.
    
    """
    def __init__(self, unit: Unit, unit2: Unit): ...
    def convert(self, double: float) -> float:
        """
            Convert a value.
        
            Parameters:
                value (double): value in the :meth:`~org.orekit.utils.units.UnitsConverter.getFrom`
        
            Returns:
                value converted in the :meth:`~org.orekit.utils.units.UnitsConverter.getTo`
        
        
        """
        ...
    def getFrom(self) -> Unit:
        """
            Get the source unit.
        
            Returns:
                source unit
        
        
        """
        ...
    def getTo(self) -> Unit:
        """
            Get the destination unit.
        
            Returns:
                destination unit
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.utils.units")``.

    Parser: typing.Type[Parser]
    PowerTerm: typing.Type[PowerTerm]
    Unit: typing.Type[Unit]
    UnitsCache: typing.Type[UnitsCache]
    UnitsConverter: typing.Type[UnitsConverter]
