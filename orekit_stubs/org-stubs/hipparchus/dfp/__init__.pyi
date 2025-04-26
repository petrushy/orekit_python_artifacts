
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import jpype
import org.hipparchus
import org.hipparchus.util
import typing



class Dfp(org.hipparchus.CalculusFieldElement['Dfp']):
    """
    public classDfp extends :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.dfp.Dfp`>
    
        Decimal floating point library for Java
    
        Another floating point class. This one is built using radix 10000 which is 10 :sup:`4` , so its almost decimal.
    
        The design goals here are:
    
          1.  Decimal math, or close to it
          2.  Settable precision (but no mix between numbers using different settings)
          3.  Portability. Code should be kept as portable as possible.
          4.  Performance
          5.  Accuracy - Results should always be +/- 1 ULP for basic algebraic operation
          6.  Comply with IEEE 854-1987 as much as possible. (See IEEE 854-1987 notes below)
    
    
        Trade offs:
    
          1.  Memory foot print. I'm using more memory than necessary to represent numbers to get better performance.
          2.  Digits are bigger, so rounding is a greater loss. So, if you really need 12 decimal digits, better use 4 base 10000
            digits there can be one partially filled.
    
    
        Numbers are represented in the following form: \[ n = \mathrm{sign} \times \mathrm{mant} \times
        \mathrm{radix}^\mathrm{exp} \] where sign is ±1, mantissa represents a fractional number between zero and one. mant[0]
        is the least significant digit. exp is in the range of -32767 to 32768
    
        IEEE 854-1987 Notes and differences
    
        IEEE 854 requires the radix to be either 2 or 10. The radix here is 10000, so that requirement is not met, but it is
        possible that a subclassed can be made to make it behave as a radix 10 number. It is my opinion that if it looks and
        behaves as a radix 10 number then it is one and that requirement would be met.
    
        The radix of 10000 was chosen because it should be faster to operate on 4 decimal digits at once instead of one at a
        time. Radix 10 behavior can be realized by adding an additional rounding step to ensure that the number of decimal
        digits represented is constant.
    
        The IEEE standard specifically leaves out internal data encoding, so it is reasonable to conclude that such a subclass
        of this radix 10000 system is merely an encoding of a radix 10 system.
    
        IEEE 854 also specifies the existence of "sub-normal" numbers. This class does not contain any such entities. The most
        significant radix 10000 digit is always non-zero. Instead, we support "gradual underflow" by raising the underflow flag
        for numbers less with exponent less than expMin, but don't flush to zero until the exponent reaches MIN_EXP-digits. Thus
        the smallest number we can represent would be: 1E(-(MIN_EXP-digits-1)*4), eg, for digits=5, MIN_EXP=-32767, that would
        be 1e-131092.
    
        IEEE 854 defines that the implied radix point lies just to the right of the most significant digit and to the left of
        the remaining digits. This implementation puts the implied radix point to the left of all digits including the most
        significant one. The most significant digit here is the one just to the right of the radix point. This is a fine detail
        and is really only a matter of definition. Any side effects of this can be rendered invisible by a subclass.
    
        Also see:
    
              - :class:`~org.hipparchus.dfp.DfpField`
    """
    RADIX: typing.ClassVar[int] = ...
    """
    public static final int RADIX
    
        The radix, or base of this system. Set to 10000
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    MIN_EXP: typing.ClassVar[int] = ...
    """
    public static final int MIN_EXP
    
        The minimum exponent before underflow is signaled. Flush to zero occurs at minExp-DIGITS
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    MAX_EXP: typing.ClassVar[int] = ...
    """
    public static final int MAX_EXP
    
        The maximum exponent before overflow is signaled and results flushed to infinity
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    ERR_SCALE: typing.ClassVar[int] = ...
    """
    public static final int ERR_SCALE
    
        The amount under/overflows are scaled by before going to trap handler
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    FINITE: typing.ClassVar[int] = ...
    """
    public static final byte FINITE
    
        Indicator value for normal finite numbers.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    INFINITE: typing.ClassVar[int] = ...
    """
    public static final byte INFINITE
    
        Indicator value for Infinity.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    SNAN: typing.ClassVar[int] = ...
    """
    public static final byte SNAN
    
        Indicator value for signaling NaN.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    QNAN: typing.ClassVar[int] = ...
    """
    public static final byte QNAN
    
        Indicator value for quiet NaN.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    def __init__(self, dfp: 'Dfp'): ...
    def abs(self) -> 'Dfp':
        """
            absolute value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'Dfp':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Dfp':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> org.hipparchus.FieldElement:
        """
            Add x to this.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): number to add
        
            Returns:
                sum of this and x
        
        
        """
        ...
    @typing.overload
    def add(self, dfp: 'Dfp') -> 'Dfp': ...
    def asin(self) -> 'Dfp':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Dfp':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'Dfp':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, dfp: 'Dfp') -> 'Dfp':
        """
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders are inconsistent
        
        
        """
        ...
    def atanh(self) -> 'Dfp':
        """
            Inverse hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def ceil(self) -> 'Dfp':
        """
            Round to an integer using the round ceil mode. That is, round toward +Infinity
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                rounded value
        
        
        """
        ...
    def classify(self) -> int:
        """
            Returns the type - one of FINITE, INFINITE, SNAN, QNAN.
        
            Returns:
                type of the number
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Dfp':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                s (:class:`~org.hipparchus.dfp.Dfp`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                s (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, dfp: 'Dfp') -> 'Dfp': ...
    @staticmethod
    def copysign(dfp: 'Dfp', dfp2: 'Dfp') -> 'Dfp':
        """
            Creates an instance that is the same as x except that it has the sign of y. abs(x) = dfp.copysign(x, dfp.one)
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): number to get the value from
                y (:class:`~org.hipparchus.dfp.Dfp`): number to get the sign from
        
            Returns:
                a number with the value of x and the sign of y
        
        
        """
        ...
    def cos(self) -> 'Dfp':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Dfp':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> org.hipparchus.FieldElement:
        """
            Divide this by divisor.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                divisor (:class:`~org.hipparchus.dfp.Dfp`): divisor
        
            Returns:
                quotient of this by divisor
        
            Divide by a single digit less than radix. Special case, so there are speed advantages. 0 <= divisor < radix
        
            Parameters:
                divisor (int): divisor
        
            Returns:
                quotient of this by divisor
        
        
        """
        ...
    @typing.overload
    def divide(self, int: int) -> 'Dfp': ...
    @typing.overload
    def divide(self, dfp: 'Dfp') -> 'Dfp': ...
    def dotrap(self, int: int, string: str, dfp: 'Dfp', dfp2: 'Dfp') -> 'Dfp':
        """
            Raises a trap. This does not set the corresponding flag however.
        
            Parameters:
                type (int): the trap type
                what (:class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): - name of routine trap occurred in
                oper (:class:`~org.hipparchus.dfp.Dfp`): - input operator to function
                result (:class:`~org.hipparchus.dfp.Dfp`): - the result computed prior to the trap
        
            Returns:
                The suggested return value from the trap handler
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
            Check if instance is equal to x.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Parameters:
                other (:class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`): object to check instance against
        
            Returns:
                true if instance is equal to x and neither are NaN, false otherwise
        
        
        """
        ...
    def exp(self) -> 'Dfp':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Dfp':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'Dfp':
        """
            Round to an integer using the round floor mode. That is, round toward -Infinity
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                rounded value
        
        
        """
        ...
    def getAddendum(self) -> 'Dfp':
        """
            Get the addendum to the real value of the number.
        
            The addendum is considered to be the part that when added back to the :meth:`~org.hipparchus.FieldElement.getReal`
            recovers the instance. This means that when :code:`e.getReal()` is finite (i.e. neither infinite nor NaN), then
            :code:`e.getAddendum().add(e.getReal())` is :code:`e` and :code:`e.subtract(e.getReal())` is :code:`e.getAddendum()`.
            Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always
            holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives
            types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the
            subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getAddendum` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def getExponent(self) -> int:
        """
            Return the exponent of the instance, removing the bias.
        
            For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getExponent` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponent for the instance, without bias
        
        
        """
        ...
    def getField(self) -> 'DfpField':
        """
            Get the :class:`~org.hipparchus.Field` (really a :class:`~org.hipparchus.dfp.DfpField`) to which the instance belongs.
        
            The field is linked to the number of digits and acts as a factory for :class:`~org.hipparchus.dfp.Dfp` instances.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getField` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                :class:`~org.hipparchus.Field` (really a :class:`~org.hipparchus.dfp.DfpField`) to which the instance belongs
        
        
        """
        ...
    def getOne(self) -> 'Dfp':
        """
            Get the constant 1.
        
            Returns:
                a Dfp with value one
        
        
        """
        ...
    def getPi(self) -> 'Dfp':
        """
            Get the Archimedes constant π.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant π
        
        
        """
        ...
    def getRadixDigits(self) -> int:
        """
            Get the number of radix digits of the instance.
        
            Returns:
                number of radix digits
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def getTwo(self) -> 'Dfp':
        """
            Get the constant 2.
        
            Returns:
                a Dfp with value two
        
        
        """
        ...
    def getZero(self) -> 'Dfp':
        """
            Get the constant 0.
        
            Returns:
                a Dfp with value zero
        
        
        """
        ...
    def greaterThan(self, dfp: 'Dfp') -> bool:
        """
            Check if instance is greater than x.
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): number to check instance against
        
            Returns:
                true if instance is greater than x and neither are NaN, false otherwise
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Gets a hashCode for the instance.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, dfp: 'Dfp') -> 'Dfp':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2`  +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.dfp.Dfp`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    def intLog10(self) -> int:
        """
            Get the exponent of the greatest power of 10 that is less than or equal to abs(this).
        
            Returns:
                integer base 10 logarithm
        
        
        """
        ...
    def intValue(self) -> int:
        """
            Convert this to an integer. If greater than 2147483647, it returns 2147483647. If less than -2147483648 it returns
            -2147483648.
        
            Returns:
                converted number
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Check if the instance is infinite.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isInfinite` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                true if the instance is infinite
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check if the instance is Not a Number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.isNaN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                true if the instance is Not a Number
        
        
        """
        ...
    def isZero(self) -> bool:
        """
            Check if instance is equal to zero.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.isZero` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                true if instance is equal to zero
        
        
        """
        ...
    def lessThan(self, dfp: 'Dfp') -> bool:
        """
            Check if instance is less than x.
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): number to check instance against
        
            Returns:
                true if instance is less than x and neither are NaN, false otherwise
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, dfp: 'Dfp', double2: float, dfp2: 'Dfp') -> 'Dfp':
        """
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the first term
                b1 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the first term
                a2 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the second term
                b2 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the first term
                b1 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the first term
                a2 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the second term
                b2 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the second term
                a3 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the third term
                b3 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the first term
                b1 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the first term
                a2 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the second term
                b2 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the second term
                a3 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the third term
                b3 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the third term
                a4 (:class:`~org.hipparchus.dfp.Dfp`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination` in
                interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.dfp.Dfp`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, dfp: 'Dfp', double2: float, dfp2: 'Dfp', double3: float, dfp3: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, double: float, dfp: 'Dfp', double2: float, dfp2: 'Dfp', double3: float, dfp3: 'Dfp', double4: float, dfp4: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], dfpArray: typing.Union[typing.List['Dfp'], jpype.JArray]) -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfp: 'Dfp', dfp2: 'Dfp', dfp3: 'Dfp', dfp4: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfp: 'Dfp', dfp2: 'Dfp', dfp3: 'Dfp', dfp4: 'Dfp', dfp5: 'Dfp', dfp6: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfp: 'Dfp', dfp2: 'Dfp', dfp3: 'Dfp', dfp4: 'Dfp', dfp5: 'Dfp', dfp6: 'Dfp', dfp7: 'Dfp', dfp8: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def linearCombination(self, dfpArray: typing.Union[typing.List['Dfp'], jpype.JArray], dfpArray2: typing.Union[typing.List['Dfp'], jpype.JArray]) -> 'Dfp': ...
    def log(self) -> 'Dfp':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Dfp':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log10K(self) -> int:
        """
            Get the exponent of the greatest power of 10000 that is less than or equal to the absolute value of this. I.E. if this
            is 10 :sup:`6` then log10K would return 1.
        
            Returns:
                integer base 10000 logarithm
        
        
        """
        ...
    def log1p(self) -> 'Dfp':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> org.hipparchus.FieldElement:
        """
            Multiply this by x.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): multiplicand
        
            Returns:
                product of this and x
        
            Multiply this by a single digit x.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                x (int): multiplicand
        
            Returns:
                product of this and x
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'Dfp': ...
    @typing.overload
    def multiply(self, dfp: 'Dfp') -> 'Dfp': ...
    def negate(self) -> 'Dfp':
        """
            Returns a number that is this number with the sign bit reversed.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of this
        
        
        """
        ...
    def negativeOrNull(self) -> bool:
        """
            Check if instance is less than or equal to 0.
        
            Returns:
                true if instance is not NaN and less than or equal to 0, false otherwise
        
        
        """
        ...
    @typing.overload
    def newInstance(self) -> 'Dfp':
        """
            Create an instance with a value of 0. Use this internally in preference to constructors to facilitate subclasses
        
            Returns:
                a new instance with a value of 0
        
        """
        ...
    @typing.overload
    def newInstance(self, byte: int) -> 'Dfp':
        """
            Create an instance from a byte value.
        
            Parameters:
                x (byte): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance from an int value.
        
            Parameters:
                x (int): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance from a long value.
        
            Parameters:
                x (long): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                x (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
            Create an instance by copying an existing one. Use this internally in preference to constructors to facilitate
            subclasses.
        
            Parameters:
                d (:class:`~org.hipparchus.dfp.Dfp`): instance to copy
        
            Returns:
                a new instance with the same value as d
        
            Create an instance from a String representation. Use this internally in preference to constructors to facilitate
            subclasses.
        
            Parameters:
                s (:class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): string representation of the instance
        
            Returns:
                a new instance parsed from specified string
        
            Creates an instance with a non-finite value.
        
            Parameters:
                sig (byte): sign of the Dfp to create
                code (byte): code of the value, must be one of :meth:`~org.hipparchus.dfp.Dfp.INFINITE`, :meth:`~org.hipparchus.dfp.Dfp.SNAN`,
                    :meth:`~org.hipparchus.dfp.Dfp.QNAN`
        
            Returns:
                a new instance with a non-finite value
        
            Creates an instance by converting the instance to a different field (i.e. different accuracy).
        
            If the target field as a greater number of digits, the extra least significant digits will be set to zero.
        
            Parameters:
                targetField (:class:`~org.hipparchus.dfp.DfpField`): field to convert the instance to
                rmode (:class:`~org.hipparchus.dfp.DfpField.RoundingMode`): rounding mode to use if target field as less digits than the instance, can be null otherwise
        
            Returns:
                converted instance (or the instance itself if it already has the required number of digits)
        
            Since:
                1.7
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.DfpField.getExtendedField`
        
        
        
        """
        ...
    @typing.overload
    def newInstance(self, byte: int, byte2: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, double: float) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, int: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, string: str) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, long: int) -> 'Dfp': ...
    @typing.overload
    def newInstance(self, dfp: 'Dfp') -> 'Dfp': ...
    @typing.overload
    def newInstance(self, dfpField: 'DfpField', roundingMode: 'DfpField.RoundingMode') -> 'Dfp': ...
    def nextAfter(self, dfp: 'Dfp') -> 'Dfp':
        """
            Returns the next number greater than this one in the direction of x. If this==x then simply returns this.
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): direction where to look at
        
            Returns:
                closest number next to instance in the direction of x
        
        
        """
        ...
    def positiveOrNull(self) -> bool:
        """
            Check if instance is greater than or equal to 0.
        
            Returns:
                true if instance is not NaN and greater than or equal to 0, false otherwise
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'Dfp':
        """
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
            Integer power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                e (:class:`~org.hipparchus.dfp.Dfp`): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'Dfp': ...
    @typing.overload
    def pow(self, dfp: 'Dfp') -> 'Dfp': ...
    def power10(self, int: int) -> 'Dfp':
        """
            Return the specified power of 10.
        
            Parameters:
                e (int): desired power
        
            Returns:
                10 :sup:`e`
        
        
        """
        ...
    def power10K(self, int: int) -> 'Dfp':
        """
            Get the specified power of 10000.
        
            Parameters:
                e (int): desired power
        
            Returns:
                10000 :sup:`e`
        
        
        """
        ...
    def reciprocal(self) -> 'Dfp':
        """
            Returns the multiplicative inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Dfp':
        """
            Returns the IEEE remainder.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                d (:class:`~org.hipparchus.dfp.Dfp`): divisor
        
            Returns:
                this less n × d, where n is the integer closest to this/d
        
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, dfp: 'Dfp') -> 'Dfp': ...
    def rint(self) -> 'Dfp':
        """
            Round to nearest integer using the round-half-even method. That is round to nearest integer unless both are equidistant.
            In which case round to the even one.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                rounded value
        
        
        """
        ...
    def rootN(self, int: int) -> 'Dfp':
        """
            N :sup:`th` root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rootN` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, int: int) -> 'Dfp':
        """
            Multiply the instance by a power of 2.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.scalb` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power of 2
        
            Returns:
                this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'Dfp':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Dfp':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinh(self) -> 'Dfp':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Dfp']: ...
    def sqrt(self) -> 'Dfp':
        """
            Compute the square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    def square(self) -> 'Dfp':
        """
            Compute this × this.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.square` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a new element representing this × this
        
        
        """
        ...
    def strictlyNegative(self) -> bool:
        """
            Check if instance is strictly less than 0.
        
            Returns:
                true if instance is not NaN and less than or equal to 0, false otherwise
        
        
        """
        ...
    def strictlyPositive(self) -> bool:
        """
            Check if instance is strictly greater than 0.
        
            Returns:
                true if instance is not NaN and greater than or equal to 0, false otherwise
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> org.hipparchus.FieldElement:
        """
            Subtract x from this.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): number to subtract
        
            Returns:
                difference of this and a
        
        
        """
        ...
    @typing.overload
    def subtract(self, dfp: 'Dfp') -> 'Dfp': ...
    def tan(self) -> 'Dfp':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Dfp':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> 'Dfp':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toDouble(self) -> float:
        """
            Convert the instance into a double.
        
            Returns:
                a double approximating the instance
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.Dfp.toSplitDouble`
        
        
        
        """
        ...
    def toRadians(self) -> 'Dfp':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toRadians` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def toSplitDouble(self) -> typing.MutableSequence[float]:
        """
            Convert the instance into a split double.
        
            Returns:
                an array of two doubles which sum represent the instance
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.Dfp.toDouble`
        
        
        
        """
        ...
    def toString(self) -> str:
        """
            Get a string representation of the instance.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.toString` in
                class :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
            Returns:
                string representation of the instance
        
        
        """
        ...
    def ulp(self) -> 'Dfp':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
        
        """
        ...
    def unequal(self, dfp: 'Dfp') -> bool:
        """
            Check if instance is not equal to x.
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): number to check instance against
        
            Returns:
                true if instance is not equal to x and neither are NaN, false otherwise
        
        
        """
        ...

class DfpField(org.hipparchus.Field[Dfp]):
    """
    public classDfpField extends :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.dfp.Dfp`>
    
        Field for Decimal floating point instances.
    """
    FLAG_INVALID: typing.ClassVar[int] = ...
    """
    public static final int FLAG_INVALID
    
        IEEE 854-1987 flag for invalid operation.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    FLAG_DIV_ZERO: typing.ClassVar[int] = ...
    """
    public static final int FLAG_DIV_ZERO
    
        IEEE 854-1987 flag for division by zero.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    FLAG_OVERFLOW: typing.ClassVar[int] = ...
    """
    public static final int FLAG_OVERFLOW
    
        IEEE 854-1987 flag for overflow.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    FLAG_UNDERFLOW: typing.ClassVar[int] = ...
    """
    public static final int FLAG_UNDERFLOW
    
        IEEE 854-1987 flag for underflow.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    FLAG_INEXACT: typing.ClassVar[int] = ...
    """
    public static final int FLAG_INEXACT
    
        IEEE 854-1987 flag for inexact result.
    
        Also see:
    
              - :meth:`~constant`
    
    
    
    """
    def __init__(self, int: int): ...
    def clearIEEEFlags(self) -> None:
        """
            Clears the IEEE 854 status flags.
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.DfpField.getIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlagsBits`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        
        """
        ...
    @staticmethod
    def computeExp(dfp: Dfp, dfp2: Dfp) -> Dfp:
        """
            Compute exp(a).
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number for which we want the exponential
                one (:class:`~org.hipparchus.dfp.Dfp`): constant with value 1 at desired precision
        
            Returns:
                exp(a)
        
        
        """
        ...
    @staticmethod
    def computeLn(dfp: Dfp, dfp2: Dfp, dfp3: Dfp) -> Dfp:
        """
            Compute ln(a). Let f(x) = ln(x), We know that f'(x) = 1/x, thus from Taylor's theorem we have: ----- n+1 n f(x) = \ (-1)
            (x - 1) / ---------------- for 1 <= n <= infinity ----- n or 2 3 4 (x-1) (x-1) (x-1) ln(x) = (x-1) - ----- + ------ -
            ------ + ... 2 3 4 alternatively, 2 3 4 x x x ln(x+1) = x - - + - - - + ... 2 3 4 This series can be used to compute
            ln(x), but it converges too slowly. If we substitute -x for x above, we get 2 3 4 x x x ln(1-x) = -x - - - - - - + ... 2
            3 4 Note that all terms are now negative. Because the even powered ones absorbed the sign. Now, subtract the series
            above from the previous one to get ln(x+1) - ln(1-x). Note the even terms cancel out leaving only the odd ones 3 5 7 2x
            2x 2x ln(x+1) - ln(x-1) = 2x + --- + --- + ---- + ... 3 5 7 By the property of logarithms that ln(a) - ln(b) = ln (a/b)
            we have: 3 5 7 x+1 / x x x \ ln ----- = 2 * | x + ---- + ---- + ---- + ... | x-1 \ 3 5 7 / But now we want to find
            ln(a), so we need to find the value of x such that a = (x+1)/(x-1). This is easily solved to find that x = (a-1)/(a+1).
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number for which we want the exponential
                one (:class:`~org.hipparchus.dfp.Dfp`): constant with value 1 at desired precision
                two (:class:`~org.hipparchus.dfp.Dfp`): constant with value 2 at desired precision
        
            Returns:
                ln(a)
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Two fields are considered equals if they have the same number of radix digits and the same rounding mode.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.equals` in
                class :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    def getDegToRad(self) -> Dfp:
        """
            Get the degrees to radians conversion factor.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` for degrees to radians conversion factor
        
        
        """
        ...
    def getE(self) -> Dfp:
        """
            Get the constant e.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value e
        
        
        """
        ...
    def getESplit(self) -> typing.MutableSequence[Dfp]:
        """
            Get the constant e split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value e split in two pieces
        
        
        """
        ...
    def getExtendedField(self, int: int, boolean: bool) -> 'DfpField':
        """
            Get extended field for accuracy conversion.
        
            Parameters:
                digitsFactor (int): multiplication factor for number of digits
                computeConstants (boolean): if true, the transcendental constants for the given precision must be computed (setting this flag to false is RESERVED
                    for the internal recursive call)
        
            Returns:
                field with extended precision
        
            Since:
                1.7
        
        
        """
        ...
    def getIEEEFlags(self) -> int:
        """
            Get the IEEE 854 status flags.
        
            Returns:
                IEEE 854 status flags
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.DfpField.clearIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlagsBits`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        
        """
        ...
    def getLn10(self) -> Dfp:
        """
            Get the constant ln(10).
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(10)
        
        
        """
        ...
    def getLn2(self) -> Dfp:
        """
            Get the constant ln(2).
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(2)
        
        
        """
        ...
    def getLn2Split(self) -> typing.MutableSequence[Dfp]:
        """
            Get the constant ln(2) split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(2) split in two pieces
        
        
        """
        ...
    def getLn5(self) -> Dfp:
        """
            Get the constant ln(5).
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(5)
        
        
        """
        ...
    def getLn5Split(self) -> typing.MutableSequence[Dfp]:
        """
            Get the constant ln(5) split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value ln(5) split in two pieces
        
        
        """
        ...
    def getOne(self) -> Dfp:
        """
            Get the constant 1.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value 1
        
        
        """
        ...
    def getPi(self) -> Dfp:
        """
            Get the constant π.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value π
        
        
        """
        ...
    def getPiSplit(self) -> typing.MutableSequence[Dfp]:
        """
            Get the constant π split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value π split in two pieces
        
        
        """
        ...
    def getRadToDeg(self) -> Dfp:
        """
            Get the radians to degrees conversion factor.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` for radians to degrees conversion factor
        
        
        """
        ...
    def getRadixDigits(self) -> int:
        """
            Get the number of radix digits of the :class:`~org.hipparchus.dfp.Dfp` instances built by this factory.
        
            Returns:
                number of radix digits
        
        
        """
        ...
    def getRoundingMode(self) -> 'DfpField.RoundingMode':
        """
            Get the current rounding mode.
        
            Returns:
                current rounding mode
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[Dfp]: ...
    def getSqr2(self) -> Dfp:
        """
            Get the constant √2.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √2
        
        
        """
        ...
    def getSqr2Reciprocal(self) -> Dfp:
        """
            Get the constant √2 / 2.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √2 / 2
        
        
        """
        ...
    def getSqr2Split(self) -> typing.MutableSequence[Dfp]:
        """
            Get the constant √2 split in two pieces.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √2 split in two pieces
        
        
        """
        ...
    def getSqr3(self) -> Dfp:
        """
            Get the constant √3.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √3
        
        
        """
        ...
    def getSqr3Reciprocal(self) -> Dfp:
        """
            Get the constant √3 / 3.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value √3 / 3
        
        
        """
        ...
    def getTwo(self) -> Dfp:
        """
            Get the constant 2.
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value 2
        
        
        """
        ...
    def getZero(self) -> Dfp:
        """
            Get the constant 0.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getZero` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                a :class:`~org.hipparchus.dfp.Dfp` with value 0
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                :meth:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.hashCode` in
                class :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
        
        
        """
        ...
    @typing.overload
    def newDfp(self) -> Dfp:
        """
            Makes a :class:`~org.hipparchus.dfp.Dfp` with a value of 0.
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with a value of 0
        
        """
        ...
    @typing.overload
    def newDfp(self, byte: int) -> Dfp:
        """
            Create an instance from a byte value.
        
            Parameters:
                x (byte): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Create an instance from an int value.
        
            Parameters:
                x (int): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Create an instance from a long value.
        
            Parameters:
                x (long): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Create an instance from a double value.
        
            Parameters:
                x (double): value to convert to an instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as x
        
            Copy constructor.
        
            Parameters:
                d (:class:`~org.hipparchus.dfp.Dfp`): instance to copy
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with the same value as d
        
            Create a :class:`~org.hipparchus.dfp.Dfp` given a String representation.
        
            Parameters:
                s (:class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): string representation of the instance
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` parsed from specified string
        
            Creates a :class:`~org.hipparchus.dfp.Dfp` with a non-finite value.
        
            Parameters:
                sign (byte): sign of the Dfp to create
                nans (byte): code of the value, must be one of :meth:`~org.hipparchus.dfp.Dfp.INFINITE`, :meth:`~org.hipparchus.dfp.Dfp.SNAN`,
                    :meth:`~org.hipparchus.dfp.Dfp.QNAN`
        
            Returns:
                a new :class:`~org.hipparchus.dfp.Dfp` with a non-finite value
        
        
        """
        ...
    @typing.overload
    def newDfp(self, byte: int, byte2: int) -> Dfp: ...
    @typing.overload
    def newDfp(self, double: float) -> Dfp: ...
    @typing.overload
    def newDfp(self, int: int) -> Dfp: ...
    @typing.overload
    def newDfp(self, string: str) -> Dfp: ...
    @typing.overload
    def newDfp(self, long: int) -> Dfp: ...
    @typing.overload
    def newDfp(self, dfp: Dfp) -> Dfp: ...
    def setIEEEFlags(self, int: int) -> None:
        """
            Sets the IEEE 854 status flags.
        
            Parameters:
                flags (int): desired value for the flags
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.DfpField.getIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.clearIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlagsBits`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        
        """
        ...
    def setIEEEFlagsBits(self, int: int) -> None:
        """
            Sets some bits in the IEEE 854 status flags, without changing the already set bits.
        
            Calling this method is equivalent to call :code:`setIEEEFlags(getIEEEFlags() | bits)`
        
            Parameters:
                bits (int): bits to set
        
            Also see:
        
                  - :meth:`~org.hipparchus.dfp.DfpField.getIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.clearIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.setIEEEFlags`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INVALID`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_DIV_ZERO`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_OVERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_UNDERFLOW`
                  - :meth:`~org.hipparchus.dfp.DfpField.FLAG_INEXACT`
        
        
        
        """
        ...
    def setRoundingMode(self, roundingMode: 'DfpField.RoundingMode') -> None:
        """
            Set the rounding mode. If not set, the default value is
            :meth:`~org.hipparchus.dfp.DfpField.RoundingMode.ROUND_HALF_EVEN`.
        
            Parameters:
                mode (:class:`~org.hipparchus.dfp.DfpField.RoundingMode`): desired rounding mode Note that the rounding mode is common to all :class:`~org.hipparchus.dfp.Dfp` instances belonging
                    to the current :class:`~org.hipparchus.dfp.DfpField` in the system and will affect all future calculations.
        
        
        """
        ...
    class RoundingMode(java.lang.Enum['DfpField.RoundingMode']):
        ROUND_DOWN: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_UP: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_UP: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_DOWN: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_EVEN: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_HALF_ODD: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_CEIL: typing.ClassVar['DfpField.RoundingMode'] = ...
        ROUND_FLOOR: typing.ClassVar['DfpField.RoundingMode'] = ...
        _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
        @typing.overload
        @staticmethod
        def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
        @typing.overload
        @staticmethod
        def valueOf(string: str) -> 'DfpField.RoundingMode': ...
        @staticmethod
        def values() -> typing.MutableSequence['DfpField.RoundingMode']: ...

class DfpMath:
    """
    public classDfpMath extends :class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Mathematical routines for use with :class:`~org.hipparchus.dfp.Dfp`. The constants are defined in
        :class:`~org.hipparchus.dfp.DfpField`
    """
    @staticmethod
    def acos(dfp: Dfp) -> Dfp:
        """
            computes the arc-cosine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which arc-cosine is desired
        
            Returns:
                acos(a)
        
        
        """
        ...
    @staticmethod
    def asin(dfp: Dfp) -> Dfp:
        """
            computes the arc-sine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which arc-sine is desired
        
            Returns:
                asin(a)
        
        
        """
        ...
    @staticmethod
    def atan(dfp: Dfp) -> Dfp:
        """
            computes the arc tangent of the argument Uses the typical taylor series but may reduce arguments using the following
            identity tan(x+y) = (tan(x) + tan(y)) / (1 - tan(x)*tan(y)) since tan(PI/8) = sqrt(2)-1, atan(x) = atan( (x - sqrt(2) +
            1) / (1+x*sqrt(2) - x) + PI/8.0
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which arc-tangent is desired
        
            Returns:
                atan(a)
        
        
        """
        ...
    @staticmethod
    def cos(dfp: Dfp) -> Dfp:
        """
            computes the cosine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which cosine is desired
        
            Returns:
                cos(a)
        
        
        """
        ...
    @staticmethod
    def exp(dfp: Dfp) -> Dfp:
        """
            Computes e to the given power. a is broken into two parts, such that a = n+m where n is an integer. We use pow() to
            compute e :sup:`n` and a Taylor series to compute e :sup:`m` . We return e* :sup:`n` × e :sup:`m`
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): power at which e should be raised
        
            Returns:
                e :sup:`a`
        
        
        """
        ...
    @staticmethod
    def log(dfp: Dfp) -> Dfp:
        """
            Returns the natural logarithm of a. a is first split into three parts such that a = (10000^h)(2^j)k. ln(a) is computed
            by ln(a) = ln(5)*h + ln(2)*(h+j) + ln(k) k is in the range 2/3 < k < 4/3 and is passed on to a series expansion.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which logarithm is requested
        
            Returns:
                log(a)
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def pow(dfp: Dfp, int: int) -> Dfp:
        """
            Raises base to the power a by successive squaring.
        
            Parameters:
                base (:class:`~org.hipparchus.dfp.Dfp`): number to raise
                a (int): power
        
            Returns:
                base :sup:`a`
        
            Computes x to the y power.
        
            Uses the following method:
        
              1.  Set u = rint(y), v = y-u
              2.  Compute a = v * ln(x)
              3.  Compute b = rint( a/ln(2) )
              4.  Compute c = a - b*ln(2)
              5.  x :sup:`y` = x :sup:`u` * 2 :sup:`b` * e :sup:`c`
        
            if |y| > 1e8, then we compute by exp(y*ln(x))
        
            Special Cases
        
              - if y is 0.0 or -0.0 then result is 1.0
              - if y is 1.0 then result is x
              - if y is NaN then result is NaN
              - if x is NaN and y is not zero then result is NaN
              - if |x| > 1.0 and y is +Infinity then result is +Infinity
              - if |x| < 1.0 and y is -Infinity then result is +Infinity
              - if |x| > 1.0 and y is -Infinity then result is +0
              - if |x| < 1.0 and y is +Infinity then result is +0
              - if |x| = 1.0 and y is +/-Infinity then result is NaN
              - if x = +0 and y > 0 then result is +0
              - if x = +Inf and y < 0 then result is +0
              - if x = +0 and y < 0 then result is +Inf
              - if x = +Inf and y > 0 then result is +Inf
              - if x = -0 and y > 0, finite, not odd integer then result is +0
              - if x = -0 and y < 0, finite, and odd integer then result is -Inf
              - if x = -Inf and y > 0, finite, and odd integer then result is -Inf
              - if x = -0 and y < 0, not finite odd integer then result is +Inf
              - if x = -Inf and y > 0, not finite odd integer then result is +Inf
              - if x < 0 and y > 0, finite, and odd integer then result is -(|x| :sup:`y` )
              - if x < 0 and y > 0, finite, and not integer then result is NaN
        
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): base to be raised
                y (:class:`~org.hipparchus.dfp.Dfp`): power to which base should be raised
        
            Returns:
                x :sup:`y`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def pow(dfp: Dfp, dfp2: Dfp) -> Dfp: ...
    @staticmethod
    def sin(dfp: Dfp) -> Dfp:
        """
            computes the sine of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which sine is desired
        
            Returns:
                sin(a)
        
        
        """
        ...
    @staticmethod
    def tan(dfp: Dfp) -> Dfp:
        """
            computes the tangent of the argument.
        
            Parameters:
                a (:class:`~org.hipparchus.dfp.Dfp`): number from which tangent is desired
        
            Returns:
                tan(a)
        
        
        """
        ...

class DfpDec(Dfp):
    """
    public classDfpDec extends :class:`~org.hipparchus.dfp.Dfp`
    
        Subclass of :class:`~org.hipparchus.dfp.Dfp` which hides the radix-10000 artifacts of the superclass. This should give
        outward appearances of being a decimal number with DIGITS*4-3 decimal digits. This class can be subclassed to appear to
        be an arbitrary number of decimal digits less than DIGITS*4-3.
    """
    def __init__(self, dfp: Dfp): ...
    @typing.overload
    def newInstance(self, dfpField: DfpField, roundingMode: DfpField.RoundingMode) -> Dfp:
        """
            Creates an instance with a non-finite value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                sign (byte): sign of the Dfp to create
                nans (byte): code of the value, must be one of :meth:`~org.hipparchus.dfp.Dfp.INFINITE`, :meth:`~org.hipparchus.dfp.Dfp.SNAN`,
                    :meth:`~org.hipparchus.dfp.Dfp.QNAN`
        
            Returns:
                a new instance with a non-finite value
        
        
        """
        ...
    @typing.overload
    def newInstance(self) -> Dfp:
        """
            Create an instance with a value of 0. Use this internally in preference to constructors to facilitate subclasses
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Returns:
                a new instance with a value of 0
        
        """
        ...
    @typing.overload
    def newInstance(self, byte: int) -> Dfp:
        """
            Create an instance from a byte value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (byte): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance from an int value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (int): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance from a long value.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (long): value to convert to an instance
        
            Returns:
                a new instance with value x
        
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
            Create an instance by copying an existing one. Use this internally in preference to constructors to facilitate
            subclasses.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                d (:class:`~org.hipparchus.dfp.Dfp`): instance to copy
        
            Returns:
                a new instance with the same value as d
        
            Create an instance from a String representation. Use this internally in preference to constructors to facilitate
            subclasses.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.newInstance` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                s (:class:`~org.hipparchus.dfp.https:.docs.oracle.com.javase.8.docs.api.java.lang.String`): string representation of the instance
        
            Returns:
                a new instance parsed from specified string
        
        """
        ...
    @typing.overload
    def newInstance(self, byte: int, byte2: int) -> Dfp: ...
    @typing.overload
    def newInstance(self, double: float) -> Dfp: ...
    @typing.overload
    def newInstance(self, int: int) -> Dfp: ...
    @typing.overload
    def newInstance(self, string: str) -> Dfp: ...
    @typing.overload
    def newInstance(self, long: int) -> Dfp: ...
    @typing.overload
    def newInstance(self, dfp: Dfp) -> Dfp: ...
    def nextAfter(self, dfp: Dfp) -> Dfp:
        """
            Returns the next number greater than this one in the direction of x. If this==x then simply returns this.
        
            Overrides:
                :meth:`~org.hipparchus.dfp.Dfp.nextAfter` in class :class:`~org.hipparchus.dfp.Dfp`
        
            Parameters:
                x (:class:`~org.hipparchus.dfp.Dfp`): direction where to look at
        
            Returns:
                closest number next to instance in the direction of x
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.dfp")``.

    Dfp: typing.Type[Dfp]
    DfpDec: typing.Type[DfpDec]
    DfpField: typing.Type[DfpField]
    DfpMath: typing.Type[DfpMath]
