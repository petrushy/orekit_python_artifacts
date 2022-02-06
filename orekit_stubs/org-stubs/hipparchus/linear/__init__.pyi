import java.io
import java.lang
import java.text
import java.util
import java.util.function
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.complex
import org.hipparchus.fraction
import org.hipparchus.util
import typing



class AnyMatrix:
    """
    public interface AnyMatrix
    
        Interface defining very basic matrix operations.
    """
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns in the matrix.
        
            Returns:
                columnDimension
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows in the matrix.
        
            Returns:
                rowDimension
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
            Is this a square matrix?
        
            Returns:
                true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...

class CholeskyDecomposition:
    """
    public class CholeskyDecomposition extends Object
    
        Calculates the Cholesky decomposition of a matrix.
    
        The Cholesky decomposition of a real symmetric positive-definite matrix A consists of a lower triangular matrix L with
        same size such that: A = LL :sup:`T` . In a sense, this is the square root of A.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library,
        with the following changes:
    
          - a :meth:`~org.hipparchus.linear.CholeskyDecomposition.getLT` method has been added,
          - the :code:`isspd` method has been removed, since the constructor of this class throws a
            :class:`~org.hipparchus.exception.MathIllegalArgumentException` when a matrix cannot be decomposed,
          - a :meth:`~org.hipparchus.linear.CholeskyDecomposition.getDeterminant` method has been added,
          - the :code:`solve` method has been replaced by a :meth:`~org.hipparchus.linear.CholeskyDecomposition.getSolver` method
            and the equivalent method provided by the returned :class:`~org.hipparchus.linear.DecompositionSolver`.
    
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/CholeskyDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/Cholesky_decomposition>`
    """
    DEFAULT_RELATIVE_SYMMETRY_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_RELATIVE_SYMMETRY_THRESHOLD
    
        Default threshold above which off-diagonal elements are considered too different and matrix not symmetric.
    
        Also see:
            :meth:`~constant`
    
    
    """
    DEFAULT_ABSOLUTE_POSITIVITY_THRESHOLD: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ABSOLUTE_POSITIVITY_THRESHOLD
    
        Default threshold below which diagonal elements are considered null and matrix not positive definite.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float): ...
    def getDeterminant(self) -> float:
        """
            Return the determinant of the matrix
        
            Returns:
                determinant of the matrix
        
        
        """
        ...
    def getL(self) -> 'RealMatrix':
        """
            Returns the matrix L of the decomposition.
        
            L is an lower-triangular matrix
        
            Returns:
                the L matrix
        
        
        """
        ...
    def getLT(self) -> 'RealMatrix':
        """
            Returns the transpose of the matrix L of the decomposition.
        
            L :sup:`T` is an upper-triangular matrix
        
            Returns:
                the transpose of the matrix L of the decomposition
        
        
        """
        ...
    def getSolver(self) -> 'DecompositionSolver':
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Returns:
                a solver
        
        
        """
        ...

class ComplexEigenDecomposition:
    DEFAULT_EIGENVECTORS_EQUALITY: typing.ClassVar[float] = ...
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    DEFAULT_EPSILON_AV_VD_CHECK: typing.ClassVar[float] = ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float, double3: float): ...
    def getD(self) -> 'FieldMatrix'[org.hipparchus.complex.Complex]: ...
    def getDeterminant(self) -> float: ...
    def getEigenvalues(self) -> typing.List[org.hipparchus.complex.Complex]: ...
    def getEigenvector(self, int: int) -> 'FieldVector'[org.hipparchus.complex.Complex]: ...
    def getV(self) -> 'FieldMatrix'[org.hipparchus.complex.Complex]: ...
    def getVT(self) -> 'FieldMatrix'[org.hipparchus.complex.Complex]: ...
    def hasComplexEigenvalues(self) -> bool: ...

class DecompositionSolver:
    """
    public interface DecompositionSolver
    
        Interface handling decomposition algorithms that can solve A × X = B.
    
        Decomposition algorithms decompose an A matrix as a product of several specific matrices from which they can solve A Ã—
        X = B in least squares sense: they find X such that ||A Ã— X - B|| is minimal.
    
        Some solvers like :class:`~org.hipparchus.linear.LUDecomposition` can only find the solution for square matrices and
        when the solution is an exact linear solution, i.e. when ||A Ã— X - B|| is exactly 0. Other solvers can also find
        solutions with non-square matrix A and with non-null minimal norm. If an exact linear solution exists it is also the
        minimal norm solution.
    """
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns in the matrix.
        
            Returns:
                columnDimension
        
            Since:
                2.0
        
        
        """
        ...
    def getInverse(self) -> 'RealMatrix': ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows in the matrix.
        
            Returns:
                rowDimension
        
            Since:
                2.0
        
        
        """
        ...
    def isNonSingular(self) -> bool:
        """
            Check if the decomposed matrix is non-singular.
        
            Returns:
                true if the decomposed matrix is non-singular.
        
        
        """
        ...
    @typing.overload
    def solve(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    def solve(self, realVector: 'RealVector') -> 'RealVector': ...

class EigenDecomposition:
    """
    public class EigenDecomposition extends Object
    
        Calculates the eigen decomposition of a real matrix.
    
        The eigen decomposition of matrix A is a set of two matrices: V and D such that A = V Ã— D Ã— V :sup:`T` . A, V and D
        are all m Ã— m matrices.
    
        This class is similar in spirit to the :code:`EigenvalueDecomposition` class from the `JAMA
        <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
          - a :meth:`~org.hipparchus.linear.EigenDecomposition.getVT` method has been added,
          - two :meth:`~org.hipparchus.linear.EigenDecomposition.getRealEigenvalue` and
            :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalue` methods to pick up a single eigenvalue have been
            added,
          - a :meth:`~org.hipparchus.linear.EigenDecomposition.getEigenvector` method to pick up a single eigenvector has been
            added,
          - a :meth:`~org.hipparchus.linear.EigenDecomposition.getDeterminant` method has been added.
          - a :meth:`~org.hipparchus.linear.EigenDecomposition.getSolver` method has been added.
    
    
        As of 3.1, this class supports general real matrices (both symmetric and non-symmetric):
    
        If A is symmetric, then A = V*D*V' where the eigenvalue matrix D is diagonal and the eigenvector matrix V is orthogonal,
        i.e. :code:`A = V.multiply(D.multiply(V.transpose()))` and :code:`V.multiply(V.transpose())` equals the identity matrix.
    
        If A is not symmetric, then the eigenvalue matrix D is block diagonal with the real eigenvalues in 1-by-1 blocks and any
        complex eigenvalues, lambda + i*mu, in 2-by-2 blocks:
    
        .. code-block: java
        
            [lambda, mu    ]
            [   -mu, lambda]
         
        The columns of V represent the eigenvectors in the sense that :code:`A*V = V*D`, i.e. A.multiply(V) equals
        V.multiply(D). The matrix V may be badly conditioned, or even singular, so the validity of the equation :code:`A =
        V*D*inverse(V)` depends upon the condition of V.
    
        This implementation is based on the paper by A. Drubrulle, R.S. Martin and J.H. Wilkinson "The Implicit QL Algorithm" in
        Wilksinson and Reinsch (1971) Handbook for automatic computation, vol. 2, Linear algebra, Springer-Verlag, New-York.
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/EigenDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix>`
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float], double3: float): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getD(self) -> 'RealMatrix':
        """
            Gets the block diagonal matrix D of the decomposition. D is a block diagonal matrix. Real eigenvalues are on the
            diagonal while complex values are on 2x2 blocks { {real +imaginary}, {-imaginary, real} }.
        
            Returns:
                the D matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getRealEigenvalues`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalues`
        
        
        """
        ...
    def getDeterminant(self) -> float:
        """
            Computes the determinant of the matrix.
        
            Returns:
                the determinant of the matrix.
        
        
        """
        ...
    def getEigenvector(self, int: int) -> 'RealVector':
        """
            Gets a copy of the i :sup:`th` eigenvector of the original matrix.
        
            Parameters:
                i (int): Index of the eigenvector (counting from 0).
        
            Returns:
                a copy of the i :sup:`th` eigenvector of the original matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getD`
        
        
        """
        ...
    def getEpsilon(self) -> float:
        """
            Get's the value for epsilon which is used for internal tests (e.g. is singular, eigenvalue ratio, etc.)
        
            Returns:
                the epsilon value.
        
        
        """
        ...
    def getImagEigenvalue(self, int: int) -> float:
        """
            Gets the imaginary part of the i :sup:`th` eigenvalue of the original matrix.
        
            Parameters:
                i (int): Index of the eigenvalue (counting from 0).
        
            Returns:
                the imaginary part of the i :sup:`th` eigenvalue of the original matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getD`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalues`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getRealEigenvalue`
        
        
        """
        ...
    def getImagEigenvalues(self) -> typing.List[float]:
        """
            Gets a copy of the imaginary parts of the eigenvalues of the original matrix.
        
            Returns:
                a copy of the imaginary parts of the eigenvalues of the original matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getD`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalue`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getRealEigenvalues`
        
        
        """
        ...
    def getRealEigenvalue(self, int: int) -> float:
        """
            Returns the real part of the i :sup:`th` eigenvalue of the original matrix.
        
            Parameters:
                i (int): index of the eigenvalue (counting from 0)
        
            Returns:
                real part of the i :sup:`th` eigenvalue of the original matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getD`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getRealEigenvalues`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalue`
        
        
        """
        ...
    def getRealEigenvalues(self) -> typing.List[float]:
        """
            Gets a copy of the real parts of the eigenvalues of the original matrix.
        
            Returns:
                a copy of the real parts of the eigenvalues of the original matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getD`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getRealEigenvalue`,
                :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalues`
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Gets a solver for finding the A × X = B solution in exact linear sense.
        
            Since 3.1, eigen decomposition of a general matrix is supported, but the
            :class:`~org.hipparchus.linear.DecompositionSolver` only supports real eigenvalues.
        
            Returns:
                a solver
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the decomposition resulted in complex eigenvalues
        
        
        """
        ...
    def getSquareRoot(self) -> 'RealMatrix':
        """
            Computes the square-root of the matrix. This implementation assumes that the matrix is symmetric and positive definite.
        
            Returns:
                the square-root of the matrix.
        
            Raises:
                :class:`~org.hipparchus.exception.MathRuntimeException`: if the matrix is not symmetric or not positive definite.
        
        
        """
        ...
    def getV(self) -> 'RealMatrix':
        """
            Gets the matrix V of the decomposition. V is an orthogonal matrix, i.e. its transpose is also its inverse. The columns
            of V are the eigenvectors of the original matrix. No assumption is made about the orientation of the system axes formed
            by the columns of V (e.g. in a 3-dimension space, V can form a left- or right-handed system).
        
            Returns:
                the V matrix.
        
        
        """
        ...
    def getVT(self) -> 'RealMatrix':
        """
            Gets the transpose of the matrix V of the decomposition. V is an orthogonal matrix, i.e. its transpose is also its
            inverse. The columns of V are the eigenvectors of the original matrix. No assumption is made about the orientation of
            the system axes formed by the columns of V (e.g. in a 3-dimension space, V can form a left- or right-handed system).
        
            Returns:
                the transpose of the V matrix.
        
        
        """
        ...
    def hasComplexEigenvalues(self) -> bool:
        """
            Returns whether the calculated eigen values are complex or real.
        
            The method performs a zero check for each element of the
            :meth:`~org.hipparchus.linear.EigenDecomposition.getImagEigenvalues` array and returns :code:`true` if any element is
            not equal to zero.
        
            Returns:
                :code:`true` if the eigen values are complex, :code:`false` otherwise
        
        
        """
        ...

_FieldDecompositionSolver__T = typing.TypeVar('_FieldDecompositionSolver__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldDecompositionSolver(typing.Generic[_FieldDecompositionSolver__T]):
    """
    public interface FieldDecompositionSolver<T extends :class:`~org.hipparchus.FieldElement`<T>>
    
        Interface handling decomposition algorithms that can solve A × X = B.
    
        Decomposition algorithms decompose an A matrix has a product of several specific matrices from which they can solve A Ã—
        X = B in least squares sense: they find X such that ||A Ã— X - B|| is minimal.
    
        Some solvers like :class:`~org.hipparchus.linear.FieldLUDecomposition` can only find the solution for square matrices
        and when the solution is an exact linear solution, i.e. when ||A Ã— X - B|| is exactly 0. Other solvers can also find
        solutions with non-square matrix A and with non-null minimal norm. If an exact linear solution exists it is also the
        minimal norm solution.
    """
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns in the matrix.
        
            Returns:
                columnDimension
        
            Since:
                2.0
        
        
        """
        ...
    def getInverse(self) -> 'FieldMatrix'[_FieldDecompositionSolver__T]: ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows in the matrix.
        
            Returns:
                rowDimension
        
            Since:
                2.0
        
        
        """
        ...
    def isNonSingular(self) -> bool:
        """
            Check if the decomposed matrix is non-singular.
        
            Returns:
                true if the decomposed matrix is non-singular
        
        
        """
        ...
    @typing.overload
    def solve(self, fieldMatrix: 'FieldMatrix'[_FieldDecompositionSolver__T]) -> 'FieldMatrix'[_FieldDecompositionSolver__T]: ...
    @typing.overload
    def solve(self, fieldVector: 'FieldVector'[_FieldDecompositionSolver__T]) -> 'FieldVector'[_FieldDecompositionSolver__T]: ...

_FieldLUDecomposition__T = typing.TypeVar('_FieldLUDecomposition__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldLUDecomposition(typing.Generic[_FieldLUDecomposition__T]):
    """
    public class FieldLUDecomposition<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object
    
        Calculates the LUP-decomposition of a square matrix.
    
        The LUP-decomposition of a matrix A consists of three matrices L, U and P that satisfy: PA = LU, L is lower triangular,
        and U is upper triangular and P is a permutation matrix. All matrices are mÃ—m.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
          - a :meth:`~org.hipparchus.linear.FieldLUDecomposition.getP` method has been added,
          - the :code:`det` method has been renamed as :meth:`~org.hipparchus.linear.FieldLUDecomposition.getDeterminant`,
          - the :code:`getDoublePivot` method has been removed (but the int based
            :meth:`~org.hipparchus.linear.FieldLUDecomposition.getPivot` method has been kept),
          - the :code:`solve` and :code:`isNonSingular` methods have been replaced by a
            :meth:`~org.hipparchus.linear.FieldLUDecomposition.getSolver` method and the equivalent methods provided by the returned
            :class:`~org.hipparchus.linear.DecompositionSolver`.
    
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/LUDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/LU_decomposition>`
    """
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldLUDecomposition__T]): ...
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldLUDecomposition__T], predicate: typing.Union[java.util.function.Predicate[_FieldLUDecomposition__T], typing.Callable[[_FieldLUDecomposition__T], bool]]): ...
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldLUDecomposition__T], predicate: typing.Union[java.util.function.Predicate[_FieldLUDecomposition__T], typing.Callable[[_FieldLUDecomposition__T], bool]], boolean: bool): ...
    def getDeterminant(self) -> _FieldLUDecomposition__T:
        """
            Return the determinant of the matrix.
        
            Returns:
                determinant of the matrix
        
        
        """
        ...
    def getL(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]: ...
    def getP(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]: ...
    def getPivot(self) -> typing.List[int]:
        """
            Returns the pivot permutation vector.
        
            Returns:
                the pivot permutation vector
        
            Also see:
                :meth:`~org.hipparchus.linear.FieldLUDecomposition.getP`
        
        
        """
        ...
    def getSolver(self) -> FieldDecompositionSolver[_FieldLUDecomposition__T]: ...
    def getU(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]: ...

_FieldMatrixChangingVisitor__T = typing.TypeVar('_FieldMatrixChangingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrixChangingVisitor(typing.Generic[_FieldMatrixChangingVisitor__T]):
    """
    public interface FieldMatrixChangingVisitor<T extends :class:`~org.hipparchus.FieldElement`<?>>
    
        Interface defining a visitor for matrix entries.
    """
    def end(self) -> _FieldMatrixChangingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _FieldMatrixChangingVisitor__T) -> _FieldMatrixChangingVisitor__T:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~org.hipparchus.linear.FieldMatrixChangingVisitor`): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

_FieldMatrixPreservingVisitor__T = typing.TypeVar('_FieldMatrixPreservingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrixPreservingVisitor(typing.Generic[_FieldMatrixPreservingVisitor__T]):
    """
    public interface FieldMatrixPreservingVisitor<T extends :class:`~org.hipparchus.FieldElement`<?>>
    
        Interface defining a visitor for matrix entries.
    """
    def end(self) -> _FieldMatrixPreservingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _FieldMatrixPreservingVisitor__T) -> None:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~org.hipparchus.linear.FieldMatrixPreservingVisitor`): current value of the entry
        
        
        """
        ...

_FieldQRDecomposition__T = typing.TypeVar('_FieldQRDecomposition__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQRDecomposition(typing.Generic[_FieldQRDecomposition__T]):
    """
    public class FieldQRDecomposition<T extends :class:`~org.hipparchus.CalculusFieldElement`<T>> extends Object
    
        Calculates the QR-decomposition of a field matrix.
    
        The QR-decomposition of a matrix A consists of two matrices Q and R that satisfy: A = QR, Q is orthogonal (Q :sup:`T` Q
        = I), and R is upper triangular. If A is mÃ—n, Q is mÃ—m and R mÃ—n.
    
        This class compute the decomposition using Householder reflectors.
    
        For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows,
        which is much more cache-efficient in Java.
    
        This class is based on the class :class:`~org.hipparchus.linear.QRDecomposition`.
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldQRDecomposition__T]): ...
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldQRDecomposition__T], t: _FieldQRDecomposition__T): ...
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldQRDecomposition__T], t: _FieldQRDecomposition__T, predicate: typing.Union[java.util.function.Predicate[_FieldQRDecomposition__T], typing.Callable[[_FieldQRDecomposition__T], bool]]): ...
    def getH(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]: ...
    def getQ(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]: ...
    def getQT(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]: ...
    def getR(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]: ...
    def getSolver(self) -> FieldDecompositionSolver[_FieldQRDecomposition__T]: ...

_FieldVector__T = typing.TypeVar('_FieldVector__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldVector(typing.Generic[_FieldVector__T]):
    """
    public interface FieldVector<T extends :class:`~org.hipparchus.FieldElement`<T>>
    
        Interface defining a field-valued vector with basic algebraic operations.
    
        vector element indexing is 0-based -- e.g., :code:`getEntry(0)` returns the first element of the vector.
    
        The various :code:`mapXxx` and :code:`mapXxxToSelf` methods operate on vectors element-wise, i.e. they perform the same
        operation (adding a scalar, applying a function ...) on each element in turn. The :code:`mapXxx` versions create a new
        vector to hold the result and do not change the instance. The :code:`mapXxxToSelf` versions use the instance itself to
        store the results, so the instance is changed by these methods. In both cases, the result vector is returned by the
        methods, this allows to use the *fluent API* style, like this:
    
        .. code-block: java
        
           RealVector result = v.mapAddToSelf(3.0).mapTanToSelf().mapSquareToSelf();
         
    
        Note that as almost all operations on :class:`~org.hipparchus.FieldElement` throw
        :class:`~org.hipparchus.exception.NullArgumentException` when operating on a null element, it is the responsibility of
        :code:`FieldVector` implementations to make sure no null elements are inserted into the vector. This must be done in all
        constructors and all setters.
    """
    def add(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    @typing.overload
    def append(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    @typing.overload
    def append(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def copy(self) -> 'FieldVector'[_FieldVector__T]: ...
    def dotProduct(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> _FieldVector__T: ...
    def ebeDivide(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def ebeMultiply(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Returns:
                size
        
        
        """
        ...
    def getEntry(self, int: int) -> _FieldVector__T: ...
    def getField(self) -> org.hipparchus.Field[_FieldVector__T]: ...
    def getSubVector(self, int: int, int2: int) -> 'FieldVector'[_FieldVector__T]: ...
    def mapAdd(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapAddToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapDivide(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapDivideToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapInv(self) -> 'FieldVector'[_FieldVector__T]: ...
    def mapInvToSelf(self) -> 'FieldVector'[_FieldVector__T]: ...
    def mapMultiply(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapMultiplyToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapSubtract(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def mapSubtractToSelf(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    def outerProduct(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldMatrix'[_FieldVector__T]: ...
    def projection(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def set(self, t: _FieldVector__T) -> None:
        """
            Set all elements to a single value.
        
            Parameters:
                value (:class:`~org.hipparchus.linear.FieldVector`): single value to set for all elements
        
        
        """
        ...
    def setEntry(self, int: int, t: _FieldVector__T) -> None: ...
    def setSubVector(self, int: int, fieldVector: 'FieldVector'[_FieldVector__T]) -> None: ...
    def subtract(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def toArray(self) -> typing.List[_FieldVector__T]:
        """
            Convert the vector to a T array.
        
            The array is independent from vector data, it's elements are copied.
        
            Returns:
                array containing a copy of vector elements
        
        
        """
        ...

_FieldVectorChangingVisitor__T = typing.TypeVar('_FieldVectorChangingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldVectorChangingVisitor(typing.Generic[_FieldVectorChangingVisitor__T]):
    """
    public interface FieldVectorChangingVisitor<T extends :class:`~org.hipparchus.FieldElement`<?>>
    
        This interface defines a visitor for the entries of a vector. Visitors implementing this interface may alter the entries
        of the vector being visited.
    """
    def end(self) -> _FieldVectorChangingVisitor__T:
        """
            End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
            Returns:
                the value returned after visiting all entries
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int) -> None:
        """
            Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
            Parameters:
                dimension (int): the size of the vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, int: int, t: _FieldVectorChangingVisitor__T) -> _FieldVectorChangingVisitor__T:
        """
            Visit one entry of the vector.
        
            Parameters:
                index (int): the index of the entry being visited
                value (:class:`~org.hipparchus.linear.FieldVectorChangingVisitor`): the value of the entry being visited
        
            Returns:
                the new value of the entry being visited
        
        
        """
        ...

_FieldVectorPreservingVisitor__T = typing.TypeVar('_FieldVectorPreservingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldVectorPreservingVisitor(typing.Generic[_FieldVectorPreservingVisitor__T]):
    """
    public interface FieldVectorPreservingVisitor<T extends :class:`~org.hipparchus.FieldElement`<?>>
    
        This interface defines a visitor for the entries of a vector. Visitors implementing this interface do not alter the
        entries of the vector being visited.
    """
    def end(self) -> _FieldVectorPreservingVisitor__T:
        """
            End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
            Returns:
                the value returned after visiting all entries
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int) -> None:
        """
            Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
            Parameters:
                dimension (int): the size of the vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, int: int, t: _FieldVectorPreservingVisitor__T) -> None:
        """
            Visit one entry of the vector.
        
            Parameters:
                index (int): the index of the entry being visited
                value (:class:`~org.hipparchus.linear.FieldVectorPreservingVisitor`): the value of the entry being visited
        
        
        """
        ...

class IterativeLinearSolver:
    """
    public abstract class IterativeLinearSolver extends Object
    
        This abstract class defines an iterative solver for the linear system A Â· x = b. In what follows, the *residual* r is
        defined as r = b - A Â· x, where A is the linear operator of the linear system, b is the right-hand side vector, and x
        the current estimate of the solution.
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager): ...
    def getIterationManager(self) -> org.hipparchus.util.IterationManager:
        """
            Returns the iteration manager attached to this solver.
        
            Returns:
                the manager
        
        
        """
        ...
    @typing.overload
    def solve(self, realLinearOperator: 'RealLinearOperator', realVector: 'RealVector') -> 'RealVector': ...
    @typing.overload
    def solve(self, realLinearOperator: 'RealLinearOperator', realVector: 'RealVector', realVector2: 'RealVector') -> 'RealVector': ...
    def solveInPlace(self, realLinearOperator: 'RealLinearOperator', realVector: 'RealVector', realVector2: 'RealVector') -> 'RealVector': ...

class IterativeLinearSolverEvent(org.hipparchus.util.IterationEvent):
    """
    public abstract class IterativeLinearSolverEvent extends :class:`~org.hipparchus.util.IterationEvent`
    
        This is the base class for all events occurring during the iterations of a
        :class:`~org.hipparchus.linear.IterativeLinearSolver`.
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self, object: typing.Any, int: int): ...
    def getNormOfResidual(self) -> float:
        """
            Returns the norm of the residual. The returned value is not required to be *exact*. Instead, the norm of the so-called
            *updated* residual (if available) should be returned. For example, the :class:`~org.hipparchus.linear.ConjugateGradient`
            method computes a sequence of residuals, the norm of which is cheap to compute. However, due to accumulation of
            round-off errors, this residual might differ from the true residual after some iterations. See e.g. A. Greenbaum and Z.
            Strakos, *Predicting the Behavior of Finite Precision Lanzos and Conjugate Gradient Computations*, Technical Report 538,
            Department of Computer Science, New York University, 1991 (available `here
            <http://www.archive.org/details/predictingbehavi00gree>`).
        
            Returns:
                the norm of the residual, ||r||
        
        
        """
        ...
    def getResidual(self) -> 'RealVector':
        """
        
            Returns the residual. This is an optional operation, as all iterative linear solvers do not provide cheap estimate of
            the updated residual vector, in which case
        
              - this method should throw a :class:`~org.hipparchus.exception.MathRuntimeException`,
              - :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.providesResidual` returns :code:`false`.
        
        
            The default implementation throws a :class:`~org.hipparchus.exception.MathRuntimeException`. If this method is
            overriden, then :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.providesResidual` should be overriden as well.
        
            Returns:
                the updated residual, r
        
        
        """
        ...
    def getRightHandSideVector(self) -> 'RealVector':
        """
            Returns the current right-hand side of the linear system to be solved. This method should return an unmodifiable view,
            or a deep copy of the actual right-hand side vector, in order not to compromise subsequent iterations of the source
            :class:`~org.hipparchus.linear.IterativeLinearSolver`.
        
            Returns:
                the right-hand side vector, b
        
        
        """
        ...
    def getSolution(self) -> 'RealVector':
        """
            Returns the current estimate of the solution to the linear system to be solved. This method should return an
            unmodifiable view, or a deep copy of the actual current solution, in order not to compromise subsequent iterations of
            the source :class:`~org.hipparchus.linear.IterativeLinearSolver`.
        
            Returns:
                the solution, x
        
        
        """
        ...
    def providesResidual(self) -> bool:
        """
            Returns :code:`true` if :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getResidual` is supported. The default
            implementation returns :code:`false`.
        
            Returns:
                :code:`false` if :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getResidual` throws a
                :class:`~org.hipparchus.exception.MathRuntimeException`
        
        
        """
        ...

class LUDecomposition:
    """
    public class LUDecomposition extends Object
    
        Calculates the LUP-decomposition of a square matrix.
    
        The LUP-decomposition of a matrix A consists of three matrices L, U and P that satisfy: PÃ—A = LÃ—U. L is lower
        triangular (with unit diagonal terms), U is upper triangular and P is a permutation matrix. All matrices are mÃ—m.
    
        As shown by the presence of the P matrix, this decomposition is implemented using partial pivoting.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
          - a :meth:`~org.hipparchus.linear.LUDecomposition.getP` method has been added,
          - the :code:`det` method has been renamed as :meth:`~org.hipparchus.linear.LUDecomposition.getDeterminant`,
          - the :code:`getDoublePivot` method has been removed (but the int based
            :meth:`~org.hipparchus.linear.LUDecomposition.getPivot` method has been kept),
          - the :code:`solve` and :code:`isNonSingular` methods have been replaced by a
            :meth:`~org.hipparchus.linear.LUDecomposition.getSolver` method and the equivalent methods provided by the returned
            :class:`~org.hipparchus.linear.DecompositionSolver`.
    
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/LUDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/LU_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getDeterminant(self) -> float:
        """
            Return the determinant of the matrix
        
            Returns:
                determinant of the matrix
        
        
        """
        ...
    def getL(self) -> 'RealMatrix':
        """
            Returns the matrix L of the decomposition.
        
            L is a lower-triangular matrix
        
            Returns:
                the L matrix (or null if decomposed matrix is singular)
        
        
        """
        ...
    def getP(self) -> 'RealMatrix':
        """
            Returns the P rows permutation matrix.
        
            P is a sparse matrix with exactly one element set to 1.0 in each row and each column, all other elements being set to
            0.0.
        
            The positions of the 1 elements are given by the :meth:`~org.hipparchus.linear.LUDecomposition.getPivot`.
        
            Returns:
                the P rows permutation matrix (or null if decomposed matrix is singular)
        
            Also see:
                :meth:`~org.hipparchus.linear.LUDecomposition.getPivot`
        
        
        """
        ...
    def getPivot(self) -> typing.List[int]:
        """
            Returns the pivot permutation vector.
        
            Returns:
                the pivot permutation vector
        
            Also see:
                :meth:`~org.hipparchus.linear.LUDecomposition.getP`
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in exact linear sense.
        
            Returns:
                a solver
        
        
        """
        ...
    def getU(self) -> 'RealMatrix':
        """
            Returns the matrix U of the decomposition.
        
            U is an upper-triangular matrix
        
            Returns:
                the U matrix (or null if decomposed matrix is singular)
        
        
        """
        ...

class MatrixDecomposer:
    """
    public interface MatrixDecomposer
    
        Interface for all algorithms providing matrix decomposition.
    
        Since:
            1.3
    """
    def decompose(self, realMatrix: 'RealMatrix') -> DecompositionSolver: ...

class MatrixUtils:
    """
    public class MatrixUtils extends Object
    
        A collection of static methods that operate on or return matrices.
    """
    DEFAULT_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~org.hipparchus.linear.RealMatrixFormat` DEFAULT_FORMAT
    
        The default format for :class:`~org.hipparchus.linear.RealMatrix` objects.
    
    """
    OCTAVE_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    public static final :class:`~org.hipparchus.linear.RealMatrixFormat` OCTAVE_FORMAT
    
        A format for :class:`~org.hipparchus.linear.RealMatrix` objects compatible with octave.
    
    """
    @staticmethod
    def bigFractionMatrixToRealMatrix(fieldMatrix: 'FieldMatrix'[org.hipparchus.fraction.BigFraction]) -> 'Array2DRowRealMatrix': ...
    @staticmethod
    def blockInverse(realMatrix: 'RealMatrix', int: int) -> 'RealMatrix':
        """
            Computes the inverse of the given matrix by splitting it into 4 sub-matrices.
        
            Parameters:
                m (:class:`~org.hipparchus.linear.RealMatrix`): Matrix whose inverse must be computed.
                splitIndex (int): Index that determines the "split" line and column. The element corresponding to this index will part of the upper-left
                    sub-matrix.
        
            Returns:
                the inverse of :code:`m`.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`m` is not square.
        
        
        """
        ...
    @staticmethod
    def checkAdditionCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None: ...
    @staticmethod
    def checkColumnIndex(anyMatrix: AnyMatrix, int: int) -> None: ...
    @staticmethod
    def checkMatrixIndex(anyMatrix: AnyMatrix, int: int, int2: int) -> None: ...
    @staticmethod
    def checkMultiplicationCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None: ...
    @staticmethod
    def checkRowIndex(anyMatrix: AnyMatrix, int: int) -> None: ...
    @staticmethod
    def checkSameColumnDimension(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None: ...
    @staticmethod
    def checkSameRowDimension(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None: ...
    @typing.overload
    @staticmethod
    def checkSubMatrixIndex(anyMatrix: AnyMatrix, int: int, int2: int, int3: int, int4: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkSubMatrixIndex(anyMatrix: AnyMatrix, intArray: typing.List[int], intArray2: typing.List[int]) -> None: ...
    @staticmethod
    def checkSubtractionCompatible(anyMatrix: AnyMatrix, anyMatrix2: AnyMatrix) -> None: ...
    @staticmethod
    def checkSymmetric(realMatrix: 'RealMatrix', double: float) -> None:
        """
            Checks whether a matrix is symmetric.
        
            Parameters:
                matrix (:class:`~org.hipparchus.linear.RealMatrix`): Matrix to check.
                eps (double): Relative tolerance.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the matrix is not square.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the matrix is not symmetric.
        
        
        """
        ...
    _createColumnFieldMatrix__T = typing.TypeVar('_createColumnFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createColumnFieldMatrix(tArray: typing.List[_createColumnFieldMatrix__T]) -> 'FieldMatrix'[_createColumnFieldMatrix__T]: ...
    @staticmethod
    def createColumnRealMatrix(doubleArray: typing.List[float]) -> 'RealMatrix': ...
    _createFieldDiagonalMatrix__T = typing.TypeVar('_createFieldDiagonalMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createFieldDiagonalMatrix(tArray: typing.List[_createFieldDiagonalMatrix__T]) -> 'FieldMatrix'[_createFieldDiagonalMatrix__T]:
        """
            Returns a diagonal matrix with specified elements.
        
            Parameters:
                diagonal (T[]): diagonal elements of the matrix (the array elements will be copied)
        
            Returns:
                diagonal matrix
        
        
        """
        ...
    _createFieldIdentityMatrix__T = typing.TypeVar('_createFieldIdentityMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createFieldIdentityMatrix(field: org.hipparchus.Field[_createFieldIdentityMatrix__T], int: int) -> 'FieldMatrix'[_createFieldIdentityMatrix__T]:
        """
            Returns :code:`dimension x dimension` identity matrix.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field to which the elements belong
                dimension (int): dimension of identity matrix to generate
        
            Returns:
                identity matrix
        
            Raises:
                : if dimension is not positive
        
        
        """
        ...
    _createFieldMatrix_0__T = typing.TypeVar('_createFieldMatrix_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _createFieldMatrix_1__T = typing.TypeVar('_createFieldMatrix_1__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createFieldMatrix(field: org.hipparchus.Field[_createFieldMatrix_0__T], int: int, int2: int) -> 'FieldMatrix'[_createFieldMatrix_0__T]:
        """
            Returns a :class:`~org.hipparchus.linear.FieldMatrix` with specified dimensions.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64Ã—64 for a
            square matrix), a :class:`~org.hipparchus.linear.FieldMatrix` instance is built. Above this threshold a
            :class:`~org.hipparchus.linear.BlockFieldMatrix` instance is built.
        
            The matrix elements are all set to field.getZero().
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field to which the matrix elements belong
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
        
            Returns:
                FieldMatrix with specified dimensions
        
            Also see:
        
        public static <T extends :class:`~org.hipparchus.FieldElement`<T>> :class:`~org.hipparchus.linear.FieldMatrix`<T> createFieldMatrix(T[][] data) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.NullArgumentException`
        
            Returns a :class:`~org.hipparchus.linear.FieldMatrix` whose entries are the the values in the the input array.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64Ã—64 for a
            square matrix), a :class:`~org.hipparchus.linear.FieldMatrix` instance is built. Above this threshold a
            :class:`~org.hipparchus.linear.BlockFieldMatrix` instance is built.
        
            The input array is copied, not referenced.
        
            Parameters:
                data (T[][]): input array
        
            Returns:
                a matrix containing the values of the array.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`data` is not rectangular (not all rows have the same length).
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if a row or column is empty.
                :class:`~org.hipparchus.exception.NullArgumentException`: if either :code:`data` or :code:`data[0]` is :code:`null`.
        
            Also see:
                :meth:`~org.hipparchus.linear.MatrixUtils.createFieldMatrix`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createFieldMatrix(tArray: typing.List[typing.List[_createFieldMatrix_1__T]]) -> 'FieldMatrix'[_createFieldMatrix_1__T]: ...
    _createFieldVector_0__T = typing.TypeVar('_createFieldVector_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _createFieldVector_1__T = typing.TypeVar('_createFieldVector_1__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createFieldVector(field: org.hipparchus.Field[_createFieldVector_0__T], int: int) -> FieldVector[_createFieldVector_0__T]:
        """
            Creates a :class:`~org.hipparchus.linear.FieldVector` with specified dimensions.
        
            Parameters:
                field (:class:`~org.hipparchus.Field`<T> field): field to which array elements belong
                dimension (int): dimension of the vector
        
            Returns:
                a new vector
        
            Since:
                1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createFieldVector(tArray: typing.List[_createFieldVector_1__T]) -> FieldVector[_createFieldVector_1__T]: ...
    @staticmethod
    def createRealDiagonalMatrix(doubleArray: typing.List[float]) -> 'RealMatrix':
        """
            Returns a diagonal matrix with specified elements.
        
            Parameters:
                diagonal (double[]): diagonal elements of the matrix (the array elements will be copied)
        
            Returns:
                diagonal matrix
        
        
        """
        ...
    @staticmethod
    def createRealIdentityMatrix(int: int) -> 'RealMatrix':
        """
            Returns :code:`dimension x dimension` identity matrix.
        
            Parameters:
                dimension (int): dimension of identity matrix to generate
        
            Returns:
                identity matrix
        
            Raises:
                : if dimension is not positive
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealMatrix(doubleArray: typing.List[typing.List[float]]) -> 'RealMatrix':
        """
            Returns a :class:`~org.hipparchus.linear.RealMatrix` with specified dimensions.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64Ã—64 for a
            square matrix) which can be stored in a 32kB array, a :class:`~org.hipparchus.linear.Array2DRowRealMatrix` instance is
            built. Above this threshold a :class:`~org.hipparchus.linear.BlockRealMatrix` instance is built.
        
            The matrix elements are all set to 0.0.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
        
            Returns:
                RealMatrix with specified dimensions
        
            Also see:
        
        public static :class:`~org.hipparchus.linear.RealMatrix` createRealMatrix(double[][] data) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`, :class:`~org.hipparchus.exception.NullArgumentException`
        
            Returns a :class:`~org.hipparchus.linear.RealMatrix` whose entries are the the values in the the input array.
        
            The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64Ã—64 for a
            square matrix) which can be stored in a 32kB array, a :class:`~org.hipparchus.linear.Array2DRowRealMatrix` instance is
            built. Above this threshold a :class:`~org.hipparchus.linear.BlockRealMatrix` instance is built.
        
            The input array is copied, not referenced.
        
            Parameters:
                data (double[][]): input array
        
            Returns:
                RealMatrix containing the values of the array
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`data` is not rectangular (not all rows have the same length).
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if a row or column is empty.
                :class:`~org.hipparchus.exception.NullArgumentException`: if either :code:`data` or :code:`data[0]` is :code:`null`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`data` is not rectangular.
        
            Also see:
                :meth:`~org.hipparchus.linear.MatrixUtils.createRealMatrix`
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealMatrix(int: int, int2: int) -> 'RealMatrix': ...
    @typing.overload
    @staticmethod
    def createRealVector(doubleArray: typing.List[float]) -> 'RealVector':
        """
            Creates a :class:`~org.hipparchus.linear.RealVector` with specified dimensions.
        
            Parameters:
                dimension (int): dimension of the vector
        
            Returns:
                a new vector
        
            Since:
                1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealVector(int: int) -> 'RealVector': ...
    _createRowFieldMatrix__T = typing.TypeVar('_createRowFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createRowFieldMatrix(tArray: typing.List[_createRowFieldMatrix__T]) -> 'FieldMatrix'[_createRowFieldMatrix__T]: ...
    @staticmethod
    def createRowRealMatrix(doubleArray: typing.List[float]) -> 'RealMatrix': ...
    @staticmethod
    def deserializeRealMatrix(object: typing.Any, string: str, objectInputStream: java.io.ObjectInputStream) -> None: ...
    @staticmethod
    def deserializeRealVector(object: typing.Any, string: str, objectInputStream: java.io.ObjectInputStream) -> None: ...
    @staticmethod
    def fractionMatrixToRealMatrix(fieldMatrix: 'FieldMatrix'[org.hipparchus.fraction.Fraction]) -> 'Array2DRowRealMatrix': ...
    @typing.overload
    @staticmethod
    def inverse(realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    @staticmethod
    def inverse(realMatrix: 'RealMatrix', double: float) -> 'RealMatrix': ...
    @staticmethod
    def isSymmetric(realMatrix: 'RealMatrix', double: float) -> bool:
        """
            Checks whether a matrix is symmetric.
        
            Parameters:
                matrix (:class:`~org.hipparchus.linear.RealMatrix`): Matrix to check.
                eps (double): Relative tolerance.
        
            Returns:
                :code:`true` if :code:`matrix` is symmetric.
        
        
        """
        ...
    @staticmethod
    def matrixExponential(realMatrix: 'RealMatrix') -> 'RealMatrix':
        """
            Computes the matrix exponential of the given matrix. The algorithm implementation follows the Pade approximant method of
        
            Higham, Nicholas J. Ã¢â‚¬Å“The Scaling and Squaring Method for the Matrix Exponential Revisited.Ã¢â‚¬ï¿½ SIAM Journal on
            Matrix Analysis and Applications 26, no. 4 (January 2005): 1179Ã¢â‚¬â€œ93.
        
            Parameters:
                rm (:class:`~org.hipparchus.linear.RealMatrix`): RealMatrix whose inverse shall be computed
        
            Returns:
                The inverse of :code:`rm`
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if matrix is not square
        
        
        """
        ...
    @staticmethod
    def serializeRealMatrix(realMatrix: 'RealMatrix', objectOutputStream: java.io.ObjectOutputStream) -> None: ...
    @staticmethod
    def serializeRealVector(realVector: 'RealVector', objectOutputStream: java.io.ObjectOutputStream) -> None: ...
    @staticmethod
    def solveLowerTriangularSystem(realMatrix: 'RealMatrix', realVector: 'RealVector') -> None: ...
    @staticmethod
    def solveUpperTriangularSystem(realMatrix: 'RealMatrix', realVector: 'RealVector') -> None: ...

class QRDecomposition:
    """
    public class QRDecomposition extends Object
    
        Calculates the QR-decomposition of a matrix.
    
        The QR-decomposition of a matrix A consists of two matrices Q and R that satisfy: A = QR, Q is orthogonal (Q :sup:`T` Q
        = I), and R is upper triangular. If A is mÃ—n, Q is mÃ—m and R mÃ—n.
    
        This class compute the decomposition using Householder reflectors.
    
        For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows,
        which is much more cache-efficient in Java.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library,
        with the following changes:
    
          - a :meth:`~org.hipparchus.linear.QRDecomposition.getQT` method has been added,
          - the :code:`solve` and :code:`isFullRank` methods have been replaced by a
            :meth:`~org.hipparchus.linear.QRDecomposition.getSolver` method and the equivalent methods provided by the returned
            :class:`~org.hipparchus.linear.DecompositionSolver`.
    
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getH(self) -> 'RealMatrix':
        """
            Returns the Householder reflector vectors.
        
            H is a lower trapezoidal matrix whose columns represent each successive Householder reflector vector. This matrix is
            used to compute Q.
        
            Returns:
                a matrix containing the Householder reflector vectors
        
        
        """
        ...
    def getQ(self) -> 'RealMatrix':
        """
            Returns the matrix Q of the decomposition.
        
            Q is an orthogonal matrix
        
            Returns:
                the Q matrix
        
        
        """
        ...
    def getQT(self) -> 'RealMatrix':
        """
            Returns the transpose of the matrix Q of the decomposition.
        
            Q is an orthogonal matrix
        
            Returns:
                the transpose of the Q matrix, Q :sup:`T`
        
        
        """
        ...
    def getR(self) -> 'RealMatrix':
        """
            Returns the matrix R of the decomposition.
        
            R is an upper-triangular matrix
        
            Returns:
                the R matrix
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Least Square sense means a solver can be computed for an overdetermined system, (i.e. a system with more equations than
            unknowns, which corresponds to a tall A matrix with more rows than columns). In any case, if the matrix is singular
            within the tolerance set at :meth:`~org.hipparchus.linear.QRDecomposition.QRDecomposition`, an error will be triggered
            when the :meth:`~org.hipparchus.linear.DecompositionSolver.solve` method will be called.
        
            Returns:
                a solver
        
        
        """
        ...

class RealLinearOperator:
    """
    public interface RealLinearOperator
    
        This class defines a linear operator operating on real (:code:`double`) vector spaces. No direct access to the
        coefficients of the underlying matrix is provided.
    
        The motivation for such an interface is well stated by :meth:`~org.hipparchus.linear.RealLinearOperator.BARR1994`:
            We restrict ourselves to iterative methods, which work by repeatedly improving an approximate solution until it is
            accurate enough. These methods access the coefficient matrix A of the linear system only via the matrix-vector product y
            = A Â· x (and perhaps z = A :sup:`T` Â· x). Thus the user need only supply a subroutine for computing y (and perhaps z)
            given x, which permits full exploitation of the sparsity or other special structure of A.
    
    
        :class:`~org.hipparchus.linear`
          R. Barrett, M. Berry, T. F. Chan, J. Demmel, J. M. Donato, J. Dongarra, V. Eijkhout, R. Pozo, C. Romine and H. Van der
            Vorst, *Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods*, SIAM
    """
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def isTransposable(self) -> bool:
        """
            Returns :code:`true` if this operator supports :meth:`~org.hipparchus.linear.RealLinearOperator.operateTranspose`.
        
            If :code:`true` is returned, :meth:`~org.hipparchus.linear.RealLinearOperator.operateTranspose` should not throw
            :code:`UnsupportedOperationException`.
        
            The default implementation returns :code:`false`.
        
            Returns:
                :code:`false`
        
        
        """
        ...
    def operate(self, realVector: 'RealVector') -> 'RealVector': ...
    def operateTranspose(self, realVector: 'RealVector') -> 'RealVector': ...

class RealMatrixChangingVisitor:
    """
    public interface RealMatrixChangingVisitor
    
        Interface defining a visitor for matrix entries.
    
        Also see:
            :class:`~org.hipparchus.linear.DefaultRealMatrixChangingVisitor`
    """
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> float:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

class RealMatrixFormat:
    """
    public class RealMatrixFormat extends Object
    
        Formats a :code:`nxm` matrix in components list format "{{a :sub:`0` :sub:`0` ,a :sub:`0` :sub:`1` , ..., a :sub:`0`
        :sub:`m-1` },{a :sub:`1` :sub:`0` , a :sub:`1` :sub:`1` , ..., a :sub:`1` :sub:`m-1` },{...},{ a :sub:`n-1` :sub:`0` , a
        :sub:`n-1` :sub:`1` , ..., a :sub:`n-1` :sub:`m-1` }}".
    
        The prefix and suffix "{" and "}", the row prefix and suffix "{" and "}", the row separator "," and the column separator
        "," can be replaced by any user-defined strings. The number format for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{{1,1,1}}" and " { { 1
        , 1 , 1 } } " will be parsed without error and the same matrix will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
        **Note:** the grouping functionality of the used null is disabled to prevent problems when parsing (e.g. 1,345.34 would
        be a valid number but conflicts with the default column separator).
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, string4: str, string5: str, string6: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, realMatrix: 'RealMatrix') -> str:
        """
            This method calls :meth:`~org.hipparchus.linear.RealMatrixFormat.format`.
        
            Parameters:
                m (:class:`~org.hipparchus.linear.RealMatrix`): RealMatrix object to format.
        
            Returns:
                a formatted matrix.
        
            Formats a :class:`~org.hipparchus.linear.RealMatrix` object to produce a string.
        
            Parameters:
                matrix (:class:`~org.hipparchus.linear.RealMatrix`): the object to format.
                toAppendTo (StringBuffer): where the text is to be appended
                pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    def format(self, realMatrix: 'RealMatrix', stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]:
        """
            Get the set of locales for which real vectors formats are available.
        
            This is the same set as the null set.
        
            Returns:
                available real vector format locales.
        
        
        """
        ...
    def getColumnSeparator(self) -> str:
        """
            Get the format separator between components.
        
            Returns:
                format separator between components.
        
        
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
    @typing.overload
    @staticmethod
    def getRealMatrixFormat() -> 'RealMatrixFormat':
        """
            Returns the default real vector format for the current locale.
        
            Returns:
                the default real vector format.
        
            Since:
                1.4
        
        """
        ...
    @typing.overload
    @staticmethod
    def getRealMatrixFormat(locale: java.util.Locale) -> 'RealMatrixFormat':
        """
            Returns the default real vector format for the given locale.
        
            Parameters:
                locale (Locale): the specific locale used by the format.
        
            Returns:
                the real vector format specific to the given locale.
        
            Since:
                1.4
        
        
        """
        ...
    def getRowPrefix(self) -> str:
        """
            Get the format prefix.
        
            Returns:
                format prefix.
        
        
        """
        ...
    def getRowSeparator(self) -> str:
        """
            Get the format separator between rows of the matrix.
        
            Returns:
                format separator for rows.
        
        
        """
        ...
    def getRowSuffix(self) -> str:
        """
            Get the format suffix.
        
            Returns:
                format suffix.
        
        
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
    def parse(self, string: str) -> 'RealMatrix':
        """
            Parse a string to produce a :class:`~org.hipparchus.linear.RealMatrix` object.
        
            Parameters:
                source (String): String to parse.
        
            Returns:
                the parsed :class:`~org.hipparchus.linear.RealMatrix` object.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the beginning of the specified string cannot be parsed.
        
            Parse a string to produce a :class:`~org.hipparchus.linear.RealMatrix` object.
        
            Parameters:
                source (String): String to parse.
                pos (ParsePosition): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.linear.RealMatrix` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'RealMatrix': ...

class RealMatrixPreservingVisitor:
    """
    public interface RealMatrixPreservingVisitor
    
        Interface defining a visitor for matrix entries.
    
        Also see:
            :class:`~org.hipparchus.linear.DefaultRealMatrixPreservingVisitor`
    """
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> None:
        """
            Visit one matrix entry.
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
        
        """
        ...

class RealVector:
    """
    public abstract class RealVector extends Object
    
        Class defining a real-valued vector with basic algebraic operations.
    
        vector element indexing is 0-based -- e.g., :code:`getEntry(0)` returns the first element of the vector.
    
        The :code:`code map` and :code:`mapToSelf` methods operate on vectors element-wise, i.e. they perform the same operation
        (adding a scalar, applying a function ...) on each element in turn. The :code:`map` versions create a new vector to hold
        the result and do not change the instance. The :code:`mapToSelf` version uses the instance itself to store the results,
        so the instance is changed by this method. In all cases, the result vector is returned by the methods, allowing the
        *fluent API* style, like this:
    
        .. code-block: java
        
           RealVector result = v.mapAddToSelf(3.4).mapToSelf(new Tan()).mapToSelf(new Power(2.3));
    """
    def __init__(self): ...
    def add(self, realVector: 'RealVector') -> 'RealVector': ...
    def addToEntry(self, int: int, double: float) -> None: ...
    @typing.overload
    def append(self, double: float) -> 'RealVector':
        """
            Construct a new vector by appending a vector to this vector.
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a new vector by appending a double to this vector.
        
            Parameters:
                d (double): double to append.
        
            Returns:
                a new vector.
        
        
        """
        ...
    @typing.overload
    def append(self, realVector: 'RealVector') -> 'RealVector': ...
    def combine(self, double: float, double2: float, realVector: 'RealVector') -> 'RealVector': ...
    def combineToSelf(self, double: float, double2: float, realVector: 'RealVector') -> 'RealVector': ...
    def copy(self) -> 'RealVector':
        """
            Returns a (deep) copy of this vector.
        
            Returns:
                a vector copy.
        
        
        """
        ...
    def cosine(self, realVector: 'RealVector') -> float: ...
    def dotProduct(self, realVector: 'RealVector') -> float: ...
    def ebeDivide(self, realVector: 'RealVector') -> 'RealVector': ...
    def ebeMultiply(self, realVector: 'RealVector') -> 'RealVector': ...
    def equals(self, object: typing.Any) -> bool: ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Returns:
                the size of this vector.
        
        
        """
        ...
    def getDistance(self, realVector: 'RealVector') -> float: ...
    def getEntry(self, int: int) -> float: ...
    def getL1Distance(self, realVector: 'RealVector') -> float: ...
    def getL1Norm(self) -> float:
        """
            Returns the L :sub:`1` norm of the vector.
        
            The L :sub:`1` norm is the sum of the absolute values of the elements.
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealVector.getNorm`, :meth:`~org.hipparchus.linear.RealVector.getLInfNorm`,
                :meth:`~org.hipparchus.linear.RealVector.getL1Distance`
        
        
        """
        ...
    def getLInfDistance(self, realVector: 'RealVector') -> float: ...
    def getLInfNorm(self) -> float:
        """
            Returns the L :sub:`∞` norm of the vector.
        
            The L :sub:`∞` norm is the max of the absolute values of the elements.
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealVector.getNorm`, :meth:`~org.hipparchus.linear.RealVector.getL1Norm`,
                :meth:`~org.hipparchus.linear.RealVector.getLInfDistance`
        
        
        """
        ...
    def getMaxIndex(self) -> int:
        """
            Get the index of the maximum entry.
        
            Returns:
                the index of the maximum entry or -1 if vector length is 0 or all entries are :code:`NaN`
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
            Get the value of the maximum entry.
        
            Returns:
                the value of the maximum entry or :code:`NaN` if all entries are :code:`NaN`.
        
        
        """
        ...
    def getMinIndex(self) -> int:
        """
            Get the index of the minimum entry.
        
            Returns:
                the index of the minimum entry or -1 if vector length is 0 or all entries are :code:`NaN`.
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
            Get the value of the minimum entry.
        
            Returns:
                the value of the minimum entry or :code:`NaN` if all entries are :code:`NaN`.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the L :sub:`2` norm of the vector.
        
            The L :sub:`2` norm is the root of the sum of the squared elements.
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealVector.getL1Norm`, :meth:`~org.hipparchus.linear.RealVector.getLInfNorm`,
                :meth:`~org.hipparchus.linear.RealVector.getDistance`
        
        
        """
        ...
    def getSubVector(self, int: int, int2: int) -> 'RealVector': ...
    def hashCode(self) -> int: ...
    def isInfinite(self) -> bool:
        """
            Check whether any coordinate of this vector is infinite and none are :code:`NaN`.
        
            Returns:
                :code:`true` if any coordinate of this vector is infinite and none are :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check whether any coordinate of this vector is :code:`NaN`.
        
            Returns:
                :code:`true` if any coordinate of this vector is :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator['RealVector.Entry']: ...
    def map(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> 'RealVector':
        """
            Acts as if implemented as:
        
            .. code-block: java
            
              return copy().mapToSelf(function);
             
            Returns a new vector. Does not change instance data.
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a new vector.
        
        
        """
        ...
    def mapAdd(self, double: float) -> 'RealVector':
        """
            Add a value to each entry. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this` + :code:`d`.
        
        
        """
        ...
    def mapAddToSelf(self, double: float) -> 'RealVector':
        """
            Add a value to each entry. The instance is changed in-place.
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapDivide(self, double: float) -> 'RealVector':
        """
            Divide each entry by the argument. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Value to divide by.
        
            Returns:
                :code:`this` / :code:`d`.
        
        
        """
        ...
    def mapDivideToSelf(self, double: float) -> 'RealVector':
        """
            Divide each entry by the argument. The instance is changed in-place.
        
            Parameters:
                d (double): Value to divide by.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapMultiply(self, double: float) -> 'RealVector':
        """
            Multiply each entry by the argument. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Multiplication factor.
        
            Returns:
                :code:`this` * :code:`d`.
        
        
        """
        ...
    def mapMultiplyToSelf(self, double: float) -> 'RealVector':
        """
            Multiply each entry. The instance is changed in-place.
        
            Parameters:
                d (double): Multiplication factor.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapSubtract(self, double: float) -> 'RealVector':
        """
            Subtract a value from each entry. Returns a new vector. Does not change instance data.
        
            Parameters:
                d (double): Value to be subtracted.
        
            Returns:
                :code:`this` - :code:`d`.
        
        
        """
        ...
    def mapSubtractToSelf(self, double: float) -> 'RealVector':
        """
            Subtract a value from each entry. The instance is changed in-place.
        
            Parameters:
                d (double): Value to be subtracted.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapToSelf(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> 'RealVector':
        """
            Acts as if it is implemented as:
        
            .. code-block: java
            
              Entry e = null;
              for(Iterator it = iterator(); it.hasNext(); e = it.next()) {
                  e.setValue(function.value(e.getValue()));
              }
             
             Entries of this vector are modified in-place by this method.
        
            Parameters:
              :code:`function` - Function to apply to each entry.
        
            Returns:
              a reference to this vector.
        
        
        """
        ...
    def outerProduct(self, realVector: 'RealVector') -> 'RealMatrix':
        """
            Compute the outer product.
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): Vector with which outer product should be computed.
        
            Returns:
                the matrix outer product between this instance and :code:`v`.
        
        
        """
        ...
    def projection(self, realVector: 'RealVector') -> 'RealVector': ...
    def set(self, double: float) -> None:
        """
            Set all elements to a single value.
        
            Parameters:
                value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, int: int, double: float) -> None: ...
    def setSubVector(self, int: int, realVector: 'RealVector') -> None: ...
    def sparseIterator(self) -> java.util.Iterator['RealVector.Entry']: ...
    def subtract(self, realVector: 'RealVector') -> 'RealVector': ...
    def toArray(self) -> typing.List[float]:
        """
            Convert the vector to an array of :code:`double`s. The array is independent from this vector data: the elements are
            copied.
        
            Returns:
                an array containing a copy of the vector elements.
        
        
        """
        ...
    def unitVector(self) -> 'RealVector': ...
    def unitize(self) -> None: ...
    @staticmethod
    def unmodifiableRealVector(realVector: 'RealVector') -> 'RealVector':
        """
            Returns an unmodifiable view of the specified vector. The returned vector has read-only access. An attempt to modify it
            will result in a :class:`~org.hipparchus.exception.MathRuntimeException`. However, the returned vector is *not*
            immutable, since any modification of :code:`v` will also change the returned view. For example, in the following piece
            of code
        
            .. code-block: java
            
                 RealVector v = new ArrayRealVector(2);
                 RealVector w = RealVector.unmodifiableRealVector(v);
                 v.setEntry(0, 1.2);
                 v.setEntry(1, -3.4);
             
            the changes will be seen in the :code:`w` view of :code:`v`.
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): Vector for which an unmodifiable view is to be returned.
        
            Returns:
                an unmodifiable view of :code:`v`.
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor') -> float:
        """
            Visits (but does not alter) all entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
        public double walkInDefaultOrder(:class:`~org.hipparchus.linear.RealVectorPreservingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (but does not alter) some entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Visits (and possibly alters) all entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): the visitor to be used to process and modify the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
        public double walkInDefaultOrder(:class:`~org.hipparchus.linear.RealVectorChangingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (and possibly alters) some entries of this vector in default order (increasing index).
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor', int: int, int2: int) -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor') -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor', int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor') -> float:
        """
            Visits (but does not alter) all entries of this vector in optimized order. The order in which the entries are visited is
            selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealVectorPreservingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (but does not alter) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Visits (and possibly alters) all entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealVectorChangingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (and possibly change) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor', int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor') -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: 'RealVectorPreservingVisitor', int: int, int2: int) -> float: ...
    class Entry:
        def __init__(self, realVector: 'RealVector'): ...
        def getIndex(self) -> int: ...
        def getValue(self) -> float: ...
        def setIndex(self, int: int) -> None: ...
        def setValue(self, double: float) -> None: ...

class RealVectorChangingVisitor:
    """
    public interface RealVectorChangingVisitor
    
        This interface defines a visitor for the entries of a vector. Visitors implementing this interface may alter the entries
        of the vector being visited.
    """
    def end(self) -> float:
        """
            End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder`,
                :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder`,
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder` or
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder`
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int) -> None:
        """
            Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
            Parameters:
                dimension (int): the size of the vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, int: int, double: float) -> float:
        """
            Visit one entry of the vector.
        
            Parameters:
                index (int): the index of the entry being visited
                value (double): the value of the entry being visited
        
            Returns:
                the new value of the entry being visited
        
        
        """
        ...

class RealVectorFormat:
    """
    public class RealVectorFormat extends Object
    
        Formats a vector in components list format "{v0; v1; ...; vk-1}".
    
        The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format
        for components can be configured.
    
        White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the
        default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1
        ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse
        position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str): ...
    @typing.overload
    def __init__(self, string: str, string2: str, string3: str, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def __init__(self, numberFormat: java.text.NumberFormat): ...
    @typing.overload
    def format(self, realVector: RealVector) -> str:
        """
            This method calls :meth:`~org.hipparchus.linear.RealVectorFormat.format`.
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): RealVector object to format.
        
            Returns:
                a formatted vector.
        
            Formats a :class:`~org.hipparchus.linear.RealVector` object to produce a string.
        
            Parameters:
                vector (:class:`~org.hipparchus.linear.RealVector`): the object to format.
                toAppendTo (StringBuffer): where the text is to be appended
                pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
            Returns:
                the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    def format(self, realVector: RealVector, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.List[java.util.Locale]:
        """
            Get the set of locales for which real vectors formats are available.
        
            This is the same set as the null set.
        
            Returns:
                available real vector format locales.
        
        
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
    @typing.overload
    @staticmethod
    def getRealVectorFormat() -> 'RealVectorFormat':
        """
            Returns the default real vector format for the current locale.
        
            Returns:
                the default real vector format.
        
            Since:
                1.4
        
        """
        ...
    @typing.overload
    @staticmethod
    def getRealVectorFormat(locale: java.util.Locale) -> 'RealVectorFormat':
        """
            Returns the default real vector format for the given locale.
        
            Parameters:
                locale (Locale): the specific locale used by the format.
        
            Returns:
                the real vector format specific to the given locale.
        
            Since:
                1.4
        
        
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
    def parse(self, string: str) -> 'ArrayRealVector':
        """
            Parse a string to produce a :class:`~org.hipparchus.linear.RealVector` object.
        
            Parameters:
                source (String): String to parse.
        
            Returns:
                the parsed :class:`~org.hipparchus.linear.RealVector` object.
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalStateException`: if the beginning of the specified string cannot be parsed.
        
            Parse a string to produce a :class:`~org.hipparchus.linear.RealVector` object.
        
            Parameters:
                source (String): String to parse.
                pos (ParsePosition): input/ouput parsing parameter.
        
            Returns:
                the parsed :class:`~org.hipparchus.linear.RealVector` object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'ArrayRealVector': ...

class RealVectorPreservingVisitor:
    """
    public interface RealVectorPreservingVisitor
    
        This interface defines a visitor for the entries of a vector. Visitors implementing this interface do not alter the
        entries of the vector being visited.
    """
    def end(self) -> float:
        """
            End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder`,
                :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder`,
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder` or
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder`
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int) -> None:
        """
            Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
            Parameters:
                dimension (int): the size of the vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, int: int, double: float) -> None:
        """
            Visit one entry of the vector.
        
            Parameters:
                index (int): the index of the entry being visited
                value (double): the value of the entry being visited
        
        
        """
        ...

class RectangularCholeskyDecomposition:
    """
    public class RectangularCholeskyDecomposition extends Object
    
        Calculates the rectangular Cholesky decomposition of a matrix.
    
        The rectangular Cholesky decomposition of a real symmetric positive semidefinite matrix A consists of a rectangular
        matrix B with the same number of rows such that: A is almost equal to BB :sup:`T` , depending on a user-defined
        tolerance. In a sense, this is the square root of A.
    
        The difference with respect to the regular :class:`~org.hipparchus.linear.CholeskyDecomposition` is that rows/columns
        may be permuted (hence the rectangular shape instead of the traditional triangular shape) and there is a threshold to
        ignore small diagonal elements. This is used for example to generate
        :class:`~org.hipparchus.random.CorrelatedRandomVectorGenerator` in a p-dimension subspace (p < n). In other words, it
        allows generating random vectors from a covariance matrix that is only positive semidefinite, and not positive definite.
    
        Rectangular Cholesky decomposition is *not* suited for solving linear systems, so it does not provide any
        :class:`~org.hipparchus.linear.DecompositionSolver`.
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/CholeskyDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/Cholesky_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getRank(self) -> int:
        """
            Get the rank of the symmetric positive semidefinite matrix. The r is the number of independent rows in the symmetric
            positive semidefinite matrix, it is also the number of columns of the rectangular matrix of the decomposition.
        
            Returns:
                r of the square matrix.
        
            Also see:
                :meth:`~org.hipparchus.linear.RectangularCholeskyDecomposition.getRootMatrix`
        
        
        """
        ...
    def getRootMatrix(self) -> 'RealMatrix':
        """
            Get the root of the covariance matrix. The root is the rectangular matrix :code:`B` such that the covariance matrix is
            equal to :code:`B.B :sup:`T``
        
            Returns:
                root of the square matrix
        
            Also see:
                :meth:`~org.hipparchus.linear.RectangularCholeskyDecomposition.getRank`
        
        
        """
        ...

class RiccatiEquationSolver:
    """
    public interface RiccatiEquationSolver
    
        An algebraic Riccati equation is a type of nonlinear equation that arises in the context of infinite-horizon optimal
        control problems in continuous time or discrete time. The continuous time algebraic Riccati equation (CARE): \[
        A^{T}X+XA-XBR^{-1}B^{T}X+Q=0 \} And the respective linear controller is: \[ K = R^{-1}B^{T}P \] A solver receives A, B,
        Q and R and computes P and K.
    """
    def getK(self) -> 'RealMatrix':
        """
            Get the linear controller k.
        
            Returns:
                the linear controller k
        
        
        """
        ...
    def getP(self) -> 'RealMatrix':
        """
            Get the solution.
        
            Returns:
                the p
        
        
        """
        ...

class SingularValueDecomposition:
    """
    public class SingularValueDecomposition extends Object
    
        Calculates the compact Singular Value Decomposition of a matrix.
    
        The Singular Value Decomposition of matrix A is a set of three matrices: U, Î£ and V such that A = U Ã— Î£ Ã— V :sup:`T`
        . Let A be a m Ã— n matrix, then U is a m Ã— p orthogonal matrix, Î£ is a p Ã— p diagonal matrix with positive or null
        elements, V is a p Ã— n orthogonal matrix (hence V :sup:`T` is also orthogonal) where p=min(m,n).
    
        This class is similar to the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library,
        with the following changes:
    
          - the :code:`norm2` method which has been renamed as :meth:`~org.hipparchus.linear.SingularValueDecomposition.getNorm`,
          - the :code:`cond` method which has been renamed as
            :meth:`~org.hipparchus.linear.SingularValueDecomposition.getConditionNumber`,
          - the :code:`rank` method which has been renamed as :meth:`~org.hipparchus.linear.SingularValueDecomposition.getRank`,
          - a :meth:`~org.hipparchus.linear.SingularValueDecomposition.getUT` method has been added,
          - a :meth:`~org.hipparchus.linear.SingularValueDecomposition.getVT` method has been added,
          - a :meth:`~org.hipparchus.linear.SingularValueDecomposition.getSolver` method has been added,
          - a :meth:`~org.hipparchus.linear.SingularValueDecomposition.getCovariance` method has been added.
    
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/SingularValueDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/Singular_value_decomposition>`
    """
    def __init__(self, realMatrix: 'RealMatrix'): ...
    def getConditionNumber(self) -> float:
        """
            Return the condition number of the matrix.
        
            Returns:
                condition number of the matrix
        
        
        """
        ...
    def getCovariance(self, double: float) -> 'RealMatrix':
        """
            Returns the n × n covariance matrix.
        
            The covariance matrix is V Ã— J Ã— V :sup:`T` where J is the diagonal matrix of the inverse of the squares of the
            singular values.
        
            Parameters:
                minSingularValue (double): value below which singular values are ignored (a 0 or negative value implies all singular value will be used)
        
            Returns:
                covariance matrix
        
            Raises:
                : if minSingularValue is larger than the largest singular value, meaning all singular values are ignored
        
        
        """
        ...
    def getInverseConditionNumber(self) -> float:
        """
            Computes the inverse of the condition number. In cases of rank deficiency, the
            :meth:`~org.hipparchus.linear.SingularValueDecomposition.getConditionNumber` will become undefined.
        
            Returns:
                the inverse of the condition number.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the L :sub:`2` norm of the matrix.
        
            The L :sub:`2` norm is max(|A Ã— u| :sub:`2` / |u| :sub:`2` ), where |.| :sub:`2` denotes the vectorial 2-norm (i.e. the
            traditional euclidian norm).
        
            Returns:
                norm
        
        
        """
        ...
    def getRank(self) -> int:
        """
            Return the effective numerical matrix rank.
        
            The effective numerical rank is the number of non-negligible singular values. The threshold used to identify
            non-negligible terms is max(m,n) Ã— ulp(s :sub:`1` ) where ulp(s :sub:`1` ) is the least significant bit of the largest
            singular value.
        
            Returns:
                effective numerical matrix rank
        
        
        """
        ...
    def getS(self) -> 'RealMatrix':
        """
            Returns the diagonal matrix Σ of the decomposition.
        
            Σ is a diagonal matrix. The singular values are provided in non-increasing order, for compatibility with Jama.
        
            Returns:
                the Σ matrix
        
        
        """
        ...
    def getSingularValues(self) -> typing.List[float]:
        """
            Returns the diagonal elements of the matrix Σ of the decomposition.
        
            The singular values are provided in non-increasing order, for compatibility with Jama.
        
            Returns:
                the diagonal elements of the Σ matrix
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Returns:
                a solver
        
        
        """
        ...
    def getU(self) -> 'RealMatrix':
        """
            Returns the matrix U of the decomposition.
        
            U is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the U matrix
        
            Also see:
                :meth:`~org.hipparchus.linear.SingularValueDecomposition.getUT`
        
        
        """
        ...
    def getUT(self) -> 'RealMatrix':
        """
            Returns the transpose of the matrix U of the decomposition.
        
            U is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the U matrix (or null if decomposed matrix is singular)
        
            Also see:
                :meth:`~org.hipparchus.linear.SingularValueDecomposition.getU`
        
        
        """
        ...
    def getV(self) -> 'RealMatrix':
        """
            Returns the matrix V of the decomposition.
        
            V is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the V matrix (or null if decomposed matrix is singular)
        
            Also see:
                :meth:`~org.hipparchus.linear.SingularValueDecomposition.getVT`
        
        
        """
        ...
    def getVT(self) -> 'RealMatrix':
        """
            Returns the transpose of the matrix V of the decomposition.
        
            V is an orthogonal matrix, i.e. its transpose is also its inverse.
        
            Returns:
                the V matrix (or null if decomposed matrix is singular)
        
            Also see:
                :meth:`~org.hipparchus.linear.SingularValueDecomposition.getV`
        
        
        """
        ...

_ArrayFieldVector__T = typing.TypeVar('_ArrayFieldVector__T', bound=org.hipparchus.FieldElement)  # <T>
class ArrayFieldVector(FieldVector[_ArrayFieldVector__T], java.io.Serializable, typing.Generic[_ArrayFieldVector__T]):
    """
    public class ArrayFieldVector<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object implements :class:`~org.hipparchus.linear.FieldVector`<T>, Serializable
    
        This class implements the :class:`~org.hipparchus.linear.FieldVector` interface with a
        :class:`~org.hipparchus.FieldElement` array.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, int: int, t: _ArrayFieldVector__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.List[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.List[_ArrayFieldVector__T], boolean: bool): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.List[_ArrayFieldVector__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.List[_ArrayFieldVector__T], tArray2: typing.List[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, tArray: typing.List[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, tArray: typing.List[_ArrayFieldVector__T], boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.List[_ArrayFieldVector__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, tArray: typing.List[_ArrayFieldVector__T], tArray2: typing.List[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, tArray: typing.List[_ArrayFieldVector__T], fieldVector: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T], boolean: bool): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T], tArray: typing.List[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T], fieldVector2: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def add(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def add(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def append(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def append(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def append(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def copy(self) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def dotProduct(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def dotProduct(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def ebeDivide(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def ebeDivide(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def ebeMultiply(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def ebeMultiply(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Test for the equality of two vectors.
        
            Overrides:
                 in class 
        
            Parameters:
                other (Object): Object to test for equality.
        
            Returns:
                :code:`true` if two vector objects are equal, :code:`false` otherwise.
        
        
        """
        ...
    def getDataRef(self) -> typing.List[_ArrayFieldVector__T]:
        """
            Returns a reference to the underlying data array.
        
            Does not make a fresh copy of the underlying data.
        
            Returns:
                array of entries
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.getDimension` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Returns:
                size
        
        
        """
        ...
    def getEntry(self, int: int) -> _ArrayFieldVector__T:
        """
            Returns the entry in the specified index.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.getEntry` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Parameters:
                index (int): Index location of entry to be fetched.
        
            Returns:
                the vector entry at :code:`index`.
        
            Also see:
                :meth:`~org.hipparchus.linear.FieldVector.setEntry`
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_ArrayFieldVector__T]: ...
    def getSubVector(self, int: int, int2: int) -> FieldVector[_ArrayFieldVector__T]: ...
    def hashCode(self) -> int:
        """
            Get a hashCode for the real vector.
        
            All NaN values have the same hash code.
        
            Overrides:
                 in class 
        
            Returns:
                a hash code value for this object
        
        
        """
        ...
    def mapAdd(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapAddToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapDivide(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapDivideToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapInv(self) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapInvToSelf(self) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapMultiply(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapMultiplyToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapSubtract(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    def mapSubtractToSelf(self, t: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'FieldMatrix'[_ArrayFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> 'FieldMatrix'[_ArrayFieldVector__T]: ...
    @typing.overload
    def projection(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def projection(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    @typing.overload
    def set(self, int: int, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> None: ...
    @typing.overload
    def set(self, t: _ArrayFieldVector__T) -> None:
        """
            Set all elements to a single value.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.set` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Parameters:
                value (:class:`~org.hipparchus.linear.ArrayFieldVector`): single value to set for all elements
        
        
        """
        ...
    def setEntry(self, int: int, t: _ArrayFieldVector__T) -> None:
        """
            Set a single element.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.setEntry` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Parameters:
                index (int): element index.
                value (:class:`~org.hipparchus.linear.ArrayFieldVector`): new value for the element.
        
            Also see:
                :meth:`~org.hipparchus.linear.FieldVector.getEntry`
        
        
        """
        ...
    def setSubVector(self, int: int, fieldVector: FieldVector[_ArrayFieldVector__T]) -> None: ...
    @typing.overload
    def subtract(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def subtract(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def toArray(self) -> typing.List[_ArrayFieldVector__T]:
        """
            Convert the vector to a T array.
        
            The array is independent from vector data, it's elements are copied.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.toArray` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Returns:
                array containing a copy of vector elements
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
            Since:
                2.0
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_ArrayFieldVector__T], int: int, int2: int) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_ArrayFieldVector__T], int: int, int2: int) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_ArrayFieldVector__T], int: int, int2: int) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_ArrayFieldVector__T]) -> _ArrayFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_ArrayFieldVector__T], int: int, int2: int) -> _ArrayFieldVector__T: ...

class ArrayRealVector(RealVector, java.io.Serializable):
    """
    public class ArrayRealVector extends :class:`~org.hipparchus.linear.RealVector` implements Serializable
    
        This class implements the :class:`~org.hipparchus.linear.RealVector` interface with a double array.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], boolean: bool): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], doubleArray2: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], int: int, int2: int): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], int: int, int2: int): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', boolean: bool): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', arrayRealVector2: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', realVector: RealVector): ...
    @typing.overload
    def __init__(self, realVector: RealVector): ...
    @typing.overload
    def __init__(self, realVector: RealVector, arrayRealVector: 'ArrayRealVector'): ...
    def add(self, realVector: RealVector) -> 'ArrayRealVector': ...
    def addToEntry(self, int: int, double: float) -> None: ...
    @typing.overload
    def append(self, arrayRealVector: 'ArrayRealVector') -> 'ArrayRealVector':
        """
            Construct a new vector by appending a vector to this vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.append` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a vector by appending a vector to this vector.
        
            Parameters:
                v (:class:`~org.hipparchus.linear.ArrayRealVector`): Vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a new vector by appending a double to this vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.append` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                in (double): double to append.
        
            Returns:
                a new vector.
        
        
        """
        ...
    @typing.overload
    def append(self, double: float) -> RealVector: ...
    @typing.overload
    def append(self, realVector: RealVector) -> RealVector: ...
    def combine(self, double: float, double2: float, realVector: RealVector) -> 'ArrayRealVector': ...
    def combineToSelf(self, double: float, double2: float, realVector: RealVector) -> 'ArrayRealVector': ...
    def copy(self) -> 'ArrayRealVector':
        """
            Returns a (deep) copy of this vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.copy` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                a vector copy.
        
        
        """
        ...
    def dotProduct(self, realVector: RealVector) -> float: ...
    def ebeDivide(self, realVector: RealVector) -> 'ArrayRealVector': ...
    def ebeMultiply(self, realVector: RealVector) -> 'ArrayRealVector': ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are
            :code:`NaN`, the two real vectors are considered to be equal. :code:`NaN` coordinates are considered to affect globally
            the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to
            :code:`NaN`, the real vector is equal to a vector with all :code:`NaN` coordinates.
        
            This method *must* be overriden by concrete subclasses of :class:`~org.hipparchus.linear.RealVector` (the current
            implementation throws an exception).
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.equals` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                other (Object): Object to test for equality.
        
            Returns:
                :code:`true` if two vector objects are equal, :code:`false` if :code:`other` is null, not an instance of
                :code:`RealVector`, or not equal to this :code:`RealVector` instance.
        
        
        """
        ...
    def getDataRef(self) -> typing.List[float]:
        """
            Get a reference to the underlying data array. This method does not make a fresh copy of the underlying data.
        
            Returns:
                the array of entries.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.getDimension` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                the size of this vector.
        
        
        """
        ...
    def getDistance(self, realVector: RealVector) -> float: ...
    def getEntry(self, int: int) -> float: ...
    def getL1Distance(self, realVector: RealVector) -> float: ...
    def getL1Norm(self) -> float:
        """
            Returns the L :sub:`1` norm of the vector.
        
            The L :sub:`1` norm is the sum of the absolute values of the elements.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.getL1Norm` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealVector.getNorm`, :meth:`~org.hipparchus.linear.RealVector.getLInfNorm`,
                :meth:`~org.hipparchus.linear.RealVector.getL1Distance`
        
        
        """
        ...
    def getLInfDistance(self, realVector: RealVector) -> float: ...
    def getLInfNorm(self) -> float:
        """
            Returns the L :sub:`∞` norm of the vector.
        
            The L :sub:`∞` norm is the max of the absolute values of the elements.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.getLInfNorm` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealVector.getNorm`, :meth:`~org.hipparchus.linear.RealVector.getL1Norm`,
                :meth:`~org.hipparchus.linear.RealVector.getLInfDistance`
        
        
        """
        ...
    def getNorm(self) -> float:
        """
            Returns the L :sub:`2` norm of the vector.
        
            The L :sub:`2` norm is the root of the sum of the squared elements.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.getNorm` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                the norm.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealVector.getL1Norm`, :meth:`~org.hipparchus.linear.RealVector.getLInfNorm`,
                :meth:`~org.hipparchus.linear.RealVector.getDistance`
        
        
        """
        ...
    def getSubVector(self, int: int, int2: int) -> RealVector: ...
    def hashCode(self) -> int:
        """
            . This method *must* be overriden by concrete subclasses of :class:`~org.hipparchus.linear.RealVector` (current
            implementation throws an exception). All :code:`NaN` values have the same hash code.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.hashCode` in class :class:`~org.hipparchus.linear.RealVector`
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Check whether any coordinate of this vector is infinite and none are :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.isInfinite` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                :code:`true` if any coordinate of this vector is infinite and none are :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check if any coordinate of this vector is :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.isNaN` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                :code:`true` if any coordinate of this vector is :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def map(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> 'ArrayRealVector':
        """
            Acts as if implemented as:
        
            .. code-block: java
            
              return copy().mapToSelf(function);
             
            Returns a new vector. Does not change instance data.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.map` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a new vector.
        
        
        """
        ...
    def mapAddToSelf(self, double: float) -> RealVector:
        """
            Add a value to each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.mapAddToSelf` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapDivideToSelf(self, double: float) -> RealVector:
        """
            Divide each entry by the argument. The instance is changed in-place.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.mapDivideToSelf` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): Value to divide by.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapMultiplyToSelf(self, double: float) -> RealVector:
        """
            Multiply each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.mapMultiplyToSelf` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): Multiplication factor.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapSubtractToSelf(self, double: float) -> RealVector:
        """
            Subtract a value from each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.mapSubtractToSelf` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): Value to be subtracted.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def mapToSelf(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> 'ArrayRealVector':
        """
            Acts as if it is implemented as:
        
            .. code-block: java
            
              Entry e = null;
              for(Iterator it = iterator(); it.hasNext(); e = it.next()) {
                  e.setValue(function.value(e.getValue()));
              }
             
             Entries of this vector are modified in-place by this method.
        
            Overrides:
              :meth:`~org.hipparchus.linear.RealVector.mapToSelf` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
              :code:`function` - Function to apply to each entry.
        
            Returns:
              a reference to this vector.
        
        
        """
        ...
    def outerProduct(self, realVector: RealVector) -> 'RealMatrix':
        """
            Compute the outer product.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.outerProduct` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): Vector with which outer product should be computed.
        
            Returns:
                the matrix outer product between this instance and :code:`v`.
        
        
        """
        ...
    def set(self, double: float) -> None:
        """
            Set all elements to a single value.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.set` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, int: int, double: float) -> None: ...
    @typing.overload
    def setSubVector(self, int: int, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setSubVector(self, int: int, realVector: RealVector) -> None: ...
    def subtract(self, realVector: RealVector) -> 'ArrayRealVector': ...
    def toArray(self) -> typing.List[float]:
        """
            Convert the vector to an array of :code:`double`s. The array is independent from this vector data: the elements are
            copied.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.toArray` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                an array containing a copy of the vector elements.
        
        
        """
        ...
    def toString(self) -> str:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor) -> float:
        """
            Visits (but does not alter) all entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
        public double walkInDefaultOrder(:class:`~org.hipparchus.linear.RealVectorPreservingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (but does not alter) some entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
        
            Visits (and possibly alters) all entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): the visitor to be used to process and modify the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
        public double walkInDefaultOrder(:class:`~org.hipparchus.linear.RealVectorChangingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (and possibly alters) some entries of this vector in default order (increasing index).
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInDefaultOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor, int: int, int2: int) -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor) -> float: ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor, int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor) -> float:
        """
            Visits (but does not alter) all entries of this vector in optimized order. The order in which the entries are visited is
            selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealVectorPreservingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (but does not alter) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorPreservingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
        
            Visits (and possibly alters) all entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): the visitor to be used to process the entries of this vector
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealVectorChangingVisitor` visitor, int start, int end) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visits (and possibly change) some entries of this vector in optimized order. The order in which the entries are visited
            is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this
            abstract class. In this implementation, the optimized order is the default order.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.walkInOptimizedOrder` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealVectorChangingVisitor`): visitor to be used to process the entries of this vector
                start (int): the index of the first entry to be visited
                end (int): the index of the last entry to be visited (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealVectorChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`end < start`.
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor, int: int, int2: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realVectorPreservingVisitor: RealVectorPreservingVisitor, int: int, int2: int) -> float: ...

class CholeskyDecomposer(MatrixDecomposer):
    """
    public class CholeskyDecomposer extends Object implements :class:`~org.hipparchus.linear.MatrixDecomposer`
    
        Matrix decomposer using Cholseky decomposition.
    
        Since:
            1.3
    """
    def __init__(self, double: float, double2: float): ...
    def decompose(self, realMatrix: 'RealMatrix') -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Specified by:
                :meth:`~org.hipparchus.linear.MatrixDecomposer.decompose` in interface :class:`~org.hipparchus.linear.MatrixDecomposer`
        
            Parameters:
                a (:class:`~org.hipparchus.linear.RealMatrix`): coefficient matrix A to decompose
        
            Returns:
                a solver
        
        
        """
        ...

_DefaultFieldMatrixChangingVisitor__T = typing.TypeVar('_DefaultFieldMatrixChangingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class DefaultFieldMatrixChangingVisitor(FieldMatrixChangingVisitor[_DefaultFieldMatrixChangingVisitor__T], typing.Generic[_DefaultFieldMatrixChangingVisitor__T]):
    """
    public class DefaultFieldMatrixChangingVisitor<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object implements :class:`~org.hipparchus.linear.FieldMatrixChangingVisitor`<T>
    
        Default implementation of the :class:`~org.hipparchus.linear.FieldMatrixChangingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    """
    def __init__(self, t: _DefaultFieldMatrixChangingVisitor__T): ...
    def end(self) -> _DefaultFieldMatrixChangingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldMatrixChangingVisitor.end`Â in
                interfaceÂ :class:`~org.hipparchus.linear.FieldMatrixChangingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldMatrixChangingVisitor.start`Â in
                interfaceÂ :class:`~org.hipparchus.linear.FieldMatrixChangingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _DefaultFieldMatrixChangingVisitor__T) -> _DefaultFieldMatrixChangingVisitor__T:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldMatrixChangingVisitor.visit`Â in
                interfaceÂ :class:`~org.hipparchus.linear.FieldMatrixChangingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~org.hipparchus.linear.DefaultFieldMatrixChangingVisitor`): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

_DefaultFieldMatrixPreservingVisitor__T = typing.TypeVar('_DefaultFieldMatrixPreservingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class DefaultFieldMatrixPreservingVisitor(FieldMatrixPreservingVisitor[_DefaultFieldMatrixPreservingVisitor__T], typing.Generic[_DefaultFieldMatrixPreservingVisitor__T]):
    """
    public class DefaultFieldMatrixPreservingVisitor<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object implements :class:`~org.hipparchus.linear.FieldMatrixPreservingVisitor`<T>
    
        Default implementation of the :class:`~org.hipparchus.linear.FieldMatrixPreservingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    """
    def __init__(self, t: _DefaultFieldMatrixPreservingVisitor__T): ...
    def end(self) -> _DefaultFieldMatrixPreservingVisitor__T:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldMatrixPreservingVisitor.end`Â in
                interfaceÂ :class:`~org.hipparchus.linear.FieldMatrixPreservingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldMatrixPreservingVisitor.start`Â in
                interfaceÂ :class:`~org.hipparchus.linear.FieldMatrixPreservingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, t: _DefaultFieldMatrixPreservingVisitor__T) -> None:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldMatrixPreservingVisitor.visit`Â in
                interfaceÂ :class:`~org.hipparchus.linear.FieldMatrixPreservingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (:class:`~org.hipparchus.linear.DefaultFieldMatrixPreservingVisitor`): current value of the entry
        
        
        """
        ...

class DefaultIterativeLinearSolverEvent(IterativeLinearSolverEvent):
    """
    public class DefaultIterativeLinearSolverEvent extends :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`
    
        A default concrete implementation of the abstract class :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, object: typing.Any, int: int, realVector: RealVector, realVector2: RealVector, double: float): ...
    @typing.overload
    def __init__(self, object: typing.Any, int: int, realVector: RealVector, realVector2: RealVector, realVector3: RealVector, double: float): ...
    def getNormOfResidual(self) -> float:
        """
            Returns the norm of the residual. The returned value is not required to be *exact*. Instead, the norm of the so-called
            *updated* residual (if available) should be returned. For example, the :class:`~org.hipparchus.linear.ConjugateGradient`
            method computes a sequence of residuals, the norm of which is cheap to compute. However, due to accumulation of
            round-off errors, this residual might differ from the true residual after some iterations. See e.g. A. Greenbaum and Z.
            Strakos, *Predicting the Behavior of Finite Precision Lanzos and Conjugate Gradient Computations*, Technical Report 538,
            Department of Computer Science, New York University, 1991 (available `here
            <http://www.archive.org/details/predictingbehavi00gree>`).
        
            Specified by:
                :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getNormOfResidual`Â in
                classÂ :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`
        
            Returns:
                the norm of the residual, ||r||
        
        
        """
        ...
    def getResidual(self) -> RealVector:
        """
        
            Returns the residual. This is an optional operation, as all iterative linear solvers do not provide cheap estimate of
            the updated residual vector, in which case
        
              - this method should throw a :class:`~org.hipparchus.exception.MathRuntimeException`,
              - :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.providesResidual` returns :code:`false`.
        
        
            The default implementation throws a :class:`~org.hipparchus.exception.MathRuntimeException`. If this method is
            overriden, then :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.providesResidual` should be overriden as well.
            This implementation throws a :class:`~org.hipparchus.exception.MathRuntimeException` if no residual vector :code:`r` was
            provided at construction time.
        
            Overrides:
                :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getResidual`Â in
                classÂ :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`
        
            Returns:
                the updated residual, r
        
        
        """
        ...
    def getRightHandSideVector(self) -> RealVector:
        """
            Returns the current right-hand side of the linear system to be solved. This method should return an unmodifiable view,
            or a deep copy of the actual right-hand side vector, in order not to compromise subsequent iterations of the source
            :class:`~org.hipparchus.linear.IterativeLinearSolver`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getRightHandSideVector`Â in
                classÂ :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`
        
            Returns:
                the right-hand side vector, b
        
        
        """
        ...
    def getSolution(self) -> RealVector:
        """
            Returns the current estimate of the solution to the linear system to be solved. This method should return an
            unmodifiable view, or a deep copy of the actual current solution, in order not to compromise subsequent iterations of
            the source :class:`~org.hipparchus.linear.IterativeLinearSolver`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getSolution`Â in
                classÂ :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`
        
            Returns:
                the solution, x
        
        
        """
        ...
    def providesResidual(self) -> bool:
        """
            Returns :code:`true` if :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getResidual` is supported. The default
            implementation returns :code:`false`. This implementation returns :code:`true` if a non-:code:`null` value was specified
            for the residual vector :code:`r` at construction time.
        
            Overrides:
                :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.providesResidual`Â in
                classÂ :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`
        
            Returns:
                :code:`true` if :code:`r != null`
        
        
        """
        ...

class DefaultRealMatrixChangingVisitor(RealMatrixChangingVisitor):
    """
    public class DefaultRealMatrixChangingVisitor extends Object implements :class:`~org.hipparchus.linear.RealMatrixChangingVisitor`
    
        Default implementation of the :class:`~org.hipparchus.linear.RealMatrixChangingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    """
    def __init__(self): ...
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealMatrixChangingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.start`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealMatrixChangingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> float:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.visit`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealMatrixChangingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
            Returns:
                the new value to be set for the entry
        
        
        """
        ...

class DefaultRealMatrixPreservingVisitor(RealMatrixPreservingVisitor):
    """
    public class DefaultRealMatrixPreservingVisitor extends Object implements :class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`
    
        Default implementation of the :class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` interface.
    
        This class is a convenience to create custom visitors without defining all methods. This class provides default
        implementations that do nothing.
    """
    def __init__(self): ...
    def end(self) -> float:
        """
            End visiting a matrix.
        
            This method is called once after all entries of the matrix have been visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`
        
            Returns:
                the value that the :code:`walkInXxxOrder` must return
        
        
        """
        ...
    def start(self, int: int, int2: int, int3: int, int4: int, int5: int, int6: int) -> None:
        """
            Start visiting a matrix.
        
            This method is called once before any entry of the matrix is visited.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.start`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`
        
            Parameters:
                rows (int): number of rows of the matrix
                columns (int): number of columns of the matrix
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, int: int, int2: int, double: float) -> None:
        """
            Visit one matrix entry.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.visit`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`
        
            Parameters:
                row (int): row index of the entry
                column (int): column index of the entry
                value (double): current value of the entry
        
        
        """
        ...

_FieldMatrix__T = typing.TypeVar('_FieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrix(AnyMatrix, typing.Generic[_FieldMatrix__T]):
    def add(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _FieldMatrix__T) -> None: ...
    def copy(self) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, tArray: typing.List[typing.List[_FieldMatrix__T]]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int], tArray: typing.List[typing.List[_FieldMatrix__T]]) -> None: ...
    def createMatrix(self, int: int, int2: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getColumn(self, int: int) -> typing.List[_FieldMatrix__T]: ...
    def getColumnMatrix(self, int: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getColumnVector(self, int: int) -> FieldVector[_FieldMatrix__T]: ...
    def getData(self) -> typing.List[typing.List[_FieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _FieldMatrix__T: ...
    def getField(self) -> org.hipparchus.Field[_FieldMatrix__T]: ...
    def getRow(self, int: int) -> typing.List[_FieldMatrix__T]: ...
    def getRowMatrix(self, int: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getRowVector(self, int: int) -> FieldVector[_FieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getTrace(self) -> _FieldMatrix__T: ...
    def map(self, function: typing.Union[java.util.function.Function[_FieldMatrix__T, _FieldMatrix__T], typing.Callable[[_FieldMatrix__T], _FieldMatrix__T]]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def mapToSelf(self, function: typing.Union[java.util.function.Function[_FieldMatrix__T, _FieldMatrix__T], typing.Callable[[_FieldMatrix__T], _FieldMatrix__T]]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def multiply(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _FieldMatrix__T) -> None: ...
    def multiplyTransposed(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def operate(self, tArray: typing.List[_FieldMatrix__T]) -> typing.List[_FieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_FieldMatrix__T]) -> FieldVector[_FieldMatrix__T]: ...
    def power(self, int: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.List[_FieldMatrix__T]) -> typing.List[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_FieldMatrix__T]) -> FieldVector[_FieldMatrix__T]: ...
    def scalarAdd(self, t: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def scalarMultiply(self, t: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def setColumn(self, int: int, tArray: typing.List[_FieldMatrix__T]) -> None: ...
    def setColumnMatrix(self, int: int, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> None: ...
    def setColumnVector(self, int: int, fieldVector: FieldVector[_FieldMatrix__T]) -> None: ...
    def setEntry(self, int: int, int2: int, t: _FieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.List[_FieldMatrix__T]) -> None: ...
    def setRowMatrix(self, int: int, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> None: ...
    def setRowVector(self, int: int, fieldVector: FieldVector[_FieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.List[typing.List[_FieldMatrix__T]], int: int, int2: int) -> None: ...
    def subtract(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def transpose(self) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def transposeMultiply(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T]) -> _FieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_FieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _FieldMatrix__T: ...

class JacobiPreconditioner(RealLinearOperator):
    """
    public class JacobiPreconditioner extends Object implements :class:`~org.hipparchus.linear.RealLinearOperator`
    
        This class implements the standard Jacobi (diagonal) preconditioner. For a matrix A :sub:`ij` , this preconditioner is M
        = diag(1 / A :sub:`11` , 1 / A :sub:`22` , â€¦).
    """
    def __init__(self, doubleArray: typing.List[float], boolean: bool): ...
    @staticmethod
    def create(realLinearOperator: RealLinearOperator) -> 'JacobiPreconditioner': ...
    def getColumnDimension(self) -> int:
        """
            Returns the dimension of the domain of this operator.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getColumnDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Returns:
                the number of columns of the underlying matrix
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
            Returns the dimension of the codomain of this operator.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getRowDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Returns:
                the number of rows of the underlying matrix
        
        
        """
        ...
    def operate(self, realVector: RealVector) -> RealVector:
        """
            Returns the result of multiplying :code:`this` by the vector :code:`x`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.operate`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Parameters:
                x (:class:`~org.hipparchus.linear.RealVector`): the vector to operate on
        
            Returns:
                the product of :code:`this` instance with :code:`x`
        
        
        """
        ...
    def sqrt(self) -> RealLinearOperator:
        """
            Returns the square root of :code:`this` diagonal operator. More precisely, this method returns P = diag(1 / âˆšA
            :sub:`11` , 1 / âˆšA :sub:`22` , â€¦).
        
            Returns:
                the square root of :code:`this` preconditioner
        
        
        """
        ...

class LUDecomposer(MatrixDecomposer):
    """
    public class LUDecomposer extends Object implements :class:`~org.hipparchus.linear.MatrixDecomposer`
    
        Matrix decomposer using LU-decomposition.
    
        Since:
            1.3
    """
    def __init__(self, double: float): ...
    def decompose(self, realMatrix: 'RealMatrix') -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Specified by:
                :meth:`~org.hipparchus.linear.MatrixDecomposer.decompose` in interface :class:`~org.hipparchus.linear.MatrixDecomposer`
        
            Parameters:
                a (:class:`~org.hipparchus.linear.RealMatrix`): coefficient matrix A to decompose
        
            Returns:
                a solver
        
        
        """
        ...

class OrderedComplexEigenDecomposition(ComplexEigenDecomposition):
    """
    public class OrderedComplexEigenDecomposition extends :class:`~org.hipparchus.linear.ComplexEigenDecomposition`
    
        Given a matrix A, it computes a complex eigen decomposition A = VDV^{T}. It ensures that eigen values in the diagonal of
        D are in ascending order.
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float, double3: float): ...
    def getVT(self) -> FieldMatrix[org.hipparchus.complex.Complex]: ...

class OrderedEigenDecomposition(EigenDecomposition):
    """
    public class OrderedEigenDecomposition extends :class:`~org.hipparchus.linear.EigenDecomposition`
    
        Given a matrix A, it computes an eigen decomposition A = VDV^{T}. It also ensures that eigen values in the diagonal of D
        are in ascending order.
    """
    def __init__(self, realMatrix: 'RealMatrix'): ...
    def getVT(self) -> 'RealMatrix':
        """
            Gets the transpose of the matrix V of the decomposition. V is an orthogonal matrix, i.e. its transpose is also its
            inverse. The columns of V are the eigenvectors of the original matrix. No assumption is made about the orientation of
            the system axes formed by the columns of V (e.g. in a 3-dimension space, V can form a left- or right-handed system).
        
            Overrides:
                :meth:`~org.hipparchus.linear.EigenDecomposition.getVT` in class :class:`~org.hipparchus.linear.EigenDecomposition`
        
            Returns:
                the transpose of the V matrix.
        
        
        """
        ...

class PreconditionedIterativeLinearSolver(IterativeLinearSolver):
    """
    public abstract class PreconditionedIterativeLinearSolver extends :class:`~org.hipparchus.linear.IterativeLinearSolver`
    
    
        This abstract class defines preconditioned iterative solvers. When A is ill-conditioned, instead of solving system A Â·
        x = b directly, it is preferable to solve either
        (M · A) · x = M · b
        (left preconditioning), or
        (A · M) · y = b,     followed by M · y = x
        (right preconditioning), where M approximates in some way A :sup:`-1` , while matrix-vector products of the type M Â· y
        remain comparatively easy to compute. In this library, M (not M :sup:`-1` !) is called the *preconditionner*.
    
        Concrete implementations of this abstract class must be provided with the preconditioner M, as a
        :class:`~org.hipparchus.linear.RealLinearOperator`.
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager): ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...

class QRDecomposer(MatrixDecomposer):
    """
    public class QRDecomposer extends Object implements :class:`~org.hipparchus.linear.MatrixDecomposer`
    
        Matrix decomposer using QR-decomposition.
    
        Since:
            1.3
    """
    def __init__(self, double: float): ...
    def decompose(self, realMatrix: 'RealMatrix') -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Specified by:
                :meth:`~org.hipparchus.linear.MatrixDecomposer.decompose` in interface :class:`~org.hipparchus.linear.MatrixDecomposer`
        
            Parameters:
                a (:class:`~org.hipparchus.linear.RealMatrix`): coefficient matrix A to decompose
        
            Returns:
                a solver
        
        
        """
        ...

class RRQRDecomposition(QRDecomposition):
    """
    public class RRQRDecomposition extends :class:`~org.hipparchus.linear.QRDecomposition`
    
        Calculates the rank-revealing QR-decomposition of a matrix, with column pivoting.
    
        The rank-revealing QR-decomposition of a matrix A consists of three matrices Q, R and P such that AP=QR. Q is orthogonal
        (Q :sup:`T` Q = I), and R is upper triangular. If A is mÃ—n, Q is mÃ—m and R is mÃ—n and P is nÃ—n.
    
        QR decomposition with column pivoting produces a rank-revealing QR decomposition and the
        :meth:`~org.hipparchus.linear.RRQRDecomposition.getRank` method may be used to return the rank of the input matrix A.
    
        This class compute the decomposition using Householder reflectors.
    
        For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows,
        which is much more cache-efficient in Java.
    
        This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library,
        with the following changes:
    
          - a :meth:`~org.hipparchus.linear.QRDecomposition.getQT` method has been added,
          - the :code:`solve` and :code:`isFullRank` methods have been replaced by a
            :meth:`~org.hipparchus.linear.RRQRDecomposition.getSolver` method and the equivalent methods provided by the returned
            :class:`~org.hipparchus.linear.DecompositionSolver`.
    
    
        Also see:
            `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`, `Wikipedia
            <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getP(self) -> 'RealMatrix':
        """
            Returns the pivot matrix, P, used in the QR Decomposition of matrix A such that AP = QR. If no pivoting is used in this
            decomposition then P is equal to the identity matrix.
        
            Returns:
                a permutation matrix.
        
        
        """
        ...
    def getRank(self, double: float) -> int:
        """
            Return the effective numerical matrix rank.
        
            The effective numerical rank is the number of non-negligible singular values.
        
            This implementation looks at Frobenius norms of the sequence of bottom right submatrices. When a large fall in norm is
            seen, the rank is returned. The drop is computed as:
        
            .. code-block: java
            
               (thisNorm/lastNorm) * rNorm < dropThreshold
             
        
            where thisNorm is the Frobenius norm of the current submatrix, lastNorm is the Frobenius norm of the previous submatrix,
            rNorm is is the Frobenius norm of the complete matrix
        
            Parameters:
                dropThreshold (double): threshold triggering rank computation
        
            Returns:
                effective numerical matrix rank
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Least Square sense means a solver can be computed for an overdetermined system, (i.e. a system with more equations than
            unknowns, which corresponds to a tall A matrix with more rows than columns). In any case, if the matrix is singular
            within the tolerance set at :meth:`~org.hipparchus.linear.RRQRDecomposition.RRQRDecomposition`, an error will be
            triggered when the :meth:`~org.hipparchus.linear.DecompositionSolver.solve` method will be called.
        
            Overrides:
                :meth:`~org.hipparchus.linear.QRDecomposition.getSolver` in class :class:`~org.hipparchus.linear.QRDecomposition`
        
            Returns:
                a solver
        
        
        """
        ...

class RealMatrix(AnyMatrix):
    """
    public interface RealMatrix extends :class:`~org.hipparchus.linear.AnyMatrix`
    
        Interface defining a real-valued matrix with basic algebraic operations.
    
        Matrix element indexing is 0-based -- e.g., :code:`getEntry(0, 0)` returns the element in the first row, first column of
        the matrix.
    """
    def add(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    def copy(self) -> 'RealMatrix':
        """
            Returns a (deep) copy of this.
        
            Returns:
                matrix copy
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.List[typing.List[float]]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int], doubleArray: typing.List[typing.List[float]]) -> None: ...
    def createMatrix(self, int: int, int2: int) -> 'RealMatrix': ...
    def getColumn(self, int: int) -> typing.List[float]: ...
    def getColumnMatrix(self, int: int) -> 'RealMatrix': ...
    def getColumnVector(self, int: int) -> RealVector: ...
    def getData(self) -> typing.List[typing.List[float]]:
        """
            Returns matrix entries as a two-dimensional array.
        
            Returns:
                2-dimensional array of entries
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float: ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Returns:
                norm
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
            Returns the ` maximum absolute column sum norm <http://mathworld.wolfram.com/MaximumAbsoluteColumnSumNorm.html>` (L
            :sub:`1` ) of the matrix.
        
            Returns:
                norm
        
        
        """
        ...
    def getNormInfty(self) -> float:
        """
            Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` (L :sub:`âˆž`
            ) of the matrix.
        
            Returns:
                norm
        
        
        """
        ...
    def getRow(self, int: int) -> typing.List[float]: ...
    def getRowMatrix(self, int: int) -> 'RealMatrix': ...
    def getRowVector(self, int: int) -> RealVector: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'RealMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> 'RealMatrix': ...
    def getTrace(self) -> float: ...
    def map(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> 'RealMatrix':
        """
            Acts as if implemented as:
        
            .. code-block: java
            
              return copy().mapToSelf(function);
             
            Returns a new matrix. Does not change instance data.
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a new matrix.
        
            Since:
                1.7
        
        
        """
        ...
    def mapToSelf(self, univariateFunction: org.hipparchus.analysis.UnivariateFunction) -> 'RealMatrix':
        """
            Replace each entry by the result of applying the function to it.
        
            Parameters:
                function (:class:`~org.hipparchus.analysis.UnivariateFunction`): Function to apply to each entry.
        
            Returns:
                a reference to this matrix.
        
            Since:
                1.7
        
        
        """
        ...
    def multiply(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    def multiplyTransposed(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    def operate(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, int: int) -> 'RealMatrix': ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, double: float) -> 'RealMatrix':
        """
            Returns the result of adding :code:`d` to each entry of :code:`this`.
        
            Parameters:
                d (double): value to be added to each entry
        
            Returns:
                :code:`d + this`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> 'RealMatrix':
        """
            Returns the result of multiplying each entry of :code:`this` by :code:`d`.
        
            Parameters:
                d (double): value to multiply all entries by
        
            Returns:
                :code:`d * this`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.List[float]) -> None: ...
    def setColumnMatrix(self, int: int, realMatrix: 'RealMatrix') -> None: ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    def setRow(self, int: int, doubleArray: typing.List[float]) -> None: ...
    def setRowMatrix(self, int: int, realMatrix: 'RealMatrix') -> None: ...
    def setRowVector(self, int: int, realVector: RealVector) -> None: ...
    def setSubMatrix(self, doubleArray: typing.List[typing.List[float]], int: int, int2: int) -> None: ...
    def subtract(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    def transpose(self) -> 'RealMatrix':
        """
            Returns the transpose of this matrix.
        
            Returns:
                transpose matrix
        
        
        """
        ...
    def transposeMultiply(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        double walkInColumnOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        double walkInColumnOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if :code:`endRow < startRow` or :code:`endColumn < startColumn`.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class RiccatiEquationSolverImpl(RiccatiEquationSolver):
    """
    public class RiccatiEquationSolverImpl extends Object implements :class:`~org.hipparchus.linear.RiccatiEquationSolver`
    
        This solver computes the solution using the following approach: 1. Compute the Hamiltonian matrix 2. Extract its complex
        eigen vectors (not the best solution, a better solution would be ordered Schur transformation) 3. Approximate the
        initial solution given by 2 using the Kleinman algorithm (an iterative method)
    """
    def __init__(self, realMatrix: RealMatrix, realMatrix2: RealMatrix, realMatrix3: RealMatrix, realMatrix4: RealMatrix): ...
    def getK(self) -> RealMatrix:
        """
            {inheritDoc}
        
            Specified by:
                :meth:`~org.hipparchus.linear.RiccatiEquationSolver.getK`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RiccatiEquationSolver`
        
            Returns:
                the linear controller k
        
        
        """
        ...
    def getP(self) -> RealMatrix:
        """
            {inheritDoc}
        
            Specified by:
                :meth:`~org.hipparchus.linear.RiccatiEquationSolver.getP`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RiccatiEquationSolver`
        
            Returns:
                the p
        
        
        """
        ...

class SingularValueDecomposer(MatrixDecomposer):
    """
    public class SingularValueDecomposer extends Object implements :class:`~org.hipparchus.linear.MatrixDecomposer`
    
        Matrix decomposer using Singular Value Decomposition.
    
        Since:
            1.3
    """
    def __init__(self): ...
    def decompose(self, realMatrix: RealMatrix) -> DecompositionSolver:
        """
            Get a solver for finding the A × X = B solution in least square sense.
        
            Specified by:
                :meth:`~org.hipparchus.linear.MatrixDecomposer.decompose` in interface :class:`~org.hipparchus.linear.MatrixDecomposer`
        
            Parameters:
                a (:class:`~org.hipparchus.linear.RealMatrix`): coefficient matrix A to decompose
        
            Returns:
                a solver
        
        
        """
        ...

_SparseFieldVector__T = typing.TypeVar('_SparseFieldVector__T', bound=org.hipparchus.FieldElement)  # <T>
class SparseFieldVector(FieldVector[_SparseFieldVector__T], java.io.Serializable, typing.Generic[_SparseFieldVector__T]):
    """
    public class SparseFieldVector<T extends :class:`~org.hipparchus.FieldElement`<T>> extends Object implements :class:`~org.hipparchus.linear.FieldVector`<T>, Serializable
    
        This class implements the :class:`~org.hipparchus.linear.FieldVector` interface with a
        :class:`~org.hipparchus.util.OpenIntToFieldHashMap` backing store.
    
        Caveat: This implementation assumes that, for any :code:`x`, the equality :code:`x * 0d == 0d` holds. But it is is not
        true for :code:`NaN`. Moreover, zero entries will lose their sign. Some operations (that involve :code:`NaN` and/or
        infinities) may thus give incorrect results.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T], tArray: typing.List[_SparseFieldVector__T]): ...
    @typing.overload
    def __init__(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]): ...
    @typing.overload
    def add(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def add(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def append(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def append(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def append(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    def copy(self) -> FieldVector[_SparseFieldVector__T]: ...
    def dotProduct(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> _SparseFieldVector__T: ...
    def ebeDivide(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    def ebeMultiply(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.getDimension` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Returns:
                size
        
        
        """
        ...
    def getEntry(self, int: int) -> _SparseFieldVector__T: ...
    def getField(self) -> org.hipparchus.Field[_SparseFieldVector__T]: ...
    def getSubVector(self, int: int, int2: int) -> FieldVector[_SparseFieldVector__T]: ...
    def hashCode(self) -> int:
        """
        
            Overrides:
                 in class 
        
        
        """
        ...
    def mapAdd(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapAddToSelf(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapDivide(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapDivideToSelf(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapInv(self) -> FieldVector[_SparseFieldVector__T]: ...
    def mapInvToSelf(self) -> FieldVector[_SparseFieldVector__T]: ...
    def mapMultiply(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapMultiplyToSelf(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapSubtract(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    def mapSubtractToSelf(self, t: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldMatrix[_SparseFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]) -> FieldMatrix[_SparseFieldVector__T]: ...
    def projection(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    def set(self, t: _SparseFieldVector__T) -> None:
        """
            Set all elements to a single value.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.set` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Parameters:
                value (:class:`~org.hipparchus.linear.SparseFieldVector`): single value to set for all elements
        
            Raises:
                :class:`~org.hipparchus.exception.NullArgumentException`: if value is null
        
        
        """
        ...
    def setEntry(self, int: int, t: _SparseFieldVector__T) -> None: ...
    def setSubVector(self, int: int, fieldVector: FieldVector[_SparseFieldVector__T]) -> None: ...
    @typing.overload
    def subtract(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def subtract(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]) -> 'SparseFieldVector'[_SparseFieldVector__T]: ...
    def toArray(self) -> typing.List[_SparseFieldVector__T]:
        """
            Convert the vector to a T array.
        
            The array is independent from vector data, it's elements are copied.
        
            Specified by:
                :meth:`~org.hipparchus.linear.FieldVector.toArray` in interface :class:`~org.hipparchus.linear.FieldVector`
        
            Returns:
                array containing a copy of vector elements
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_SparseFieldVector__T]) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_SparseFieldVector__T], int: int, int2: int) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_SparseFieldVector__T]) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInDefaultOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_SparseFieldVector__T], int: int, int2: int) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_SparseFieldVector__T]) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorChangingVisitor: FieldVectorChangingVisitor[_SparseFieldVector__T], int: int, int2: int) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_SparseFieldVector__T]) -> _SparseFieldVector__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldVectorPreservingVisitor: FieldVectorPreservingVisitor[_SparseFieldVector__T], int: int, int2: int) -> _SparseFieldVector__T: ...

class SparseRealVector(RealVector):
    """
    public abstract class SparseRealVector extends :class:`~org.hipparchus.linear.RealVector`
    
        Marker class for RealVectors that require sparse backing storage
    
        Caveat: Implementation are allowed to assume that, for any :code:`x`, the equality :code:`x * 0d == 0d` holds. But it is
        is not true for :code:`NaN`. Moreover, zero entries will lose their sign. Some operations (that involve :code:`NaN`
        and/or infinities) may thus give incorrect results, like multiplications, divisions or functions mapping.
    """
    def __init__(self): ...

_AbstractFieldMatrix__T = typing.TypeVar('_AbstractFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class AbstractFieldMatrix(FieldMatrix[_AbstractFieldMatrix__T], typing.Generic[_AbstractFieldMatrix__T]):
    def add(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _AbstractFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, tArray: typing.List[typing.List[_AbstractFieldMatrix__T]]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int], tArray: typing.List[typing.List[_AbstractFieldMatrix__T]]) -> None: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def equals(self, object: typing.Any) -> bool: ...
    def getColumn(self, int: int) -> typing.List[_AbstractFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getColumnMatrix(self, int: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getColumnVector(self, int: int) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def getData(self) -> typing.List[typing.List[_AbstractFieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _AbstractFieldMatrix__T: ...
    def getField(self) -> org.hipparchus.Field[_AbstractFieldMatrix__T]: ...
    def getRow(self, int: int) -> typing.List[_AbstractFieldMatrix__T]: ...
    def getRowDimension(self) -> int: ...
    def getRowMatrix(self, int: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getRowVector(self, int: int) -> FieldVector[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getTrace(self) -> _AbstractFieldMatrix__T: ...
    def hashCode(self) -> int: ...
    def isSquare(self) -> bool: ...
    def multiply(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _AbstractFieldMatrix__T) -> None: ...
    @typing.overload
    def operate(self, tArray: typing.List[_AbstractFieldMatrix__T]) -> typing.List[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def power(self, int: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.List[_AbstractFieldMatrix__T]) -> typing.List[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def scalarAdd(self, t: _AbstractFieldMatrix__T) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def scalarMultiply(self, t: _AbstractFieldMatrix__T) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def setColumn(self, int: int, tArray: typing.List[_AbstractFieldMatrix__T]) -> None: ...
    def setColumnMatrix(self, int: int, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> None: ...
    def setColumnVector(self, int: int, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> None: ...
    def setEntry(self, int: int, int2: int, t: _AbstractFieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.List[_AbstractFieldMatrix__T]) -> None: ...
    def setRowMatrix(self, int: int, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> None: ...
    def setRowVector(self, int: int, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.List[typing.List[_AbstractFieldMatrix__T]], int: int, int2: int) -> None: ...
    def subtract(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def toString(self) -> str: ...
    def transpose(self) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T]) -> _AbstractFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_AbstractFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _AbstractFieldMatrix__T: ...

class AbstractRealMatrix(RealMatrix, RealLinearOperator):
    """
    public abstract class AbstractRealMatrix extends Object implements :class:`~org.hipparchus.linear.RealMatrix`, :class:`~org.hipparchus.linear.RealLinearOperator`
    
        Basic implementation of RealMatrix methods regardless of the underlying storage.
    
        All the methods implemented here use :meth:`~org.hipparchus.linear.AbstractRealMatrix.getEntry` to access matrix
        elements. Derived class can provide faster implementations.
    """
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    def copy(self) -> RealMatrix:
        """
            Returns a (deep) copy of this.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.copy` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Returns:
                matrix copy
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.List[typing.List[float]]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int], doubleArray: typing.List[typing.List[float]]) -> None: ...
    def createMatrix(self, int: int, int2: int) -> RealMatrix: ...
    def equals(self, object: typing.Any) -> bool:
        """
            Returns true iff :code:`object` is a :code:`RealMatrix` instance with the same dimensions as this and all corresponding
            matrix entries are equal.
        
            Overrides:
                 in class 
        
            Parameters:
                object (Object): the object to test equality against.
        
            Returns:
                true if object equals this
        
        
        """
        ...
    def getColumn(self, int: int) -> typing.List[float]: ...
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getColumnDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getColumnDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Returns:
                the number of columns.
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> RealMatrix: ...
    def getColumnVector(self, int: int) -> RealVector: ...
    def getData(self) -> typing.List[typing.List[float]]:
        """
            Returns matrix entries as a two-dimensional array.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getData` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Returns:
                2-dimensional array of entries
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float: ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getFrobeniusNorm` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Returns:
                norm
        
        
        """
        ...
    def getRow(self, int: int) -> typing.List[float]: ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getRowDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getRowDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Returns:
                the number of rows.
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> RealMatrix: ...
    def getRowVector(self, int: int) -> RealVector: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> RealMatrix: ...
    def getTrace(self) -> float: ...
    def hashCode(self) -> int:
        """
            Computes a hashcode for the matrix.
        
            Overrides:
                 in class 
        
            Returns:
                hashcode for matrix
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
            Is this a square matrix?
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.isSquare` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Returns:
                true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def operate(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, int: int) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, double: float) -> RealMatrix:
        """
            Returns the result of adding :code:`d` to each entry of :code:`this`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.scalarAdd` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                d (double): value to be added to each entry
        
            Returns:
                :code:`d + this`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> RealMatrix:
        """
            Returns the result of multiplying each entry of :code:`this` by :code:`d`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.scalarMultiply` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                d (double): value to multiply all entries by
        
            Returns:
                :code:`d * this`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.List[float]) -> None: ...
    def setColumnMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    def setRow(self, int: int, doubleArray: typing.List[float]) -> None: ...
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setRowVector(self, int: int, realVector: RealVector) -> None: ...
    def setSubMatrix(self, doubleArray: typing.List[typing.List[float]], int: int, int2: int) -> None: ...
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def toString(self) -> str:
        """
            Get a string representation for this matrix.
        
            Overrides:
                 in class 
        
            Returns:
                a string representation for this matrix
        
        
        """
        ...
    def transpose(self) -> RealMatrix:
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.transpose` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Returns:
                transpose matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInColumnOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInColumnOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class ConjugateGradient(PreconditionedIterativeLinearSolver):
    """
    public class ConjugateGradient extends :class:`~org.hipparchus.linear.PreconditionedIterativeLinearSolver`
    
    
        This is an implementation of the conjugate gradient method for :class:`~org.hipparchus.linear.RealLinearOperator`. It
        follows closely the template by :meth:`~org.hipparchus.linear.ConjugateGradient.BARR1994` (figure 2.5). The linear
        system at hand is A Â· x = b, and the residual is r = b - A Â· x.
    
        :class:`~org.hipparchus.linear`
    -------------------------------
    
    
        A default stopping criterion is implemented. The iterations stop when || r || â‰¤ Î´ || b ||, where b is the right-hand
        side vector, r the current estimate of the residual, and Î´ a user-specified tolerance. It should be noted that r is the
        so-called *updated* residual, which might differ from the true residual due to rounding-off errors (see e.g.
        :meth:`~org.hipparchus.linear.ConjugateGradient.STRA2002`).
    
        Iteration count
    ---------------
    
    
        In the present context, an iteration should be understood as one evaluation of the matrix-vector product A Â· x. The
        initialization phase therefore counts as one iteration.
    
        :class:`~org.hipparchus.linear`
    -------------------------------
    
    
        Besides standard :class:`~org.hipparchus.exception.MathIllegalArgumentException`, this class might throw
        :class:`~org.hipparchus.exception.MathIllegalArgumentException` if the linear operator or the preconditioner are not
        positive definite.
    
          - key :code:`"operator"` points to the offending linear operator, say L,
          - key :code:`"vector"` points to the offending vector, say x, such that x :sup:`T` · L · x < 0.
    
    
        References
    ----------
    
    
        :class:`~org.hipparchus.linear`
          R. Barrett, M. Berry, T. F. Chan, J. Demmel, J. M. Donato, J. Dongarra, V. Eijkhout, R. Pozo, C. Romine and H. Van der
            Vorst, `*Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods*
            <http://www.netlib.org/linalg/html_templates/Templates.html>`, SIAM
    
        :class:`~org.hipparchus.linear`
    """
    OPERATOR: typing.ClassVar[str] = ...
    """
    public static final String OPERATOR
    
        Key for the :meth:`~org.hipparchus.linear.ConjugateGradient.context`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    VECTOR: typing.ClassVar[str] = ...
    """
    public static final String VECTOR
    
        Key for the :meth:`~org.hipparchus.linear.ConjugateGradient.context`.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, int: int, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager, double: float, boolean: bool): ...
    def shouldCheck(self) -> bool:
        """
            Returns :code:`true` if positive-definiteness should be checked for both matrix and preconditioner.
        
            Returns:
                :code:`true` if the tests are to be performed
        
            Since:
                1.4
        
        
        """
        ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...

class OpenMapRealVector(SparseRealVector, java.io.Serializable):
    """
    public class OpenMapRealVector extends :class:`~org.hipparchus.linear.SparseRealVector` implements Serializable
    
        This class implements the :class:`~org.hipparchus.linear.RealVector` interface with a
        :class:`~org.hipparchus.util.OpenIntToDoubleHashMap` backing store.
    
        Caveat: This implementation assumes that, for any :code:`x`, the equality :code:`x * 0d == 0d` holds. But it is is not
        true for :code:`NaN`. Moreover, zero entries will lose their sign. Some operations (that involve :code:`NaN` and/or
        infinities) may thus give incorrect results, like multiplications, divisions or functions mapping.
    
        Also see:
            :meth:`~serialized`
    """
    DEFAULT_ZERO_TOLERANCE: typing.ClassVar[float] = ...
    """
    public static final double DEFAULT_ZERO_TOLERANCE
    
        Default Tolerance for having a value considered zero.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], double2: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], double2: float): ...
    @typing.overload
    def __init__(self, openMapRealVector: 'OpenMapRealVector'): ...
    @typing.overload
    def __init__(self, realVector: RealVector): ...
    @typing.overload
    def add(self, openMapRealVector: 'OpenMapRealVector') -> 'OpenMapRealVector': ...
    @typing.overload
    def add(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def append(self, double: float) -> 'OpenMapRealVector':
        """
            Optimized method to append a OpenMapRealVector.
        
            Parameters:
                v (:class:`~org.hipparchus.linear.OpenMapRealVector`): vector to append
        
            Returns:
                The result of appending :code:`v` to self
        
            Construct a new vector by appending a vector to this vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.append` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                v (:class:`~org.hipparchus.linear.RealVector`): vector to append to this one.
        
            Returns:
                a new vector.
        
            Construct a new vector by appending a double to this vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.append` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): double to append.
        
            Returns:
                a new vector.
        
        
        """
        ...
    @typing.overload
    def append(self, openMapRealVector: 'OpenMapRealVector') -> 'OpenMapRealVector': ...
    @typing.overload
    def append(self, realVector: RealVector) -> 'OpenMapRealVector': ...
    def copy(self) -> 'OpenMapRealVector':
        """
            Returns a (deep) copy of this vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.copy` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                a vector copy.
        
        
        """
        ...
    def ebeDivide(self, realVector: RealVector) -> 'OpenMapRealVector': ...
    def ebeMultiply(self, realVector: RealVector) -> 'OpenMapRealVector': ...
    def equals(self, object: typing.Any) -> bool:
        """
        
            Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are
            :code:`NaN`, the two real vectors are considered to be equal. :code:`NaN` coordinates are considered to affect globally
            the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to
            :code:`NaN`, the real vector is equal to a vector with all :code:`NaN` coordinates.
        
            This method *must* be overriden by concrete subclasses of :class:`~org.hipparchus.linear.RealVector` (the current
            implementation throws an exception).
            Implementation Note: This performs an exact comparison, and as a result it is possible for :code:`a.subtract(b`} to be
            the zero vector, while :code:`a.equals(b) == false`.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.equals` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                obj (Object): Object to test for equality.
        
            Returns:
                :code:`true` if two vector objects are equal, :code:`false` if :code:`other` is null, not an instance of
                :code:`RealVector`, or not equal to this :code:`RealVector` instance.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
            Returns the size of the vector.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.getDimension` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                the size of this vector.
        
        
        """
        ...
    @typing.overload
    def getDistance(self, openMapRealVector: 'OpenMapRealVector') -> float: ...
    @typing.overload
    def getDistance(self, realVector: RealVector) -> float: ...
    def getEntry(self, int: int) -> float: ...
    @typing.overload
    def getL1Distance(self, openMapRealVector: 'OpenMapRealVector') -> float: ...
    @typing.overload
    def getL1Distance(self, realVector: RealVector) -> float: ...
    def getLInfDistance(self, realVector: RealVector) -> float: ...
    def getSparsity(self) -> float:
        """
        
            Returns:
                the percentage of none zero elements as a decimal percent.
        
        
        """
        ...
    def getSubVector(self, int: int, int2: int) -> 'OpenMapRealVector': ...
    def hashCode(self) -> int:
        """
            . This method *must* be overriden by concrete subclasses of :class:`~org.hipparchus.linear.RealVector` (current
            implementation throws an exception). Implementation Note: This works on exact values, and as a result it is possible for
            :code:`a.subtract(b)` to be the zero vector, while :code:`a.hashCode() != b.hashCode()`.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.hashCode` in class :class:`~org.hipparchus.linear.RealVector`
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
            Check whether any coordinate of this vector is infinite and none are :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.isInfinite` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                :code:`true` if any coordinate of this vector is infinite and none are :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
            Check whether any coordinate of this vector is :code:`NaN`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealVector.isNaN` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                :code:`true` if any coordinate of this vector is :code:`NaN`, :code:`false` otherwise.
        
        
        """
        ...
    def mapAdd(self, double: float) -> 'OpenMapRealVector':
        """
            Add a value to each entry. Returns a new vector. Does not change instance data.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.mapAdd` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this` + :code:`d`.
        
        
        """
        ...
    def mapAddToSelf(self, double: float) -> 'OpenMapRealVector':
        """
            Add a value to each entry. The instance is changed in-place.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.mapAddToSelf` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                d (double): Value to be added to each entry.
        
            Returns:
                :code:`this`.
        
        
        """
        ...
    def set(self, double: float) -> None:
        """
            Set all elements to a single value.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.set` in class :class:`~org.hipparchus.linear.RealVector`
        
            Parameters:
                value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, int: int, double: float) -> None: ...
    def setSubVector(self, int: int, realVector: RealVector) -> None: ...
    def sparseIterator(self) -> java.util.Iterator[RealVector.Entry]: ...
    @typing.overload
    def subtract(self, openMapRealVector: 'OpenMapRealVector') -> 'OpenMapRealVector': ...
    @typing.overload
    def subtract(self, realVector: RealVector) -> RealVector: ...
    def toArray(self) -> typing.List[float]:
        """
            Convert the vector to an array of :code:`double`s. The array is independent from this vector data: the elements are
            copied.
        
            Overrides:
                :meth:`~org.hipparchus.linear.RealVector.toArray` in class :class:`~org.hipparchus.linear.RealVector`
        
            Returns:
                an array containing a copy of the vector elements.
        
        
        """
        ...
    def unitVector(self) -> 'OpenMapRealVector': ...
    def unitize(self) -> None: ...

class SparseRealMatrix(RealMatrix):
    """
    public interface SparseRealMatrix extends :class:`~org.hipparchus.linear.RealMatrix`
    
        Marker interface for :class:`~org.hipparchus.linear.RealMatrix` implementations that require sparse backing storage
    
        Caveat: Implementation are allowed to assume that, for any :code:`x`, the equality :code:`x * 0d == 0d` holds. But it is
        is not true for :code:`NaN`. Moreover, zero entries will lose their sign. Some operations (that involve :code:`NaN`
        and/or infinities) may thus give incorrect results.
    """
    ...

class SymmLQ(PreconditionedIterativeLinearSolver):
    """
    public class SymmLQ extends :class:`~org.hipparchus.linear.PreconditionedIterativeLinearSolver`
    
    
        Implementation of the SYMMLQ iterative linear solver proposed by :meth:`~org.hipparchus.linear.SymmLQ.PAIG1975`. This
        implementation is largely based on the FORTRAN code by Pr. Michael A. Saunders, available `here
        <http://www.stanford.edu/group/SOL/software/symmlq/f77/>`.
    
        SYMMLQ is designed to solve the system of linear equations A Â· x = b where A is an n Ã— n self-adjoint linear operator
        (defined as a :class:`~org.hipparchus.linear.RealLinearOperator`), and b is a given vector. The operator A is not
        required to be positive definite. If A is known to be definite, the method of conjugate gradients might be preferred,
        since it will require about the same number of iterations as SYMMLQ but slightly less work per iteration.
    
        SYMMLQ is designed to solve the system (A - shift Â· I) Â· x = b, where shift is a specified scalar value. If shift and
        b are suitably chosen, the computed vector x may approximate an (unnormalized) eigenvector of A, as in the methods of
        inverse iteration and/or Rayleigh-quotient iteration. Again, the linear operator (A - shift Â· I) need not be positive
        definite (but *must* be self-adjoint). The work per iteration is very slightly less if shift = 0.
    
        Preconditioning
    ---------------
    
    
        Preconditioning may reduce the number of iterations required. The solver may be provided with a positive definite
        preconditioner M = P :sup:`T` Â· P that is known to approximate (A - shift Â· I) :sup:`-1` in some sense, where
        matrix-vector products of the form M Â· y = x can be computed efficiently. Then SYMMLQ will implicitly solve the system
        of equations P Â· (A - shift Â· I) Â· P :sup:`T` Â· x :sub:`hat` = P Â· b, i.e. A :sub:`hat` Â· x :sub:`hat` = b
        :sub:`hat` , where A :sub:`hat` = P Â· (A - shift Â· I) Â· P :sup:`T` , b :sub:`hat` = P Â· b, and return the solution x
        = P :sup:`T` Â· x :sub:`hat` . The associated residual is r :sub:`hat` = b :sub:`hat` - A :sub:`hat` Â· x :sub:`hat` = P
        Â· [b - (A - shift Â· I) Â· x] = P Â· r.
    
        In the case of preconditioning, the :class:`~org.hipparchus.linear.IterativeLinearSolverEvent`s that this solver fires
        are such that :meth:`~org.hipparchus.linear.IterativeLinearSolverEvent.getNormOfResidual` returns the norm of the
        *preconditioned*, updated residual, ||P Â· r||, not the norm of the *true* residual ||r||.
    
        :class:`~org.hipparchus.linear`
    -------------------------------
    
    
        A default stopping criterion is implemented. The iterations stop when || rhat || â‰¤ Î´ || Ahat || || xhat ||, where
        xhat is the current estimate of the solution of the transformed system, rhat the current estimate of the corresponding
        residual, and Î´ a user-specified tolerance.
    
        Iteration count
    ---------------
    
    
        In the present context, an iteration should be understood as one evaluation of the matrix-vector product A Â· x. The
        initialization phase therefore counts as one iteration. If the user requires checks on the symmetry of A, this entails
        one further matrix-vector product in the initial phase. This further product is *not* accounted for in the iteration
        count. In other words, the number of iterations required to reach convergence will be identical, whether checks have
        been required or not.
    
        The present definition of the iteration count differs from that adopted in the original FOTRAN code, where the
        initialization phase was *not* taken into account.
    
        :class:`~org.hipparchus.linear`
    -------------------------------
    
    
        The :code:`x` parameter in
    
          - :meth:`~org.hipparchus.linear.SymmLQ.solve`,
          - :meth:`~org.hipparchus.linear.SymmLQ.solve`},
          - :meth:`~org.hipparchus.linear.SymmLQ.solveInPlace`,
          - :meth:`~org.hipparchus.linear.SymmLQ.solveInPlace`,
          - :meth:`~org.hipparchus.linear.SymmLQ.solveInPlace`,
    
        should not be considered as an initial guess, as it is set to zero in the initial phase. If x :sub:`0` is known to be a
        good approximation to x, one should compute r :sub:`0` = b - A Â· x, solve A Â· dx = r0, and set x = x :sub:`0` + dx.
    
        :class:`~org.hipparchus.linear`
    -------------------------------
    
    
        Besides standard :class:`~org.hipparchus.exception.MathIllegalArgumentException`, this class might throw
        :class:`~org.hipparchus.exception.MathIllegalArgumentException` if the linear operator or the preconditioner are not
        symmetric.
    
          - key :code:`"operator"` points to the offending linear operator, say L,
          - key :code:`"vector1"` points to the first offending vector, say x,
          - key :code:`"vector2"` points to the second offending vector, say y, such that x :sup:`T` Â· L Â· y â‰  y :sup:`T` Â· L
            Â· x (within a certain accuracy).
    
    
        :class:`~org.hipparchus.exception.MathIllegalArgumentException` might also be thrown in case the preconditioner is not
        positive definite.
    
        References
    ----------
    
    
        :class:`~org.hipparchus.linear`
          C. C. Paige and M. A. Saunders, `*Solution of Sparse Indefinite Systems of Linear Equations*
            <http://www.stanford.edu/group/SOL/software/symmlq/PS75.pdf>`, SIAM Journal on Numerical Analysis 12(4): 617-629, 1975
    """
    @typing.overload
    def __init__(self, int: int, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager, double: float, boolean: bool): ...
    def shouldCheck(self) -> bool:
        """
            Returns :code:`true` if symmetry of the matrix, and symmetry as well as positive definiteness of the preconditioner
            should be checked.
        
            Returns:
                :code:`true` if the tests are to be performed
        
            Since:
                1.4
        
        
        """
        ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, boolean: bool, double: float) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector, boolean: bool, double: float) -> RealVector: ...
    @typing.overload
    def solve(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realLinearOperator2: RealLinearOperator, realVector: RealVector, realVector2: RealVector, boolean: bool, double: float) -> RealVector: ...
    @typing.overload
    def solveInPlace(self, realLinearOperator: RealLinearOperator, realVector: RealVector, realVector2: RealVector) -> RealVector: ...

_Array2DRowFieldMatrix__T = typing.TypeVar('_Array2DRowFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class Array2DRowFieldMatrix(AbstractFieldMatrix[_Array2DRowFieldMatrix__T], java.io.Serializable, typing.Generic[_Array2DRowFieldMatrix__T]):
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], tArray: typing.List[_Array2DRowFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], tArray: typing.List[typing.List[_Array2DRowFieldMatrix__T]]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], tArray: typing.List[typing.List[_Array2DRowFieldMatrix__T]], boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.List[_Array2DRowFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, tArray: typing.List[typing.List[_Array2DRowFieldMatrix__T]]): ...
    @typing.overload
    def __init__(self, tArray: typing.List[typing.List[_Array2DRowFieldMatrix__T]], boolean: bool): ...
    @typing.overload
    def add(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def add(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _Array2DRowFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getData(self) -> typing.List[typing.List[_Array2DRowFieldMatrix__T]]: ...
    def getDataRef(self) -> typing.List[typing.List[_Array2DRowFieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _Array2DRowFieldMatrix__T: ...
    def getRow(self, int: int) -> typing.List[_Array2DRowFieldMatrix__T]: ...
    def getRowDimension(self) -> int: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _Array2DRowFieldMatrix__T) -> None: ...
    @typing.overload
    def multiplyTransposed(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiplyTransposed(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def operate(self, tArray: typing.List[_Array2DRowFieldMatrix__T]) -> typing.List[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_Array2DRowFieldMatrix__T]) -> FieldVector[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.List[_Array2DRowFieldMatrix__T]) -> typing.List[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_Array2DRowFieldMatrix__T]) -> FieldVector[_Array2DRowFieldMatrix__T]: ...
    def setEntry(self, int: int, int2: int, t: _Array2DRowFieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.List[_Array2DRowFieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.List[typing.List[_Array2DRowFieldMatrix__T]], int: int, int2: int) -> None: ...
    @typing.overload
    def subtract(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def subtract(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def transposeMultiply(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def transposeMultiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInColumnOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T]) -> _Array2DRowFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_Array2DRowFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _Array2DRowFieldMatrix__T: ...

class Array2DRowRealMatrix(AbstractRealMatrix, java.io.Serializable):
    """
    public class Array2DRowRealMatrix extends :class:`~org.hipparchus.linear.AbstractRealMatrix` implements Serializable
    
        Implementation of :class:`~org.hipparchus.linear.RealMatrix` using a :code:`double[][]` array to store entries.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]], boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def add(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    def copy(self) -> RealMatrix:
        """
            Returns a (deep) copy of this.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.copy` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.copy` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                matrix copy
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> RealMatrix: ...
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getColumnDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getColumnDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getColumnDimension`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns.
        
        
        """
        ...
    def getData(self) -> typing.List[typing.List[float]]:
        """
            Returns matrix entries as a two-dimensional array.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getData` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getData` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                2-dimensional array of entries
        
        
        """
        ...
    def getDataRef(self) -> typing.List[typing.List[float]]:
        """
            Get a reference to the underlying data array.
        
            Returns:
                2-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float: ...
    def getRow(self, int: int) -> typing.List[float]: ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getRowDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getRowDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getRowDimension`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    def kroneckerProduct(self, realMatrix: RealMatrix) -> RealMatrix:
        """
            Kronecker product of the current matrix and the parameter matrix.
        
            Parameters:
                b (:class:`~org.hipparchus.linear.RealMatrix`): matrix to post Kronecker-multiply by
        
            Returns:
                this â¨‚ b
        
        
        """
        ...
    @typing.overload
    def multiply(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def multiplyTransposed(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> RealMatrix:
        """
            Returns the result of postmultiplying :code:`this` by :code:`m^T`.
        
            This is equivalent to call
            :meth:`~org.hipparchus.linear.RealMatrix.multiply`(m.:meth:`~org.hipparchus.linear.RealMatrix.transpose`), but some
            implementations may avoid building the intermediate transposed matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.multiplyTransposed` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                m (:class:`~org.hipparchus.linear.RealMatrix`): matrix to first transpose and second postmultiply by
        
            Returns:
                :code:`this * m^T`
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def operate(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    def setRow(self, int: int, doubleArray: typing.List[float]) -> None: ...
    def setSubMatrix(self, doubleArray: typing.List[typing.List[float]], int: int, int2: int) -> None: ...
    def stack(self) -> RealMatrix:
        """
            Transforms a matrix in a vector (Vectorization).
        
            Returns:
                a one column matrix
        
        
        """
        ...
    @typing.overload
    def subtract(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def transposeMultiply(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> RealMatrix:
        """
            Returns the result of postmultiplying :code:`this^T` by :code:`m`.
        
            This is equivalent to call
            :meth:`~org.hipparchus.linear.RealMatrix.transpose`.:meth:`~org.hipparchus.linear.RealMatrix.multiply`, but some
            implementations may avoid building the intermediate transposed matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.transposeMultiply` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Parameters:
                m (:class:`~org.hipparchus.linear.RealMatrix`): matrix to postmultiply by
        
            Returns:
                :code:`this^T * m`
        
        
        """
        ...
    @typing.overload
    def transposeMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def unstackSquare(self) -> RealMatrix:
        """
            Transforms a one-column stacked matrix into a squared matrix (devectorization).
        
            Returns:
                square matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInColumnOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInColumnOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInColumnOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInColumnOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInColumnOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in column order.
        
            Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the
            topmost element of the next column.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInColumnOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

_BlockFieldMatrix__T = typing.TypeVar('_BlockFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class BlockFieldMatrix(AbstractFieldMatrix[_BlockFieldMatrix__T], java.io.Serializable, typing.Generic[_BlockFieldMatrix__T]):
    BLOCK_SIZE: typing.ClassVar[int] = ...
    @typing.overload
    def __init__(self, int: int, int2: int, tArray: typing.List[typing.List[_BlockFieldMatrix__T]], boolean: bool): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_BlockFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, tArray: typing.List[typing.List[_BlockFieldMatrix__T]]): ...
    @typing.overload
    def add(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def add(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def addToEntry(self, int: int, int2: int, t: _BlockFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    _createBlocksLayout__T = typing.TypeVar('_createBlocksLayout__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createBlocksLayout(field: org.hipparchus.Field[_createBlocksLayout__T], int: int, int2: int) -> typing.List[typing.List[_createBlocksLayout__T]]: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def getColumn(self, int: int) -> typing.List[_BlockFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getColumnMatrix(self, int: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def getColumnVector(self, int: int) -> FieldVector[_BlockFieldMatrix__T]: ...
    def getData(self) -> typing.List[typing.List[_BlockFieldMatrix__T]]: ...
    def getEntry(self, int: int, int2: int) -> _BlockFieldMatrix__T: ...
    def getRow(self, int: int) -> typing.List[_BlockFieldMatrix__T]: ...
    def getRowDimension(self) -> int: ...
    def getRowMatrix(self, int: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def getRowVector(self, int: int) -> FieldVector[_BlockFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def multiplyEntry(self, int: int, int2: int, t: _BlockFieldMatrix__T) -> None: ...
    @typing.overload
    def multiplyTransposed(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiplyTransposed(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def operate(self, tArray: typing.List[_BlockFieldMatrix__T]) -> typing.List[_BlockFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> FieldVector[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.List[_BlockFieldMatrix__T]) -> typing.List[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> FieldVector[_BlockFieldMatrix__T]: ...
    def scalarAdd(self, t: _BlockFieldMatrix__T) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def scalarMultiply(self, t: _BlockFieldMatrix__T) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def setColumn(self, int: int, tArray: typing.List[_BlockFieldMatrix__T]) -> None: ...
    def setColumnMatrix(self, int: int, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> None: ...
    def setColumnVector(self, int: int, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> None: ...
    def setEntry(self, int: int, int2: int, t: _BlockFieldMatrix__T) -> None: ...
    def setRow(self, int: int, tArray: typing.List[_BlockFieldMatrix__T]) -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> None: ...
    def setRowVector(self, int: int, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> None: ...
    def setSubMatrix(self, tArray: typing.List[typing.List[_BlockFieldMatrix__T]], int: int, int2: int) -> None: ...
    @typing.overload
    def subtract(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def subtract(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    _toBlocksLayout__T = typing.TypeVar('_toBlocksLayout__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def toBlocksLayout(tArray: typing.List[typing.List[_toBlocksLayout__T]]) -> typing.List[typing.List[_toBlocksLayout__T]]: ...
    def transpose(self) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def transposeMultiply(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def transposeMultiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInOptimizedOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixChangingVisitor: FieldMatrixChangingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T]) -> _BlockFieldMatrix__T: ...
    @typing.overload
    def walkInRowOrder(self, fieldMatrixPreservingVisitor: FieldMatrixPreservingVisitor[_BlockFieldMatrix__T], int: int, int2: int, int3: int, int4: int) -> _BlockFieldMatrix__T: ...

class BlockRealMatrix(AbstractRealMatrix, java.io.Serializable):
    """
    public class BlockRealMatrix extends :class:`~org.hipparchus.linear.AbstractRealMatrix` implements Serializable
    
        Cache-friendly implementation of RealMatrix using a flat arrays to store square blocks of the matrix.
    
        This implementation is specially designed to be cache-friendly. Square blocks are stored as small arrays and allow
        efficient traversal of data both in row major direction and columns major direction, one block at a time. This greatly
        increases performances for algorithms that use crossed directions loops like multiplication or transposition.
    
        The size of square blocks is a static parameter. It may be tuned according to the cache size of the target computer
        processor. As a rule of thumbs, it should be the largest value that allows three blocks to be simultaneously cached
        (this is necessary for example for matrix multiplication). The default value is to use 52x52 blocks which is well suited
        for processors with 64k L1 cache (one block holds 2704 values or 21632 bytes). This value could be lowered to 36x36 for
        processors with 32k L1 cache.
    
        The regular blocks represent :meth:`~org.hipparchus.linear.BlockRealMatrix.BLOCK_SIZE` x
        :meth:`~org.hipparchus.linear.BlockRealMatrix.BLOCK_SIZE` squares. Blocks at right hand side and bottom side may be
        smaller to fit matrix dimensions. The square blocks are flattened in row major order in single dimension arrays which
        are therefore :meth:`~org.hipparchus.linear.BlockRealMatrix.BLOCK_SIZE` :sup:`2` elements long for regular blocks. The
        blocks are themselves organized in row major order.
    
        As an example, for a block size of 52x52, a 100x60 matrix would be stored in 4 blocks. Block 0 would be a
        :code:`double[2704]` array holding the upper left 52x52 square, block 1 would be a :code:`double[416]` array holding the
        upper right 52x8 rectangle, block 2 would be a :code:`double[2496]` array holding the lower left 48x52 rectangle and
        block 3 would be a :code:`double[384]` array holding the lower right 48x8 rectangle.
    
        The layout complexity overhead versus simple mapping of matrices to java arrays is negligible for small matrices (about
        1%). The gain from cache efficiency leads to up to 3-fold improvements for matrices of moderate to large size.
    
        Also see:
            :meth:`~serialized`
    """
    BLOCK_SIZE: typing.ClassVar[int] = ...
    """
    public static final int BLOCK_SIZE
    
        Block size.
    
        Also see:
            :meth:`~constant`
    
    
    """
    @typing.overload
    def __init__(self, doubleArray: typing.List[typing.List[float]]): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, doubleArray: typing.List[typing.List[float]], boolean: bool): ...
    @typing.overload
    def add(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    def copy(self) -> 'BlockRealMatrix':
        """
            Returns a (deep) copy of this.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.copy` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.copy` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                matrix copy
        
        
        """
        ...
    @staticmethod
    def createBlocksLayout(int: int, int2: int) -> typing.List[typing.List[float]]:
        """
            Create a data array in blocks layout.
        
            This method can be used to create the array argument of the null constructor.
        
            Parameters:
                rows (int): Number of rows in the new matrix.
                columns (int): Number of columns in the new matrix.
        
            Returns:
                a new data array in blocks layout.
        
            Also see:
                null, null
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'BlockRealMatrix': ...
    def getColumn(self, int: int) -> typing.List[float]: ...
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getColumnDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getColumnDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getColumnDimension`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns.
        
        
        """
        ...
    def getColumnMatrix(self, int: int) -> 'BlockRealMatrix': ...
    def getColumnVector(self, int: int) -> RealVector: ...
    def getData(self) -> typing.List[typing.List[float]]:
        """
            Returns matrix entries as a two-dimensional array.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getData` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getData` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                2-dimensional array of entries
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float: ...
    def getFrobeniusNorm(self) -> float:
        """
            Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getFrobeniusNorm` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getFrobeniusNorm`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                norm
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
            Returns the ` maximum absolute column sum norm <http://mathworld.wolfram.com/MaximumAbsoluteColumnSumNorm.html>` (L
            :sub:`1` ) of the matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getNorm1` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Returns:
                norm
        
        
        """
        ...
    def getNormInfty(self) -> float:
        """
            Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` (L :sub:`âˆž`
            ) of the matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.getNormInfty` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Returns:
                norm
        
        
        """
        ...
    def getRow(self, int: int) -> typing.List[float]: ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getRowDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getRowDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getRowDimension`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows.
        
        
        """
        ...
    def getRowMatrix(self, int: int) -> 'BlockRealMatrix': ...
    def getRowVector(self, int: int) -> RealVector: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'BlockRealMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.List[int], intArray2: typing.List[int]) -> RealMatrix: ...
    @typing.overload
    def multiply(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def multiplyTransposed(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def multiplyTransposed(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    @typing.overload
    def operate(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, double: float) -> 'BlockRealMatrix':
        """
            Returns the result of adding :code:`d` to each entry of :code:`this`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.scalarAdd` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.scalarAdd` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): value to be added to each entry
        
            Returns:
                :code:`d + this`
        
        
        """
        ...
    def scalarMultiply(self, double: float) -> RealMatrix:
        """
            Returns the result of multiplying each entry of :code:`this` by :code:`d`.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.scalarMultiply` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.scalarMultiply`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                d (double): value to multiply all entries by
        
            Returns:
                :code:`d * this`
        
        
        """
        ...
    def setColumn(self, int: int, doubleArray: typing.List[float]) -> None: ...
    def setColumnMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setColumnVector(self, int: int, realVector: RealVector) -> None: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    def setRow(self, int: int, doubleArray: typing.List[float]) -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, blockRealMatrix: 'BlockRealMatrix') -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setRowVector(self, int: int, realVector: RealVector) -> None: ...
    def setSubMatrix(self, doubleArray: typing.List[typing.List[float]], int: int, int2: int) -> None: ...
    @typing.overload
    def subtract(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    @staticmethod
    def toBlocksLayout(doubleArray: typing.List[typing.List[float]]) -> typing.List[typing.List[float]]: ...
    def transpose(self) -> 'BlockRealMatrix':
        """
            Returns the transpose of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.transpose` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.transpose` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                transpose matrix
        
        
        """
        ...
    @typing.overload
    def transposeMultiply(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def transposeMultiply(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInOptimizedOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInOptimizedOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInOptimizedOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInOptimizedOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries using the fastest possible order.
        
            The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInOptimizedOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index (inclusive)
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInOptimizedOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
            Visit (and possibly change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
            Visit (but don't change) all matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixChangingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (and possibly change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixChangingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixChangingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        public double walkInRowOrder(:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor` visitor, int startRow, int endRow, int startColumn, int endColumn) throws :class:`~org.hipparchus.exception.MathIllegalArgumentException`
        
            Visit (but don't change) some matrix entries in row order.
        
            Row order starts at upper left and iterating through all elements of a row from left to right before going to the
            leftmost element of the next row.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Overrides:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.walkInRowOrder`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Parameters:
                visitor (:class:`~org.hipparchus.linear.RealMatrixPreservingVisitor`): visitor used to process all matrix entries
                startRow (int): Initial row index
                endRow (int): Final row index (inclusive)
                startColumn (int): Initial column index
                endColumn (int): Final column index
        
            Returns:
                the value returned by :meth:`~org.hipparchus.linear.RealMatrixPreservingVisitor.end` at the end of the walk
        
            Raises:
                :class:`~org.hipparchus.exception.MathIllegalArgumentException`: if the indices are not valid.
        
            Also see:
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInRowOrder`, :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInColumnOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`,
                :meth:`~org.hipparchus.linear.RealMatrix.walkInOptimizedOrder`
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class DiagonalMatrix(AbstractRealMatrix, java.io.Serializable):
    @typing.overload
    def __init__(self, doubleArray: typing.List[float]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.List[float], boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def add(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    def copy(self) -> RealMatrix: ...
    def createMatrix(self, int: int, int2: int) -> RealMatrix: ...
    def getColumnDimension(self) -> int: ...
    def getData(self) -> typing.List[typing.List[float]]: ...
    def getDataRef(self) -> typing.List[float]: ...
    def getEntry(self, int: int, int2: int) -> float: ...
    def getRowDimension(self) -> int: ...
    @typing.overload
    def inverse(self) -> 'DiagonalMatrix': ...
    @typing.overload
    def inverse(self, double: float) -> 'DiagonalMatrix': ...
    def isSingular(self, double: float) -> bool: ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def multiplyTransposed(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def multiplyTransposed(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def operate(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.List[float]) -> typing.List[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def subtract(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def transposeMultiply(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def transposeMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...

class OpenMapRealMatrix(AbstractRealMatrix, SparseRealMatrix, java.io.Serializable):
    """
    public class OpenMapRealMatrix extends :class:`~org.hipparchus.linear.AbstractRealMatrix` implements :class:`~org.hipparchus.linear.SparseRealMatrix`, Serializable
    
        Sparse matrix implementation based on an open addressed map.
    
        Caveat: This implementation assumes that, for any :code:`x`, the equality :code:`x * 0d == 0d` holds. But it is is not
        true for :code:`NaN`. Moreover, zero entries will lose their sign. Some operations (that involve :code:`NaN` and/or
        infinities) may thus give incorrect results.
    
        Also see:
            :meth:`~serialized`
    """
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, openMapRealMatrix: 'OpenMapRealMatrix'): ...
    @typing.overload
    def add(self, openMapRealMatrix: 'OpenMapRealMatrix') -> 'OpenMapRealMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, int: int, int2: int, double: float) -> None: ...
    def copy(self) -> 'OpenMapRealMatrix':
        """
            Returns a (deep) copy of this.
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealMatrix.copy` in interface :class:`~org.hipparchus.linear.RealMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.copy` in class :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                matrix copy
        
        
        """
        ...
    def createMatrix(self, int: int, int2: int) -> 'OpenMapRealMatrix': ...
    def getColumnDimension(self) -> int:
        """
            Returns the number of columns of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getColumnDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getColumnDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getColumnDimension`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                the number of columns.
        
        
        """
        ...
    def getEntry(self, int: int, int2: int) -> float: ...
    def getRowDimension(self) -> int:
        """
            Returns the number of rows of this matrix.
        
            Specified by:
                :meth:`~org.hipparchus.linear.AnyMatrix.getRowDimension` in interface :class:`~org.hipparchus.linear.AnyMatrix`
        
            Specified by:
                :meth:`~org.hipparchus.linear.RealLinearOperator.getRowDimension`Â in
                interfaceÂ :class:`~org.hipparchus.linear.RealLinearOperator`
        
            Specified by:
                :meth:`~org.hipparchus.linear.AbstractRealMatrix.getRowDimension`Â in
                classÂ :class:`~org.hipparchus.linear.AbstractRealMatrix`
        
            Returns:
                the number of rows.
        
        
        """
        ...
    @typing.overload
    def multiply(self, openMapRealMatrix: 'OpenMapRealMatrix') -> 'OpenMapRealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, int: int, int2: int, double: float) -> None: ...
    def multiplyTransposed(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def setEntry(self, int: int, int2: int, double: float) -> None: ...
    @typing.overload
    def subtract(self, openMapRealMatrix: 'OpenMapRealMatrix') -> 'OpenMapRealMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> 'OpenMapRealMatrix': ...
    def transposeMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...

_SparseFieldMatrix__T = typing.TypeVar('_SparseFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class SparseFieldMatrix(AbstractFieldMatrix[_SparseFieldMatrix__T], typing.Generic[_SparseFieldMatrix__T]):
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, fieldMatrix: FieldMatrix[_SparseFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, sparseFieldMatrix: 'SparseFieldMatrix'[_SparseFieldMatrix__T]): ...
    def addToEntry(self, int: int, int2: int, t: _SparseFieldMatrix__T) -> None: ...
    def copy(self) -> FieldMatrix[_SparseFieldMatrix__T]: ...
    def createMatrix(self, int: int, int2: int) -> FieldMatrix[_SparseFieldMatrix__T]: ...
    def getColumnDimension(self) -> int: ...
    def getEntry(self, int: int, int2: int) -> _SparseFieldMatrix__T: ...
    def getRowDimension(self) -> int: ...
    def multiplyEntry(self, int: int, int2: int, t: _SparseFieldMatrix__T) -> None: ...
    def multiplyTransposed(self, fieldMatrix: FieldMatrix[_SparseFieldMatrix__T]) -> FieldMatrix[_SparseFieldMatrix__T]: ...
    def setEntry(self, int: int, int2: int, t: _SparseFieldMatrix__T) -> None: ...
    def transposeMultiply(self, fieldMatrix: FieldMatrix[_SparseFieldMatrix__T]) -> FieldMatrix[_SparseFieldMatrix__T]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.linear")``.

    AbstractFieldMatrix: typing.Type[AbstractFieldMatrix]
    AbstractRealMatrix: typing.Type[AbstractRealMatrix]
    AnyMatrix: typing.Type[AnyMatrix]
    Array2DRowFieldMatrix: typing.Type[Array2DRowFieldMatrix]
    Array2DRowRealMatrix: typing.Type[Array2DRowRealMatrix]
    ArrayFieldVector: typing.Type[ArrayFieldVector]
    ArrayRealVector: typing.Type[ArrayRealVector]
    BlockFieldMatrix: typing.Type[BlockFieldMatrix]
    BlockRealMatrix: typing.Type[BlockRealMatrix]
    CholeskyDecomposer: typing.Type[CholeskyDecomposer]
    CholeskyDecomposition: typing.Type[CholeskyDecomposition]
    ComplexEigenDecomposition: typing.Type[ComplexEigenDecomposition]
    ConjugateGradient: typing.Type[ConjugateGradient]
    DecompositionSolver: typing.Type[DecompositionSolver]
    DefaultFieldMatrixChangingVisitor: typing.Type[DefaultFieldMatrixChangingVisitor]
    DefaultFieldMatrixPreservingVisitor: typing.Type[DefaultFieldMatrixPreservingVisitor]
    DefaultIterativeLinearSolverEvent: typing.Type[DefaultIterativeLinearSolverEvent]
    DefaultRealMatrixChangingVisitor: typing.Type[DefaultRealMatrixChangingVisitor]
    DefaultRealMatrixPreservingVisitor: typing.Type[DefaultRealMatrixPreservingVisitor]
    DiagonalMatrix: typing.Type[DiagonalMatrix]
    EigenDecomposition: typing.Type[EigenDecomposition]
    FieldDecompositionSolver: typing.Type[FieldDecompositionSolver]
    FieldLUDecomposition: typing.Type[FieldLUDecomposition]
    FieldMatrix: typing.Type[FieldMatrix]
    FieldMatrixChangingVisitor: typing.Type[FieldMatrixChangingVisitor]
    FieldMatrixPreservingVisitor: typing.Type[FieldMatrixPreservingVisitor]
    FieldQRDecomposition: typing.Type[FieldQRDecomposition]
    FieldVector: typing.Type[FieldVector]
    FieldVectorChangingVisitor: typing.Type[FieldVectorChangingVisitor]
    FieldVectorPreservingVisitor: typing.Type[FieldVectorPreservingVisitor]
    IterativeLinearSolver: typing.Type[IterativeLinearSolver]
    IterativeLinearSolverEvent: typing.Type[IterativeLinearSolverEvent]
    JacobiPreconditioner: typing.Type[JacobiPreconditioner]
    LUDecomposer: typing.Type[LUDecomposer]
    LUDecomposition: typing.Type[LUDecomposition]
    MatrixDecomposer: typing.Type[MatrixDecomposer]
    MatrixUtils: typing.Type[MatrixUtils]
    OpenMapRealMatrix: typing.Type[OpenMapRealMatrix]
    OpenMapRealVector: typing.Type[OpenMapRealVector]
    OrderedComplexEigenDecomposition: typing.Type[OrderedComplexEigenDecomposition]
    OrderedEigenDecomposition: typing.Type[OrderedEigenDecomposition]
    PreconditionedIterativeLinearSolver: typing.Type[PreconditionedIterativeLinearSolver]
    QRDecomposer: typing.Type[QRDecomposer]
    QRDecomposition: typing.Type[QRDecomposition]
    RRQRDecomposition: typing.Type[RRQRDecomposition]
    RealLinearOperator: typing.Type[RealLinearOperator]
    RealMatrix: typing.Type[RealMatrix]
    RealMatrixChangingVisitor: typing.Type[RealMatrixChangingVisitor]
    RealMatrixFormat: typing.Type[RealMatrixFormat]
    RealMatrixPreservingVisitor: typing.Type[RealMatrixPreservingVisitor]
    RealVector: typing.Type[RealVector]
    RealVectorChangingVisitor: typing.Type[RealVectorChangingVisitor]
    RealVectorFormat: typing.Type[RealVectorFormat]
    RealVectorPreservingVisitor: typing.Type[RealVectorPreservingVisitor]
    RectangularCholeskyDecomposition: typing.Type[RectangularCholeskyDecomposition]
    RiccatiEquationSolver: typing.Type[RiccatiEquationSolver]
    RiccatiEquationSolverImpl: typing.Type[RiccatiEquationSolverImpl]
    SingularValueDecomposer: typing.Type[SingularValueDecomposer]
    SingularValueDecomposition: typing.Type[SingularValueDecomposition]
    SparseFieldMatrix: typing.Type[SparseFieldMatrix]
    SparseFieldVector: typing.Type[SparseFieldVector]
    SparseRealMatrix: typing.Type[SparseRealMatrix]
    SparseRealVector: typing.Type[SparseRealVector]
    SymmLQ: typing.Type[SymmLQ]
