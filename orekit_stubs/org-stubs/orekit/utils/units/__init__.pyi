
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.util
import org.hipparchus
import org.hipparchus.fraction
import typing



class Parser:
    """
    Parser for units.
    
    This fairly basic parser uses recursive descent with the following grammar, where '' can in fact be either '', '×', '.', or '·', '/' can be either '/' or '⁄' and '^' can be either '^', "*" or implicit with switch to superscripts, and fraction are either unicode fractions like ½ or ⅞ or the decimal value 0.5. The special cases "n/a" returns a null list. It is intended to manage the special unit NONE.
    
       unit         ::=  "n/a" | chain chain        ::=  operand { ('' | '/') operand } operand      ::=  integer | integer term | term term         ::=  '√' base | base power power        ::=  '^' exponent | ε exponent     ::=  'fraction'   | integer | '(' integer denominator ')' denominator  ::=  '/' integer  | ε base         ::=  identifier | '(' chain ')'
    
    This parses correctly units like MHz, km/√d, kg.m.s⁻¹, µas^⅖/(h*(2)×m)³, km/√(kg.s), √kgkm** (3/2) /(µs^2Ω⁻⁷), km*0.5/s, #/y, 2rev/d², 1/s.
    
    Note that we don't accept combining square roots and power on the same operand; km/√d³ is refused (but km/√(d³) is accepted). We also accept a single integer prefix and only at the start of the specification.
    
    Since:
        11.0
    """
    @staticmethod
    def buildTermsList(unitsSpecification: str) -> java.util.List['PowerTerm']:
        """
        Build the list of terms corresponding to a units specification.
        
        Parameters:
            unitsSpecification (String): units specification to parse
        
        Returns:
            parse tree
        
        
        """
        ...

class PowerTerm:
    """
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
    Basic handling of multiplicative units.
    
    This class is by no means a complete handling of units. For complete support, look at libraries like UOM. This class handles only time, length, mass and current dimensions, as well as angles (which are dimensionless).
    
    Instances of this class are immutable.
    
    Since:
        11.0
    
    Also see:
        uom, serialized
    """
    NONE: typing.ClassVar['Unit'] = ...
    """
    No unit.
    """
    ONE: typing.ClassVar['Unit'] = ...
    """
    Dimensionless unit.
    """
    CYCLE: typing.ClassVar['Unit'] = ...
    """
    Cycle unit.
    
    Since:
        13.0
    
    
    """
    PERCENT: typing.ClassVar['Unit'] = ...
    """
    Percentage unit.
    """
    SECOND: typing.ClassVar['Unit'] = ...
    """
    Second unit.
    """
    MINUTE: typing.ClassVar['Unit'] = ...
    """
    Minute unit.
    """
    HOUR: typing.ClassVar['Unit'] = ...
    """
    Hour unit.
    """
    DAY: typing.ClassVar['Unit'] = ...
    """
    Day unit.
    """
    YEAR: typing.ClassVar['Unit'] = ...
    """
    Julian year unit.
    
    Also see:
        units
    
    
    """
    HERTZ: typing.ClassVar['Unit'] = ...
    """
    Hertz unit.
    """
    METRE: typing.ClassVar['Unit'] = ...
    """
    Metre unit.
    """
    KILOMETRE: typing.ClassVar['Unit'] = ...
    """
    Kilometre unit.
    """
    KILOGRAM: typing.ClassVar['Unit'] = ...
    """
    Kilogram unit.
    """
    GRAM: typing.ClassVar['Unit'] = ...
    """
    Gram unit.
    """
    AMPERE: typing.ClassVar['Unit'] = ...
    """
    Ampere unit.
    """
    RADIAN: typing.ClassVar['Unit'] = ...
    """
    Radian unit.
    """
    DEGREE: typing.ClassVar['Unit'] = ...
    """
    Degree unit.
    """
    ARC_MINUTE: typing.ClassVar['Unit'] = ...
    """
    Arc minute unit.
    """
    ARC_SECOND: typing.ClassVar['Unit'] = ...
    """
    Arc second unit.
    """
    REVOLUTION: typing.ClassVar['Unit'] = ...
    """
    Revolution unit.
    """
    NEWTON: typing.ClassVar['Unit'] = ...
    """
    Newton unit.
    """
    PASCAL: typing.ClassVar['Unit'] = ...
    """
    Pascal unit.
    """
    BAR: typing.ClassVar['Unit'] = ...
    """
    Bar unit.
    """
    JOULE: typing.ClassVar['Unit'] = ...
    """
    Joule unit.
    """
    WATT: typing.ClassVar['Unit'] = ...
    """
    Watt unit.
    """
    COULOMB: typing.ClassVar['Unit'] = ...
    """
    Coulomb unit.
    """
    VOLT: typing.ClassVar['Unit'] = ...
    """
    Volt unit.
    """
    OHM: typing.ClassVar['Unit'] = ...
    """
    Ohm unit.
    """
    TESLA: typing.ClassVar['Unit'] = ...
    """
    tesla unit.
    """
    SOLAR_FLUX_UNIT: typing.ClassVar['Unit'] = ...
    """
    Solar Flux Unit.
    """
    TOTAL_ELECTRON_CONTENT_UNIT: typing.ClassVar['Unit'] = ...
    """
    Total Electron Content Unit.
    """
    EARTH_RADII: typing.ClassVar['Unit'] = ...
    """
    Earth Radii used as Bstar unit in CCSDS OMM.
    """
    def __init__(self, name: str, scale: float, mass: org.hipparchus.fraction.Fraction, length: org.hipparchus.fraction.Fraction, time: org.hipparchus.fraction.Fraction, current: org.hipparchus.fraction.Fraction, angle: org.hipparchus.fraction.Fraction):
        """
        Simple constructor.
        
        Parameters:
            name (String): name of the unit
            scale (double): scaling factor to SI units
            mass (Fraction): mass exponent
            length (Fraction): length exponent
            time (Fraction): time exponent
            current (Fraction): current exponent
            angle (Fraction): angle exponent
        
        
        """
        ...
    def alias(self, newName: str) -> 'Unit':
        """
        Create an alias for a unit.
        
        Parameters:
            newName (String): name of the new unit
        
        Returns:
            a new unit representing same unit as the instance but with a different name
        
        
        """
        ...
    def divide(self, newName: str, other: 'Unit') -> 'Unit':
        """
        Create quotient of units.
        
        Parameters:
            newName (String): name of the new unit
            other (Unit): unit to divide with
        
        Returns:
            a new unit representing the this divided by the other unit
        
        
        """
        ...
    @staticmethod
    def ensureCompatible(description: str, reference: java.util.List['Unit'], units: bool, allowScaleDifferences: java.util.List['Unit']) -> None:
        """
        Ensure some units are compatible with reference units.
        
        Parameters:
            description (String): description of the units list (for error message generation)
            reference (List<Unit> reference): reference units
            units (boolean): units to check
            allowScaleDifferences (List<Unit> units): if true, unit with same dimension but different scale (like KILOMETRE versus
                METRE) are allowed, otherwise they will trigger an exception
        
        Raises:
            OrekitException: if units are not compatible (number of elements, dimensions or scaling)
        
        
        """
        ...
    def equals(self, unit: typing.Any) -> bool:
        """
        Check if the instance represents the same unit as another instance.
        
        The name is not considered so aliases are considered equal.
        
        Overrides: Object in class Object
        
        Parameters:
            unit (Object): other unit
        
        Returns:
            true if the instance and the other unit refer to the same unit
        
        
        """
        ...
    _fromSI_2__T = typing.TypeVar('_fromSI_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
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
    @typing.overload
    def fromSI(self, value: _fromSI_2__T) -> _fromSI_2__T:
        """
        Convert a value from SI units.
        
        Parameters:
            value (T): value SI unit
        
        Returns:
            value in instance units
        
        
        """
        ...
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
        
        Overrides: Object in class Object
        
        Returns:
            hashcode
        
        
        """
        ...
    def multiply(self, newName: str, other: 'Unit') -> 'Unit':
        """
        Create product of units.
        
        Parameters:
            newName (String): name of the new unit
            other (Unit): unit to multiply with
        
        Returns:
            a new unit representing the this times the other unit
        
        
        """
        ...
    @staticmethod
    def parse(unitSpecification: str) -> 'Unit':
        """
        Parse a unit.
        
        The grammar for unit specification allows chains units multiplication and division, as well as putting powers on units.
        
        The symbols used for units are the SI units with some extensions.
        
        year the accepted non-SI unit for Julian year is "a" but we also accept "yr"
        
        day the accepted non-SI unit for day is "d" but we also accept "day"
        
        dimensionless both "1" and "#" (U+0023, NUMBER SIGN) are accepted
        
        mass "g" is the standard symbol, despite the unit is "kg" (it is the only unit that has a prefix in its name, so all multiples must be based on "g")
        
        degrees the base symbol for degrees is "°" (U+00B0, DEGREE SIGN), but we also accept "◦" (U+25E6, WHITE BULLET) and "deg"
        
        arcminute The base symbol for arcminute is "′" (U+2032, PRIME) but we also accept "'" (U+0027, APOSTROPHE)
        
        arcsecond The base symbol for arcsecond is "″" (U+2033, DOUBLE PRIME) but we also accept "''" (two occurrences of U+0027, APOSTROPHE), "\"" (U+0022, QUOTATION MARK) and "as"
        
        All the SI prefix (from "y", yocto, to "Y", Yotta) are accepted, as well as integer prefixes. The standard symbol for micro 10⁻⁶ is "µ" (U+00B5, MICRO SIGN), but we also accept "μ" (U+03BC, GREEK SMALL LETTER MU). Beware that some combinations are forbidden, for example "Pa" is Pascal, not peta-years, and "as" is arcsecond for this parser, not atto-seconds, because many people in the space field use mas for milliarcseconds and µas for microarcseconds. Beware that prefixes are case-sensitive! Integer prefixes can be used to specify units like "30s", but only once at the beginning of the specification (i.e. "2rev/d²" is accepted, but "rev/(2d)²" is refused). Conforming with SI brochure "The International System of Units" (9th edition, 2019), each SI prefix is part of the unit and precedes the unit symbol without a separator (i.e. MHz is seen as one identifier).
        
        multiplication can specified with either "" (U+002A, ASTERISK), "×" (U+00D7, MULTIPLICATION SIGN), "." (U+002E, FULL STOP) or "·" (U+00B7, MIDDLE DOT) as the operator
        
        division can be specified with either "/" (U+002F, SOLIDUS) or "⁄" (U+2044, FRACTION SLASH) as the operator
        
        powers can be specified either by
        
              - prefixing with the unicode "√" (U+221A, SQUARE ROOT) character
              - postfixing with "", "^" or implicitly using unicode superscripts
        
        
        
        Exponents can be specified in different ways:
        
          - as an integer, as in "m^-2" or "m⁻²"
          - directly as unicode characters for the few fractions that unicode supports, as in "Ω^⅞"
          - as the special decimal value 0.5 which is used by CCSDS, as in "km0.5"
          - as a pair of parentheses surrounding two integers separated by a solidus or fraction slash, as in "Pa^(11/12)"
        
        For integer exponents, the digits must be ASCII digits from the Basic Latin block from unicode if explicit exponent marker "" or "^" is used, or using unicode superscript digits if implicit exponentiation (i.e. no markers at all) is used. Unicode superscripts are not allowed for fractional exponents because unicode does not provide a superscript solidus. Negative exponents can be used too.
        
        These rules mean all the following (silly) examples are parsed properly: MHz, km/√d, kg.m.s⁻¹, µas^⅖/(h(2)×m)³, km/√(kg.s), km*0.5, 2rev/d²
        
        Parameters:
            unitSpecification (String): unit specification to parse
        
        Returns:
            parsed unit
        
        
        """
        ...
    def power(self, newName: str, exponent: org.hipparchus.fraction.Fraction) -> 'Unit':
        """
        Create power of unit.
        
        Parameters:
            newName (String): name of the new unit
            exponent (Fraction): exponent to apply
        
        Returns:
            a new unit representing the power of the instance
        
        
        """
        ...
    def sameDimension(self, other: 'Unit') -> bool:
        """
        Check if a unit has the same dimension as another unit.
        
        Parameters:
            other (Unit): other unit to check against
        
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
    def scale(self, newName: str, factor: float) -> 'Unit':
        """
        Scale a unit.
        
        Parameters:
            newName (String): name of the new unit
            factor (double): scaling factor
        
        Returns:
            a new unit representing scale times the instance
        
        
        """
        ...
    def sqrt(self, newName: str) -> 'Unit':
        """
        Create root of unit.
        
        Parameters:
            newName (String): name of the new unit
        
        Returns:
            a new unit representing the square root of the instance
        
        
        """
        ...
    _toSI_2__T = typing.TypeVar('_toSI_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
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
    @typing.overload
    def toSI(self, value: _toSI_2__T) -> _toSI_2__T:
        """
        Convert a value to SI units.
        
        Parameters:
            value (T): value instance unit
        
        Returns:
            value in SI units
        
        Since:
            12.1
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class UnitsCache:
    """
    Cache for parsed units.
    
    Since:
        11.0
    """
    def __init__(self):
        """
        Simple constructor.
        """
        ...
    def getUnits(self, specification: str) -> Unit:
        """
        Get units from a string specification.
        
        Parsing is performed only the first time a specification is encountered, so the cache speeds up cases where the same units is encountered many times (for example when parsing CCSDS messages with many entries).
        
        Parameters:
            specification (String): units specification (may be null)
        
        Returns:
            parsed units (NONE if specification is null)
        
        
        """
        ...

class UnitsConverter:
    """
    Converter between units.
    
    Instances of this class are immutable.
    
    Since:
        11.0
    """
    IDENTITY: typing.ClassVar['UnitsConverter'] = ...
    """
    Identity converter.
    """
    PERCENTS_TO_UNIT: typing.ClassVar['UnitsConverter'] = ...
    """
    Percents to units converter.
    """
    ARC_SECONDS_TO_RADIANS: typing.ClassVar['UnitsConverter'] = ...
    """
    Arcseconds to radians converter.
    """
    MILLI_ARC_SECONDS_TO_RADIANS: typing.ClassVar['UnitsConverter'] = ...
    """
    Milli arcseconds to radians converter.
    """
    MILLI_SECONDS_TO_SECONDS: typing.ClassVar['UnitsConverter'] = ...
    """
    Milli seconds to seconds converter.
    """
    NANO_TESLAS_TO_TESLAS: typing.ClassVar['UnitsConverter'] = ...
    """
    Nano Teslas to Tesla converter.
    """
    DAYS_TO_SECONDS: typing.ClassVar['UnitsConverter'] = ...
    """
    Days to seconds converter.
    """
    KILOMETRES_TO_METRES: typing.ClassVar['UnitsConverter'] = ...
    """
    Kilometres to metres converter.
    """
    KILOMETRES_2_TO_METRES_2: typing.ClassVar['UnitsConverter'] = ...
    """
    Square kilometres to square metres converter.
    """
    KM3_P_S2_TO_M3_P_S2: typing.ClassVar['UnitsConverter'] = ...
    """
    km³/s² to m³/s² converter.
    """
    def __init__(self, from_: Unit, to: Unit):
        """
        Simple constructor.
        
        Parameters:
            from (Unit): source unit
            to (Unit): destination unit
        
        
        """
        ...
    def convert(self, value: float) -> float:
        """
        Convert a value.
        
        Parameters:
            value (double): value in the getFrom
        
        Returns:
            value converted in the getTo
        
        
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
        Overrides: Object in class Object
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.utils.units")``.

    Parser: typing.Type[Parser]
    PowerTerm: typing.Type[PowerTerm]
    Unit: typing.Type[Unit]
    UnitsCache: typing.Type[UnitsCache]
    UnitsConverter: typing.Type[UnitsConverter]
