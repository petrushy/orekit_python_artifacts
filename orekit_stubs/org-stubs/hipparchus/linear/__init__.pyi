
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import java.lang
import java.text
import java.util
import java.util.function
import jpype
import org.hipparchus
import org.hipparchus.analysis
import org.hipparchus.complex
import org.hipparchus.fraction
import org.hipparchus.util
import typing



class AnyMatrix:
    """
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
    Calculates the Cholesky decomposition of a matrix.
    
    The Cholesky decomposition of a real symmetric positive-definite matrix A consists of a lower triangular matrix L with same size such that: A = LL :sup:`T` . In a sense, this is the square root of A.
    
    This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
      - a getLT method has been added,
      - the isspd method has been removed, since the constructor of this class throws a
        MathIllegalArgumentException when a matrix cannot be decomposed,
      - a getDeterminant method has been added,
      - the solve method has been replaced by a getSolver method
        and the equivalent method provided by the returned DecompositionSolver.
    
    
          - `MathWorld <http://mathworld.wolfram.com/CholeskyDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/Cholesky_decomposition>`
    """
    DEFAULT_RELATIVE_SYMMETRY_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default threshold above which off-diagonal elements are considered too different and matrix not symmetric.
    
          - constant
    
    
    
    """
    DEFAULT_ABSOLUTE_POSITIVITY_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default threshold below which diagonal elements are considered null and matrix not positive definite.
    
          - constant
    
    
    
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
    """
    Given a matrix A, it computes a complex eigen decomposition AV = VD.
    
    Complex Eigen Decomposition differs from the EigenDecompositionSymmetric since it computes the eigen vectors as complex eigen vectors (if applicable).
    
    Beware that in the complex case, you do not always have \(V \times V^{T} = I\) or even a diagonal matrix, even if the eigenvectors that form the columns of the V matrix are independent. On example is the square matrix \[ A = \left(\begin{matrix} 3 & -2\\ 4 & -1 \end{matrix}\right) \] which has two conjugate eigenvalues \(\lambda_1=1+2i\) and \(\lambda_2=1-2i\) with associated eigenvectors \(v_1^T = (1, 1-i)\) and \(v_2^T = (1, 1+i)\). \[ V\timesV^T = \left(\begin{matrix} 2 & 2\\ 2 & 0 \end{matrix}\right) \] which is not the identity matrix. Therefore, despite \(A \times V = V \times D\), \(A \ne V \times D \time V^T\), which would hold for real eigendecomposition.
    
    Also note that for consistency with Wolfram langage Eigenvectors, we add zero vectors when the geometric multiplicity of the eigenvalue is smaller than its algebraic multiplicity (hence the regular eigenvector matrix should be non-square). With these additional null vectors, the eigenvectors matrix becomes square. This happens for example with the square matrix \[ A = \left(\begin{matrix} 1 & 0 & 0\\ -2 & 1 & 0\\ 0 & 0 & 1 \end{matrix}\right) \] Its characteristic polynomial is \((1-\lambda)^3\), hence is has one eigen value \(\lambda=1\) with algebraic multiplicity 3. However, this eigenvalue leads to only two eigenvectors \(v_1=(0, 1, 0)\) and \(v_2=(0, 0, 1)\), hence its geometric multiplicity is only 2, not 3. So we add a third zero vector \(v_3=(0, 0, 0)\), in the same way Wolfram language does. Compute complex eigen values from the Schur transform. Compute complex eigen vectors based on eigen values and the inverse iteration method. see: Inverse_iteration Shifted_inverse_iteration pdf
    """
    DEFAULT_EIGENVECTORS_EQUALITY: typing.ClassVar[float] = ...
    """
    Default threshold below which eigenvectors are considered equal.
    
          - constant
    
    
    
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default value to use for internal epsilon.
    
          - constant
    
    
    
    """
    DEFAULT_EPSILON_AV_VD_CHECK: typing.ClassVar[float] = ...
    """
    Internally used epsilon criteria for final AV=VD check.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float, double3: float): ...
    def getD(self) -> 'FieldMatrix'[org.hipparchus.complex.Complex]:
        """
        Getter D.
        
        Returns:
            D.
        
        
        """
        ...
    def getDeterminant(self) -> float:
        """
        Computes the determinant.
        
        Returns:
            the determinant.
        
        
        """
        ...
    def getEigenvalues(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Getter of the eigen values.
        
        Returns:
            eigen values.
        
        
        """
        ...
    def getEigenvector(self, i: int) -> 'FieldVector'[org.hipparchus.complex.Complex]:
        """
        Getter of the eigen vectors.
        
        Parameters:
            i (int): which eigen vector.
        
        Returns:
            eigen vector.
        
        
        """
        ...
    def getV(self) -> 'FieldMatrix'[org.hipparchus.complex.Complex]:
        """
        Getter V.
        
        Returns:
            V.
        
        
        """
        ...
    def getVT(self) -> 'FieldMatrix'[org.hipparchus.complex.Complex]:
        """
        Getter VT.
        
        Returns:
            VT.
        
        
        """
        ...
    def hasComplexEigenvalues(self) -> bool:
        """
        Confirm if there are complex eigen values.
        
        Returns:
            true if there are complex eigen values.
        
        
        """
        ...

class DecompositionSolver:
    """
    Interface handling decomposition algorithms that can solve A × X = B.
    
    Decomposition algorithms decompose an A matrix as a product of several specific matrices from which they can solve A × X = B in least squares sense: they find X such that ||A × X - B|| is minimal.
    
    Some solvers like LUDecomposition can only find the solution for square matrices and when the solution is an exact linear solution, i.e. when ||A × X - B|| is exactly 0. Other solvers can also find solutions with non-square matrix A and with non-null minimal norm. If an exact linear solution exists it is also the minimal norm solution.
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
    def getInverse(self) -> 'RealMatrix':
        """
        Get the `pseudo-inverse <http://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_pseudoinverse>` of the decomposed matrix.
        
        This is equal to the inverse of the decomposed matrix, if such an inverse exists.
        
        If no such inverse exists, then the result has properties that resemble that of an inverse.
        
        In particular, in this case, if the decomposed matrix is A, then the system of equations \( A x = b \) may have no solutions, or many. If it has no solutions, then the pseudo-inverse \( A^+ \) gives the "closest" solution \( z = A^+ b \), meaning \( \left \| A z - b \right \|_2 \) is minimized. If there are many solutions, then \( z = A^+ b \) is the smallest solution, meaning \( \left \| z \right \|_2 \) is minimized.
        
        Note however that some decompositions cannot compute a pseudo-inverse for all matrices. For example, the LUDecomposition is not defined for non-square matrices to begin with. The QRDecomposition can operate on non-square matrices, but will throw MathIllegalArgumentException if the decomposed matrix is singular. Refer to the javadoc of specific decomposition implementations for more details.
        
        Returns:
            pseudo-inverse matrix (which is the inverse, if it exists), if the decomposition can pseudo-invert the decomposed matrix
        
        Raises:
            MathIllegalArgumentException: if the decomposed matrix is singular and the decomposition can not compute a pseudo-inverse
        
        
        """
        ...
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

class DependentVectorsHandler(java.lang.Enum['DependentVectorsHandler']):
    """
    Enumerate to specify how dependent vectors should be handled in orthonormalize and orthonormalize.
    
    Since:
        2.1
    """
    GENERATE_EXCEPTION: typing.ClassVar['DependentVectorsHandler'] = ...
    ADD_ZERO_VECTOR: typing.ClassVar['DependentVectorsHandler'] = ...
    REDUCE_BASE_TO_SPAN: typing.ClassVar['DependentVectorsHandler'] = ...
    _manageDependent_1__T = typing.TypeVar('_manageDependent_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    def manageDependent(self, int: int, list: java.util.List['RealVector']) -> int: ...
    @typing.overload
    def manageDependent(self, field: org.hipparchus.Field[_manageDependent_1__T], int: int, list: java.util.List['FieldVector'[_manageDependent_1__T]]) -> int: ...
    _valueOf_0__T = typing.TypeVar('_valueOf_0__T', bound=java.lang.Enum)  # <T>
    @typing.overload
    @staticmethod
    def valueOf(class_: typing.Type[_valueOf_0__T], string: str) -> _valueOf_0__T: ...
    @typing.overload
    @staticmethod
    def valueOf(name: str) -> 'DependentVectorsHandler':
        """
        Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)
        
        Parameters:
            name (String): the name of the enum constant to be returned.
        
        Returns:
            the enum constant with the specified name
        
        Raises:
            IllegalArgumentException: if this enum type has no constant with the specified name
            NullPointerException: if the argument is null
        
        
        """
        ...
    @staticmethod
    def values() -> typing.MutableSequence['DependentVectorsHandler']:
        """
        Returns an array containing the constants of this enum type, in the order they are declared.
        
        Returns:
            an array containing the constants of this enum type, in the order they are declared
        
        
        """
        ...

class EigenDecompositionNonSymmetric:
    """
    Calculates the eigen decomposition of a non-symmetric real matrix.
    
    The eigen decomposition of matrix A is a set of two matrices: \(V\) and \(D\) such that \(A V = V D\) where $\(A\), \(V\) and \(D\) are all \(m \times m\) matrices.
    
    This class is similar in spirit to the EigenvalueDecomposition class from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
      - a getVInv method has been added,
      - z getEigenvalue method to pick up a single eigenvalue has
        been added,
      - a getEigenvector method to pick up a single eigenvector
        has been added,
      - a getDeterminant method has been added.
    
    This class supports non-symmetric matrices, which have complex eigenvalues. Support for symmetric matrices is provided by EigenDecompositionSymmetric.
    
    As \(A\) is not symmetric, then the eigenvalue matrix \(D\) is block diagonal with the real eigenvalues in 1-by-1 blocks and any complex eigenvalues, \(\lambda \pm i \mu\), in 2-by-2 blocks:
    
    \[ \begin{bmatrix} \lambda & \mu\\ -\mu & \lambda \end{bmatrix} \]
    
    The columns of \(V\) represent the eigenvectors in the sense that \(A V = V D\), i.e. multiply(V) equals multiply(D). The matrix \(V\) may be badly conditioned, or even singular, so the validity of the equation \(A = V D V^{-1}\) depends upon the condition of \(V\).
    
    This implementation is based on the paper by A. Drubrulle, R.S. Martin and J.H. Wilkinson "The Implicit QL Algorithm" in Wilksinson and Reinsch (1971) Handbook for automatic computation, vol. 2, Linear algebra, Springer-Verlag, New-York.
    
    Since:
        3.0
    
          - `MathWorld <http://mathworld.wolfram.com/EigenDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix>`
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default epsilon value to use for internal epsilon
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getD(self) -> 'RealMatrix':
        """
        Gets the block diagonal matrix D of the decomposition. D is a block diagonal matrix. Real eigenvalues are on the diagonal while complex values are on 2x2 blocks { {real +imaginary}, {-imaginary, real} }.
        
        Returns:
            the D matrix.
        
        
        """
        ...
    def getDeterminant(self) -> org.hipparchus.complex.Complex:
        """
        Computes the determinant of the matrix.
        
        Returns:
            the determinant of the matrix.
        
        
        """
        ...
    def getEigenvalue(self, i: int) -> org.hipparchus.complex.Complex:
        """
        Returns the i :sup:`th` eigenvalue of the original matrix.
        
        Parameters:
            i (int): index of the eigenvalue (counting from 0)
        
        Returns:
            i :sup:`th` eigenvalue of the original matrix.
        
              - getD
              - getEigenvalues
        
        
        
        """
        ...
    def getEigenvalues(self) -> typing.MutableSequence[org.hipparchus.complex.Complex]:
        """
        Gets a copy of the eigenvalues of the original matrix.
        
        Returns:
            a copy of the eigenvalues of the original matrix.
        
              - getD
              - getEigenvalue
        
        
        
        """
        ...
    def getEigenvector(self, i: int) -> 'FieldVector'[org.hipparchus.complex.Complex]:
        """
        Gets a copy of the i :sup:`th` eigenvector of the original matrix.
        
        Note that if the the i :sup:`th` is complex this method will throw an exception.
        
        Parameters:
            i (int): Index of the eigenvector (counting from 0).
        
        Returns:
            a copy of the i :sup:`th` eigenvector of the original matrix.
        
              - getD
        
        
        
        """
        ...
    def getEpsilon(self) -> float:
        """
        Get's the value for epsilon which is used for internal tests (e.g. is singular, eigenvalue ratio, etc.)
        
        Returns:
            the epsilon value.
        
        
        """
        ...
    def getV(self) -> 'RealMatrix':
        """
        Gets the matrix V of the decomposition. V is a matrix whose columns hold either the real or the imaginary part of eigenvectors.
        
        Returns:
            the V matrix.
        
        
        """
        ...
    def getVInv(self) -> 'RealMatrix':
        """
        Gets the inverse of the matrix V of the decomposition.
        
        Returns:
            the inverse of the V matrix.
        
        
        """
        ...

class EigenDecompositionSymmetric:
    """
    Calculates the eigen decomposition of a symmetric real matrix.
    
    The eigen decomposition of matrix A is a set of two matrices: \(V\) and \(D\) such that \(A V = V D\) where $\(A\), \(V\) and \(D\) are all \(m \times m\) matrices.
    
    This class is similar in spirit to the EigenvalueDecomposition class from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
      - a getVT method has been added,
      - a getEigenvalue method to pick up a single eigenvalue has
        been added,
      - a getEigenvector method to pick up a single eigenvector has
        been added,
      - a getDeterminant method has been added.
      - a getSolver method has been added.
    
    As \(A\) is symmetric, then \(A = V D V^T\) where the eigenvalue matrix \(D\) is diagonal and the eigenvector matrix \(V\) is orthogonal, i.e. transpose())) and transpose()) equals the identity matrix.
    
    The columns of \(V\) represent the eigenvectors in the sense that \(A V = V D\), i.e. multiply(V) equals multiply(D). The matrix \(V\) may be badly conditioned, or even singular, so the validity of the equation \(A = V D V^{-1}\) depends upon the condition of \(V\). This implementation is based on the paper by A. Drubrulle, R.S. Martin and J.H. Wilkinson "The Implicit QL Algorithm" in Wilksinson and Reinsch (1971) Handbook for automatic computation, vol. 2, Linear algebra, Springer-Verlag, New-York.
    
          - `MathWorld <http://mathworld.wolfram.com/EigenDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix>`
    """
    DEFAULT_EPSILON: typing.ClassVar[float] = ...
    """
    Default epsilon value to use for internal epsilon
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray], double3: float, boolean: bool): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, boolean: bool): ...
    def getD(self) -> 'DiagonalMatrix':
        """
        Gets the diagonal matrix D of the decomposition. D is a diagonal matrix.
        
        Returns:
            the D matrix.
        
              - getEigenvalues
        
        
        
        """
        ...
    def getDeterminant(self) -> float:
        """
        Computes the determinant of the matrix.
        
        Returns:
            the determinant of the matrix.
        
        
        """
        ...
    def getEigenvalue(self, i: int) -> float:
        """
        Returns the i :sup:`th` eigenvalue of the original matrix.
        
        Parameters:
            i (int): index of the eigenvalue (counting from 0)
        
        Returns:
            real part of the i :sup:`th` eigenvalue of the original matrix.
        
              - getD
              - getEigenvalues
        
        
        
        """
        ...
    def getEigenvalues(self) -> typing.MutableSequence[float]:
        """
        Gets a copy of the eigenvalues of the original matrix.
        
        Returns:
            a copy of the eigenvalues of the original matrix.
        
              - getD
              - getEigenvalue
        
        
        
        """
        ...
    def getEigenvector(self, i: int) -> 'RealVector':
        """
        Gets a copy of the i :sup:`th` eigenvector of the original matrix.
        
        Note that if the the i :sup:`th` is complex this method will throw an exception.
        
        Parameters:
            i (int): Index of the eigenvector (counting from 0).
        
        Returns:
            a copy of the i :sup:`th` eigenvector of the original matrix.
        
              - getD
        
        
        
        """
        ...
    def getEpsilon(self) -> float:
        """
        Get's the value for epsilon which is used for internal tests (e.g. is singular, eigenvalue ratio, etc.)
        
        Returns:
            the epsilon value.
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
        Gets a solver for finding the \(A \times X = B\) solution in exact linear sense.
        
        Returns:
            a solver
        
        
        """
        ...
    def getSquareRoot(self) -> 'RealMatrix':
        """
        Computes the square-root of the matrix. This implementation assumes that the matrix is positive definite.
        
        Returns:
            the square-root of the matrix.
        
        Raises:
            MathRuntimeException: if the matrix is not symmetric or not positive definite.
        
        
        """
        ...
    def getV(self) -> 'RealMatrix':
        """
        Gets the matrix V of the decomposition. V is an orthogonal matrix, i.e. its transpose is also its inverse. The columns of V are the eigenvectors of the original matrix. No assumption is made about the orientation of the system axes formed by the columns of V (e.g. in a 3-dimension space, V can form a left- or right-handed system).
        
        Returns:
            the V matrix.
        
        
        """
        ...
    def getVT(self) -> 'RealMatrix':
        """
        Gets the transpose of the matrix V of the decomposition. V is an orthogonal matrix, i.e. its transpose is also its inverse. The columns of V are the eigenvectors of the original matrix. No assumption is made about the orientation of the system axes formed by the columns of V (e.g. in a 3-dimension space, V can form a left- or right-handed system).
        
        Returns:
            the transpose of the V matrix.
        
        
        """
        ...

_FieldDecompositionSolver__T = typing.TypeVar('_FieldDecompositionSolver__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldDecompositionSolver(typing.Generic[_FieldDecompositionSolver__T]):
    """
    Interface handling decomposition algorithms that can solve A × X = B.
    
    Decomposition algorithms decompose an A matrix has a product of several specific matrices from which they can solve A × X = B in least squares sense: they find X such that ||A × X - B|| is minimal.
    
    Some solvers like FieldLUDecomposition can only find the solution for square matrices and when the solution is an exact linear solution, i.e. when ||A × X - B|| is exactly 0. Other solvers can also find solutions with non-square matrix A and with non-null minimal norm. If an exact linear solution exists it is also the minimal norm solution.
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
    def getInverse(self) -> 'FieldMatrix'[_FieldDecompositionSolver__T]:
        """
        Get the inverse (or pseudo-inverse) of the decomposed matrix.
        
        Returns:
            inverse matrix
        
        Raises:
            MathIllegalArgumentException: if the decomposed matrix is singular.
        
        
        """
        ...
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
    Calculates the LUP-decomposition of a square matrix.
    
    The LUP-decomposition of a matrix A consists of three matrices L, U and P that satisfy: PA = LU, L is lower triangular, and U is upper triangular and P is a permutation matrix. All matrices are m×m.
    
    This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
      - a getP method has been added,
      - the det method has been renamed as getDeterminant,
      - the getDoublePivot method has been removed (but the int based
        getPivot method has been kept),
      - the solve and isNonSingular methods have been replaced by a
        getSolver method and the equivalent methods provided by the returned
        DecompositionSolver.
    
    
          - `MathWorld <http://mathworld.wolfram.com/LUDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/LU_decomposition>`
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
    def getL(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]:
        """
        Returns the matrix L of the decomposition.
        
        L is a lower-triangular matrix
        
        Returns:
            the L matrix (or null if decomposed matrix is singular)
        
        
        """
        ...
    def getP(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]:
        """
        Returns the P rows permutation matrix.
        
        P is a sparse matrix with exactly one element set to 1.0 in each row and each column, all other elements being set to 0.0.
        
        The positions of the 1 elements are given by the getPivot.
        
        Returns:
            the P rows permutation matrix (or null if decomposed matrix is singular)
        
              - getPivot
        
        
        
        """
        ...
    def getPivot(self) -> typing.MutableSequence[int]:
        """
        Returns the pivot permutation vector.
        
        Returns:
            the pivot permutation vector
        
              - getP
        
        
        
        """
        ...
    def getSolver(self) -> FieldDecompositionSolver[_FieldLUDecomposition__T]:
        """
        Get a solver for finding the A × X = B solution in exact linear sense.
        
        Returns:
            a solver
        
        
        """
        ...
    def getU(self) -> 'FieldMatrix'[_FieldLUDecomposition__T]:
        """
        Returns the matrix U of the decomposition.
        
        U is an upper-triangular matrix
        
        Returns:
            the U matrix (or null if decomposed matrix is singular)
        
        
        """
        ...

_FieldMatrixChangingVisitor__T = typing.TypeVar('_FieldMatrixChangingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrixChangingVisitor(typing.Generic[_FieldMatrixChangingVisitor__T]):
    """
    Interface defining a visitor for matrix entries.
    """
    def end(self) -> _FieldMatrixChangingVisitor__T:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
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
    def visit(self, row: int, column: int, value: _FieldMatrixChangingVisitor__T) -> _FieldMatrixChangingVisitor__T:
        """
        Visit one matrix entry.
        
        Parameters:
            row (int): row index of the entry
            column (int): column index of the entry
            value (FieldMatrixChangingVisitor): current value of the entry
        
        Returns:
            the new value to be set for the entry
        
        
        """
        ...

_FieldMatrixDecomposer__T = typing.TypeVar('_FieldMatrixDecomposer__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrixDecomposer(typing.Generic[_FieldMatrixDecomposer__T]):
    """
    Interface for all algorithms providing matrix decomposition.
    
    Since:
        2.2
    """
    def decompose(self, a: 'FieldMatrix'[_FieldMatrixDecomposer__T]) -> FieldDecompositionSolver[_FieldMatrixDecomposer__T]:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Parameters:
            a (FieldMatrix<FieldMatrixDecomposer> a): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        Raises:
            MathIllegalArgumentException: if decomposition fails
        
        
        """
        ...

_FieldMatrixPreservingVisitor__T = typing.TypeVar('_FieldMatrixPreservingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrixPreservingVisitor(typing.Generic[_FieldMatrixPreservingVisitor__T]):
    """
    Interface defining a visitor for matrix entries.
    """
    def end(self) -> _FieldMatrixPreservingVisitor__T:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
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
    def visit(self, row: int, column: int, value: _FieldMatrixPreservingVisitor__T) -> None:
        """
        Visit one matrix entry.
        
        Parameters:
            row (int): row index of the entry
            column (int): column index of the entry
            value (FieldMatrixPreservingVisitor): current value of the entry
        
        
        """
        ...

_FieldQRDecomposition__T = typing.TypeVar('_FieldQRDecomposition__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQRDecomposition(typing.Generic[_FieldQRDecomposition__T]):
    """
    Calculates the QR-decomposition of a field matrix.
    
    The QR-decomposition of a matrix A consists of two matrices Q and R that satisfy: A = QR, Q is orthogonal (Q :sup:`T` Q = I), and R is upper triangular. If A is m×n, Q is m×m and R m×n.
    
    This class compute the decomposition using Householder reflectors.
    
    For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows, which is much more cache-efficient in Java.
    
    This class is based on the class QRDecomposition.
    
          - `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldQRDecomposition__T]): ...
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldQRDecomposition__T], t: _FieldQRDecomposition__T): ...
    @typing.overload
    def __init__(self, fieldMatrix: 'FieldMatrix'[_FieldQRDecomposition__T], t: _FieldQRDecomposition__T, predicate: typing.Union[java.util.function.Predicate[_FieldQRDecomposition__T], typing.Callable[[_FieldQRDecomposition__T], bool]]): ...
    def getH(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]:
        """
        Returns the Householder reflector vectors.
        
        H is a lower trapezoidal matrix whose columns represent each successive Householder reflector vector. This matrix is used to compute Q.
        
        Returns:
            a matrix containing the Householder reflector vectors
        
        
        """
        ...
    def getQ(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]:
        """
        Returns the matrix Q of the decomposition.
        
        Q is an orthogonal matrix
        
        Returns:
            the Q matrix
        
        
        """
        ...
    def getQT(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]:
        """
        Returns the transpose of the matrix Q of the decomposition.
        
        Q is an orthogonal matrix
        
        Returns:
            the transpose of the Q matrix, Q :sup:`T`
        
        
        """
        ...
    def getR(self) -> 'FieldMatrix'[_FieldQRDecomposition__T]:
        """
        Returns the matrix R of the decomposition.
        
        R is an upper-triangular matrix
        
        Returns:
            the R matrix
        
        
        """
        ...
    def getSolver(self) -> FieldDecompositionSolver[_FieldQRDecomposition__T]:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Least Square sense means a solver can be computed for an overdetermined system, (i.e. a system with more equations than unknowns, which corresponds to a tall A matrix with more rows than columns). In any case, if the matrix is singular within the tolerance set at , an error will be triggered when the solve method will be called.
        
        Returns:
            a solver
        
        
        """
        ...

_FieldVector__T = typing.TypeVar('_FieldVector__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldVector(typing.Generic[_FieldVector__T]):
    """
    Interface defining a field-valued vector with basic algebraic operations.
    
    vector element indexing is 0-based -- e.g., getEntry(0) returns the first element of the vector.
    
    The various mapXxx and mapXxxToSelf methods operate on vectors element-wise, i.e. they perform the same operation (adding a scalar, applying a function ...) on each element in turn. The mapXxx versions create a new vector to hold the result and do not change the instance. The mapXxxToSelf versions use the instance itself to store the results, so the instance is changed by these methods. In both cases, the result vector is returned by the methods, this allows to use the fluent API style, like this:
    
    
       RealVector result = v.mapAddToSelf(3.0).mapTanToSelf().mapSquareToSelf();
     
    
    Note that as almost all operations on FieldElement throw NullArgumentException when operating on a null element, it is the responsibility of FieldVector implementations to make sure no null elements are inserted into the vector. This must be done in all constructors and all setters.
    """
    def add(self, v: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]:
        """
        Compute the sum of this and v.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector to be added
        
        Returns:
            this + v
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
        
        
        """
        ...
    @typing.overload
    def append(self, t: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]: ...
    @typing.overload
    def append(self, fieldVector: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]: ...
    def copy(self) -> 'FieldVector'[_FieldVector__T]:
        """
        Returns a (deep) copy of this.
        
        Returns:
            vector copy
        
        
        """
        ...
    def dotProduct(self, v: 'FieldVector'[_FieldVector__T]) -> _FieldVector__T:
        """
        Compute the dot product.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector with which dot product should be computed
        
        Returns:
            the scalar dot product of this and v
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
        
        
        """
        ...
    def ebeDivide(self, v: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]:
        """
        Element-by-element division.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector by which instance elements must be divided
        
        Returns:
            a vector containing this[i] / v[i] for all i
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
            MathRuntimeException: if one entry of v is zero.
        
        
        """
        ...
    def ebeMultiply(self, v: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]:
        """
        Element-by-element multiplication.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector by which instance elements must be multiplied
        
        Returns:
            a vector containing this[i] * v[i] for all i
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the size of the vector.
        
        Returns:
            size
        
        
        """
        ...
    def getEntry(self, index: int) -> _FieldVector__T:
        """
        Returns the entry in the specified index.
        
        Parameters:
            index (int): Index location of entry to be fetched.
        
        Returns:
            the vector entry at index.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - setEntry
        
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldVector__T]:
        """
        Get the type of field elements of the vector.
        
        Returns:
            type of field elements of the vector
        
        
        """
        ...
    def getSubVector(self, index: int, n: int) -> 'FieldVector'[_FieldVector__T]:
        """
        Get a subvector from consecutive elements.
        
        Parameters:
            index (int): index of first element.
            n (int): number of elements to be retrieved.
        
        Returns:
            a vector containing n elements.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
            MathIllegalArgumentException: if the number of elements if not positive.
        
        
        """
        ...
    def mapAdd(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map an addition operation to each entry.
        
        Parameters:
            d (FieldVector): value to be added to each entry
        
        Returns:
            this + d
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapAddToSelf(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map an addition operation to each entry.
        
        The instance is changed by this method.
        
        Parameters:
            d (FieldVector): value to be added to each entry
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapDivide(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map a division operation to each entry.
        
        Parameters:
            d (FieldVector): value to divide all entries by
        
        Returns:
            this / d
        
        Raises:
            NullArgumentException: if d is null.
            MathRuntimeException: if d is zero.
        
        
        """
        ...
    def mapDivideToSelf(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map a division operation to each entry.
        
        The instance is changed by this method.
        
        Parameters:
            d (FieldVector): value to divide all entries by
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
            MathRuntimeException: if d is zero.
        
        
        """
        ...
    def mapInv(self) -> 'FieldVector'[_FieldVector__T]:
        """
        Map the 1/x function to each entry.
        
        Returns:
            a vector containing the result of applying the function to each entry.
        
        Raises:
            MathRuntimeException: if one of the entries is zero.
        
        
        """
        ...
    def mapInvToSelf(self) -> 'FieldVector'[_FieldVector__T]:
        """
        Map the 1/x function to each entry.
        
        The instance is changed by this method.
        
        Returns:
            for convenience, return this
        
        Raises:
            MathRuntimeException: if one of the entries is zero.
        
        
        """
        ...
    def mapMultiply(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map a multiplication operation to each entry.
        
        Parameters:
            d (FieldVector): value to multiply all entries by
        
        Returns:
            this * d
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapMultiplyToSelf(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map a multiplication operation to each entry.
        
        The instance is changed by this method.
        
        Parameters:
            d (FieldVector): value to multiply all entries by
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapSubtract(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map a subtraction operation to each entry.
        
        Parameters:
            d (FieldVector): value to be subtracted to each entry
        
        Returns:
            this - d
        
        Raises:
            NullArgumentException: if d is null
        
        
        """
        ...
    def mapSubtractToSelf(self, d: _FieldVector__T) -> 'FieldVector'[_FieldVector__T]:
        """
        Map a subtraction operation to each entry.
        
        The instance is changed by this method.
        
        Parameters:
            d (FieldVector): value to be subtracted to each entry
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null
        
        
        """
        ...
    def outerProduct(self, v: 'FieldVector'[_FieldVector__T]) -> 'FieldMatrix'[_FieldVector__T]:
        """
        Compute the outer product.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector with which outer product should be computed
        
        Returns:
            the matrix outer product between instance and v
        
        
        """
        ...
    def projection(self, v: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]:
        """
        Find the orthogonal projection of this vector onto another vector.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector onto which this must be projected
        
        Returns:
            projection of this onto v
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
            MathRuntimeException: if v is the null vector.
        
        
        """
        ...
    def set(self, value: _FieldVector__T) -> None:
        """
        Set all elements to a single value.
        
        Parameters:
            value (FieldVector): single value to set for all elements
        
        
        """
        ...
    def setEntry(self, index: int, value: _FieldVector__T) -> None:
        """
        Set a single element.
        
        Parameters:
            index (int): element index.
            value (FieldVector): new value for the element.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - getEntry
        
        
        
        """
        ...
    def setSubVector(self, index: int, v: 'FieldVector'[_FieldVector__T]) -> None:
        """
        Set a set of consecutive elements.
        
        Parameters:
            index (int): index of first element to be set.
            v (FieldVector<FieldVector> v): vector containing the values to set.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    def subtract(self, v: 'FieldVector'[_FieldVector__T]) -> 'FieldVector'[_FieldVector__T]:
        """
        Compute this minus v.
        
        Parameters:
            v (FieldVector<FieldVector> v): vector to be subtracted
        
        Returns:
            this - v
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[_FieldVector__T]:
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
    This interface defines a visitor for the entries of a vector. Visitors implementing this interface may alter the entries of the vector being visited.
    """
    def end(self) -> _FieldVectorChangingVisitor__T:
        """
        End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
        Returns:
            the value returned after visiting all entries
        
        
        """
        ...
    def start(self, dimension: int, start: int, end: int) -> None:
        """
        Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
        Parameters:
            dimension (int): the size of the vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, index: int, value: _FieldVectorChangingVisitor__T) -> _FieldVectorChangingVisitor__T:
        """
        Visit one entry of the vector.
        
        Parameters:
            index (int): the index of the entry being visited
            value (FieldVectorChangingVisitor): the value of the entry being visited
        
        Returns:
            the new value of the entry being visited
        
        
        """
        ...

_FieldVectorPreservingVisitor__T = typing.TypeVar('_FieldVectorPreservingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldVectorPreservingVisitor(typing.Generic[_FieldVectorPreservingVisitor__T]):
    """
    This interface defines a visitor for the entries of a vector. Visitors implementing this interface do not alter the entries of the vector being visited.
    """
    def end(self) -> _FieldVectorPreservingVisitor__T:
        """
        End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
        Returns:
            the value returned after visiting all entries
        
        
        """
        ...
    def start(self, dimension: int, start: int, end: int) -> None:
        """
        Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
        Parameters:
            dimension (int): the size of the vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, index: int, value: _FieldVectorPreservingVisitor__T) -> None:
        """
        Visit one entry of the vector.
        
        Parameters:
            index (int): the index of the entry being visited
            value (FieldVectorPreservingVisitor): the value of the entry being visited
        
        
        """
        ...

class HessenbergTransformer:
    """
    Class transforming a general real matrix to Hessenberg form.
    
    A m × m matrix A can be written as the product of three matrices: A = P × H × P :sup:`T` with P an orthogonal matrix and H a Hessenberg matrix. Both P and H are m × m matrices.
    
    Transformation to Hessenberg form is often not a goal by itself, but it is an intermediate step in more general decomposition algorithms like EigenDecompositionSymmetric. This class is therefore intended for internal use by the library and is not public. As a consequence of this explicitly limited scope, many methods directly returns references to internal arrays, not copies.
    
    This class is based on the method orthes in class EigenvalueDecomposition from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
          - `MathWorld <http://mathworld.wolfram.com/HessenbergDecomposition.html>`
          - `Householder Transformations <http://en.wikipedia.org/wiki/Householder_transformation>`
    """
    def __init__(self, matrix: 'RealMatrix'):
        """
        Build the transformation to Hessenberg form of a general matrix.
        
        Parameters:
            matrix (RealMatrix): matrix to transform
        
        Raises:
            MathIllegalArgumentException: if the matrix is not square
        
        
        """
        ...
    def getH(self) -> 'RealMatrix':
        """
        Returns the Hessenberg matrix H of the transform.
        
        Returns:
            the H matrix
        
        
        """
        ...
    def getP(self) -> 'RealMatrix':
        """
        Returns the matrix P of the transform.
        
        P is an orthogonal matrix, i.e. its inverse is also its transpose.
        
        Returns:
            the P matrix
        
        
        """
        ...
    def getPT(self) -> 'RealMatrix':
        """
        Returns the transpose of the matrix P of the transform.
        
        P is an orthogonal matrix, i.e. its inverse is also its transpose.
        
        Returns:
            the transpose of the P matrix
        
        
        """
        ...

class IterativeLinearSolver:
    """
    This abstract class defines an iterative solver for the linear system A · x = b. In what follows, the residual r is defined as r = b - A · x, where A is the linear operator of the linear system, b is the right-hand side vector, and x the current estimate of the solution.
    """
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
    def solveInPlace(self, a: 'RealLinearOperator', b: 'RealVector', x0: 'RealVector') -> 'RealVector':
        """
        Returns an estimate of the solution to the linear system A · x = b. The solution is computed in-place (initial guess is modified).
        
        Parameters:
            a (RealLinearOperator): the linear operator A of the system
            b (RealVector): the right-hand side vector
            x0 (RealVector): initial guess of the solution
        
        Returns:
            a reference to x0 (shallow copy) updated with the solution
        
        Raises:
            NullArgumentException: if one of the parameters is null
            MathIllegalArgumentException: if a is not square
            MathIllegalArgumentException: if b or x0 have dimensions inconsistent with a
            MathIllegalStateException: at exhaustion of the iteration count, unless a custom MaxCountExceededCallback
                has been set at construction of the IterationManager
        
        
        """
        ...

class IterativeLinearSolverEvent(org.hipparchus.util.IterationEvent):
    """
    This is the base class for all events occurring during the iterations of a IterativeLinearSolver.
    
          - serialized
    """
    def getNormOfResidual(self) -> float:
        """
        Returns the norm of the residual. The returned value is not required to be exact. Instead, the norm of the so-called updated residual (if available) should be returned. For example, the ConjugateGradient method computes a sequence of residuals, the norm of which is cheap to compute. However, due to accumulation of round-off errors, this residual might differ from the true residual after some iterations. See e.g. A. Greenbaum and Z. Strakos, Predicting the Behavior of Finite Precision Lanzos and Conjugate Gradient Computations, Technical Report 538, Department of Computer Science, New York University, 1991 (available `here <http://www.archive.org/details/predictingbehavi00gree>`).
        
        Returns:
            the norm of the residual, ||r||
        
        
        """
        ...
    def getResidual(self) -> 'RealVector':
        """
        Returns the residual. This is an optional operation, as all iterative linear solvers do not provide cheap estimate of the updated residual vector, in which case
        
          - this method should throw a MathRuntimeException,
          - providesResidual returns false.
        
        The default implementation throws a MathRuntimeException. If this method is overriden, then providesResidual should be overriden as well.
        
        Returns:
            the updated residual, r
        
        
        """
        ...
    def getRightHandSideVector(self) -> 'RealVector':
        """
        Returns the current right-hand side of the linear system to be solved. This method should return an unmodifiable view, or a deep copy of the actual right-hand side vector, in order not to compromise subsequent iterations of the source IterativeLinearSolver.
        
        Returns:
            the right-hand side vector, b
        
        
        """
        ...
    def getSolution(self) -> 'RealVector':
        """
        Returns the current estimate of the solution to the linear system to be solved. This method should return an unmodifiable view, or a deep copy of the actual current solution, in order not to compromise subsequent iterations of the source IterativeLinearSolver.
        
        Returns:
            the solution, x
        
        
        """
        ...
    def providesResidual(self) -> bool:
        """
        Returns true if getResidual is supported. The default implementation returns false.
        
        Returns:
            false if getResidual throws a
            MathRuntimeException
        
        
        """
        ...

class LUDecomposition:
    """
    Calculates the LUP-decomposition of a square matrix.
    
    The LUP-decomposition of a matrix A consists of three matrices L, U and P that satisfy: P×A = L×U. L is lower triangular (with unit diagonal terms), U is upper triangular and P is a permutation matrix. All matrices are m×m.
    
    As shown by the presence of the P matrix, this decomposition is implemented using partial pivoting.
    
    This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
      - a getP method has been added,
      - the det method has been renamed as getDeterminant,
      - the getDoublePivot method has been removed (but the int based
        getPivot method has been kept),
      - the solve and isNonSingular methods have been replaced by a
        getSolver method and the equivalent methods provided by the returned
        DecompositionSolver.
    
    
          - `MathWorld <http://mathworld.wolfram.com/LUDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/LU_decomposition>`
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
        
        P is a sparse matrix with exactly one element set to 1.0 in each row and each column, all other elements being set to 0.0.
        
        The positions of the 1 elements are given by the getPivot.
        
        Returns:
            the P rows permutation matrix (or null if decomposed matrix is singular)
        
              - getPivot
        
        
        
        """
        ...
    def getPivot(self) -> typing.MutableSequence[int]:
        """
        Returns the pivot permutation vector.
        
        Returns:
            the pivot permutation vector
        
              - getP
        
        
        
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
    Interface for all algorithms providing matrix decomposition.
    
    Since:
        1.3
    """
    def decompose(self, a: 'RealMatrix') -> DecompositionSolver:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Parameters:
            a (RealMatrix): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        Raises:
            MathIllegalArgumentException: if decomposition fails
        
        
        """
        ...

class MatrixUtils:
    """
    A collection of static methods that operate on or return matrices.
    """
    DEFAULT_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    The default format for RealMatrix objects.
    """
    OCTAVE_FORMAT: typing.ClassVar['RealMatrixFormat'] = ...
    """
    A format for RealMatrix objects compatible with octave.
    """
    @staticmethod
    def bigFractionMatrixToRealMatrix(m: 'FieldMatrix'[org.hipparchus.fraction.BigFraction]) -> 'Array2DRowRealMatrix':
        """
        Convert a FieldMatrix/BigFraction matrix to a RealMatrix.
        
        Parameters:
            m (FieldMatrix<BigFraction> m): Matrix to convert.
        
        Returns:
            the converted matrix.
        
        
        """
        ...
    @staticmethod
    def blockInverse(m: 'RealMatrix', splitIndex: int) -> 'RealMatrix':
        """
        Computes the inverse of the given matrix by splitting it into 4 sub-matrices.
        
        Parameters:
            m (RealMatrix): Matrix whose inverse must be computed.
            splitIndex (int): Index that determines the "split" line and column. The element corresponding to this index will part of the upper-left
                sub-matrix.
        
        Returns:
            the inverse of m.
        
        Raises:
            MathIllegalArgumentException: if m is not square.
        
        
        """
        ...
    @staticmethod
    def checkAdditionCompatible(left: AnyMatrix, right: AnyMatrix) -> None:
        """
        Check if matrices are addition compatible.
        
        Parameters:
            left (AnyMatrix): Left hand side matrix.
            right (AnyMatrix): Right hand side matrix.
        
        Raises:
            MathIllegalArgumentException: if the matrices are not addition compatible.
        
        
        """
        ...
    @staticmethod
    def checkColumnIndex(m: AnyMatrix, column: int) -> None:
        """
        Check if a column index is valid.
        
        Parameters:
            m (AnyMatrix): Matrix.
            column (int): Column index to check.
        
        Raises:
            MathIllegalArgumentException: if column is not a valid index.
        
        
        """
        ...
    @staticmethod
    def checkMatrixIndex(m: AnyMatrix, row: int, column: int) -> None:
        """
        Check if matrix indices are valid.
        
        Parameters:
            m (AnyMatrix): Matrix.
            row (int): Row index to check.
            column (int): Column index to check.
        
        Raises:
            MathIllegalArgumentException: if row or column is not a valid index.
        
        
        """
        ...
    @staticmethod
    def checkMultiplicationCompatible(left: AnyMatrix, right: AnyMatrix) -> None:
        """
        Check if matrices are multiplication compatible
        
        Parameters:
            left (AnyMatrix): Left hand side matrix.
            right (AnyMatrix): Right hand side matrix.
        
        Raises:
            MathIllegalArgumentException: if matrices are not multiplication compatible.
        
        
        """
        ...
    @staticmethod
    def checkRowIndex(m: AnyMatrix, row: int) -> None:
        """
        Check if a row index is valid.
        
        Parameters:
            m (AnyMatrix): Matrix.
            row (int): Row index to check.
        
        Raises:
            MathIllegalArgumentException: if row is not a valid index.
        
        
        """
        ...
    @staticmethod
    def checkSameColumnDimension(left: AnyMatrix, right: AnyMatrix) -> None:
        """
        Check if matrices have the same number of columns.
        
        Parameters:
            left (AnyMatrix): Left hand side matrix.
            right (AnyMatrix): Right hand side matrix.
        
        Raises:
            MathIllegalArgumentException: if matrices don't have the same number of columns.
        
        Since:
            1.3
        
        
        """
        ...
    @staticmethod
    def checkSameRowDimension(left: AnyMatrix, right: AnyMatrix) -> None:
        """
        Check if matrices have the same number of rows.
        
        Parameters:
            left (AnyMatrix): Left hand side matrix.
            right (AnyMatrix): Right hand side matrix.
        
        Raises:
            MathIllegalArgumentException: if matrices don't have the same number of rows.
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def checkSubMatrixIndex(anyMatrix: AnyMatrix, int: int, int2: int, int3: int, int4: int) -> None: ...
    @typing.overload
    @staticmethod
    def checkSubMatrixIndex(anyMatrix: AnyMatrix, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> None: ...
    @staticmethod
    def checkSubtractionCompatible(left: AnyMatrix, right: AnyMatrix) -> None:
        """
        Check if matrices are subtraction compatible
        
        Parameters:
            left (AnyMatrix): Left hand side matrix.
            right (AnyMatrix): Right hand side matrix.
        
        Raises:
            MathIllegalArgumentException: if the matrices are not addition compatible.
        
        
        """
        ...
    @staticmethod
    def checkSymmetric(matrix: 'RealMatrix', eps: float) -> None:
        """
        Checks whether a matrix is symmetric.
        
        Parameters:
            matrix (RealMatrix): Matrix to check.
            eps (double): Relative tolerance.
        
        Raises:
            MathIllegalArgumentException: if the matrix is not square.
            MathIllegalArgumentException: if the matrix is not symmetric.
        
        
        """
        ...
    _createColumnFieldMatrix__T = typing.TypeVar('_createColumnFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createColumnFieldMatrix(columnData: typing.Union[typing.List[_createColumnFieldMatrix__T], jpype.JArray]) -> 'FieldMatrix'[_createColumnFieldMatrix__T]:
        """
        Creates a column FieldMatrix using the data from the input array.
        
        Parameters:
            columnData (T[]): the input column data
        
        Returns:
            a columnData x 1 FieldMatrix
        
        Raises:
            MathIllegalArgumentException: if data is empty.
            NullArgumentException: if columnData is null.
        
        
        """
        ...
    @staticmethod
    def createColumnRealMatrix(columnData: typing.Union[typing.List[float], jpype.JArray]) -> 'RealMatrix':
        """
        Creates a column RealMatrix using the data from the input array.
        
        Parameters:
            columnData (double[]): the input column data
        
        Returns:
            a columnData x 1 RealMatrix
        
        Raises:
            MathIllegalArgumentException: if columnData is empty.
            NullArgumentException: if columnData is null.
        
        
        """
        ...
    _createFieldDiagonalMatrix__T = typing.TypeVar('_createFieldDiagonalMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createFieldDiagonalMatrix(diagonal: typing.Union[typing.List[_createFieldDiagonalMatrix__T], jpype.JArray]) -> 'FieldMatrix'[_createFieldDiagonalMatrix__T]:
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
    def createFieldIdentityMatrix(field: org.hipparchus.Field[_createFieldIdentityMatrix__T], dimension: int) -> 'FieldMatrix'[_createFieldIdentityMatrix__T]:
        """
        Returns dimension x dimension identity matrix.
        
        Parameters:
            field (Field<T> field): field to which the elements belong
            dimension (int): dimension of identity matrix to generate
        
        Returns:
            identity matrix
        
        Raises:
            IllegalArgumentException: if dimension is not positive
        
        
        """
        ...
    _createFieldMatrix_0__T = typing.TypeVar('_createFieldMatrix_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _createFieldMatrix_1__T = typing.TypeVar('_createFieldMatrix_1__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createFieldMatrix(field: org.hipparchus.Field[_createFieldMatrix_0__T], int: int, int2: int) -> 'FieldMatrix'[_createFieldMatrix_0__T]:
        """
        Returns a FieldMatrix with specified dimensions.
        
        The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a square matrix), a FieldMatrix instance is built. Above this threshold a BlockFieldMatrix instance is built.
        
        The matrix elements are all set to field.getZero().
        
        Parameters:
            field (Field<T> field): field to which the matrix elements belong
            rows (int): number of rows of the matrix
            columns (int): number of columns of the matrix
        
        Returns:
            FieldMatrix with specified dimensions
        
              - createFieldMatrix
        
        public static <T extends FieldElement<T>> FieldMatrix<T> createFieldMatrix(T[][] data) throws MathIllegalArgumentException, NullArgumentException
        
        Returns a FieldMatrix whose entries are the the values in the the input array.
        
        The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a square matrix), a FieldMatrix instance is built. Above this threshold a BlockFieldMatrix instance is built.
        
        The input array is copied, not referenced.
        
        Parameters:
            data (T[][]): input array
        
        Returns:
            a matrix containing the values of the array.
        
        Raises:
            MathIllegalArgumentException: if data is not rectangular (not all rows have the same length).
            MathIllegalArgumentException: if a row or column is empty.
            NullArgumentException: if either data or data[0] is null.
        
              - createFieldMatrix
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createFieldMatrix(tArray: typing.Union[typing.List[typing.MutableSequence[_createFieldMatrix_1__T]], jpype.JArray]) -> 'FieldMatrix'[_createFieldMatrix_1__T]: ...
    _createFieldVector_0__T = typing.TypeVar('_createFieldVector_0__T', bound=org.hipparchus.FieldElement)  # <T>
    _createFieldVector_1__T = typing.TypeVar('_createFieldVector_1__T', bound=org.hipparchus.FieldElement)  # <T>
    @typing.overload
    @staticmethod
    def createFieldVector(field: org.hipparchus.Field[_createFieldVector_0__T], dimension: int) -> FieldVector[_createFieldVector_0__T]:
        """
        Creates a FieldVector with specified dimensions.
        
        Parameters:
            field (Field<T> field): field to which array elements belong
            dimension (int): dimension of the vector
        
        Returns:
            a new vector
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createFieldVector(tArray: typing.Union[typing.List[_createFieldVector_1__T], jpype.JArray]) -> FieldVector[_createFieldVector_1__T]: ...
    @staticmethod
    def createRealDiagonalMatrix(diagonal: typing.Union[typing.List[float], jpype.JArray]) -> 'RealMatrix':
        """
        Returns a diagonal matrix with specified elements.
        
        Parameters:
            diagonal (double[]): diagonal elements of the matrix (the array elements will be copied)
        
        Returns:
            diagonal matrix
        
        
        """
        ...
    @staticmethod
    def createRealIdentityMatrix(dimension: int) -> 'RealMatrix':
        """
        Returns dimension x dimension identity matrix.
        
        Parameters:
            dimension (int): dimension of identity matrix to generate
        
        Returns:
            identity matrix
        
        Raises:
            IllegalArgumentException: if dimension is not positive
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealMatrix(doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> 'RealMatrix':
        """
        Returns a RealMatrix with specified dimensions.
        
        The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a square matrix) which can be stored in a 32kB array, a Array2DRowRealMatrix instance is built. Above this threshold a BlockRealMatrix instance is built.
        
        The matrix elements are all set to 0.0.
        
        Parameters:
            rows (int): number of rows of the matrix
            columns (int): number of columns of the matrix
        
        Returns:
            RealMatrix with specified dimensions
        
              - createRealMatrix
        
        public static RealMatrix createRealMatrix(double[][] data) throws MathIllegalArgumentException, NullArgumentException
        
        Returns a RealMatrix whose entries are the the values in the the input array.
        
        The type of matrix returned depends on the dimension. Below 2 :sup:`12` elements (i.e. 4096 elements or 64×64 for a square matrix) which can be stored in a 32kB array, a Array2DRowRealMatrix instance is built. Above this threshold a BlockRealMatrix instance is built.
        
        The input array is copied, not referenced.
        
        Parameters:
            data (double[][]): input array
        
        Returns:
            RealMatrix containing the values of the array
        
        Raises:
            MathIllegalArgumentException: if data is not rectangular (not all rows have the same length).
            MathIllegalArgumentException: if a row or column is empty.
            NullArgumentException: if either data or data[0] is null.
            MathIllegalArgumentException: if data is not rectangular.
        
              - createRealMatrix
        
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def createRealMatrix(int: int, int2: int) -> 'RealMatrix': ...
    @typing.overload
    @staticmethod
    def createRealVector(dimension: typing.Union[typing.List[float], jpype.JArray]) -> 'RealVector':
        """
        Creates a RealVector with specified dimensions.
        
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
    def createRowFieldMatrix(rowData: typing.Union[typing.List[_createRowFieldMatrix__T], jpype.JArray]) -> 'FieldMatrix'[_createRowFieldMatrix__T]:
        """
        Create a row FieldMatrix using the data from the input array.
        
        Parameters:
            rowData (T[]): the input row data
        
        Returns:
            a 1 x rowData.length FieldMatrix
        
        Raises:
            MathIllegalArgumentException: if rowData is empty.
            NullArgumentException: if rowData is null.
        
        
        """
        ...
    @staticmethod
    def createRowRealMatrix(rowData: typing.Union[typing.List[float], jpype.JArray]) -> 'RealMatrix':
        """
        Create a row RealMatrix using the data from the input array.
        
        Parameters:
            rowData (double[]): the input row data
        
        Returns:
            a 1 x rowData.length RealMatrix
        
        Raises:
            MathIllegalArgumentException: if rowData is empty.
            NullArgumentException: if rowData is null.
        
        
        """
        ...
    @staticmethod
    def fractionMatrixToRealMatrix(m: 'FieldMatrix'[org.hipparchus.fraction.Fraction]) -> 'Array2DRowRealMatrix':
        """
        Convert a FieldMatrix/Fraction matrix to a RealMatrix.
        
        Parameters:
            m (FieldMatrix<Fraction> m): Matrix to convert.
        
        Returns:
            the converted matrix.
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def inverse(realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    @staticmethod
    def inverse(realMatrix: 'RealMatrix', double: float) -> 'RealMatrix': ...
    @staticmethod
    def isSymmetric(matrix: 'RealMatrix', eps: float) -> bool:
        """
        Checks whether a matrix is symmetric.
        
        Parameters:
            matrix (RealMatrix): Matrix to check.
            eps (double): Relative tolerance.
        
        Returns:
            true if matrix is symmetric.
        
        
        """
        ...
    @staticmethod
    def matrixExponential(rm: 'RealMatrix') -> 'RealMatrix':
        """
        Computes the MatrixExponential of the given matrix. The algorithm implementation follows the Pade approximant method of
        
        Higham, Nicholas J. “The Scaling and Squaring Method for the Matrix Exponential Revisited.” SIAM Journal on Matrix Analysis and Applications 26, no. 4 (January 2005): 1179–93.
        
        Parameters:
            rm (RealMatrix): RealMatrix whose inverse shall be computed
        
        Returns:
            The inverse of rm
        
        Raises:
            MathIllegalArgumentException: if matrix is not square
        
        
        """
        ...
    _orthonormalize_1__T = typing.TypeVar('_orthonormalize_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def orthonormalize(list: java.util.List['RealVector'], double: float, dependentVectorsHandler: DependentVectorsHandler) -> java.util.List['RealVector']: ...
    @typing.overload
    @staticmethod
    def orthonormalize(field: org.hipparchus.Field[_orthonormalize_1__T], list: java.util.List[FieldVector[_orthonormalize_1__T]], t: _orthonormalize_1__T, dependentVectorsHandler: DependentVectorsHandler) -> java.util.List[FieldVector[_orthonormalize_1__T]]: ...
    @staticmethod
    def solveLowerTriangularSystem(rm: 'RealMatrix', b: 'RealVector') -> None:
        """
        Solve a system of composed of a Lower Triangular Matrix RealMatrix.
        
        This method is called to solve systems of equations which are of the lower triangular form. The matrix RealMatrix is assumed, though not checked, to be in lower triangular form. The vector RealVector is overwritten with the solution. The matrix is checked that it is square and its dimensions match the length of the vector.
        
        Parameters:
            rm (RealMatrix): RealMatrix which is lower triangular
            b (RealVector): RealVector this is overwritten
        
        Raises:
            MathIllegalArgumentException: if the matrix and vector are not conformable
            MathIllegalArgumentException: if the matrix rm is not square
            MathRuntimeException: if the absolute value of one of the diagonal coefficient of rm is lower than
                SAFE_MIN
        
        
        """
        ...
    @staticmethod
    def solveUpperTriangularSystem(rm: 'RealMatrix', b: 'RealVector') -> None:
        """
        Solver a system composed of an Upper Triangular Matrix RealMatrix.
        
        This method is called to solve systems of equations which are of the lower triangular form. The matrix RealMatrix is assumed, though not checked, to be in upper triangular form. The vector RealVector is overwritten with the solution. The matrix is checked that it is square and its dimensions match the length of the vector.
        
        Parameters:
            rm (RealMatrix): RealMatrix which is upper triangular
            b (RealVector): RealVector this is overwritten
        
        Raises:
            MathIllegalArgumentException: if the matrix and vector are not conformable
            MathIllegalArgumentException: if the matrix rm is not square
            MathRuntimeException: if the absolute value of one of the diagonal coefficient of rm is lower than
                SAFE_MIN
        
        
        """
        ...

class QRDecomposition:
    """
    Calculates the QR-decomposition of a matrix.
    
    The QR-decomposition of a matrix A consists of two matrices Q and R that satisfy: A = QR, Q is orthogonal (Q :sup:`T` Q = I), and R is upper triangular. If A is m×n, Q is m×m and R m×n.
    
    This class compute the decomposition using Householder reflectors.
    
    For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows, which is much more cache-efficient in Java.
    
    This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
      - a getQT method has been added,
      - the solve and isFullRank methods have been replaced by a
        getSolver method and the equivalent methods provided by the returned
        DecompositionSolver.
    
    
          - `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getH(self) -> 'RealMatrix':
        """
        Returns the Householder reflector vectors.
        
        H is a lower trapezoidal matrix whose columns represent each successive Householder reflector vector. This matrix is used to compute Q.
        
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
        
        Least Square sense means a solver can be computed for an overdetermined system, (i.e. a system with more equations than unknowns, which corresponds to a tall A matrix with more rows than columns). In any case, if the matrix is singular within the tolerance set at , an error will be triggered when the solve method will be called.
        
        Returns:
            a solver
        
        
        """
        ...

class RealLinearOperator:
    """
    This class defines a linear operator operating on real (double) vector spaces. No direct access to the coefficients of the underlying matrix is provided.
    
    The motivation for such an interface is well stated by BARR1994: We restrict ourselves to iterative methods, which work by repeatedly improving an approximate solution until it is accurate enough. These methods access the coefficient matrix A of the linear system only via the matrix-vector product y = A · x (and perhaps z = A :sup:`T` · x). Thus the user need only supply a subroutine for computing y (and perhaps z) given x, which permits full exploitation of the sparsity or other special structure of A.
    
    Barret et al. (1994) R. Barrett, M. Berry, T. F. Chan, J. Demmel, J. M. Donato, J. Dongarra, V. Eijkhout, R. Pozo, C. Romine and H. Van der Vorst, Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods, SIAM
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
        Returns true if this operator supports operateTranspose.
        
        If true is returned, operateTranspose should not throw UnsupportedOperationException.
        
        The default implementation returns false.
        
        Returns:
            false
        
        
        """
        ...
    def operate(self, x: 'RealVector') -> 'RealVector':
        """
        Returns the result of multiplying this by the vector x.
        
        Parameters:
            x (RealVector): the vector to operate on
        
        Returns:
            the product of this instance with x
        
        Raises:
            MathIllegalArgumentException: if the column dimension does not match the size of x
        
        
        """
        ...
    def operateTranspose(self, x: 'RealVector') -> 'RealVector':
        """
        Returns the result of multiplying the transpose of this operator by the vector x (optional operation).
        
        The default implementation throws an UnsupportedOperationException. Users overriding this method must also override isTransposable.
        
        Parameters:
            x (RealVector): the vector to operate on
        
        Returns:
            the product of the transpose of this instance with x
        
        Raises:
            MathIllegalArgumentException: if the row dimension does not match the size of x
            UnsupportedOperationException: if this operation is not supported by this operator
        
        
        """
        ...

class RealMatrixChangingVisitor:
    """
    Interface defining a visitor for matrix entries.
    
          - DefaultRealMatrixChangingVisitor
    """
    def end(self) -> float:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
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
    def visit(self, row: int, column: int, value: float) -> float:
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
    Formats a nxm matrix in components list format "{{a :sub:`0` :sub:`0` ,a :sub:`0` :sub:`1` ..., a :sub:`0` :sub:`m-1` },{a :sub:`1` :sub:`0` , a :sub:`1` :sub:`1` ..., a :sub:`1` :sub:`m-1` },{...},{ a :sub:`n-1` :sub:`0` , a :sub:`n-1` :sub:`1` ..., a :sub:`n-1` :sub:`m-1` }}".
    
    The prefix and suffix "{" and "}", the row prefix and suffix "{" and "}", the row separator "," and the column separator "," can be replaced by any user-defined strings. The number format for components can be configured.
    
    White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the default separator does include a space character that is used at format time, both input string "{{1,1,1}}" and " { { 1 , 1 , 1 } } " will be parsed without error and the same matrix will be returned. In the second case, however, the parse position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
    
    Note: the grouping functionality of the used NumberFormat is disabled to prevent problems when parsing (e.g. 1,345.34 would be a valid number but conflicts with the default column separator).
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
        This method calls format.
        
        Parameters:
            m (RealMatrix): RealMatrix object to format.
        
        Returns:
            a formatted matrix.
        
        Formats a RealMatrix object to produce a string.
        
        Parameters:
            matrix (RealMatrix): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    def format(self, realMatrix: 'RealMatrix', stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
        Get the set of locales for which real vectors formats are available.
        
        This is the same set as the NumberFormat set.
        
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
        Parse a string to produce a RealMatrix object.
        
        Parameters:
            source (String): String to parse.
        
        Returns:
            the parsed RealMatrix object.
        
        Raises:
            MathIllegalStateException: if the beginning of the specified string cannot be parsed.
        
        Parse a string to produce a RealMatrix object.
        
        Parameters:
            source (String): String to parse.
            pos (ParsePosition): input/ouput parsing parameter.
        
        Returns:
            the parsed RealMatrix object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'RealMatrix': ...

class RealMatrixPreservingVisitor:
    """
    Interface defining a visitor for matrix entries.
    
          - DefaultRealMatrixPreservingVisitor
    """
    def end(self) -> float:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
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
    def visit(self, row: int, column: int, value: float) -> None:
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
    Class defining a real-valued vector with basic algebraic operations.
    
    vector element indexing is 0-based -- e.g., getEntry(0) returns the first element of the vector.
    
    The code map and mapToSelf methods operate on vectors element-wise, i.e. they perform the same operation (adding a scalar, applying a function ...) on each element in turn. The map versions create a new vector to hold the result and do not change the instance. The mapToSelf version uses the instance itself to store the results, so the instance is changed by this method. In all cases, the result vector is returned by the methods, allowing the fluent API style, like this:
    
    
       RealVector result = v.mapAddToSelf(3.4).mapToSelf(new Tan()).mapToSelf(new Power(2.3));
    """
    def add(self, v: 'RealVector') -> 'RealVector':
        """
        Compute the sum of this vector and v. Returns a new vector. Does not change instance data.
        
        Parameters:
            v (RealVector): Vector to be added.
        
        Returns:
            this + v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def addToEntry(self, index: int, increment: float) -> None:
        """
        Change an entry at the specified index.
        
        Parameters:
            index (int): Index location of entry to be set.
            increment (double): Value to add to the vector entry.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    @typing.overload
    def append(self, double: float) -> 'RealVector':
        """
        Construct a new vector by appending a vector to this vector.
        
        Parameters:
            v (RealVector): vector to append to this one.
        
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
    def combine(self, a: float, b: float, y: 'RealVector') -> 'RealVector':
        """
        Returns a new vector representing a * this + b * y, the linear combination of this and y. Returns a new vector. Does not change instance data.
        
        Parameters:
            a (double): Coefficient of this.
            b (double): Coefficient of y.
            y (RealVector): Vector with which this is linearly combined.
        
        Returns:
            a vector containing a * this[i] + b * y[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if y is not the same size as this vector.
        
        
        """
        ...
    def combineToSelf(self, a: float, b: float, y: 'RealVector') -> 'RealVector':
        """
        Updates this with the linear combination of this and y.
        
        Parameters:
            a (double): Weight of this.
            b (double): Weight of y.
            y (RealVector): Vector with which this is linearly combined.
        
        Returns:
            this, with components equal to a * this[i] + b * y[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if y is not the same size as this vector.
        
        
        """
        ...
    def copy(self) -> 'RealVector':
        """
        Returns a (deep) copy of this vector.
        
        Returns:
            a vector copy.
        
        
        """
        ...
    def cosine(self, v: 'RealVector') -> float:
        """
        Computes the cosine of the angle between this vector and the argument.
        
        Parameters:
            v (RealVector): Vector.
        
        Returns:
            the cosine of the angle between this vector and v.
        
        Raises:
            MathRuntimeException: if this or v is the null vector
            MathIllegalArgumentException: if the dimensions of this and v do not match
        
        
        """
        ...
    def dotProduct(self, v: 'RealVector') -> float:
        """
        Compute the dot product of this vector with v.
        
        Parameters:
            v (RealVector): Vector with which dot product should be computed
        
        Returns:
            the scalar dot product between this instance and v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def ebeDivide(self, v: 'RealVector') -> 'RealVector':
        """
        Element-by-element division.
        
        Parameters:
            v (RealVector): Vector by which instance elements must be divided.
        
        Returns:
            a vector containing this[i] / v[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def ebeMultiply(self, v: 'RealVector') -> 'RealVector':
        """
        Element-by-element multiplication.
        
        Parameters:
            v (RealVector): Vector by which instance elements must be multiplied
        
        Returns:
            a vector containing this[i] * v[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are NaN, the two real vectors are considered to be equal. NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to NaN, the real vector is equal to a vector with all NaN coordinates.
        
        This method must be overriden by concrete subclasses of RealVector (the current implementation throws an exception).
        
        Overrides: equals in class Object
        
        Parameters:
            other (Object): Object to test for equality.
        
        Returns:
            true if two vector objects are equal, false if other is null, not an instance of
            RealVector, or not equal to this RealVector instance.
        
        Raises:
            MathRuntimeException: if this method is not overridden.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the size of the vector.
        
        Returns:
            the size of this vector.
        
        
        """
        ...
    def getDistance(self, v: 'RealVector') -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with the L :sub:`2` norm, i.e. the square root of the sum of element differences, or Euclidean distance.
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
              - getL1Distance
              - getLInfDistance
              - getNorm
        
        
        
        """
        ...
    def getEntry(self, index: int) -> float:
        """
        Return the entry at the specified index.
        
        Parameters:
            index (int): Index location of entry to be fetched.
        
        Returns:
            the vector entry at index.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - setEntry
        
        
        
        """
        ...
    def getL1Distance(self, v: 'RealVector') -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with L :sub:`1` norm, i.e. the sum of the absolute values of the elements differences.
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def getL1Norm(self) -> float:
        """
        Returns the L :sub:`1` norm of the vector.
        
        The L :sub:`1` norm is the sum of the absolute values of the elements.
        
        Returns:
            the norm.
        
              - getNorm
              - getLInfNorm
              - getL1Distance
        
        
        
        """
        ...
    def getLInfDistance(self, v: 'RealVector') -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with L :sub:`∞` norm, i.e. the max of the absolute values of element differences.
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
              - getDistance
              - getL1Distance
              - getLInfNorm
        
        
        
        """
        ...
    def getLInfNorm(self) -> float:
        """
        Returns the L :sub:`∞` norm of the vector.
        
        The L :sub:`∞` norm is the max of the absolute values of the elements.
        
        Returns:
            the norm.
        
              - getNorm
              - getL1Norm
              - getLInfDistance
        
        
        
        """
        ...
    def getMaxIndex(self) -> int:
        """
        Get the index of the maximum entry.
        
        Returns:
            the index of the maximum entry or -1 if vector length is 0 or all entries are NaN
        
        
        """
        ...
    def getMaxValue(self) -> float:
        """
        Get the value of the maximum entry.
        
        Returns:
            the value of the maximum entry or NaN if all entries are NaN.
        
        
        """
        ...
    def getMinIndex(self) -> int:
        """
        Get the index of the minimum entry.
        
        Returns:
            the index of the minimum entry or -1 if vector length is 0 or all entries are NaN.
        
        
        """
        ...
    def getMinValue(self) -> float:
        """
        Get the value of the minimum entry.
        
        Returns:
            the value of the minimum entry or NaN if all entries are NaN.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
        Returns the L :sub:`2` norm of the vector.
        
        The L :sub:`2` norm is the root of the sum of the squared elements.
        
        Returns:
            the norm.
        
              - getL1Norm
              - getLInfNorm
              - getDistance
        
        
        
        """
        ...
    def getSubVector(self, index: int, n: int) -> 'RealVector':
        """
        Get a subvector from consecutive elements.
        
        Parameters:
            index (int): index of first element.
            n (int): number of elements to be retrieved.
        
        Returns:
            a vector containing n elements.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
            MathIllegalArgumentException: if the number of elements is not positive.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        . This method must be overriden by concrete subclasses of RealVector (current implementation throws an exception).
        
        Overrides: hashCode in class Object
        
        Raises:
            MathRuntimeException: if this method is not overridden.
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Check whether any coordinate of this vector is infinite and none are NaN.
        
        Returns:
            true if any coordinate of this vector is infinite and none are NaN, false otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Check whether any coordinate of this vector is NaN.
        
        Returns:
            true if any coordinate of this vector is NaN, false otherwise.
        
        
        """
        ...
    def iterator(self) -> java.util.Iterator['RealVector.Entry']:
        """
        Generic dense iterator. Iteration is in increasing order of the vector index.
        
        Note: derived classes are required to return an Iterator that returns non-null Entry objects as long as hasNext returns true.
        
        Returns:
            a dense iterator.
        
        
        """
        ...
    def map(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> 'RealVector':
        """
        Acts as if implemented as:
        
        
          return copy().mapToSelf(function);
         
        Returns a new vector. Does not change instance data.
        
        Parameters:
            function (UnivariateFunction): Function to apply to each entry.
        
        Returns:
            a new vector.
        
        
        """
        ...
    def mapAdd(self, d: float) -> 'RealVector':
        """
        Add a value to each entry. Returns a new vector. Does not change instance data.
        
        Parameters:
            d (double): Value to be added to each entry.
        
        Returns:
            this + d.
        
        
        """
        ...
    def mapAddToSelf(self, d: float) -> 'RealVector':
        """
        Add a value to each entry. The instance is changed in-place.
        
        Parameters:
            d (double): Value to be added to each entry.
        
        Returns:
            this.
        
        
        """
        ...
    def mapDivide(self, d: float) -> 'RealVector':
        """
        Divide each entry by the argument. Returns a new vector. Does not change instance data.
        
        Parameters:
            d (double): Value to divide by.
        
        Returns:
            this / d.
        
        
        """
        ...
    def mapDivideToSelf(self, d: float) -> 'RealVector':
        """
        Divide each entry by the argument. The instance is changed in-place.
        
        Parameters:
            d (double): Value to divide by.
        
        Returns:
            this.
        
        
        """
        ...
    def mapMultiply(self, d: float) -> 'RealVector':
        """
        Multiply each entry by the argument. Returns a new vector. Does not change instance data.
        
        Parameters:
            d (double): Multiplication factor.
        
        Returns:
            this * d.
        
        
        """
        ...
    def mapMultiplyToSelf(self, d: float) -> 'RealVector':
        """
        Multiply each entry. The instance is changed in-place.
        
        Parameters:
            d (double): Multiplication factor.
        
        Returns:
            this.
        
        
        """
        ...
    def mapSubtract(self, d: float) -> 'RealVector':
        """
        Subtract a value from each entry. Returns a new vector. Does not change instance data.
        
        Parameters:
            d (double): Value to be subtracted.
        
        Returns:
            this - d.
        
        
        """
        ...
    def mapSubtractToSelf(self, d: float) -> 'RealVector':
        """
        Subtract a value from each entry. The instance is changed in-place.
        
        Parameters:
            d (double): Value to be subtracted.
        
        Returns:
            this.
        
        
        """
        ...
    def mapToSelf(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> 'RealVector':
        """
        Acts as if it is implemented as:
        
        
          Entry e = null;
          for(Iterator<Entry> it = iterator(); it.hasNext(); e = it.next()) {
              e.setValue(function.value(e.getValue()));
          }
         
        Entries of this vector are modified in-place by this method.
        
        Parameters:
            function (UnivariateFunction): Function to apply to each entry.
        
        Returns:
            a reference to this vector.
        
        
        """
        ...
    def outerProduct(self, v: 'RealVector') -> 'RealMatrix':
        """
        Compute the outer product.
        
        Parameters:
            v (RealVector): Vector with which outer product should be computed.
        
        Returns:
            the matrix outer product between this instance and v.
        
        
        """
        ...
    def projection(self, v: 'RealVector') -> 'RealVector':
        """
        Find the orthogonal projection of this vector onto another vector.
        
        Parameters:
            v (RealVector): vector onto which instance must be projected.
        
        Returns:
            projection of the instance onto v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
            MathRuntimeException: if this or v is the null vector
        
        
        """
        ...
    def set(self, value: float) -> None:
        """
        Set all elements to a single value.
        
        Parameters:
            value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, index: int, value: float) -> None:
        """
        Set a single element.
        
        Parameters:
            index (int): element index.
            value (double): new value for the element.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - getEntry
        
        
        
        """
        ...
    def setSubVector(self, index: int, v: 'RealVector') -> None:
        """
        Set a sequence of consecutive elements.
        
        Parameters:
            index (int): index of first element to be set.
            v (RealVector): vector containing the values to set.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    def sparseIterator(self) -> java.util.Iterator['RealVector.Entry']:
        """
        Create a sparse iterator over the vector, which may omit some entries. The ommitted entries are either exact zeroes (for dense implementations) or are the entries which are not stored (for real sparse vectors). No guarantees are made about order of iteration.
        
        Note: derived classes are required to return an Iterator that returns non-null Entry objects as long as hasNext returns true.
        
        Returns:
            a sparse iterator.
        
        
        """
        ...
    def subtract(self, v: 'RealVector') -> 'RealVector':
        """
        Subtract v from this vector. Returns a new vector. Does not change instance data.
        
        Parameters:
            v (RealVector): Vector to be subtracted.
        
        Returns:
            this - v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Convert the vector to an array of doubles. The array is independent from this vector data: the elements are copied.
        
        Returns:
            an array containing a copy of the vector elements.
        
        
        """
        ...
    def unitVector(self) -> 'RealVector':
        """
        Creates a unit vector pointing in the direction of this vector. The instance is not changed by this method.
        
        Returns:
            a unit vector pointing in direction of this vector.
        
        Raises:
            MathRuntimeException: if the norm is zero.
        
        
        """
        ...
    def unitize(self) -> None:
        """
        Converts this vector into a unit vector. The instance itself is changed by this method.
        
        Raises:
            MathRuntimeException: if the norm is zero.
        
        
        """
        ...
    @staticmethod
    def unmodifiableRealVector(v: 'RealVector') -> 'RealVector':
        """
        Returns an unmodifiable view of the specified vector. The returned vector has read-only access. An attempt to modify it will result in a MathRuntimeException. However, the returned vector is not immutable, since any modification of v will also change the returned view. For example, in the following piece of code
        
        
             RealVector v = new ArrayRealVector(2);
             RealVector w = RealVector.unmodifiableRealVector(v);
             v.setEntry(0, 1.2);
             v.setEntry(1, -3.4);
         
        the changes will be seen in the w view of v.
        
        Parameters:
            v (RealVector): Vector for which an unmodifiable view is to be returned.
        
        Returns:
            an unmodifiable view of v.
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: 'RealVectorChangingVisitor') -> float:
        """
        Parameters:
            visitor (RealVectorPreservingVisitor): the visitor to be used to process the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInDefaultOrder(RealVectorPreservingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (but does not alter) some entries of this vector in default order (increasing index).
        
        Parameters:
            visitor (RealVectorPreservingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        Visits (and possibly alters) all entries of this vector in default order (increasing index).
        
        Parameters:
            visitor (RealVectorChangingVisitor): the visitor to be used to process and modify the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInDefaultOrder(RealVectorChangingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (and possibly alters) some entries of this vector in default order (increasing index).
        
        Parameters:
            visitor (RealVectorChangingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        
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
        Visits (but does not alter) all entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class.
        
        Parameters:
            visitor (RealVectorPreservingVisitor): the visitor to be used to process the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInOptimizedOrder(RealVectorPreservingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (but does not alter) some entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class.
        
        Parameters:
            visitor (RealVectorPreservingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        Visits (and possibly alters) all entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class.
        
        Parameters:
            visitor (RealVectorChangingVisitor): the visitor to be used to process the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInOptimizedOrder(RealVectorChangingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (and possibly change) some entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class.
        
        Parameters:
            visitor (RealVectorChangingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        
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
    This interface defines a visitor for the entries of a vector. Visitors implementing this interface may alter the entries of the vector being visited.
    """
    def end(self) -> float:
        """
        End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
        Returns:
            the value returned by walkInDefaultOrder,
            walkInDefaultOrder,
            walkInOptimizedOrder or
            walkInOptimizedOrder
        
        
        """
        ...
    def start(self, dimension: int, start: int, end: int) -> None:
        """
        Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
        Parameters:
            dimension (int): the size of the vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, index: int, value: float) -> float:
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
    Formats a vector in components list format "{v0; v1; ...; vk-1}".
    
    The prefix and suffix "{" and "}" and the separator "; " can be replaced by any user-defined strings. The number format for components can be configured.
    
    White space is ignored at parse time, even if it is in the prefix, suffix or separator specifications. So even if the default separator does include a space character that is used at format time, both input string "{1;1;1}" and " { 1 ; 1 ; 1 } " will be parsed without error and the same vector will be returned. In the second case, however, the parse position after parsing will be just after the closing curly brace, i.e. just before the trailing space.
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
        This method calls format.
        
        Parameters:
            v (RealVector): RealVector object to format.
        
        Returns:
            a formatted vector.
        
        Formats a RealVector object to produce a string.
        
        Parameters:
            vector (RealVector): the object to format.
            toAppendTo (StringBuffer): where the text is to be appended
            pos (FieldPosition): On input: an alignment field, if desired. On output: the offsets of the alignment field
        
        Returns:
            the value passed in as toAppendTo.
        
        
        """
        ...
    @typing.overload
    def format(self, realVector: RealVector, stringBuffer: java.lang.StringBuffer, fieldPosition: java.text.FieldPosition) -> java.lang.StringBuffer: ...
    @staticmethod
    def getAvailableLocales() -> typing.MutableSequence[java.util.Locale]:
        """
        Get the set of locales for which real vectors formats are available.
        
        This is the same set as the NumberFormat set.
        
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
        Parse a string to produce a RealVector object.
        
        Parameters:
            source (String): String to parse.
        
        Returns:
            the parsed RealVector object.
        
        Raises:
            MathIllegalStateException: if the beginning of the specified string cannot be parsed.
        
        Parse a string to produce a RealVector object.
        
        Parameters:
            source (String): String to parse.
            pos (ParsePosition): input/ouput parsing parameter.
        
        Returns:
            the parsed RealVector object.
        
        
        """
        ...
    @typing.overload
    def parse(self, string: str, parsePosition: java.text.ParsePosition) -> 'ArrayRealVector': ...

class RealVectorPreservingVisitor:
    """
    This interface defines a visitor for the entries of a vector. Visitors implementing this interface do not alter the entries of the vector being visited.
    """
    def end(self) -> float:
        """
        End visiting a vector. This method is called once, after all entries of the vector have been visited.
        
        Returns:
            the value returned by walkInDefaultOrder,
            walkInDefaultOrder,
            walkInOptimizedOrder or
            walkInOptimizedOrder
        
        
        """
        ...
    def start(self, dimension: int, start: int, end: int) -> None:
        """
        Start visiting a vector. This method is called once, before any entry of the vector is visited.
        
        Parameters:
            dimension (int): the size of the vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        
        """
        ...
    def visit(self, index: int, value: float) -> None:
        """
        Visit one entry of the vector.
        
        Parameters:
            index (int): the index of the entry being visited
            value (double): the value of the entry being visited
        
        
        """
        ...

class RectangularCholeskyDecomposition:
    """
    Calculates the rectangular Cholesky decomposition of a matrix.
    
    The rectangular Cholesky decomposition of a real symmetric positive semidefinite matrix A consists of a rectangular matrix B with the same number of rows such that: A is almost equal to BB :sup:`T` , depending on a user-defined tolerance. In a sense, this is the square root of A.
    
    The difference with respect to the regular CholeskyDecomposition is that rows/columns may be permuted (hence the rectangular shape instead of the traditional triangular shape) and there is a threshold to ignore small diagonal elements. This is used for example to generate CorrelatedRandomVectorGenerator in a p-dimension subspace (p < n). In other words, it allows generating random vectors from a covariance matrix that is only positive semidefinite, and not positive definite.
    
    Rectangular Cholesky decomposition is not suited for solving linear systems, so it does not provide any DecompositionSolver.
    
          - `MathWorld <http://mathworld.wolfram.com/CholeskyDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/Cholesky_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getRank(self) -> int:
        """
        Get the rank of the symmetric positive semidefinite matrix. The r is the number of independent rows in the symmetric positive semidefinite matrix, it is also the number of columns of the rectangular matrix of the decomposition.
        
        Returns:
            r of the square matrix.
        
              - getRootMatrix
        
        
        
        """
        ...
    def getRootMatrix(self) -> 'RealMatrix':
        """
        Get the root of the covariance matrix. The root is the rectangular matrix B such that the covariance matrix is equal to BT``
        
        Returns:
            root of the square matrix
        
              - getRank
        
        
        
        """
        ...

class RiccatiEquationSolver:
    """
    An algebraic Riccati equation is a type of nonlinear equation that arises in the context of infinite-horizon optimal control problems in continuous time or discrete time. The continuous time algebraic Riccati equation (CARE): \[ A^{T}X+XA-XBR^{-1}B^{T}X+Q=0 \} And the respective linear controller is: \[ K = R^{-1}B^{T}P \] A solver receives A, B, Q and R and computes P and K.
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

class SchurTransformer:
    """
    Class transforming a general real matrix to Schur form.
    
    A m × m matrix A can be written as the product of three matrices: A = P × T × P :sup:`T` with P an orthogonal matrix and T an quasi-triangular matrix. Both P and T are m × m matrices.
    
    Transformation to Schur form is often not a goal by itself, but it is an intermediate step in more general decomposition algorithms like EigenDecompositionSymmetric. This class is therefore intended for expert use. As a consequence of this explicitly limited scope, many methods directly returns references to internal arrays, not copies.
    
    This class is based on the method hqr2 in class EigenvalueDecomposition from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library.
    
          - `Schur Decomposition - MathWorld <http://mathworld.wolfram.com/SchurDecomposition.html>`
          - `Schur Decomposition - Wikipedia <http://en.wikipedia.org/wiki/Schur_decomposition>`
          - `Householder Transformations <http://en.wikipedia.org/wiki/Householder_transformation>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getP(self) -> 'RealMatrix':
        """
        Returns the matrix P of the transform.
        
        P is an orthogonal matrix, i.e. its inverse is also its transpose.
        
        Returns:
            the P matrix
        
        
        """
        ...
    def getPT(self) -> 'RealMatrix':
        """
        Returns the transpose of the matrix P of the transform.
        
        P is an orthogonal matrix, i.e. its inverse is also its transpose.
        
        Returns:
            the transpose of the P matrix
        
        
        """
        ...
    def getT(self) -> 'RealMatrix':
        """
        Returns the quasi-triangular Schur matrix T of the transform.
        
        Returns:
            the T matrix
        
        
        """
        ...

class SemiDefinitePositiveCholeskyDecomposition:
    """
    Calculates the Cholesky decomposition of a positive semidefinite matrix.
    
    The classic Cholesky decomposition (CholeskyDecomposition) applies to real symmetric positive-definite matrix. This class extends the Cholesky decomposition to positive semidefinite matrix. The main application is for estimation based on the Unscented Kalman Filter.
    
    Since:
        2.2
    
          - "J. Hartikainen, A. Solin, and S. Särkkä. Optimal ﬁltering with Kalman ﬁlters and smoothers, Dept. of Biomedica
            Engineering and Computational Sciences, Aalto University School of Science, Aug. 2011."
    """
    POSITIVITY_THRESHOLD: typing.ClassVar[float] = ...
    """
    Default threshold below which elements are not considered positive.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
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

class SingularValueDecomposition:
    """
    Calculates the compact Singular Value Decomposition of a matrix.
    
    The Singular Value Decomposition of matrix A is a set of three matrices: U, Σ and V such that A = U × Σ × V :sup:`T` . Let A be a m × n matrix, then U is a m × p orthogonal matrix, Σ is a p × p diagonal matrix with positive or null elements, V is a p × n orthogonal matrix (hence V :sup:`T` is also orthogonal) where p=min(m,n).
    
    This class is similar to the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
      - the norm2 method which has been renamed as getNorm,
      - the cond method which has been renamed as
        getConditionNumber,
      - the rank method which has been renamed as getRank,
      - a getUT method has been added,
      - a getVT method has been added,
      - a getSolver method has been added,
      - a getCovariance method has been added.
    
    
          - `MathWorld <http://mathworld.wolfram.com/SingularValueDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/Singular_value_decomposition>`
    """
    def __init__(self, matrix: 'RealMatrix'):
        """
        Calculates the compact Singular Value Decomposition of the given matrix.
        
        Parameters:
            matrix (RealMatrix): Matrix to decompose.
        
        
        """
        ...
    def getConditionNumber(self) -> float:
        """
        Return the condition number of the matrix.
        
        Returns:
            condition number of the matrix
        
        
        """
        ...
    def getCovariance(self, minSingularValue: float) -> 'RealMatrix':
        """
        Returns the n × n covariance matrix.
        
        The covariance matrix is V × J × V :sup:`T` where J is the diagonal matrix of the inverse of the squares of the singular values.
        
        Parameters:
            minSingularValue (double): value below which singular values are ignored (a 0 or negative value implies all singular value will be used)
        
        Returns:
            covariance matrix
        
        Raises:
            IllegalArgumentException: if minSingularValue is larger than the largest singular value, meaning all singular values are ignored
        
        
        """
        ...
    def getInverseConditionNumber(self) -> float:
        """
        Computes the inverse of the condition number. In cases of rank deficiency, the getConditionNumber will become undefined.
        
        Returns:
            the inverse of the condition number.
        
        
        """
        ...
    def getNorm(self) -> float:
        """
        Returns the L :sub:`2` norm of the matrix.
        
        The L :sub:`2` norm is max(|A × u| :sub:`2` / |u| :sub:`2` ), where |.| :sub:`2` denotes the vectorial 2-norm (i.e. the traditional euclidian norm).
        
        Returns:
            norm
        
        
        """
        ...
    def getRank(self) -> int:
        """
        Return the effective numerical matrix rank.
        
        The effective numerical rank is the number of non-negligible singular values. The threshold used to identify non-negligible terms is max(m,n) × ulp(s :sub:`1` ) where ulp(s :sub:`1` ) is the least significant bit of the largest singular value.
        
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
    def getSingularValues(self) -> typing.MutableSequence[float]:
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
        
              - getUT
        
        
        
        """
        ...
    def getUT(self) -> 'RealMatrix':
        """
        Returns the transpose of the matrix U of the decomposition.
        
        U is an orthogonal matrix, i.e. its transpose is also its inverse.
        
        Returns:
            the U matrix (or null if decomposed matrix is singular)
        
              - getU
        
        
        
        """
        ...
    def getV(self) -> 'RealMatrix':
        """
        Returns the matrix V of the decomposition.
        
        V is an orthogonal matrix, i.e. its transpose is also its inverse.
        
        Returns:
            the V matrix (or null if decomposed matrix is singular)
        
              - getVT
        
        
        
        """
        ...
    def getVT(self) -> 'RealMatrix':
        """
        Returns the transpose of the matrix V of the decomposition.
        
        V is an orthogonal matrix, i.e. its transpose is also its inverse.
        
        Returns:
            the V matrix (or null if decomposed matrix is singular)
        
              - getV
        
        
        
        """
        ...

_ArrayFieldVector__T = typing.TypeVar('_ArrayFieldVector__T', bound=org.hipparchus.FieldElement)  # <T>
class ArrayFieldVector(FieldVector[_ArrayFieldVector__T], java.io.Serializable, typing.Generic[_ArrayFieldVector__T]):
    """
    implements FieldVector<T>, Serializable
    
    This class implements the FieldVector interface with a FieldElement array.
    
          - serialized
    """
    @typing.overload
    def __init__(self, int: int, t: _ArrayFieldVector__T): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], tArray2: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], tArray2: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray], fieldVector: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T], boolean: bool): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T]): ...
    @typing.overload
    def __init__(self, fieldVector: FieldVector[_ArrayFieldVector__T], tArray: typing.Union[typing.List[_ArrayFieldVector__T], jpype.JArray]): ...
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
    def copy(self) -> FieldVector[_ArrayFieldVector__T]:
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface FieldVector
        
        Returns:
            vector copy
        
        
        """
        ...
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
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two vectors.
        
        Overrides: equals in class Object
        
        Parameters:
            other (Object): Object to test for equality.
        
        Returns:
            true if two vector objects are equal, false otherwise.
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[_ArrayFieldVector__T]:
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
        
        Specified by: getDimension in interface FieldVector
        
        Returns:
            size
        
        
        """
        ...
    def getEntry(self, index: int) -> _ArrayFieldVector__T:
        """
        Returns the entry in the specified index.
        
        Specified by: getEntry in interface FieldVector
        
        Parameters:
            index (int): Index location of entry to be fetched.
        
        Returns:
            the vector entry at index.
        
              - setEntry
        
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_ArrayFieldVector__T]:
        """
        Get the type of field elements of the vector.
        
        Specified by: getField in interface FieldVector
        
        Returns:
            type of field elements of the vector
        
        
        """
        ...
    def getSubVector(self, index: int, n: int) -> FieldVector[_ArrayFieldVector__T]:
        """
        Get a subvector from consecutive elements.
        
        Specified by: getSubVector in interface FieldVector
        
        Parameters:
            index (int): index of first element.
            n (int): number of elements to be retrieved.
        
        Returns:
            a vector containing n elements.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
            MathIllegalArgumentException: if the number of elements if not positive.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Get a hashCode for the real vector.
        
        All NaN values have the same hash code.
        
        Overrides: hashCode in class Object
        
        Returns:
            a hash code value for this object
        
        
        """
        ...
    def mapAdd(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map an addition operation to each entry.
        
        Specified by: mapAdd in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to be added to each entry
        
        Returns:
            this + d
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapAddToSelf(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map an addition operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapAddToSelf in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to be added to each entry
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapDivide(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map a division operation to each entry.
        
        Specified by: mapDivide in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to divide all entries by
        
        Returns:
            this / d
        
        Raises:
            NullArgumentException: if d is null.
            MathRuntimeException: if d is zero.
        
        
        """
        ...
    def mapDivideToSelf(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map a division operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapDivideToSelf in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to divide all entries by
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
            MathRuntimeException: if d is zero.
        
        
        """
        ...
    def mapInv(self) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map the 1/x function to each entry.
        
        Specified by: mapInv in interface FieldVector
        
        Returns:
            a vector containing the result of applying the function to each entry.
        
        Raises:
            MathRuntimeException: if one of the entries is zero.
        
        
        """
        ...
    def mapInvToSelf(self) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map the 1/x function to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapInvToSelf in interface FieldVector
        
        Returns:
            for convenience, return this
        
        Raises:
            MathRuntimeException: if one of the entries is zero.
        
        
        """
        ...
    def mapMultiply(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map a multiplication operation to each entry.
        
        Specified by: mapMultiply in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to multiply all entries by
        
        Returns:
            this * d
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapMultiplyToSelf(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map a multiplication operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapMultiplyToSelf in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to multiply all entries by
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapSubtract(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map a subtraction operation to each entry.
        
        Specified by: mapSubtract in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to be subtracted to each entry
        
        Returns:
            this - d
        
        Raises:
            NullArgumentException: if d is null
        
        
        """
        ...
    def mapSubtractToSelf(self, d: _ArrayFieldVector__T) -> FieldVector[_ArrayFieldVector__T]:
        """
        Map a subtraction operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapSubtractToSelf in interface FieldVector
        
        Parameters:
            d (ArrayFieldVector): value to be subtracted to each entry
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null
        
        
        """
        ...
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
    def set(self, value: _ArrayFieldVector__T) -> None:
        """
        Set all elements to a single value.
        
        Specified by: set in interface FieldVector
        
        Parameters:
            value (ArrayFieldVector): single value to set for all elements
        
        
        """
        ...
    def setEntry(self, index: int, value: _ArrayFieldVector__T) -> None:
        """
        Set a single element.
        
        Specified by: setEntry in interface FieldVector
        
        Parameters:
            index (int): element index.
            value (ArrayFieldVector): new value for the element.
        
              - getEntry
        
        
        
        """
        ...
    def setSubVector(self, index: int, v: FieldVector[_ArrayFieldVector__T]) -> None:
        """
        Set a set of consecutive elements.
        
        Specified by: setSubVector in interface FieldVector
        
        Parameters:
            index (int): index of first element to be set.
            v (FieldVector<ArrayFieldVector> v): vector containing the values to set.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    @typing.overload
    def subtract(self, arrayFieldVector: 'ArrayFieldVector'[_ArrayFieldVector__T]) -> 'ArrayFieldVector'[_ArrayFieldVector__T]: ...
    @typing.overload
    def subtract(self, fieldVector: FieldVector[_ArrayFieldVector__T]) -> FieldVector[_ArrayFieldVector__T]: ...
    def toArray(self) -> typing.MutableSequence[_ArrayFieldVector__T]:
        """
        Convert the vector to a T array.
        
        The array is independent from vector data, it's elements are copied.
        
        Specified by: toArray in interface FieldVector
        
        Returns:
            array containing a copy of vector elements
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: toString in class Object
        
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
    implements Serializable
    
    This class implements the RealVector interface with a double array.
    
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], doubleArray2: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], int: int, int2: int): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', boolean: bool): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', arrayRealVector2: 'ArrayRealVector'): ...
    @typing.overload
    def __init__(self, arrayRealVector: 'ArrayRealVector', realVector: RealVector): ...
    @typing.overload
    def __init__(self, realVector: RealVector): ...
    @typing.overload
    def __init__(self, realVector: RealVector, arrayRealVector: 'ArrayRealVector'): ...
    def add(self, v: RealVector) -> 'ArrayRealVector':
        """
        Compute the sum of this vector and v. Returns a new vector. Does not change instance data.
        
        Overrides: add in class RealVector
        
        Parameters:
            v (RealVector): Vector to be added.
        
        Returns:
            this + v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def addToEntry(self, index: int, increment: float) -> None:
        """
        Change an entry at the specified index.
        
        Overrides: addToEntry in class RealVector
        
        Parameters:
            index (int): Index location of entry to be set.
            increment (double): Value to add to the vector entry.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    @typing.overload
    def append(self, arrayRealVector: 'ArrayRealVector') -> 'ArrayRealVector':
        """
        Construct a new vector by appending a vector to this vector.
        
        Specified by: append in class RealVector
        
        Parameters:
            v (RealVector): vector to append to this one.
        
        Returns:
            a new vector.
        
        Construct a vector by appending a vector to this vector.
        
        Parameters:
            v (ArrayRealVector): Vector to append to this one.
        
        Returns:
            a new vector.
        
        Construct a new vector by appending a double to this vector.
        
        Specified by: append in class RealVector
        
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
    def combine(self, a: float, b: float, y: RealVector) -> 'ArrayRealVector':
        """
        Returns a new vector representing a * this + b * y, the linear combination of this and y. Returns a new vector. Does not change instance data.
        
        Overrides: combine in class RealVector
        
        Parameters:
            a (double): Coefficient of this.
            b (double): Coefficient of y.
            y (RealVector): Vector with which this is linearly combined.
        
        Returns:
            a vector containing a * this[i] + b * y[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if y is not the same size as this vector.
        
        
        """
        ...
    def combineToSelf(self, a: float, b: float, y: RealVector) -> 'ArrayRealVector':
        """
        Updates this with the linear combination of this and y.
        
        Overrides: combineToSelf in class RealVector
        
        Parameters:
            a (double): Weight of this.
            b (double): Weight of y.
            y (RealVector): Vector with which this is linearly combined.
        
        Returns:
            this, with components equal to a * this[i] + b * y[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if y is not the same size as this vector.
        
        
        """
        ...
    def copy(self) -> 'ArrayRealVector':
        """
        Returns a (deep) copy of this vector.
        
        Specified by: copy in class RealVector
        
        Returns:
            a vector copy.
        
        
        """
        ...
    def dotProduct(self, v: RealVector) -> float:
        """
        Compute the dot product of this vector with v.
        
        Overrides: dotProduct in class RealVector
        
        Parameters:
            v (RealVector): Vector with which dot product should be computed
        
        Returns:
            the scalar dot product between this instance and v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def ebeDivide(self, v: RealVector) -> 'ArrayRealVector':
        """
        Element-by-element division.
        
        Specified by: ebeDivide in class RealVector
        
        Parameters:
            v (RealVector): Vector by which instance elements must be divided.
        
        Returns:
            a vector containing this[i] / v[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def ebeMultiply(self, v: RealVector) -> 'ArrayRealVector':
        """
        Element-by-element multiplication.
        
        Specified by: ebeMultiply in class RealVector
        
        Parameters:
            v (RealVector): Vector by which instance elements must be multiplied
        
        Returns:
            a vector containing this[i] * v[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def equals(self, other: typing.Any) -> bool:
        """
        Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are NaN, the two real vectors are considered to be equal. NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to NaN, the real vector is equal to a vector with all NaN coordinates.
        
        This method must be overriden by concrete subclasses of RealVector (the current implementation throws an exception).
        
        Overrides: equals in class RealVector
        
        Parameters:
            other (Object): Object to test for equality.
        
        Returns:
            true if two vector objects are equal, false if other is null, not an instance of
            RealVector, or not equal to this RealVector instance.
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[float]:
        """
        Get a reference to the underlying data array. This method does not make a fresh copy of the underlying data.
        
        Returns:
            the array of entries.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the size of the vector.
        
        Specified by: getDimension in class RealVector
        
        Returns:
            the size of this vector.
        
        
        """
        ...
    def getDistance(self, v: RealVector) -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with the L :sub:`2` norm, i.e. the square root of the sum of element differences, or Euclidean distance.
        
        Overrides: getDistance in class RealVector
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
              - getL1Distance
              - getLInfDistance
              - getNorm
        
        
        
        """
        ...
    def getEntry(self, index: int) -> float:
        """
        Return the entry at the specified index.
        
        Specified by: getEntry in class RealVector
        
        Parameters:
            index (int): Index location of entry to be fetched.
        
        Returns:
            the vector entry at index.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - setEntry
        
        
        
        """
        ...
    def getL1Distance(self, v: RealVector) -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with L :sub:`1` norm, i.e. the sum of the absolute values of the elements differences.
        
        Overrides: getL1Distance in class RealVector
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def getL1Norm(self) -> float:
        """
        Returns the L :sub:`1` norm of the vector.
        
        The L :sub:`1` norm is the sum of the absolute values of the elements.
        
        Overrides: getL1Norm in class RealVector
        
        Returns:
            the norm.
        
              - getNorm
              - getLInfNorm
              - getL1Distance
        
        
        
        """
        ...
    def getLInfDistance(self, v: RealVector) -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with L :sub:`∞` norm, i.e. the max of the absolute values of element differences.
        
        Overrides: getLInfDistance in class RealVector
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
              - getDistance
              - getL1Distance
              - getLInfNorm
        
        
        
        """
        ...
    def getLInfNorm(self) -> float:
        """
        Returns the L :sub:`∞` norm of the vector.
        
        The L :sub:`∞` norm is the max of the absolute values of the elements.
        
        Overrides: getLInfNorm in class RealVector
        
        Returns:
            the norm.
        
              - getNorm
              - getL1Norm
              - getLInfDistance
        
        
        
        """
        ...
    def getNorm(self) -> float:
        """
        Returns the L :sub:`2` norm of the vector.
        
        The L :sub:`2` norm is the root of the sum of the squared elements.
        
        Overrides: getNorm in class RealVector
        
        Returns:
            the norm.
        
              - getL1Norm
              - getLInfNorm
              - getDistance
        
        
        
        """
        ...
    def getSubVector(self, index: int, n: int) -> RealVector:
        """
        Get a subvector from consecutive elements.
        
        Specified by: getSubVector in class RealVector
        
        Parameters:
            index (int): index of first element.
            n (int): number of elements to be retrieved.
        
        Returns:
            a vector containing n elements.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
            MathIllegalArgumentException: if the number of elements is not positive.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        . This method must be overriden by concrete subclasses of RealVector (current implementation throws an exception). All NaN values have the same hash code.
        
        Overrides: hashCode in class RealVector
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Check whether any coordinate of this vector is infinite and none are NaN.
        
        Specified by: isInfinite in class RealVector
        
        Returns:
            true if any coordinate of this vector is infinite and none are NaN, false otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Check if any coordinate of this vector is NaN.
        
        Specified by: isNaN in class RealVector
        
        Returns:
            true if any coordinate of this vector is NaN, false otherwise.
        
        
        """
        ...
    def map(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> 'ArrayRealVector':
        """
        Acts as if implemented as:
        
        
          return copy().mapToSelf(function);
         
        Returns a new vector. Does not change instance data.
        
        Overrides: map in class RealVector
        
        Parameters:
            function (UnivariateFunction): Function to apply to each entry.
        
        Returns:
            a new vector.
        
        
        """
        ...
    def mapAddToSelf(self, d: float) -> RealVector:
        """
        Add a value to each entry. The instance is changed in-place.
        
        Overrides: mapAddToSelf in class RealVector
        
        Parameters:
            d (double): Value to be added to each entry.
        
        Returns:
            this.
        
        
        """
        ...
    def mapDivideToSelf(self, d: float) -> RealVector:
        """
        Divide each entry by the argument. The instance is changed in-place.
        
        Overrides: mapDivideToSelf in class RealVector
        
        Parameters:
            d (double): Value to divide by.
        
        Returns:
            this.
        
        
        """
        ...
    def mapMultiplyToSelf(self, d: float) -> RealVector:
        """
        Multiply each entry. The instance is changed in-place.
        
        Overrides: mapMultiplyToSelf in class RealVector
        
        Parameters:
            d (double): Multiplication factor.
        
        Returns:
            this.
        
        
        """
        ...
    def mapSubtractToSelf(self, d: float) -> RealVector:
        """
        Subtract a value from each entry. The instance is changed in-place.
        
        Overrides: mapSubtractToSelf in class RealVector
        
        Parameters:
            d (double): Value to be subtracted.
        
        Returns:
            this.
        
        
        """
        ...
    def mapToSelf(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> 'ArrayRealVector':
        """
        Acts as if it is implemented as:
        
        
          Entry e = null;
          for(Iterator<Entry> it = iterator(); it.hasNext(); e = it.next()) {
              e.setValue(function.value(e.getValue()));
          }
         
        Entries of this vector are modified in-place by this method.
        
        Overrides: mapToSelf in class RealVector
        
        Parameters:
            function (UnivariateFunction): Function to apply to each entry.
        
        Returns:
            a reference to this vector.
        
        
        """
        ...
    def outerProduct(self, v: RealVector) -> 'RealMatrix':
        """
        Compute the outer product.
        
        Overrides: outerProduct in class RealVector
        
        Parameters:
            v (RealVector): Vector with which outer product should be computed.
        
        Returns:
            the matrix outer product between this instance and v.
        
        
        """
        ...
    def set(self, value: float) -> None:
        """
        Set all elements to a single value.
        
        Overrides: set in class RealVector
        
        Parameters:
            value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, index: int, value: float) -> None:
        """
        Set a single element.
        
        Specified by: setEntry in class RealVector
        
        Parameters:
            index (int): element index.
            value (double): new value for the element.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - getEntry
        
        
        
        """
        ...
    @typing.overload
    def setSubVector(self, int: int, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> None: ...
    @typing.overload
    def setSubVector(self, int: int, realVector: RealVector) -> None: ...
    def subtract(self, v: RealVector) -> 'ArrayRealVector':
        """
        Subtract v from this vector. Returns a new vector. Does not change instance data.
        
        Overrides: subtract in class RealVector
        
        Parameters:
            v (RealVector): Vector to be subtracted.
        
        Returns:
            this - v.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Convert the vector to an array of doubles. The array is independent from this vector data: the elements are copied.
        
        Overrides: toArray in class RealVector
        
        Returns:
            an array containing a copy of the vector elements.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Overrides: toString in class Object
        
        
        """
        ...
    @typing.overload
    def walkInDefaultOrder(self, realVectorChangingVisitor: RealVectorChangingVisitor) -> float:
        """
        Overrides: walkInDefaultOrder in class RealVector
        
        Parameters:
            visitor (RealVectorPreservingVisitor): the visitor to be used to process the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInDefaultOrder(RealVectorPreservingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (but does not alter) some entries of this vector in default order (increasing index).
        
        Overrides: walkInDefaultOrder in class RealVector
        
        Parameters:
            visitor (RealVectorPreservingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        Visits (and possibly alters) all entries of this vector in default order (increasing index).
        
        Overrides: walkInDefaultOrder in class RealVector
        
        Parameters:
            visitor (RealVectorChangingVisitor): the visitor to be used to process and modify the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInDefaultOrder(RealVectorChangingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (and possibly alters) some entries of this vector in default order (increasing index).
        
        Overrides: walkInDefaultOrder in class RealVector
        
        Parameters:
            visitor (RealVectorChangingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        
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
        Visits (but does not alter) all entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class. In this implementation, the optimized order is the default order.
        
        Overrides: walkInOptimizedOrder in class RealVector
        
        Parameters:
            visitor (RealVectorPreservingVisitor): the visitor to be used to process the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInOptimizedOrder(RealVectorPreservingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (but does not alter) some entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class. In this implementation, the optimized order is the default order.
        
        Overrides: walkInOptimizedOrder in class RealVector
        
        Parameters:
            visitor (RealVectorPreservingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        Visits (and possibly alters) all entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class. In this implementation, the optimized order is the default order.
        
        Overrides: walkInOptimizedOrder in class RealVector
        
        Parameters:
            visitor (RealVectorChangingVisitor): the visitor to be used to process the entries of this vector
        
        Returns:
            the value returned by end at the end of the walk
        
        public double walkInOptimizedOrder(RealVectorChangingVisitor visitor, int start, int end) throws MathIllegalArgumentException
        
        Visits (and possibly change) some entries of this vector in optimized order. The order in which the entries are visited is selected so as to lead to the most efficient implementation; it might depend on the concrete implementation of this abstract class. In this implementation, the optimized order is the default order.
        
        Overrides: walkInOptimizedOrder in class RealVector
        
        Parameters:
            visitor (RealVectorChangingVisitor): visitor to be used to process the entries of this vector
            start (int): the index of the first entry to be visited
            end (int): the index of the last entry to be visited (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if end < start.
            MathIllegalArgumentException: if the indices are not valid.
        
        
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
    implements MatrixDecomposer
    
    Matrix decomposer using Cholseky decomposition.
    
    Since:
        1.3
    """
    def __init__(self, relativeSymmetryThreshold: float, absolutePositivityThreshold: float):
        """
        Creates a Cholesky decomposer with specify threshold for several matrices.
        
        Parameters:
            relativeSymmetryThreshold (double): threshold above which off-diagonal elements are considered too different and matrix not symmetric
            absolutePositivityThreshold (double): threshold below which diagonal elements are considered null and matrix not positive definite
        
        
        """
        ...
    def decompose(self, a: 'RealMatrix') -> DecompositionSolver:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Specified by: decompose in interface MatrixDecomposer
        
        Parameters:
            a (RealMatrix): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        
        """
        ...

_DefaultFieldMatrixChangingVisitor__T = typing.TypeVar('_DefaultFieldMatrixChangingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class DefaultFieldMatrixChangingVisitor(FieldMatrixChangingVisitor[_DefaultFieldMatrixChangingVisitor__T], typing.Generic[_DefaultFieldMatrixChangingVisitor__T]):
    """
    implements FieldMatrixChangingVisitor<T>
    
    Default implementation of the FieldMatrixChangingVisitor interface.
    
    This class is a convenience to create custom visitors without defining all methods. This class provides default implementations that do nothing.
    """
    def __init__(self, zero: _DefaultFieldMatrixChangingVisitor__T):
        """
        Build a new instance.
        
        Parameters:
            zero (DefaultFieldMatrixChangingVisitor): additive identity of the field
        
        
        """
        ...
    def end(self) -> _DefaultFieldMatrixChangingVisitor__T:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Specified by: end in interface FieldMatrixChangingVisitor
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
        """
        Start visiting a matrix.
        
        This method is called once before any entry of the matrix is visited.
        
        Specified by: start in interface FieldMatrixChangingVisitor
        
        Parameters:
            rows (int): number of rows of the matrix
            columns (int): number of columns of the matrix
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, row: int, column: int, value: _DefaultFieldMatrixChangingVisitor__T) -> _DefaultFieldMatrixChangingVisitor__T:
        """
        Visit one matrix entry.
        
        Specified by: visit in interface FieldMatrixChangingVisitor
        
        Parameters:
            row (int): row index of the entry
            column (int): column index of the entry
            value (DefaultFieldMatrixChangingVisitor): current value of the entry
        
        Returns:
            the new value to be set for the entry
        
        
        """
        ...

_DefaultFieldMatrixPreservingVisitor__T = typing.TypeVar('_DefaultFieldMatrixPreservingVisitor__T', bound=org.hipparchus.FieldElement)  # <T>
class DefaultFieldMatrixPreservingVisitor(FieldMatrixPreservingVisitor[_DefaultFieldMatrixPreservingVisitor__T], typing.Generic[_DefaultFieldMatrixPreservingVisitor__T]):
    """
    implements FieldMatrixPreservingVisitor<T>
    
    Default implementation of the FieldMatrixPreservingVisitor interface.
    
    This class is a convenience to create custom visitors without defining all methods. This class provides default implementations that do nothing.
    """
    def __init__(self, zero: _DefaultFieldMatrixPreservingVisitor__T):
        """
        Build a new instance.
        
        Parameters:
            zero (DefaultFieldMatrixPreservingVisitor): additive identity of the field
        
        
        """
        ...
    def end(self) -> _DefaultFieldMatrixPreservingVisitor__T:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Specified by: end in interface FieldMatrixPreservingVisitor
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
        """
        Start visiting a matrix.
        
        This method is called once before any entry of the matrix is visited.
        
        Specified by: start in interface FieldMatrixPreservingVisitor
        
        Parameters:
            rows (int): number of rows of the matrix
            columns (int): number of columns of the matrix
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, row: int, column: int, value: _DefaultFieldMatrixPreservingVisitor__T) -> None:
        """
        Visit one matrix entry.
        
        Specified by: visit in interface FieldMatrixPreservingVisitor
        
        Parameters:
            row (int): row index of the entry
            column (int): column index of the entry
            value (DefaultFieldMatrixPreservingVisitor): current value of the entry
        
        
        """
        ...

class DefaultIterativeLinearSolverEvent(IterativeLinearSolverEvent):
    """
    A default concrete implementation of the abstract class IterativeLinearSolverEvent.
    
          - serialized
    """
    @typing.overload
    def __init__(self, object: typing.Any, int: int, realVector: RealVector, realVector2: RealVector, double: float): ...
    @typing.overload
    def __init__(self, object: typing.Any, int: int, realVector: RealVector, realVector2: RealVector, realVector3: RealVector, double: float): ...
    def getNormOfResidual(self) -> float:
        """
        Returns the norm of the residual. The returned value is not required to be exact. Instead, the norm of the so-called updated residual (if available) should be returned. For example, the ConjugateGradient method computes a sequence of residuals, the norm of which is cheap to compute. However, due to accumulation of round-off errors, this residual might differ from the true residual after some iterations. See e.g. A. Greenbaum and Z. Strakos, Predicting the Behavior of Finite Precision Lanzos and Conjugate Gradient Computations, Technical Report 538, Department of Computer Science, New York University, 1991 (available `here <http://www.archive.org/details/predictingbehavi00gree>`).
        
        Specified by: getNormOfResidual in class IterativeLinearSolverEvent
        
        Returns:
            the norm of the residual, ||r||
        
        
        """
        ...
    def getResidual(self) -> RealVector:
        """
        Returns the residual. This is an optional operation, as all iterative linear solvers do not provide cheap estimate of the updated residual vector, in which case
        
          - this method should throw a MathRuntimeException,
          - providesResidual returns false.
        
        The default implementation throws a MathRuntimeException. If this method is overriden, then providesResidual should be overriden as well. This implementation throws a MathRuntimeException if no residual vector r was provided at construction time.
        
        Overrides: getResidual in class IterativeLinearSolverEvent
        
        Returns:
            the updated residual, r
        
        
        """
        ...
    def getRightHandSideVector(self) -> RealVector:
        """
        Returns the current right-hand side of the linear system to be solved. This method should return an unmodifiable view, or a deep copy of the actual right-hand side vector, in order not to compromise subsequent iterations of the source IterativeLinearSolver.
        
        Specified by: getRightHandSideVector in class IterativeLinearSolverEvent
        
        Returns:
            the right-hand side vector, b
        
        
        """
        ...
    def getSolution(self) -> RealVector:
        """
        Returns the current estimate of the solution to the linear system to be solved. This method should return an unmodifiable view, or a deep copy of the actual current solution, in order not to compromise subsequent iterations of the source IterativeLinearSolver.
        
        Specified by: getSolution in class IterativeLinearSolverEvent
        
        Returns:
            the solution, x
        
        
        """
        ...
    def providesResidual(self) -> bool:
        """
        Returns true if getResidual is supported. The default implementation returns false. This implementation returns true if a non-null value was specified for the residual vector r at construction time.
        
        Overrides: providesResidual in class IterativeLinearSolverEvent
        
        Returns:
            true if r != null
        
        
        """
        ...

class DefaultRealMatrixChangingVisitor(RealMatrixChangingVisitor):
    """
    implements RealMatrixChangingVisitor
    
    Default implementation of the RealMatrixChangingVisitor interface.
    
    This class is a convenience to create custom visitors without defining all methods. This class provides default implementations that do nothing.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def end(self) -> float:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Specified by: end in interface RealMatrixChangingVisitor
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
        """
        Start visiting a matrix.
        
        This method is called once before any entry of the matrix is visited.
        
        Specified by: start in interface RealMatrixChangingVisitor
        
        Parameters:
            rows (int): number of rows of the matrix
            columns (int): number of columns of the matrix
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, row: int, column: int, value: float) -> float:
        """
        Visit one matrix entry.
        
        Specified by: visit in interface RealMatrixChangingVisitor
        
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
    implements RealMatrixPreservingVisitor
    
    Default implementation of the RealMatrixPreservingVisitor interface.
    
    This class is a convenience to create custom visitors without defining all methods. This class provides default implementations that do nothing.
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def end(self) -> float:
        """
        End visiting a matrix.
        
        This method is called once after all entries of the matrix have been visited.
        
        Specified by: end in interface RealMatrixPreservingVisitor
        
        Returns:
            the value that the walkInXxxOrder must return
        
        
        """
        ...
    def start(self, rows: int, columns: int, startRow: int, endRow: int, startColumn: int, endColumn: int) -> None:
        """
        Start visiting a matrix.
        
        This method is called once before any entry of the matrix is visited.
        
        Specified by: start in interface RealMatrixPreservingVisitor
        
        Parameters:
            rows (int): number of rows of the matrix
            columns (int): number of columns of the matrix
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        
        """
        ...
    def visit(self, row: int, column: int, value: float) -> None:
        """
        Visit one matrix entry.
        
        Specified by: visit in interface RealMatrixPreservingVisitor
        
        Parameters:
            row (int): row index of the entry
            column (int): column index of the entry
            value (double): current value of the entry
        
        
        """
        ...

_FieldLUDecomposer__T = typing.TypeVar('_FieldLUDecomposer__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldLUDecomposer(FieldMatrixDecomposer[_FieldLUDecomposer__T], typing.Generic[_FieldLUDecomposer__T]):
    """
    implements FieldMatrixDecomposer<T>
    
    Matrix decomposer using LU-decomposition.
    
    Since:
        2.2
    """
    def __init__(self, zeroChecker: typing.Union[java.util.function.Predicate[_FieldLUDecomposer__T], typing.Callable[[_FieldLUDecomposer__T], bool]]):
        """
        Creates a LU decomposer with specific zero checker for several matrices.
        
        Parameters:
            zeroChecker (Predicate<FieldLUDecomposer> zeroChecker): checker for zero elements
        
        
        """
        ...
    def decompose(self, a: 'FieldMatrix'[_FieldLUDecomposer__T]) -> FieldDecompositionSolver[_FieldLUDecomposer__T]:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Specified by: decompose in interface FieldMatrixDecomposer
        
        Parameters:
            a (FieldMatrix<FieldLUDecomposer> a): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        
        """
        ...

_FieldMatrix__T = typing.TypeVar('_FieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class FieldMatrix(AnyMatrix, org.hipparchus.util.FieldBlendable['FieldMatrix'[_FieldMatrix__T], _FieldMatrix__T], typing.Generic[_FieldMatrix__T]):
    """
    Interface defining field-valued matrix with basic algebraic operations.
    
    Matrix element indexing is 0-based -- e.g., getEntry(0, 0) returns the element in the first row, first column of the matrix.
    """
    def add(self, m: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Compute the sum of this and m.
        
        Parameters:
            m (FieldMatrix<FieldMatrix> m): Matrix to be added.
        
        Returns:
            this + m.
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this matrix.
        
        
        """
        ...
    def addToEntry(self, row: int, column: int, increment: _FieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            increment (FieldMatrix): Value to add to the current matrix entry in (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def blendArithmeticallyWith(self, other: 'FieldMatrix'[_FieldMatrix__T], blendingValue: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Blend arithmetically this instance with another one.
        
        Specified by: blendArithmeticallyWith in interface FieldBlendable
        
        Parameters:
            other (FieldMatrix<FieldMatrix> other): other instance to blend arithmetically with
            blendingValue (FieldMatrix): value from smoothstep function B(x). It is expected to be between [0:1] and will throw an exception otherwise.
        
        Returns:
            this * (1 - B(x)) + other * B(x)
        
        
        """
        ...
    def copy(self) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Make a (deep) copy of this.
        
        Returns:
            a copy of this matrix.
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, tArray: typing.Union[typing.List[typing.MutableSequence[_FieldMatrix__T]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], tArray: typing.Union[typing.List[typing.MutableSequence[_FieldMatrix__T]], jpype.JArray]) -> None: ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Create a new FieldMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def getColumn(self, column: int) -> typing.MutableSequence[_FieldMatrix__T]:
        """
        Get the entries in column number col as an array.
        
        Parameters:
            column (int): the column to be fetched
        
        Returns:
            array of entries in the column
        
        Raises:
            MathIllegalArgumentException: if the specified column index is not valid.
        
        
        """
        ...
    def getColumnMatrix(self, column: int) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Get the entries in column number column as a column matrix.
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getColumnVector(self, column: int) -> FieldVector[_FieldMatrix__T]:
        """
        Returns the entries in column number column as a vector.
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column vector.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_FieldMatrix__T]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Returns:
            a 2-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> _FieldMatrix__T:
        """
        Returns the entry in the specified row and column.
        
        Parameters:
            row (int): row location of entry to be fetched
            column (int): column location of entry to be fetched
        
        Returns:
            matrix entry in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_FieldMatrix__T]:
        """
        Get the type of field elements of the matrix.
        
        Returns:
            the type of field elements of the matrix.
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[_FieldMatrix__T]:
        """
        Get the entries in row number row as an array.
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowMatrix(self, row: int) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Get the entries in row number row as a row matrix.
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            a row matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    def getRowVector(self, row: int) -> FieldVector[_FieldMatrix__T]:
        """
        Get the entries in row number row as a vector.
        
        Parameters:
            row (int): Row to be fetched
        
        Returns:
            a row vector.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    def getTrace(self) -> _FieldMatrix__T:
        """
        Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main diagonal).
        
        Returns:
            trace
        
        Raises:
            MathIllegalArgumentException: if the matrix is not square.
        
        
        """
        ...
    def map(self, function: typing.Union[java.util.function.Function[_FieldMatrix__T, _FieldMatrix__T], typing.Callable[[_FieldMatrix__T], _FieldMatrix__T]]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Acts as if implemented as:
        
        
          return copy().mapToSelf(function);
         
        Returns a new matrix. Does not change instance data.
        
        Parameters:
            function (Function<FieldMatrix,FieldMatrix> function): Function to apply to each entry.
        
        Returns:
            a new matrix.
        
        Since:
            1.7
        
        
        """
        ...
    def mapToSelf(self, function: typing.Union[java.util.function.Function[_FieldMatrix__T, _FieldMatrix__T], typing.Callable[[_FieldMatrix__T], _FieldMatrix__T]]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Replace each entry by the result of applying the function to it.
        
        Parameters:
            function (Function<FieldMatrix,FieldMatrix> function): Function to apply to each entry.
        
        Returns:
            a reference to this matrix.
        
        Since:
            1.7
        
        
        """
        ...
    def multiply(self, m: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Postmultiply this matrix by m.
        
        Parameters:
            m (FieldMatrix<FieldMatrix> m): Matrix to postmultiply by.
        
        Returns:
            this * m.
        
        Raises:
            MathIllegalArgumentException: if the number of columns of this matrix is not equal to the number of rows of matrix m.
        
        
        """
        ...
    def multiplyEntry(self, row: int, column: int, factor: _FieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            factor (FieldMatrix): Multiplication factor for the current matrix entry in (row,column)
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def multiplyTransposed(self, m: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Returns the result of postmultiplying this by m^T.
        
        This is equivalent to call multiply(m.transpose), but some implementations may avoid building the intermediate transposed matrix.
        
        Parameters:
            m (FieldMatrix<FieldMatrix> m): matrix to first transpose and second postmultiply by
        
        Returns:
            this * m^T
        
        Raises:
            MathIllegalArgumentException: if columnDimension(this) != columnDimension(m)
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_FieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_FieldMatrix__T]) -> FieldVector[_FieldMatrix__T]: ...
    def power(self, p: int) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Returns the result multiplying this with itself p times. Depending on the type of the field elements, T, instability for high powers might occur.
        
        Parameters:
            p (int): raise this to power p
        
        Returns:
            this^p
        
        Raises:
            MathIllegalArgumentException: if p < 0
            MathIllegalArgumentException: if this matrix is not square
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_FieldMatrix__T]) -> FieldVector[_FieldMatrix__T]: ...
    def scalarAdd(self, d: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Increment each entry of this matrix.
        
        Parameters:
            d (FieldMatrix): Value to be added to each entry.
        
        Returns:
            d + this.
        
        
        """
        ...
    def scalarMultiply(self, d: _FieldMatrix__T) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Multiply each entry by d.
        
        Parameters:
            d (FieldMatrix): Value to multiply all entries by.
        
        Returns:
            d * this.
        
        
        """
        ...
    def setColumn(self, column: int, array: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in column number column as a column matrix.
        
        Parameters:
            column (int): the column to be set
            array (FieldMatrix[]): column array (must have the same number of rows as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance column.
        
        
        """
        ...
    def setColumnMatrix(self, column: int, matrix: 'FieldMatrix'[_FieldMatrix__T]) -> None:
        """
        Set the entries in column number column as a column matrix.
        
        Parameters:
            column (int): Column to be set.
            matrix (FieldMatrix<FieldMatrix> matrix): column matrix (must have one column and the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the matrix dimensions do not match one instance column.
        
        
        """
        ...
    def setColumnVector(self, column: int, vector: FieldVector[_FieldMatrix__T]) -> None:
        """
        Set the entries in column number column as a vector.
        
        Parameters:
            column (int): Column to be set.
            vector (FieldVector<FieldMatrix> vector): Column vector (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match one instance column.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: _FieldMatrix__T) -> None:
        """
        Set the entry in the specified row and column.
        
        Parameters:
            row (int): row location of entry to be set
            column (int): column location of entry to be set
            value (FieldMatrix): matrix entry to be set in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[_FieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in row number row as a row matrix.
        
        Parameters:
            row (int): Row to be set.
            array (FieldMatrix[]): Row matrix (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance row.
        
        
        """
        ...
    def setRowMatrix(self, row: int, matrix: 'FieldMatrix'[_FieldMatrix__T]) -> None:
        """
        Set the entries in row number row as a row matrix.
        
        Parameters:
            row (int): Row to be set.
            matrix (FieldMatrix<FieldMatrix> matrix): Row matrix (must have one row and the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the matrix dimensions do not match one instance row.
        
        
        """
        ...
    def setRowVector(self, row: int, vector: FieldVector[_FieldMatrix__T]) -> None:
        """
        Set the entries in row number row as a vector.
        
        Parameters:
            row (int): Row to be set.
            vector (FieldVector<FieldMatrix> vector): row vector (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match one instance row.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[_FieldMatrix__T]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at (row, column) using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Parameters:
            subMatrix (FieldMatrix[][]): Array containing the submatrix replacement data.
            row (int): Row coordinate of the top-left element to be replaced.
            column (int): Column coordinate of the top-left element to be replaced.
        
        Raises:
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if a row or column of subMatrix is empty.
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length).
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
    def subtract(self, m: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Subtract m from this matrix.
        
        Parameters:
            m (FieldMatrix<FieldMatrix> m): Matrix to be subtracted.
        
        Returns:
            this - m.
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this matrix.
        
        
        """
        ...
    def transpose(self) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Returns the transpose of this matrix.
        
        Returns:
            transpose matrix
        
        
        """
        ...
    def transposeMultiply(self, m: 'FieldMatrix'[_FieldMatrix__T]) -> 'FieldMatrix'[_FieldMatrix__T]:
        """
        Returns the result of postmultiplying this^T by m.
        
        This is equivalent to call transpose.multiply, but some implementations may avoid building the intermediate transposed matrix.
        
        Parameters:
            m (FieldMatrix<FieldMatrix> m): matrix to postmultiply by
        
        Returns:
            this^T * m
        
        Raises:
            MathIllegalArgumentException: if columnDimension(this) != columnDimension(m)
        
        Since:
            1.3
        
        
        """
        ...
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

_FieldQRDecomposer__T = typing.TypeVar('_FieldQRDecomposer__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldQRDecomposer(FieldMatrixDecomposer[_FieldQRDecomposer__T], typing.Generic[_FieldQRDecomposer__T]):
    """
    implements FieldMatrixDecomposer<T>
    
    Matrix decomposer using QR-decomposition.
    
    Since:
        2.2
    """
    def __init__(self, singularityThreshold: _FieldQRDecomposer__T):
        """
        Creates a QR decomposer with specify threshold for several matrices.
        
        Parameters:
            singularityThreshold (FieldQRDecomposer): threshold (based on partial row norm) under which a matrix is considered singular
        
        
        """
        ...
    def decompose(self, a: FieldMatrix[_FieldQRDecomposer__T]) -> FieldDecompositionSolver[_FieldQRDecomposer__T]:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Specified by: decompose in interface FieldMatrixDecomposer
        
        Parameters:
            a (FieldMatrix<FieldQRDecomposer> a): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        
        """
        ...

class JacobiPreconditioner(RealLinearOperator):
    """
    implements RealLinearOperator
    
    This class implements the standard Jacobi (diagonal) preconditioner. For a matrix A :sub:`ij` , this preconditioner is M = diag(1 / A :sub:`11` , 1 / A :sub:`22` , …).
    """
    def __init__(self, diag: typing.Union[typing.List[float], jpype.JArray], deep: bool):
        """
        Creates a new instance of this class.
        
        Parameters:
            diag (double[]): the diagonal coefficients of the linear operator to be preconditioned
            deep (boolean): true if a deep copy of the above array should be performed
        
        
        """
        ...
    @staticmethod
    def create(a: RealLinearOperator) -> 'JacobiPreconditioner':
        """
        Creates a new instance of this class. This method extracts the diagonal coefficients of the specified linear operator. If a does not extend AbstractRealMatrix, then the coefficients of the underlying matrix are not accessible, coefficient extraction is made by matrix-vector products with the basis vectors (and might therefore take some time). With matrices, direct entry access is carried out.
        
        Parameters:
            a (RealLinearOperator): the linear operator for which the preconditioner should be built
        
        Returns:
            the diagonal preconditioner made of the inverse of the diagonal coefficients of the specified linear operator
        
        Raises:
            MathIllegalArgumentException: if a is not square
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the dimension of the domain of this operator.
        
        Specified by: getColumnDimension in interface RealLinearOperator
        
        Returns:
            the number of columns of the underlying matrix
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the dimension of the codomain of this operator.
        
        Specified by: getRowDimension in interface RealLinearOperator
        
        Returns:
            the number of rows of the underlying matrix
        
        
        """
        ...
    def operate(self, x: RealVector) -> RealVector:
        """
        Returns the result of multiplying this by the vector x.
        
        Specified by: operate in interface RealLinearOperator
        
        Parameters:
            x (RealVector): the vector to operate on
        
        Returns:
            the product of this instance with x
        
        
        """
        ...
    def sqrt(self) -> RealLinearOperator:
        """
        Returns the square root of this diagonal operator. More precisely, this method returns P = diag(1 / √A :sub:`11` , 1 / √A :sub:`22` , …).
        
        Returns:
            the square root of this preconditioner
        
        
        """
        ...

class LUDecomposer(MatrixDecomposer):
    """
    implements MatrixDecomposer
    
    Matrix decomposer using LU-decomposition.
    
    Since:
        1.3
    """
    def __init__(self, singularityThreshold: float):
        """
        Creates a LU decomposer with specify threshold for several matrices.
        
        Parameters:
            singularityThreshold (double): threshold (based on partial row norm) under which a matrix is considered singular
        
        
        """
        ...
    def decompose(self, a: 'RealMatrix') -> DecompositionSolver:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Specified by: decompose in interface MatrixDecomposer
        
        Parameters:
            a (RealMatrix): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        
        """
        ...

class OrderedComplexEigenDecomposition(ComplexEigenDecomposition):
    """
    Given a matrix A, it computes a complex eigen decomposition A = VDV^{T}. It ensures that eigen values in the diagonal of D are in ascending order.
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float, double3: float): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float, double2: float, double3: float, comparator: typing.Union[java.util.Comparator[org.hipparchus.complex.Complex], typing.Callable[[org.hipparchus.complex.Complex, org.hipparchus.complex.Complex], int]]): ...
    def getVT(self) -> FieldMatrix[org.hipparchus.complex.Complex]:
        """
        Getter VT.
        
        Overrides: getVT in class ComplexEigenDecomposition
        
        Returns:
            VT.
        
        
        """
        ...

class PreconditionedIterativeLinearSolver(IterativeLinearSolver):
    """
    This abstract class defines preconditioned iterative solvers. When A is ill-conditioned, instead of solving system A · x = b directly, it is preferable to solve either \[ (M \cdot A) \cdot x = M \cdot b \] (left preconditioning), or \[ (A \cdot M) \cdot y = b, \text{followed by} M \cdot y = x \]
    
    (right preconditioning), where M approximates in some way A :sup:`-1` , while matrix-vector products of the type \(M \cdot y\) remain comparatively easy to compute. In this library, M (not M :sup:`-1` !) is called the preconditioner.
    
    Concrete implementations of this abstract class must be provided with the preconditioner M, as a RealLinearOperator.
    """
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager):
        """
        Creates a new instance of this class, with default iteration manager.
        
        Parameters:
            maxIterations (int): the maximum number of iterations
        
        public PreconditionedIterativeLinearSolver(IterationManager manager) throws NullArgumentException
        
        Creates a new instance of this class, with custom iteration manager.
        
        Parameters:
            manager (IterationManager): the custom iteration manager
        
        Raises:
            NullArgumentException: if manager is null
        
        
        """
        ...
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
    implements MatrixDecomposer
    
    Matrix decomposer using QR-decomposition.
    
    Since:
        1.3
    """
    def __init__(self, singularityThreshold: float):
        """
        Creates a QR decomposer with specify threshold for several matrices.
        
        Parameters:
            singularityThreshold (double): threshold (based on partial row norm) under which a matrix is considered singular
        
        
        """
        ...
    def decompose(self, a: 'RealMatrix') -> DecompositionSolver:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Specified by: decompose in interface MatrixDecomposer
        
        Parameters:
            a (RealMatrix): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        
        """
        ...

class RRQRDecomposition(QRDecomposition):
    """
    Calculates the rank-revealing QR-decomposition of a matrix, with column pivoting.
    
    The rank-revealing QR-decomposition of a matrix A consists of three matrices Q, R and P such that AP=QR. Q is orthogonal (Q :sup:`T` Q = I), and R is upper triangular. If A is m×n, Q is m×m and R is m×n and P is n×n.
    
    QR decomposition with column pivoting produces a rank-revealing QR decomposition and the getRank method may be used to return the rank of the input matrix A.
    
    This class compute the decomposition using Householder reflectors.
    
    For efficiency purposes, the decomposition in packed form is transposed. This allows inner loop to iterate inside rows, which is much more cache-efficient in Java.
    
    This class is based on the class with similar name from the `JAMA <http://math.nist.gov/javanumerics/jama/>` library, with the following changes:
    
      - a getQT method has been added,
      - the solve and isFullRank methods have been replaced by a
        getSolver method and the equivalent methods provided by the returned
        DecompositionSolver.
    
    
          - `MathWorld <http://mathworld.wolfram.com/QRDecomposition.html>`
          - `Wikipedia <http://en.wikipedia.org/wiki/QR_decomposition>`
    """
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix'): ...
    @typing.overload
    def __init__(self, realMatrix: 'RealMatrix', double: float): ...
    def getP(self) -> 'RealMatrix':
        """
        Returns the pivot matrix, P, used in the QR Decomposition of matrix A such that AP = QR. If no pivoting is used in this decomposition then P is equal to the identity matrix.
        
        Returns:
            a permutation matrix.
        
        
        """
        ...
    def getRank(self, dropThreshold: float) -> int:
        """
        Return the effective numerical matrix rank.
        
        The effective numerical rank is the number of non-negligible singular values.
        
        This implementation looks at Frobenius norms of the sequence of bottom right submatrices. When a large fall in norm is seen, the rank is returned. The drop is computed as:
        
           (thisNorm/lastNorm) * rNorm < dropThreshold
        
        where thisNorm is the Frobenius norm of the current submatrix, lastNorm is the Frobenius norm of the previous submatrix, rNorm is is the Frobenius norm of the complete matrix
        
        Parameters:
            dropThreshold (double): threshold triggering rank computation
        
        Returns:
            effective numerical matrix rank
        
        
        """
        ...
    def getSolver(self) -> DecompositionSolver:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Least Square sense means a solver can be computed for an overdetermined system, (i.e. a system with more equations than unknowns, which corresponds to a tall A matrix with more rows than columns). In any case, if the matrix is singular within the tolerance set at , an error will be triggered when the solve method will be called.
        
        Overrides: getSolver in class QRDecomposition
        
        Returns:
            a solver
        
        
        """
        ...

class RealMatrix(AnyMatrix, org.hipparchus.util.Blendable['RealMatrix']):
    """
    Interface defining a real-valued matrix with basic algebraic operations.
    
    Matrix element indexing is 0-based -- e.g., getEntry(0, 0) returns the element in the first row, first column of the matrix.
    """
    def add(self, m: 'RealMatrix') -> 'RealMatrix':
        """
        Returns the sum of this and m.
        
        Parameters:
            m (RealMatrix): matrix to be added
        
        Returns:
            this + m
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this.
        
        
        """
        ...
    def addToEntry(self, row: int, column: int, increment: float) -> None:
        """
        Adds (in place) the specified value to the specified entry of this matrix. Row and column indices start at 0.
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            increment (double): value to add to the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def blendArithmeticallyWith(self, other: 'RealMatrix', blendingValue: float) -> 'RealMatrix':
        """
        Blend arithmetically this instance with another one.
        
        Specified by: blendArithmeticallyWith in interface Blendable
        
        Parameters:
            other (RealMatrix): other instance to blend arithmetically with
            blendingValue (double): value from smoothstep function B(x). It is expected to be between [0:1] and will throw an exception otherwise.
        
        Returns:
            this * (1 - B(x)) + other * B(x)
        
        
        """
        ...
    def copy(self) -> 'RealMatrix':
        """
        Returns a (deep) copy of this.
        
        Returns:
            matrix copy
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> 'RealMatrix':
        """
        Create a new RealMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def getColumn(self, column: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given column index as an array. Column indices start at 0.
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            the array of entries in the column.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is not valid.
        
        
        """
        ...
    def getColumnMatrix(self, column: int) -> 'RealMatrix':
        """
        Get the entries at the given column index as a column matrix. Column indices start at 0.
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            column Matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getColumnVector(self, column: int) -> RealVector:
        """
        Get the entries at the given column index as a vector. Column indices start at 0.
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column vector.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Returns:
            2-dimensional array of entries
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> float:
        """
        Get the entry in the specified row and column. Row and column indices start at 0.
        
        Parameters:
            row (int): Row index of entry to be fetched.
            column (int): Column index of entry to be fetched.
        
        Returns:
            the matrix entry at (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
        Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
        Returns:
            norm
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
        Returns the ` maximum absolute column sum norm <http://mathworld.wolfram.com/MaximumAbsoluteColumnSumNorm.html>` (L :sub:`1` ) of the matrix.
        
        Returns:
            norm
        
        
        """
        ...
    def getNormInfty(self) -> float:
        """
        Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` (L :sub:`∞` ) of the matrix.
        
        Returns:
            norm
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given row index. Row indices start at 0.
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            the array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowMatrix(self, row: int) -> 'RealMatrix':
        """
        Get the entries at the given row index as a row matrix. Row indices start at 0.
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            row Matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    def getRowVector(self, row: int) -> RealVector:
        """
        Returns the entries in row number row as a vector. Row indices start at 0.
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            a row vector.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'RealMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> 'RealMatrix': ...
    def getTrace(self) -> float:
        """
        Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main diagonal).
        
        Returns:
            the trace.
        
        Raises:
            MathIllegalArgumentException: if the matrix is not square.
        
        
        """
        ...
    def map(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> 'RealMatrix':
        """
        Acts as if implemented as:
        
        
          return copy().mapToSelf(function);
         
        Returns a new matrix. Does not change instance data.
        
        Parameters:
            function (UnivariateFunction): Function to apply to each entry.
        
        Returns:
            a new matrix.
        
        Since:
            1.7
        
        
        """
        ...
    def mapToSelf(self, function: typing.Union[org.hipparchus.analysis.UnivariateFunction, typing.Callable]) -> 'RealMatrix':
        """
        Replace each entry by the result of applying the function to it.
        
        Parameters:
            function (UnivariateFunction): Function to apply to each entry.
        
        Returns:
            a reference to this matrix.
        
        Since:
            1.7
        
        
        """
        ...
    def multiply(self, m: 'RealMatrix') -> 'RealMatrix':
        """
        Returns the result of postmultiplying this by m.
        
        Parameters:
            m (RealMatrix): matrix to postmultiply by
        
        Returns:
            this * m
        
        Raises:
            MathIllegalArgumentException: if columnDimension(this) != rowDimension(m)
        
        
        """
        ...
    def multiplyEntry(self, row: int, column: int, factor: float) -> None:
        """
        Multiplies (in place) the specified entry of this matrix by the specified value. Row and column indices start at 0.
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            factor (double): Multiplication factor for the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def multiplyTransposed(self, m: 'RealMatrix') -> 'RealMatrix':
        """
        Returns the result of postmultiplying this by m^T.
        
        This is equivalent to call multiply(m.transpose), but some implementations may avoid building the intermediate transposed matrix.
        
        Parameters:
            m (RealMatrix): matrix to first transpose and second postmultiply by
        
        Returns:
            this * m^T
        
        Raises:
            MathIllegalArgumentException: if columnDimension(this) != columnDimension(m)
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, p: int) -> 'RealMatrix':
        """
        Returns the result of multiplying this with itself p times. Depending on the underlying storage, instability for high powers might occur.
        
        Parameters:
            p (int): raise this to power p
        
        Returns:
            this^p
        
        Raises:
            MathIllegalArgumentException: if p < 0
            MathIllegalArgumentException: if the matrix is not square
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: 'RealMatrix') -> 'RealMatrix': ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, d: float) -> 'RealMatrix':
        """
        Returns the result of adding d to each entry of this.
        
        Parameters:
            d (double): value to be added to each entry
        
        Returns:
            d + this
        
        
        """
        ...
    def scalarMultiply(self, d: float) -> 'RealMatrix':
        """
        Returns the result of multiplying each entry of this by d.
        
        Parameters:
            d (double): value to multiply all entries by
        
        Returns:
            d * this
        
        
        """
        ...
    def setColumn(self, column: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified array. Column indices start at 0.
        
        Parameters:
            column (int): Column to be set.
            array (double[]): Column array to be copied (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the array length does not match the row dimension of this matrix.
        
        
        """
        ...
    def setColumnMatrix(self, column: int, matrix: 'RealMatrix') -> None:
        """
        Sets the specified column of this matrix to the entries of the specified column matrix. Column indices start at 0.
        
        Parameters:
            column (int): Column to be set.
            matrix (RealMatrix): Column matrix to be copied (must have one column and the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the column dimension of the matrix is not , or the row dimensions of this and matrix
                do not match.
        
        
        """
        ...
    def setColumnVector(self, column: int, vector: RealVector) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified vector. Column indices start at 0.
        
        Parameters:
            column (int): Column to be set.
            vector (RealVector): column vector to be copied (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match the row dimension of this matrix.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: float) -> None:
        """
        Set the entry in the specified row and column. Row and column indices start at 0.
        
        Parameters:
            row (int): Row index of entry to be set.
            column (int): Column index of entry to be set.
            value (double): the new value of the entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified array. Row indices start at 0.
        
        Parameters:
            row (int): Row to be set.
            array (double[]): Row matrix to be copied (must have the same number of columns as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array length does not match the column dimension of this matrix.
        
        
        """
        ...
    def setRowMatrix(self, row: int, matrix: 'RealMatrix') -> None:
        """
        Sets the specified row of this matrix to the entries of the specified row matrix. Row indices start at 0.
        
        Parameters:
            row (int): Row to be set.
            matrix (RealMatrix): Row matrix to be copied (must have one row and the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the row dimension of the matrix is not , or the column dimensions of this and matrix
                do not match.
        
        
        """
        ...
    def setRowVector(self, row: int, vector: RealVector) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified vector. Row indices start at 0.
        
        Parameters:
            row (int): Row to be set.
            vector (RealVector): row vector to be copied (must have the same number of column as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match the column dimension of this matrix.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at row, column using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Parameters:
            subMatrix (double[][]): array containing the submatrix replacement data
            row (int): row coordinate of the top, left element to be replaced
            column (int): column coordinate of the top, left element to be replaced
        
        Raises:
            MathIllegalArgumentException: if subMatrix is empty.
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length) or empty.
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
    def subtract(self, m: 'RealMatrix') -> 'RealMatrix':
        """
        Returns this minus m.
        
        Parameters:
            m (RealMatrix): matrix to be subtracted
        
        Returns:
            this - m
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this.
        
        
        """
        ...
    def transpose(self) -> 'RealMatrix':
        """
        Returns the transpose of this matrix.
        
        Returns:
            transpose matrix
        
        
        """
        ...
    def transposeMultiply(self, m: 'RealMatrix') -> 'RealMatrix':
        """
        Returns the result of postmultiplying this^T by m.
        
        This is equivalent to call transpose.multiply, but some implementations may avoid building the intermediate transposed matrix.
        
        Parameters:
            m (RealMatrix): matrix to postmultiply by
        
        Returns:
            this^T * m
        
        Raises:
            MathIllegalArgumentException: if columnDimension(this) != columnDimension(m)
        
        Since:
            1.3
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
        Visit (and possibly change) all matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        double walkInColumnOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        double walkInColumnOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        double walkInOptimizedOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        double walkInOptimizedOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        double walkInRowOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        double walkInRowOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
    implements RiccatiEquationSolver
    
    This solver computes the solution using the following approach: 1. Compute the Hamiltonian matrix 2. Extract its complex eigen vectors (not the best solution, a better solution would be ordered Schur transformation) 3. Approximate the initial solution given by 2 using the Kleinman algorithm (an iterative method)
    """
    def __init__(self, A: RealMatrix, B: RealMatrix, Q: RealMatrix, R: RealMatrix):
        """
        Constructor of the solver. A and B should be compatible. B and R must be multiplicative compatible. A and Q must be multiplicative compatible. R must be invertible.
        
        Parameters:
            A (RealMatrix): state transition matrix
            B (RealMatrix): control multipliers matrix
            Q (RealMatrix): state cost matrix
            R (RealMatrix): control cost matrix
        
        
        """
        ...
    def getK(self) -> RealMatrix:
        """
        {inheritDoc}
        
        Specified by: getK in interface RiccatiEquationSolver
        
        Returns:
            the linear controller k
        
        
        """
        ...
    def getP(self) -> RealMatrix:
        """
        {inheritDoc}
        
        Specified by: getP in interface RiccatiEquationSolver
        
        Returns:
            the p
        
        
        """
        ...

class SingularValueDecomposer(MatrixDecomposer):
    """
    implements MatrixDecomposer
    
    Matrix decomposer using Singular Value Decomposition.
    
    Since:
        1.3
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            3.0
        
        
        """
        ...
    def decompose(self, a: RealMatrix) -> DecompositionSolver:
        """
        Get a solver for finding the A × X = B solution in least square sense.
        
        Specified by: decompose in interface MatrixDecomposer
        
        Parameters:
            a (RealMatrix): coefficient matrix A to decompose
        
        Returns:
            a solver
        
        
        """
        ...

_SparseFieldVector__T = typing.TypeVar('_SparseFieldVector__T', bound=org.hipparchus.FieldElement)  # <T>
class SparseFieldVector(FieldVector[_SparseFieldVector__T], java.io.Serializable, typing.Generic[_SparseFieldVector__T]):
    """
    implements FieldVector<T>, Serializable
    
    This class implements the FieldVector interface with a OpenIntToFieldHashMap backing store.
    
    Caveat: This implementation assumes that, for any x, the equality x * 0d == 0d holds. But it is is not true for NaN. Moreover, zero entries will lose their sign. Some operations (that involve NaN and/or infinities) may thus give incorrect results.
    
          - serialized
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T], int: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldVector__T], tArray: typing.Union[typing.List[_SparseFieldVector__T], jpype.JArray]): ...
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
    def copy(self) -> FieldVector[_SparseFieldVector__T]:
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface FieldVector
        
        Returns:
            vector copy
        
        
        """
        ...
    def dotProduct(self, v: FieldVector[_SparseFieldVector__T]) -> _SparseFieldVector__T:
        """
        Compute the dot product.
        
        Specified by: dotProduct in interface FieldVector
        
        Parameters:
            v (FieldVector<SparseFieldVector> v): vector with which dot product should be computed
        
        Returns:
            the scalar dot product of this and v
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
        
        
        """
        ...
    def ebeDivide(self, v: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]:
        """
        Element-by-element division.
        
        Specified by: ebeDivide in interface FieldVector
        
        Parameters:
            v (FieldVector<SparseFieldVector> v): vector by which instance elements must be divided
        
        Returns:
            a vector containing this[i] / v[i] for all i
        
        Raises:
            MathRuntimeException: if one entry of v is zero.
        
        
        """
        ...
    def ebeMultiply(self, v: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]:
        """
        Element-by-element multiplication.
        
        Specified by: ebeMultiply in interface FieldVector
        
        Parameters:
            v (FieldVector<SparseFieldVector> v): vector by which instance elements must be multiplied
        
        Returns:
            a vector containing this[i] * v[i] for all i
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Overrides: equals in class Object
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the size of the vector.
        
        Specified by: getDimension in interface FieldVector
        
        Returns:
            size
        
        
        """
        ...
    def getEntry(self, index: int) -> _SparseFieldVector__T:
        """
        Returns the entry in the specified index.
        
        Specified by: getEntry in interface FieldVector
        
        Parameters:
            index (int): Index location of entry to be fetched.
        
        Returns:
            the vector entry at index.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - setEntry
        
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_SparseFieldVector__T]:
        """
        Get the type of field elements of the vector.
        
        Specified by: getField in interface FieldVector
        
        Returns:
            type of field elements of the vector
        
        
        """
        ...
    def getSubVector(self, index: int, n: int) -> FieldVector[_SparseFieldVector__T]:
        """
        Get a subvector from consecutive elements.
        
        Specified by: getSubVector in interface FieldVector
        
        Parameters:
            index (int): index of first element.
            n (int): number of elements to be retrieved.
        
        Returns:
            a vector containing n elements.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
            MathIllegalArgumentException: if the number of elements if not positive.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Overrides: hashCode in class Object
        
        
        """
        ...
    def mapAdd(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map an addition operation to each entry.
        
        Specified by: mapAdd in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to be added to each entry
        
        Returns:
            this + d
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapAddToSelf(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map an addition operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapAddToSelf in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to be added to each entry
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapDivide(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map a division operation to each entry.
        
        Specified by: mapDivide in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to divide all entries by
        
        Returns:
            this / d
        
        Raises:
            NullArgumentException: if d is null.
            MathRuntimeException: if d is zero.
        
        
        """
        ...
    def mapDivideToSelf(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map a division operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapDivideToSelf in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to divide all entries by
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
            MathRuntimeException: if d is zero.
        
        
        """
        ...
    def mapInv(self) -> FieldVector[_SparseFieldVector__T]:
        """
        Map the 1/x function to each entry.
        
        Specified by: mapInv in interface FieldVector
        
        Returns:
            a vector containing the result of applying the function to each entry.
        
        Raises:
            MathRuntimeException: if one of the entries is zero.
        
        
        """
        ...
    def mapInvToSelf(self) -> FieldVector[_SparseFieldVector__T]:
        """
        Map the 1/x function to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapInvToSelf in interface FieldVector
        
        Returns:
            for convenience, return this
        
        Raises:
            MathRuntimeException: if one of the entries is zero.
        
        
        """
        ...
    def mapMultiply(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map a multiplication operation to each entry.
        
        Specified by: mapMultiply in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to multiply all entries by
        
        Returns:
            this * d
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapMultiplyToSelf(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map a multiplication operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapMultiplyToSelf in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to multiply all entries by
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null.
        
        
        """
        ...
    def mapSubtract(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map a subtraction operation to each entry.
        
        Specified by: mapSubtract in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to be subtracted to each entry
        
        Returns:
            this - d
        
        Raises:
            NullArgumentException: if d is null
        
        
        """
        ...
    def mapSubtractToSelf(self, d: _SparseFieldVector__T) -> FieldVector[_SparseFieldVector__T]:
        """
        Map a subtraction operation to each entry.
        
        The instance is changed by this method.
        
        Specified by: mapSubtractToSelf in interface FieldVector
        
        Parameters:
            d (SparseFieldVector): value to be subtracted to each entry
        
        Returns:
            for convenience, return this
        
        Raises:
            NullArgumentException: if d is null
        
        
        """
        ...
    @typing.overload
    def outerProduct(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldMatrix[_SparseFieldVector__T]: ...
    @typing.overload
    def outerProduct(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]) -> FieldMatrix[_SparseFieldVector__T]: ...
    def projection(self, v: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]:
        """
        Find the orthogonal projection of this vector onto another vector.
        
        Specified by: projection in interface FieldVector
        
        Parameters:
            v (FieldVector<SparseFieldVector> v): vector onto which this must be projected
        
        Returns:
            projection of this onto v
        
        Raises:
            MathRuntimeException: if v is the null vector.
        
        
        """
        ...
    def set(self, value: _SparseFieldVector__T) -> None:
        """
        Set all elements to a single value.
        
        Specified by: set in interface FieldVector
        
        Parameters:
            value (SparseFieldVector): single value to set for all elements
        
        Raises:
            NullArgumentException: if value is null
        
        
        """
        ...
    def setEntry(self, index: int, value: _SparseFieldVector__T) -> None:
        """
        Set a single element.
        
        Specified by: setEntry in interface FieldVector
        
        Parameters:
            index (int): element index.
            value (SparseFieldVector): new value for the element.
        
        Raises:
            NullArgumentException: if value is null
            MathIllegalArgumentException: if the index is not valid.
        
              - getEntry
        
        
        
        """
        ...
    def setSubVector(self, index: int, v: FieldVector[_SparseFieldVector__T]) -> None:
        """
        Set a set of consecutive elements.
        
        Specified by: setSubVector in interface FieldVector
        
        Parameters:
            index (int): index of first element to be set.
            v (FieldVector<SparseFieldVector> v): vector containing the values to set.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    @typing.overload
    def subtract(self, fieldVector: FieldVector[_SparseFieldVector__T]) -> FieldVector[_SparseFieldVector__T]: ...
    @typing.overload
    def subtract(self, sparseFieldVector: 'SparseFieldVector'[_SparseFieldVector__T]) -> 'SparseFieldVector'[_SparseFieldVector__T]: ...
    def toArray(self) -> typing.MutableSequence[_SparseFieldVector__T]:
        """
        Convert the vector to a T array.
        
        The array is independent from vector data, it's elements are copied.
        
        Specified by: toArray in interface FieldVector
        
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
    Marker class for RealVectors that require sparse backing storage
    
    Caveat: Implementation are allowed to assume that, for any x, the equality x * 0d == 0d holds. But it is is not true for NaN. Moreover, zero entries will lose their sign. Some operations (that involve NaN and/or infinities) may thus give incorrect results, like multiplications, divisions or functions mapping.
    """
    ...

_AbstractFieldMatrix__T = typing.TypeVar('_AbstractFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class AbstractFieldMatrix(FieldMatrix[_AbstractFieldMatrix__T], typing.Generic[_AbstractFieldMatrix__T]):
    """
    implements FieldMatrix<T>
    
    Basic implementation of FieldMatrix methods regardless of the underlying storage.
    
    All the methods implemented here use getEntry to access matrix elements. Derived class can provide faster implementations.
    """
    def add(self, m: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Compute the sum of this and m.
        
        Specified by: add in interface FieldMatrix
        
        Parameters:
            m (FieldMatrix<AbstractFieldMatrix> m): Matrix to be added.
        
        Returns:
            this + m.
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this matrix.
        
        
        """
        ...
    def addToEntry(self, row: int, column: int, increment: _AbstractFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: addToEntry in interface FieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            increment (AbstractFieldMatrix): Value to add to the current matrix entry in (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Make a (deep) copy of this.
        
        Specified by: copy in interface FieldMatrix
        
        Returns:
            a copy of this matrix.
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, tArray: typing.Union[typing.List[typing.MutableSequence[_AbstractFieldMatrix__T]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], tArray: typing.Union[typing.List[typing.MutableSequence[_AbstractFieldMatrix__T]], jpype.JArray]) -> None: ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Create a new FieldMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface FieldMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff object is a FieldMatrix instance with the same dimensions as this and all corresponding matrix entries are equal.
        
        Overrides: equals in class Object
        
        Parameters:
            object (Object): the object to test equality against.
        
        Returns:
            true if object equals this
        
        
        """
        ...
    def getColumn(self, column: int) -> typing.MutableSequence[_AbstractFieldMatrix__T]:
        """
        Get the entries in column number col as an array.
        
        Specified by: getColumn in interface FieldMatrix
        
        Parameters:
            column (int): the column to be fetched
        
        Returns:
            array of entries in the column
        
        Raises:
            MathIllegalArgumentException: if the specified column index is not valid.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns in the matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Returns:
            columnDimension
        
        
        """
        ...
    def getColumnMatrix(self, column: int) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Get the entries in column number column as a column matrix.
        
        Specified by: getColumnMatrix in interface FieldMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getColumnVector(self, column: int) -> FieldVector[_AbstractFieldMatrix__T]:
        """
        Returns the entries in column number column as a vector.
        
        Specified by: getColumnVector in interface FieldMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column vector.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_AbstractFieldMatrix__T]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface FieldMatrix
        
        Returns:
            a 2-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> _AbstractFieldMatrix__T:
        """
        Returns the entry in the specified row and column.
        
        Specified by: getEntry in interface FieldMatrix
        
        Parameters:
            row (int): row location of entry to be fetched
            column (int): column location of entry to be fetched
        
        Returns:
            matrix entry in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getField(self) -> org.hipparchus.Field[_AbstractFieldMatrix__T]:
        """
        Get the type of field elements of the matrix.
        
        Specified by: getField in interface FieldMatrix
        
        Returns:
            the type of field elements of the matrix.
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[_AbstractFieldMatrix__T]:
        """
        Get the entries in row number row as an array.
        
        Specified by: getRow in interface FieldMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows in the matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Returns:
            rowDimension
        
        
        """
        ...
    def getRowMatrix(self, row: int) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Get the entries in row number row as a row matrix.
        
        Specified by: getRowMatrix in interface FieldMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            a row matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    def getRowVector(self, row: int) -> FieldVector[_AbstractFieldMatrix__T]:
        """
        Get the entries in row number row as a vector.
        
        Specified by: getRowVector in interface FieldMatrix
        
        Parameters:
            row (int): Row to be fetched
        
        Returns:
            a row vector.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    def getTrace(self) -> _AbstractFieldMatrix__T:
        """
        Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main diagonal).
        
        Specified by: getTrace in interface FieldMatrix
        
        Returns:
            trace
        
        Raises:
            MathIllegalArgumentException: if the matrix is not square.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Computes a hashcode for the matrix.
        
        Overrides: hashCode in class Object
        
        Returns:
            hashcode for matrix
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
        Is this a square matrix?
        
        Specified by: isSquare in interface AnyMatrix
        
        Returns:
            true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...
    def multiply(self, m: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Postmultiply this matrix by m.
        
        Specified by: multiply in interface FieldMatrix
        
        Parameters:
            m (FieldMatrix<AbstractFieldMatrix> m): Matrix to postmultiply by.
        
        Returns:
            this * m.
        
        Raises:
            MathIllegalArgumentException: if the number of columns of this matrix is not equal to the number of rows of matrix m.
        
        
        """
        ...
    def multiplyEntry(self, row: int, column: int, factor: _AbstractFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: multiplyEntry in interface FieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            factor (AbstractFieldMatrix): Multiplication factor for the current matrix entry in (row,column)
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def power(self, p: int) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Returns the result multiplying this with itself p times. Depending on the type of the field elements, T, instability for high powers might occur.
        
        Specified by: power in interface FieldMatrix
        
        Parameters:
            p (int): raise this to power p
        
        Returns:
            this^p
        
        Raises:
            MathIllegalArgumentException: if p < 0
            MathIllegalArgumentException: if this matrix is not square
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_AbstractFieldMatrix__T]) -> FieldVector[_AbstractFieldMatrix__T]: ...
    def scalarAdd(self, d: _AbstractFieldMatrix__T) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Increment each entry of this matrix.
        
        Specified by: scalarAdd in interface FieldMatrix
        
        Parameters:
            d (AbstractFieldMatrix): Value to be added to each entry.
        
        Returns:
            d + this.
        
        
        """
        ...
    def scalarMultiply(self, d: _AbstractFieldMatrix__T) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Multiply each entry by d.
        
        Specified by: scalarMultiply in interface FieldMatrix
        
        Parameters:
            d (AbstractFieldMatrix): Value to multiply all entries by.
        
        Returns:
            d * this.
        
        
        """
        ...
    def setColumn(self, column: int, array: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in column number column as a column matrix.
        
        Specified by: setColumn in interface FieldMatrix
        
        Parameters:
            column (int): the column to be set
            array (AbstractFieldMatrix[]): column array (must have the same number of rows as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance column.
        
        
        """
        ...
    def setColumnMatrix(self, column: int, matrix: FieldMatrix[_AbstractFieldMatrix__T]) -> None:
        """
        Set the entries in column number column as a column matrix.
        
        Specified by: setColumnMatrix in interface FieldMatrix
        
        Parameters:
            column (int): Column to be set.
            matrix (FieldMatrix<AbstractFieldMatrix> matrix): column matrix (must have one column and the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the matrix dimensions do not match one instance column.
        
        
        """
        ...
    def setColumnVector(self, column: int, vector: FieldVector[_AbstractFieldMatrix__T]) -> None:
        """
        Set the entries in column number column as a vector.
        
        Specified by: setColumnVector in interface FieldMatrix
        
        Parameters:
            column (int): Column to be set.
            vector (FieldVector<AbstractFieldMatrix> vector): Column vector (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match one instance column.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: _AbstractFieldMatrix__T) -> None:
        """
        Set the entry in the specified row and column.
        
        Specified by: setEntry in interface FieldMatrix
        
        Parameters:
            row (int): row location of entry to be set
            column (int): column location of entry to be set
            value (AbstractFieldMatrix): matrix entry to be set in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[_AbstractFieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in row number row as a row matrix.
        
        Specified by: setRow in interface FieldMatrix
        
        Parameters:
            row (int): Row to be set.
            array (AbstractFieldMatrix[]): Row matrix (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance row.
        
        
        """
        ...
    def setRowMatrix(self, row: int, matrix: FieldMatrix[_AbstractFieldMatrix__T]) -> None:
        """
        Set the entries in row number row as a row matrix.
        
        Specified by: setRowMatrix in interface FieldMatrix
        
        Parameters:
            row (int): Row to be set.
            matrix (FieldMatrix<AbstractFieldMatrix> matrix): Row matrix (must have one row and the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the matrix dimensions do not match one instance row.
        
        
        """
        ...
    def setRowVector(self, row: int, vector: FieldVector[_AbstractFieldMatrix__T]) -> None:
        """
        Set the entries in row number row as a vector.
        
        Specified by: setRowVector in interface FieldMatrix
        
        Parameters:
            row (int): Row to be set.
            vector (FieldVector<AbstractFieldMatrix> vector): row vector (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match one instance row.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[_AbstractFieldMatrix__T]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at (row, column) using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Specified by: setSubMatrix in interface FieldMatrix
        
        Parameters:
            subMatrix (AbstractFieldMatrix[][]): Array containing the submatrix replacement data.
            row (int): Row coordinate of the top-left element to be replaced.
            column (int): Column coordinate of the top-left element to be replaced.
        
        Raises:
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if a row or column of subMatrix is empty.
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length).
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
    def subtract(self, m: FieldMatrix[_AbstractFieldMatrix__T]) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Subtract m from this matrix.
        
        Specified by: subtract in interface FieldMatrix
        
        Parameters:
            m (FieldMatrix<AbstractFieldMatrix> m): Matrix to be subtracted.
        
        Returns:
            this - m.
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this matrix.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get a string representation for this matrix.
        
        Overrides: toString in class Object
        
        Returns:
            a string representation for this matrix
        
        
        """
        ...
    def transpose(self) -> FieldMatrix[_AbstractFieldMatrix__T]:
        """
        Returns the transpose of this matrix.
        
        Specified by: transpose in interface FieldMatrix
        
        Returns:
            transpose matrix
        
        
        """
        ...
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
    implements RealMatrix, RealLinearOperator
    
    Basic implementation of RealMatrix methods regardless of the underlying storage.
    
    All the methods implemented here use getEntry to access matrix elements. Derived class can provide faster implementations.
    """
    def add(self, m: RealMatrix) -> RealMatrix:
        """
        Returns the sum of this and m.
        
        Specified by: add in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to be added
        
        Returns:
            this + m
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this.
        
        
        """
        ...
    def addToEntry(self, row: int, column: int, increment: float) -> None:
        """
        Adds (in place) the specified value to the specified entry of this matrix. Row and column indices start at 0.
        
        Specified by: addToEntry in interface RealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            increment (double): value to add to the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> RealMatrix:
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface RealMatrix
        
        Returns:
            matrix copy
        
        
        """
        ...
    @typing.overload
    def copySubMatrix(self, int: int, int2: int, int3: int, int4: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    @typing.overload
    def copySubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray], doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None: ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> RealMatrix:
        """
        Create a new RealMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface RealMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def equals(self, object: typing.Any) -> bool:
        """
        Returns true iff object is a RealMatrix instance with the same dimensions as this and all corresponding matrix entries are equal.
        
        Overrides: equals in class Object
        
        Parameters:
            object (Object): the object to test equality against.
        
        Returns:
            true if object equals this
        
        
        """
        ...
    def getColumn(self, column: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given column index as an array. Column indices start at 0.
        
        Specified by: getColumn in interface RealMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            the array of entries in the column.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is not valid.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns of this matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in interface RealLinearOperator
        
        Returns:
            the number of columns.
        
        
        """
        ...
    def getColumnMatrix(self, column: int) -> RealMatrix:
        """
        Get the entries at the given column index as a column matrix. Column indices start at 0.
        
        Specified by: getColumnMatrix in interface RealMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            column Matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getColumnVector(self, column: int) -> RealVector:
        """
        Get the entries at the given column index as a vector. Column indices start at 0.
        
        Specified by: getColumnVector in interface RealMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column vector.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface RealMatrix
        
        Returns:
            2-dimensional array of entries
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> float:
        """
        Get the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: getEntry in interface RealMatrix
        
        Parameters:
            row (int): Row index of entry to be fetched.
            column (int): Column index of entry to be fetched.
        
        Returns:
            the matrix entry at (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
        Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
        Specified by: getFrobeniusNorm in interface RealMatrix
        
        Returns:
            norm
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given row index. Row indices start at 0.
        
        Specified by: getRow in interface RealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            the array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows of this matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in interface RealLinearOperator
        
        Returns:
            the number of rows.
        
        
        """
        ...
    def getRowMatrix(self, row: int) -> RealMatrix:
        """
        Get the entries at the given row index as a row matrix. Row indices start at 0.
        
        Specified by: getRowMatrix in interface RealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            row Matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    def getRowVector(self, row: int) -> RealVector:
        """
        Returns the entries in row number row as a vector. Row indices start at 0.
        
        Specified by: getRowVector in interface RealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            a row vector.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    def getTrace(self) -> float:
        """
        Returns the ` trace <http://mathworld.wolfram.com/MatrixTrace.html>` of the matrix (the sum of the elements on the main diagonal).
        
        Specified by: getTrace in interface RealMatrix
        
        Returns:
            the trace.
        
        Raises:
            MathIllegalArgumentException: if the matrix is not square.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        Computes a hashcode for the matrix.
        
        Overrides: hashCode in class Object
        
        Returns:
            hashcode for matrix
        
        
        """
        ...
    def isSquare(self) -> bool:
        """
        Is this a square matrix?
        
        Specified by: isSquare in interface AnyMatrix
        
        Returns:
            true if the matrix is square (rowDimension = columnDimension)
        
        
        """
        ...
    def multiply(self, m: RealMatrix) -> RealMatrix:
        """
        Returns the result of postmultiplying this by m.
        
        Specified by: multiply in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to postmultiply by
        
        Returns:
            this * m
        
        Raises:
            MathIllegalArgumentException: if columnDimension(this) != rowDimension(m)
        
        
        """
        ...
    def multiplyEntry(self, row: int, column: int, factor: float) -> None:
        """
        Multiplies (in place) the specified entry of this matrix by the specified value. Row and column indices start at 0.
        
        Specified by: multiplyEntry in interface RealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            factor (double): Multiplication factor for the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    def power(self, p: int) -> RealMatrix:
        """
        Returns the result of multiplying this with itself p times. Depending on the underlying storage, instability for high powers might occur.
        
        Specified by: power in interface RealMatrix
        
        Parameters:
            p (int): raise this to power p
        
        Returns:
            this^p
        
        Raises:
            MathIllegalArgumentException: if p < 0
            MathIllegalArgumentException: if the matrix is not square
        
        
        """
        ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, d: float) -> RealMatrix:
        """
        Returns the result of adding d to each entry of this.
        
        Specified by: scalarAdd in interface RealMatrix
        
        Parameters:
            d (double): value to be added to each entry
        
        Returns:
            d + this
        
        
        """
        ...
    def scalarMultiply(self, d: float) -> RealMatrix:
        """
        Returns the result of multiplying each entry of this by d.
        
        Specified by: scalarMultiply in interface RealMatrix
        
        Parameters:
            d (double): value to multiply all entries by
        
        Returns:
            d * this
        
        
        """
        ...
    def setColumn(self, column: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified array. Column indices start at 0.
        
        Specified by: setColumn in interface RealMatrix
        
        Parameters:
            column (int): Column to be set.
            array (double[]): Column array to be copied (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the array length does not match the row dimension of this matrix.
        
        
        """
        ...
    def setColumnMatrix(self, column: int, matrix: RealMatrix) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified column matrix. Column indices start at 0.
        
        Specified by: setColumnMatrix in interface RealMatrix
        
        Parameters:
            column (int): Column to be set.
            matrix (RealMatrix): Column matrix to be copied (must have one column and the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the column dimension of the matrix is not , or the row dimensions of this and matrix
                do not match.
        
        
        """
        ...
    def setColumnVector(self, column: int, vector: RealVector) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified vector. Column indices start at 0.
        
        Specified by: setColumnVector in interface RealMatrix
        
        Parameters:
            column (int): Column to be set.
            vector (RealVector): column vector to be copied (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match the row dimension of this matrix.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: float) -> None:
        """
        Set the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: setEntry in interface RealMatrix
        
        Parameters:
            row (int): Row index of entry to be set.
            column (int): Column index of entry to be set.
            value (double): the new value of the entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified array. Row indices start at 0.
        
        Specified by: setRow in interface RealMatrix
        
        Parameters:
            row (int): Row to be set.
            array (double[]): Row matrix to be copied (must have the same number of columns as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array length does not match the column dimension of this matrix.
        
        
        """
        ...
    def setRowMatrix(self, row: int, matrix: RealMatrix) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified row matrix. Row indices start at 0.
        
        Specified by: setRowMatrix in interface RealMatrix
        
        Parameters:
            row (int): Row to be set.
            matrix (RealMatrix): Row matrix to be copied (must have one row and the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the row dimension of the matrix is not , or the column dimensions of this and matrix
                do not match.
        
        
        """
        ...
    def setRowVector(self, row: int, vector: RealVector) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified vector. Row indices start at 0.
        
        Specified by: setRowVector in interface RealMatrix
        
        Parameters:
            row (int): Row to be set.
            vector (RealVector): row vector to be copied (must have the same number of column as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match the column dimension of this matrix.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at row, column using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Specified by: setSubMatrix in interface RealMatrix
        
        Parameters:
            subMatrix (double[][]): array containing the submatrix replacement data
            row (int): row coordinate of the top, left element to be replaced
            column (int): column coordinate of the top, left element to be replaced
        
        Raises:
            MathIllegalArgumentException: if subMatrix is empty.
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length) or empty.
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
    def subtract(self, m: RealMatrix) -> RealMatrix:
        """
        Returns this minus m.
        
        Specified by: subtract in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to be subtracted
        
        Returns:
            this - m
        
        Raises:
            MathIllegalArgumentException: if m is not the same size as this.
        
        
        """
        ...
    def toString(self) -> str:
        """
        Get a string representation for this matrix.
        
        Overrides: toString in class Object
        
        Returns:
            a string representation for this matrix
        
        
        """
        ...
    def transpose(self) -> RealMatrix:
        """
        Returns the transpose of this matrix.
        
        Specified by: transpose in interface RealMatrix
        
        Returns:
            transpose matrix
        
        
        """
        ...
    @typing.overload
    def walkInColumnOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor) -> float:
        """
        Visit (and possibly change) all matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInColumnOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInColumnOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInOptimizedOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInOptimizedOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInRowOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInRowOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
    This is an implementation of the conjugate gradient method for RealLinearOperator. It follows closely the template by BARR1994 (figure 2.5). The linear system at hand is A · x = b, and the residual is r = b - A · x.
    
    Default stopping criterion
    
    A default stopping criterion is implemented. The iterations stop when || r || ≤ δ || b ||, where b is the right-hand side vector, r the current estimate of the residual, and δ a user-specified tolerance. It should be noted that r is the so-called updated residual, which might differ from the true residual due to rounding-off errors (see e.g. STRA2002).
    
    Iteration count
    
    In the present context, an iteration should be understood as one evaluation of the matrix-vector product A · x. The initialization phase therefore counts as one iteration.
    
    linear
    
    Besides standard MathIllegalArgumentException, this class might throw MathIllegalArgumentException if the linear operator or the preconditioner are not positive definite.
    
      - key "operator" points to the offending linear operator, say L,
      - key "vector" points to the offending vector, say x, such that x :sup:`T` · L · x < 0.
    
    References
    
    Barret et al. (1994) R. Barrett, M. Berry, T. F. Chan, J. Demmel, J. M. Donato, J. Dongarra, V. Eijkhout, R. Pozo, C. Romine and H. Van der Vorst, `Templates for the Solution of Linear Systems: Building Blocks for Iterative Methods <http://www.netlib.org/linalg/html_templates/Templates.html>`, SIAM
    
    Strakos and Tichy (2002) Z. Strakos and P. Tichy, ` On error estimation in the conjugate gradient method and why it works in finite precision computations <http://etna.mcs.kent.edu/vol.13.2002/pp56-80.dir/pp56-80.pdf>`, Electronic Transactions on Numerical Analysis 13: 56-80, 2002
    """
    OPERATOR: typing.ClassVar[str] = ...
    """
    Key for the context.
    
          - constant
    
    
    
    """
    VECTOR: typing.ClassVar[str] = ...
    """
    Key for the context.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, int: int, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager, double: float, boolean: bool): ...
    def shouldCheck(self) -> bool:
        """
        Returns true if positive-definiteness should be checked for both matrix and preconditioner.
        
        Returns:
            true if the tests are to be performed
        
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
    implements Serializable
    
    This class implements the RealVector interface with a OpenIntToDoubleHashMap backing store.
    
    Caveat: This implementation assumes that, for any x, the equality x * 0d == 0d holds. But it is is not true for NaN. Moreover, zero entries will lose their sign. Some operations (that involve NaN and/or infinities) may thus give incorrect results, like multiplications, divisions or functions mapping.
    
          - serialized
    """
    DEFAULT_ZERO_TOLERANCE: typing.ClassVar[float] = ...
    """
    Default Tolerance for having a value considered zero.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, double: float): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, double: float): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], double2: float): ...
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
            v (OpenMapRealVector): vector to append
        
        Returns:
            The result of appending v to self
        
        Construct a new vector by appending a vector to this vector.
        
        Specified by: append in class RealVector
        
        Parameters:
            v (RealVector): vector to append to this one.
        
        Returns:
            a new vector.
        
        Construct a new vector by appending a double to this vector.
        
        Specified by: append in class RealVector
        
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
        
        Specified by: copy in class RealVector
        
        Returns:
            a vector copy.
        
        
        """
        ...
    def ebeDivide(self, v: RealVector) -> 'OpenMapRealVector':
        """
        Element-by-element division.
        
        Specified by: ebeDivide in class RealVector
        
        Parameters:
            v (RealVector): Vector by which instance elements must be divided.
        
        Returns:
            a vector containing this[i] / v[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def ebeMultiply(self, v: RealVector) -> 'OpenMapRealVector':
        """
        Element-by-element multiplication.
        
        Specified by: ebeMultiply in class RealVector
        
        Parameters:
            v (RealVector): Vector by which instance elements must be multiplied
        
        Returns:
            a vector containing this[i] * v[i] for all i.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
        
        """
        ...
    def equals(self, obj: typing.Any) -> bool:
        """
        Test for the equality of two real vectors. If all coordinates of two real vectors are exactly the same, and none are NaN, the two real vectors are considered to be equal. NaN coordinates are considered to affect globally the vector and be equals to each other - i.e, if either (or all) coordinates of the real vector are equal to NaN, the real vector is equal to a vector with all NaN coordinates.
        
        This method must be overriden by concrete subclasses of RealVector (the current implementation throws an exception). Implementation Note: This performs an exact comparison, and as a result it is possible for subtract(b} to be the zero vector, while equals(b) == false.
        
        Overrides: equals in class RealVector
        
        Parameters:
            obj (Object): Object to test for equality.
        
        Returns:
            true if two vector objects are equal, false if other is null, not an instance of
            RealVector, or not equal to this RealVector instance.
        
        
        """
        ...
    def getDimension(self) -> int:
        """
        Returns the size of the vector.
        
        Specified by: getDimension in class RealVector
        
        Returns:
            the size of this vector.
        
        
        """
        ...
    @typing.overload
    def getDistance(self, openMapRealVector: 'OpenMapRealVector') -> float: ...
    @typing.overload
    def getDistance(self, realVector: RealVector) -> float: ...
    def getEntry(self, index: int) -> float:
        """
        Return the entry at the specified index.
        
        Specified by: getEntry in class RealVector
        
        Parameters:
            index (int): Index location of entry to be fetched.
        
        Returns:
            the vector entry at index.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - setEntry
        
        
        
        """
        ...
    @typing.overload
    def getL1Distance(self, openMapRealVector: 'OpenMapRealVector') -> float: ...
    @typing.overload
    def getL1Distance(self, realVector: RealVector) -> float: ...
    def getLInfDistance(self, v: RealVector) -> float:
        """
        Distance between two vectors.
        
        This method computes the distance consistent with L :sub:`∞` norm, i.e. the max of the absolute values of element differences.
        
        Overrides: getLInfDistance in class RealVector
        
        Parameters:
            v (RealVector): Vector to which distance is requested.
        
        Returns:
            the distance between two vectors.
        
        Raises:
            MathIllegalArgumentException: if v is not the same size as this vector.
        
              - getDistance
              - getL1Distance
              - getLInfNorm
        
        
        
        """
        ...
    def getSparsity(self) -> float:
        """
        Get percentage of none zero elements as a decimal percent.
        
        Returns:
            the percentage of none zero elements as a decimal percent
        
        
        """
        ...
    def getSubVector(self, index: int, n: int) -> 'OpenMapRealVector':
        """
        Get a subvector from consecutive elements.
        
        Specified by: getSubVector in class RealVector
        
        Parameters:
            index (int): index of first element.
            n (int): number of elements to be retrieved.
        
        Returns:
            a vector containing n elements.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
            MathIllegalArgumentException: if the number of elements is not positive.
        
        
        """
        ...
    def hashCode(self) -> int:
        """
        . This method must be overriden by concrete subclasses of RealVector (current implementation throws an exception). Implementation Note: This works on exact values, and as a result it is possible for subtract(b) to be the zero vector, while hashCode().
        
        Overrides: hashCode in class RealVector
        
        
        """
        ...
    def isInfinite(self) -> bool:
        """
        Check whether any coordinate of this vector is infinite and none are NaN.
        
        Specified by: isInfinite in class RealVector
        
        Returns:
            true if any coordinate of this vector is infinite and none are NaN, false otherwise.
        
        
        """
        ...
    def isNaN(self) -> bool:
        """
        Check whether any coordinate of this vector is NaN.
        
        Specified by: isNaN in class RealVector
        
        Returns:
            true if any coordinate of this vector is NaN, false otherwise.
        
        
        """
        ...
    def mapAdd(self, d: float) -> 'OpenMapRealVector':
        """
        Add a value to each entry. Returns a new vector. Does not change instance data.
        
        Overrides: mapAdd in class RealVector
        
        Parameters:
            d (double): Value to be added to each entry.
        
        Returns:
            this + d.
        
        
        """
        ...
    def mapAddToSelf(self, d: float) -> 'OpenMapRealVector':
        """
        Add a value to each entry. The instance is changed in-place.
        
        Overrides: mapAddToSelf in class RealVector
        
        Parameters:
            d (double): Value to be added to each entry.
        
        Returns:
            this.
        
        
        """
        ...
    def set(self, value: float) -> None:
        """
        Set all elements to a single value.
        
        Overrides: set in class RealVector
        
        Parameters:
            value (double): Single value to set for all elements.
        
        
        """
        ...
    def setEntry(self, index: int, value: float) -> None:
        """
        Set a single element.
        
        Specified by: setEntry in class RealVector
        
        Parameters:
            index (int): element index.
            value (double): new value for the element.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
              - getEntry
        
        
        
        """
        ...
    def setSubVector(self, index: int, v: RealVector) -> None:
        """
        Set a sequence of consecutive elements.
        
        Specified by: setSubVector in class RealVector
        
        Parameters:
            index (int): index of first element to be set.
            v (RealVector): vector containing the values to set.
        
        Raises:
            MathIllegalArgumentException: if the index is not valid.
        
        
        """
        ...
    def sparseIterator(self) -> java.util.Iterator[RealVector.Entry]:
        """
        Create a sparse iterator over the vector, which may omit some entries. The ommitted entries are either exact zeroes (for dense implementations) or are the entries which are not stored (for real sparse vectors). No guarantees are made about order of iteration.
        
        Note: derived classes are required to return an Iterator that returns non-null Entry objects as long as hasNext returns true.
        
        Overrides: sparseIterator in class RealVector
        
        Returns:
            a sparse iterator.
        
        
        """
        ...
    @typing.overload
    def subtract(self, openMapRealVector: 'OpenMapRealVector') -> 'OpenMapRealVector': ...
    @typing.overload
    def subtract(self, realVector: RealVector) -> RealVector: ...
    def toArray(self) -> typing.MutableSequence[float]:
        """
        Convert the vector to an array of doubles. The array is independent from this vector data: the elements are copied.
        
        Overrides: toArray in class RealVector
        
        Returns:
            an array containing a copy of the vector elements.
        
        
        """
        ...
    def unitVector(self) -> 'OpenMapRealVector':
        """
        Creates a unit vector pointing in the direction of this vector. The instance is not changed by this method.
        
        Overrides: unitVector in class RealVector
        
        Returns:
            a unit vector pointing in direction of this vector.
        
        Raises:
            MathRuntimeException: if the norm is zero.
        
        
        """
        ...
    def unitize(self) -> None:
        """
        Converts this vector into a unit vector. The instance itself is changed by this method.
        
        Overrides: unitize in class RealVector
        
        Raises:
            MathRuntimeException: if the norm is zero.
        
        
        """
        ...

class SparseRealMatrix(RealMatrix):
    """
    Marker interface for RealMatrix implementations that require sparse backing storage
    
    Caveat: Implementation are allowed to assume that, for any x, the equality x * 0d == 0d holds. But it is is not true for NaN. Moreover, zero entries will lose their sign. Some operations (that involve NaN and/or infinities) may thus give incorrect results.
    """
    ...

class SymmLQ(PreconditionedIterativeLinearSolver):
    """
    Implementation of the SYMMLQ iterative linear solver proposed by PAIG1975. This implementation is largely based on the FORTRAN code by Pr. Michael A. Saunders, available `here <http://www.stanford.edu/group/SOL/software/symmlq/f77/>`.
    
    SYMMLQ is designed to solve the system of linear equations A · x = b where A is an n × n self-adjoint linear operator (defined as a RealLinearOperator), and b is a given vector. The operator A is not required to be positive definite. If A is known to be definite, the method of conjugate gradients might be preferred, since it will require about the same number of iterations as SYMMLQ but slightly less work per iteration.
    
    SYMMLQ is designed to solve the system (A - shift · I) · x = b, where shift is a specified scalar value. If shift and b are suitably chosen, the computed vector x may approximate an (unnormalized) eigenvector of A, as in the methods of inverse iteration and/or Rayleigh-quotient iteration. Again, the linear operator (A - shift · I) need not be positive definite (but must be self-adjoint). The work per iteration is very slightly less if shift = 0.
    
    Preconditioning
    
    Preconditioning may reduce the number of iterations required. The solver may be provided with a positive definite preconditioner M = P :sup:`T` · P that is known to approximate (A - shift · I) :sup:`-1` in some sense, where matrix-vector products of the form M · y = x can be computed efficiently. Then SYMMLQ will implicitly solve the system of equations P · (A - shift · I) · P :sup:`T` · x :sub:`hat` = P · b, i.e. A :sub:`hat` · x :sub:`hat` = b :sub:`hat` , where A :sub:`hat` = P · (A - shift · I) · P :sup:`T` , b :sub:`hat` = P · b, and return the solution x = P :sup:`T` · x :sub:`hat` . The associated residual is r :sub:`hat` = b :sub:`hat` - A :sub:`hat` · x :sub:`hat` = P · [b - (A - shift · I) · x] = P · r.
    
    In the case of preconditioning, the IterativeLinearSolverEvents that this solver fires are such that getNormOfResidual returns the norm of the preconditioned, updated residual, ||P · r||, not the norm of the true residual ||r||.
    
    Default stopping criterion
    
    A default stopping criterion is implemented. The iterations stop when || rhat || ≤ δ || Ahat || || xhat ||, where xhat is the current estimate of the solution of the transformed system, rhat the current estimate of the corresponding residual, and δ a user-specified tolerance. Iteration count
    
    In the present context, an iteration should be understood as one evaluation of the matrix-vector product A · x. The initialization phase therefore counts as one iteration. If the user requires checks on the symmetry of A, this entails one further matrix-vector product in the initial phase. This further product is not accounted for in the iteration count. In other words, the number of iterations required to reach convergence will be identical, whether checks have been required or not.
    
    The present definition of the iteration count differs from that adopted in the original FOTRAN code, where the initialization phase was not taken into account. Initial guess of the solution
    
    The x parameter in
    
      - solve,
      - solve},
      - solveInPlace,
      - solveInPlace,
      - solveInPlace,
    
    should not be considered as an initial guess, as it is set to zero in the initial phase. If x :sub:`0` is known to be a good approximation to x, one should compute r :sub:`0` = b - A · x, solve A · dx = r0, and set x = x :sub:`0` + dx.
    
    Exception context
    
    Besides standard MathIllegalArgumentException, this class might throw MathIllegalArgumentException if the linear operator or the preconditioner are not symmetric.
    
      - key "operator" points to the offending linear operator, say L,
      - key "vector1" points to the first offending vector, say x,
      - key "vector2" points to the second offending vector, say y, such that x :sup:`T` · L · y ≠ y :sup:`T` · L
        · x (within a certain accuracy).
    
    MathIllegalArgumentException might also be thrown in case the preconditioner is not positive definite.
    
    References
    
    linear C. C. Paige and M. A. Saunders, `Solution of Sparse Indefinite Systems of Linear Equations <http://www.stanford.edu/group/SOL/software/symmlq/PS75.pdf>`, SIAM Journal on Numerical Analysis 12(4): 617-629, 1975
    """
    @typing.overload
    def __init__(self, int: int, double: float, boolean: bool): ...
    @typing.overload
    def __init__(self, iterationManager: org.hipparchus.util.IterationManager, double: float, boolean: bool): ...
    def shouldCheck(self) -> bool:
        """
        Returns true if symmetry of the matrix, and symmetry as well as positive definiteness of the preconditioner should be checked.
        
        Returns:
            true if the tests are to be performed
        
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
    """
    implements Serializable
    
    Implementation of FieldMatrix using a FieldElement[][] array to store entries.
    
    As specified in the FieldMatrix interface, matrix element indexing is 0-based -- e.g., getEntry(0, 0) returns the element in the first row, first column of the matrix
    
          - serialized
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_Array2DRowFieldMatrix__T], tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def add(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def add(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def addToEntry(self, row: int, column: int, increment: _Array2DRowFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: addToEntry in interface FieldMatrix
        
        Specified by: addToEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            increment (Array2DRowFieldMatrix): Value to add to the current matrix entry in (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> FieldMatrix[_Array2DRowFieldMatrix__T]:
        """
        Make a (deep) copy of this.
        
        Specified by: copy in interface FieldMatrix
        
        Specified by: copy in class AbstractFieldMatrix
        
        Returns:
            a copy of this matrix.
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> FieldMatrix[_Array2DRowFieldMatrix__T]:
        """
        Create a new FieldMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface FieldMatrix
        
        Specified by: createMatrix in class AbstractFieldMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns in the matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in class AbstractFieldMatrix
        
        Returns:
            columnDimension
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_Array2DRowFieldMatrix__T]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface FieldMatrix
        
        Overrides: getData in class AbstractFieldMatrix
        
        Returns:
            a 2-dimensional array of entries.
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[typing.MutableSequence[_Array2DRowFieldMatrix__T]]:
        """
        Get a reference to the underlying data array. This methods returns internal data, not fresh copy of it.
        
        Returns:
            the 2-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> _Array2DRowFieldMatrix__T:
        """
        Returns the entry in the specified row and column.
        
        Specified by: getEntry in interface FieldMatrix
        
        Specified by: getEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): row location of entry to be fetched
            column (int): column location of entry to be fetched
        
        Returns:
            matrix entry in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[_Array2DRowFieldMatrix__T]:
        """
        Get the entries in row number row as an array.
        
        Specified by: getRow in interface FieldMatrix
        
        Overrides: getRow in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows in the matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in class AbstractFieldMatrix
        
        Returns:
            rowDimension
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    def multiplyEntry(self, row: int, column: int, factor: _Array2DRowFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: multiplyEntry in interface FieldMatrix
        
        Specified by: multiplyEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            factor (Array2DRowFieldMatrix): Multiplication factor for the current matrix entry in (row,column)
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, array2DRowFieldMatrix: 'Array2DRowFieldMatrix'[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def multiplyTransposed(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_Array2DRowFieldMatrix__T]) -> FieldVector[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_Array2DRowFieldMatrix__T]) -> FieldMatrix[_Array2DRowFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_Array2DRowFieldMatrix__T]) -> FieldVector[_Array2DRowFieldMatrix__T]: ...
    def setEntry(self, row: int, column: int, value: _Array2DRowFieldMatrix__T) -> None:
        """
        Set the entry in the specified row and column.
        
        Specified by: setEntry in interface FieldMatrix
        
        Specified by: setEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): row location of entry to be set
            column (int): column location of entry to be set
            value (Array2DRowFieldMatrix): matrix entry to be set in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[_Array2DRowFieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in row number row as a row matrix.
        
        Specified by: setRow in interface FieldMatrix
        
        Overrides: setRow in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be set.
            array (Array2DRowFieldMatrix[]): Row matrix (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance row.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[_Array2DRowFieldMatrix__T]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at (row, column) using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Specified by: setSubMatrix in interface FieldMatrix
        
        Overrides: setSubMatrix in class AbstractFieldMatrix
        
        Parameters:
            subMatrix (Array2DRowFieldMatrix[][]): Array containing the submatrix replacement data.
            row (int): Row coordinate of the top-left element to be replaced.
            column (int): Column coordinate of the top-left element to be replaced.
        
        Raises:
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if a row or column of subMatrix is empty.
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length).
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
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
    implements Serializable
    
    Implementation of RealMatrix using a double[][] array to store entries.
    
          - serialized
    """
    @typing.overload
    def __init__(self): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def add(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, row: int, column: int, increment: float) -> None:
        """
        Adds (in place) the specified value to the specified entry of this matrix. Row and column indices start at 0.
        
        Specified by: addToEntry in interface RealMatrix
        
        Overrides: addToEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            increment (double): value to add to the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> RealMatrix:
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface RealMatrix
        
        Specified by: copy in class AbstractRealMatrix
        
        Returns:
            matrix copy
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> RealMatrix:
        """
        Create a new RealMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface RealMatrix
        
        Specified by: createMatrix in class AbstractRealMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns of this matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in interface RealLinearOperator
        
        Specified by: getColumnDimension in class AbstractRealMatrix
        
        Returns:
            the number of columns.
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface RealMatrix
        
        Overrides: getData in class AbstractRealMatrix
        
        Returns:
            2-dimensional array of entries
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Get a reference to the underlying data array.
        
        Returns:
            2-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> float:
        """
        Get the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: getEntry in interface RealMatrix
        
        Specified by: getEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be fetched.
            column (int): Column index of entry to be fetched.
        
        Returns:
            the matrix entry at (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given row index. Row indices start at 0.
        
        Specified by: getRow in interface RealMatrix
        
        Overrides: getRow in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            the array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows of this matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in interface RealLinearOperator
        
        Specified by: getRowDimension in class AbstractRealMatrix
        
        Returns:
            the number of rows.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> RealMatrix: ...
    def kroneckerProduct(self, b: RealMatrix) -> RealMatrix:
        """
        Kronecker product of the current matrix and the parameter matrix.
        
        Parameters:
            b (RealMatrix): matrix to post Kronecker-multiply by
        
        Returns:
            this ⨂ b
        
        
        """
        ...
    @typing.overload
    def multiply(self, array2DRowRealMatrix: 'Array2DRowRealMatrix') -> 'Array2DRowRealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, row: int, column: int, factor: float) -> None:
        """
        Multiplies (in place) the specified entry of this matrix by the specified value. Row and column indices start at 0.
        
        Specified by: multiplyEntry in interface RealMatrix
        
        Overrides: multiplyEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            factor (double): Multiplication factor for the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, m: 'Array2DRowRealMatrix') -> RealMatrix:
        """
        Returns the result of postmultiplying this by m^T.
        
        This is equivalent to call multiply(m.transpose), but some implementations may avoid building the intermediate transposed matrix.
        
        Specified by: multiplyTransposed in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to first transpose and second postmultiply by
        
        Returns:
            this * m^T
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def setEntry(self, row: int, column: int, value: float) -> None:
        """
        Set the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: setEntry in interface RealMatrix
        
        Specified by: setEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be set.
            column (int): Column index of entry to be set.
            value (double): the new value of the entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified array. Row indices start at 0.
        
        Specified by: setRow in interface RealMatrix
        
        Overrides: setRow in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be set.
            array (double[]): Row matrix to be copied (must have the same number of columns as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array length does not match the column dimension of this matrix.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at row, column using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Specified by: setSubMatrix in interface RealMatrix
        
        Overrides: setSubMatrix in class AbstractRealMatrix
        
        Parameters:
            subMatrix (double[][]): array containing the submatrix replacement data
            row (int): row coordinate of the top, left element to be replaced
            column (int): column coordinate of the top, left element to be replaced
        
        Raises:
            MathIllegalArgumentException: if subMatrix is empty.
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length) or empty.
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
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
    def transposeMultiply(self, m: 'Array2DRowRealMatrix') -> RealMatrix:
        """
        Returns the result of postmultiplying this^T by m.
        
        This is equivalent to call transpose.multiply, but some implementations may avoid building the intermediate transposed matrix.
        
        Specified by: transposeMultiply in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to postmultiply by
        
        Returns:
            this^T * m
        
        
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
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Overrides: walkInColumnOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Overrides: walkInColumnOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInColumnOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Overrides: walkInColumnOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInColumnOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in column order.
        
        Column order starts at upper left and iterating through all elements of a column from top to bottom before going to the topmost element of the next column.
        
        Specified by: walkInColumnOrder in interface RealMatrix
        
        Overrides: walkInColumnOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInRowOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInRowOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
    """
    implements Serializable
    
    Cache-friendly implementation of FieldMatrix using a flat arrays to store square blocks of the matrix.
    
    This implementation is specially designed to be cache-friendly. Square blocks are stored as small arrays and allow efficient traversal of data both in row major direction and columns major direction, one block at a time. This greatly increases performances for algorithms that use crossed directions loops like multiplication or transposition.
    
    The size of square blocks is a static parameter. It may be tuned according to the cache size of the target computer processor. As a rule of thumbs, it should be the largest value that allows three blocks to be simultaneously cached (this is necessary for example for matrix multiplication). The default value is to use 36x36 blocks.
    
    The regular blocks represent BLOCK_SIZE x BLOCK_SIZE squares. Blocks at right hand side and bottom side which may be smaller to fit matrix dimensions. The square blocks are flattened in row major order in single dimension arrays which are therefore BLOCK_SIZE :sup:`2` elements long for regular blocks. The blocks are themselves organized in row major order.
    
    As an example, for a block size of 36x36, a 100x60 matrix would be stored in 6 blocks. Block 0 would be a Field[1296] array holding the upper left 36x36 square, block 1 would be a Field[1296] array holding the upper center 36x36 square, block 2 would be a Field[1008] array holding the upper right 36x28 rectangle, block 3 would be a Field[864] array holding the lower left 24x36 rectangle, block 4 would be a Field[864] array holding the lower center 24x36 rectangle and block 5 would be a Field[672] array holding the lower right 24x28 rectangle.
    
    The layout complexity overhead versus simple mapping of matrices to java arrays is negligible for small matrices (about 1%). The gain from cache efficiency leads to up to 3-fold improvements for matrices of moderate to large size.
    
          - serialized
    """
    BLOCK_SIZE: typing.ClassVar[int] = ...
    """
    Block size.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, int: int, int2: int, tArray: typing.Union[typing.List[typing.MutableSequence[_BlockFieldMatrix__T]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_BlockFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, tArray: typing.Union[typing.List[typing.MutableSequence[_BlockFieldMatrix__T]], jpype.JArray]): ...
    @typing.overload
    def add(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def add(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def addToEntry(self, row: int, column: int, increment: _BlockFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: addToEntry in interface FieldMatrix
        
        Specified by: addToEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            increment (BlockFieldMatrix): Value to add to the current matrix entry in (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Make a (deep) copy of this.
        
        Specified by: copy in interface FieldMatrix
        
        Specified by: copy in class AbstractFieldMatrix
        
        Returns:
            a copy of this matrix.
        
        
        """
        ...
    _createBlocksLayout__T = typing.TypeVar('_createBlocksLayout__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def createBlocksLayout(field: org.hipparchus.Field[_createBlocksLayout__T], rows: int, columns: int) -> typing.MutableSequence[typing.MutableSequence[_createBlocksLayout__T]]:
        """
        Create a data array in blocks layout.
        
        This method can be used to create the array argument of the constructor.
        
        Parameters:
            field (Field<T> field): Field to which the elements belong.
            rows (int): Number of rows in the new matrix.
            columns (int): Number of columns in the new matrix.
        
        Returns:
            a new data array in blocks layout.
        
              - toBlocksLayout
              - 
        
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Create a new FieldMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface FieldMatrix
        
        Specified by: createMatrix in class AbstractFieldMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def getColumn(self, column: int) -> typing.MutableSequence[_BlockFieldMatrix__T]:
        """
        Get the entries in column number col as an array.
        
        Specified by: getColumn in interface FieldMatrix
        
        Overrides: getColumn in class AbstractFieldMatrix
        
        Parameters:
            column (int): the column to be fetched
        
        Returns:
            array of entries in the column
        
        Raises:
            MathIllegalArgumentException: if the specified column index is not valid.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns in the matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in class AbstractFieldMatrix
        
        Returns:
            columnDimension
        
        
        """
        ...
    def getColumnMatrix(self, column: int) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Get the entries in column number column as a column matrix.
        
        Specified by: getColumnMatrix in interface FieldMatrix
        
        Overrides: getColumnMatrix in class AbstractFieldMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getColumnVector(self, column: int) -> FieldVector[_BlockFieldMatrix__T]:
        """
        Returns the entries in column number column as a vector.
        
        Specified by: getColumnVector in interface FieldMatrix
        
        Overrides: getColumnVector in class AbstractFieldMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column vector.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[_BlockFieldMatrix__T]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface FieldMatrix
        
        Overrides: getData in class AbstractFieldMatrix
        
        Returns:
            a 2-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> _BlockFieldMatrix__T:
        """
        Returns the entry in the specified row and column.
        
        Specified by: getEntry in interface FieldMatrix
        
        Specified by: getEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): row location of entry to be fetched
            column (int): column location of entry to be fetched
        
        Returns:
            matrix entry in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[_BlockFieldMatrix__T]:
        """
        Get the entries in row number row as an array.
        
        Specified by: getRow in interface FieldMatrix
        
        Overrides: getRow in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows in the matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in class AbstractFieldMatrix
        
        Returns:
            rowDimension
        
        
        """
        ...
    def getRowMatrix(self, row: int) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Get the entries in row number row as a row matrix.
        
        Specified by: getRowMatrix in interface FieldMatrix
        
        Overrides: getRowMatrix in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            a row matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    def getRowVector(self, row: int) -> FieldVector[_BlockFieldMatrix__T]:
        """
        Get the entries in row number row as a vector.
        
        Specified by: getRowVector in interface FieldMatrix
        
        Overrides: getRowVector in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be fetched
        
        Returns:
            a row vector.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    def multiplyEntry(self, row: int, column: int, factor: _BlockFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: multiplyEntry in interface FieldMatrix
        
        Specified by: multiplyEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            factor (BlockFieldMatrix): Multiplication factor for the current matrix entry in (row,column)
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def multiplyTransposed(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def operate(self, tArray: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_BlockFieldMatrix__T]: ...
    @typing.overload
    def operate(self, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> FieldVector[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, tArray: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> typing.MutableSequence[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    @typing.overload
    def preMultiply(self, fieldVector: FieldVector[_BlockFieldMatrix__T]) -> FieldVector[_BlockFieldMatrix__T]: ...
    def scalarAdd(self, d: _BlockFieldMatrix__T) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Increment each entry of this matrix.
        
        Specified by: scalarAdd in interface FieldMatrix
        
        Overrides: scalarAdd in class AbstractFieldMatrix
        
        Parameters:
            d (BlockFieldMatrix): Value to be added to each entry.
        
        Returns:
            d + this.
        
        
        """
        ...
    def scalarMultiply(self, d: _BlockFieldMatrix__T) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Multiply each entry by d.
        
        Specified by: scalarMultiply in interface FieldMatrix
        
        Overrides: scalarMultiply in class AbstractFieldMatrix
        
        Parameters:
            d (BlockFieldMatrix): Value to multiply all entries by.
        
        Returns:
            d * this.
        
        
        """
        ...
    def setColumn(self, column: int, array: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in column number column as a column matrix.
        
        Specified by: setColumn in interface FieldMatrix
        
        Overrides: setColumn in class AbstractFieldMatrix
        
        Parameters:
            column (int): the column to be set
            array (BlockFieldMatrix[]): column array (must have the same number of rows as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance column.
        
        
        """
        ...
    def setColumnMatrix(self, column: int, matrix: FieldMatrix[_BlockFieldMatrix__T]) -> None:
        """
        Set the entries in column number column as a column matrix.
        
        Specified by: setColumnMatrix in interface FieldMatrix
        
        Overrides: setColumnMatrix in class AbstractFieldMatrix
        
        Parameters:
            column (int): Column to be set.
            matrix (FieldMatrix<BlockFieldMatrix> matrix): column matrix (must have one column and the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the matrix dimensions do not match one instance column.
        
        
        """
        ...
    def setColumnVector(self, column: int, vector: FieldVector[_BlockFieldMatrix__T]) -> None:
        """
        Set the entries in column number column as a vector.
        
        Specified by: setColumnVector in interface FieldMatrix
        
        Overrides: setColumnVector in class AbstractFieldMatrix
        
        Parameters:
            column (int): Column to be set.
            vector (FieldVector<BlockFieldMatrix> vector): Column vector (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match one instance column.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: _BlockFieldMatrix__T) -> None:
        """
        Set the entry in the specified row and column.
        
        Specified by: setEntry in interface FieldMatrix
        
        Specified by: setEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): row location of entry to be set
            column (int): column location of entry to be set
            value (BlockFieldMatrix): matrix entry to be set in row,column
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[_BlockFieldMatrix__T], jpype.JArray]) -> None:
        """
        Set the entries in row number row as a row matrix.
        
        Specified by: setRow in interface FieldMatrix
        
        Overrides: setRow in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be set.
            array (BlockFieldMatrix[]): Row matrix (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array size does not match one instance row.
        
        
        """
        ...
    @typing.overload
    def setRowMatrix(self, int: int, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> None: ...
    def setRowVector(self, row: int, vector: FieldVector[_BlockFieldMatrix__T]) -> None:
        """
        Set the entries in row number row as a vector.
        
        Specified by: setRowVector in interface FieldMatrix
        
        Overrides: setRowVector in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row to be set.
            vector (FieldVector<BlockFieldMatrix> vector): row vector (must have the same number of columns as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match one instance row.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[_BlockFieldMatrix__T]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at (row, column) using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Specified by: setSubMatrix in interface FieldMatrix
        
        Overrides: setSubMatrix in class AbstractFieldMatrix
        
        Parameters:
            subMatrix (BlockFieldMatrix[][]): Array containing the submatrix replacement data.
            row (int): Row coordinate of the top-left element to be replaced.
            column (int): Column coordinate of the top-left element to be replaced.
        
        Raises:
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if a row or column of subMatrix is empty.
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length).
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
    @typing.overload
    def subtract(self, blockFieldMatrix: 'BlockFieldMatrix'[_BlockFieldMatrix__T]) -> 'BlockFieldMatrix'[_BlockFieldMatrix__T]: ...
    @typing.overload
    def subtract(self, fieldMatrix: FieldMatrix[_BlockFieldMatrix__T]) -> FieldMatrix[_BlockFieldMatrix__T]: ...
    _toBlocksLayout__T = typing.TypeVar('_toBlocksLayout__T', bound=org.hipparchus.FieldElement)  # <T>
    @staticmethod
    def toBlocksLayout(rawData: typing.Union[typing.List[typing.MutableSequence[_toBlocksLayout__T]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[_toBlocksLayout__T]]:
        """
        Convert a data array from raw layout to blocks layout.
        
        Raw layout is the straightforward layout where element at row i and column j is in array element rawData[i][j]. Blocks layout is the layout used in BlockFieldMatrix instances, where the matrix is split in square blocks (except at right and bottom side where blocks may be rectangular to fit matrix size) and each block is stored in a flattened one-dimensional array.
        
        This method creates an array in blocks layout from an input array in raw layout. It can be used to provide the array argument of the  constructor.
        
        Parameters:
            rawData (T[][]): Data array in raw layout.
        
        Returns:
            a new data array containing the same entries but in blocks layout
        
        Raises:
            MathIllegalArgumentException: if rawData is not rectangular (not all rows have the same length).
        
              - createBlocksLayout
              - 
        
        
        
        """
        ...
    def transpose(self) -> FieldMatrix[_BlockFieldMatrix__T]:
        """
        Returns the transpose of this matrix.
        
        Specified by: transpose in interface FieldMatrix
        
        Overrides: transpose in class AbstractFieldMatrix
        
        Returns:
            transpose matrix
        
        
        """
        ...
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
    implements Serializable
    
    Cache-friendly implementation of RealMatrix using a flat arrays to store square blocks of the matrix.
    
    This implementation is specially designed to be cache-friendly. Square blocks are stored as small arrays and allow efficient traversal of data both in row major direction and columns major direction, one block at a time. This greatly increases performances for algorithms that use crossed directions loops like multiplication or transposition.
    
    The size of square blocks is a static parameter. It may be tuned according to the cache size of the target computer processor. As a rule of thumbs, it should be the largest value that allows three blocks to be simultaneously cached (this is necessary for example for matrix multiplication). The default value is to use 52x52 blocks which is well suited for processors with 64k L1 cache (one block holds 2704 values or 21632 bytes). This value could be lowered to 36x36 for processors with 32k L1 cache.
    
    The regular blocks represent BLOCK_SIZE x BLOCK_SIZE squares. Blocks at right hand side and bottom side may be smaller to fit matrix dimensions. The square blocks are flattened in row major order in single dimension arrays which are therefore BLOCK_SIZE :sup:`2` elements long for regular blocks. The blocks are themselves organized in row major order.
    
    As an example, for a block size of 52x52, a 100x60 matrix would be stored in 4 blocks. Block 0 would be a double[2704] array holding the upper left 52x52 square, block 1 would be a double[416] array holding the upper right 52x8 rectangle, block 2 would be a double[2496] array holding the lower left 48x52 rectangle and block 3 would be a double[384] array holding the lower right 48x8 rectangle.
    
    The layout complexity overhead versus simple mapping of matrices to java arrays is negligible for small matrices (about 1%). The gain from cache efficiency leads to up to 3-fold improvements for matrices of moderate to large size.
    
          - serialized
    """
    BLOCK_SIZE: typing.ClassVar[int] = ...
    """
    Block size.
    
          - constant
    
    
    
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]): ...
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, int: int, int2: int, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], boolean: bool): ...
    @typing.overload
    def add(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    def addToEntry(self, row: int, column: int, increment: float) -> None:
        """
        Adds (in place) the specified value to the specified entry of this matrix. Row and column indices start at 0.
        
        Specified by: addToEntry in interface RealMatrix
        
        Overrides: addToEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            increment (double): value to add to the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> 'BlockRealMatrix':
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface RealMatrix
        
        Specified by: copy in class AbstractRealMatrix
        
        Returns:
            matrix copy
        
        
        """
        ...
    @staticmethod
    def createBlocksLayout(rows: int, columns: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Create a data array in blocks layout.
        
        This method can be used to create the array argument of the constructor.
        
        Parameters:
            rows (int): Number of rows in the new matrix.
            columns (int): Number of columns in the new matrix.
        
        Returns:
            a new data array in blocks layout.
        
              - toBlocksLayout
              - 
        
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> 'BlockRealMatrix':
        """
        Create a new RealMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface RealMatrix
        
        Specified by: createMatrix in class AbstractRealMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if row or column dimension is not positive.
        
        
        """
        ...
    def getColumn(self, column: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given column index as an array. Column indices start at 0.
        
        Specified by: getColumn in interface RealMatrix
        
        Overrides: getColumn in class AbstractRealMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            the array of entries in the column.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is not valid.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns of this matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in interface RealLinearOperator
        
        Specified by: getColumnDimension in class AbstractRealMatrix
        
        Returns:
            the number of columns.
        
        
        """
        ...
    def getColumnMatrix(self, column: int) -> 'BlockRealMatrix':
        """
        Get the entries at the given column index as a column matrix. Column indices start at 0.
        
        Specified by: getColumnMatrix in interface RealMatrix
        
        Overrides: getColumnMatrix in class AbstractRealMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            column Matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
        
        
        """
        ...
    def getColumnVector(self, column: int) -> RealVector:
        """
        Get the entries at the given column index as a vector. Column indices start at 0.
        
        Specified by: getColumnVector in interface RealMatrix
        
        Overrides: getColumnVector in class AbstractRealMatrix
        
        Parameters:
            column (int): Column to be fetched.
        
        Returns:
            a column vector.
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface RealMatrix
        
        Overrides: getData in class AbstractRealMatrix
        
        Returns:
            2-dimensional array of entries
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> float:
        """
        Get the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: getEntry in interface RealMatrix
        
        Specified by: getEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be fetched.
            column (int): Column index of entry to be fetched.
        
        Returns:
            the matrix entry at (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getFrobeniusNorm(self) -> float:
        """
        Returns the ` Frobenius norm <http://mathworld.wolfram.com/FrobeniusNorm.html>` of the matrix.
        
        Specified by: getFrobeniusNorm in interface RealMatrix
        
        Overrides: getFrobeniusNorm in class AbstractRealMatrix
        
        Returns:
            norm
        
        
        """
        ...
    def getNorm1(self) -> float:
        """
        Returns the ` maximum absolute column sum norm <http://mathworld.wolfram.com/MaximumAbsoluteColumnSumNorm.html>` (L :sub:`1` ) of the matrix.
        
        Specified by: getNorm1 in interface RealMatrix
        
        Returns:
            norm
        
        
        """
        ...
    def getNormInfty(self) -> float:
        """
        Returns the ` maximum absolute row sum norm <http://mathworld.wolfram.com/MaximumAbsoluteRowSumNorm.html>` (L :sub:`∞` ) of the matrix.
        
        Specified by: getNormInfty in interface RealMatrix
        
        Returns:
            norm
        
        
        """
        ...
    def getRow(self, row: int) -> typing.MutableSequence[float]:
        """
        Get the entries at the given row index. Row indices start at 0.
        
        Specified by: getRow in interface RealMatrix
        
        Overrides: getRow in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            the array of entries in the row.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows of this matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in interface RealLinearOperator
        
        Specified by: getRowDimension in class AbstractRealMatrix
        
        Returns:
            the number of rows.
        
        
        """
        ...
    def getRowMatrix(self, row: int) -> 'BlockRealMatrix':
        """
        Get the entries at the given row index as a row matrix. Row indices start at 0.
        
        Specified by: getRowMatrix in interface RealMatrix
        
        Overrides: getRowMatrix in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            row Matrix.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    def getRowVector(self, row: int) -> RealVector:
        """
        Returns the entries in row number row as a vector. Row indices start at 0.
        
        Specified by: getRowVector in interface RealMatrix
        
        Overrides: getRowVector in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be fetched.
        
        Returns:
            a row vector.
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
        
        
        """
        ...
    @typing.overload
    def getSubMatrix(self, int: int, int2: int, int3: int, int4: int) -> 'BlockRealMatrix': ...
    @typing.overload
    def getSubMatrix(self, intArray: typing.Union[typing.List[int], jpype.JArray], intArray2: typing.Union[typing.List[int], jpype.JArray]) -> RealMatrix: ...
    @typing.overload
    def multiply(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    def multiplyEntry(self, row: int, column: int, factor: float) -> None:
        """
        Multiplies (in place) the specified entry of this matrix by the specified value. Row and column indices start at 0.
        
        Specified by: multiplyEntry in interface RealMatrix
        
        Overrides: multiplyEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            factor (double): Multiplication factor for the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def multiplyTransposed(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def scalarAdd(self, d: float) -> 'BlockRealMatrix':
        """
        Returns the result of adding d to each entry of this.
        
        Specified by: scalarAdd in interface RealMatrix
        
        Overrides: scalarAdd in class AbstractRealMatrix
        
        Parameters:
            d (double): value to be added to each entry
        
        Returns:
            d + this
        
        
        """
        ...
    def scalarMultiply(self, d: float) -> RealMatrix:
        """
        Returns the result of multiplying each entry of this by d.
        
        Specified by: scalarMultiply in interface RealMatrix
        
        Overrides: scalarMultiply in class AbstractRealMatrix
        
        Parameters:
            d (double): value to multiply all entries by
        
        Returns:
            d * this
        
        
        """
        ...
    def setColumn(self, column: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified array. Column indices start at 0.
        
        Specified by: setColumn in interface RealMatrix
        
        Overrides: setColumn in class AbstractRealMatrix
        
        Parameters:
            column (int): Column to be set.
            array (double[]): Column array to be copied (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the array length does not match the row dimension of this matrix.
        
        
        """
        ...
    def setColumnMatrix(self, column: int, matrix: RealMatrix) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified column matrix. Column indices start at 0.
        
        Specified by: setColumnMatrix in interface RealMatrix
        
        Overrides: setColumnMatrix in class AbstractRealMatrix
        
        Parameters:
            column (int): Column to be set.
            matrix (RealMatrix): Column matrix to be copied (must have one column and the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the column dimension of the matrix is not , or the row dimensions of this and matrix
                do not match.
        
        
        """
        ...
    def setColumnVector(self, column: int, vector: RealVector) -> None:
        """
        Sets the specified column of this matrix to the entries of the specified vector. Column indices start at 0.
        
        Specified by: setColumnVector in interface RealMatrix
        
        Overrides: setColumnVector in class AbstractRealMatrix
        
        Parameters:
            column (int): Column to be set.
            vector (RealVector): column vector to be copied (must have the same number of rows as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified column index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match the row dimension of this matrix.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: float) -> None:
        """
        Set the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: setEntry in interface RealMatrix
        
        Specified by: setEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be set.
            column (int): Column index of entry to be set.
            value (double): the new value of the entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid
        
        
        """
        ...
    def setRow(self, row: int, array: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified array. Row indices start at 0.
        
        Specified by: setRow in interface RealMatrix
        
        Overrides: setRow in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be set.
            array (double[]): Row matrix to be copied (must have the same number of columns as the instance)
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the array length does not match the column dimension of this matrix.
        
        
        """
        ...
    @typing.overload
    def setRowMatrix(self, int: int, blockRealMatrix: 'BlockRealMatrix') -> None: ...
    @typing.overload
    def setRowMatrix(self, int: int, realMatrix: RealMatrix) -> None: ...
    def setRowVector(self, row: int, vector: RealVector) -> None:
        """
        Sets the specified row of this matrix to the entries of the specified vector. Row indices start at 0.
        
        Specified by: setRowVector in interface RealMatrix
        
        Overrides: setRowVector in class AbstractRealMatrix
        
        Parameters:
            row (int): Row to be set.
            vector (RealVector): row vector to be copied (must have the same number of column as the instance).
        
        Raises:
            MathIllegalArgumentException: if the specified row index is invalid.
            MathIllegalArgumentException: if the vector dimension does not match the column dimension of this matrix.
        
        
        """
        ...
    def setSubMatrix(self, subMatrix: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], row: int, column: int) -> None:
        """
        Replace the submatrix starting at row, column using data in the input subMatrix array. Indexes are 0-based.
        
        Example:
        
        Starting with
        
         1  2  3  4 5  6  7  8 9  0  1  2
        
        and subMatrix = {{3, 4} {5,6}}, invoking setSubMatrix(subMatrix,1,1)) will result in
        
         1  2  3  4 5  3  4  8 9  5  6  2
        
        Specified by: setSubMatrix in interface RealMatrix
        
        Overrides: setSubMatrix in class AbstractRealMatrix
        
        Parameters:
            subMatrix (double[][]): array containing the submatrix replacement data
            row (int): row coordinate of the top, left element to be replaced
            column (int): column coordinate of the top, left element to be replaced
        
        Raises:
            MathIllegalArgumentException: if subMatrix is empty.
            MathIllegalArgumentException: if subMatrix does not fit into this matrix from element in (row, column).
            MathIllegalArgumentException: if subMatrix is not rectangular (not all rows have the same length) or empty.
            NullArgumentException: if subMatrix is null.
        
        
        """
        ...
    @typing.overload
    def subtract(self, blockRealMatrix: 'BlockRealMatrix') -> 'BlockRealMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> 'BlockRealMatrix': ...
    @staticmethod
    def toBlocksLayout(rawData: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Convert a data array from raw layout to blocks layout.
        
        Raw layout is the straightforward layout where element at row i and column j is in array element rawData[i][j]. Blocks layout is the layout used in BlockRealMatrix instances, where the matrix is split in square blocks (except at right and bottom side where blocks may be rectangular to fit matrix size) and each block is stored in a flattened one-dimensional array.
        
        This method creates an array in blocks layout from an input array in raw layout. It can be used to provide the array argument of the  constructor.
        
        Parameters:
            rawData (double[][]): Data array in raw layout.
        
        Returns:
            a new data array containing the same entries but in blocks layout.
        
        Raises:
            MathIllegalArgumentException: if rawData is not rectangular.
        
              - createBlocksLayout
              - 
        
        
        
        """
        ...
    def transpose(self) -> 'BlockRealMatrix':
        """
        Returns the transpose of this matrix.
        
        Specified by: transpose in interface RealMatrix
        
        Overrides: transpose in class AbstractRealMatrix
        
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
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Overrides: walkInOptimizedOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Overrides: walkInOptimizedOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInOptimizedOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Overrides: walkInOptimizedOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInOptimizedOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries using the fastest possible order.
        
        The fastest walking order depends on the exact matrix class. It may be different from traditional row or column orders.
        
        Specified by: walkInOptimizedOrder in interface RealMatrix
        
        Overrides: walkInOptimizedOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index (inclusive)
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
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
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        Visit (but don't change) all matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
        
        Returns:
            the value returned by end at the end of the walk
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInRowOrder(RealMatrixChangingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (and possibly change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixChangingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        public double walkInRowOrder(RealMatrixPreservingVisitor visitor, int startRow, int endRow, int startColumn, int endColumn) throws MathIllegalArgumentException
        
        Visit (but don't change) some matrix entries in row order.
        
        Row order starts at upper left and iterating through all elements of a row from left to right before going to the leftmost element of the next row.
        
        Specified by: walkInRowOrder in interface RealMatrix
        
        Overrides: walkInRowOrder in class AbstractRealMatrix
        
        Parameters:
            visitor (RealMatrixPreservingVisitor): visitor used to process all matrix entries
            startRow (int): Initial row index
            endRow (int): Final row index (inclusive)
            startColumn (int): Initial column index
            endColumn (int): Final column index
        
        Returns:
            the value returned by end at the end of the walk
        
        Raises:
            MathIllegalArgumentException: if the indices are not valid.
            MathIllegalArgumentException: if endRow < startRow or endColumn < startColumn.
        
              - walkInRowOrder
              - walkInRowOrder
              - walkInRowOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInColumnOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
              - walkInOptimizedOrder
        
        
        
        """
        ...
    @typing.overload
    def walkInRowOrder(self, realMatrixChangingVisitor: RealMatrixChangingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor) -> float: ...
    @typing.overload
    def walkInRowOrder(self, realMatrixPreservingVisitor: RealMatrixPreservingVisitor, int: int, int2: int, int3: int, int4: int) -> float: ...

class DiagonalMatrix(AbstractRealMatrix, java.io.Serializable):
    """
    implements Serializable
    
    Implementation of a diagonal matrix.
    
          - serialized
    """
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]): ...
    @typing.overload
    def __init__(self, doubleArray: typing.Union[typing.List[float], jpype.JArray], boolean: bool): ...
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def add(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, row: int, column: int, increment: float) -> None:
        """
        Adds (in place) the specified value to the specified entry of this matrix. Row and column indices start at 0.
        
        Specified by: addToEntry in interface RealMatrix
        
        Overrides: addToEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            increment (double): value to add to the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if row != column and increment is non-zero.
        
        
        """
        ...
    def copy(self) -> RealMatrix:
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface RealMatrix
        
        Specified by: copy in class AbstractRealMatrix
        
        Returns:
            matrix copy
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> RealMatrix:
        """
        Create a new RealMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface RealMatrix
        
        Specified by: createMatrix in class AbstractRealMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if the requested dimensions are not equal.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns of this matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in interface RealLinearOperator
        
        Specified by: getColumnDimension in class AbstractRealMatrix
        
        Returns:
            the number of columns.
        
        
        """
        ...
    def getData(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Returns matrix entries as a two-dimensional array.
        
        Specified by: getData in interface RealMatrix
        
        Overrides: getData in class AbstractRealMatrix
        
        Returns:
            2-dimensional array of entries
        
        
        """
        ...
    def getDataRef(self) -> typing.MutableSequence[float]:
        """
        Gets a reference to the underlying data array.
        
        Returns:
            1-dimensional array of entries.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> float:
        """
        Get the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: getEntry in interface RealMatrix
        
        Specified by: getEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be fetched.
            column (int): Column index of entry to be fetched.
        
        Returns:
            the matrix entry at (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows of this matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in interface RealLinearOperator
        
        Specified by: getRowDimension in class AbstractRealMatrix
        
        Returns:
            the number of rows.
        
        
        """
        ...
    @typing.overload
    def inverse(self) -> 'DiagonalMatrix': ...
    @typing.overload
    def inverse(self, double: float) -> 'DiagonalMatrix': ...
    def isSingular(self, threshold: float) -> bool:
        """
        Returns whether this diagonal matrix is singular, i.e. any diagonal entry is equal to  within the given threshold.
        
        Parameters:
            threshold (double): Singularity threshold.
        
        Returns:
            true if the matrix is singular, false otherwise
        
        
        """
        ...
    @typing.overload
    def multiply(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, row: int, column: int, factor: float) -> None:
        """
        Multiplies (in place) the specified entry of this matrix by the specified value. Row and column indices start at 0.
        
        Specified by: multiplyEntry in interface RealMatrix
        
        Overrides: multiplyEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            factor (double): Multiplication factor for the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    @typing.overload
    def multiplyTransposed(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def multiplyTransposed(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def operate(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def operate(self, realVector: RealVector) -> RealVector: ...
    @typing.overload
    def preMultiply(self, doubleArray: typing.Union[typing.List[float], jpype.JArray]) -> typing.MutableSequence[float]: ...
    @typing.overload
    def preMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def preMultiply(self, realVector: RealVector) -> RealVector: ...
    def setEntry(self, row: int, column: int, value: float) -> None:
        """
        Set the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: setEntry in interface RealMatrix
        
        Specified by: setEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be set.
            column (int): Column index of entry to be set.
            value (double): the new value of the entry.
        
        Raises:
            MathIllegalArgumentException: if row != column and value is non-zero.
        
        
        """
        ...
    @typing.overload
    def subtract(self, diagonalMatrix: 'DiagonalMatrix') -> 'DiagonalMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> RealMatrix: ...
    @typing.overload
    def transposeMultiply(self, m: 'DiagonalMatrix') -> 'DiagonalMatrix':
        """
        Returns the result of postmultiplying this^T by m.
        
        This is equivalent to call transpose.multiply, but some implementations may avoid building the intermediate transposed matrix.
        
        Specified by: transposeMultiply in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to postmultiply by
        
        Returns:
            this^T * m
        
        
        """
        ...
    @typing.overload
    def transposeMultiply(self, realMatrix: RealMatrix) -> RealMatrix: ...

class OpenMapRealMatrix(AbstractRealMatrix, SparseRealMatrix, java.io.Serializable):
    """
    implements SparseRealMatrix, Serializable
    
    Sparse matrix implementation based on an open addressed map.
    
    Caveat: This implementation assumes that, for any x, the equality x * 0d == 0d holds. But it is is not true for NaN. Moreover, zero entries will lose their sign. Some operations (that involve NaN and/or infinities) may thus give incorrect results.
    
          - serialized
    """
    @typing.overload
    def __init__(self, int: int, int2: int): ...
    @typing.overload
    def __init__(self, openMapRealMatrix: 'OpenMapRealMatrix'): ...
    @typing.overload
    def add(self, openMapRealMatrix: 'OpenMapRealMatrix') -> 'OpenMapRealMatrix': ...
    @typing.overload
    def add(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def addToEntry(self, row: int, column: int, increment: float) -> None:
        """
        Adds (in place) the specified value to the specified entry of this matrix. Row and column indices start at 0.
        
        Specified by: addToEntry in interface RealMatrix
        
        Overrides: addToEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            increment (double): value to add to the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def copy(self) -> 'OpenMapRealMatrix':
        """
        Returns a (deep) copy of this.
        
        Specified by: copy in interface RealMatrix
        
        Specified by: copy in class AbstractRealMatrix
        
        Returns:
            matrix copy
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> 'OpenMapRealMatrix':
        """
        Create a new RealMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface RealMatrix
        
        Specified by: createMatrix in class AbstractRealMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        Raises:
            MathIllegalArgumentException: if the total number of entries of the matrix is larger than MAX_VALUE.
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns of this matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in interface RealLinearOperator
        
        Specified by: getColumnDimension in class AbstractRealMatrix
        
        Returns:
            the number of columns.
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> float:
        """
        Get the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: getEntry in interface RealMatrix
        
        Specified by: getEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be fetched.
            column (int): Column index of entry to be fetched.
        
        Returns:
            the matrix entry at (row, column).
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows of this matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in interface RealLinearOperator
        
        Specified by: getRowDimension in class AbstractRealMatrix
        
        Returns:
            the number of rows.
        
        
        """
        ...
    @typing.overload
    def multiply(self, openMapRealMatrix: 'OpenMapRealMatrix') -> 'OpenMapRealMatrix': ...
    @typing.overload
    def multiply(self, realMatrix: RealMatrix) -> RealMatrix: ...
    def multiplyEntry(self, row: int, column: int, factor: float) -> None:
        """
        Multiplies (in place) the specified entry of this matrix by the specified value. Row and column indices start at 0.
        
        Specified by: multiplyEntry in interface RealMatrix
        
        Overrides: multiplyEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of the entry to be modified.
            column (int): Column index of the entry to be modified.
            factor (double): Multiplication factor for the matrix entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid.
        
        
        """
        ...
    def multiplyTransposed(self, m: RealMatrix) -> RealMatrix:
        """
        Returns the result of postmultiplying this by m^T.
        
        This is equivalent to call multiply(m.transpose), but some implementations may avoid building the intermediate transposed matrix.
        
        Specified by: multiplyTransposed in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to first transpose and second postmultiply by
        
        Returns:
            this * m^T
        
        Raises:
            MathIllegalArgumentException: if m is an OpenMapRealMatrix, and the total number of entries of the product is larger than
                MAX_VALUE.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: float) -> None:
        """
        Set the entry in the specified row and column. Row and column indices start at 0.
        
        Specified by: setEntry in interface RealMatrix
        
        Specified by: setEntry in class AbstractRealMatrix
        
        Parameters:
            row (int): Row index of entry to be set.
            column (int): Column index of entry to be set.
            value (double): the new value of the entry.
        
        Raises:
            MathIllegalArgumentException: if the row or column index is not valid
        
        
        """
        ...
    @typing.overload
    def subtract(self, openMapRealMatrix: 'OpenMapRealMatrix') -> 'OpenMapRealMatrix': ...
    @typing.overload
    def subtract(self, realMatrix: RealMatrix) -> 'OpenMapRealMatrix': ...
    def transposeMultiply(self, m: RealMatrix) -> RealMatrix:
        """
        Returns the result of postmultiplying this^T by m.
        
        This is equivalent to call transpose.multiply, but some implementations may avoid building the intermediate transposed matrix.
        
        Specified by: transposeMultiply in interface RealMatrix
        
        Parameters:
            m (RealMatrix): matrix to postmultiply by
        
        Returns:
            this^T * m
        
        Raises:
            MathIllegalArgumentException: if m is an OpenMapRealMatrix, and the total number of entries of the product is larger than
                MAX_VALUE.
        
        
        """
        ...

_SparseFieldMatrix__T = typing.TypeVar('_SparseFieldMatrix__T', bound=org.hipparchus.FieldElement)  # <T>
class SparseFieldMatrix(AbstractFieldMatrix[_SparseFieldMatrix__T], typing.Generic[_SparseFieldMatrix__T]):
    """
    Sparse matrix implementation based on an open addressed map.
    
    Caveat: This implementation assumes that, for any x, the equality x * 0d == 0d holds. But it is is not true for NaN. Moreover, zero entries will lose their sign. Some operations (that involve NaN and/or infinities) may thus give incorrect results.
    """
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, field: org.hipparchus.Field[_SparseFieldMatrix__T], int: int, int2: int): ...
    @typing.overload
    def __init__(self, fieldMatrix: FieldMatrix[_SparseFieldMatrix__T]): ...
    @typing.overload
    def __init__(self, sparseFieldMatrix: 'SparseFieldMatrix'[_SparseFieldMatrix__T]): ...
    def addToEntry(self, row: int, column: int, increment: _SparseFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: addToEntry in interface FieldMatrix
        
        Specified by: addToEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            increment (SparseFieldMatrix): Value to add to the current matrix entry in (row, column).
        
        
        """
        ...
    def copy(self) -> FieldMatrix[_SparseFieldMatrix__T]:
        """
        Make a (deep) copy of this.
        
        Specified by: copy in interface FieldMatrix
        
        Specified by: copy in class AbstractFieldMatrix
        
        Returns:
            a copy of this matrix.
        
        
        """
        ...
    def createMatrix(self, rowDimension: int, columnDimension: int) -> FieldMatrix[_SparseFieldMatrix__T]:
        """
        Create a new FieldMatrix of the same type as the instance with the supplied row and column dimensions.
        
        Specified by: createMatrix in interface FieldMatrix
        
        Specified by: createMatrix in class AbstractFieldMatrix
        
        Parameters:
            rowDimension (int): the number of rows in the new matrix
            columnDimension (int): the number of columns in the new matrix
        
        Returns:
            a new matrix of the same type as the instance
        
        
        """
        ...
    def getColumnDimension(self) -> int:
        """
        Returns the number of columns in the matrix.
        
        Specified by: getColumnDimension in interface AnyMatrix
        
        Specified by: getColumnDimension in class AbstractFieldMatrix
        
        Returns:
            columnDimension
        
        
        """
        ...
    def getEntry(self, row: int, column: int) -> _SparseFieldMatrix__T:
        """
        Returns the entry in the specified row and column.
        
        Specified by: getEntry in interface FieldMatrix
        
        Specified by: getEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): row location of entry to be fetched
            column (int): column location of entry to be fetched
        
        Returns:
            matrix entry in row,column
        
        
        """
        ...
    def getRowDimension(self) -> int:
        """
        Returns the number of rows in the matrix.
        
        Specified by: getRowDimension in interface AnyMatrix
        
        Specified by: getRowDimension in class AbstractFieldMatrix
        
        Returns:
            rowDimension
        
        
        """
        ...
    def multiplyEntry(self, row: int, column: int, factor: _SparseFieldMatrix__T) -> None:
        """
        Change an entry in the specified row and column.
        
        Specified by: multiplyEntry in interface FieldMatrix
        
        Specified by: multiplyEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): Row location of entry to be set.
            column (int): Column location of entry to be set.
            factor (SparseFieldMatrix): Multiplication factor for the current matrix entry in (row,column)
        
        
        """
        ...
    def multiplyTransposed(self, m: FieldMatrix[_SparseFieldMatrix__T]) -> FieldMatrix[_SparseFieldMatrix__T]:
        """
        Returns the result of postmultiplying this by m^T.
        
        This is equivalent to call multiply(m.transpose), but some implementations may avoid building the intermediate transposed matrix.
        
        Parameters:
            m (FieldMatrix<SparseFieldMatrix> m): matrix to first transpose and second postmultiply by
        
        Returns:
            this * m^T
        
        Raises:
            MathIllegalArgumentException: if m is an OpenMapRealMatrix, and the total number of entries of the product is larger than
                MAX_VALUE.
        
        
        """
        ...
    def setEntry(self, row: int, column: int, value: _SparseFieldMatrix__T) -> None:
        """
        Set the entry in the specified row and column.
        
        Specified by: setEntry in interface FieldMatrix
        
        Specified by: setEntry in class AbstractFieldMatrix
        
        Parameters:
            row (int): row location of entry to be set
            column (int): column location of entry to be set
            value (SparseFieldMatrix): matrix entry to be set in row,column
        
        
        """
        ...
    def transposeMultiply(self, m: FieldMatrix[_SparseFieldMatrix__T]) -> FieldMatrix[_SparseFieldMatrix__T]:
        """
        Returns the result of postmultiplying this^T by m.
        
        This is equivalent to call transpose.multiply, but some implementations may avoid building the intermediate transposed matrix.
        
        Parameters:
            m (FieldMatrix<SparseFieldMatrix> m): matrix to postmultiply by
        
        Returns:
            this^T * m
        
        Raises:
            MathIllegalArgumentException: if m is an OpenMapRealMatrix, and the total number of entries of the product is larger than
                MAX_VALUE.
        
        
        """
        ...


class __module_protocol__(Protocol):
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
    DependentVectorsHandler: typing.Type[DependentVectorsHandler]
    DiagonalMatrix: typing.Type[DiagonalMatrix]
    EigenDecompositionNonSymmetric: typing.Type[EigenDecompositionNonSymmetric]
    EigenDecompositionSymmetric: typing.Type[EigenDecompositionSymmetric]
    FieldDecompositionSolver: typing.Type[FieldDecompositionSolver]
    FieldLUDecomposer: typing.Type[FieldLUDecomposer]
    FieldLUDecomposition: typing.Type[FieldLUDecomposition]
    FieldMatrix: typing.Type[FieldMatrix]
    FieldMatrixChangingVisitor: typing.Type[FieldMatrixChangingVisitor]
    FieldMatrixDecomposer: typing.Type[FieldMatrixDecomposer]
    FieldMatrixPreservingVisitor: typing.Type[FieldMatrixPreservingVisitor]
    FieldQRDecomposer: typing.Type[FieldQRDecomposer]
    FieldQRDecomposition: typing.Type[FieldQRDecomposition]
    FieldVector: typing.Type[FieldVector]
    FieldVectorChangingVisitor: typing.Type[FieldVectorChangingVisitor]
    FieldVectorPreservingVisitor: typing.Type[FieldVectorPreservingVisitor]
    HessenbergTransformer: typing.Type[HessenbergTransformer]
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
    SchurTransformer: typing.Type[SchurTransformer]
    SemiDefinitePositiveCholeskyDecomposition: typing.Type[SemiDefinitePositiveCholeskyDecomposition]
    SingularValueDecomposer: typing.Type[SingularValueDecomposer]
    SingularValueDecomposition: typing.Type[SingularValueDecomposition]
    SparseFieldMatrix: typing.Type[SparseFieldMatrix]
    SparseFieldVector: typing.Type[SparseFieldVector]
    SparseRealMatrix: typing.Type[SparseRealMatrix]
    SparseRealVector: typing.Type[SparseRealVector]
    SymmLQ: typing.Type[SymmLQ]
