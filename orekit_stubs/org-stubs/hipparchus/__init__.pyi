
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus.analysis
import org.hipparchus.complex
import org.hipparchus.dfp
import org.hipparchus.distribution
import org.hipparchus.exception
import org.hipparchus.filtering
import org.hipparchus.fitting
import org.hipparchus.fraction
import org.hipparchus.geometry
import org.hipparchus.linear
import org.hipparchus.ode
import org.hipparchus.optim
import org.hipparchus.random
import org.hipparchus.special
import org.hipparchus.stat
import org.hipparchus.util
import typing



_Field__T = typing.TypeVar('_Field__T', bound='FieldElement')  # <T>
class Field(typing.Generic[_Field__T]):
    """
    public interfaceField<T extends :class:`~org.hipparchus.FieldElement`<T>>
    
        Interface representing a `field <http://mathworld.wolfram.com/Field.html>`.
    
        Classes implementing this interface will often be singletons.
    
        Also see:
    
              - :class:`~org.hipparchus.FieldElement`
    """
    def getOne(self) -> _Field__T:
        """
            Get the multiplicative identity of the field.
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type[_Field__T]: ...
    def getZero(self) -> _Field__T:
        """
            Get the additive identity of the field.
        
            The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a
            + e :sub:`0` = e :sub:`0` + a = a hold.
        
            Returns:
                additive identity of the field
        
        
        """
        ...

_FieldElement__T = typing.TypeVar('_FieldElement__T', bound='FieldElement')  # <T>
class FieldElement(typing.Generic[_FieldElement__T]):
    """
    public interfaceFieldElement<T extends FieldElement<T>>
    
        Interface representing `field <http://mathworld.wolfram.com/Field.html>` elements.
    
        Also see:
    
              - :class:`~org.hipparchus.Field`
    """
    def add(self, t: _FieldElement__T) -> _FieldElement__T: ...
    def divide(self, t: _FieldElement__T) -> _FieldElement__T: ...
    def getField(self) -> Field[_FieldElement__T]: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Returns:
                real value
        
        
        """
        ...
    def isZero(self) -> bool:
        """
            Check if an element is semantically equal to zero.
        
            The default implementation simply calls :code:`equals(getField().getZero())`. However, this may need to be overridden in
            some cases as due to compatibility with :code:`hashCode()` some classes implements :code:`equals(Object)` in such a way
            that -0.0 and +0.0 are different, which may be a problem. It prevents for example identifying a diagonal element is zero
            and should be avoided when doing partial pivoting in LU decomposition.
        
            Returns:
                true if the element is semantically equal to zero
        
            Since:
                1.8
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> _FieldElement__T:
        """
            Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} =
            \sum_{i=1}^n \mathrm{this} \]
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
        :class:`~org.hipparchus.FieldElement` multiply(:class:`~org.hipparchus.FieldElement` a) throws :class:`~org.hipparchus.exception.NullArgumentException`
        
            Compute this × a.
        
            Parameters:
                a (:class:`~org.hipparchus.FieldElement`): element to multiply
        
            Returns:
                a new element representing this × a
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if :code:`a` is :code:`null`.
        
        
        """
        ...
    @typing.overload
    def multiply(self, t: _FieldElement__T) -> _FieldElement__T: ...
    def negate(self) -> _FieldElement__T:
        """
            Returns the additive inverse of :code:`this` element.
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def reciprocal(self) -> _FieldElement__T: ...
    def subtract(self, t: _FieldElement__T) -> _FieldElement__T: ...

_CalculusFieldElement__T = typing.TypeVar('_CalculusFieldElement__T', bound=FieldElement)  # <T>
class CalculusFieldElement(FieldElement[_CalculusFieldElement__T], typing.Generic[_CalculusFieldElement__T]):
    """
    public interfaceCalculusFieldElement<T extends :class:`~org.hipparchus.FieldElement`<T>>extends :class:`~org.hipparchus.FieldElement`<T>
    
        Interface representing a `field <http://mathworld.wolfram.com/Field.html>` with calculus capabilities (sin, cos, ...).
    
        Since:
            1.7
    
        Also see:
    
              - :class:`~org.hipparchus.FieldElement`
    """
    def abs(self) -> _CalculusFieldElement__T:
        """
            absolute value.
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> _CalculusFieldElement__T:
        """
            Arc cosine operation.
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> _CalculusFieldElement__T:
        """
            Inverse hyperbolic cosine operation.
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T:
        """
            '+' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> _CalculusFieldElement__T: ...
    def asin(self) -> _CalculusFieldElement__T:
        """
            Arc sine operation.
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> _CalculusFieldElement__T:
        """
            Inverse hyperbolic sine operation.
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> _CalculusFieldElement__T:
        """
            Arc tangent operation.
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T:
        """
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders are inconsistent
        
        
        """
        ...
    def atanh(self) -> _CalculusFieldElement__T:
        """
            Inverse hyperbolic tangent operation.
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def cbrt(self) -> _CalculusFieldElement__T:
        """
            Cubic root.
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> _CalculusFieldElement__T:
        """
            Get the smallest whole number larger than instance.
        
            Returns:
                ceil(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T:
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                sign (:class:`~org.hipparchus.CalculusFieldElement`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                sign (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> _CalculusFieldElement__T: ...
    def cos(self) -> _CalculusFieldElement__T:
        """
            Cosine operation.
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> _CalculusFieldElement__T:
        """
            Hyperbolic cosine operation.
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> _CalculusFieldElement__T:
        """
            '÷' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
            Compute this ÷ a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.CalculusFieldElement`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    def exp(self) -> _CalculusFieldElement__T:
        """
            Exponential.
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> _CalculusFieldElement__T:
        """
            Exponential minus 1.
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> _CalculusFieldElement__T:
        """
            Get the largest whole number smaller than instance.
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getAddendum(self) -> _CalculusFieldElement__T:
        """
            Get the addendum to the real value of the number.
        
            The addendum is considered to be the part that when added back to the :meth:`~org.hipparchus.FieldElement.getReal`
            recovers the instance. This means that when :code:`e.getReal()` is finite (i.e. neither infinite nor NaN), then
            :code:`e.getAddendum().add(e.getReal())` is :code:`e` and :code:`e.subtract(e.getReal())` is :code:`e.getAddendum()`.
            Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always
            holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives
            types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the
            subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
            Returns:
                real value
        
            Since:
                4.0
        
        
        """
        ...
    def getExponent(self) -> int:
        """
            Return the exponent of the instance, removing the bias.
        
            For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
            Returns:
                exponent for the instance, without bias
        
        
        """
        ...
    def getPi(self) -> _CalculusFieldElement__T:
        """
            Get the Archimedes constant π.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Returns:
                Archimedes constant π
        
            Since:
                2.0
        
        
        """
        ...
    def hypot(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    def isFinite(self) -> bool:
        """
            Check if the instance is finite (neither infinite nor NaN).
        
            Returns:
                true if the instance is finite (neither infinite nor NaN)
        
            Since:
                2.0
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Check if the instance is infinite.
        
            Returns:
                true if the instance is infinite
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check if the instance is Not a Number.
        
            Returns:
                true if the instance is Not a Number
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, t: _CalculusFieldElement__T, t2: _CalculusFieldElement__T, t3: _CalculusFieldElement__T, t4: _CalculusFieldElement__T) -> _CalculusFieldElement__T:
        """
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the first term
                b1 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the first term
                a2 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the second term
                b2 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the first term
                b1 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the first term
                a2 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the second term
                b2 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the second term
                a3 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the third term
                b3 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the first term
                b1 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the first term
                a2 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the second term
                b2 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the second term
                a3 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the third term
                b3 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the third term
                a4 (:class:`~org.hipparchus.CalculusFieldElement`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.CalculusFieldElement`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
        
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
                  - :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, t: _CalculusFieldElement__T, t2: _CalculusFieldElement__T, t3: _CalculusFieldElement__T, t4: _CalculusFieldElement__T, t5: _CalculusFieldElement__T, t6: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    @typing.overload
    def linearCombination(self, t: _CalculusFieldElement__T, t2: _CalculusFieldElement__T, t3: _CalculusFieldElement__T, t4: _CalculusFieldElement__T, t5: _CalculusFieldElement__T, t6: _CalculusFieldElement__T, t7: _CalculusFieldElement__T, t8: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    @typing.overload
    def linearCombination(self, tArray: typing.Union[typing.List[_CalculusFieldElement__T], jpype.JArray], tArray2: typing.Union[typing.List[_CalculusFieldElement__T], jpype.JArray]) -> _CalculusFieldElement__T: ...
    @typing.overload
    def linearCombination(self, double: float, t: _CalculusFieldElement__T, double2: float, t2: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    @typing.overload
    def linearCombination(self, double: float, t: _CalculusFieldElement__T, double2: float, t2: _CalculusFieldElement__T, double3: float, t3: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    @typing.overload
    def linearCombination(self, double: float, t: _CalculusFieldElement__T, double2: float, t2: _CalculusFieldElement__T, double3: float, t3: _CalculusFieldElement__T, double4: float, t4: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], tArray: typing.Union[typing.List[_CalculusFieldElement__T], jpype.JArray]) -> _CalculusFieldElement__T: ...
    def log(self) -> _CalculusFieldElement__T:
        """
            Natural logarithm.
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> _CalculusFieldElement__T:
        """
            Base 10 logarithm.
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> _CalculusFieldElement__T:
        """
            Shifted natural logarithm.
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T:
        """
            '×' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this×a
        
            Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} =
            \sum_{i=1}^n \mathrm{this} \]
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> _CalculusFieldElement__T: ...
    @typing.overload
    def multiply(self, int: int) -> _CalculusFieldElement__T: ...
    def newInstance(self, double: float) -> _CalculusFieldElement__T:
        """
            Create an instance corresponding to a constant real value.
        
            Parameters:
                value (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    def norm(self) -> float:
        """
            norm.
        
            Returns:
                norm(this)
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    def pow(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T:
        """
            Power operation.
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
            Integer power operation.
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
        :class:`~org.hipparchus.CalculusFieldElement` pow(:class:`~org.hipparchus.CalculusFieldElement` e) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Power operation.
        
            Parameters:
                e (:class:`~org.hipparchus.CalculusFieldElement`): exponent
        
            Returns:
                this :sup:`e`
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders are inconsistent
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> _CalculusFieldElement__T: ...
    @typing.overload
    def pow(self, int: int) -> _CalculusFieldElement__T: ...
    @typing.overload
    def remainder(self, double: float) -> _CalculusFieldElement__T:
        """
            IEEE remainder operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Parameters:
                a (:class:`~org.hipparchus.CalculusFieldElement`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    def rint(self) -> _CalculusFieldElement__T:
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> _CalculusFieldElement__T:
        """
            N :sup:`th` root.
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
        
        """
        ...
    def round(self) -> int:
        """
            Get the closest long to instance real value.
        
            Returns:
                closest long to :meth:`~org.hipparchus.FieldElement.getReal`
        
        
        """
        ...
    def scalb(self, int: int) -> _CalculusFieldElement__T:
        """
            Multiply the instance by a power of 2.
        
            Parameters:
                n (int): power of 2
        
            Returns:
                this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> _CalculusFieldElement__T:
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> _CalculusFieldElement__T:
        """
            Sine operation.
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos[_CalculusFieldElement__T]: ...
    def sinh(self) -> _CalculusFieldElement__T:
        """
            Hyperbolic sine operation.
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh[_CalculusFieldElement__T]: ...
    def sqrt(self) -> _CalculusFieldElement__T:
        """
            Square root.
        
            Returns:
                square root of the instance
        
        
        """
        ...
    def square(self) -> _CalculusFieldElement__T:
        """
            Compute this × this.
        
            Returns:
                a new element representing this × this
        
            Since:
                3.1
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> _CalculusFieldElement__T:
        """
            '-' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
            Compute this - a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.CalculusFieldElement`): element to subtract
        
            Returns:
                a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, t: _CalculusFieldElement__T) -> _CalculusFieldElement__T: ...
    def tan(self) -> _CalculusFieldElement__T:
        """
            Tangent operation.
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> _CalculusFieldElement__T:
        """
            Hyperbolic tangent operation.
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def toDegrees(self) -> _CalculusFieldElement__T:
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> _CalculusFieldElement__T:
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def ulp(self) -> _CalculusFieldElement__T:
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            Returns:
                ulp(this)
        
            Since:
                2.0
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus")``.

    CalculusFieldElement: typing.Type[CalculusFieldElement]
    Field: typing.Type[Field]
    FieldElement: typing.Type[FieldElement]
    analysis: org.hipparchus.analysis.__module_protocol__
    complex: org.hipparchus.complex.__module_protocol__
    dfp: org.hipparchus.dfp.__module_protocol__
    distribution: org.hipparchus.distribution.__module_protocol__
    exception: org.hipparchus.exception.__module_protocol__
    filtering: org.hipparchus.filtering.__module_protocol__
    fitting: org.hipparchus.fitting.__module_protocol__
    fraction: org.hipparchus.fraction.__module_protocol__
    geometry: org.hipparchus.geometry.__module_protocol__
    linear: org.hipparchus.linear.__module_protocol__
    ode: org.hipparchus.ode.__module_protocol__
    optim: org.hipparchus.optim.__module_protocol__
    random: org.hipparchus.random.__module_protocol__
    special: org.hipparchus.special.__module_protocol__
    stat: org.hipparchus.stat.__module_protocol__
    util: org.hipparchus.util.__module_protocol__
