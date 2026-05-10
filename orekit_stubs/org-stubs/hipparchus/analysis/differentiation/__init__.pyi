
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.linear
import org.hipparchus.util
import typing



class DSCompiler:
    """
    Class holding "compiled" computation rules for derivative structures.
    
    This class implements the computation rules described in Dan Kalman's paper `Doubly Recursive Multivariate Automatic Differentiation <http://www1.american.edu/cas/mathstat/People/kalman/pdffiles/mmgautodiff.pdf>`, Mathematics Magazine, vol. 75, no. 3, June 2002. However, in order to avoid performances bottlenecks, the recursive rules are "compiled" once in an unfold form. This class does this recursion unrolling and stores the computation rules as simple loops with pre-computed indirection arrays.
    
    This class maps all derivative computation into single dimension arrays that hold the value and partial derivatives. The class does not hold these arrays, which remains under the responsibility of the caller. For each combination of number of free parameters and derivation order, only one compiler is necessary, and this compiler will be used to perform computations on all arrays provided to it, which can represent hundreds or thousands of different parameters kept together with all their partial derivatives.
    
    The arrays on which compilers operate contain only the partial derivatives together with the 0 :sup:`th` derivative, i.e. the value. The partial derivatives are stored in a compiler-specific order, which can be retrieved using methods getPartialDerivativeIndex and getPartialDerivativeOrders. The value is guaranteed to be stored as the first element (i.e. the getPartialDerivativeIndex method returns 0 when called with 0 for all derivation orders and getPartialDerivativeOrders returns an array filled with 0 when called with 0 as the index).
    
    Note that the ordering changes with number of parameters and derivation order. For example given 2 parameters x and y, df/dy is stored at index 2 when derivation order is set to 1 (in this case the array has three elements: f, df/dx and df/dy). If derivation order is set to 2, then df/dy will be stored at index 3 (in this case the array has six elements: f, df/dx, d²f/dxdx, df/dy, d²f/dxdy and d²f/dydy).
    
    Given this structure, users can perform some simple operations like adding, subtracting or multiplying constants and negating the elements by themselves, knowing if they want to mutate their array or create a new array. These simple operations are not provided by the compiler. The compiler provides only the more complex operations between several arrays.
    
    This class is mainly used as the engine for scalar variable DerivativeStructure. It can also be used directly to hold several variables in arrays for more complex data structures. User can for example store a vector of n variables depending on three x, y and z free parameters in one array as follows:
    
    
       // parameter 0 is x, parameter 1 is y, parameter 2 is z
       int parameters = 3;
       DSCompiler compiler = DSCompiler.getCompiler(parameters, order);
       int size = compiler.getSize();
    
       // pack all elements in a single array
       double[] array = new double[n * size];
       for (int i = 0; i < n; ++i) {
    
         // we know value is guaranteed to be the first element
         array[i * size] = v[i];
    
         // we don't know where first derivatives are stored, so we ask the compiler
         array[i * size + compiler.getPartialDerivativeIndex(1, 0, 0) = dvOnDx[i][0];
         array[i * size + compiler.getPartialDerivativeIndex(0, 1, 0) = dvOnDy[i][0];
         array[i * size + compiler.getPartialDerivativeIndex(0, 0, 1) = dvOnDz[i][0];
    
         // we let all higher order derivatives set to 0
    
       }
     
    
    Then in another function, user can perform some operations on all elements stored in the single array, such as a simple product of all variables:
    
    
       // compute the product of all elements
       double[] product = new double[size];
       prod[0] = 1.0;
       for (int i = 0; i < n; ++i) {
         double[] tmp = product.clone();
         compiler.multiply(tmp, 0, array, i * size, product, 0);
       }
    
       // value
       double p = product[0];
    
       // first derivatives
       double dPdX = product[compiler.getPartialDerivativeIndex(1, 0, 0)];
       double dPdY = product[compiler.getPartialDerivativeIndex(0, 1, 0)];
       double dPdZ = product[compiler.getPartialDerivativeIndex(0, 0, 1)];
    
       // cross derivatives (assuming order was at least 2)
       double dPdXdX = product[compiler.getPartialDerivativeIndex(2, 0, 0)];
       double dPdXdY = product[compiler.getPartialDerivativeIndex(1, 1, 0)];
       double dPdXdZ = product[compiler.getPartialDerivativeIndex(1, 0, 1)];
       double dPdYdY = product[compiler.getPartialDerivativeIndex(0, 2, 0)];
       double dPdYdZ = product[compiler.getPartialDerivativeIndex(0, 1, 1)];
       double dPdZdZ = product[compiler.getPartialDerivativeIndex(0, 0, 2)];
     
    
    Also see:
        DerivativeStructure,
        FieldDerivativeStructure
    """
    _acos_1__T = typing.TypeVar('_acos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acos(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute arc cosine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for arc cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def acos(self, operand: typing.Union[typing.List[_acos_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_acos_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute arc cosine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for arc cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _acosh_1__T = typing.TypeVar('_acosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acosh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute inverse hyperbolic cosine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for inverse hyperbolic cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def acosh(self, operand: typing.Union[typing.List[_acosh_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_acosh_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute inverse hyperbolic cosine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for inverse hyperbolic cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _add_1__T = typing.TypeVar('_add_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def add(self, lhs: typing.Union[typing.List[float], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[float], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Perform addition of two derivative structures.
        
        Parameters:
            lhs (double[]): array holding left hand side of addition
            lhsOffset (int): offset of the left hand side in its array
            rhs (double[]): array right hand side of addition
            rhsOffset (int): offset of the right hand side in its array
            result (double[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def add(self, lhs: typing.Union[typing.List[_add_1__T], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[_add_1__T], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[_add_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Perform addition of two derivative structures.
        
        Parameters:
            lhs (T[]): array holding left hand side of addition
            lhsOffset (int): offset of the left hand side in its array
            rhs (T[]): array right hand side of addition
            rhsOffset (int): offset of the right hand side in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _asin_1__T = typing.TypeVar('_asin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def asin(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute arc sine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for arc sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def asin(self, operand: typing.Union[typing.List[_asin_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_asin_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute arc sine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for arc sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _asinh_1__T = typing.TypeVar('_asinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def asinh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute inverse hyperbolic sine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for inverse hyperbolic sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def asinh(self, operand: typing.Union[typing.List[_asinh_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_asinh_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute inverse hyperbolic sine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for inverse hyperbolic sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _atan_1__T = typing.TypeVar('_atan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atan(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute arc tangent of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for arc tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def atan(self, operand: typing.Union[typing.List[_atan_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_atan_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute arc tangent of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for arc tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _atan2_1__T = typing.TypeVar('_atan2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atan2(self, y: typing.Union[typing.List[float], jpype.JArray], yOffset: int, x: typing.Union[typing.List[float], jpype.JArray], xOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute two arguments arc tangent of a derivative structure.
        
        Parameters:
            y (double[]): array holding the first operand
            yOffset (int): offset of the first operand in its array
            x (double[]): array holding the second operand
            xOffset (int): offset of the second operand in its array
            result (double[]): array where result must be stored (for two arguments arc tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def atan2(self, y: typing.Union[typing.List[_atan2_1__T], jpype.JArray], yOffset: int, x: typing.Union[typing.List[_atan2_1__T], jpype.JArray], xOffset: int, result: typing.Union[typing.List[_atan2_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute two arguments arc tangent of a derivative structure.
        
        Parameters:
            y (T[]): array holding the first operand
            yOffset (int): offset of the first operand in its array
            x (T[]): array holding the second operand
            xOffset (int): offset of the second operand in its array
            result (T[]): array where result must be stored (for two arguments arc tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _atanh_1__T = typing.TypeVar('_atanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atanh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute inverse hyperbolic tangent of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for inverse hyperbolic tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def atanh(self, operand: typing.Union[typing.List[_atanh_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_atanh_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute inverse hyperbolic tangent of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for inverse hyperbolic tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    def checkCompatibility(self, compiler: 'DSCompiler') -> None:
        """
        Check rules set compatibility.
        
        Parameters:
            compiler (DSCompiler): other compiler to check against instance
        
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders are inconsistent
        
        
        """
        ...
    _compose_1__T = typing.TypeVar('_compose_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compose_2__T = typing.TypeVar('_compose_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compose(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, f: typing.Union[typing.List[float], jpype.JArray], result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute composition of a derivative structure by a function.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            f (double[]): array of value and derivatives of the function at the current point (i.e. at operand[operandOffset]).
            result (double[]): array where result must be stored (for composition the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def compose(self, operand: typing.Union[typing.List[_compose_1__T], jpype.JArray], operandOffset: int, f: typing.Union[typing.List[float], jpype.JArray], result: typing.Union[typing.List[_compose_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute composition of a derivative structure by a function.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            f (T[]): array of value and derivatives of the function at the current point (i.e. at operand[operandOffset]).
            result (T[]): array where result must be stored (for composition the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute composition of a derivative structure by a function.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            f (double[]): array of value and derivatives of the function at the current point (i.e. at operand[operandOffset]).
            result (T[]): array where result must be stored (for composition the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @typing.overload
    def compose(self, operand: typing.Union[typing.List[_compose_2__T], jpype.JArray], operandOffset: int, f: typing.Union[typing.List[_compose_2__T], jpype.JArray], result: typing.Union[typing.List[_compose_2__T], jpype.JArray], resultOffset: int) -> None: ...
    _cos_1__T = typing.TypeVar('_cos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def cos(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute cosine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def cos(self, operand: typing.Union[typing.List[_cos_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_cos_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute cosine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _cosh_1__T = typing.TypeVar('_cosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def cosh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute hyperbolic cosine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for hyperbolic cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def cosh(self, operand: typing.Union[typing.List[_cosh_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_cosh_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute hyperbolic cosine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for hyperbolic cosine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _divide_1__T = typing.TypeVar('_divide_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def divide(self, lhs: typing.Union[typing.List[float], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[float], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Perform division of two derivative structures. Based on the multiplication operator.
        
        Parameters:
            lhs (double[]): array holding left hand side of division
            lhsOffset (int): offset of the left hand side in its array
            rhs (double[]): array right hand side of division
            rhsOffset (int): offset of the right hand side in its array
            result (double[]): array where result must be stored (for division the result array cannot be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def divide(self, lhs: typing.Union[typing.List[_divide_1__T], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[_divide_1__T], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[_divide_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Perform division of two derivative structures. Based on the multiplication operator.
        
        Parameters:
            lhs (T[]): array holding left hand side of division
            lhsOffset (int): offset of the left hand side in its array
            rhs (T[]): array right hand side of division
            rhsOffset (int): offset of the right hand side in its array
            result (T[]): array where result must be stored (for division the result array cannot be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _exp_1__T = typing.TypeVar('_exp_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def exp(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute exponential of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for exponential the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def exp(self, operand: typing.Union[typing.List[_exp_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_exp_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute exponential of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for exponential the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _expm1_1__T = typing.TypeVar('_expm1_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def expm1(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for exponential the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def expm1(self, operand: typing.Union[typing.List[_expm1_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_expm1_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for exponential the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @staticmethod
    def getCompiler(parameters: int, order: int) -> 'DSCompiler':
        """
        Get the compiler for number of free parameters and order.
        
        Parameters:
            parameters (int): number of free parameters
            order (int): derivation order
        
        Returns:
            cached rules set
        
        Raises:
            MathIllegalArgumentException: if order is too large
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the derivation order.
        
        Returns:
            derivation order
        
        
        """
        ...
    def getPartialDerivativeIndex(self, *orders: int) -> int:
        """
        Get the index of a partial derivative in the array.
        
        If all orders are set to 0, then the 0 :sup:`th` order derivative is returned, which is the value of the function.
        
        The indices of derivatives are between 0 and getSize - 1. Their specific order is fixed for a given compiler, but otherwise not publicly specified. There are however some simple cases which have guaranteed indices:
        
          - the index of 0 :sup:`th` order derivative is always 0
          - if there is only 1 getFreeParameters, then the derivatives
            are sorted in increasing derivation order (i.e. f at index 0, df/dp at index 1, d :sup:`2` f/dp :sup:`2` at index 2 ...
            d :sup:`k` f/dp :sup:`k` at index k),
          - if the getOrder is 1, then the derivatives are sorted in
            increasing free parameter order (i.e. f at index 0, df/dx :sub:`1` at index 1, df/dx :sub:`2` at index 2 ... df/dx
            :sub:`k` at index k),
          - all other cases are not publicly specified
        
        This method is the inverse of method getPartialDerivativeOrders
        
        Parameters:
            orders (int...): derivation orders with respect to each parameter
        
        Returns:
            index of the partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of parameters does not match the instance
            MathIllegalArgumentException: if sum of derivation orders is larger than the instance limits
        
        Also see:
            getPartialDerivativeOrders
        
        
        """
        ...
    def getPartialDerivativeOrders(self, index: int) -> typing.MutableSequence[int]:
        """
        Get the derivation orders for a specific index in the array.
        
        This method is the inverse of getPartialDerivativeIndex.
        
        Parameters:
            index (int): of the partial derivative
        
        Returns:
            derivation orders with respect to each parameter
        
        Also see:
            getPartialDerivativeIndex
        
        
        """
        ...
    def getPartialDerivativeOrdersSum(self, index: int) -> int:
        """
        Get the sum of derivation orders for a specific index in the array.
        
        This method return the sum of the elements returned by getPartialDerivativeIndex, using precomputed values
        
        Parameters:
            index (int): of the partial derivative
        
        Returns:
            sum of derivation orders with respect to each parameter
        
        Since:
            2.2
        
        Also see:
            getPartialDerivativeIndex
        
        
        """
        ...
    def getSize(self) -> int:
        """
        Get the array size required for holding partial derivatives data.
        
        This number includes the single 0 order derivative element, which is guaranteed to be stored in the first element of the array.
        
        Returns:
            array size required for holding partial derivatives data
        
        
        """
        ...
    _linearCombination_3__T = typing.TypeVar('_linearCombination_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _linearCombination_4__T = typing.TypeVar('_linearCombination_4__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _linearCombination_5__T = typing.TypeVar('_linearCombination_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _linearCombination_6__T = typing.TypeVar('_linearCombination_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _linearCombination_7__T = typing.TypeVar('_linearCombination_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _linearCombination_8__T = typing.TypeVar('_linearCombination_8__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def linearCombination(self, a1: float, c1: typing.Union[typing.List[float], jpype.JArray], offset1: int, a2: float, c2: typing.Union[typing.List[float], jpype.JArray], offset2: int, a3: float, c3: typing.Union[typing.List[float], jpype.JArray], offset3: int, a4: float, c4: typing.Union[typing.List[float], jpype.JArray], offset4: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2 + a3 * ds3 + a4 * ds4
        
        Parameters:
            a1 (double): first scale factor
            c1 (double[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (double): second scale factor
            c2 (double[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            a3 (double): third scale factor
            c3 (double[]): third base (unscaled) component
            offset3 (int): offset of third operand in its array
            a4 (double): fourth scale factor
            c4 (double[]): fourth base (unscaled) component
            offset4 (int): offset of fourth operand in its array
            result (double[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, c1: typing.Union[typing.List[float], jpype.JArray], offset1: int, a2: float, c2: typing.Union[typing.List[float], jpype.JArray], offset2: int, a3: float, c3: typing.Union[typing.List[float], jpype.JArray], offset3: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2 + a3 * ds3 + a4 * ds4
        
        Parameters:
            a1 (double): first scale factor
            c1 (double[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (double): second scale factor
            c2 (double[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            a3 (double): third scale factor
            c3 (double[]): third base (unscaled) component
            offset3 (int): offset of third operand in its array
            result (double[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, c1: typing.Union[typing.List[float], jpype.JArray], offset1: int, a2: float, c2: typing.Union[typing.List[float], jpype.JArray], offset2: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2
        
        Parameters:
            a1 (double): first scale factor
            c1 (double[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (double): second scale factor
            c2 (double[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            result (double[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, c1: typing.Union[typing.List[_linearCombination_3__T], jpype.JArray], offset1: int, a2: float, c2: typing.Union[typing.List[_linearCombination_3__T], jpype.JArray], offset2: int, a3: float, c3: typing.Union[typing.List[_linearCombination_3__T], jpype.JArray], offset3: int, a4: float, c4: typing.Union[typing.List[_linearCombination_3__T], jpype.JArray], offset4: int, result: typing.Union[typing.List[_linearCombination_3__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2 + a3 * ds3 + a4 * ds4
        
        Parameters:
            a1 (T): first scale factor
            c1 (T[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (T): second scale factor
            c2 (T[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            a3 (T): third scale factor
            c3 (T[]): third base (unscaled) component
            offset3 (int): offset of third operand in its array
            a4 (T): fourth scale factor
            c4 (T[]): fourth base (unscaled) component
            offset4 (int): offset of fourth operand in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2 + a3 * ds3 + a4 * ds4
        
        Parameters:
            a1 (double): first scale factor
            c1 (T[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (double): second scale factor
            c2 (T[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            a3 (double): third scale factor
            c3 (T[]): third base (unscaled) component
            offset3 (int): offset of third operand in its array
            a4 (double): fourth scale factor
            c4 (T[]): fourth base (unscaled) component
            offset4 (int): offset of fourth operand in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, c1: typing.Union[typing.List[_linearCombination_4__T], jpype.JArray], offset1: int, a2: float, c2: typing.Union[typing.List[_linearCombination_4__T], jpype.JArray], offset2: int, a3: float, c3: typing.Union[typing.List[_linearCombination_4__T], jpype.JArray], offset3: int, result: typing.Union[typing.List[_linearCombination_4__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2 + a3 * ds3 + a4 * ds4
        
        Parameters:
            a1 (T): first scale factor
            c1 (T[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (T): second scale factor
            c2 (T[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            a3 (T): third scale factor
            c3 (T[]): third base (unscaled) component
            offset3 (int): offset of third operand in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2 + a3 * ds3 + a4 * ds4
        
        Parameters:
            a1 (double): first scale factor
            c1 (T[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (double): second scale factor
            c2 (T[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            a3 (double): third scale factor
            c3 (T[]): third base (unscaled) component
            offset3 (int): offset of third operand in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, c1: typing.Union[typing.List[_linearCombination_5__T], jpype.JArray], offset1: int, a2: float, c2: typing.Union[typing.List[_linearCombination_5__T], jpype.JArray], offset2: int, result: typing.Union[typing.List[_linearCombination_5__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2
        
        Parameters:
            a1 (T): first scale factor
            c1 (T[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (T): second scale factor
            c2 (T[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        Compute linear combination. The derivative structure built will be a1 * ds1 + a2 * ds2
        
        Parameters:
            a1 (double): first scale factor
            c1 (T[]): first base (unscaled) component
            offset1 (int): offset of first operand in its array
            a2 (double): second scale factor
            c2 (T[]): second base (unscaled) component
            offset2 (int): offset of second operand in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: _linearCombination_6__T, c1: typing.Union[typing.List[_linearCombination_6__T], jpype.JArray], offset1: int, a2: _linearCombination_6__T, c2: typing.Union[typing.List[_linearCombination_6__T], jpype.JArray], offset2: int, a3: _linearCombination_6__T, c3: typing.Union[typing.List[_linearCombination_6__T], jpype.JArray], offset3: int, a4: _linearCombination_6__T, c4: typing.Union[typing.List[_linearCombination_6__T], jpype.JArray], offset4: int, result: typing.Union[typing.List[_linearCombination_6__T], jpype.JArray], resultOffset: int) -> None: ...
    @typing.overload
    def linearCombination(self, a1: _linearCombination_7__T, c1: typing.Union[typing.List[_linearCombination_7__T], jpype.JArray], offset1: int, a2: _linearCombination_7__T, c2: typing.Union[typing.List[_linearCombination_7__T], jpype.JArray], offset2: int, a3: _linearCombination_7__T, c3: typing.Union[typing.List[_linearCombination_7__T], jpype.JArray], offset3: int, result: typing.Union[typing.List[_linearCombination_7__T], jpype.JArray], resultOffset: int) -> None: ...
    @typing.overload
    def linearCombination(self, a1: _linearCombination_8__T, c1: typing.Union[typing.List[_linearCombination_8__T], jpype.JArray], offset1: int, a2: _linearCombination_8__T, c2: typing.Union[typing.List[_linearCombination_8__T], jpype.JArray], offset2: int, result: typing.Union[typing.List[_linearCombination_8__T], jpype.JArray], resultOffset: int) -> None: ...
    _log_1__T = typing.TypeVar('_log_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def log(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute natural logarithm of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for logarithm the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def log(self, operand: typing.Union[typing.List[_log_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_log_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute natural logarithm of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for logarithm the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _log10_1__T = typing.TypeVar('_log10_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def log10(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Computes base 10 logarithm of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for base 10 logarithm the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def log10(self, operand: typing.Union[typing.List[_log10_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_log10_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Computes base 10 logarithm of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for base 10 logarithm the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _log1p_1__T = typing.TypeVar('_log1p_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def log1p(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Computes shifted logarithm of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for shifted logarithm the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def log1p(self, operand: typing.Union[typing.List[_log1p_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_log1p_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Computes shifted logarithm of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for shifted logarithm the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _multiply_1__T = typing.TypeVar('_multiply_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def multiply(self, lhs: typing.Union[typing.List[float], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[float], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Perform multiplication of two derivative structures.
        
        Parameters:
            lhs (double[]): array holding left hand side of multiplication
            lhsOffset (int): offset of the left hand side in its array
            rhs (double[]): array right hand side of multiplication
            rhsOffset (int): offset of the right hand side in its array
            result (double[]): array where result must be stored (for multiplication the result array cannot be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def multiply(self, lhs: typing.Union[typing.List[_multiply_1__T], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[_multiply_1__T], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[_multiply_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Perform multiplication of two derivative structures.
        
        Parameters:
            lhs (T[]): array holding left hand side of multiplication
            lhsOffset (int): offset of the left hand side in its array
            rhs (T[]): array right hand side of multiplication
            rhsOffset (int): offset of the right hand side in its array
            result (T[]): array where result must be stored (for multiplication the result array cannot be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _pow_1__T = typing.TypeVar('_pow_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_5__T = typing.TypeVar('_pow_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_6__T = typing.TypeVar('_pow_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_7__T = typing.TypeVar('_pow_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, a: float, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute power of a double to a derivative structure.
        
        Parameters:
            a (double): number to exponentiate
            operand (double[]): array holding the power
            operandOffset (int): offset of the power in its array
            result (double[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute power of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            p (double): power to apply
            result (double[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute integer power of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            n (int): power to apply
            result (double[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute power of a derivative structure.
        
        Parameters:
            x (double[]): array holding the base
            xOffset (int): offset of the base in its array
            y (double[]): array holding the exponent
            yOffset (int): offset of the exponent in its array
            result (double[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def pow(self, a: float, operand: typing.Union[typing.List[_pow_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_pow_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute power of a double to a derivative structure.
        
        Parameters:
            a (double): number to exponentiate
            operand (T[]): array holding the power
            operandOffset (int): offset of the power in its array
            result (T[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute power of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            p (double): power to apply
            result (T[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute integer power of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            n (int): power to apply
            result (T[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        Compute power of a derivative structure.
        
        Parameters:
            x (T[]): array holding the base
            xOffset (int): offset of the base in its array
            y (T[]): array holding the exponent
            yOffset (int): offset of the exponent in its array
            result (T[]): array where result must be stored (for power the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @typing.overload
    def pow(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, double2: float, doubleArray2: typing.Union[typing.List[float], jpype.JArray], int2: int) -> None: ...
    @typing.overload
    def pow(self, x: typing.Union[typing.List[float], jpype.JArray], xOffset: int, y: typing.Union[typing.List[float], jpype.JArray], yOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None: ...
    @typing.overload
    def pow(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int, doubleArray2: typing.Union[typing.List[float], jpype.JArray], int3: int) -> None: ...
    @typing.overload
    def pow(self, tArray: typing.Union[typing.List[_pow_5__T], jpype.JArray], int: int, double: float, tArray2: typing.Union[typing.List[_pow_5__T], jpype.JArray], int2: int) -> None: ...
    @typing.overload
    def pow(self, tArray: typing.Union[typing.List[_pow_6__T], jpype.JArray], int: int, int2: int, tArray2: typing.Union[typing.List[_pow_6__T], jpype.JArray], int3: int) -> None: ...
    @typing.overload
    def pow(self, x: typing.Union[typing.List[_pow_7__T], jpype.JArray], xOffset: int, y: typing.Union[typing.List[_pow_7__T], jpype.JArray], yOffset: int, result: typing.Union[typing.List[_pow_7__T], jpype.JArray], resultOffset: int) -> None: ...
    _rebase_1__T = typing.TypeVar('_rebase_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rebase(self, ds: typing.Union[typing.List[float], jpype.JArray], dsOffset: int, baseCompiler: 'DSCompiler', p: typing.Union[typing.List[float], jpype.JArray], result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Rebase derivative structure with respect to low level parameter functions.
        
        Parameters:
            ds (double[]): array holding the derivative structure
            dsOffset (int): offset of the derivative structure in its array
            baseCompiler (DSCompiler): compiler associated with the low level parameter functions
            p (double[]): array holding the low level parameter functions (one flat array)
            result (double[]): array where result must be stored (for composition the result array cannot be the input
            resultOffset (int): offset of the result in its array
        
        Since:
            2.2
        
        """
        ...
    @typing.overload
    def rebase(self, ds: typing.Union[typing.List[_rebase_1__T], jpype.JArray], dsOffset: int, baseCompiler: 'DSCompiler', p: typing.Union[typing.List[_rebase_1__T], jpype.JArray], result: typing.Union[typing.List[_rebase_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Rebase derivative structure with respect to low level parameter functions.
        
        Parameters:
            ds (T[]): array holding the derivative structure
            dsOffset (int): offset of the derivative structure in its array
            baseCompiler (DSCompiler): compiler associated with the low level parameter functions
            p (T[]): array holding the low level parameter functions (one flat array)
            result (T[]): array where result must be stored (for composition the result array cannot be the input
            resultOffset (int): offset of the result in its array
        
        Since:
            2.2
        
        
        """
        ...
    _reciprocal_1__T = typing.TypeVar('_reciprocal_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def reciprocal(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute reciprocal of derivative structure. Based on the multiplication operator.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def reciprocal(self, operand: typing.Union[typing.List[_reciprocal_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_reciprocal_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute reciprocal of derivative structure. Based on the multiplication operator.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _remainder_1__T = typing.TypeVar('_remainder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def remainder(self, lhs: typing.Union[typing.List[float], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[float], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Perform remainder of two derivative structures.
        
        Parameters:
            lhs (double[]): array holding left hand side of remainder
            lhsOffset (int): offset of the left hand side in its array
            rhs (double[]): array right hand side of remainder
            rhsOffset (int): offset of the right hand side in its array
            result (double[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def remainder(self, lhs: typing.Union[typing.List[_remainder_1__T], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[_remainder_1__T], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[_remainder_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Perform remainder of two derivative structures.
        
        Parameters:
            lhs (T[]): array holding left hand side of remainder
            lhsOffset (int): offset of the left hand side in its array
            rhs (T[]): array right hand side of remainder
            rhsOffset (int): offset of the right hand side in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _rootN_1__T = typing.TypeVar('_rootN_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def rootN(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, n: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute n :sup:`th` root of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            n (int): order of the root
            result (double[]): array where result must be stored (for n :sup:`th` root the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def rootN(self, operand: typing.Union[typing.List[_rootN_1__T], jpype.JArray], operandOffset: int, n: int, result: typing.Union[typing.List[_rootN_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute n :sup:`th` root of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            n (int): order of the root
            result (T[]): array where result must be stored (for n :sup:`th` root the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _sin_1__T = typing.TypeVar('_sin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sin(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute sine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def sin(self, operand: typing.Union[typing.List[_sin_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_sin_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute sine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _sinCos_1__T = typing.TypeVar('_sinCos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sinCos(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, sin: typing.Union[typing.List[float], jpype.JArray], sinOffset: int, cos: typing.Union[typing.List[float], jpype.JArray], cosOffset: int) -> None:
        """
        Compute combined sine and cosine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            sin (double[]): array where sine must be stored (for sine the result array cannot be the input array)
            sinOffset (int): offset of the result in its array
            cos (double[]): array where cosine must be stored (for cosine the result array cannot be the input array)
            cosOffset (int): offset of the result in its array
        
        Since:
            1.4
        
        """
        ...
    @typing.overload
    def sinCos(self, operand: typing.Union[typing.List[_sinCos_1__T], jpype.JArray], operandOffset: int, sin: typing.Union[typing.List[_sinCos_1__T], jpype.JArray], sinOffset: int, cos: typing.Union[typing.List[_sinCos_1__T], jpype.JArray], cosOffset: int) -> None:
        """
        Compute combined sine and cosine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            sin (T[]): array where sine must be stored (for sine the result array cannot be the input array)
            sinOffset (int): offset of the result in its array
            cos (T[]): array where cosine must be stored (for cosine the result array cannot be the input array)
            cosOffset (int): offset of the result in its array
        
        Since:
            1.4
        
        
        """
        ...
    _sinh_1__T = typing.TypeVar('_sinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sinh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute hyperbolic sine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for hyperbolic sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def sinh(self, operand: typing.Union[typing.List[_sinh_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_sinh_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute hyperbolic sine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for hyperbolic sine the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _sinhCosh_1__T = typing.TypeVar('_sinhCosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sinhCosh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, sinh: typing.Union[typing.List[float], jpype.JArray], sinhOffset: int, cosh: typing.Union[typing.List[float], jpype.JArray], coshOffset: int) -> None:
        """
        Compute combined hyperbolic sine and cosine of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            sinh (double[]): array where hyperbolic sine must be stored (for sine the result array cannot be the input array)
            sinhOffset (int): offset of the result in its array
            cosh (double[]): array where hyperbolic cannot be the input array)
            coshOffset (int): offset of the result in its array
        
        Since:
            2.0
        
        """
        ...
    @typing.overload
    def sinhCosh(self, operand: typing.Union[typing.List[_sinhCosh_1__T], jpype.JArray], operandOffset: int, sinh: typing.Union[typing.List[_sinhCosh_1__T], jpype.JArray], sinhOffset: int, cosh: typing.Union[typing.List[_sinhCosh_1__T], jpype.JArray], coshOffset: int) -> None:
        """
        Compute combined hyperbolic sine and cosine of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            sinh (T[]): array where hyperbolic sine must be stored (for sine the result array cannot be the input array)
            sinhOffset (int): offset of the result in its array
            cosh (T[]): array where hyperbolic cosine must be stored (for cosine the result array cannot be the input array)
            coshOffset (int): offset of the result in its array
        
        Since:
            1.4
        
        
        """
        ...
    _sqrt_1__T = typing.TypeVar('_sqrt_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sqrt(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute square root of a derivative structure. Based on the multiplication operator.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for square root the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def sqrt(self, operand: typing.Union[typing.List[_sqrt_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_sqrt_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute square root of a derivative structure. Based on the multiplication operator.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for square root the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _subtract_1__T = typing.TypeVar('_subtract_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def subtract(self, lhs: typing.Union[typing.List[float], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[float], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Perform subtraction of two derivative structures.
        
        Parameters:
            lhs (double[]): array holding left hand side of subtraction
            lhsOffset (int): offset of the left hand side in its array
            rhs (double[]): array right hand side of subtraction
            rhsOffset (int): offset of the right hand side in its array
            result (double[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def subtract(self, lhs: typing.Union[typing.List[_subtract_1__T], jpype.JArray], lhsOffset: int, rhs: typing.Union[typing.List[_subtract_1__T], jpype.JArray], rhsOffset: int, result: typing.Union[typing.List[_subtract_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Perform subtraction of two derivative structures.
        
        Parameters:
            lhs (T[]): array holding left hand side of subtraction
            lhsOffset (int): offset of the left hand side in its array
            rhs (T[]): array right hand side of subtraction
            rhsOffset (int): offset of the right hand side in its array
            result (T[]): array where result must be stored (it may be one of the input arrays)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _tan_1__T = typing.TypeVar('_tan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def tan(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute tangent of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def tan(self, operand: typing.Union[typing.List[_tan_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_tan_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute tangent of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _tanh_1__T = typing.TypeVar('_tanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def tanh(self, operand: typing.Union[typing.List[float], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[float], jpype.JArray], resultOffset: int) -> None:
        """
        Compute hyperbolic tangent of a derivative structure.
        
        Parameters:
            operand (double[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (double[]): array where result must be stored (for hyperbolic tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def tanh(self, operand: typing.Union[typing.List[_tanh_1__T], jpype.JArray], operandOffset: int, result: typing.Union[typing.List[_tanh_1__T], jpype.JArray], resultOffset: int) -> None:
        """
        Compute hyperbolic tangent of a derivative structure.
        
        Parameters:
            operand (T[]): array holding the operand
            operandOffset (int): offset of the operand in its array
            result (T[]): array where result must be stored (for hyperbolic tangent the result array cannot be the input array)
            resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _taylor_1__T = typing.TypeVar('_taylor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _taylor_2__T = typing.TypeVar('_taylor_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def taylor(self, ds: typing.Union[typing.List[float], jpype.JArray], dsOffset: int, *delta: float) -> float: ...
    @typing.overload
    def taylor(self, ds: typing.Union[typing.List[_taylor_1__T], jpype.JArray], dsOffset: int, *delta: _taylor_1__T) -> _taylor_1__T: ...
    @typing.overload
    def taylor(self, ds: typing.Union[typing.List[_taylor_2__T], jpype.JArray], dsOffset: int, *delta: float) -> _taylor_2__T: ...

class DSFactory(java.io.Serializable):
    """
    Factory for DerivativeStructure.
    
    This class is a factory for DerivativeStructure instances.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.1
    
    Also see:
        DerivativeStructure, serialized
    """
    def __init__(self, parameters: int, order: int):
        """
        Simple constructor.
        
        Parameters:
            parameters (int): number of free parameters
            order (int): derivation order
        
        
        """
        ...
    def build(self, *derivatives: float) -> 'DerivativeStructure':
        """
        Build a DerivativeStructure from all its derivatives.
        
        Parameters:
            derivatives (double...): derivatives sorted according to getPartialDerivativeIndex
        
        Returns:
            a DerivativeStructure with specified derivatives
        
        Raises:
            MathIllegalArgumentException: if derivatives array does not match the getSize expected by
                the compiler
            MathIllegalArgumentException: if order is too large
        
        Also see:
            getAllDerivatives
        
        
        """
        ...
    def constant(self, value: float) -> 'DerivativeStructure':
        """
        Build a DerivativeStructure representing a constant value.
        
        Parameters:
            value (double): value of the constant
        
        Returns:
            a DerivativeStructure representing a constant value
        
        
        """
        ...
    def getCompiler(self) -> DSCompiler:
        """
        Get the compiler for the current dimensions.
        
        Returns:
            compiler for the current dimensions
        
        
        """
        ...
    def getDerivativeField(self) -> 'DSFactory.DSField':
        """
        Get the Field the DerivativeStructure instances belong to.
        
        Returns:
            Field the DerivativeStructure instances
            belong to
        
        
        """
        ...
    def variable(self, index: int, value: float) -> 'DerivativeStructure':
        """
        Build a DerivativeStructure representing a variable.
        
        Instances built using this method are considered to be the free variables with respect to which differentials are computed. As such, their differential with respect to themselves is +1.
        
        Parameters:
            index (int): index of the variable (from 0 to
                getCompiler.getFreeParameters
                - 1)
            value (double): value of the variable
        
        Returns:
            a DerivativeStructure representing a variable
        
        Raises:
            MathIllegalArgumentException: if index if greater or equal to
                getCompiler.getFreeParameters.
        
        
        """
        ...
    class DSField(org.hipparchus.Field['DerivativeStructure']):
        def equals(self, object: typing.Any) -> bool: ...
        def getOne(self) -> 'DerivativeStructure': ...
        def getPi(self) -> 'DerivativeStructure': ...
        def getRuntimeClass(self) -> typing.Type['DerivativeStructure']: ...
        def getZero(self) -> 'DerivativeStructure': ...
        def hashCode(self) -> int: ...

class DifferentialAlgebra:
    """
    Interface representing an object holding partial derivatives.
    
    Since:
        3.1
    
    Also see:
        Derivative,
        TaylorMap,
        FieldDerivative,
        FieldTaylorMap
    """
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Returns:
            maximum derivation order
        
        
        """
        ...

_FDSFactory__DerivativeField__T = typing.TypeVar('_FDSFactory__DerivativeField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FDSFactory__T = typing.TypeVar('_FDSFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FDSFactory(typing.Generic[_FDSFactory__T]):
    """
    Factory for FieldDerivativeStructure.
    
    This class is a factory for FieldDerivativeStructure instances.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        FieldDerivativeStructure
    """
    def __init__(self, valueField: org.hipparchus.Field[_FDSFactory__T], parameters: int, order: int):
        """
        Simple constructor.
        
        Parameters:
            valueField (Field<FDSFactory> valueField): field for the function parameters and value
            parameters (int): number of free parameters
            order (int): derivation order
        
        
        """
        ...
    @typing.overload
    def build(self, *derivatives: _FDSFactory__T) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def build(self, *derivatives: float) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def constant(self, value: float) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def constant(self, value: _FDSFactory__T) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    def getCompiler(self) -> DSCompiler:
        """
        Get the compiler for the current dimensions.
        
        Returns:
            compiler for the current dimensions
        
        
        """
        ...
    def getDerivativeField(self) -> 'FDSFactory.DerivativeField'[_FDSFactory__T]:
        """
        Get the Field the FieldDerivativeStructure instances belong to.
        
        Returns:
            Field the FieldDerivativeStructure instances
            belong to
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FDSFactory__T]:
        """
        Get the Field the value and parameters of the function belongs to.
        
        Returns:
            Field the value and parameters of the function belongs to
        
        
        """
        ...
    @typing.overload
    def variable(self, index: int, value: float) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def variable(self, index: int, value: _FDSFactory__T) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    class DerivativeField(org.hipparchus.Field['FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]], typing.Generic[_FDSFactory__DerivativeField__T]):
        def equals(self, object: typing.Any) -> bool: ...
        def getOne(self) -> 'FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]: ...
        def getPi(self) -> 'FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]: ...
        def getRuntimeClass(self) -> typing.Type['FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]]: ...
        def getZero(self) -> 'FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]: ...
        def hashCode(self) -> int: ...

_FieldGradientField__T = typing.TypeVar('_FieldGradientField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGradientField(org.hipparchus.Field['FieldGradient'[_FieldGradientField__T]], typing.Generic[_FieldGradientField__T]):
    """
    Field for Gradient instances.
    
    Since:
        1.7
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    _getField__T = typing.TypeVar('_getField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getField(valueField: org.hipparchus.Field[_getField__T], parameters: int) -> 'FieldGradientField'[_getField__T]:
        """
        Get the field for number of free parameters.
        
        Parameters:
            valueField (Field<T> valueField): field for the function parameters and value
            parameters (int): number of free parameters
        
        Returns:
            cached field
        
        
        """
        ...
    def getOne(self) -> 'FieldGradient'[_FieldGradientField__T]:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['FieldGradient'[_FieldGradientField__T]]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> 'FieldGradient'[_FieldGradientField__T]:
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

_FieldUnivariateDerivative1Field__T = typing.TypeVar('_FieldUnivariateDerivative1Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative1Field(org.hipparchus.Field['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]], typing.Generic[_FieldUnivariateDerivative1Field__T]):
    """
    Field for FieldUnivariateDerivative1 instances.
    
    Since:
        1.7
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getOne(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    _getUnivariateDerivative1Field__T = typing.TypeVar('_getUnivariateDerivative1Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getUnivariateDerivative1Field(valueField: org.hipparchus.Field[_getUnivariateDerivative1Field__T]) -> 'FieldUnivariateDerivative1Field'[_getUnivariateDerivative1Field__T]:
        """
        Get the univariate derivative field corresponding to a value field.
        
        Parameters:
            valueField (Field<T> valueField): field for the function parameters and value
        
        Returns:
            univariate derivative field
        
        
        """
        ...
    def getZero(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]:
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

_FieldUnivariateDerivative2Field__T = typing.TypeVar('_FieldUnivariateDerivative2Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative2Field(org.hipparchus.Field['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]], typing.Generic[_FieldUnivariateDerivative2Field__T]):
    """
    Field for FieldUnivariateDerivative2 instances.
    
    Since:
        1.7
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    def getOne(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]:
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]]:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    _getUnivariateDerivative2Field__T = typing.TypeVar('_getUnivariateDerivative2Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getUnivariateDerivative2Field(valueField: org.hipparchus.Field[_getUnivariateDerivative2Field__T]) -> 'FieldUnivariateDerivative2Field'[_getUnivariateDerivative2Field__T]:
        """
        Get the univariate derivative field corresponding to a value field.
        
        Parameters:
            valueField (Field<T> valueField): field for the function parameters and value
        
        Returns:
            univariate derivative field
        
        
        """
        ...
    def getZero(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]:
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class GradientField(org.hipparchus.Field['Gradient']):
    """
    Field for Gradient instances.
    
    Since:
        1.7
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def getField(parameters: int) -> 'GradientField':
        """
        Get the field for number of free parameters.
        
        Parameters:
            parameters (int): number of free parameters
        
        Returns:
            cached field
        
        
        """
        ...
    def getOne(self) -> 'Gradient':
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['Gradient']:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> 'Gradient':
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class GradientFunction(org.hipparchus.analysis.MultivariateVectorFunction):
    """
    Class representing the gradient of a multivariate function.
    
    The vectorial components of the function represent the derivatives with respect to each function parameters.
    """
    def __init__(self, f: 'MultivariateDifferentiableFunction'):
        """
        Simple constructor.
        
        Parameters:
            f (MultivariateDifferentiableFunction): underlying real-valued function
        
        
        """
        ...
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]:
        """
        Compute the value for the function at the given point.
        
        Specified by: value in interface MultivariateVectorFunction
        
        Parameters:
            point (double[]): point at which the function must be evaluated
        
        Returns:
            function value for the given point
        
        
        """
        ...

class JacobianFunction(org.hipparchus.analysis.MultivariateMatrixFunction):
    """
    Class representing the Jacobian of a multivariate vector function.
    
    The rows iterate on the model functions while the columns iterate on the parameters; thus, the numbers of rows is equal to the dimension of the underlying function vector value and the number of columns is equal to the number of free parameters of the underlying function.
    """
    def __init__(self, f: 'MultivariateDifferentiableVectorFunction'):
        """
        Simple constructor.
        
        Parameters:
            f (MultivariateDifferentiableVectorFunction): underlying vector-valued function
        
        
        """
        ...
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the value for the function at the given point.
        
        Specified by: value in interface MultivariateMatrixFunction
        
        Parameters:
            point (double[]): point at which the function must be evaluated
        
        Returns:
            function value for the given point
        
        
        """
        ...

class MultivariateDifferentiableFunction(org.hipparchus.analysis.MultivariateFunction):
    """
    Extension of MultivariateFunction representing a multivariate differentiable real function.
    """
    @typing.overload
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> float: ...
    @typing.overload
    def value(self, point: typing.Union[typing.List['DerivativeStructure'], jpype.JArray]) -> 'DerivativeStructure': ...

class MultivariateDifferentiableVectorFunction(org.hipparchus.analysis.MultivariateVectorFunction):
    """
    Extension of MultivariateVectorFunction representing a multivariate differentiable vectorial function.
    """
    @typing.overload
    def value(self, point: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def value(self, point: typing.Union[typing.List['DerivativeStructure'], jpype.JArray]) -> typing.MutableSequence['DerivativeStructure']: ...

class UnivariateDerivative1Field(org.hipparchus.Field['UnivariateDerivative1'], java.io.Serializable):
    """
    Field for UnivariateDerivative1 instances.
    
    This class is a singleton.
    
    Since:
        1.7
    
    Also see:
        serialized
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'UnivariateDerivative1Field':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getOne(self) -> 'UnivariateDerivative1':
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['UnivariateDerivative1']:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> 'UnivariateDerivative1':
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class UnivariateDerivative2Field(org.hipparchus.Field['UnivariateDerivative2'], java.io.Serializable):
    """
    Field for UnivariateDerivative2 instances.
    
    This class is a singleton.
    
    Since:
        1.7
    
    Also see:
        serialized
    """
    def equals(self, other: typing.Any) -> bool:
        """
        Overrides: Object in class Object
        
        
        """
        ...
    @staticmethod
    def getInstance() -> 'UnivariateDerivative2Field':
        """
        Get the unique instance.
        
        Returns:
            the unique instance
        
        
        """
        ...
    def getOne(self) -> 'UnivariateDerivative2':
        """
        Get the multiplicative identity of the field.
        
        The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the equalities a × e :sub:`1` = e :sub:`1` × a = a hold.
        
        Specified by: getOne in interface Field
        
        Returns:
            multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['UnivariateDerivative2']:
        """
        Returns the runtime class of the FieldElement.
        
        Specified by: getRuntimeClass in interface Field
        
        Returns:
            The Class object that represents the runtime class of this object.
        
        
        """
        ...
    def getZero(self) -> 'UnivariateDerivative2':
        """
        Get the additive identity of the field.
        
        The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a + e :sub:`0` = e :sub:`0` + a = a hold.
        
        Specified by: getZero in interface Field
        
        Returns:
            additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: Object in class Object
        
        
        """
        ...

class UnivariateDifferentiableFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    Interface for univariate functions derivatives.
    
    This interface represents a simple function which computes both the value and the first derivative of a mathematical function. The derivative is computed with respect to the input variable.
    
    Also see:
        UnivariateDifferentiableFunction,
        UnivariateFunctionDifferentiator
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound='Derivative')  # <T>
    @typing.overload
    def value(self, x: float) -> float: ...
    @typing.overload
    def value(self, x: _value_1__T) -> _value_1__T: ...

class UnivariateDifferentiableMatrixFunction(org.hipparchus.analysis.UnivariateMatrixFunction):
    """
    Extension of UnivariateMatrixFunction representing a univariate differentiable matrix function.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound='Derivative')  # <T>
    @typing.overload
    def value(self, x: float) -> typing.MutableSequence[typing.MutableSequence[float]]: ...
    @typing.overload
    def value(self, x: _value_1__T) -> typing.MutableSequence[typing.MutableSequence[_value_1__T]]: ...

class UnivariateDifferentiableVectorFunction(org.hipparchus.analysis.UnivariateVectorFunction):
    """
    Extension of UnivariateVectorFunction representing a univariate differentiable vectorial function.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound='Derivative')  # <T>
    @typing.overload
    def value(self, x: float) -> typing.MutableSequence[float]: ...
    @typing.overload
    def value(self, x: _value_1__T) -> typing.MutableSequence[_value_1__T]: ...

class UnivariateFunctionDifferentiator:
    """
    Interface defining the function differentiation operation.
    """
    def differentiate(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> UnivariateDifferentiableFunction:
        """
        Create an implementation of a UnivariateDifferentiableFunction from a regular UnivariateFunction.
        
        Parameters:
            function (UnivariateFunction): function to differentiate
        
        Returns:
            differential function
        
        
        """
        ...

class UnivariateMatrixFunctionDifferentiator:
    """
    Interface defining the function differentiation operation.
    """
    def differentiate(self, function: typing.Union[org.hipparchus.analysis.UnivariateMatrixFunction, typing.Callable]) -> UnivariateDifferentiableMatrixFunction:
        """
        Create an implementation of a UnivariateDifferentiableMatrixFunction from a regular UnivariateMatrixFunction.
        
        Parameters:
            function (UnivariateMatrixFunction): function to differentiate
        
        Returns:
            differential function
        
        
        """
        ...

class UnivariateVectorFunctionDifferentiator:
    """
    Interface defining the function differentiation operation.
    """
    def differentiate(self, function: typing.Union[org.hipparchus.analysis.UnivariateVectorFunction, typing.Callable]) -> UnivariateDifferentiableVectorFunction:
        """
        Create an implementation of a UnivariateDifferentiableVectorFunction from a regular UnivariateVectorFunction.
        
        Parameters:
            function (UnivariateVectorFunction): function to differentiate
        
        Returns:
            differential function
        
        
        """
        ...

_Derivative__T = typing.TypeVar('_Derivative__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class Derivative(org.hipparchus.CalculusFieldElement[_Derivative__T], DifferentialAlgebra, typing.Generic[_Derivative__T]):
    """
    Interface representing both the value and the differentials of a function.
    
    Since:
        1.7
    """
    def acos(self) -> _Derivative__T:
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            acos(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: _Derivative__T) -> _Derivative__T:
        """
        '+' operator.
        
        Specified by: add in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this+a
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> _Derivative__T: ...
    def compose(self, *f: float) -> _Derivative__T:
        """
        Compute composition of the instance by a univariate function.
        
        Parameters:
            f (double...): array of value and derivatives of the function at the current point (i.e.
                [f(getValue),
                f'(getValue),
                f''(getValue)...]).
        
        Returns:
            f(this)
        
        Raises:
            MathIllegalArgumentException: if the number of derivatives in the array is not equal to
                getOrder + 1
        
        
        """
        ...
    def cosh(self) -> _Derivative__T:
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            cosh(this)
        
        
        """
        ...
    def getExponent(self) -> int:
        """
        Return the exponent of the instance, removing the bias.
        
        For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
        Specified by: getExponent in interface CalculusFieldElement
        
        Returns:
            exponent for the instance, without bias
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> float:
        """
        Get a partial derivative.
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
            MathIllegalArgumentException: if sum of derivation orders is larger than the instance limits
        
        Also see:
            getValue
        
        
        """
        ...
    def getReal(self) -> float:
        """
        Get the real value of the number.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get the value part of the function.
        
        Returns:
            value part of the value of the function
        
        
        """
        ...
    def log10(self) -> _Derivative__T:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    @typing.overload
    def pow(self, e: _Derivative__T) -> _Derivative__T:
        """
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            e (Derivative): exponent
        
        Returns:
            this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, e: float) -> _Derivative__T: ...
    @typing.overload
    def pow(self, e: int) -> _Derivative__T: ...
    @typing.overload
    def remainder(self, a: _Derivative__T) -> _Derivative__T:
        """
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> _Derivative__T: ...
    def sinh(self) -> _Derivative__T:
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            sinh(this)
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> _Derivative__T:
        """
        '-' operator.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this-a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: _Derivative__T) -> _Derivative__T: ...
    def withValue(self, value: float) -> _Derivative__T:
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Parameters:
            value (double): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        Since:
            3.1
        
        
        """
        ...

_FieldDerivative__S = typing.TypeVar('_FieldDerivative__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
_FieldDerivative__T = typing.TypeVar('_FieldDerivative__T', bound='FieldDerivative')  # <T>
class FieldDerivative(org.hipparchus.CalculusFieldElement[_FieldDerivative__T], DifferentialAlgebra, typing.Generic[_FieldDerivative__S, _FieldDerivative__T]):
    """
    Interface representing both the value and the differentials of a function.
    
    Since:
        1.7
    
    Also see:
        Derivative
    """
    def acos(self) -> _FieldDerivative__T:
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Returns:
            acos(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: _FieldDerivative__T) -> _FieldDerivative__T:
        """
        '+' operator.
        
        Parameters:
            a (FieldDerivative): right hand side parameter of the operator
        
        Returns:
            this+a
        
        Since:
            3.1
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> _FieldDerivative__T: ...
    @typing.overload
    def add(self, a: _FieldDerivative__S) -> _FieldDerivative__T: ...
    def ceil(self) -> _FieldDerivative__T:
        """
        Get the smallest whole number larger than instance.
        
        Specified by: ceil in interface CalculusFieldElement
        
        Returns:
            ceil(this)
        
        
        """
        ...
    def cosh(self) -> _FieldDerivative__T:
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Returns:
            cosh(this)
        
        
        """
        ...
    def floor(self) -> _FieldDerivative__T:
        """
        Get the largest whole number smaller than instance.
        
        Specified by: floor in interface CalculusFieldElement
        
        Returns:
            floor(this)
        
        
        """
        ...
    def getExponent(self) -> int:
        """
        Return the exponent of the instance, removing the bias.
        
        For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
        Specified by: getExponent in interface CalculusFieldElement
        
        Returns:
            exponent for the instance, without bias
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> _FieldDerivative__S:
        """
        Get a partial derivative.
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
            MathIllegalArgumentException: if sum of derivation orders is larger than the instance limits
        
        Also see:
            getValue
        
        
        """
        ...
    def getReal(self) -> float:
        """
        Get the real value of the number.
        
        Specified by: getReal in interface FieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getValue(self) -> _FieldDerivative__S:
        """
        Get the value part of the function.
        
        Returns:
            value part of the value of the function
        
        
        """
        ...
    def log10(self) -> _FieldDerivative__T:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    @typing.overload
    def newInstance(self, value: float) -> _FieldDerivative__T:
        """
        Create an instance corresponding to a constant Field value.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Parameters:
            value (FieldDerivative): constant value
        
        Returns:
            instance corresponding to a constant Field value
        
        Since:
            3.1
        
        
        """
        ...
    @typing.overload
    def newInstance(self, value: _FieldDerivative__S) -> _FieldDerivative__T: ...
    @typing.overload
    def pow(self, e: float) -> _FieldDerivative__T:
        """
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            e (FieldDerivative): exponent
        
        Returns:
            this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, e: int) -> _FieldDerivative__T: ...
    @typing.overload
    def pow(self, e: _FieldDerivative__T) -> _FieldDerivative__T: ...
    def rint(self) -> _FieldDerivative__T:
        """
        Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
        Specified by: rint in interface CalculusFieldElement
        
        Returns:
            a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def sign(self) -> _FieldDerivative__T:
        """
        Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
        Specified by: sign in interface CalculusFieldElement
        
        Returns:
            -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sinh(self) -> _FieldDerivative__T:
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Returns:
            sinh(this)
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> _FieldDerivative__T:
        """
        '-' operator.
        
        Parameters:
            a (FieldDerivative): right hand side parameter of the operator
        
        Returns:
            this-a
        
        Since:
            3.1
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: _FieldDerivative__T) -> _FieldDerivative__T: ...
    @typing.overload
    def subtract(self, a: _FieldDerivative__S) -> _FieldDerivative__T: ...
    def ulp(self) -> _FieldDerivative__T:
        """
        Compute least significant bit (Unit in Last Position) for a number.
        
        Specified by: ulp in interface CalculusFieldElement
        
        Returns:
            ulp(this)
        
        
        """
        ...
    def withValue(self, value: _FieldDerivative__S) -> _FieldDerivative__T:
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Parameters:
            value (FieldDerivative): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        Since:
            3.1
        
        
        """
        ...

_FieldTaylorMap__T = typing.TypeVar('_FieldTaylorMap__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldTaylorMap(DifferentialAlgebra, typing.Generic[_FieldTaylorMap__T]):
    """
    Container for a Taylor map.
    
    A Taylor map is a set of n DerivativeStructure \((f_1, f_2, \ldots, f_n)\) depending on m parameters \((p_1, p_2, \ldots, p_m)\), with positive n and m.
    
    Since:
        2.2
    """
    @typing.overload
    def __init__(self, point: typing.Union[typing.List[_FieldTaylorMap__T], jpype.JArray], functions: typing.Union[typing.List['FieldDerivativeStructure'[_FieldTaylorMap__T]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, valueField: org.hipparchus.Field[_FieldTaylorMap__T], parameters: int, order: int, nbFunctions: int): ...
    def compose(self, other: 'FieldTaylorMap'[_FieldTaylorMap__T]) -> 'FieldTaylorMap'[_FieldTaylorMap__T]:
        """
        Compose the instance with another Taylor map as \(\mathrm{this} \circ \mathrm{other}\).
        
        Parameters:
            other (FieldTaylorMap<FieldTaylorMap> other): map with which instance must be composed
        
        Returns:
            composed map \(\mathrm{this} \circ \mathrm{other}\)
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getFunction(self, i: int) -> 'FieldDerivativeStructure'[_FieldTaylorMap__T]:
        """
        Get a function from the map.
        
        Parameters:
            i (int): index of the function (must be between 0 included and
                getNbFunctions excluded
        
        Returns:
            function at index i
        
        
        """
        ...
    def getNbFunctions(self) -> int:
        """
        Get the number of functions of the map.
        
        Returns:
            number of functions of the map
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Specified by: getOrder in interface DifferentialAlgebra
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def getPoint(self) -> typing.MutableSequence[_FieldTaylorMap__T]:
        """
        Get the point at which map is evaluated.
        
        Returns:
            point at which map is evaluated
        
        
        """
        ...
    def invert(self, decomposer: typing.Union[org.hipparchus.linear.FieldMatrixDecomposer[_FieldTaylorMap__T], typing.Callable[[org.hipparchus.linear.FieldMatrix[org.hipparchus.FieldElement]], org.hipparchus.linear.FieldDecompositionSolver[org.hipparchus.FieldElement]]]) -> 'FieldTaylorMap'[_FieldTaylorMap__T]:
        """
        Invert the instance.
        
        Consider value of the map with small parameters offsets \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\) which leads to evaluation offsets \((f_1 + df_1, f_2 + df_2, \ldots, f_n + df_n)\). The map inversion defines a Taylor map that computes \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\) from \((df_1, df_2, \ldots, df_n)\).
        
        The map must be square to be invertible (i.e. the number of functions and the number of parameters in the functions must match)
        
        Parameters:
            decomposer (FieldMatrixDecomposer<FieldTaylorMap> decomposer): matrix decomposer to user for inverting the linear part
        
        Returns:
            inverted map
        
        Also see:
            S1076
        
        
        """
        ...
    @typing.overload
    def value(self, *deltaP: float) -> typing.MutableSequence[_FieldTaylorMap__T]:
        """
        Evaluate Taylor expansion of the map at some offset.
        
        Parameters:
            deltaP (double...): parameters offsets \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\)
        
        Returns:
            value of the Taylor expansion at \((p_1 + \Delta p_1, p_2 + \Delta p_2, \ldots, p_n + \Delta p_n)\)
        
        Evaluate Taylor expansion of the map at some offset.
        
        Parameters:
            deltaP (FieldTaylorMap...): parameters offsets \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\)
        
        Returns:
            value of the Taylor expansion at \((p_1 + \Delta p_1, p_2 + \Delta p_2, \ldots, p_n + \Delta p_n)\)
        
        
        """
        ...
    @typing.overload
    def value(self, *deltaP: _FieldTaylorMap__T) -> typing.MutableSequence[_FieldTaylorMap__T]: ...

class FiniteDifferencesDifferentiator(UnivariateFunctionDifferentiator, UnivariateVectorFunctionDifferentiator, UnivariateMatrixFunctionDifferentiator, java.io.Serializable):
    """
    Univariate functions differentiator using finite differences.
    
    This class creates some wrapper objects around regular UnivariateFunction (or UnivariateVectorFunction or UnivariateMatrixFunction). These wrapper objects compute derivatives in addition to function values.
    
    The wrapper objects work by calling the underlying function on a sampling grid around the current point and performing polynomial interpolation. A finite differences scheme with n points is theoretically able to compute derivatives up to order n-1, but it is generally better to have a slight margin. The step size must also be small enough in order for the polynomial approximation to be good in the current point neighborhood, but it should not be too small because numerical instability appears quickly (there are several differences of close points). Choosing the number of points and the step size is highly problem dependent.
    
    As an example of good and bad settings, lets consider the quintic polynomial function 5)*(x+1). Since it is a polynomial, finite differences with at least 6 points should theoretically recover the exact same polynomial and hence compute accurate derivatives for any order. However, due to numerical errors, we get the following results for a 7 points finite differences for abscissae in the [-10, 10] range:
    
      - step size = 0.25, second order derivative error about 9.97e-10
      - step size = 0.25, fourth order derivative error about 5.43e-8
      - step size = 1.0e-6, second order derivative error about 148
      - step size = 1.0e-6, fourth order derivative error about 6.35e+14
    
    This example shows that the small step size is really bad, even simply for second order derivative!
    
    Also see:
        serialized
    """
    @typing.overload
    def __init__(self, nbPoints: int, stepSize: float): ...
    @typing.overload
    def __init__(self, nbPoints: int, stepSize: float, tLower: float, tUpper: float): ...
    @typing.overload
    def differentiate(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> UnivariateDifferentiableFunction:
        """
        Create an implementation of a UnivariateDifferentiableFunction from a regular UnivariateFunction.
        
        The returned object cannot compute derivatives to arbitrary orders. The value function will throw a MathIllegalArgumentException if the requested derivation order is larger or equal to the number of points.
        
        Specified by: differentiate in interface UnivariateFunctionDifferentiator
        
        Parameters:
            function (UnivariateFunction): function to differentiate
        
        Returns:
            differential function
        
        Create an implementation of a UnivariateDifferentiableVectorFunction from a regular UnivariateVectorFunction.
        
        The returned object cannot compute derivatives to arbitrary orders. The value function will throw a MathIllegalArgumentException if the requested derivation order is larger or equal to the number of points.
        
        Specified by: differentiate in interface UnivariateVectorFunctionDifferentiator
        
        Parameters:
            function (UnivariateVectorFunction): function to differentiate
        
        Returns:
            differential function
        
        Create an implementation of a UnivariateDifferentiableMatrixFunction from a regular UnivariateMatrixFunction.
        
        The returned object cannot compute derivatives to arbitrary orders. The value function will throw a MathIllegalArgumentException if the requested derivation order is larger or equal to the number of points.
        
        Specified by: differentiate in interface UnivariateMatrixFunctionDifferentiator
        
        Parameters:
            function (UnivariateMatrixFunction): function to differentiate
        
        Returns:
            differential function
        
        
        """
        ...
    @typing.overload
    def differentiate(self, function: typing.Union[org.hipparchus.analysis.UnivariateMatrixFunction, typing.Callable]) -> UnivariateDifferentiableMatrixFunction: ...
    @typing.overload
    def differentiate(self, function: typing.Union[org.hipparchus.analysis.UnivariateVectorFunction, typing.Callable]) -> UnivariateDifferentiableVectorFunction: ...
    def getNbPoints(self) -> int:
        """
        Get the number of points to use.
        
        Returns:
            number of points to use
        
        
        """
        ...
    def getStepSize(self) -> float:
        """
        Get the step size.
        
        Returns:
            step size
        
        
        """
        ...

class TaylorMap(DifferentialAlgebra):
    """
    Container for a Taylor map.
    
    A Taylor map is a set of n DerivativeStructure \((f_1, f_2, \ldots, f_n)\) depending on m parameters \((p_1, p_2, \ldots, p_m)\), with positive n and m.
    
    Since:
        2.2
    """
    @typing.overload
    def __init__(self, point: typing.Union[typing.List[float], jpype.JArray], functions: typing.Union[typing.List['DerivativeStructure'], jpype.JArray]): ...
    @typing.overload
    def __init__(self, parameters: int, order: int, nbFunctions: int): ...
    def compose(self, other: 'TaylorMap') -> 'TaylorMap':
        """
        Compose the instance with another Taylor map as \(\mathrm{this} \circ \mathrm{other}\).
        
        Parameters:
            other (TaylorMap): map with which instance must be composed
        
        Returns:
            composed map \(\mathrm{this} \circ \mathrm{other}\)
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getFunction(self, i: int) -> 'DerivativeStructure':
        """
        Get a function from the map.
        
        Parameters:
            i (int): index of the function (must be between 0 included and
                getNbFunctions excluded
        
        Returns:
            function at index i
        
        
        """
        ...
    def getNbFunctions(self) -> int:
        """
        Get the number of functions of the map.
        
        Returns:
            number of functions of the map
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Specified by: getOrder in interface DifferentialAlgebra
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def getPoint(self) -> typing.MutableSequence[float]:
        """
        Get the point at which map is evaluated.
        
        Returns:
            point at which map is evaluated
        
        
        """
        ...
    def invert(self, decomposer: typing.Union[org.hipparchus.linear.MatrixDecomposer, typing.Callable]) -> 'TaylorMap':
        """
        Invert the instance.
        
        Consider value of the map with small parameters offsets \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\) which leads to evaluation offsets \((f_1 + df_1, f_2 + df_2, \ldots, f_n + df_n)\). The map inversion defines a Taylor map that computes \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\) from \((df_1, df_2, \ldots, df_n)\).
        
        The map must be square to be invertible (i.e. the number of functions and the number of parameters in the functions must match)
        
        Parameters:
            decomposer (MatrixDecomposer): matrix decomposer to user for inverting the linear part
        
        Returns:
            inverted map
        
        Also see:
            S1076
        
        
        """
        ...
    def value(self, *deltaP: float) -> typing.MutableSequence[float]:
        """
        Evaluate Taylor expansion of the map at some offset.
        
        Parameters:
            deltaP (double...): parameters offsets \((\Delta p_1, \Delta p_2, \ldots, \Delta p_n)\)
        
        Returns:
            value of the Taylor expansion at \((p_1 + \Delta p_1, p_2 + \Delta p_2, \ldots, p_n + \Delta p_n)\)
        
        
        """
        ...

_Derivative1__T = typing.TypeVar('_Derivative1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class Derivative1(Derivative[_Derivative1__T], typing.Generic[_Derivative1__T]):
    """
    Interface representing an object holding partial derivatives up to first order.
    
    Since:
        3.1
    
    Also see:
        Derivative,
        UnivariateDerivative1,
        Gradient,
        SparseGradient
    """
    def acos(self) -> _Derivative1__T:
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Specified by: acos in interface Derivative
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> _Derivative1__T:
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    def asin(self) -> _Derivative1__T:
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> _Derivative1__T:
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> _Derivative1__T:
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atanh(self) -> _Derivative1__T:
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> _Derivative1__T:
        """
        Cubic root.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    @typing.overload
    def compose(self, *double: float) -> _Derivative1__T:
        """
        Compute composition of the instance by a univariate function differentiable at order 1.
        
        Parameters:
            f0 (double): value of function
            f1 (double): first-order derivative
        
        Returns:
            f(this)
        
        
        """
        ...
    @typing.overload
    def compose(self, f0: float, f1: float) -> _Derivative1__T: ...
    def cos(self) -> _Derivative1__T:
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> _Derivative1__T:
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Specified by: cosh in interface Derivative
        
        Returns:
            cosh(this)
        
        
        """
        ...
    def exp(self) -> _Derivative1__T:
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> _Derivative1__T:
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Specified by: getOrder in interface DifferentialAlgebra
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def log(self) -> _Derivative1__T:
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> _Derivative1__T:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Specified by: log10 in interface Derivative
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> _Derivative1__T:
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    def reciprocal(self) -> _Derivative1__T:
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    def rootN(self, n: int) -> _Derivative1__T:
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def sin(self) -> _Derivative1__T:
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos[_Derivative1__T]:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> _Derivative1__T:
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Specified by: sinh in interface Derivative
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh[_Derivative1__T]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> _Derivative1__T:
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> _Derivative1__T:
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    def tan(self) -> _Derivative1__T:
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> _Derivative1__T:
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...

class DerivativeStructure(Derivative['DerivativeStructure'], java.io.Serializable):
    """
    Class representing both the value and the differentials of a function.
    
    This class is the workhorse of the differentiation package.
    
    This class is an implementation of the extension to Rall's numbers described in Dan Kalman's paper `Doubly Recursive Multivariate Automatic Differentiation <http://www.dankalman.net/AUhome/pdffiles/mmgautodiff.pdf>`, Mathematics Magazine, vol. 75, no. 3, June 2002. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function. Dan Kalman's derivative structures hold all partial derivatives up to any specified order, with respect to any number of free parameters. Rall's numbers therefore can be seen as derivative structures for order one derivative and one free parameter, and real numbers can be seen as derivative structures with zero order derivative and no free parameters.
    
    DerivativeStructure instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Implementing complex expression can also be done by developing computation code using standard primitive double values and to use UnivariateFunctionDifferentiator to create the DerivativeStructure-based instances. This method is simpler but may be limited in the accuracy and derivation orders and may be computationally intensive (this is typically the case for FiniteDifferencesDifferentiator.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        DSCompiler,
        FieldDerivativeStructure, serialized
    """
    def abs(self) -> 'DerivativeStructure':
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'DerivativeStructure':
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Specified by: acos in interface Derivative
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'DerivativeStructure':
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> org.hipparchus.CalculusFieldElement: ...
    @typing.overload
    def add(self, a: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def asin(self) -> 'DerivativeStructure':
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'DerivativeStructure':
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'DerivativeStructure':
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    @typing.overload
    def atan2(self, x: 'DerivativeStructure') -> 'DerivativeStructure':
        """
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders are inconsistent
        
        public static DerivativeStructure atan2 (DerivativeStructure y, DerivativeStructure x) throws MathIllegalArgumentException
        
        Two arguments arc tangent operation.
        
        Parameters:
            y (DerivativeStructure): first argument of the arc tangent
            x (DerivativeStructure): second argument of the arc tangent
        
        Returns:
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(y: 'DerivativeStructure', x: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def atanh(self) -> 'DerivativeStructure':
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def compose(self, *f: float) -> 'DerivativeStructure':
        """
        Compute composition of the instance by a univariate function.
        
        Specified by: compose in interface Derivative
        
        Parameters:
            f (double...): array of value and derivatives of the function at the current point (i.e.
                [f(getValue),
                f'(getValue),
                f''(getValue)...]).
        
        Returns:
            f(this)
        
        Raises:
            MathIllegalArgumentException: if the number of derivatives in the array is not equal to
                getOrder + 1
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'DerivativeStructure':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (DerivativeStructure): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def cos(self) -> 'DerivativeStructure':
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'DerivativeStructure':
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Specified by: cosh in interface Derivative
        
        Returns:
            cosh(this)
        
        
        """
        ...
    def differentiate(self, varIndex: int, differentiationOrder: int) -> 'DerivativeStructure':
        """
        Differentiate w.r.t. one independent variable.
        
        Rigorously, if the derivatives of a function are known up to order N, the ones of its M-th derivative w.r.t. a given variable (seen as a function itself) are only known up to order N-M. However, this method still casts the output as a DerivativeStructure of order N with zeroes for the higher order terms.
        
        Parameters:
            varIndex (int): Index of independent variable w.r.t. which differentiation is done.
            differentiationOrder (int): Number of times the differentiation operator must be applied. If non-positive, call the integration operator instead.
        
        Returns:
            DerivativeStructure on which differentiation operator has been applied a certain number of times
        
        Since:
            2.2
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'DerivativeStructure':
        """
        '÷' operator.
        
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        public DerivativeStructure divide (DerivativeStructure a) throws MathIllegalArgumentException
        
        Compute this ÷ a.
        
        Specified by: divide in interface CalculusFieldElement
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (DerivativeStructure): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def divide(self, a: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two derivative structures.
        
        Derivative structures are considered equal if they have the same number of free parameters, the same derivation order, and the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two derivative structures are equal
        
        
        """
        ...
    def exp(self) -> 'DerivativeStructure':
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'DerivativeStructure':
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def getAddendum(self) -> 'DerivativeStructure':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getAllDerivatives(self) -> typing.MutableSequence[float]:
        """
        Get all partial derivatives.
        
        Returns:
            a fresh copy of partial derivatives, in an array sorted according to
            getPartialDerivativeIndex
        
        
        """
        ...
    def getFactory(self) -> DSFactory:
        """
        Get the factory that built the instance.
        
        Returns:
            factory that built the instance
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['DerivativeStructure']:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Specified by: getOrder in interface DifferentialAlgebra
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> float:
        """
        Get a partial derivative.
        
        Specified by: getPartialDerivative in interface Derivative
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
        
        Also see:
            getValue
        
        
        """
        ...
    def getPi(self) -> 'DerivativeStructure':
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get the value part of the derivative structure.
        
        Specified by: getValue in interface Derivative
        
        Returns:
            value part of the derivative structure
        
        Also see:
            getPartialDerivative
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the derivative structure.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    @typing.overload
    def hypot(self, y: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    @staticmethod
    def hypot(x: 'DerivativeStructure', y: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def integrate(self, varIndex: int, integrationOrder: int) -> 'DerivativeStructure':
        """
        Integrate w.r.t. one independent variable.
        
        Rigorously, if the derivatives of a function are known up to order N, the ones of its M-th integral w.r.t. a given variable (seen as a function itself) are actually known up to order N+M. However, this method still casts the output as a DerivativeStructure of order N. The integration constants are systematically set to zero.
        
        Parameters:
            varIndex (int): Index of independent variable w.r.t. which integration is done.
            integrationOrder (int): Number of times the integration operator must be applied. If non-positive, call the differentiation operator.
        
        Returns:
            DerivativeStructure on which integration operator has been applied a certain number of times.
        
        Since:
            2.2
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'DerivativeStructure', a2: float, b2: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'DerivativeStructure', a2: float, b2: 'DerivativeStructure', a3: float, b3: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'DerivativeStructure', a2: float, b2: 'DerivativeStructure', a3: float, b3: 'DerivativeStructure', a4: float, b4: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['DerivativeStructure'], jpype.JArray]) -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a1: 'DerivativeStructure', b1: 'DerivativeStructure', a2: 'DerivativeStructure', b2: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a1: 'DerivativeStructure', b1: 'DerivativeStructure', a2: 'DerivativeStructure', b2: 'DerivativeStructure', a3: 'DerivativeStructure', b3: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a1: 'DerivativeStructure', b1: 'DerivativeStructure', a2: 'DerivativeStructure', b2: 'DerivativeStructure', a3: 'DerivativeStructure', b3: 'DerivativeStructure', a4: 'DerivativeStructure', b4: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['DerivativeStructure'], jpype.JArray], b: typing.Union[typing.List['DerivativeStructure'], jpype.JArray]) -> 'DerivativeStructure': ...
    def log(self) -> 'DerivativeStructure':
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'DerivativeStructure':
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Specified by: log10 in interface Derivative
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'DerivativeStructure':
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, a: int) -> org.hipparchus.FieldElement:
        """
        '×' operator.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        public DerivativeStructure multiply (DerivativeStructure a) throws MathIllegalArgumentException
        
        Compute this × a.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (DerivativeStructure): element to multiply
        
        Returns:
            a new element representing this × a
        
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def multiply(self, a: float) -> 'DerivativeStructure': ...
    @typing.overload
    def multiply(self, a: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def negate(self) -> 'DerivativeStructure':
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, value: float) -> 'DerivativeStructure':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            value (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'DerivativeStructure':
        """
        Compute a :sup:`x` where a is a double and x a DerivativeStructure
        
        Parameters:
            a (double): number to exponentiate
            x (DerivativeStructure): power to apply
        
        Returns:
            a :sup:`x`
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        public DerivativeStructure pow (DerivativeStructure e) throws MathIllegalArgumentException
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Specified by: pow in interface Derivative
        
        Parameters:
            e (DerivativeStructure): exponent
        
        Returns:
            this :sup:`e`
        
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'DerivativeStructure': ...
    @typing.overload
    def pow(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def rebase(self, *p: 'DerivativeStructure') -> 'DerivativeStructure':
        """
        Rebase instance with respect to low level parameter functions.
        
        The instance is considered to be a function of getFreeParameters up to order getOrder \(f(p_0, p_1, \ldots p_{n-1})\). Its getPartialDerivative are therefore \(f, \frac{\partial f}{\partial p_0}, \frac{\partial f}{\partial p_1}, \ldots \frac{\partial^2 f}{\partial p_0^2}, \frac{\partial^2 f}{\partial p_0 p_1}, \ldots \frac{\partial^o f}{\partial p_{n-1}^o}\). The free parameters \(p_0, p_1, \ldots p_{n-1}\) are considered to be functions of \(m\) lower level other parameters \(q_0, q_1, \ldots q_{m-1}\). \( \begin{align} p_0 & = p_0(q_0, q_1, \ldots q_{m-1})\\ p_1 & = p_1(q_0, q_1, \ldots q_{m-1})\\ p_{n-1} & = p_{n-1}(q_0, q_1, \ldots q_{m-1}) \end{align}\)
        
        This method compute the composition of the partial derivatives of \(f\) and the partial derivatives of \(p_0, p_1, \ldots p_{n-1}\), i.e. the getPartialDerivative of the value returned will be \(f, \frac{\partial f}{\partial q_0}, \frac{\partial f}{\partial q_1}, \ldots \frac{\partial^2 f}{\partial q_0^2}, \frac{\partial^2 f}{\partial q_0 q_1}, \ldots \frac{\partial^o f}{\partial q_{m-1}^o}\).
        
        The number of parameters must match getFreeParameters and the derivation orders of the instance and parameters must also match.
        
        Parameters:
            p (DerivativeStructure...): base parameters with respect to which partial derivatives were computed in the instance
        
        Returns:
            derivative structure with partial derivatives computed with respect to the lower level parameters used in the \(p_i\)
        
        Since:
            2.2
        
        
        """
        ...
    def reciprocal(self) -> 'DerivativeStructure':
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> org.hipparchus.CalculusFieldElement: ...
    @typing.overload
    def remainder(self, a: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def rootN(self, n: int) -> 'DerivativeStructure':
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'DerivativeStructure':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sin(self) -> 'DerivativeStructure':
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['DerivativeStructure']:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'DerivativeStructure':
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Specified by: sinh in interface Derivative
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['DerivativeStructure']:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'DerivativeStructure':
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'DerivativeStructure':
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> org.hipparchus.CalculusFieldElement: ...
    @typing.overload
    def subtract(self, a: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def tan(self) -> 'DerivativeStructure':
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'DerivativeStructure':
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...
    def taylor(self, *delta: float) -> float:
        """
        Evaluate Taylor expansion a derivative structure.
        
        Parameters:
            delta (double...): parameters offsets (Δx, Δy...)
        
        Returns:
            value of the Taylor expansion at x + Δx, y + Δy...
        
        Raises:
            MathRuntimeException: if factorials becomes too large
        
        
        """
        ...
    def toDegrees(self) -> 'DerivativeStructure':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'DerivativeStructure':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, value: float) -> 'DerivativeStructure':
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface Derivative
        
        Parameters:
            value (double): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

_FieldDerivative1__S = typing.TypeVar('_FieldDerivative1__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
_FieldDerivative1__T = typing.TypeVar('_FieldDerivative1__T', bound=FieldDerivative)  # <T>
class FieldDerivative1(FieldDerivative[_FieldDerivative1__S, _FieldDerivative1__T], typing.Generic[_FieldDerivative1__S, _FieldDerivative1__T]):
    """
    Interface representing a Field object holding partial derivatives up to first order.
    
    Since:
        3.1
    
    Also see:
        FieldDerivative,
        FieldUnivariateDerivative1,
        FieldGradient,
        Derivative1
    """
    def acos(self) -> _FieldDerivative1__T:
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Specified by: acos in interface FieldDerivative
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> _FieldDerivative1__T:
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    def asin(self) -> _FieldDerivative1__T:
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> _FieldDerivative1__T:
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> _FieldDerivative1__T:
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atanh(self) -> _FieldDerivative1__T:
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> _FieldDerivative1__T:
        """
        Cubic root.
        
        Specified by: cbrt in interface CalculusFieldElement
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def compose(self, f0: _FieldDerivative1__S, f1: _FieldDerivative1__S) -> _FieldDerivative1__T:
        """
        Compute composition of the instance by a univariate function differentiable at order 1.
        
        Parameters:
            f0 (FieldDerivative1): value of function
            f1 (FieldDerivative1): first-order derivative
        
        Returns:
            f(this)
        
        
        """
        ...
    def cos(self) -> _FieldDerivative1__T:
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> _FieldDerivative1__T:
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Specified by: cosh in interface FieldDerivative
        
        Returns:
            cosh(this)
        
        
        """
        ...
    def exp(self) -> _FieldDerivative1__T:
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> _FieldDerivative1__T:
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Specified by: getOrder in interface DifferentialAlgebra
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def log(self) -> _FieldDerivative1__T:
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> _FieldDerivative1__T:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Specified by: log10 in interface FieldDerivative
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> _FieldDerivative1__T:
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    def reciprocal(self) -> _FieldDerivative1__T:
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    def sin(self) -> _FieldDerivative1__T:
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos[_FieldDerivative1__T]:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> _FieldDerivative1__T:
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Specified by: sinh in interface FieldDerivative
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh[_FieldDerivative1__T]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> _FieldDerivative1__T:
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> _FieldDerivative1__T:
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    def tan(self) -> _FieldDerivative1__T:
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> _FieldDerivative1__T:
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...

_FieldDerivativeStructure__T = typing.TypeVar('_FieldDerivativeStructure__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDerivativeStructure(FieldDerivative[_FieldDerivativeStructure__T, 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]], typing.Generic[_FieldDerivativeStructure__T]):
    """
    Class representing both the value and the differentials of a function.
    
    This class is similar to DerivativeStructure except function parameters and value can be any CalculusFieldElement.
    
    Instances of this class are guaranteed to be immutable.
    
    Also see:
        DerivativeStructure,
        FDSFactory,
        DSCompiler
    """
    def abs(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Arc cosine operation.
        
        Specified by: acos in interface CalculusFieldElement
        
        Specified by: acos in interface FieldDerivative
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Inverse hyperbolic cosine operation.
        
        Specified by: acosh in interface CalculusFieldElement
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: org.hipparchus.CalculusFieldElement) -> _FieldDerivativeStructure__T: ...
    @typing.overload
    def add(self, a: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def add(self, a: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def asin(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Arc sine operation.
        
        Specified by: asin in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Inverse hyperbolic sine operation.
        
        Specified by: asinh in interface CalculusFieldElement
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Arc tangent operation.
        
        Specified by: atan in interface CalculusFieldElement
        
        Returns:
            atan(this)
        
        
        """
        ...
    _atan2_1__T = typing.TypeVar('_atan2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atan2(self, x: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders are inconsistent
        
        public static <T extends CalculusFieldElement<T>> FieldDerivativeStructure<T> atan2 (FieldDerivativeStructure<T> y, FieldDerivativeStructure<T> x) throws MathIllegalArgumentException
        
        Two arguments arc tangent operation.
        
        Parameters:
            y (FieldDerivativeStructure<T> y): first argument of the arc tangent
            x (FieldDerivativeStructure<T> x): second argument of the arc tangent
        
        Returns:
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(y: 'FieldDerivativeStructure'[_atan2_1__T], x: 'FieldDerivativeStructure'[_atan2_1__T]) -> 'FieldDerivativeStructure'[_atan2_1__T]: ...
    def atanh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Inverse hyperbolic tangent operation.
        
        Specified by: atanh in interface CalculusFieldElement
        
        Returns:
            atanh(this)
        
        
        """
        ...
    @typing.overload
    def compose(self, *f: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def compose(self, *f: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def copySign(self, sign: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def copySign(self, sign: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def copySign(self, sign: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def cos(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Cosine operation.
        
        Specified by: cos in interface CalculusFieldElement
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Hyperbolic cosine operation.
        
        Specified by: cosh in interface CalculusFieldElement
        
        Specified by: cosh in interface FieldDerivative
        
        Returns:
            cosh(this)
        
        
        """
        ...
    def differentiate(self, varIndex: int, differentiationOrder: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Differentiate w.r.t. one independent variable.
        
        Rigorously, if the derivatives of a function are known up to order N, the ones of its M-th derivative w.r.t. a given variable (seen as a function itself) are only known up to order N-M. However, this method still casts the output as a DerivativeStructure of order N with zeroes for the higher order terms.
        
        Parameters:
            varIndex (int): Index of independent variable w.r.t. which differentiation is done.
            differentiationOrder (int): Number of times the differentiation operator must be applied. If non-positive, call the integration operator instead.
        
        Returns:
            DerivativeStructure on which differentiation operator has been applied a certain number of times
        
        Since:
            2.2
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def divide(self, a: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def divide(self, a: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two derivative structures.
        
        Derivative structures are considered equal if they have the same number of free parameters, the same derivation order, and the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two derivative structures are equal
        
        
        """
        ...
    def exp(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Exponential.
        
        Specified by: exp in interface CalculusFieldElement
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Exponential minus 1.
        
        Specified by: expm1 in interface CalculusFieldElement
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def getAddendum(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getAllDerivatives(self) -> typing.MutableSequence[_FieldDerivativeStructure__T]:
        """
        Get all partial derivatives.
        
        Returns:
            a fresh copy of partial derivatives, in an array sorted according to
            getPartialDerivativeIndex
        
        
        """
        ...
    def getFactory(self) -> FDSFactory[_FieldDerivativeStructure__T]:
        """
        Get the factory that built the instance.
        
        Returns:
            factory that built the instance
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Specified by: getOrder in interface DifferentialAlgebra
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> _FieldDerivativeStructure__T:
        """
        Get a partial derivative.
        
        Specified by: getPartialDerivative in interface FieldDerivative
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
        
        Also see:
            getValue
        
        
        """
        ...
    def getPi(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getValue(self) -> _FieldDerivativeStructure__T:
        """
        Get the value part of the derivative structure.
        
        Specified by: getValue in interface FieldDerivative
        
        Returns:
            value part of the derivative structure
        
        Also see:
            getPartialDerivative
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the derivative structure.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    _hypot_1__T = typing.TypeVar('_hypot_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def hypot(self, y: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    @staticmethod
    def hypot(x: 'FieldDerivativeStructure'[_hypot_1__T], y: 'FieldDerivativeStructure'[_hypot_1__T]) -> 'FieldDerivativeStructure'[_hypot_1__T]: ...
    def integrate(self, varIndex: int, integrationOrder: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Integrate w.r.t. one independent variable.
        
        Rigorously, if the derivatives of a function are known up to order N, the ones of its M-th integral w.r.t. a given variable (seen as a function itself) are actually known up to order N+M. However, this method still casts the output as a DerivativeStructure of order N. The integration constants are systematically set to zero.
        
        Parameters:
            varIndex (int): Index of independent variable w.r.t. which integration is done.
            integrationOrder (int): Number of times the integration operator must be applied. If non-positive, call the differentiation operator.
        
        Returns:
            DerivativeStructure on which integration operator has been applied a certain number of times.
        
        Since:
            2.2
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: float, b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: float, b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a3: float, b3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: float, b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a3: float, b3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a4: float, b4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]], jpype.JArray]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: _FieldDerivativeStructure__T, b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: _FieldDerivativeStructure__T, b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: _FieldDerivativeStructure__T, b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: _FieldDerivativeStructure__T, b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a3: _FieldDerivativeStructure__T, b3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: _FieldDerivativeStructure__T, b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: _FieldDerivativeStructure__T, b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a3: _FieldDerivativeStructure__T, b3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a4: _FieldDerivativeStructure__T, b4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[_FieldDerivativeStructure__T], jpype.JArray], b: typing.Union[typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]], jpype.JArray]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b1: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], a4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], b4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]], jpype.JArray], b: typing.Union[typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]], jpype.JArray]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def log(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Natural logarithm.
        
        Specified by: log in interface CalculusFieldElement
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Base 10 logarithm.
        
        Specified by: log10 in interface CalculusFieldElement
        
        Specified by: log10 in interface FieldDerivative
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Shifted natural logarithm.
        
        Specified by: log1p in interface CalculusFieldElement
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, a: int) -> _FieldDerivativeStructure__T: ...
    @typing.overload
    def multiply(self, a: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def multiply(self, a: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def multiply(self, a: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def negate(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    @typing.overload
    def newInstance(self, value: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def newInstance(self, value: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def pow(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'FieldDerivativeStructure'[_pow_3__T]) -> 'FieldDerivativeStructure'[_pow_3__T]:
        """
        Compute a :sup:`x` where a is a double and x a FieldDerivativeStructure
        
        Parameters:
            a (double): number to exponentiate
            x (FieldDerivativeStructure<T> x): power to apply
        
        Returns:
            a :sup:`x`
        
        public FieldDerivativeStructure<FieldDerivativeStructure> pow (double p)
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        public FieldDerivativeStructure<FieldDerivativeStructure> pow (int n)
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        public FieldDerivativeStructure<FieldDerivativeStructure> pow (FieldDerivativeStructure<FieldDerivativeStructure> e) throws MathIllegalArgumentException
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Specified by: pow in interface FieldDerivative
        
        Parameters:
            e (FieldDerivativeStructure<FieldDerivativeStructure> e): exponent
        
        Returns:
            this :sup:`e`
        
        Raises:
            MathIllegalArgumentException: if number of free parameters or orders do not match
        
        
        """
        ...
    def rebase(self, *p: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Rebase instance with respect to low level parameter functions.
        
        The instance is considered to be a function of getFreeParameters up to order getOrder \(f(p_0, p_1, \ldots p_{n-1})\). Its getPartialDerivative are therefore \(f, \frac{\partial f}{\partial p_0}, \frac{\partial f}{\partial p_1}, \ldots \frac{\partial^2 f}{\partial p_0^2}, \frac{\partial^2 f}{\partial p_0 p_1}, \ldots \frac{\partial^o f}{\partial p_{n-1}^o}\). The free parameters \(p_0, p_1, \ldots p_{n-1}\) are considered to be functions of \(m\) lower level other parameters \(q_0, q_1, \ldots q_{m-1}\). \( \begin{align} p_0 & = p_0(q_0, q_1, \ldots q_{m-1})\\ p_1 & = p_1(q_0, q_1, \ldots q_{m-1})\\ p_{n-1} & = p_{n-1}(q_0, q_1, \ldots q_{m-1}) \end{align}\)
        
        This method compute the composition of the partial derivatives of \(f\) and the partial derivatives of \(p_0, p_1, \ldots p_{n-1}\), i.e. the getPartialDerivative of the value returned will be \(f, \frac{\partial f}{\partial q_0}, \frac{\partial f}{\partial q_1}, \ldots \frac{\partial^2 f}{\partial q_0^2}, \frac{\partial^2 f}{\partial q_0 q_1}, \ldots \frac{\partial^o f}{\partial q_{m-1}^o}\).
        
        The number of parameters must match getFreeParameters and the derivation orders of the instance and parameters must also match.
        
        Parameters:
            p (FieldDerivativeStructure<FieldDerivativeStructure>...): base parameters with respect to which partial derivatives were computed in the instance
        
        Returns:
            derivative structure with partial derivatives computed with respect to the lower level parameters used in the \(p_i\)
        
        Since:
            2.2
        
        
        """
        ...
    def reciprocal(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Returns the multiplicative inverse of this element.
        
        Specified by: reciprocal in interface FieldElement
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def remainder(self, a: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def remainder(self, a: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def rootN(self, n: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sin(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Sine operation.
        
        Specified by: sin in interface CalculusFieldElement
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Hyperbolic sine operation.
        
        Specified by: sinh in interface CalculusFieldElement
        
        Specified by: sinh in interface FieldDerivative
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Compute this × this.
        
        Specified by: square in interface CalculusFieldElement
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: org.hipparchus.CalculusFieldElement) -> _FieldDerivativeStructure__T: ...
    @typing.overload
    def subtract(self, a: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def subtract(self, a: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def tan(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Tangent operation.
        
        Specified by: tan in interface CalculusFieldElement
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Hyperbolic tangent operation.
        
        Specified by: tanh in interface CalculusFieldElement
        
        Returns:
            tanh(this)
        
        
        """
        ...
    @typing.overload
    def taylor(self, *delta: _FieldDerivativeStructure__T) -> _FieldDerivativeStructure__T: ...
    @typing.overload
    def taylor(self, *delta: float) -> _FieldDerivativeStructure__T: ...
    def toDegrees(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, value: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface FieldDerivative
        
        Parameters:
            value (FieldDerivativeStructure): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

_FieldUnivariateDerivative__S = typing.TypeVar('_FieldUnivariateDerivative__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
_FieldUnivariateDerivative__T = typing.TypeVar('_FieldUnivariateDerivative__T', bound='FieldUnivariateDerivative')  # <T>
class FieldUnivariateDerivative(FieldDerivative[_FieldUnivariateDerivative__S, _FieldUnivariateDerivative__T], typing.Generic[_FieldUnivariateDerivative__S, _FieldUnivariateDerivative__T]):
    """
    Abstract class representing both the value and the differentials of a function.
    
    Since:
        1.7
    """
    def getDerivative(self, n: int) -> _FieldUnivariateDerivative__S:
        """
        Get a derivative from the univariate derivative.
        
        Parameters:
            n (int): derivation order (must be between 0 and getOrder,
                both inclusive)
        
        Returns:
            n :sup:`th` derivative
        
        Raises:
            MathIllegalArgumentException: if n is either negative or strictly larger than
                getOrder
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> _FieldUnivariateDerivative__S:
        """
        Get a partial derivative.
        
        Specified by: getPartialDerivative in interface FieldDerivative
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
        
        Also see:
            getValue
        
        
        """
        ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldUnivariateDerivative__S]:
        """
        Convert the instance to a DerivativeStructure.
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...

_UnivariateDerivative__T = typing.TypeVar('_UnivariateDerivative__T', bound='UnivariateDerivative')  # <T>
class UnivariateDerivative(Derivative[_UnivariateDerivative__T], java.io.Serializable, java.lang.Comparable[_UnivariateDerivative__T], typing.Generic[_UnivariateDerivative__T]):
    """
    Abstract class representing both the value and the differentials of a function.
    
    Since:
        1.7
    
    Also see:
        serialized
    """
    def getDerivative(self, n: int) -> float:
        """
        Get a derivative from the univariate derivative.
        
        Parameters:
            n (int): derivation order (must be between 0 and getOrder,
                both inclusive)
        
        Returns:
            n :sup:`th` derivative
        
        Raises:
            MathIllegalArgumentException: if n is either negative or strictly larger than
                getOrder
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> float:
        """
        Get a partial derivative.
        
        Specified by: getPartialDerivative in interface Derivative
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
        
        Also see:
            getValue
        
        
        """
        ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
        Convert the instance to a DerivativeStructure.
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...

_FieldGradient__T = typing.TypeVar('_FieldGradient__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGradient(FieldDerivative1[_FieldGradient__T, 'FieldGradient'[_FieldGradient__T]], typing.Generic[_FieldGradient__T]):
    """
    Class representing both the value and the differentials of a function.
    
    This class is a stripped-down version of FieldDerivativeStructure with getOrder limited to one. It should have less overhead than FieldDerivativeStructure in its domain.
    
    This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function.
    
    FieldGradient instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.7
    
    Also see:
        DerivativeStructure,
        UnivariateDerivative1,
        UnivariateDerivative2,
        Gradient,
        FieldDerivativeStructure,
        FieldUnivariateDerivative1,
        FieldUnivariateDerivative2
    """
    @typing.overload
    def __init__(self, value: _FieldGradient__T, *gradient: _FieldGradient__T): ...
    @typing.overload
    def __init__(self, ds: FieldDerivativeStructure[_FieldGradient__T]): ...
    def abs(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: org.hipparchus.CalculusFieldElement) -> _FieldGradient__T: ...
    @typing.overload
    def add(self, a: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def add(self, a: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def atan2(self, x: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (FieldGradient<FieldGradient> x): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def compose(self, g0: _FieldGradient__T, g1: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Compute composition of the instance by a function.
        
        Specified by: compose in interface FieldDerivative1
        
        Parameters:
            g0 (FieldGradient): value of the function at the current point (i.e. at g(getValue()))
            g1 (FieldGradient): first derivative of the function at the current point (i.e. at g'(getValue()))
        
        Returns:
            g(this)
        
        
        """
        ...
    _constant__T = typing.TypeVar('_constant__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def constant(freeParameters: int, value: _constant__T) -> 'FieldGradient'[_constant__T]:
        """
        Build an instance corresponding to a constant value.
        
        Parameters:
            freeParameters (int): number of free parameters (i.e. dimension of the gradient)
            value (T): constant value of the function
        
        Returns:
            a FieldGradient with a constant value and all derivatives set to 0.0
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def copySign(self, sign: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def copySign(self, sign: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def divide(self, a: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def divide(self, a: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def divide(self, a: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two univariate derivatives.
        
        univariate derivatives are considered equal if they have the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two univariate derivatives are equal
        
        
        """
        ...
    def getAddendum(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getField(self) -> FieldGradientField[_FieldGradient__T]:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getGradient(self) -> typing.MutableSequence[_FieldGradient__T]:
        """
        Get the gradient part of the function.
        
        Returns:
            gradient part of the value of the function
        
        
        """
        ...
    @typing.overload
    def getPartialDerivative(self, int: int) -> _FieldGradient__T: ...
    @typing.overload
    def getPartialDerivative(self, *int: int) -> _FieldGradient__T: ...
    def getPi(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getValue(self) -> _FieldGradient__T:
        """
        Get the value part of the function.
        
        Specified by: getValue in interface FieldDerivative
        
        Returns:
            value part of the value of the function
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FieldGradient__T]:
        """
        Get the Field the value and parameters of the function belongs to.
        
        Returns:
            Field the value and parameters of the function belongs to
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the univariate derivative.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def hypot(self, y: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (FieldGradient<FieldGradient> y): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldGradient'[_FieldGradient__T], a2: float, b2: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldGradient'[_FieldGradient__T], a2: float, b2: 'FieldGradient'[_FieldGradient__T], a3: float, b3: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldGradient'[_FieldGradient__T], a2: float, b2: 'FieldGradient'[_FieldGradient__T], a3: float, b3: 'FieldGradient'[_FieldGradient__T], a4: float, b4: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['FieldGradient'[_FieldGradient__T]], jpype.JArray]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a1: _FieldGradient__T, b1: 'FieldGradient'[_FieldGradient__T], a2: _FieldGradient__T, b2: 'FieldGradient'[_FieldGradient__T], a3: _FieldGradient__T, b3: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[_FieldGradient__T], jpype.JArray], b: typing.Union[typing.List['FieldGradient'[_FieldGradient__T]], jpype.JArray]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldGradient'[_FieldGradient__T], b1: 'FieldGradient'[_FieldGradient__T], a2: 'FieldGradient'[_FieldGradient__T], b2: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldGradient'[_FieldGradient__T], b1: 'FieldGradient'[_FieldGradient__T], a2: 'FieldGradient'[_FieldGradient__T], b2: 'FieldGradient'[_FieldGradient__T], a3: 'FieldGradient'[_FieldGradient__T], b3: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldGradient'[_FieldGradient__T], b1: 'FieldGradient'[_FieldGradient__T], a2: 'FieldGradient'[_FieldGradient__T], b2: 'FieldGradient'[_FieldGradient__T], a3: 'FieldGradient'[_FieldGradient__T], b3: 'FieldGradient'[_FieldGradient__T], a4: 'FieldGradient'[_FieldGradient__T], b4: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['FieldGradient'[_FieldGradient__T]], jpype.JArray], b: typing.Union[typing.List['FieldGradient'[_FieldGradient__T]], jpype.JArray]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def negate(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    @typing.overload
    def newInstance(self, c: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def newInstance(self, c: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, t: _FieldGradient__T) -> _FieldGradient__T: ...
    @typing.overload
    def pow(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'FieldGradient'[_pow_3__T]) -> 'FieldGradient'[_pow_3__T]:
        """
        Compute a :sup:`x` where a is a double and x a FieldGradient
        
        Parameters:
            a (double): number to exponentiate
            x (FieldGradient<T> x): power to apply
        
        Returns:
            a :sup:`x`
        
        public FieldGradient<FieldGradient> pow (double p)
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        public FieldGradient<FieldGradient> pow (int n)
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def remainder(self, a: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def remainder(self, a: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def rootN(self, n: int) -> 'FieldGradient'[_FieldGradient__T]:
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldGradient'[_FieldGradient__T]]:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Specified by: sinCos in interface FieldDerivative1
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldGradient'[_FieldGradient__T]]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Specified by: sinhCosh in interface FieldDerivative1
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def stackVariable(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Add an independent variable to the Taylor expansion.
        
        Returns:
            object with one more variable
        
        Since:
            4.0
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: org.hipparchus.CalculusFieldElement) -> _FieldGradient__T: ...
    @typing.overload
    def subtract(self, a: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def subtract(self, a: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def taylor(self, *delta: float) -> _FieldGradient__T:
        """
        Evaluate Taylor expansion of a gradient.
        
        Parameters:
            delta (double...): parameters offsets (Δx, Δy...)
        
        Returns:
            value of the Taylor expansion at x + Δx, y + Δy...
        
        Evaluate Taylor expansion of a gradient.
        
        Parameters:
            delta (FieldGradient...): parameters offsets (Δx, Δy...)
        
        Returns:
            value of the Taylor expansion at x + Δx, y + Δy...
        
        
        """
        ...
    @typing.overload
    def taylor(self, *delta: _FieldGradient__T) -> _FieldGradient__T: ...
    def toDegrees(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldGradient__T]:
        """
        Convert the instance to a FieldDerivativeStructure.
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    _variable__T = typing.TypeVar('_variable__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def variable(freeParameters: int, index: int, value: _variable__T) -> 'FieldGradient'[_variable__T]:
        """
        Build a Gradient representing a variable.
        
        Instances built using this method are considered to be the free variables with respect to which differentials are computed. As such, their differential with respect to themselves is +1.
        
        Parameters:
            freeParameters (int): number of free parameters (i.e. dimension of the gradient)
            index (int): index of the variable (from 0 to getFreeParameters - 1)
            value (T): value of the variable
        
        Returns:
            a FieldGradient with a constant value and all derivatives set to 0.0 except the one at index which will
            be set to 1.0
        
        
        """
        ...
    def withValue(self, v: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]:
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface FieldDerivative
        
        Parameters:
            v (FieldGradient): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

_FieldUnivariateDerivative1__T = typing.TypeVar('_FieldUnivariateDerivative1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative1(FieldUnivariateDerivative[_FieldUnivariateDerivative1__T, 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], FieldDerivative1[_FieldUnivariateDerivative1__T, 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], typing.Generic[_FieldUnivariateDerivative1__T]):
    """
    Class representing both the value and the differentials of a function.
    
    This class is a stripped-down version of FieldDerivativeStructure with only one getFreeParameters and getOrder also limited to one. It should have less overhead than FieldDerivativeStructure in its domain.
    
    This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function.
    
    FieldUnivariateDerivative1 instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.7
    
    Also see:
        DerivativeStructure,
        UnivariateDerivative1,
        UnivariateDerivative2,
        Gradient,
        FieldDerivativeStructure,
        FieldUnivariateDerivative2,
        FieldGradient
    """
    @typing.overload
    def __init__(self, f0: _FieldUnivariateDerivative1__T, f1: _FieldUnivariateDerivative1__T): ...
    @typing.overload
    def __init__(self, ds: FieldDerivativeStructure[_FieldUnivariateDerivative1__T]): ...
    def abs(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: org.hipparchus.CalculusFieldElement) -> _FieldUnivariateDerivative1__T: ...
    @typing.overload
    def add(self, a: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def add(self, a: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def atan2(self, x: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (FieldUnivariateDerivative1<FieldUnivariateDerivative1> x): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def compose(self, g0: _FieldUnivariateDerivative1__T, g1: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Compute composition of the instance by a function.
        
        Specified by: compose in interface FieldDerivative1
        
        Parameters:
            g0 (FieldUnivariateDerivative1): value of the function at the current point (i.e. at g(getValue()))
            g1 (FieldUnivariateDerivative1): first derivative of the function at the current point (i.e. at g'(getValue()))
        
        Returns:
            g(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def copySign(self, sign: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def copySign(self, sign: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def divide(self, a: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def divide(self, a: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def divide(self, a: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two univariate derivatives.
        
        univariate derivatives are considered equal if they have the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two univariate derivatives are equal
        
        
        """
        ...
    def getAddendum(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getDerivative(self, n: int) -> _FieldUnivariateDerivative1__T:
        """
        Get a derivative from the univariate derivative.
        
        Specified by: getDerivative in class FieldUnivariateDerivative
        
        Parameters:
            n (int): derivation order (must be between 0 and getOrder,
                both inclusive)
        
        Returns:
            n :sup:`th` derivative, or NaN if n is either negative or strictly larger than
            getOrder
        
        
        """
        ...
    def getField(self) -> FieldUnivariateDerivative1Field[_FieldUnivariateDerivative1__T]:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFirstDerivative(self) -> _FieldUnivariateDerivative1__T:
        """
        Get the first derivative.
        
        Returns:
            first derivative
        
        Also see:
            getValue
        
        
        """
        ...
    def getPi(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getValue(self) -> _FieldUnivariateDerivative1__T:
        """
        Get the value part of the univariate derivative.
        
        Specified by: getValue in interface FieldDerivative
        
        Returns:
            value part of the univariate derivative
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FieldUnivariateDerivative1__T]:
        """
        Get the Field the value and parameters of the function belongs to.
        
        Returns:
            Field the value and parameters of the function belongs to
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the univariate derivative.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def hypot(self, y: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (FieldUnivariateDerivative1<FieldUnivariateDerivative1> y): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: float, b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: float, b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a3: float, b3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: float, b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a3: float, b3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a4: float, b4: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], jpype.JArray]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a1: _FieldUnivariateDerivative1__T, b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: _FieldUnivariateDerivative1__T, b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a3: _FieldUnivariateDerivative1__T, b3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[_FieldUnivariateDerivative1__T], jpype.JArray], b: typing.Union[typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], jpype.JArray]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b2: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b3: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], a4: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], b4: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], jpype.JArray], b: typing.Union[typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], jpype.JArray]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def negate(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    @typing.overload
    def newInstance(self, value: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def newInstance(self, value: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, t: _FieldUnivariateDerivative1__T) -> _FieldUnivariateDerivative1__T: ...
    @typing.overload
    def pow(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'FieldUnivariateDerivative1'[_pow_3__T]) -> 'FieldUnivariateDerivative1'[_pow_3__T]:
        """
        Compute a :sup:`x` where a is a double and x a FieldUnivariateDerivative1
        
        Parameters:
            a (double): number to exponentiate
            x (FieldUnivariateDerivative1<T> x): power to apply
        
        Returns:
            a :sup:`x`
        
        public FieldUnivariateDerivative1<FieldUnivariateDerivative1> pow (double p)
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        public FieldUnivariateDerivative1<FieldUnivariateDerivative1> pow (int n)
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def remainder(self, a: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def remainder(self, a: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def rootN(self, n: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        N :sup:`th` root.
        
        Specified by: rootN in interface CalculusFieldElement
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: org.hipparchus.CalculusFieldElement) -> _FieldUnivariateDerivative1__T: ...
    @typing.overload
    def subtract(self, a: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def subtract(self, a: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def taylor(self, delta: float) -> _FieldUnivariateDerivative1__T:
        """
        Evaluate Taylor expansion of a univariate derivative.
        
        Parameters:
            delta (double): parameter offset Δx
        
        Returns:
            value of the Taylor expansion at x + Δx
        
        Evaluate Taylor expansion of a univariate derivative.
        
        Parameters:
            delta (FieldUnivariateDerivative1): parameter offset Δx
        
        Returns:
            value of the Taylor expansion at x + Δx
        
        
        """
        ...
    @typing.overload
    def taylor(self, delta: _FieldUnivariateDerivative1__T) -> _FieldUnivariateDerivative1__T: ...
    def toDegrees(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldUnivariateDerivative1__T]:
        """
        Convert the instance to a FieldDerivativeStructure.
        
        Specified by: toDerivativeStructure in class FieldUnivariateDerivative
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, value: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]:
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface FieldDerivative
        
        Parameters:
            value (FieldUnivariateDerivative1): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

_FieldUnivariateDerivative2__T = typing.TypeVar('_FieldUnivariateDerivative2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative2(FieldUnivariateDerivative[_FieldUnivariateDerivative2__T, 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], typing.Generic[_FieldUnivariateDerivative2__T]):
    """
    Class representing both the value and the differentials of a function.
    
    This class is a stripped-down version of FieldDerivativeStructure with only one getFreeParameters and getOrder limited to two. It should have less overhead than FieldDerivativeStructure in its domain.
    
    This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function.
    
    FieldUnivariateDerivative2 instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.7
    
    Also see:
        DerivativeStructure,
        UnivariateDerivative1,
        UnivariateDerivative2,
        Gradient,
        FieldDerivativeStructure,
        FieldUnivariateDerivative1,
        FieldGradient
    """
    @typing.overload
    def __init__(self, f0: _FieldUnivariateDerivative2__T, f1: _FieldUnivariateDerivative2__T, f2: _FieldUnivariateDerivative2__T): ...
    @typing.overload
    def __init__(self, ds: FieldDerivativeStructure[_FieldUnivariateDerivative2__T]): ...
    def abs(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        absolute value.
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Arc cosine operation.
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Inverse hyperbolic cosine operation.
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: org.hipparchus.CalculusFieldElement) -> _FieldUnivariateDerivative2__T: ...
    @typing.overload
    def add(self, a: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def add(self, a: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def asin(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Arc sine operation.
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Inverse hyperbolic sine operation.
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Arc tangent operation.
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atan2(self, x: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Parameters:
            x (FieldUnivariateDerivative2<FieldUnivariateDerivative2> x): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def atanh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Inverse hyperbolic tangent operation.
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Cubic root.
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def compose(self, g0: _FieldUnivariateDerivative2__T, g1: _FieldUnivariateDerivative2__T, g2: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Compute composition of the instance by a function.
        
        Parameters:
            g0 (FieldUnivariateDerivative2): value of the function at the current point (i.e. at g(getValue()))
            g1 (FieldUnivariateDerivative2): first derivative of the function at the current point (i.e. at g'(getValue()))
            g2 (FieldUnivariateDerivative2): second derivative of the function at the current point (i.e. at g''(getValue()))
        
        Returns:
            g(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def copySign(self, sign: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def copySign(self, sign: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def cos(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Cosine operation.
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Hyperbolic cosine operation.
        
        Returns:
            cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def divide(self, a: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def divide(self, a: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two univariate derivatives.
        
        univariate derivatives are considered equal if they have the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Exponential.
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Exponential minus 1.
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def getAddendum(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Returns:
            real value
        
        
        """
        ...
    def getDerivative(self, n: int) -> _FieldUnivariateDerivative2__T:
        """
        Get a derivative from the univariate derivative.
        
        Specified by: getDerivative in class FieldUnivariateDerivative
        
        Parameters:
            n (int): derivation order (must be between 0 and
                getOrder, both inclusive)
        
        Returns:
            n :sup:`th` derivative, or NaN if n is either negative or strictly larger than
            getOrder
        
        
        """
        ...
    def getField(self) -> FieldUnivariateDerivative2Field[_FieldUnivariateDerivative2__T]:
        """
        Get the Field to which the instance belongs.
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFirstDerivative(self) -> _FieldUnivariateDerivative2__T:
        """
        Get the first derivative.
        
        Returns:
            first derivative
        
        Also see:
            getValue
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the derivation order.
        
        Returns:
            derivation order
        
        
        """
        ...
    def getPi(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getSecondDerivative(self) -> _FieldUnivariateDerivative2__T:
        """
        Get the second derivative.
        
        Returns:
            second derivative
        
        Also see:
            getValue,
            getFirstDerivative
        
        
        """
        ...
    def getValue(self) -> _FieldUnivariateDerivative2__T:
        """
        Get the value part of the univariate derivative.
        
        Returns:
            value part of the univariate derivative
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FieldUnivariateDerivative2__T]:
        """
        Get the Field the value and parameters of the function belongs to.
        
        Returns:
            Field the value and parameters of the function belongs to
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the univariate derivative.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def hypot(self, y: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        
        Parameters:
            y (FieldUnivariateDerivative2<FieldUnivariateDerivative2> y): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: float, b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: float, b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a3: float, b3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: float, b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a3: float, b3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a4: float, b4: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], jpype.JArray]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a1: _FieldUnivariateDerivative2__T, b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: _FieldUnivariateDerivative2__T, b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a3: _FieldUnivariateDerivative2__T, b3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[_FieldUnivariateDerivative2__T], jpype.JArray], b: typing.Union[typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], jpype.JArray]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b1: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b3: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], a4: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], b4: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], jpype.JArray], b: typing.Union[typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], jpype.JArray]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def log(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Natural logarithm.
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Base 10 logarithm.
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Shifted natural logarithm.
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def negate(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Returns the additive inverse of this element.
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    @typing.overload
    def newInstance(self, value: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def newInstance(self, value: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, t: _FieldUnivariateDerivative2__T) -> _FieldUnivariateDerivative2__T: ...
    @typing.overload
    def pow(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'FieldUnivariateDerivative2'[_pow_3__T]) -> 'FieldUnivariateDerivative2'[_pow_3__T]:
        """
        Compute a :sup:`x` where a is a double and x a FieldUnivariateDerivative2
        
        Parameters:
            a (double): number to exponentiate
            x (FieldUnivariateDerivative2<T> x): power to apply
        
        Returns:
            a :sup:`x`
        
        public FieldUnivariateDerivative2<FieldUnivariateDerivative2> pow (double p)
        
        Power operation.
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        public FieldUnivariateDerivative2<FieldUnivariateDerivative2> pow (int n)
        
        Integer power operation.
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        
        """
        ...
    def reciprocal(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Returns the multiplicative inverse of this element.
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def remainder(self, a: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def remainder(self, a: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def rootN(self, n: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        N :sup:`th` root.
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Multiply the instance by a power of 2.
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sin(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Sine operation.
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]:
        """
        Combined Sine and Cosine operation.
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Hyperbolic sine operation.
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]:
        """
        Combined hyperbolic sine and cosine operation.
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Square root.
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Compute this × this.
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: org.hipparchus.CalculusFieldElement) -> _FieldUnivariateDerivative2__T: ...
    @typing.overload
    def subtract(self, a: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def subtract(self, a: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def tan(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Tangent operation.
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Hyperbolic tangent operation.
        
        Returns:
            tanh(this)
        
        
        """
        ...
    @typing.overload
    def taylor(self, delta: float) -> _FieldUnivariateDerivative2__T:
        """
        Evaluate Taylor expansion a univariate derivative.
        
        Parameters:
            delta (double): parameter offset Δx
        
        Returns:
            value of the Taylor expansion at x + Δx
        
        Evaluate Taylor expansion a univariate derivative.
        
        Parameters:
            delta (FieldUnivariateDerivative2): parameter offset Δx
        
        Returns:
            value of the Taylor expansion at x + Δx
        
        
        """
        ...
    @typing.overload
    def taylor(self, delta: _FieldUnivariateDerivative2__T) -> _FieldUnivariateDerivative2__T: ...
    def toDegrees(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldUnivariateDerivative2__T]:
        """
        Convert the instance to a FieldDerivativeStructure.
        
        Specified by: toDerivativeStructure in class FieldUnivariateDerivative
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, value: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]:
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Parameters:
            value (FieldUnivariateDerivative2): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

class Gradient(Derivative1['Gradient'], java.io.Serializable):
    """
    Class representing both the value and the differentials of a function.
    
    This class is a stripped-down version of DerivativeStructure with getOrder limited to one. It should have less overhead than DerivativeStructure in its domain.
    
    This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function.
    
    Gradient instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.7
    
    Also see:
        DerivativeStructure,
        UnivariateDerivative1,
        UnivariateDerivative2,
        FieldDerivativeStructure,
        FieldUnivariateDerivative1,
        FieldUnivariateDerivative2,
        FieldGradient, serialized
    """
    @typing.overload
    def __init__(self, value: float, *gradient: float): ...
    @typing.overload
    def __init__(self, ds: DerivativeStructure): ...
    def abs(self) -> 'Gradient':
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this + a.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            a (Gradient): element to add
        
        Returns:
            a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, a: 'Gradient') -> 'Gradient': ...
    def atan2(self, x: 'Gradient') -> 'Gradient':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (Gradient): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    @typing.overload
    def compose(self, f0: float, f1: float) -> 'Gradient':
        """
        Compute composition of the instance by a univariate function differentiable at order 1.
        
        Specified by: compose in interface Derivative1
        
        Parameters:
            f0 (double): value of function
            f1 (double): first-order derivative
        
        Returns:
            f(this)
        
        
        """
        ...
    @typing.overload
    def compose(self, *f: float) -> 'Gradient':
        """
        Compute composition of the instance by a univariate function.
        
        Specified by: compose in interface Derivative
        
        Parameters:
            f (double...): array of value and derivatives of the function at the current point (i.e.
                [f(getValue),
                f'(getValue),
                f''(getValue)...]).
        
        Returns:
            f(this)
        
        """
        ...
    @staticmethod
    def constant(freeParameters: int, value: float) -> 'Gradient':
        """
        Build an instance corresponding to a constant value.
        
        Parameters:
            freeParameters (int): number of free parameters (i.e. dimension of the gradient)
            value (double): constant value of the function
        
        Returns:
            a Gradient with a constant value and all derivatives set to 0.0
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'Gradient':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (Gradient): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def divide(self, a: float) -> 'Gradient':
        """
        '÷' operator.
        
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        Compute this ÷ a.
        
        Specified by: divide in interface CalculusFieldElement
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (Gradient): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, a: 'Gradient') -> 'Gradient': ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two univariate derivatives.
        
        univariate derivatives are considered equal if they have the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two univariate derivatives are equal
        
        
        """
        ...
    def getAddendum(self) -> 'Gradient':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getField(self) -> GradientField:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getGradient(self) -> typing.MutableSequence[float]:
        """
        Get the gradient part of the function.
        
        Returns:
            gradient part of the value of the function
        
        Also see:
            getPartialDerivative
        
        
        """
        ...
    @typing.overload
    def getPartialDerivative(self, int: int) -> float: ...
    @typing.overload
    def getPartialDerivative(self, *int: int) -> float: ...
    def getValue(self) -> float:
        """
        Get the value part of the function.
        
        Specified by: getValue in interface Derivative
        
        Returns:
            value part of the value of the function
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the univariate derivative.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def hypot(self, y: 'Gradient') -> 'Gradient':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (Gradient): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Gradient', a2: float, b2: 'Gradient') -> 'Gradient':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Gradient): first factor of the first term
            b1 (Gradient): second factor of the first term
            a2 (Gradient): first factor of the second term
            b2 (Gradient): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Gradient): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Gradient): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Gradient): first factor of the first term
            b1 (Gradient): second factor of the first term
            a2 (Gradient): first factor of the second term
            b2 (Gradient): second factor of the second term
            a3 (Gradient): first factor of the third term
            b3 (Gradient): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Gradient): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Gradient): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Gradient): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (Gradient): first factor of the first term
            b1 (Gradient): second factor of the first term
            a2 (Gradient): first factor of the second term
            b2 (Gradient): second factor of the second term
            a3 (Gradient): first factor of the third term
            b3 (Gradient): second factor of the third term
            a4 (Gradient): first factor of the fourth term
            b4 (Gradient): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (Gradient): second factor of the first term
            a2 (double): first factor of the second term
            b2 (Gradient): second factor of the second term
            a3 (double): first factor of the third term
            b3 (Gradient): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (Gradient): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Gradient', a2: float, b2: 'Gradient', a3: float, b3: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'Gradient', a2: float, b2: 'Gradient', a3: float, b3: 'Gradient', a4: float, b4: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['Gradient'], jpype.JArray]) -> 'Gradient':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a (Gradient[]): Factors.
            b (Gradient[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a (double[]): Factors.
            b (Gradient[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: 'Gradient', b1: 'Gradient', a2: 'Gradient', b2: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, a1: 'Gradient', b1: 'Gradient', a2: 'Gradient', b2: 'Gradient', a3: 'Gradient', b3: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, a1: 'Gradient', b1: 'Gradient', a2: 'Gradient', b2: 'Gradient', a3: 'Gradient', b3: 'Gradient', a4: 'Gradient', b4: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['Gradient'], jpype.JArray], b: typing.Union[typing.List['Gradient'], jpype.JArray]) -> 'Gradient': ...
    @typing.overload
    def multiply(self, n: float) -> 'Gradient':
        """
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \]
        
        Specified by: multiply in interface CalculusFieldElement
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        '×' operator.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        Compute this × a.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (Gradient): element to multiply
        
        Returns:
            a new element representing this × a
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'Gradient': ...
    @typing.overload
    def multiply(self, gradient: 'Gradient') -> 'Gradient': ...
    def negate(self) -> 'Gradient':
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, c: float) -> 'Gradient':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            c (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, t: org.hipparchus.CalculusFieldElement) -> org.hipparchus.CalculusFieldElement:
        """
        Compute a :sup:`x` where a is a double and x a Gradient
        
        Parameters:
            a (double): number to exponentiate
            x (Gradient): power to apply
        
        Returns:
            a :sup:`x`
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'Gradient': ...
    @typing.overload
    def pow(self, int: int) -> 'Gradient': ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def remainder(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (Gradient): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: 'Gradient') -> 'Gradient': ...
    def scalb(self, n: int) -> 'Gradient':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['Gradient']:
        """
        Combined Sine and Cosine operation.
        
        Specified by: sinCos in interface CalculusFieldElement
        
        Specified by: sinCos in interface Derivative1
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Gradient']:
        """
        Combined hyperbolic sine and cosine operation.
        
        Specified by: sinhCosh in interface CalculusFieldElement
        
        Specified by: sinhCosh in interface Derivative1
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def stackVariable(self) -> 'Gradient':
        """
        Add an independent variable to the Taylor expansion.
        
        Returns:
            object with one more variable
        
        Since:
            4.0
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this - a.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            a (Gradient): element to subtract
        
        Returns:
            a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: 'Gradient') -> 'Gradient': ...
    def taylor(self, *delta: float) -> float:
        """
        Evaluate Taylor expansion a derivative structure.
        
        Parameters:
            delta (double...): parameters offsets (Δx, Δy...)
        
        Returns:
            value of the Taylor expansion at x + Δx, y + Δy...
        
        
        """
        ...
    def toDegrees(self) -> 'Gradient':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
        Convert the instance to a DerivativeStructure.
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'Gradient':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    @staticmethod
    def variable(freeParameters: int, index: int, value: float) -> 'Gradient':
        """
        Build a Gradient representing a variable.
        
        Instances built using this method are considered to be the free variables with respect to which differentials are computed. As such, their differential with respect to themselves is +1.
        
        Parameters:
            freeParameters (int): number of free parameters (i.e. dimension of the gradient)
            index (int): index of the variable (from 0 to getFreeParameters - 1)
            value (double): value of the variable
        
        Returns:
            a Gradient with a constant value and all derivatives set to 0.0 except the one at index which will be
            set to 1.0
        
        
        """
        ...
    def withValue(self, v: float) -> 'Gradient':
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface Derivative
        
        Parameters:
            v (double): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

class SparseGradient(Derivative1['SparseGradient'], java.io.Serializable):
    """
    First derivative computation with large number of variables.
    
    This class plays a similar role to DerivativeStructure, with a focus on efficiency when dealing with large number of independent variables and most computation depend only on a few of them, and when only first derivative is desired. When these conditions are met, this class should be much faster than DerivativeStructure and use less memory.
    
    Also see:
        serialized
    """
    def abs(self) -> 'SparseGradient':
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this + a.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            a (SparseGradient): element to add
        
        Returns:
            a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, a: 'SparseGradient') -> 'SparseGradient': ...
    def addInPlace(self, a: 'SparseGradient') -> None:
        """
        Add in place.
        
        This method is designed to be faster when used multiple times in a loop.
        
        The instance is changed here, in order to not change the instance the add method should be used.
        
        Parameters:
            a (SparseGradient): instance to add
        
        
        """
        ...
    @typing.overload
    def atan2(self, x: 'SparseGradient') -> 'SparseGradient':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (SparseGradient): second argument of the arc tangent
        
        Returns:
        public static SparseGradient atan2 (SparseGradient y, SparseGradient x)
        
        Two arguments arc tangent operation.
        
        Parameters:
            y (SparseGradient): first argument of the arc tangent
            x (SparseGradient): second argument of the arc tangent
        
        Returns:
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(y: 'SparseGradient', x: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def compose(self, f0: float, f1: float) -> 'SparseGradient':
        """
        Compute composition of the instance by a univariate function differentiable at order 1.
        
        Specified by: compose in interface Derivative1
        
        Parameters:
            f0 (double): value of function
            f1 (double): first-order derivative
        
        Returns:
            f(this)
        
        
        """
        ...
    @typing.overload
    def compose(self, *f: float) -> 'SparseGradient':
        """
        Compute composition of the instance by a univariate function.
        
        Specified by: compose in interface Derivative
        
        Parameters:
            f (double...): array of value and derivatives of the function at the current point (i.e.
                [f(getValue),
                f'(getValue),
                f''(getValue)...]).
        
        Returns:
            f(this)
        
        Raises:
            MathIllegalArgumentException: if the number of elements in the array is not equal to 2 (i.e. value and first derivative)
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'SparseGradient':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (SparseGradient): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'SparseGradient') -> 'SparseGradient': ...
    @staticmethod
    def createConstant(value: float) -> 'SparseGradient':
        """
        Factory method creating a constant.
        
        Parameters:
            value (double): value of the constant
        
        Returns:
            a new instance
        
        
        """
        ...
    @staticmethod
    def createVariable(idx: int, value: float) -> 'SparseGradient':
        """
        Factory method creating an independent variable.
        
        Parameters:
            idx (int): index of the variable
            value (double): value of the variable
        
        Returns:
            a new instance
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'SparseGradient':
        """
        Compute this ÷ a.
        
        Specified by: divide in interface CalculusFieldElement
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (SparseGradient): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        '÷' operator.
        
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            c (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        
        """
        ...
    @typing.overload
    def divide(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two sparse gradients.
        
        Sparse gradients are considered equal if they have the same value and the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two sparse gradients are equal
        
        
        """
        ...
    def getAddendum(self) -> 'SparseGradient':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getDerivative(self, index: int) -> float:
        """
        Get the derivative with respect to a particular index variable.
        
        Parameters:
            index (int): index to differentiate with.
        
        Returns:
            derivative with respect to a particular index variable
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['SparseGradient']:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
        Get the number of free parameters.
        
        Specified by: getFreeParameters in interface DifferentialAlgebra
        
        Returns:
            number of free parameters
        
        
        """
        ...
    def getPartialDerivative(self, *orders: int) -> float:
        """
        Get a partial derivative.
        
        Specified by: getPartialDerivative in interface Derivative
        
        Parameters:
            orders (int...): derivation orders with respect to each variable (if all orders are 0, the value is returned)
        
        Returns:
            partial derivative
        
        Raises:
            MathIllegalArgumentException: if the numbers of variables does not match the instance
        
        Also see:
            getValue
        
        
        """
        ...
    def getPi(self) -> 'SparseGradient':
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get the value of the function.
        
        Specified by: getValue in interface Derivative
        
        Returns:
            value of the function.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the derivative structure.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    @typing.overload
    def hypot(self, y: 'SparseGradient') -> 'SparseGradient':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (SparseGradient): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        Returns the hypotenuse of a triangle with sides x and y - sqrt(x :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        
        Parameters:
            x (SparseGradient): a value
            y (SparseGradient): a value
        
        Returns:
            sqrt(x :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hypot(x: 'SparseGradient', y: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'SparseGradient', a2: float, b2: 'SparseGradient') -> 'SparseGradient':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (SparseGradient): first factor of the first term
            b1 (SparseGradient): second factor of the first term
            a2 (SparseGradient): first factor of the second term
            b2 (SparseGradient): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (SparseGradient): second factor of the first term
            a2 (double): first factor of the second term
            b2 (SparseGradient): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (SparseGradient): first factor of the first term
            b1 (SparseGradient): second factor of the first term
            a2 (SparseGradient): first factor of the second term
            b2 (SparseGradient): second factor of the second term
            a3 (SparseGradient): first factor of the third term
            b3 (SparseGradient): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (SparseGradient): second factor of the first term
            a2 (double): first factor of the second term
            b2 (SparseGradient): second factor of the second term
            a3 (double): first factor of the third term
            b3 (SparseGradient): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (SparseGradient): first factor of the first term
            b1 (SparseGradient): second factor of the first term
            a2 (SparseGradient): first factor of the second term
            b2 (SparseGradient): second factor of the second term
            a3 (SparseGradient): first factor of the third term
            b3 (SparseGradient): second factor of the third term
            a4 (SparseGradient): first factor of the fourth term
            b4 (SparseGradient): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (SparseGradient): second factor of the first term
            a2 (double): first factor of the second term
            b2 (SparseGradient): second factor of the second term
            a3 (double): first factor of the third term
            b3 (SparseGradient): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (SparseGradient): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'SparseGradient', a2: float, b2: 'SparseGradient', a3: float, b3: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'SparseGradient', a2: float, b2: 'SparseGradient', a3: float, b3: 'SparseGradient', a4: float, b4: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['SparseGradient'], jpype.JArray]) -> 'SparseGradient':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a (double[]): Factors.
            b (SparseGradient[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: 'SparseGradient', b1: 'SparseGradient', a2: 'SparseGradient', b2: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, a1: 'SparseGradient', b1: 'SparseGradient', a2: 'SparseGradient', b2: 'SparseGradient', a3: 'SparseGradient', b3: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, a1: 'SparseGradient', b1: 'SparseGradient', a2: 'SparseGradient', b2: 'SparseGradient', a3: 'SparseGradient', b3: 'SparseGradient', a4: 'SparseGradient', b4: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['SparseGradient'], jpype.JArray], b: typing.Union[typing.List['SparseGradient'], jpype.JArray]) -> 'SparseGradient': ...
    @typing.overload
    def multiply(self, a: float) -> 'SparseGradient':
        """
        Compute this × a.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (SparseGradient): element to multiply
        
        Returns:
            a new element representing this × a
        
        '×' operator.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            c (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \]
        
        Specified by: multiply in interface CalculusFieldElement
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'SparseGradient': ...
    @typing.overload
    def multiply(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def multiplyInPlace(self, a: 'SparseGradient') -> None:
        """
        Multiply in place.
        
        This method is designed to be faster when used multiple times in a loop.
        
        The instance is changed here, in order to not change the instance the add method should be used.
        
        Parameters:
            a (SparseGradient): instance to multiply
        
        
        """
        ...
    def negate(self) -> 'SparseGradient':
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, v: float) -> 'SparseGradient':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            v (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, p: org.hipparchus.CalculusFieldElement) -> org.hipparchus.CalculusFieldElement:
        """
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        Compute a :sup:`x` where a is a double and x a SparseGradient
        
        Parameters:
            a (double): number to exponentiate
            x (SparseGradient): power to apply
        
        Returns:
            a :sup:`x`
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'SparseGradient': ...
    @typing.overload
    def pow(self, int: int) -> 'SparseGradient': ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def remainder(self, a: float) -> 'SparseGradient':
        """
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Specified by: remainder in interface Derivative
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (SparseGradient): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: 'SparseGradient') -> 'SparseGradient': ...
    def scalb(self, n: int) -> 'SparseGradient':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sqrt(self) -> 'SparseGradient':
        """
        Square root.
        
        Specified by: sqrt in interface CalculusFieldElement
        
        Specified by: sqrt in interface Derivative1
        
        Returns:
            square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this - a.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            a (SparseGradient): element to subtract
        
        Returns:
            a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: 'SparseGradient') -> 'SparseGradient': ...
    def taylor(self, *delta: float) -> float:
        """
        Evaluate Taylor expansion of a sparse gradient.
        
        Parameters:
            delta (double...): parameters offsets (Δx, Δy...)
        
        Returns:
            value of the Taylor expansion at x + Δx, y + Δy...
        
        
        """
        ...
    def toDegrees(self) -> 'SparseGradient':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'SparseGradient':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, v: float) -> 'SparseGradient':
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface Derivative
        
        Parameters:
            v (double): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

class UnivariateDerivative1(UnivariateDerivative['UnivariateDerivative1'], Derivative1['UnivariateDerivative1']):
    """
    Class representing both the value and the differentials of a function.
    
    This class is a stripped-down version of DerivativeStructure with only one getFreeParameters and getOrder also limited to one. It should have less overhead than DerivativeStructure in its domain.
    
    This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function.
    
    UnivariateDerivative1 instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.7
    
    Also see:
        DerivativeStructure,
        UnivariateDerivative2,
        Gradient,
        FieldDerivativeStructure,
        FieldUnivariateDerivative1,
        FieldUnivariateDerivative2,
        FieldGradient, serialized
    """
    PI: typing.ClassVar['UnivariateDerivative1'] = ...
    """
    The constant value of π as a UnivariateDerivative1.
    
    Since:
        2.0
    
    
    """
    @typing.overload
    def __init__(self, f0: float, f1: float): ...
    @typing.overload
    def __init__(self, ds: DerivativeStructure): ...
    def abs(self) -> 'UnivariateDerivative1':
        """
        absolute value.
        
        Specified by: abs in interface CalculusFieldElement
        
        Returns:
            abs(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this + a.
        
        Specified by: add in interface FieldElement
        
        Parameters:
            a (UnivariateDerivative1): element to add
        
        Returns:
            a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, a: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def atan2(self, x: 'UnivariateDerivative1') -> 'UnivariateDerivative1':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Specified by: atan2 in interface CalculusFieldElement
        
        Parameters:
            x (UnivariateDerivative1): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def compareTo(self, o: 'UnivariateDerivative1') -> int:
        """
        Comparison performed considering that derivatives are intrinsically linked to monomials in the corresponding Taylor expansion and that the higher the degree, the smaller the term.
        
        Specified by: meth:`~org.hipparchus.analysis.differentiation.https:.docs.oracle.com.javase.8.docs.api.java.lang.Comparable.html?is` in interface Comparable
        
        Since:
            3.0
        
        
        """
        ...
    @typing.overload
    def compose(self, ff0: float, ff1: float) -> 'UnivariateDerivative1':
        """
        Compute composition of the instance by a univariate function differentiable at order 1.
        
        Specified by: compose in interface Derivative1
        
        Parameters:
            ff0 (double): value of function
            ff1 (double): first-order derivative
        
        Returns:
            f(this)
        
        
        """
        ...
    @typing.overload
    def compose(self, *f: float) -> 'UnivariateDerivative1':
        """
        Compute composition of the instance by a univariate function.
        
        Specified by: compose in interface Derivative
        
        Parameters:
            f (double...): array of value and derivatives of the function at the current point (i.e.
                [f(getValue),
                f'(getValue),
                f''(getValue)...]).
        
        Returns:
            f(this)
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'UnivariateDerivative1':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (UnivariateDerivative1): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Specified by: copySign in interface CalculusFieldElement
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def divide(self, a: float) -> 'UnivariateDerivative1':
        """
        '÷' operator.
        
        Specified by: divide in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        Compute this ÷ a.
        
        Specified by: divide in interface CalculusFieldElement
        
        Specified by: divide in interface FieldElement
        
        Parameters:
            a (UnivariateDerivative1): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, a: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two univariate derivatives.
        
        univariate derivatives are considered equal if they have the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two univariate derivatives are equal
        
        
        """
        ...
    def getAddendum(self) -> 'UnivariateDerivative1':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Specified by: getAddendum in interface CalculusFieldElement
        
        Returns:
            real value
        
        
        """
        ...
    def getDerivative(self, n: int) -> float:
        """
        Get a derivative from the univariate derivative.
        
        Specified by: getDerivative in class UnivariateDerivative
        
        Parameters:
            n (int): derivation order (must be between 0 and getOrder,
                both inclusive)
        
        Returns:
            n :sup:`th` derivative
        
        
        """
        ...
    def getField(self) -> UnivariateDerivative1Field:
        """
        Get the Field to which the instance belongs.
        
        Specified by: getField in interface FieldElement
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFirstDerivative(self) -> float:
        """
        Get the first derivative.
        
        Returns:
            first derivative
        
        Also see:
            getValue
        
        
        """
        ...
    def getPi(self) -> 'UnivariateDerivative1':
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Specified by: getPi in interface CalculusFieldElement
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get the value part of the function.
        
        Specified by: getValue in interface Derivative
        
        Returns:
            value part of the value of the function
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the univariate derivative.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def hypot(self, y: 'UnivariateDerivative1') -> 'UnivariateDerivative1':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        Specified by: hypot in interface CalculusFieldElement
        
        Parameters:
            y (UnivariateDerivative1): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'UnivariateDerivative1', a2: float, b2: 'UnivariateDerivative1') -> 'UnivariateDerivative1':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (UnivariateDerivative1): first factor of the first term
            b1 (UnivariateDerivative1): second factor of the first term
            a2 (UnivariateDerivative1): first factor of the second term
            b2 (UnivariateDerivative1): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (UnivariateDerivative1): second factor of the first term
            a2 (double): first factor of the second term
            b2 (UnivariateDerivative1): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (UnivariateDerivative1): first factor of the first term
            b1 (UnivariateDerivative1): second factor of the first term
            a2 (UnivariateDerivative1): first factor of the second term
            b2 (UnivariateDerivative1): second factor of the second term
            a3 (UnivariateDerivative1): first factor of the third term
            b3 (UnivariateDerivative1): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (UnivariateDerivative1): second factor of the first term
            a2 (double): first factor of the second term
            b2 (UnivariateDerivative1): second factor of the second term
            a3 (double): first factor of the third term
            b3 (UnivariateDerivative1): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (UnivariateDerivative1): first factor of the first term
            b1 (UnivariateDerivative1): second factor of the first term
            a2 (UnivariateDerivative1): first factor of the second term
            b2 (UnivariateDerivative1): second factor of the second term
            a3 (UnivariateDerivative1): first factor of the third term
            b3 (UnivariateDerivative1): second factor of the third term
            a4 (UnivariateDerivative1): first factor of the fourth term
            b4 (UnivariateDerivative1): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (UnivariateDerivative1): second factor of the first term
            a2 (double): first factor of the second term
            b2 (UnivariateDerivative1): second factor of the second term
            a3 (double): first factor of the third term
            b3 (UnivariateDerivative1): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (UnivariateDerivative1): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'UnivariateDerivative1', a2: float, b2: 'UnivariateDerivative1', a3: float, b3: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'UnivariateDerivative1', a2: float, b2: 'UnivariateDerivative1', a3: float, b3: 'UnivariateDerivative1', a4: float, b4: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['UnivariateDerivative1'], jpype.JArray]) -> 'UnivariateDerivative1':
        """
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a (UnivariateDerivative1[]): Factors.
            b (UnivariateDerivative1[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        Compute a linear combination.
        
        Specified by: linearCombination in interface CalculusFieldElement
        
        Parameters:
            a (double[]): Factors.
            b (UnivariateDerivative1[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: 'UnivariateDerivative1', b1: 'UnivariateDerivative1', a2: 'UnivariateDerivative1', b2: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, a1: 'UnivariateDerivative1', b1: 'UnivariateDerivative1', a2: 'UnivariateDerivative1', b2: 'UnivariateDerivative1', a3: 'UnivariateDerivative1', b3: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, a1: 'UnivariateDerivative1', b1: 'UnivariateDerivative1', a2: 'UnivariateDerivative1', b2: 'UnivariateDerivative1', a3: 'UnivariateDerivative1', b3: 'UnivariateDerivative1', a4: 'UnivariateDerivative1', b4: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['UnivariateDerivative1'], jpype.JArray], b: typing.Union[typing.List['UnivariateDerivative1'], jpype.JArray]) -> 'UnivariateDerivative1': ...
    @typing.overload
    def multiply(self, n: float) -> 'UnivariateDerivative1':
        """
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \]
        
        Specified by: multiply in interface CalculusFieldElement
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        '×' operator.
        
        Specified by: multiply in interface CalculusFieldElement
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        Compute this × a.
        
        Specified by: multiply in interface FieldElement
        
        Parameters:
            a (UnivariateDerivative1): element to multiply
        
        Returns:
            a new element representing this × a
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'UnivariateDerivative1': ...
    @typing.overload
    def multiply(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def negate(self) -> 'UnivariateDerivative1':
        """
        Returns the additive inverse of this element.
        
        Specified by: negate in interface FieldElement
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, value: float) -> 'UnivariateDerivative1':
        """
        Create an instance corresponding to a constant real value.
        
        Specified by: newInstance in interface CalculusFieldElement
        
        Parameters:
            value (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, t: org.hipparchus.CalculusFieldElement) -> org.hipparchus.CalculusFieldElement:
        """
        Compute a :sup:`x` where a is a double and x a UnivariateDerivative1
        
        Parameters:
            a (double): number to exponentiate
            x (UnivariateDerivative1): power to apply
        
        Returns:
            a :sup:`x`
        
        Power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            p (double): power to apply
        
        Returns:
            this :sup:`p`
        
        Integer power operation.
        
        Specified by: pow in interface CalculusFieldElement
        
        Parameters:
            n (int): power to apply
        
        Returns:
            this :sup:`n`
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'UnivariateDerivative1': ...
    @typing.overload
    def pow(self, int: int) -> 'UnivariateDerivative1': ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def remainder(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        IEEE remainder operator.
        
        Specified by: remainder in interface CalculusFieldElement
        
        Parameters:
            a (UnivariateDerivative1): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def scalb(self, n: int) -> 'UnivariateDerivative1':
        """
        Multiply the instance by a power of 2.
        
        Specified by: scalb in interface CalculusFieldElement
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this - a.
        
        Specified by: subtract in interface CalculusFieldElement
        
        Specified by: subtract in interface FieldElement
        
        Parameters:
            a (UnivariateDerivative1): element to subtract
        
        Returns:
            a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def taylor(self, delta: float) -> float:
        """
        Evaluate Taylor expansion a univariate derivative.
        
        Parameters:
            delta (double): parameter offset Δx
        
        Returns:
            value of the Taylor expansion at x + Δx
        
        
        """
        ...
    def toDegrees(self) -> 'UnivariateDerivative1':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Specified by: toDegrees in interface CalculusFieldElement
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
        Convert the instance to a DerivativeStructure.
        
        Specified by: toDerivativeStructure in class UnivariateDerivative
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'UnivariateDerivative1':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Specified by: toRadians in interface CalculusFieldElement
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, value: float) -> 'UnivariateDerivative1':
        """
        Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Specified by: withValue in interface Derivative
        
        Parameters:
            value (double): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...

class UnivariateDerivative2(UnivariateDerivative['UnivariateDerivative2']):
    """
    Class representing both the value and the differentials of a function.
    
    This class is a stripped-down version of DerivativeStructure with only one getFreeParameters and getOrder also limited to two. It should have less overhead than DerivativeStructure in its domain.
    
    This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout mathematical expressions; they hold the derivative together with the value of a function.
    
    UnivariateDerivative2 instances can be used directly thanks to the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
    Implementing complex expressions by hand using Derivative-based classes (or in fact any CalculusFieldElement class) is a tedious and error-prone task but has the advantage of not requiring users to compute the derivatives by themselves and allowing to switch for one derivative implementation to another as they all share the same filed API.
    
    Instances of this class are guaranteed to be immutable.
    
    Since:
        1.7
    
    Also see:
        DerivativeStructure,
        UnivariateDerivative2,
        Gradient,
        FieldDerivativeStructure,
        FieldUnivariateDerivative2,
        FieldUnivariateDerivative2,
        FieldGradient, serialized
    """
    PI: typing.ClassVar['UnivariateDerivative2'] = ...
    """
    The constant value of π as a UnivariateDerivative2.
    
    Since:
        2.0
    
    
    """
    @typing.overload
    def __init__(self, f0: float, f1: float, f2: float): ...
    @typing.overload
    def __init__(self, ds: DerivativeStructure): ...
    def abs(self) -> 'UnivariateDerivative2':
        """
        absolute value.
        
        Returns:
            abs(this)
        
        
        """
        ...
    def acos(self) -> 'UnivariateDerivative2':
        """
        Arc cosine operation.
        
        Returns:
            acos(this)
        
        
        """
        ...
    def acosh(self) -> 'UnivariateDerivative2':
        """
        Inverse hyperbolic cosine operation.
        
        Returns:
            acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this + a.
        
        Parameters:
            a (UnivariateDerivative2): element to add
        
        Returns:
            a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, a: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def asin(self) -> 'UnivariateDerivative2':
        """
        Arc sine operation.
        
        Returns:
            asin(this)
        
        
        """
        ...
    def asinh(self) -> 'UnivariateDerivative2':
        """
        Inverse hyperbolic sine operation.
        
        Returns:
            asin(this)
        
        
        """
        ...
    def atan(self) -> 'UnivariateDerivative2':
        """
        Arc tangent operation.
        
        Returns:
            atan(this)
        
        
        """
        ...
    def atan2(self, x: 'UnivariateDerivative2') -> 'UnivariateDerivative2':
        """
        Two arguments arc tangent operation.
        
        Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with arguments order, the instance is the first argument and the single provided argument is the second argument. In order to be consistent with programming languages atan2, this method computes atan2(this, x), i.e. the instance represents the y argument and the x argument is the one passed as a single argument. This may seem confusing especially for users of Wolfram alpha, as this site is not consistent with programming languages atan2 two-arguments arc tangent and puts x as its first argument.
        
        Parameters:
            x (UnivariateDerivative2): second argument of the arc tangent
        
        Returns:
            atan2(this, x)
        
        
        """
        ...
    def atanh(self) -> 'UnivariateDerivative2':
        """
        Inverse hyperbolic tangent operation.
        
        Returns:
            atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'UnivariateDerivative2':
        """
        Cubic root.
        
        Returns:
            cubic root of the instance
        
        
        """
        ...
    def compareTo(self, o: 'UnivariateDerivative2') -> int:
        """
        Comparison performed considering that derivatives are intrinsically linked to monomials in the corresponding Taylor expansion and that the higher the degree, the smaller the term.
        
        Since:
            3.0
        
        
        """
        ...
    def compose(self, *f: float) -> 'UnivariateDerivative2':
        """
        Compute composition of the instance by a univariate function.
        
        Parameters:
            f (double...): array of value and derivatives of the function at the current point (i.e.
                [f(getValue),
                f'(getValue),
                f''(getValue)...]).
        
        Returns:
            f(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: float) -> 'UnivariateDerivative2':
        """
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Parameters:
            sign (UnivariateDerivative2): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        Returns the instance with the sign of the argument. A NaN sign argument is treated as positive.
        
        Parameters:
            sign (double): the sign for the returned value
        
        Returns:
            the instance with the same sign as the sign argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sign: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def cos(self) -> 'UnivariateDerivative2':
        """
        Cosine operation.
        
        Returns:
            cos(this)
        
        
        """
        ...
    def cosh(self) -> 'UnivariateDerivative2':
        """
        Hyperbolic cosine operation.
        
        Returns:
            cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, a: float) -> 'UnivariateDerivative2':
        """
        '÷' operator.
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this÷a
        
        Compute this ÷ a.
        
        Parameters:
            a (UnivariateDerivative2): element to divide by
        
        Returns:
            a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, a: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two univariate derivatives.
        
        univariate derivatives are considered equal if they have the same derivatives.
        
        Overrides: Object in class Object
        
        Parameters:
            other (Object): Object to test for equality to this
        
        Returns:
            true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'UnivariateDerivative2':
        """
        Exponential.
        
        Returns:
            exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'UnivariateDerivative2':
        """
        Exponential minus 1.
        
        Returns:
            exponential minus one of the instance
        
        
        """
        ...
    def getAddendum(self) -> 'UnivariateDerivative2':
        """
        Get the addendum to the real value of the number.
        
        The addendum is considered to be the part that when added back to the getReal recovers the instance. This means that when getReal() is finite (i.e. neither infinite nor NaN), then getReal()) is e and getReal()) is getAddendum(). Beware that for non-finite numbers, these two equalities may not hold. The first equality (with the addition), always holds even for infinity and NaNs if the real part is independent of the addendum (this is the case for all derivatives types, as well as for complex and Dfp, but it is not the case for Tuple and FieldTuple). The second equality (with the subtraction), generally doesn't hold for non-finite numbers, because the subtraction generates NaNs.
        
        Returns:
            real value
        
        
        """
        ...
    def getDerivative(self, n: int) -> float:
        """
        Get a derivative from the univariate derivative.
        
        Specified by: getDerivative in class UnivariateDerivative
        
        Parameters:
            n (int): derivation order (must be between 0 and getOrder,
                both inclusive)
        
        Returns:
            n :sup:`th` derivative
        
        
        """
        ...
    def getField(self) -> UnivariateDerivative2Field:
        """
        Get the Field to which the instance belongs.
        
        Returns:
            Field to which the instance belongs
        
        
        """
        ...
    def getFirstDerivative(self) -> float:
        """
        Get the first derivative.
        
        Returns:
            first derivative
        
        Also see:
            getValue,
            getSecondDerivative
        
        
        """
        ...
    def getOrder(self) -> int:
        """
        Get the maximum derivation order.
        
        Returns:
            maximum derivation order
        
        
        """
        ...
    def getPi(self) -> 'UnivariateDerivative2':
        """
        Get the Archimedes constant π.
        
        Archimedes constant is the ratio of a circle's circumference to its diameter.
        
        Returns:
            Archimedes constant π
        
        
        """
        ...
    def getSecondDerivative(self) -> float:
        """
        Get the second derivative.
        
        Returns:
            second derivative
        
        Also see:
            getValue,
            getFirstDerivative
        
        
        """
        ...
    def getValue(self) -> float:
        """
        Get the value part of the function.
        
        Returns:
            value part of the value of the function
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the univariate derivative.
        
        Overrides: Object in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def hypot(self, y: 'UnivariateDerivative2') -> 'UnivariateDerivative2':
        """
        Returns the hypotenuse of a triangle with sides this and y - sqrt(this :sup:`2`  +y :sup:`2` ) avoiding intermediate overflow or underflow.
        
          - If either argument is infinite, then the result is positive infinity.
          - else, if either argument is NaN then the result is NaN.
        
        
        Parameters:
            y (UnivariateDerivative2): a value
        
        Returns:
            sqrt(this :sup:`2`  +y :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'UnivariateDerivative2', a2: float, b2: 'UnivariateDerivative2') -> 'UnivariateDerivative2':
        """
        Compute a linear combination.
        
        Parameters:
            a1 (UnivariateDerivative2): first factor of the first term
            b1 (UnivariateDerivative2): second factor of the first term
            a2 (UnivariateDerivative2): first factor of the second term
            b2 (UnivariateDerivative2): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (UnivariateDerivative2): second factor of the first term
            a2 (double): first factor of the second term
            b2 (UnivariateDerivative2): second factor of the second term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Parameters:
            a1 (UnivariateDerivative2): first factor of the first term
            b1 (UnivariateDerivative2): second factor of the first term
            a2 (UnivariateDerivative2): first factor of the second term
            b2 (UnivariateDerivative2): second factor of the second term
            a3 (UnivariateDerivative2): first factor of the third term
            b3 (UnivariateDerivative2): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (UnivariateDerivative2): second factor of the first term
            a2 (double): first factor of the second term
            b2 (UnivariateDerivative2): second factor of the second term
            a3 (double): first factor of the third term
            b3 (UnivariateDerivative2): second factor of the third term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Parameters:
            a1 (UnivariateDerivative2): first factor of the first term
            b1 (UnivariateDerivative2): second factor of the first term
            a2 (UnivariateDerivative2): first factor of the second term
            b2 (UnivariateDerivative2): second factor of the second term
            a3 (UnivariateDerivative2): first factor of the third term
            b3 (UnivariateDerivative2): second factor of the third term
            a4 (UnivariateDerivative2): first factor of the fourth term
            b4 (UnivariateDerivative2): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        Compute a linear combination.
        
        Parameters:
            a1 (double): first factor of the first term
            b1 (UnivariateDerivative2): second factor of the first term
            a2 (double): first factor of the second term
            b2 (UnivariateDerivative2): second factor of the second term
            a3 (double): first factor of the third term
            b3 (UnivariateDerivative2): second factor of the third term
            a4 (double): first factor of the fourth term
            b4 (UnivariateDerivative2): second factor of the fourth term
        
        Returns:
            a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
        Also see:
            linearCombination,
            linearCombination
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'UnivariateDerivative2', a2: float, b2: 'UnivariateDerivative2', a3: float, b3: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, a1: float, b1: 'UnivariateDerivative2', a2: float, b2: 'UnivariateDerivative2', a3: float, b3: 'UnivariateDerivative2', a4: float, b4: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List[float], jpype.JArray], b: typing.Union[typing.List['UnivariateDerivative2'], jpype.JArray]) -> 'UnivariateDerivative2':
        """
        Compute a linear combination.
        
        Parameters:
            a (UnivariateDerivative2[]): Factors.
            b (UnivariateDerivative2[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        Compute a linear combination.
        
        Parameters:
            a (double[]): Factors.
            b (UnivariateDerivative2[]): Factors.
        
        Returns:
            i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, a1: 'UnivariateDerivative2', b1: 'UnivariateDerivative2', a2: 'UnivariateDerivative2', b2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, a1: 'UnivariateDerivative2', b1: 'UnivariateDerivative2', a2: 'UnivariateDerivative2', b2: 'UnivariateDerivative2', a3: 'UnivariateDerivative2', b3: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, a1: 'UnivariateDerivative2', b1: 'UnivariateDerivative2', a2: 'UnivariateDerivative2', b2: 'UnivariateDerivative2', a3: 'UnivariateDerivative2', b3: 'UnivariateDerivative2', a4: 'UnivariateDerivative2', b4: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, a: typing.Union[typing.List['UnivariateDerivative2'], jpype.JArray], b: typing.Union[typing.List['UnivariateDerivative2'], jpype.JArray]) -> 'UnivariateDerivative2': ...
    def log(self) -> 'UnivariateDerivative2':
        """
        Natural logarithm.
        
        Returns:
            logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'UnivariateDerivative2':
        """
        Base 10 logarithm.
        
        Returns:
            base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'UnivariateDerivative2':
        """
        Shifted natural logarithm.
        
        Returns:
            logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, n: float) -> 'UnivariateDerivative2':
        """
        Compute n × this. Multiplication by an integer number is defined as the following sum \[ n \times \mathrm{this} = \sum_{i=1}^n \mathrm{this} \]
        
        Parameters:
            n (int): Number of times this must be added to itself.
        
        Returns:
            A new element representing n × this.
        
        '×' operator.
        
        Parameters:
            a (double): right hand side parameter of the operator
        
        Returns:
            this×a
        
        Compute this × a.
        
        Parameters:
            a (UnivariateDerivative2): element to multiply
        
        Returns:
            a new element representing this × a
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'UnivariateDerivative2': ...
    @typing.overload
    def multiply(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def negate(self) -> 'UnivariateDerivative2':
        """
        Returns the additive inverse of this element.
        
        Returns:
            the opposite of this.
        
        
        """
        ...
    def newInstance(self, value: float) -> 'UnivariateDerivative2':
        """
        Create an instance corresponding to a constant real value.
        
        Parameters:
            value (double): constant real value
        
        Returns:
            instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, t: org.hipparchus.CalculusFieldElement) -> org.hipparchus.CalculusFieldElement:
        """
        Compute a :sup:`x` where a is a double and x a UnivariateDerivative2
        
        Parameters:
            a (double): number to exponentiate
            x (UnivariateDerivative2): power to apply
        
        Returns:
            a :sup:`x`
        
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
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'UnivariateDerivative2': ...
    @typing.overload
    def pow(self, int: int) -> 'UnivariateDerivative2': ...
    @typing.overload
    @staticmethod
    def pow(a: float, x: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def reciprocal(self) -> 'UnivariateDerivative2':
        """
        Returns the multiplicative inverse of this element.
        
        Returns:
            the inverse of this.
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        IEEE remainder operator.
        
        Parameters:
            a (UnivariateDerivative2): right hand side parameter of the operator
        
        Returns:
            this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, a: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def rootN(self, n: int) -> 'UnivariateDerivative2':
        """
        N :sup:`th` root.
        
        Parameters:
            n (int): order of the root
        
        Returns:
            n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, n: int) -> 'UnivariateDerivative2':
        """
        Multiply the instance by a power of 2.
        
        Parameters:
            n (int): power of 2
        
        Returns:
            this × 2 :sup:`n`
        
        
        """
        ...
    def sin(self) -> 'UnivariateDerivative2':
        """
        Sine operation.
        
        Returns:
            sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['UnivariateDerivative2']:
        """
        Combined Sine and Cosine operation.
        
        Returns:
            [sin(this), cos(this)]
        
        
        """
        ...
    def sinh(self) -> 'UnivariateDerivative2':
        """
        Hyperbolic sine operation.
        
        Returns:
            sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['UnivariateDerivative2']:
        """
        Combined hyperbolic sine and cosine operation.
        
        Returns:
            [sinh(this), cosh(this)]
        
        
        """
        ...
    def sqrt(self) -> 'UnivariateDerivative2':
        """
        Square root.
        
        Returns:
            square root of the instance
        
        
        """
        ...
    def square(self) -> 'UnivariateDerivative2':
        """
        Compute this × this.
        
        Returns:
            a new element representing this × this
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: float) -> org.hipparchus.CalculusFieldElement:
        """
        Compute this - a.
        
        Parameters:
            a (UnivariateDerivative2): element to subtract
        
        Returns:
            a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, a: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def tan(self) -> 'UnivariateDerivative2':
        """
        Tangent operation.
        
        Returns:
            tan(this)
        
        
        """
        ...
    def tanh(self) -> 'UnivariateDerivative2':
        """
        Hyperbolic tangent operation.
        
        Returns:
            tanh(this)
        
        
        """
        ...
    def taylor(self, delta: float) -> float:
        """
        Evaluate Taylor expansion a univariate derivative.
        
        Parameters:
            delta (double): parameter offset Δx
        
        Returns:
            value of the Taylor expansion at x + Δx
        
        
        """
        ...
    def toDegrees(self) -> 'UnivariateDerivative2':
        """
        Convert radians to degrees, with error of less than 0.5 ULP
        
        Returns:
            instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
        Convert the instance to a DerivativeStructure.
        
        Specified by: toDerivativeStructure in class UnivariateDerivative
        
        Returns:
            derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'UnivariateDerivative2':
        """
        Convert degrees to radians, with error of less than 0.5 ULP
        
        Returns:
            instance converted into radians
        
        
        """
        ...
    def withValue(self, value: float) -> 'UnivariateDerivative2':
        """
        Description copied from interface: withValue Create a new object with new value (zeroth-order derivative, as passed as input) and same derivatives of order one and above.
        
        This default implementation is there so that no API gets broken by the next release, which is not a major one. Custom inheritors should probably overwrite it.
        
        Parameters:
            value (double): zeroth-order derivative of new represented function
        
        Returns:
            new object with changed value
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.differentiation")``.

    DSCompiler: typing.Type[DSCompiler]
    DSFactory: typing.Type[DSFactory]
    Derivative: typing.Type[Derivative]
    Derivative1: typing.Type[Derivative1]
    DerivativeStructure: typing.Type[DerivativeStructure]
    DifferentialAlgebra: typing.Type[DifferentialAlgebra]
    FDSFactory: typing.Type[FDSFactory]
    FieldDerivative: typing.Type[FieldDerivative]
    FieldDerivative1: typing.Type[FieldDerivative1]
    FieldDerivativeStructure: typing.Type[FieldDerivativeStructure]
    FieldGradient: typing.Type[FieldGradient]
    FieldGradientField: typing.Type[FieldGradientField]
    FieldTaylorMap: typing.Type[FieldTaylorMap]
    FieldUnivariateDerivative: typing.Type[FieldUnivariateDerivative]
    FieldUnivariateDerivative1: typing.Type[FieldUnivariateDerivative1]
    FieldUnivariateDerivative1Field: typing.Type[FieldUnivariateDerivative1Field]
    FieldUnivariateDerivative2: typing.Type[FieldUnivariateDerivative2]
    FieldUnivariateDerivative2Field: typing.Type[FieldUnivariateDerivative2Field]
    FiniteDifferencesDifferentiator: typing.Type[FiniteDifferencesDifferentiator]
    Gradient: typing.Type[Gradient]
    GradientField: typing.Type[GradientField]
    GradientFunction: typing.Type[GradientFunction]
    JacobianFunction: typing.Type[JacobianFunction]
    MultivariateDifferentiableFunction: typing.Type[MultivariateDifferentiableFunction]
    MultivariateDifferentiableVectorFunction: typing.Type[MultivariateDifferentiableVectorFunction]
    SparseGradient: typing.Type[SparseGradient]
    TaylorMap: typing.Type[TaylorMap]
    UnivariateDerivative: typing.Type[UnivariateDerivative]
    UnivariateDerivative1: typing.Type[UnivariateDerivative1]
    UnivariateDerivative1Field: typing.Type[UnivariateDerivative1Field]
    UnivariateDerivative2: typing.Type[UnivariateDerivative2]
    UnivariateDerivative2Field: typing.Type[UnivariateDerivative2Field]
    UnivariateDifferentiableFunction: typing.Type[UnivariateDifferentiableFunction]
    UnivariateDifferentiableMatrixFunction: typing.Type[UnivariateDifferentiableMatrixFunction]
    UnivariateDifferentiableVectorFunction: typing.Type[UnivariateDifferentiableVectorFunction]
    UnivariateFunctionDifferentiator: typing.Type[UnivariateFunctionDifferentiator]
    UnivariateMatrixFunctionDifferentiator: typing.Type[UnivariateMatrixFunctionDifferentiator]
    UnivariateVectorFunctionDifferentiator: typing.Type[UnivariateVectorFunctionDifferentiator]
