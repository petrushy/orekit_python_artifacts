import java.io
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.util
import typing



class DSCompiler:
    """
    public class DSCompiler extends Object
    
        Class holding "compiled" computation rules for derivative structures.
    
        This class implements the computation rules described in Dan Kalman's paper `Doubly Recursive Multivariate Automatic
        Differentiation <http://www1.american.edu/cas/mathstat/People/kalman/pdffiles/mmgautodiff.pdf>`, Mathematics Magazine,
        vol. 75, no. 3, June 2002. However, in order to avoid performances bottlenecks, the recursive rules are "compiled" once
        in an unfold form. This class does this recursion unrolling and stores the computation rules as simple loops with
        pre-computed indirection arrays.
    
        This class maps all derivative computation into single dimension arrays that hold the value and partial derivatives. The
        class does not hold these arrays, which remains under the responsibility of the caller. For each combination of number
        of free parameters and derivation order, only one compiler is necessary, and this compiler will be used to perform
        computations on all arrays provided to it, which can represent hundreds or thousands of different parameters kept
        together with all their partial derivatives.
    
        The arrays on which compilers operate contain only the partial derivatives together with the 0 :sup:`th` derivative,
        i.e. the value. The partial derivatives are stored in a compiler-specific order, which can be retrieved using methods
        :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeIndex` and
        :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeOrders`. The value is guaranteed to be
        stored as the first element (i.e. the
        :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeIndex` method returns 0 when called with
        0 for all derivation orders and :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeOrders`
        returns an array filled with 0 when called with 0 as the index).
    
        Note that the ordering changes with number of parameters and derivation order. For example given 2 parameters x and y,
        df/dy is stored at index 2 when derivation order is set to 1 (in this case the array has three elements: f, df/dx and
        df/dy). If derivation order is set to 2, then df/dy will be stored at index 3 (in this case the array has six elements:
        f, df/dx, df/dxdx, df/dy, df/dxdy and df/dydy).
    
        Given this structure, users can perform some simple operations like adding, subtracting or multiplying constants and
        negating the elements by themselves, knowing if they want to mutate their array or create a new array. These simple
        operations are not provided by the compiler. The compiler provides only the more complex operations between several
        arrays.
    
        This class is mainly used as the engine for scalar variable
        :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`. It can also be used directly to hold several
        variables in arrays for more complex data structures. User can for example store a vector of n variables depending on
        three x, y and z free parameters in one array as follows:
    
        .. code-block: java
        
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
         
    
        Then in another function, user can perform some operations on all elements stored in the single array, such as a simple
        product of all variables:
    
        .. code-block: java
        
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
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`
    """
    _acos_1__T = typing.TypeVar('_acos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acos(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute arc cosine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for arc cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def acos(self, tArray: typing.List[_acos_1__T], int: int, tArray2: typing.List[_acos_1__T], int2: int) -> None:
        """
            Compute arc cosine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for arc cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _acosh_1__T = typing.TypeVar('_acosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def acosh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute inverse hyperbolic cosine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for inverse hyperbolic cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def acosh(self, tArray: typing.List[_acosh_1__T], int: int, tArray2: typing.List[_acosh_1__T], int2: int) -> None:
        """
            Compute inverse hyperbolic cosine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for inverse hyperbolic cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _add_1__T = typing.TypeVar('_add_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def add(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
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
    def add(self, tArray: typing.List[_add_1__T], int: int, tArray2: typing.List[_add_1__T], int2: int, tArray3: typing.List[_add_1__T], int3: int) -> None:
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
    def asin(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute arc sine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for arc sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def asin(self, tArray: typing.List[_asin_1__T], int: int, tArray2: typing.List[_asin_1__T], int2: int) -> None:
        """
            Compute arc sine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for arc sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _asinh_1__T = typing.TypeVar('_asinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def asinh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute inverse hyperbolic sine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for inverse hyperbolic sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def asinh(self, tArray: typing.List[_asinh_1__T], int: int, tArray2: typing.List[_asinh_1__T], int2: int) -> None:
        """
            Compute inverse hyperbolic sine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for inverse hyperbolic sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _atan_1__T = typing.TypeVar('_atan_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atan(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute arc tangent of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for arc tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def atan(self, tArray: typing.List[_atan_1__T], int: int, tArray2: typing.List[_atan_1__T], int2: int) -> None:
        """
            Compute arc tangent of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for arc tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _atan2_1__T = typing.TypeVar('_atan2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atan2(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
        """
            Compute two arguments arc tangent of a derivative structure.
        
            Parameters:
                y (double[]): array holding the first operand
                yOffset (int): offset of the first operand in its array
                x (double[]): array holding the second operand
                xOffset (int): offset of the second operand in its array
                result (double[]): array where result must be stored (for two arguments arc tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def atan2(self, tArray: typing.List[_atan2_1__T], int: int, tArray2: typing.List[_atan2_1__T], int2: int, tArray3: typing.List[_atan2_1__T], int3: int) -> None:
        """
            Compute two arguments arc tangent of a derivative structure.
        
            Parameters:
                y (T[]): array holding the first operand
                yOffset (int): offset of the first operand in its array
                x (T[]): array holding the second operand
                xOffset (int): offset of the second operand in its array
                result (T[]): array where result must be stored (for two arguments arc tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _atanh_1__T = typing.TypeVar('_atanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atanh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute inverse hyperbolic tangent of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for inverse hyperbolic tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def atanh(self, tArray: typing.List[_atanh_1__T], int: int, tArray2: typing.List[_atanh_1__T], int2: int) -> None:
        """
            Compute inverse hyperbolic tangent of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for inverse hyperbolic tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    def checkCompatibility(self, dSCompiler: 'DSCompiler') -> None: ...
    _compose_1__T = typing.TypeVar('_compose_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _compose_2__T = typing.TypeVar('_compose_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def compose(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], doubleArray3: typing.List[float], int2: int) -> None:
        """
            Compute composition of a derivative structure by a function.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                f (double[]): array of value and derivatives of the function at the current point (i.e. at :code:`operand[operandOffset]`).
                result (double[]): array where result must be stored (for composition the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def compose(self, tArray: typing.List[_compose_1__T], int: int, doubleArray: typing.List[float], tArray2: typing.List[_compose_1__T], int2: int) -> None:
        """
            Compute composition of a derivative structure by a function.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                f (T[]): array of value and derivatives of the function at the current point (i.e. at :code:`operand[operandOffset]`).
                result (T[]): array where result must be stored (for composition the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute composition of a derivative structure by a function.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                f (double[]): array of value and derivatives of the function at the current point (i.e. at :code:`operand[operandOffset]`).
                result (T[]): array where result must be stored (for composition the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @typing.overload
    def compose(self, tArray: typing.List[_compose_2__T], int: int, tArray2: typing.List[_compose_2__T], tArray3: typing.List[_compose_2__T], int2: int) -> None: ...
    _cos_1__T = typing.TypeVar('_cos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def cos(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute cosine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def cos(self, tArray: typing.List[_cos_1__T], int: int, tArray2: typing.List[_cos_1__T], int2: int) -> None:
        """
            Compute cosine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _cosh_1__T = typing.TypeVar('_cosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def cosh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute hyperbolic cosine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for hyperbolic cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def cosh(self, tArray: typing.List[_cosh_1__T], int: int, tArray2: typing.List[_cosh_1__T], int2: int) -> None:
        """
            Compute hyperbolic cosine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for hyperbolic cosine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _divide_1__T = typing.TypeVar('_divide_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def divide(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
        """
            Perform division of two derivative structures.
        
            Parameters:
                lhs (double[]): array holding left hand side of division
                lhsOffset (int): offset of the left hand side in its array
                rhs (double[]): array right hand side of division
                rhsOffset (int): offset of the right hand side in its array
                result (double[]): array where result must be stored (for division the result array *cannot* be one of the input arrays)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def divide(self, tArray: typing.List[_divide_1__T], int: int, tArray2: typing.List[_divide_1__T], int2: int, tArray3: typing.List[_divide_1__T], int3: int) -> None:
        """
            Perform division of two derivative structures.
        
            Parameters:
                lhs (T[]): array holding left hand side of division
                lhsOffset (int): offset of the left hand side in its array
                rhs (T[]): array right hand side of division
                rhsOffset (int): offset of the right hand side in its array
                result (T[]): array where result must be stored (for division the result array *cannot* be one of the input arrays)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _exp_1__T = typing.TypeVar('_exp_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def exp(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute exponential of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for exponential the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def exp(self, tArray: typing.List[_exp_1__T], int: int, tArray2: typing.List[_exp_1__T], int2: int) -> None:
        """
            Compute exponential of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for exponential the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _expm1_1__T = typing.TypeVar('_expm1_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def expm1(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute exp(x) - 1 of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for exponential the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def expm1(self, tArray: typing.List[_expm1_1__T], int: int, tArray2: typing.List[_expm1_1__T], int2: int) -> None:
        """
            Compute exp(x) - 1 of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for exponential the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @staticmethod
    def getCompiler(int: int, int2: int) -> 'DSCompiler': ...
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
    def getPartialDerivativeIndex(self, intArray: typing.List[int]) -> int: ...
    def getPartialDerivativeOrders(self, int: int) -> typing.List[int]:
        """
            Get the derivation orders for a specific index in the array.
        
            This method is the inverse of :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeIndex`.
        
            Parameters:
                index (int): of the partial derivative
        
            Returns:
                orders derivation orders with respect to each parameter
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeIndex`
        
        
        """
        ...
    def getSize(self) -> int:
        """
            Get the array size required for holding partial derivatives data.
        
            This number includes the single 0 order derivative element, which is guaranteed to be stored in the first element of the
            array.
        
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
    def linearCombination(self, double: float, doubleArray: typing.List[float], int: int, double3: float, doubleArray2: typing.List[float], int2: int, double5: float, doubleArray3: typing.List[float], int3: int, double7: float, doubleArray4: typing.List[float], int4: int, doubleArray5: typing.List[float], int5: int) -> None:
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
    def linearCombination(self, double: float, doubleArray: typing.List[float], int: int, double3: float, doubleArray2: typing.List[float], int2: int, double5: float, doubleArray3: typing.List[float], int3: int, doubleArray4: typing.List[float], int4: int) -> None:
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
    def linearCombination(self, double: float, doubleArray: typing.List[float], int: int, double3: float, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
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
    def linearCombination(self, double: float, tArray: typing.List[_linearCombination_3__T], int: int, double2: float, tArray2: typing.List[_linearCombination_3__T], int2: int, double3: float, tArray3: typing.List[_linearCombination_3__T], int3: int, double4: float, tArray4: typing.List[_linearCombination_3__T], int4: int, tArray5: typing.List[_linearCombination_3__T], int5: int) -> None:
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
    def linearCombination(self, double: float, tArray: typing.List[_linearCombination_4__T], int: int, double2: float, tArray2: typing.List[_linearCombination_4__T], int2: int, double3: float, tArray3: typing.List[_linearCombination_4__T], int3: int, tArray4: typing.List[_linearCombination_4__T], int4: int) -> None:
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
    def linearCombination(self, double: float, tArray: typing.List[_linearCombination_5__T], int: int, double2: float, tArray2: typing.List[_linearCombination_5__T], int2: int, tArray3: typing.List[_linearCombination_5__T], int3: int) -> None:
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
    def linearCombination(self, t: _linearCombination_6__T, tArray: typing.List[_linearCombination_6__T], int: int, t3: _linearCombination_6__T, tArray2: typing.List[_linearCombination_6__T], int2: int, t5: _linearCombination_6__T, tArray3: typing.List[_linearCombination_6__T], int3: int, t7: _linearCombination_6__T, tArray4: typing.List[_linearCombination_6__T], int4: int, tArray5: typing.List[_linearCombination_6__T], int5: int) -> None: ...
    @typing.overload
    def linearCombination(self, t: _linearCombination_7__T, tArray: typing.List[_linearCombination_7__T], int: int, t3: _linearCombination_7__T, tArray2: typing.List[_linearCombination_7__T], int2: int, t5: _linearCombination_7__T, tArray3: typing.List[_linearCombination_7__T], int3: int, tArray4: typing.List[_linearCombination_7__T], int4: int) -> None: ...
    @typing.overload
    def linearCombination(self, t: _linearCombination_8__T, tArray: typing.List[_linearCombination_8__T], int: int, t3: _linearCombination_8__T, tArray2: typing.List[_linearCombination_8__T], int2: int, tArray3: typing.List[_linearCombination_8__T], int3: int) -> None: ...
    _log_1__T = typing.TypeVar('_log_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def log(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute natural logarithm of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for logarithm the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def log(self, tArray: typing.List[_log_1__T], int: int, tArray2: typing.List[_log_1__T], int2: int) -> None:
        """
            Compute natural logarithm of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for logarithm the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _log10_1__T = typing.TypeVar('_log10_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def log10(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Computes base 10 logarithm of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for base 10 logarithm the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def log10(self, tArray: typing.List[_log10_1__T], int: int, tArray2: typing.List[_log10_1__T], int2: int) -> None:
        """
            Computes base 10 logarithm of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for base 10 logarithm the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _log1p_1__T = typing.TypeVar('_log1p_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def log1p(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Computes shifted logarithm of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for shifted logarithm the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def log1p(self, tArray: typing.List[_log1p_1__T], int: int, tArray2: typing.List[_log1p_1__T], int2: int) -> None:
        """
            Computes shifted logarithm of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for shifted logarithm the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _multiply_1__T = typing.TypeVar('_multiply_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def multiply(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
        """
            Perform multiplication of two derivative structures.
        
            Parameters:
                lhs (double[]): array holding left hand side of multiplication
                lhsOffset (int): offset of the left hand side in its array
                rhs (double[]): array right hand side of multiplication
                rhsOffset (int): offset of the right hand side in its array
                result (double[]): array where result must be stored (for multiplication the result array *cannot* be one of the input arrays)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def multiply(self, tArray: typing.List[_multiply_1__T], int: int, tArray2: typing.List[_multiply_1__T], int2: int, tArray3: typing.List[_multiply_1__T], int3: int) -> None:
        """
            Perform multiplication of two derivative structures.
        
            Parameters:
                lhs (T[]): array holding left hand side of multiplication
                lhsOffset (int): offset of the left hand side in its array
                rhs (T[]): array right hand side of multiplication
                rhsOffset (int): offset of the right hand side in its array
                result (T[]): array where result must be stored (for multiplication the result array *cannot* be one of the input arrays)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _pow_1__T = typing.TypeVar('_pow_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_5__T = typing.TypeVar('_pow_5__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_6__T = typing.TypeVar('_pow_6__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _pow_7__T = typing.TypeVar('_pow_7__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, double: float, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute power of a double to a derivative structure.
        
            Parameters:
                a (double): number to exponentiate
                operand (double[]): array holding the power
                operandOffset (int): offset of the power in its array
                result (double[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute power of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                p (double): power to apply
                result (double[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute integer power of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                n (int): power to apply
                result (double[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute power of a derivative structure.
        
            Parameters:
                x (double[]): array holding the base
                xOffset (int): offset of the base in its array
                y (double[]): array holding the exponent
                yOffset (int): offset of the exponent in its array
                result (double[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def pow(self, double: float, tArray: typing.List[_pow_1__T], int: int, tArray2: typing.List[_pow_1__T], int2: int) -> None:
        """
            Compute power of a double to a derivative structure.
        
            Parameters:
                a (double): number to exponentiate
                operand (T[]): array holding the power
                operandOffset (int): offset of the power in its array
                result (T[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute power of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                p (double): power to apply
                result (T[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute integer power of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                n (int): power to apply
                result (T[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
            Compute power of a derivative structure.
        
            Parameters:
                x (T[]): array holding the base
                xOffset (int): offset of the base in its array
                y (T[]): array holding the exponent
                yOffset (int): offset of the exponent in its array
                result (T[]): array where result must be stored (for power the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    @typing.overload
    def pow(self, doubleArray: typing.List[float], int: int, double2: float, doubleArray2: typing.List[float], int2: int) -> None: ...
    @typing.overload
    def pow(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None: ...
    @typing.overload
    def pow(self, doubleArray: typing.List[float], int: int, int2: int, doubleArray2: typing.List[float], int3: int) -> None: ...
    @typing.overload
    def pow(self, tArray: typing.List[_pow_5__T], int: int, double: float, tArray2: typing.List[_pow_5__T], int2: int) -> None: ...
    @typing.overload
    def pow(self, tArray: typing.List[_pow_6__T], int: int, int2: int, tArray2: typing.List[_pow_6__T], int3: int) -> None: ...
    @typing.overload
    def pow(self, tArray: typing.List[_pow_7__T], int: int, tArray2: typing.List[_pow_7__T], int2: int, tArray3: typing.List[_pow_7__T], int3: int) -> None: ...
    _remainder_1__T = typing.TypeVar('_remainder_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def remainder(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
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
    def remainder(self, tArray: typing.List[_remainder_1__T], int: int, tArray2: typing.List[_remainder_1__T], int2: int, tArray3: typing.List[_remainder_1__T], int3: int) -> None:
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
    def rootN(self, doubleArray: typing.List[float], int: int, int2: int, doubleArray2: typing.List[float], int3: int) -> None:
        """
            Compute n :sup:`th` root of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                n (int): order of the root
                result (double[]): array where result must be stored (for n :sup:`th` root the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def rootN(self, tArray: typing.List[_rootN_1__T], int: int, int2: int, tArray2: typing.List[_rootN_1__T], int3: int) -> None:
        """
            Compute n :sup:`th` root of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                n (int): order of the root
                result (T[]): array where result must be stored (for n :sup:`th` root the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _sin_1__T = typing.TypeVar('_sin_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sin(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute sine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def sin(self, tArray: typing.List[_sin_1__T], int: int, tArray2: typing.List[_sin_1__T], int2: int) -> None:
        """
            Compute sine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _sinCos_1__T = typing.TypeVar('_sinCos_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sinCos(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
        """
            Compute combined sine and cosine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                sin (double[]): array where sine must be stored (for sine the result array *cannot* be the input array)
                sinOffset (int): offset of the result in its array
                cos (double[]): array where cosine must be stored (for cosine the result array *cannot* be the input array)
                cosOffset (int): offset of the result in its array
        
            Since:
                1.4
        
        """
        ...
    @typing.overload
    def sinCos(self, tArray: typing.List[_sinCos_1__T], int: int, tArray2: typing.List[_sinCos_1__T], int2: int, tArray3: typing.List[_sinCos_1__T], int3: int) -> None:
        """
            Compute combined sine and cosine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                sin (T[]): array where sine must be stored (for sine the result array *cannot* be the input array)
                sinOffset (int): offset of the result in its array
                cos (T[]): array where cosine must be stored (for cosine the result array *cannot* be the input array)
                cosOffset (int): offset of the result in its array
        
            Since:
                1.4
        
        
        """
        ...
    _sinh_1__T = typing.TypeVar('_sinh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sinh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute hyperbolic sine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for hyperbolic sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def sinh(self, tArray: typing.List[_sinh_1__T], int: int, tArray2: typing.List[_sinh_1__T], int2: int) -> None:
        """
            Compute hyperbolic sine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for hyperbolic sine the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _sinhCosh_1__T = typing.TypeVar('_sinhCosh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def sinhCosh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
        """
            Compute combined hyperbolic sine and cosine of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                sinh (double[]): array where hyperbolic sine must be stored (for sine the result array *cannot* be the input array)
                sinhOffset (int): offset of the result in its array
                cosh (double[]): array where hyperbolic *cannot* be the input array)
                coshOffset (int): offset of the result in its array
        
            Since:
                2.0
        
        """
        ...
    @typing.overload
    def sinhCosh(self, tArray: typing.List[_sinhCosh_1__T], int: int, tArray2: typing.List[_sinhCosh_1__T], int2: int, tArray3: typing.List[_sinhCosh_1__T], int3: int) -> None:
        """
            Compute combined hyperbolic sine and cosine of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                sinh (T[]): array where hyperbolic sine must be stored (for sine the result array *cannot* be the input array)
                sinhOffset (int): offset of the result in its array
                cosh (T[]): array where hyperbolic cosine must be stored (for cosine the result array *cannot* be the input array)
                coshOffset (int): offset of the result in its array
        
            Since:
                1.4
        
        
        """
        ...
    _subtract_1__T = typing.TypeVar('_subtract_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def subtract(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int, doubleArray3: typing.List[float], int3: int) -> None:
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
    def subtract(self, tArray: typing.List[_subtract_1__T], int: int, tArray2: typing.List[_subtract_1__T], int2: int, tArray3: typing.List[_subtract_1__T], int3: int) -> None:
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
    def tan(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute tangent of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def tan(self, tArray: typing.List[_tan_1__T], int: int, tArray2: typing.List[_tan_1__T], int2: int) -> None:
        """
            Compute tangent of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _tanh_1__T = typing.TypeVar('_tanh_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def tanh(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float], int2: int) -> None:
        """
            Compute hyperbolic tangent of a derivative structure.
        
            Parameters:
                operand (double[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (double[]): array where result must be stored (for hyperbolic tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        """
        ...
    @typing.overload
    def tanh(self, tArray: typing.List[_tanh_1__T], int: int, tArray2: typing.List[_tanh_1__T], int2: int) -> None:
        """
            Compute hyperbolic tangent of a derivative structure.
        
            Parameters:
                operand (T[]): array holding the operand
                operandOffset (int): offset of the operand in its array
                result (T[]): array where result must be stored (for hyperbolic tangent the result array *cannot* be the input array)
                resultOffset (int): offset of the result in its array
        
        
        """
        ...
    _taylor_1__T = typing.TypeVar('_taylor_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    _taylor_2__T = typing.TypeVar('_taylor_2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def taylor(self, doubleArray: typing.List[float], int: int, doubleArray2: typing.List[float]) -> float: ...
    @typing.overload
    def taylor(self, tArray: typing.List[_taylor_1__T], int: int, tArray2: typing.List[_taylor_1__T]) -> _taylor_1__T: ...
    @typing.overload
    def taylor(self, tArray: typing.List[_taylor_2__T], int: int, doubleArray: typing.List[float]) -> _taylor_2__T: ...

class DSFactory(java.io.Serializable):
    """
    public class DSFactory extends Object implements Serializable
    
        Factory for :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`.
    
        This class is a factory for :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` instances.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.1
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`, :meth:`~serialized`
    """
    def __init__(self, int: int, int2: int): ...
    def build(self, doubleArray: typing.List[float]) -> 'DerivativeStructure': ...
    def constant(self, double: float) -> 'DerivativeStructure':
        """
            Build a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` representing a constant value.
        
            Parameters:
                value (double): value of the constant
        
            Returns:
                a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` representing a constant value
        
        
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
            Get the :class:`~org.hipparchus.Field` the :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`
            instances belong to.
        
            Returns:
                :class:`~org.hipparchus.Field` the :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` instances
                belong to
        
        
        """
        ...
    def variable(self, int: int, double: float) -> 'DerivativeStructure': ...
    class DSField(org.hipparchus.Field['DerivativeStructure']):
        def equals(self, object: typing.Any) -> bool: ...
        def getOne(self) -> 'DerivativeStructure': ...
        def getPi(self) -> 'DerivativeStructure': ...
        def getRuntimeClass(self) -> typing.Type['DerivativeStructure']: ...
        def getZero(self) -> 'DerivativeStructure': ...
        def hashCode(self) -> int: ...

_Derivative__T = typing.TypeVar('_Derivative__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class Derivative(org.hipparchus.CalculusFieldElement[_Derivative__T], typing.Generic[_Derivative__T]):
    """
    public interface Derivative<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.CalculusFieldElement`<T>
    
        Interface representing both the value and the differentials of a function.
    
        Since:
            1.7
    """
    def compose(self, doubleArray: typing.List[float]) -> _Derivative__T: ...
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
    def getPartialDerivative(self, intArray: typing.List[int]) -> float: ...
    def getValue(self) -> float:
        """
            Get the value part of the function.
        
            Returns:
                value part of the value of the function
        
        
        """
        ...

_FDSFactory__DerivativeField__T = typing.TypeVar('_FDSFactory__DerivativeField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
_FDSFactory__T = typing.TypeVar('_FDSFactory__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FDSFactory(typing.Generic[_FDSFactory__T]):
    """
    public class FDSFactory<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Factory for :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`.
    
        This class is a factory for :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` instances.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`
    """
    def __init__(self, field: org.hipparchus.Field[_FDSFactory__T], int: int, int2: int): ...
    @typing.overload
    def build(self, tArray: typing.List[_FDSFactory__T]) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def build(self, doubleArray: typing.List[float]) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def constant(self, double: float) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def constant(self, t: _FDSFactory__T) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    def getCompiler(self) -> DSCompiler:
        """
            Get the compiler for the current dimensions.
        
            Returns:
                compiler for the current dimensions
        
        
        """
        ...
    def getDerivativeField(self) -> 'FDSFactory.DerivativeField'[_FDSFactory__T]: ...
    def getValueField(self) -> org.hipparchus.Field[_FDSFactory__T]: ...
    @typing.overload
    def variable(self, int: int, double: float) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    @typing.overload
    def variable(self, int: int, t: _FDSFactory__T) -> 'FieldDerivativeStructure'[_FDSFactory__T]: ...
    class DerivativeField(org.hipparchus.Field['FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]], typing.Generic[_FDSFactory__DerivativeField__T]):
        def equals(self, object: typing.Any) -> bool: ...
        def getOne(self) -> 'FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]: ...
        def getPi(self) -> 'FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]: ...
        def getRuntimeClass(self) -> typing.Type['FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]]: ...
        def getZero(self) -> 'FieldDerivativeStructure'[_FDSFactory__DerivativeField__T]: ...
        def hashCode(self) -> int: ...

_FieldDerivative__S = typing.TypeVar('_FieldDerivative__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
_FieldDerivative__T = typing.TypeVar('_FieldDerivative__T', bound='FieldDerivative')  # <T>
class FieldDerivative(org.hipparchus.CalculusFieldElement[_FieldDerivative__T], typing.Generic[_FieldDerivative__S, _FieldDerivative__T]):
    """
    public interface FieldDerivative<S extends :class:`~org.hipparchus.CalculusFieldElement`<S>,T extends FieldDerivative<S,T>> extends :class:`~org.hipparchus.CalculusFieldElement`<T>
    
        Interface representing both the value and the differentials of a function.
    
        Since:
            1.7
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
            Get the derivation order.
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPartialDerivative(self, intArray: typing.List[int]) -> _FieldDerivative__S: ...
    def getValue(self) -> _FieldDerivative__S:
        """
            Get the value part of the function.
        
            Returns:
                value part of the value of the function
        
        
        """
        ...

_FieldGradientField__T = typing.TypeVar('_FieldGradientField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGradientField(org.hipparchus.Field['FieldGradient'[_FieldGradientField__T]], typing.Generic[_FieldGradientField__T]):
    """
    public class FieldGradientField<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.analysis.differentiation.FieldGradient`<T>>
    
        Field for :class:`~org.hipparchus.analysis.differentiation.Gradient` instances.
    
        Since:
            1.7
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    _getField__T = typing.TypeVar('_getField__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getField(field: org.hipparchus.Field[_getField__T], int: int) -> 'FieldGradientField'[_getField__T]:
        """
            Get the field for number of free parameters.
        
            Parameters:
                valueField (:class:`~org.hipparchus.Field`<T> valueField): field for the function parameters and value
                parameters (int): number of free parameters
        
            Returns:
                cached field
        
        
        """
        ...
    def getOne(self) -> 'FieldGradient'[_FieldGradientField__T]: ...
    def getRuntimeClass(self) -> typing.Type['FieldGradient'[_FieldGradientField__T]]: ...
    def getZero(self) -> 'FieldGradient'[_FieldGradientField__T]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_FieldUnivariateDerivative1Field__T = typing.TypeVar('_FieldUnivariateDerivative1Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative1Field(org.hipparchus.Field['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]], typing.Generic[_FieldUnivariateDerivative1Field__T]):
    """
    public class FieldUnivariateDerivative1Field<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<T>>
    
        Field for :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1` instances.
    
        Since:
            1.7
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getOne(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]: ...
    def getRuntimeClass(self) -> typing.Type['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]]: ...
    _getUnivariateDerivative1Field__T = typing.TypeVar('_getUnivariateDerivative1Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getUnivariateDerivative1Field(field: org.hipparchus.Field[_getUnivariateDerivative1Field__T]) -> 'FieldUnivariateDerivative1Field'[_getUnivariateDerivative1Field__T]:
        """
            Get the univariate derivative field corresponding to a value field.
        
            Parameters:
                valueField (:class:`~org.hipparchus.Field`<T> valueField): field for the function parameters and value
        
            Returns:
                univariate derivative field
        
        
        """
        ...
    def getZero(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1Field__T]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

_FieldUnivariateDerivative2Field__T = typing.TypeVar('_FieldUnivariateDerivative2Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative2Field(org.hipparchus.Field['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]], typing.Generic[_FieldUnivariateDerivative2Field__T]):
    """
    public class FieldUnivariateDerivative2Field<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<T>>
    
        Field for :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2` instances.
    
        Since:
            1.7
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getOne(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]: ...
    def getRuntimeClass(self) -> typing.Type['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]]: ...
    _getUnivariateDerivative2Field__T = typing.TypeVar('_getUnivariateDerivative2Field__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def getUnivariateDerivative2Field(field: org.hipparchus.Field[_getUnivariateDerivative2Field__T]) -> 'FieldUnivariateDerivative2Field'[_getUnivariateDerivative2Field__T]:
        """
            Get the univariate derivative field corresponding to a value field.
        
            Parameters:
                valueField (:class:`~org.hipparchus.Field`<T> valueField): field for the function parameters and value
        
            Returns:
                univariate derivative field
        
        
        """
        ...
    def getZero(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2Field__T]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GradientField(org.hipparchus.Field['Gradient']):
    """
    public class GradientField extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.analysis.differentiation.Gradient`>
    
        Field for :class:`~org.hipparchus.analysis.differentiation.Gradient` instances.
    
        Since:
            1.7
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @staticmethod
    def getField(int: int) -> 'GradientField':
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
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a Ã— e :sub:`1` = e :sub:`1` Ã— a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['Gradient']: ...
    def getZero(self) -> 'Gradient':
        """
            Get the additive identity of the field.
        
            The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a
            + e :sub:`0` = e :sub:`0` + a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getZero` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class GradientFunction(org.hipparchus.analysis.MultivariateVectorFunction):
    """
    public class GradientFunction extends Object implements :class:`~org.hipparchus.analysis.MultivariateVectorFunction`
    
        Class representing the gradient of a multivariate function.
    
        The vectorial components of the function represent the derivatives with respect to each function parameters.
    """
    def __init__(self, multivariateDifferentiableFunction: 'MultivariateDifferentiableFunction'): ...
    def value(self, doubleArray: typing.List[float]) -> typing.List[float]:
        """
            Compute the value for the function at the given point.
        
            Specified by:
                 in interface :class:`~org.hipparchus.analysis.MultivariateVectorFunction`
        
            Parameters:
                point (double[]): point at which the function must be evaluated
        
            Returns:
                function value for the given point
        
        
        """
        ...

class JacobianFunction(org.hipparchus.analysis.MultivariateMatrixFunction):
    """
    public class JacobianFunction extends Object implements :class:`~org.hipparchus.analysis.MultivariateMatrixFunction`
    
        Class representing the Jacobian of a multivariate vector function.
    
        The rows iterate on the model functions while the columns iterate on the parameters; thus, the numbers of rows is equal
        to the dimension of the underlying function vector value and the number of columns is equal to the number of free
        parameters of the underlying function.
    """
    def __init__(self, multivariateDifferentiableVectorFunction: 'MultivariateDifferentiableVectorFunction'): ...
    def value(self, doubleArray: typing.List[float]) -> typing.List[typing.List[float]]:
        """
            Compute the value for the function at the given point.
        
            Specified by:
                 in interface :class:`~org.hipparchus.analysis.MultivariateMatrixFunction`
        
            Parameters:
                point (double[]): point at which the function must be evaluated
        
            Returns:
                function value for the given point
        
        
        """
        ...

class MultivariateDifferentiableFunction(org.hipparchus.analysis.MultivariateFunction):
    """
    public interface MultivariateDifferentiableFunction extends :class:`~org.hipparchus.analysis.MultivariateFunction`
    
        Extension of :class:`~org.hipparchus.analysis.MultivariateFunction` representing a multivariate differentiable real
        function.
    """
    @typing.overload
    def value(self, doubleArray: typing.List[float]) -> float: ...
    @typing.overload
    def value(self, derivativeStructureArray: typing.List['DerivativeStructure']) -> 'DerivativeStructure': ...

class MultivariateDifferentiableVectorFunction(org.hipparchus.analysis.MultivariateVectorFunction):
    """
    public interface MultivariateDifferentiableVectorFunction extends :class:`~org.hipparchus.analysis.MultivariateVectorFunction`
    
        Extension of :class:`~org.hipparchus.analysis.MultivariateVectorFunction` representing a multivariate differentiable
        vectorial function.
    """
    @typing.overload
    def value(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def value(self, derivativeStructureArray: typing.List['DerivativeStructure']) -> typing.List['DerivativeStructure']: ...

class SparseGradient(org.hipparchus.CalculusFieldElement['SparseGradient'], java.io.Serializable):
    """
    public class SparseGradient extends Object implements :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.analysis.differentiation.SparseGradient`>, Serializable
    
        First derivative computation with large number of variables.
    
        This class plays a similar role to :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`, with a focus
        on efficiency when dealing with large number of independent variables and most computation depend only on a few of them,
        and when only first derivative is desired. When these conditions are met, this class should be much faster than
        :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` and use less memory.
    
        Also see:
            :meth:`~serialized`
    """
    def abs(self) -> 'SparseGradient':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'SparseGradient':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'SparseGradient':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'SparseGradient':
        """
            Compute this + a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): element to add
        
            Returns:
                a new element representing this + a
        
            '+' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.add` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                c (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
        
        """
        ...
    @typing.overload
    def add(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def addInPlace(self, sparseGradient: 'SparseGradient') -> None:
        """
            Add in place.
        
            This method is designed to be faster when used multiple times in a loop.
        
            The instance is changed here, in order to not change the instance the
            :meth:`~org.hipparchus.analysis.differentiation.SparseGradient.add` method should be used.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): instance to add
        
        
        """
        ...
    def asin(self) -> 'SparseGradient':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'SparseGradient':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'SparseGradient':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    @typing.overload
    def atan2(self, sparseGradient: 'SparseGradient') -> 'SparseGradient':
        """
            Two arguments arc tangent operation.
        
            Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with
            arguments order, the instance is the *first* argument and the single provided argument is the *second* argument. In
            order to be consistent with programming languages :code:`atan2`, this method computes :code:`atan2(this, x)`, i.e. the
            instance represents the :code:`y` argument and the :code:`x` argument is the one passed as a single argument. This may
            seem confusing especially for users of Wolfram alpha, as this site is *not* consistent with programming languages
            :code:`atan2` two-arguments arc tangent and puts :code:`x` as its first argument.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan2` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second argument of the arc tangent
        
            Returns:
        public static :class:`~org.hipparchus.analysis.differentiation.SparseGradient` atan2(:class:`~org.hipparchus.analysis.differentiation.SparseGradient` y, :class:`~org.hipparchus.analysis.differentiation.SparseGradient` x)
        
            Two arguments arc tangent operation.
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first argument of the arc tangent
                x (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second argument of the arc tangent
        
            Returns:
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(sparseGradient: 'SparseGradient', sparseGradient2: 'SparseGradient') -> 'SparseGradient': ...
    def atanh(self) -> 'SparseGradient':
        """
            Inverse hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'SparseGradient':
        """
            Cubic root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'SparseGradient':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compose(self, doubleArray: typing.List[float]) -> 'SparseGradient':
        """
            Compute composition of the instance by a univariate function.
        
            Parameters:
                f (double...): array of value and derivatives of the function at the current point (i.e.
                    [f(:meth:`~org.hipparchus.analysis.differentiation.SparseGradient.getValue`),
                    f'(:meth:`~org.hipparchus.analysis.differentiation.SparseGradient.getValue`),
                    f''(:meth:`~org.hipparchus.analysis.differentiation.SparseGradient.getValue`)...]).
        
            Returns:
                f(this)
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the number of elements in the array is not equal to 2 (i.e. value and first derivative)
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'SparseGradient':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def cos(self) -> 'SparseGradient':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'SparseGradient':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @staticmethod
    def createConstant(double: float) -> 'SparseGradient':
        """
            Factory method creating a constant.
        
            Parameters:
                value (double): value of the constant
        
            Returns:
                a new instance
        
        
        """
        ...
    @staticmethod
    def createVariable(int: int, double: float) -> 'SparseGradient':
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
    def divide(self, double: float) -> 'SparseGradient':
        """
            Compute this ÷ a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
            '÷' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                c (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
        
        """
        ...
    @typing.overload
    def divide(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two sparse gradients.
        
            Sparse gradients are considered equal if they have the same value and the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two sparse gradients are equal
        
        
        """
        ...
    def exp(self) -> 'SparseGradient':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'SparseGradient':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'SparseGradient':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getDerivative(self, int: int) -> float:
        """
            Get the derivative with respect to a particular index variable.
        
            Parameters:
                index (int): index to differentiate with.
        
            Returns:
                derivative with respect to a particular index variable
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['SparseGradient']: ...
    def getPi(self) -> 'SparseGradient':
        """
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant Ï€
        
        
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
    def getValue(self) -> float:
        """
            Get the value of the function.
        
            Returns:
                value of the function.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the derivative structure.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    @typing.overload
    def hypot(self, sparseGradient: 'SparseGradient') -> 'SparseGradient':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2` Â +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
            Returns the hypotenuse of a triangle with sides :code:`x` and :code:`y` - sqrt(*x* :sup:`2` Â +*y* :sup:`2` ) avoiding
            intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): a value
                y (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): a value
        
            Returns:
                sqrt(*x* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def hypot(sparseGradient: 'SparseGradient', sparseGradient2: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, double: float, sparseGradient: 'SparseGradient', double2: float, sparseGradient2: 'SparseGradient') -> 'SparseGradient':
        """
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the third term
                a4 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, sparseGradient: 'SparseGradient', double2: float, sparseGradient2: 'SparseGradient', double3: float, sparseGradient3: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, double: float, sparseGradient: 'SparseGradient', double2: float, sparseGradient2: 'SparseGradient', double3: float, sparseGradient3: 'SparseGradient', double4: float, sparseGradient4: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], sparseGradientArray: typing.List['SparseGradient']) -> 'SparseGradient':
        """
            Compute a linear combination.
        
            Specified by:
                 in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, sparseGradient: 'SparseGradient', sparseGradient2: 'SparseGradient', sparseGradient3: 'SparseGradient', sparseGradient4: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, sparseGradient: 'SparseGradient', sparseGradient2: 'SparseGradient', sparseGradient3: 'SparseGradient', sparseGradient4: 'SparseGradient', sparseGradient5: 'SparseGradient', sparseGradient6: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, sparseGradient: 'SparseGradient', sparseGradient2: 'SparseGradient', sparseGradient3: 'SparseGradient', sparseGradient4: 'SparseGradient', sparseGradient5: 'SparseGradient', sparseGradient6: 'SparseGradient', sparseGradient7: 'SparseGradient', sparseGradient8: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    def linearCombination(self, sparseGradientArray: typing.List['SparseGradient'], sparseGradientArray2: typing.List['SparseGradient']) -> 'SparseGradient': ...
    def log(self) -> 'SparseGradient':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'SparseGradient':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'SparseGradient':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'SparseGradient':
        """
            Compute this × a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): element to multiply
        
            Returns:
                a new element representing this × a
        
            '×' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                c (double): right hand side parameter of the operator
        
            Returns:
                this×a
        
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'SparseGradient': ...
    @typing.overload
    def multiply(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def multiplyInPlace(self, sparseGradient: 'SparseGradient') -> None:
        """
            Multiply in place.
        
            This method is designed to be faster when used multiple times in a loop.
        
            The instance is changed here, in order to not change the instance the
            :meth:`~org.hipparchus.analysis.differentiation.SparseGradient.add` method should be used.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): instance to multiply
        
        
        """
        ...
    def negate(self) -> 'SparseGradient':
        """
            Returns the additive inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'SparseGradient':
        """
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                v (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    def numVars(self) -> int:
        """
            Find the number of variables.
        
            Returns:
                number of variables
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'SparseGradient':
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
                e (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): exponent
        
            Returns:
                this :sup:`e`
        
            Compute a :sup:`x` where a is a double and x a :class:`~org.hipparchus.analysis.differentiation.SparseGradient`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): power to apply
        
            Returns:
                a :sup:`x`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'SparseGradient': ...
    @typing.overload
    def pow(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    @typing.overload
    @staticmethod
    def pow(double: float, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def reciprocal(self) -> 'SparseGradient':
        """
            Returns the multiplicative inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.reciprocal` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'SparseGradient':
        """
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def rint(self) -> 'SparseGradient':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'SparseGradient':
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
    def scalb(self, int: int) -> 'SparseGradient':
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
    def sign(self) -> 'SparseGradient':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'SparseGradient':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['SparseGradient']: ...
    def sinh(self) -> 'SparseGradient':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['SparseGradient']: ...
    def sqrt(self) -> 'SparseGradient':
        """
            Square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'SparseGradient':
        """
            Compute this - a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.SparseGradient`): element to subtract
        
            Returns:
                a new element representing this - a
        
            '-' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                c (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
        
        """
        ...
    @typing.overload
    def subtract(self, sparseGradient: 'SparseGradient') -> 'SparseGradient': ...
    def tan(self) -> 'SparseGradient':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'SparseGradient':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def taylor(self, doubleArray: typing.List[float]) -> float:
        """
            Evaluate Taylor expansion of a sparse gradient.
        
            Parameters:
                delta (double...): parameters offsets (Δx, Δy, ...)
        
            Returns:
                value of the Taylor expansion at x + Δx, y + Δy, ...
        
        
        """
        ...
    def toDegrees(self) -> 'SparseGradient':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'SparseGradient':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toRadians` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'SparseGradient':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            The :code:`ulp` function is a step function, hence all its derivatives are 0.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
            Since:
                2.0
        
        
        """
        ...

class UnivariateDerivative1Field(org.hipparchus.Field['UnivariateDerivative1'], java.io.Serializable):
    """
    public class UnivariateDerivative1Field extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`>, Serializable
    
        Field for :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1` instances.
    
        This class is a singleton.
    
        Since:
            1.7
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
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
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a Ã— e :sub:`1` = e :sub:`1` Ã— a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['UnivariateDerivative1']: ...
    def getZero(self) -> 'UnivariateDerivative1':
        """
            Get the additive identity of the field.
        
            The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a
            + e :sub:`0` = e :sub:`0` + a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getZero` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UnivariateDerivative2Field(org.hipparchus.Field['UnivariateDerivative2'], java.io.Serializable):
    """
    public class UnivariateDerivative2Field extends Object implements :class:`~org.hipparchus.Field`<:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`>, Serializable
    
        Field for :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2` instances.
    
        This class is a singleton.
    
        Since:
            1.7
    
        Also see:
            :meth:`~serialized`
    """
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
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
        
            The multiplicative identity is the element e :sub:`1` of the field such that for all elements a of the field, the
            equalities a Ã— e :sub:`1` = e :sub:`1` Ã— a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getOne` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                multiplicative identity of the field
        
        
        """
        ...
    def getRuntimeClass(self) -> typing.Type['UnivariateDerivative2']: ...
    def getZero(self) -> 'UnivariateDerivative2':
        """
            Get the additive identity of the field.
        
            The additive identity is the element e :sub:`0` of the field such that for all elements a of the field, the equalities a
            + e :sub:`0` = e :sub:`0` + a = a hold.
        
            Specified by:
                :meth:`~org.hipparchus.Field.getZero` in interface :class:`~org.hipparchus.Field`
        
            Returns:
                additive identity of the field
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...

class UnivariateDifferentiableFunction(org.hipparchus.analysis.UnivariateFunction):
    """
    public interface UnivariateDifferentiableFunction extends :class:`~org.hipparchus.analysis.UnivariateFunction`
    
        Interface for univariate functions derivatives.
    
        This interface represents a simple function which computes both the value and the first derivative of a mathematical
        function. The derivative is computed with respect to the input variable.
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateFunctionDifferentiator`
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> float: ...
    @typing.overload
    def value(self, t: _value_1__T) -> _value_1__T: ...

class UnivariateDifferentiableMatrixFunction(org.hipparchus.analysis.UnivariateMatrixFunction):
    """
    public interface UnivariateDifferentiableMatrixFunction extends :class:`~org.hipparchus.analysis.UnivariateMatrixFunction`
    
        Extension of :class:`~org.hipparchus.analysis.UnivariateMatrixFunction` representing a univariate differentiable matrix
        function.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> typing.List[typing.List[float]]: ...
    @typing.overload
    def value(self, t: _value_1__T) -> typing.List[typing.List[_value_1__T]]: ...

class UnivariateDifferentiableVectorFunction(org.hipparchus.analysis.UnivariateVectorFunction):
    """
    public interface UnivariateDifferentiableVectorFunction extends :class:`~org.hipparchus.analysis.UnivariateVectorFunction`
    
        Extension of :class:`~org.hipparchus.analysis.UnivariateVectorFunction` representing a univariate differentiable
        vectorial function.
    """
    _value_1__T = typing.TypeVar('_value_1__T', bound=Derivative)  # <T>
    @typing.overload
    def value(self, double: float) -> typing.List[float]: ...
    @typing.overload
    def value(self, t: _value_1__T) -> typing.List[_value_1__T]: ...

class UnivariateFunctionDifferentiator:
    """
    public interface UnivariateFunctionDifferentiator
    
        Interface defining the function differentiation operation.
    """
    def differentiate(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> UnivariateDifferentiableFunction:
        """
            Create an implementation of a :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction` from a
            regular :class:`~org.hipparchus.analysis.UnivariateFunction`.
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateFunction`): function to differentiate
        
            Returns:
                differential function
        
        
        """
        ...

class UnivariateMatrixFunctionDifferentiator:
    """
    public interface UnivariateMatrixFunctionDifferentiator
    
        Interface defining the function differentiation operation.
    """
    def differentiate(self, univariateMatrixFunction: org.hipparchus.analysis.UnivariateMatrixFunction) -> UnivariateDifferentiableMatrixFunction:
        """
            Create an implementation of a :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableMatrixFunction`
            from a regular :class:`~org.hipparchus.analysis.UnivariateMatrixFunction`.
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateMatrixFunction`): function to differentiate
        
            Returns:
                differential function
        
        
        """
        ...

class UnivariateVectorFunctionDifferentiator:
    """
    public interface UnivariateVectorFunctionDifferentiator
    
        Interface defining the function differentiation operation.
    """
    def differentiate(self, univariateVectorFunction: org.hipparchus.analysis.UnivariateVectorFunction) -> UnivariateDifferentiableVectorFunction:
        """
            Create an implementation of a :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableVectorFunction`
            from a regular :class:`~org.hipparchus.analysis.UnivariateVectorFunction`.
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateVectorFunction`): function to differentiate
        
            Returns:
                differential function
        
        
        """
        ...

class DerivativeStructure(Derivative['DerivativeStructure'], java.io.Serializable):
    """
    public class DerivativeStructure extends Object implements :class:`~org.hipparchus.analysis.differentiation.Derivative`<:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`>, Serializable
    
        Class representing both the value and the differentials of a function.
    
        This class is the workhorse of the differentiation package.
    
        This class is an implementation of the extension to Rall's numbers described in Dan Kalman's paper `Doubly Recursive
        Multivariate Automatic Differentiation <http://www.dankalman.net/AUhome/pdffiles/mmgautodiff.pdf>`, Mathematics
        Magazine, vol. 75, no. 3, June 2002. Rall's numbers are an extension to the real numbers used throughout mathematical
        expressions; they hold the derivative together with the value of a function. Dan Kalman's derivative structures hold all
        partial derivatives up to any specified order, with respect to any number of free parameters. Rall's numbers therefore
        can be seen as derivative structures for order one derivative and one free parameter, and real numbers can be seen as
        derivative structures with zero order derivative and no free parameters.
    
        :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` instances can be used directly thanks to the
        arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
        Implementing complex expression can also be done by developing computation code using standard primitive double values
        and to use :class:`~org.hipparchus.analysis.differentiation.UnivariateFunctionDifferentiator` to create the
        :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`-based instances. This method is simpler but may be
        limited in the accuracy and derivation orders and may be computationally intensive (this is typically the case for
        :class:`~org.hipparchus.analysis.differentiation.FiniteDifferencesDifferentiator`.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DSCompiler`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`, :meth:`~serialized`
    """
    def abs(self) -> 'DerivativeStructure':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'DerivativeStructure':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'DerivativeStructure':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'DerivativeStructure':
        """
            '+' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.add` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
        public :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` add(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` a) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute this + a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): element to add
        
            Returns:
                a new element representing this + a
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def add(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def asin(self) -> 'DerivativeStructure':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'DerivativeStructure':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'DerivativeStructure':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    @typing.overload
    def atan2(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure':
        """
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders are inconsistent
        
        public static :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` atan2(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` y, :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` x) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Two arguments arc tangent operation.
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): first argument of the arc tangent
                x (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): second argument of the arc tangent
        
            Returns:
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(derivativeStructure: 'DerivativeStructure', derivativeStructure2: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def atanh(self) -> 'DerivativeStructure':
        """
            Inverse hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'DerivativeStructure':
        """
            Cubic root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'DerivativeStructure':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compose(self, doubleArray: typing.List[float]) -> 'DerivativeStructure': ...
    @typing.overload
    def copySign(self, double: float) -> 'DerivativeStructure':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def cos(self) -> 'DerivativeStructure':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'DerivativeStructure':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'DerivativeStructure':
        """
            '÷' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
        public :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` divide(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` a) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute this ÷ a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def divide(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two derivative structures.
        
            Derivative structures are considered equal if they have the same number of free parameters, the same derivation order,
            and the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two derivative structures are equal
        
        
        """
        ...
    def exp(self) -> 'DerivativeStructure':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'DerivativeStructure':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'DerivativeStructure':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getAllDerivatives(self) -> typing.List[float]:
        """
            Get all partial derivatives.
        
            Returns:
                a fresh copy of partial derivatives, in an array sorted according to
                :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeIndex`
        
        
        """
        ...
    def getExponent(self) -> int:
        """
            Return the exponent of the instance value, removing the bias.
        
            For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getExponent` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponent for instance in IEEE754 representation, without bias
        
        
        """
        ...
    def getFactory(self) -> DSFactory:
        """
            Get the factory that built the instance.
        
            Returns:
                factory that built the instance
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field['DerivativeStructure']: ...
    def getFreeParameters(self) -> int:
        """
            Description copied from interface: :meth:`~org.hipparchus.analysis.differentiation.Derivative.getFreeParameters`
            Get the number of free parameters.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getFreeParameters`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                number of free parameters
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Description copied from interface: :meth:`~org.hipparchus.analysis.differentiation.Derivative.getOrder`
            Get the derivation order.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getOrder`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPartialDerivative(self, intArray: typing.List[int]) -> float: ...
    def getPi(self) -> 'DerivativeStructure':
        """
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant Ï€
        
        
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
    def getValue(self) -> float:
        """
            Get the value part of the derivative structure.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                value part of the derivative structure
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.DerivativeStructure.getPartialDerivative`
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the derivative structure.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    @typing.overload
    def hypot(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    @staticmethod
    def hypot(derivativeStructure: 'DerivativeStructure', derivativeStructure2: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, double: float, derivativeStructure: 'DerivativeStructure', double2: float, derivativeStructure2: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, double: float, derivativeStructure: 'DerivativeStructure', double2: float, derivativeStructure2: 'DerivativeStructure', double3: float, derivativeStructure3: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, double: float, derivativeStructure: 'DerivativeStructure', double2: float, derivativeStructure2: 'DerivativeStructure', double3: float, derivativeStructure3: 'DerivativeStructure', double4: float, derivativeStructure4: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], derivativeStructureArray: typing.List['DerivativeStructure']) -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, derivativeStructure: 'DerivativeStructure', derivativeStructure2: 'DerivativeStructure', derivativeStructure3: 'DerivativeStructure', derivativeStructure4: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, derivativeStructure: 'DerivativeStructure', derivativeStructure2: 'DerivativeStructure', derivativeStructure3: 'DerivativeStructure', derivativeStructure4: 'DerivativeStructure', derivativeStructure5: 'DerivativeStructure', derivativeStructure6: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, derivativeStructure: 'DerivativeStructure', derivativeStructure2: 'DerivativeStructure', derivativeStructure3: 'DerivativeStructure', derivativeStructure4: 'DerivativeStructure', derivativeStructure5: 'DerivativeStructure', derivativeStructure6: 'DerivativeStructure', derivativeStructure7: 'DerivativeStructure', derivativeStructure8: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    def linearCombination(self, derivativeStructureArray: typing.List['DerivativeStructure'], derivativeStructureArray2: typing.List['DerivativeStructure']) -> 'DerivativeStructure': ...
    def log(self) -> 'DerivativeStructure':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'DerivativeStructure':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'DerivativeStructure':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'DerivativeStructure':
        """
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
            '×' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this×a
        
        public :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` multiply(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` a) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute this × a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): element to multiply
        
            Returns:
                a new element representing this × a
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def multiply(self, int: int) -> 'DerivativeStructure': ...
    @typing.overload
    def multiply(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def negate(self) -> 'DerivativeStructure':
        """
            Returns the additive inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'DerivativeStructure':
        """
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                value (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'DerivativeStructure':
        """
            Compute a :sup:`x` where a is a double and x a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): power to apply
        
            Returns:
                a :sup:`x`
        
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
        
        public :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` pow(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` e) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): exponent
        
            Returns:
                this :sup:`e`
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'DerivativeStructure': ...
    @typing.overload
    def pow(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    @typing.overload
    @staticmethod
    def pow(double: float, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def reciprocal(self) -> 'DerivativeStructure':
        """
            Returns the multiplicative inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.reciprocal` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'DerivativeStructure':
        """
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        public :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` remainder(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` a) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def remainder(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def rint(self) -> 'DerivativeStructure':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'DerivativeStructure':
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
    def scalb(self, int: int) -> 'DerivativeStructure':
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
    def sign(self) -> 'DerivativeStructure':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'DerivativeStructure':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['DerivativeStructure']: ...
    def sinh(self) -> 'DerivativeStructure':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['DerivativeStructure']: ...
    def sqrt(self) -> 'DerivativeStructure':
        """
            Square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'DerivativeStructure':
        """
            '-' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
        public :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` subtract(:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` a) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Compute this - a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`): element to subtract
        
            Returns:
                a new element representing this - a
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    def subtract(self, derivativeStructure: 'DerivativeStructure') -> 'DerivativeStructure': ...
    def tan(self) -> 'DerivativeStructure':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'DerivativeStructure':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def taylor(self, doubleArray: typing.List[float]) -> float: ...
    def toDegrees(self) -> 'DerivativeStructure':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toRadians(self) -> 'DerivativeStructure':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toRadians` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'DerivativeStructure':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            The :code:`ulp` function is a step function, hence all its derivatives are 0.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
            Since:
                2.0
        
        
        """
        ...

_FieldDerivativeStructure__T = typing.TypeVar('_FieldDerivativeStructure__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldDerivativeStructure(FieldDerivative[_FieldDerivativeStructure__T, 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]], typing.Generic[_FieldDerivativeStructure__T]):
    """
    public class FieldDerivativeStructure<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`<T,:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T>>
    
        Class representing both the value and the differentials of a function.
    
        This class is similar to :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` except function
        parameters and value can be any :class:`~org.hipparchus.CalculusFieldElement`.
    
        Instances of this class are guaranteed to be immutable.
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FDSFactory`,
            :class:`~org.hipparchus.analysis.differentiation.DSCompiler`
    """
    def abs(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def acos(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def acosh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def add(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def add(self, t: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def add(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def asin(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def asinh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def atan(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    _atan2_1__T = typing.TypeVar('_atan2_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def atan2(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]:
        """
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders are inconsistent
        
        public static <T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T> atan2(:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T> y, :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T> x) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Two arguments arc tangent operation.
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T> y): first argument of the arc tangent
                x (:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T> x): second argument of the arc tangent
        
            Returns:
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def atan2(fieldDerivativeStructure: 'FieldDerivativeStructure'[_atan2_1__T], fieldDerivativeStructure2: 'FieldDerivativeStructure'[_atan2_1__T]) -> 'FieldDerivativeStructure'[_atan2_1__T]: ...
    def atanh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def cbrt(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def ceil(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def compose(self, tArray: typing.List[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def compose(self, doubleArray: typing.List[float]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def copySign(self, t: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def copySign(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def cos(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def cosh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def divide(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def divide(self, t: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def divide(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def exp(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def expm1(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def floor(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def getAllDerivatives(self) -> typing.List[_FieldDerivativeStructure__T]:
        """
            Get all partial derivatives.
        
            Returns:
                a fresh copy of partial derivatives, in an array sorted according to
                :meth:`~org.hipparchus.analysis.differentiation.DSCompiler.getPartialDerivativeIndex`
        
        
        """
        ...
    def getExponent(self) -> int:
        """
            Return the exponent of the instance value, removing the bias.
        
            For double numbers of the form 2 :sup:`x` , the unbiased exponent is exactly x.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getExponent` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponent for instance in IEEE754 representation, without bias
        
        
        """
        ...
    def getFactory(self) -> FDSFactory[_FieldDerivativeStructure__T]: ...
    def getField(self) -> org.hipparchus.Field['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]: ...
    def getFreeParameters(self) -> int:
        """
            Description copied from interface: :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getFreeParameters`
            Get the number of free parameters.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getFreeParameters`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                number of free parameters
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Description copied from interface: :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getOrder`
            Get the derivation order.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getOrder`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPartialDerivative(self, intArray: typing.List[int]) -> _FieldDerivativeStructure__T: ...
    def getPi(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def getValue(self) -> _FieldDerivativeStructure__T:
        """
            Get the value part of the derivative structure.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getValue`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                value part of the derivative structure
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure.getPartialDerivative`
        
        
        """
        ...
    _hypot_1__T = typing.TypeVar('_hypot_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def hypot(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    @staticmethod
    def hypot(fieldDerivativeStructure: 'FieldDerivativeStructure'[_hypot_1__T], fieldDerivativeStructure2: 'FieldDerivativeStructure'[_hypot_1__T]) -> 'FieldDerivativeStructure'[_hypot_1__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], double2: float, fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], double2: float, fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], double3: float, fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], double2: float, fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], double3: float, fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], double4: float, fieldDerivativeStructure4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], fieldDerivativeStructureArray: typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, t: _FieldDerivativeStructure__T, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], t2: _FieldDerivativeStructure__T, fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, t: _FieldDerivativeStructure__T, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], t2: _FieldDerivativeStructure__T, fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], t3: _FieldDerivativeStructure__T, fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, t: _FieldDerivativeStructure__T, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], t2: _FieldDerivativeStructure__T, fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], t3: _FieldDerivativeStructure__T, fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], t4: _FieldDerivativeStructure__T, fieldDerivativeStructure4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, tArray: typing.List[_FieldDerivativeStructure__T], fieldDerivativeStructureArray: typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure5: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure6: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure2: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure3: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure4: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure5: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure6: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure7: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T], fieldDerivativeStructure8: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def linearCombination(self, fieldDerivativeStructureArray: typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]], fieldDerivativeStructureArray2: typing.List['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def log(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def log10(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def log1p(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def multiply(self, t: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def multiply(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def negate(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def newInstance(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def pow(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    @staticmethod
    def pow(double: float, fieldDerivativeStructure: 'FieldDerivativeStructure'[_pow_3__T]) -> 'FieldDerivativeStructure'[_pow_3__T]:
        """
            Compute a :sup:`x` where a is a double and x a
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<T> x): power to apply
        
            Returns:
                a :sup:`x`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`> pow(double p)
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`> pow(int n)
        
            Integer power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`> pow(:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`> e) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`<:class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`> e): exponent
        
            Returns:
                this :sup:`e`
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if number of free parameters or orders do not match
        
        
        """
        ...
    def reciprocal(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def remainder(self, t: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def remainder(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def rint(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def rootN(self, int: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def scalb(self, int: int) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def sign(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def sin(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]: ...
    def sinh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldDerivativeStructure'[_FieldDerivativeStructure__T]]: ...
    def sqrt(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def subtract(self, t: _FieldDerivativeStructure__T) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def subtract(self, fieldDerivativeStructure: 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def tan(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def tanh(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    @typing.overload
    def taylor(self, tArray: typing.List[_FieldDerivativeStructure__T]) -> _FieldDerivativeStructure__T: ...
    @typing.overload
    def taylor(self, doubleArray: typing.List[float]) -> _FieldDerivativeStructure__T: ...
    def toDegrees(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def toRadians(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...
    def ulp(self) -> 'FieldDerivativeStructure'[_FieldDerivativeStructure__T]: ...

_FieldGradient__T = typing.TypeVar('_FieldGradient__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGradient(FieldDerivative[_FieldGradient__T, 'FieldGradient'[_FieldGradient__T]], typing.Generic[_FieldGradient__T]):
    """
    public class FieldGradient<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object implements :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`<T,:class:`~org.hipparchus.analysis.differentiation.FieldGradient`<T>>
    
        Class representing both the value and the differentials of a function.
    
        This class is a stripped-down version of :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` with
        :meth:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure.getOrder` limited to one. It should have less
        overhead than :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` in its domain.
    
        This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout
        mathematical expressions; they hold the derivative together with the value of a function.
    
        :class:`~org.hipparchus.analysis.differentiation.FieldGradient` instances can be used directly thanks to the arithmetic
        operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.7
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.Gradient`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`
    """
    @typing.overload
    def __init__(self, t: _FieldGradient__T, tArray: typing.List[_FieldGradient__T]): ...
    @typing.overload
    def __init__(self, fieldDerivativeStructure: FieldDerivativeStructure[_FieldGradient__T]): ...
    def abs(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def acos(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def acosh(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def add(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def add(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def add(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def asin(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def asinh(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def atan(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def atan2(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def atanh(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def cbrt(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def ceil(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def compose(self, t: _FieldGradient__T, t2: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    _constant__T = typing.TypeVar('_constant__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def constant(int: int, t: _constant__T) -> 'FieldGradient'[_constant__T]:
        """
            Build an instance corresponding to a constant value.
        
            Parameters:
                freeParameters (int): number of free parameters (i.e. dimension of the gradient)
                value (T): constant value of the function
        
            Returns:
                a :code:`FieldGradient` with a constant value and all derivatives set to 0.0
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def copySign(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def copySign(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def cos(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def cosh(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def divide(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def divide(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def divide(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two univariate derivatives.
        
            univariate derivatives are considered equal if they have the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def expm1(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def floor(self) -> 'FieldGradient'[_FieldGradient__T]: ...
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
    def getField(self) -> FieldGradientField[_FieldGradient__T]: ...
    def getFreeParameters(self) -> int:
        """
            Get the number of free parameters.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getFreeParameters`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                number of free parameters
        
        
        """
        ...
    def getGradient(self) -> typing.List[_FieldGradient__T]:
        """
            Get the gradient part of the function.
        
            Returns:
                gradient part of the value of the function
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the derivation order.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getOrder`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                derivation order
        
        
        """
        ...
    @typing.overload
    def getPartialDerivative(self, int: int) -> _FieldGradient__T: ...
    @typing.overload
    def getPartialDerivative(self, intArray: typing.List[int]) -> _FieldGradient__T: ...
    def getPi(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getReal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                real value
        
        
        """
        ...
    def getValue(self) -> _FieldGradient__T:
        """
            Get the value part of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getValue`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                value part of the value of the function
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FieldGradient__T]: ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the univariate derivative.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldGradient: 'FieldGradient'[_FieldGradient__T], double2: float, fieldGradient2: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldGradient: 'FieldGradient'[_FieldGradient__T], double2: float, fieldGradient2: 'FieldGradient'[_FieldGradient__T], double3: float, fieldGradient3: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldGradient: 'FieldGradient'[_FieldGradient__T], double2: float, fieldGradient2: 'FieldGradient'[_FieldGradient__T], double3: float, fieldGradient3: 'FieldGradient'[_FieldGradient__T], double4: float, fieldGradient4: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], fieldGradientArray: typing.List['FieldGradient'[_FieldGradient__T]]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, t: _FieldGradient__T, fieldGradient: 'FieldGradient'[_FieldGradient__T], t2: _FieldGradient__T, fieldGradient2: 'FieldGradient'[_FieldGradient__T], t3: _FieldGradient__T, fieldGradient3: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, tArray: typing.List[_FieldGradient__T], fieldGradientArray: typing.List['FieldGradient'[_FieldGradient__T]]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, fieldGradient: 'FieldGradient'[_FieldGradient__T], fieldGradient2: 'FieldGradient'[_FieldGradient__T], fieldGradient3: 'FieldGradient'[_FieldGradient__T], fieldGradient4: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, fieldGradient: 'FieldGradient'[_FieldGradient__T], fieldGradient2: 'FieldGradient'[_FieldGradient__T], fieldGradient3: 'FieldGradient'[_FieldGradient__T], fieldGradient4: 'FieldGradient'[_FieldGradient__T], fieldGradient5: 'FieldGradient'[_FieldGradient__T], fieldGradient6: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, fieldGradient: 'FieldGradient'[_FieldGradient__T], fieldGradient2: 'FieldGradient'[_FieldGradient__T], fieldGradient3: 'FieldGradient'[_FieldGradient__T], fieldGradient4: 'FieldGradient'[_FieldGradient__T], fieldGradient5: 'FieldGradient'[_FieldGradient__T], fieldGradient6: 'FieldGradient'[_FieldGradient__T], fieldGradient7: 'FieldGradient'[_FieldGradient__T], fieldGradient8: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def linearCombination(self, fieldGradientArray: typing.List['FieldGradient'[_FieldGradient__T]], fieldGradientArray2: typing.List['FieldGradient'[_FieldGradient__T]]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def log(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def log10(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def log1p(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def multiply(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def negate(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def newInstance(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def newInstance(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def pow(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    @staticmethod
    def pow(double: float, fieldGradient: 'FieldGradient'[_pow_3__T]) -> 'FieldGradient'[_pow_3__T]:
        """
            Compute a :sup:`x` where a is a double and x a :class:`~org.hipparchus.analysis.differentiation.FieldGradient`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.FieldGradient`<T> x): power to apply
        
            Returns:
                a :sup:`x`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldGradient`<:class:`~org.hipparchus.analysis.differentiation.FieldGradient`> pow(double p)
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldGradient`<:class:`~org.hipparchus.analysis.differentiation.FieldGradient`> pow(int n)
        
            Integer power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldGradient`<:class:`~org.hipparchus.analysis.differentiation.FieldGradient`> pow(:class:`~org.hipparchus.analysis.differentiation.FieldGradient`<:class:`~org.hipparchus.analysis.differentiation.FieldGradient`> e)
        
            Power operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.pow` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.FieldGradient`<:class:`~org.hipparchus.analysis.differentiation.FieldGradient`> e): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    def reciprocal(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def remainder(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def remainder(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def rint(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def rootN(self, int: int) -> 'FieldGradient'[_FieldGradient__T]: ...
    def scalb(self, int: int) -> 'FieldGradient'[_FieldGradient__T]: ...
    def sign(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def sin(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldGradient'[_FieldGradient__T]]: ...
    def sinh(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldGradient'[_FieldGradient__T]]: ...
    def sqrt(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def subtract(self, t: _FieldGradient__T) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def subtract(self, fieldGradient: 'FieldGradient'[_FieldGradient__T]) -> 'FieldGradient'[_FieldGradient__T]: ...
    def tan(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def tanh(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    @typing.overload
    def taylor(self, doubleArray: typing.List[float]) -> _FieldGradient__T:
        """
            Evaluate Taylor expansion of a gradient.
        
            Parameters:
                delta (double...): parameters offsets (Δx, Δy, ...)
        
            Returns:
                value of the Taylor expansion at x + Δx, y + Δy, ...
        
            Evaluate Taylor expansion of a gradient.
        
            Parameters:
                delta (:class:`~org.hipparchus.analysis.differentiation.FieldGradient`...): parameters offsets (Δx, Δy, ...)
        
            Returns:
                value of the Taylor expansion at x + Δx, y + Δy, ...
        
        
        """
        ...
    @typing.overload
    def taylor(self, tArray: typing.List[_FieldGradient__T]) -> _FieldGradient__T: ...
    def toDegrees(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldGradient__T]: ...
    def toRadians(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    def ulp(self) -> 'FieldGradient'[_FieldGradient__T]: ...
    _variable__T = typing.TypeVar('_variable__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @staticmethod
    def variable(int: int, int2: int, t: _variable__T) -> 'FieldGradient'[_variable__T]:
        """
            Build a :code:`Gradient` representing a variable.
        
            Instances built using this method are considered to be the free variables with respect to which differentials are
            computed. As such, their differential with respect to themselves is +1.
        
            Parameters:
                freeParameters (int): number of free parameters (i.e. dimension of the gradient)
                index (int): index of the variable (from 0 to :meth:`~org.hipparchus.analysis.differentiation.FieldGradient.getFreeParameters` - 1)
                value (T): value of the variable
        
            Returns:
                a :code:`FieldGradient` with a constant value and all derivatives set to 0.0 except the one at :code:`index` which will
                be set to 1.0
        
        
        """
        ...

_FieldUnivariateDerivative__S = typing.TypeVar('_FieldUnivariateDerivative__S', bound=org.hipparchus.CalculusFieldElement)  # <S>
_FieldUnivariateDerivative__T = typing.TypeVar('_FieldUnivariateDerivative__T', bound='FieldUnivariateDerivative')  # <T>
class FieldUnivariateDerivative(FieldDerivative[_FieldUnivariateDerivative__S, _FieldUnivariateDerivative__T], typing.Generic[_FieldUnivariateDerivative__S, _FieldUnivariateDerivative__T]):
    """
    public abstract class FieldUnivariateDerivative<S extends :class:`~org.hipparchus.CalculusFieldElement`<S>,T extends FieldUnivariateDerivative<S,T>> extends Object implements :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`<S,T>
    
        Abstract class representing both the value and the differentials of a function.
    
        Since:
            1.7
    """
    def __init__(self): ...
    def getDerivative(self, int: int) -> _FieldUnivariateDerivative__S: ...
    def getFreeParameters(self) -> int:
        """
            Get the number of free parameters.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldDerivative.getFreeParameters`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.FieldDerivative`
        
            Returns:
                number of free parameters
        
        
        """
        ...
    def getPartialDerivative(self, intArray: typing.List[int]) -> _FieldUnivariateDerivative__S: ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldUnivariateDerivative__S]: ...

class FiniteDifferencesDifferentiator(UnivariateFunctionDifferentiator, UnivariateVectorFunctionDifferentiator, UnivariateMatrixFunctionDifferentiator, java.io.Serializable):
    """
    public class FiniteDifferencesDifferentiator extends Object implements :class:`~org.hipparchus.analysis.differentiation.UnivariateFunctionDifferentiator`, :class:`~org.hipparchus.analysis.differentiation.UnivariateVectorFunctionDifferentiator`, :class:`~org.hipparchus.analysis.differentiation.UnivariateMatrixFunctionDifferentiator`, Serializable
    
        Univariate functions differentiator using finite differences.
    
        This class creates some wrapper objects around regular :class:`~org.hipparchus.analysis.UnivariateFunction` (or
        :class:`~org.hipparchus.analysis.UnivariateVectorFunction` or
        :class:`~org.hipparchus.analysis.UnivariateMatrixFunction`). These wrapper objects compute derivatives in addition to
        function values.
    
        The wrapper objects work by calling the underlying function on a sampling grid around the current point and performing
        polynomial interpolation. A finite differences scheme with n points is theoretically able to compute derivatives up to
        order n-1, but it is generally better to have a slight margin. The step size must also be small enough in order for the
        polynomial approximation to be good in the current point neighborhood, but it should not be too small because numerical
        instability appears quickly (there are several differences of close points). Choosing the number of points and the step
        size is highly problem dependent.
    
        As an example of good and bad settings, lets consider the quintic polynomial function :code:`f(x) =
        (x-1)*(x-0.5)*x*(x+0.5)*(x+1)`. Since it is a polynomial, finite differences with at least 6 points should theoretically
        recover the exact same polynomial and hence compute accurate derivatives for any order. However, due to numerical
        errors, we get the following results for a 7 points finite differences for abscissae in the [-10, 10] range:
    
          - step size = 0.25, second order derivative error about 9.97e-10
          - step size = 0.25, fourth order derivative error about 5.43e-8
          - step size = 1.0e-6, second order derivative error about 148
          - step size = 1.0e-6, fourth order derivative error about 6.35e+14
    
    
        This example shows that the small step size is really bad, even simply for second order derivative!
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, double: float, double2: float, double3: float): ...
    @typing.overload
    def differentiate(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> UnivariateDifferentiableFunction:
        """
            Create an implementation of a :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableFunction` from a
            regular :class:`~org.hipparchus.analysis.UnivariateFunction`.
        
            The returned object cannot compute derivatives to arbitrary orders. The value function will throw a
            :class:`~org.hipparchus.exception.MathIllegalArgumentException` if the requested derivation order is larger or equal to
            the number of points.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateFunctionDifferentiator.differentiate`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateFunctionDifferentiator`
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateFunction`): function to differentiate
        
            Returns:
                differential function
        
            Create an implementation of a :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableVectorFunction`
            from a regular :class:`~org.hipparchus.analysis.UnivariateVectorFunction`.
        
            The returned object cannot compute derivatives to arbitrary orders. The value function will throw a
            :class:`~org.hipparchus.exception.MathIllegalArgumentException` if the requested derivation order is larger or equal to
            the number of points.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateVectorFunctionDifferentiator.differentiate`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateVectorFunctionDifferentiator`
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateVectorFunction`): function to differentiate
        
            Returns:
                differential function
        
            Create an implementation of a :class:`~org.hipparchus.analysis.differentiation.UnivariateDifferentiableMatrixFunction`
            from a regular :class:`~org.hipparchus.analysis.UnivariateMatrixFunction`.
        
            The returned object cannot compute derivatives to arbitrary orders. The value function will throw a
            :class:`~org.hipparchus.exception.MathIllegalArgumentException` if the requested derivation order is larger or equal to
            the number of points.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateMatrixFunctionDifferentiator.differentiate`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateMatrixFunctionDifferentiator`
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateMatrixFunction`): function to differentiate
        
            Returns:
                differential function
        
        
        """
        ...
    @typing.overload
    def differentiate(self, univariateMatrixFunction: org.hipparchus.analysis.UnivariateMatrixFunction) -> UnivariateDifferentiableMatrixFunction: ...
    @typing.overload
    def differentiate(self, univariateVectorFunction: org.hipparchus.analysis.UnivariateVectorFunction) -> UnivariateDifferentiableVectorFunction: ...
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

class Gradient(Derivative['Gradient'], org.hipparchus.CalculusFieldElement['Gradient'], java.io.Serializable):
    """
    public class Gradient extends Object implements :class:`~org.hipparchus.analysis.differentiation.Derivative`<:class:`~org.hipparchus.analysis.differentiation.Gradient`>, :class:`~org.hipparchus.CalculusFieldElement`<:class:`~org.hipparchus.analysis.differentiation.Gradient`>, Serializable
    
        Class representing both the value and the differentials of a function.
    
        This class is a stripped-down version of :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` with
        :meth:`~org.hipparchus.analysis.differentiation.DerivativeStructure.getOrder` limited to one. It should have less
        overhead than :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` in its domain.
    
        This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout
        mathematical expressions; they hold the derivative together with the value of a function.
    
        :class:`~org.hipparchus.analysis.differentiation.Gradient` instances can be used directly thanks to the arithmetic
        operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.7
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.FieldGradient`, :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, double: float, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, derivativeStructure: DerivativeStructure): ...
    def abs(self) -> 'Gradient':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.abs` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'Gradient':
        """
            Arc cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'Gradient':
        """
            Inverse hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.acosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'Gradient':
        """
            '+' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.add` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
            Compute this + a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.add` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.Gradient`): element to add
        
            Returns:
                a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, gradient: 'Gradient') -> 'Gradient': ...
    def asin(self) -> 'Gradient':
        """
            Arc sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'Gradient':
        """
            Inverse hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.asinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'Gradient':
        """
            Arc tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, gradient: 'Gradient') -> 'Gradient':
        """
            Two arguments arc tangent operation.
        
            Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with
            arguments order, the instance is the *first* argument and the single provided argument is the *second* argument. In
            order to be consistent with programming languages :code:`atan2`, this method computes :code:`atan2(this, x)`, i.e. the
            instance represents the :code:`y` argument and the :code:`x` argument is the one passed as a single argument. This may
            seem confusing especially for users of Wolfram alpha, as this site is *not* consistent with programming languages
            :code:`atan2` two-arguments arc tangent and puts :code:`x` as its first argument.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atan2` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second argument of the arc tangent
        
            Returns:
        
        """
        ...
    def atanh(self) -> 'Gradient':
        """
            Inverse hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.atanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'Gradient':
        """
            Cubic root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cbrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'Gradient':
        """
            Get the smallest whole number larger than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ceil` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compose(self, doubleArray: typing.List[float]) -> 'Gradient':
        """
            Compute composition of the instance by a univariate function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.compose`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Parameters:
                f (double...): array of value and derivatives of the function at the current point (i.e.
                    [f(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`),
                    f'(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`),
                    f''(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`)...]).
        
            Returns:
                f(this)
        
        
        """
        ...
    @staticmethod
    def constant(int: int, double: float) -> 'Gradient':
        """
            Build an instance corresponding to a constant value.
        
            Parameters:
                freeParameters (int): number of free parameters (i.e. dimension of the gradient)
                value (double): constant value of the function
        
            Returns:
                a :code:`Gradient` with a constant value and all derivatives set to 0.0
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'Gradient':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (:class:`~org.hipparchus.analysis.differentiation.Gradient`): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.copySign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                sign (double): the sign for the returned value
        
            Returns:
                the instance with the same sign as the :code:`sign` argument
        
        
        """
        ...
    @typing.overload
    def copySign(self, gradient: 'Gradient') -> 'Gradient': ...
    def cos(self) -> 'Gradient':
        """
            Cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cos` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'Gradient':
        """
            Hyperbolic cosine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.cosh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'Gradient':
        """
            '÷' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.divide` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
            Compute this ÷ a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.divide` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.Gradient`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, gradient: 'Gradient') -> 'Gradient': ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two univariate derivatives.
        
            univariate derivatives are considered equal if they have the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'Gradient':
        """
            Exponential.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.exp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'Gradient':
        """
            Exponential minus 1.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.expm1` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'Gradient':
        """
            Get the largest whole number smaller than instance.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.floor` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                floor(this)
        
        
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
    def getField(self) -> GradientField:
        """
            Get the :class:`~org.hipparchus.Field` to which the instance belongs.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.getField` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                :class:`~org.hipparchus.Field` to which the instance belongs
        
        
        """
        ...
    def getFreeParameters(self) -> int:
        """
            Get the number of free parameters.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getFreeParameters`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                number of free parameters
        
        
        """
        ...
    def getGradient(self) -> typing.List[float]:
        """
            Get the gradient part of the function.
        
            Returns:
                gradient part of the value of the function
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.Gradient.getPartialDerivative`
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the derivation order.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getOrder`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                derivation order
        
        
        """
        ...
    @typing.overload
    def getPartialDerivative(self, int: int) -> float: ...
    @typing.overload
    def getPartialDerivative(self, intArray: typing.List[int]) -> float: ...
    def getPi(self) -> 'Gradient':
        """
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.getPi` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                Archimedes constant Ï€
        
        
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
    def getValue(self) -> float:
        """
            Get the value part of the function.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                value part of the value of the function
        
        
        """
        ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the univariate derivative.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, gradient: 'Gradient') -> 'Gradient':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2` Â +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.hypot` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.Gradient`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, gradient: 'Gradient', double2: float, gradient2: 'Gradient') -> 'Gradient':
        """
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the third term
                a4 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`Â in
                interfaceÂ :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.Gradient`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, gradient: 'Gradient', double2: float, gradient2: 'Gradient', double3: float, gradient3: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, double: float, gradient: 'Gradient', double2: float, gradient2: 'Gradient', double3: float, gradient3: 'Gradient', double4: float, gradient4: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], gradientArray: typing.List['Gradient']) -> 'Gradient':
        """
            Compute a linear combination.
        
            Specified by:
                 in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.Gradient`[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.Gradient`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
            Compute a linear combination.
        
            Specified by:
                 in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.Gradient`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, gradient: 'Gradient', gradient2: 'Gradient', gradient3: 'Gradient', gradient4: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, gradient: 'Gradient', gradient2: 'Gradient', gradient3: 'Gradient', gradient4: 'Gradient', gradient5: 'Gradient', gradient6: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, gradient: 'Gradient', gradient2: 'Gradient', gradient3: 'Gradient', gradient4: 'Gradient', gradient5: 'Gradient', gradient6: 'Gradient', gradient7: 'Gradient', gradient8: 'Gradient') -> 'Gradient': ...
    @typing.overload
    def linearCombination(self, gradientArray: typing.List['Gradient'], gradientArray2: typing.List['Gradient']) -> 'Gradient': ...
    def log(self) -> 'Gradient':
        """
            Natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'Gradient':
        """
            Base 10 logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log10` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'Gradient':
        """
            Shifted natural logarithm.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.log1p` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'Gradient':
        """
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
            '×' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.multiply` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this×a
        
            Compute this × a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.multiply` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.Gradient`): element to multiply
        
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
            Returns the additive inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.negate` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'Gradient':
        """
            Create an instance corresponding to a constant real value.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.newInstance` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                c (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'Gradient':
        """
            Compute a :sup:`x` where a is a double and x a :class:`~org.hipparchus.analysis.differentiation.Gradient`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.Gradient`): power to apply
        
            Returns:
                a :sup:`x`
        
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
                e (:class:`~org.hipparchus.analysis.differentiation.Gradient`): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'Gradient': ...
    @typing.overload
    def pow(self, gradient: 'Gradient') -> 'Gradient': ...
    @typing.overload
    @staticmethod
    def pow(double: float, gradient: 'Gradient') -> 'Gradient': ...
    def reciprocal(self) -> 'Gradient':
        """
            Returns the multiplicative inverse of :code:`this` element.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.reciprocal` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.reciprocal` in interface :class:`~org.hipparchus.FieldElement`
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'Gradient':
        """
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.remainder` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.Gradient`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, gradient: 'Gradient') -> 'Gradient': ...
    def rint(self) -> 'Gradient':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.rint` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'Gradient':
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
    def scalb(self, int: int) -> 'Gradient':
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
    def sign(self) -> 'Gradient':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sign` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'Gradient':
        """
            Sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sin` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['Gradient']: ...
    def sinh(self) -> 'Gradient':
        """
            Hyperbolic sine operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sinh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['Gradient']: ...
    def sqrt(self) -> 'Gradient':
        """
            Square root.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.sqrt` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'Gradient':
        """
            '-' operator.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.subtract` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
            Compute this - a.
        
            Specified by:
                :meth:`~org.hipparchus.FieldElement.subtract` in interface :class:`~org.hipparchus.FieldElement`
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.Gradient`): element to subtract
        
            Returns:
                a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, gradient: 'Gradient') -> 'Gradient': ...
    def tan(self) -> 'Gradient':
        """
            Tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tan` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'Gradient':
        """
            Hyperbolic tangent operation.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.tanh` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def taylor(self, doubleArray: typing.List[float]) -> float:
        """
            Evaluate Taylor expansion a derivative structure.
        
            Parameters:
                delta (double...): parameters offsets (Δx, Δy, ...)
        
            Returns:
                value of the Taylor expansion at x + Δx, y + Δy, ...
        
        
        """
        ...
    def toDegrees(self) -> 'Gradient':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toDegrees` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
            Convert the instance to a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`.
        
            Returns:
                derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'Gradient':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.toRadians` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'Gradient':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            The :code:`ulp` function is a step function, hence all its derivatives are 0.
        
            Specified by:
                :meth:`~org.hipparchus.CalculusFieldElement.ulp` in interface :class:`~org.hipparchus.CalculusFieldElement`
        
            Returns:
                ulp(this)
        
            Since:
                2.0
        
        
        """
        ...
    @staticmethod
    def variable(int: int, int2: int, double: float) -> 'Gradient':
        """
            Build a :code:`Gradient` representing a variable.
        
            Instances built using this method are considered to be the free variables with respect to which differentials are
            computed. As such, their differential with respect to themselves is +1.
        
            Parameters:
                freeParameters (int): number of free parameters (i.e. dimension of the gradient)
                index (int): index of the variable (from 0 to :meth:`~org.hipparchus.analysis.differentiation.Gradient.getFreeParameters` - 1)
                value (double): value of the variable
        
            Returns:
                a :code:`Gradient` with a constant value and all derivatives set to 0.0 except the one at :code:`index` which will be
                set to 1.0
        
        
        """
        ...

_UnivariateDerivative__T = typing.TypeVar('_UnivariateDerivative__T', bound='UnivariateDerivative')  # <T>
class UnivariateDerivative(Derivative[_UnivariateDerivative__T], org.hipparchus.CalculusFieldElement[_UnivariateDerivative__T], java.io.Serializable, typing.Generic[_UnivariateDerivative__T]):
    """
    public abstract class UnivariateDerivative<T extends UnivariateDerivative<T>> extends Object implements :class:`~org.hipparchus.analysis.differentiation.Derivative`<T>, :class:`~org.hipparchus.CalculusFieldElement`<T>, Serializable
    
        Abstract class representing both the value and the differentials of a function.
    
        Since:
            1.7
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def getDerivative(self, int: int) -> float: ...
    def getFreeParameters(self) -> int:
        """
            Get the number of free parameters.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.Derivative.getFreeParameters`Â in
                interfaceÂ :class:`~org.hipparchus.analysis.differentiation.Derivative`
        
            Returns:
                number of free parameters
        
        
        """
        ...
    def getPartialDerivative(self, intArray: typing.List[int]) -> float: ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
            Convert the instance to a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`.
        
            Returns:
                derivative structure with same value and derivative as the instance
        
        
        """
        ...

_FieldUnivariateDerivative1__T = typing.TypeVar('_FieldUnivariateDerivative1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative1(FieldUnivariateDerivative[_FieldUnivariateDerivative1__T, 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], typing.Generic[_FieldUnivariateDerivative1__T]):
    """
    public class FieldUnivariateDerivative1<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative`<T,:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<T>>
    
        Class representing both the value and the differentials of a function.
    
        This class is a stripped-down version of :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` with
        only one :meth:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure.getFreeParameters` and
        :meth:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure.getOrder` also limited to one. It should have
        less overhead than :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` in its domain.
    
        This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout
        mathematical expressions; they hold the derivative together with the value of a function.
    
        :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1` instances can be used directly thanks to
        the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.7
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.Gradient`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.FieldGradient`
    """
    @typing.overload
    def __init__(self, t: _FieldUnivariateDerivative1__T, t2: _FieldUnivariateDerivative1__T): ...
    @typing.overload
    def __init__(self, fieldDerivativeStructure: FieldDerivativeStructure[_FieldUnivariateDerivative1__T]): ...
    def abs(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def acos(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def acosh(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def add(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def add(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def add(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def asin(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def asinh(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def atan(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def atan2(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def atanh(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def cbrt(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def ceil(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def compose(self, t: _FieldUnivariateDerivative1__T, t2: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def copySign(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def copySign(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def cos(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def cosh(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def divide(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def divide(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def divide(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two univariate derivatives.
        
            univariate derivatives are considered equal if they have the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def expm1(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def floor(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def getDerivative(self, int: int) -> _FieldUnivariateDerivative1__T:
        """
            Get a derivative from the univariate derivative.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative.getDerivative`Â in
                classÂ :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative`
        
            Parameters:
                n (int): derivation order (must be between 0 and
                    :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1.getOrder`, both inclusive)
        
            Returns:
                n :sup:`th` derivative, or :code:`NaN` if n is either negative or strictly larger than
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1.getOrder`
        
        
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
    def getField(self) -> FieldUnivariateDerivative1Field[_FieldUnivariateDerivative1__T]: ...
    def getFirstDerivative(self) -> _FieldUnivariateDerivative1__T:
        """
            Get the first derivative.
        
            Returns:
                first derivative
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1.getValue`
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the derivation order.
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPi(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Returns:
                real value
        
        
        """
        ...
    def getValue(self) -> _FieldUnivariateDerivative1__T:
        """
            Get the value part of the univariate derivative.
        
            Returns:
                value part of the univariate derivative
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FieldUnivariateDerivative1__T]: ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the univariate derivative.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], double2: float, fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], double2: float, fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], double3: float, fieldUnivariateDerivative13: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], double2: float, fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], double3: float, fieldUnivariateDerivative13: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], double4: float, fieldUnivariateDerivative14: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], fieldUnivariateDerivative1Array: typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, t: _FieldUnivariateDerivative1__T, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], t2: _FieldUnivariateDerivative1__T, fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], t3: _FieldUnivariateDerivative1__T, fieldUnivariateDerivative13: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, tArray: typing.List[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative1Array: typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative13: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative14: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative13: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative14: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative15: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative16: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative12: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative13: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative14: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative15: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative16: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative17: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T], fieldUnivariateDerivative18: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative1Array: typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]], fieldUnivariateDerivative1Array2: typing.List['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def log(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def log10(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def log1p(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def multiply(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def negate(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def newInstance(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def pow(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    @staticmethod
    def pow(double: float, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_pow_3__T]) -> 'FieldUnivariateDerivative1'[_pow_3__T]:
        """
            Compute a :sup:`x` where a is a double and x a
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<T> x): power to apply
        
            Returns:
                a :sup:`x`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`> pow(double p)
        
            Power operation.
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`> pow(int n)
        
            Integer power operation.
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`> pow(:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`> e)
        
            Power operation.
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`> e): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    def reciprocal(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def remainder(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def remainder(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def rint(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def rootN(self, int: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def scalb(self, int: int) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def sign(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def sin(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]]: ...
    def sinh(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]]: ...
    def sqrt(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def subtract(self, t: _FieldUnivariateDerivative1__T) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def subtract(self, fieldUnivariateDerivative1: 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def tan(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def tanh(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    @typing.overload
    def taylor(self, double: float) -> _FieldUnivariateDerivative1__T:
        """
            Evaluate Taylor expansion of a univariate derivative.
        
            Parameters:
                delta (double): parameter offset Î”x
        
            Returns:
                value of the Taylor expansion at x + Î”x
        
            Evaluate Taylor expansion of a univariate derivative.
        
            Parameters:
                delta (:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`): parameter offset Î”x
        
            Returns:
                value of the Taylor expansion at x + Î”x
        
        
        """
        ...
    @typing.overload
    def taylor(self, t: _FieldUnivariateDerivative1__T) -> _FieldUnivariateDerivative1__T: ...
    def toDegrees(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldUnivariateDerivative1__T]: ...
    def toRadians(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...
    def ulp(self) -> 'FieldUnivariateDerivative1'[_FieldUnivariateDerivative1__T]: ...

_FieldUnivariateDerivative2__T = typing.TypeVar('_FieldUnivariateDerivative2__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldUnivariateDerivative2(FieldUnivariateDerivative[_FieldUnivariateDerivative2__T, 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], typing.Generic[_FieldUnivariateDerivative2__T]):
    """
    public class FieldUnivariateDerivative2<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative`<T,:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<T>>
    
        Class representing both the value and the differentials of a function.
    
        This class is a stripped-down version of :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` with
        only one :meth:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure.getFreeParameters` and
        :meth:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure.getOrder` limited to two. It should have less
        overhead than :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure` in its domain.
    
        This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout
        mathematical expressions; they hold the derivative together with the value of a function.
    
        :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2` instances can be used directly thanks to
        the arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.7
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.Gradient`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.FieldGradient`
    """
    @typing.overload
    def __init__(self, t: _FieldUnivariateDerivative2__T, t2: _FieldUnivariateDerivative2__T, t3: _FieldUnivariateDerivative2__T): ...
    @typing.overload
    def __init__(self, fieldDerivativeStructure: FieldDerivativeStructure[_FieldUnivariateDerivative2__T]): ...
    def abs(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def acos(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def acosh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def add(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def add(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def add(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def asin(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def asinh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def atan(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def atan2(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def atanh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def cbrt(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def ceil(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def compose(self, t: _FieldUnivariateDerivative2__T, t2: _FieldUnivariateDerivative2__T, t3: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def copySign(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def copySign(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def copySign(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def cos(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def cosh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def divide(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def divide(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def divide(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two univariate derivatives.
        
            univariate derivatives are considered equal if they have the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def expm1(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def floor(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def getDerivative(self, int: int) -> _FieldUnivariateDerivative2__T:
        """
            Get a derivative from the univariate derivative.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative.getDerivative`Â in
                classÂ :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative`
        
            Parameters:
                n (int): derivation order (must be between 0 and
                    :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2.getOrder`, both inclusive)
        
            Returns:
                n :sup:`th` derivative, or :code:`NaN` if n is either negative or strictly larger than
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2.getOrder`
        
        
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
    def getField(self) -> FieldUnivariateDerivative2Field[_FieldUnivariateDerivative2__T]: ...
    def getFirstDerivative(self) -> _FieldUnivariateDerivative2__T:
        """
            Get the first derivative.
        
            Returns:
                first derivative
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2.getValue`
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the derivation order.
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPi(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Returns:
                real value
        
        
        """
        ...
    def getSecondDerivative(self) -> _FieldUnivariateDerivative2__T:
        """
            Get the second derivative.
        
            Returns:
                second derivative
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2.getValue`,
                :meth:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2.getFirstDerivative`
        
        
        """
        ...
    def getValue(self) -> _FieldUnivariateDerivative2__T:
        """
            Get the value part of the univariate derivative.
        
            Returns:
                value part of the univariate derivative
        
        
        """
        ...
    def getValueField(self) -> org.hipparchus.Field[_FieldUnivariateDerivative2__T]: ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the univariate derivative.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], double2: float, fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], double2: float, fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], double3: float, fieldUnivariateDerivative23: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, double: float, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], double2: float, fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], double3: float, fieldUnivariateDerivative23: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], double4: float, fieldUnivariateDerivative24: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], fieldUnivariateDerivative2Array: typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, t: _FieldUnivariateDerivative2__T, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], t2: _FieldUnivariateDerivative2__T, fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], t3: _FieldUnivariateDerivative2__T, fieldUnivariateDerivative23: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, tArray: typing.List[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative2Array: typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative23: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative24: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative23: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative24: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative25: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative26: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative22: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative23: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative24: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative25: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative26: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative27: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T], fieldUnivariateDerivative28: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def linearCombination(self, fieldUnivariateDerivative2Array: typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]], fieldUnivariateDerivative2Array2: typing.List['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def log(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def log10(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def log1p(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, int: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def multiply(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def negate(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def newInstance(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    _pow_3__T = typing.TypeVar('_pow_3__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def pow(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def pow(self, int: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def pow(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    @staticmethod
    def pow(double: float, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_pow_3__T]) -> 'FieldUnivariateDerivative2'[_pow_3__T]:
        """
            Compute a :sup:`x` where a is a double and x a
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<T> x): power to apply
        
            Returns:
                a :sup:`x`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`> pow(double p)
        
            Power operation.
        
            Parameters:
                p (double): power to apply
        
            Returns:
                this :sup:`p`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`> pow(int n)
        
            Integer power operation.
        
            Parameters:
                n (int): power to apply
        
            Returns:
                this :sup:`n`
        
        public :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`> pow(:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`> e)
        
            Power operation.
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`<:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`> e): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    def reciprocal(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def remainder(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def remainder(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def remainder(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def rint(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def rootN(self, int: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def scalb(self, int: int) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def sign(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def sin(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]: ...
    def sinh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]]: ...
    def sqrt(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def subtract(self, double: float) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def subtract(self, t: _FieldUnivariateDerivative2__T) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def subtract(self, fieldUnivariateDerivative2: 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def tan(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def tanh(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    @typing.overload
    def taylor(self, double: float) -> _FieldUnivariateDerivative2__T:
        """
            Evaluate Taylor expansion a univariate derivative.
        
            Parameters:
                delta (double): parameter offset Î”x
        
            Returns:
                value of the Taylor expansion at x + Î”x
        
            Evaluate Taylor expansion a univariate derivative.
        
            Parameters:
                delta (:class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`): parameter offset Î”x
        
            Returns:
                value of the Taylor expansion at x + Î”x
        
        
        """
        ...
    @typing.overload
    def taylor(self, t: _FieldUnivariateDerivative2__T) -> _FieldUnivariateDerivative2__T: ...
    def toDegrees(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def toDerivativeStructure(self) -> FieldDerivativeStructure[_FieldUnivariateDerivative2__T]: ...
    def toRadians(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...
    def ulp(self) -> 'FieldUnivariateDerivative2'[_FieldUnivariateDerivative2__T]: ...

class UnivariateDerivative1(UnivariateDerivative['UnivariateDerivative1']):
    """
    public class UnivariateDerivative1 extends :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative`<:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`>
    
        Class representing both the value and the differentials of a function.
    
        This class is a stripped-down version of :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` with only
        one :meth:`~org.hipparchus.analysis.differentiation.DerivativeStructure.getFreeParameters` and
        :meth:`~org.hipparchus.analysis.differentiation.DerivativeStructure.getOrder` also limited to one. It should have less
        overhead than :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` in its domain.
    
        This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout
        mathematical expressions; they hold the derivative together with the value of a function.
    
        :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1` instances can be used directly thanks to the
        arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.7
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.Gradient`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative1`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.FieldGradient`, :meth:`~serialized`
    """
    PI: typing.ClassVar['UnivariateDerivative1'] = ...
    """
    public static final :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1` PI
    
        The constant value of Ï€ as a :code:`UnivariateDerivative1`.
    
        Since:
            2.0
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float): ...
    @typing.overload
    def __init__(self, derivativeStructure: DerivativeStructure): ...
    def abs(self) -> 'UnivariateDerivative1':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
            Returns:
                abs(this)
        
        
        """
        ...
    def acos(self) -> 'UnivariateDerivative1':
        """
            Arc cosine operation.
        
            Returns:
                acos(this)
        
        
        """
        ...
    def acosh(self) -> 'UnivariateDerivative1':
        """
            Inverse hyperbolic cosine operation.
        
            Returns:
                acosh(this)
        
        
        """
        ...
    @typing.overload
    def add(self, double: float) -> 'UnivariateDerivative1':
        """
            '+' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
            Compute this + a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): element to add
        
            Returns:
                a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def asin(self) -> 'UnivariateDerivative1':
        """
            Arc sine operation.
        
            Returns:
                asin(this)
        
        
        """
        ...
    def asinh(self) -> 'UnivariateDerivative1':
        """
            Inverse hyperbolic sine operation.
        
            Returns:
                asin(this)
        
        
        """
        ...
    def atan(self) -> 'UnivariateDerivative1':
        """
            Arc tangent operation.
        
            Returns:
                atan(this)
        
        
        """
        ...
    def atan2(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1':
        """
            Two arguments arc tangent operation.
        
            Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with
            arguments order, the instance is the *first* argument and the single provided argument is the *second* argument. In
            order to be consistent with programming languages :code:`atan2`, this method computes :code:`atan2(this, x)`, i.e. the
            instance represents the :code:`y` argument and the :code:`x` argument is the one passed as a single argument. This may
            seem confusing especially for users of Wolfram alpha, as this site is *not* consistent with programming languages
            :code:`atan2` two-arguments arc tangent and puts :code:`x` as its first argument.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second argument of the arc tangent
        
            Returns:
        
        """
        ...
    def atanh(self) -> 'UnivariateDerivative1':
        """
            Inverse hyperbolic tangent operation.
        
            Returns:
                atanh(this)
        
        
        """
        ...
    def cbrt(self) -> 'UnivariateDerivative1':
        """
            Cubic root.
        
            Returns:
                cubic root of the instance
        
        
        """
        ...
    def ceil(self) -> 'UnivariateDerivative1':
        """
            Get the smallest whole number larger than instance.
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compose(self, doubleArray: typing.List[float]) -> 'UnivariateDerivative1':
        """
            Compute composition of the instance by a univariate function.
        
            Parameters:
                f (double...): array of value and derivatives of the function at the current point (i.e.
                    [f(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`),
                    f'(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`),
                    f''(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`)...]).
        
            Returns:
                f(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'UnivariateDerivative1':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                sign (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): the sign for the returned value
        
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
    def copySign(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def cos(self) -> 'UnivariateDerivative1':
        """
            Cosine operation.
        
            Returns:
                cos(this)
        
        
        """
        ...
    def cosh(self) -> 'UnivariateDerivative1':
        """
            Hyperbolic cosine operation.
        
            Returns:
                cosh(this)
        
        
        """
        ...
    @typing.overload
    def divide(self, double: float) -> 'UnivariateDerivative1':
        """
            '÷' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
            Compute this ÷ a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two univariate derivatives.
        
            univariate derivatives are considered equal if they have the same derivatives.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality to this
        
            Returns:
                true if two univariate derivatives are equal
        
        
        """
        ...
    def exp(self) -> 'UnivariateDerivative1':
        """
            Exponential.
        
            Returns:
                exponential of the instance
        
        
        """
        ...
    def expm1(self) -> 'UnivariateDerivative1':
        """
            Exponential minus 1.
        
            Returns:
                exponential minus one of the instance
        
        
        """
        ...
    def floor(self) -> 'UnivariateDerivative1':
        """
            Get the largest whole number smaller than instance.
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getDerivative(self, int: int) -> float:
        """
            Get a derivative from the univariate derivative.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative.getDerivative`Â in
                classÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative`
        
            Parameters:
                n (int): derivation order (must be between 0 and :meth:`~org.hipparchus.analysis.differentiation.Derivative.getOrder`, both
                    inclusive)
        
            Returns:
                n :sup:`th` derivative
        
        
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
    def getField(self) -> UnivariateDerivative1Field:
        """
            Get the :class:`~org.hipparchus.Field` to which the instance belongs.
        
            Returns:
                :class:`~org.hipparchus.Field` to which the instance belongs
        
        
        """
        ...
    def getFirstDerivative(self) -> float:
        """
            Get the first derivative.
        
            Returns:
                first derivative
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1.getValue`
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the derivation order.
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPi(self) -> 'UnivariateDerivative1':
        """
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Returns:
                Archimedes constant Ï€
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
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
    def hashCode(self) -> int:
        """
            Get a hashCode for the univariate derivative.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2` Â +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, univariateDerivative1: 'UnivariateDerivative1', double2: float, univariateDerivative12: 'UnivariateDerivative1') -> 'UnivariateDerivative1':
        """
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the third term
                a4 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, univariateDerivative1: 'UnivariateDerivative1', double2: float, univariateDerivative12: 'UnivariateDerivative1', double3: float, univariateDerivative13: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, double: float, univariateDerivative1: 'UnivariateDerivative1', double2: float, univariateDerivative12: 'UnivariateDerivative1', double3: float, univariateDerivative13: 'UnivariateDerivative1', double4: float, univariateDerivative14: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], univariateDerivative1Array: typing.List['UnivariateDerivative1']) -> 'UnivariateDerivative1':
        """
            Compute a linear combination.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
            Compute a linear combination.
        
            Parameters:
                a (double[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, univariateDerivative1: 'UnivariateDerivative1', univariateDerivative12: 'UnivariateDerivative1', univariateDerivative13: 'UnivariateDerivative1', univariateDerivative14: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, univariateDerivative1: 'UnivariateDerivative1', univariateDerivative12: 'UnivariateDerivative1', univariateDerivative13: 'UnivariateDerivative1', univariateDerivative14: 'UnivariateDerivative1', univariateDerivative15: 'UnivariateDerivative1', univariateDerivative16: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, univariateDerivative1: 'UnivariateDerivative1', univariateDerivative12: 'UnivariateDerivative1', univariateDerivative13: 'UnivariateDerivative1', univariateDerivative14: 'UnivariateDerivative1', univariateDerivative15: 'UnivariateDerivative1', univariateDerivative16: 'UnivariateDerivative1', univariateDerivative17: 'UnivariateDerivative1', univariateDerivative18: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    def linearCombination(self, univariateDerivative1Array: typing.List['UnivariateDerivative1'], univariateDerivative1Array2: typing.List['UnivariateDerivative1']) -> 'UnivariateDerivative1': ...
    def log(self) -> 'UnivariateDerivative1':
        """
            Natural logarithm.
        
            Returns:
                logarithm of the instance
        
        
        """
        ...
    def log10(self) -> 'UnivariateDerivative1':
        """
            Base 10 logarithm.
        
            Returns:
                base 10 logarithm of the instance
        
        
        """
        ...
    def log1p(self) -> 'UnivariateDerivative1':
        """
            Shifted natural logarithm.
        
            Returns:
                logarithm of one plus the instance
        
        
        """
        ...
    @typing.overload
    def multiply(self, double: float) -> 'UnivariateDerivative1':
        """
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
            '×' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this×a
        
            Compute this × a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): element to multiply
        
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
            Returns the additive inverse of :code:`this` element.
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'UnivariateDerivative1':
        """
            Create an instance corresponding to a constant real value.
        
            Parameters:
                value (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'UnivariateDerivative1':
        """
            Compute a :sup:`x` where a is a double and x a :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): power to apply
        
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
        
            Power operation.
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'UnivariateDerivative1': ...
    @typing.overload
    def pow(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    @typing.overload
    @staticmethod
    def pow(double: float, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def reciprocal(self) -> 'UnivariateDerivative1':
        """
            Returns the multiplicative inverse of :code:`this` element.
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'UnivariateDerivative1':
        """
            IEEE remainder operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def rint(self) -> 'UnivariateDerivative1':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'UnivariateDerivative1':
        """
            N :sup:`th` root.
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, int: int) -> 'UnivariateDerivative1':
        """
            Multiply the instance by a power of 2.
        
            Parameters:
                n (int): power of 2
        
            Returns:
                this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'UnivariateDerivative1':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'UnivariateDerivative1':
        """
            Sine operation.
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['UnivariateDerivative1']: ...
    def sinh(self) -> 'UnivariateDerivative1':
        """
            Hyperbolic sine operation.
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['UnivariateDerivative1']: ...
    def sqrt(self) -> 'UnivariateDerivative1':
        """
            Square root.
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'UnivariateDerivative1':
        """
            '-' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
            Compute this - a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative1`): element to subtract
        
            Returns:
                a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, univariateDerivative1: 'UnivariateDerivative1') -> 'UnivariateDerivative1': ...
    def tan(self) -> 'UnivariateDerivative1':
        """
            Tangent operation.
        
            Returns:
                tan(this)
        
        
        """
        ...
    def tanh(self) -> 'UnivariateDerivative1':
        """
            Hyperbolic tangent operation.
        
            Returns:
                tanh(this)
        
        
        """
        ...
    def taylor(self, double: float) -> float:
        """
            Evaluate Taylor expansion a univariate derivative.
        
            Parameters:
                delta (double): parameter offset Î”x
        
            Returns:
                value of the Taylor expansion at x + Î”x
        
        
        """
        ...
    def toDegrees(self) -> 'UnivariateDerivative1':
        """
            Convert radians to degrees, with error of less than 0.5 ULP
        
            Returns:
                instance converted into degrees
        
        
        """
        ...
    def toDerivativeStructure(self) -> DerivativeStructure:
        """
            Convert the instance to a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative.toDerivativeStructure`Â in
                classÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative`
        
            Returns:
                derivative structure with same value and derivative as the instance
        
        
        """
        ...
    def toRadians(self) -> 'UnivariateDerivative1':
        """
            Convert degrees to radians, with error of less than 0.5 ULP
        
            Returns:
                instance converted into radians
        
        
        """
        ...
    def ulp(self) -> 'UnivariateDerivative1':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            The :code:`ulp` function is a step function, hence all its derivatives are 0.
        
            Returns:
                ulp(this)
        
            Since:
                2.0
        
        
        """
        ...

class UnivariateDerivative2(UnivariateDerivative['UnivariateDerivative2']):
    """
    public class UnivariateDerivative2 extends :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative`<:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`>
    
        Class representing both the value and the differentials of a function.
    
        This class is a stripped-down version of :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` with only
        one :meth:`~org.hipparchus.analysis.differentiation.DerivativeStructure.getFreeParameters` and
        :meth:`~org.hipparchus.analysis.differentiation.DerivativeStructure.getOrder` also limited to two. It should have less
        overhead than :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure` in its domain.
    
        This class is an implementation of Rall's numbers. Rall's numbers are an extension to the real numbers used throughout
        mathematical expressions; they hold the derivative together with the value of a function.
    
        :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2` instances can be used directly thanks to the
        arithmetic operators to the mathematical functions provided as methods by this class (+, -, *, /, %, sin, cos ...).
    
        Implementing complex expressions by hand using these classes is a tedious and error-prone task but has the advantage of
        having no limitation on the derivation order despite not requiring users to compute the derivatives by themselves.
    
        Instances of this class are guaranteed to be immutable.
    
        Since:
            1.7
    
        Also see:
            :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.Gradient`,
            :class:`~org.hipparchus.analysis.differentiation.FieldDerivativeStructure`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.FieldUnivariateDerivative2`,
            :class:`~org.hipparchus.analysis.differentiation.FieldGradient`, :meth:`~serialized`
    """
    PI: typing.ClassVar['UnivariateDerivative2'] = ...
    """
    public static final :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2` PI
    
        The constant value of Ï€ as a :code:`UnivariateDerivative2`.
    
        Since:
            2.0
    
    
    """
    @typing.overload
    def __init__(self, double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, derivativeStructure: DerivativeStructure): ...
    def abs(self) -> 'UnivariateDerivative2':
        """
            absolute value.
        
            Just another name for :meth:`~org.hipparchus.CalculusFieldElement.norm`
        
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
    def add(self, double: float) -> 'UnivariateDerivative2':
        """
            '+' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this+a
        
            Compute this + a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): element to add
        
            Returns:
                a new element representing this + a
        
        
        """
        ...
    @typing.overload
    def add(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
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
    def atan2(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2':
        """
            Two arguments arc tangent operation.
        
            Beware of the order or arguments! As this is based on a two-arguments functions, in order to be consistent with
            arguments order, the instance is the *first* argument and the single provided argument is the *second* argument. In
            order to be consistent with programming languages :code:`atan2`, this method computes :code:`atan2(this, x)`, i.e. the
            instance represents the :code:`y` argument and the :code:`x` argument is the one passed as a single argument. This may
            seem confusing especially for users of Wolfram alpha, as this site is *not* consistent with programming languages
            :code:`atan2` two-arguments arc tangent and puts :code:`x` as its first argument.
        
            Parameters:
                x (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second argument of the arc tangent
        
            Returns:
        
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
    def ceil(self) -> 'UnivariateDerivative2':
        """
            Get the smallest whole number larger than instance.
        
            Returns:
                ceil(this)
        
        
        """
        ...
    def compose(self, doubleArray: typing.List[float]) -> 'UnivariateDerivative2':
        """
            Compute composition of the instance by a univariate function.
        
            Parameters:
                f (double...): array of value and derivatives of the function at the current point (i.e.
                    [f(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`),
                    f'(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`),
                    f''(:meth:`~org.hipparchus.analysis.differentiation.Derivative.getValue`)...]).
        
            Returns:
                f(this)
        
        
        """
        ...
    @typing.overload
    def copySign(self, double: float) -> 'UnivariateDerivative2':
        """
            Returns the instance with the sign of the argument. A NaN :code:`sign` argument is treated as positive.
        
            Parameters:
                sign (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): the sign for the returned value
        
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
    def copySign(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
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
    def divide(self, double: float) -> 'UnivariateDerivative2':
        """
            '÷' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this÷a
        
            Compute this ÷ a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): element to divide by
        
            Returns:
                a new element representing this ÷ a
        
        
        """
        ...
    @typing.overload
    def divide(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two univariate derivatives.
        
            univariate derivatives are considered equal if they have the same derivatives.
        
            Overrides:
                 in class 
        
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
    def floor(self) -> 'UnivariateDerivative2':
        """
            Get the largest whole number smaller than instance.
        
            Returns:
                floor(this)
        
        
        """
        ...
    def getDerivative(self, int: int) -> float:
        """
            Get a derivative from the univariate derivative.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative.getDerivative`Â in
                classÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative`
        
            Parameters:
                n (int): derivation order (must be between 0 and :meth:`~org.hipparchus.analysis.differentiation.Derivative.getOrder`, both
                    inclusive)
        
            Returns:
                n :sup:`th` derivative
        
        
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
    def getField(self) -> UnivariateDerivative2Field:
        """
            Get the :class:`~org.hipparchus.Field` to which the instance belongs.
        
            Returns:
                :class:`~org.hipparchus.Field` to which the instance belongs
        
        
        """
        ...
    def getFirstDerivative(self) -> float:
        """
            Get the first derivative.
        
            Returns:
                first derivative
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2.getValue`,
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2.getSecondDerivative`
        
        
        """
        ...
    def getOrder(self) -> int:
        """
            Get the derivation order.
        
            Returns:
                derivation order
        
        
        """
        ...
    def getPi(self) -> 'UnivariateDerivative2':
        """
            Get the Archimedes constant Ï€.
        
            Archimedes constant is the ratio of a circle's circumference to its diameter.
        
            Returns:
                Archimedes constant Ï€
        
        
        """
        ...
    def getReal(self) -> float:
        """
            Get the real value of the number.
        
            Returns:
                real value
        
        
        """
        ...
    def getSecondDerivative(self) -> float:
        """
            Get the second derivative.
        
            Returns:
                second derivative
        
            Also see:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2.getValue`,
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2.getFirstDerivative`
        
        
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
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def hypot(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2':
        """
            Returns the hypotenuse of a triangle with sides :code:`this` and :code:`y` - sqrt(*this* :sup:`2` Â +*y* :sup:`2` )
            avoiding intermediate overflow or underflow.
        
              - If either argument is infinite, then the result is positive infinity.
              - else, if either argument is NaN then the result is NaN.
        
        
            Parameters:
                y (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): a value
        
            Returns:
                sqrt(*this* :sup:`2`  +*y* :sup:`2` )
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, univariateDerivative2: 'UnivariateDerivative2', double2: float, univariateDerivative22: 'UnivariateDerivative2') -> 'UnivariateDerivative2':
        """
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the second term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the third term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the first term
                a2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the second term
                a3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the third term
                a4 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
            Compute a linear combination.
        
            Parameters:
                a1 (double): first factor of the first term
                b1 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the first term
                a2 (double): first factor of the second term
                b2 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the second term
                a3 (double): first factor of the third term
                b3 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the third term
                a4 (double): first factor of the fourth term
                b4 (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): second factor of the fourth term
        
            Returns:
                a :sub:`1` ×b :sub:`1` + a :sub:`2` ×b :sub:`2` + a :sub:`3` ×b :sub:`3` + a :sub:`4` ×b :sub:`4`
        
            Also see:
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`,
                :meth:`~org.hipparchus.CalculusFieldElement.linearCombination`
        
        
        """
        ...
    @typing.overload
    def linearCombination(self, double: float, univariateDerivative2: 'UnivariateDerivative2', double2: float, univariateDerivative22: 'UnivariateDerivative2', double3: float, univariateDerivative23: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, double: float, univariateDerivative2: 'UnivariateDerivative2', double2: float, univariateDerivative22: 'UnivariateDerivative2', double3: float, univariateDerivative23: 'UnivariateDerivative2', double4: float, univariateDerivative24: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, doubleArray: typing.List[float], univariateDerivative2Array: typing.List['UnivariateDerivative2']) -> 'UnivariateDerivative2':
        """
            Compute a linear combination.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
            Compute a linear combination.
        
            Parameters:
                a (double[]): Factors.
                b (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`[]): Factors.
        
            Returns:
                :code:`Σ :sub:`i` a :sub:`i` b :sub:`i``.
        
        """
        ...
    @typing.overload
    def linearCombination(self, univariateDerivative2: 'UnivariateDerivative2', univariateDerivative22: 'UnivariateDerivative2', univariateDerivative23: 'UnivariateDerivative2', univariateDerivative24: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, univariateDerivative2: 'UnivariateDerivative2', univariateDerivative22: 'UnivariateDerivative2', univariateDerivative23: 'UnivariateDerivative2', univariateDerivative24: 'UnivariateDerivative2', univariateDerivative25: 'UnivariateDerivative2', univariateDerivative26: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, univariateDerivative2: 'UnivariateDerivative2', univariateDerivative22: 'UnivariateDerivative2', univariateDerivative23: 'UnivariateDerivative2', univariateDerivative24: 'UnivariateDerivative2', univariateDerivative25: 'UnivariateDerivative2', univariateDerivative26: 'UnivariateDerivative2', univariateDerivative27: 'UnivariateDerivative2', univariateDerivative28: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    def linearCombination(self, univariateDerivative2Array: typing.List['UnivariateDerivative2'], univariateDerivative2Array2: typing.List['UnivariateDerivative2']) -> 'UnivariateDerivative2': ...
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
    def multiply(self, double: float) -> 'UnivariateDerivative2':
        """
            Compute n × this. Multiplication by an integer number is defined as the following sum
            n × this = ∑ :sub:`i=1` :sup:`n` this.
        
            Parameters:
                n (int): Number of times :code:`this` must be added to itself.
        
            Returns:
                A new element representing n × this.
        
            '×' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this×a
        
            Compute this × a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): element to multiply
        
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
            Returns the additive inverse of :code:`this` element.
        
            Returns:
                the opposite of :code:`this`.
        
        
        """
        ...
    def newInstance(self, double: float) -> 'UnivariateDerivative2':
        """
            Create an instance corresponding to a constant real value.
        
            Parameters:
                value (double): constant real value
        
            Returns:
                instance corresponding to a constant real value
        
        
        """
        ...
    @typing.overload
    def pow(self, double: float) -> 'UnivariateDerivative2':
        """
            Compute a :sup:`x` where a is a double and x a :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`
        
            Parameters:
                a (double): number to exponentiate
                x (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): power to apply
        
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
        
            Power operation.
        
            Parameters:
                e (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): exponent
        
            Returns:
                this :sup:`e`
        
        
        """
        ...
    @typing.overload
    def pow(self, int: int) -> 'UnivariateDerivative2': ...
    @typing.overload
    def pow(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    @typing.overload
    @staticmethod
    def pow(double: float, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def reciprocal(self) -> 'UnivariateDerivative2':
        """
            Returns the multiplicative inverse of :code:`this` element.
        
            Returns:
                the inverse of :code:`this`.
        
        
        """
        ...
    @typing.overload
    def remainder(self, double: float) -> 'UnivariateDerivative2':
        """
            IEEE remainder operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
            IEEE remainder operator.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): right hand side parameter of the operator
        
            Returns:
                this - n × a where n is the closest integer to this/a
        
        
        """
        ...
    @typing.overload
    def remainder(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
    def rint(self) -> 'UnivariateDerivative2':
        """
            Get the whole number that is the nearest to the instance, or the even one if x is exactly half way between two integers.
        
            Returns:
                a double number r such that r is an integer r - 0.5 ≤ this ≤ r + 0.5
        
        
        """
        ...
    def rootN(self, int: int) -> 'UnivariateDerivative2':
        """
            N :sup:`th` root.
        
            Parameters:
                n (int): order of the root
        
            Returns:
                n :sup:`th` root of the instance
        
        
        """
        ...
    def scalb(self, int: int) -> 'UnivariateDerivative2':
        """
            Multiply the instance by a power of 2.
        
            Parameters:
                n (int): power of 2
        
            Returns:
                this × 2 :sup:`n`
        
        
        """
        ...
    def sign(self) -> 'UnivariateDerivative2':
        """
            Compute the sign of the instance. The sign is -1 for negative numbers, +1 for positive numbers and 0 otherwise, for
            Complex number, it is extended on the unit circle (equivalent to z/|z|, with special handling for 0 and NaN)
        
            Returns:
                -1.0, -0.0, +0.0, +1.0 or NaN depending on sign of a
        
        
        """
        ...
    def sin(self) -> 'UnivariateDerivative2':
        """
            Sine operation.
        
            Returns:
                sin(this)
        
        
        """
        ...
    def sinCos(self) -> org.hipparchus.util.FieldSinCos['UnivariateDerivative2']: ...
    def sinh(self) -> 'UnivariateDerivative2':
        """
            Hyperbolic sine operation.
        
            Returns:
                sinh(this)
        
        
        """
        ...
    def sinhCosh(self) -> org.hipparchus.util.FieldSinhCosh['UnivariateDerivative2']: ...
    def sqrt(self) -> 'UnivariateDerivative2':
        """
            Square root.
        
            Returns:
                square root of the instance
        
        
        """
        ...
    @typing.overload
    def subtract(self, double: float) -> 'UnivariateDerivative2':
        """
            '-' operator.
        
            Parameters:
                a (double): right hand side parameter of the operator
        
            Returns:
                this-a
        
            Compute this - a.
        
            Parameters:
                a (:class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative2`): element to subtract
        
            Returns:
                a new element representing this - a
        
        
        """
        ...
    @typing.overload
    def subtract(self, univariateDerivative2: 'UnivariateDerivative2') -> 'UnivariateDerivative2': ...
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
    def taylor(self, double: float) -> float:
        """
            Evaluate Taylor expansion a univariate derivative.
        
            Parameters:
                delta (double): parameter offset Î”x
        
            Returns:
                value of the Taylor expansion at x + Î”x
        
        
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
            Convert the instance to a :class:`~org.hipparchus.analysis.differentiation.DerivativeStructure`.
        
            Specified by:
                :meth:`~org.hipparchus.analysis.differentiation.UnivariateDerivative.toDerivativeStructure`Â in
                classÂ :class:`~org.hipparchus.analysis.differentiation.UnivariateDerivative`
        
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
    def ulp(self) -> 'UnivariateDerivative2':
        """
            Compute least significant bit (Unit in Last Position) for a number.
        
            The :code:`ulp` function is a step function, hence all its derivatives are 0.
        
            Returns:
                ulp(this)
        
            Since:
                2.0
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.analysis.differentiation")``.

    DSCompiler: typing.Type[DSCompiler]
    DSFactory: typing.Type[DSFactory]
    Derivative: typing.Type[Derivative]
    DerivativeStructure: typing.Type[DerivativeStructure]
    FDSFactory: typing.Type[FDSFactory]
    FieldDerivative: typing.Type[FieldDerivative]
    FieldDerivativeStructure: typing.Type[FieldDerivativeStructure]
    FieldGradient: typing.Type[FieldGradient]
    FieldGradientField: typing.Type[FieldGradientField]
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
