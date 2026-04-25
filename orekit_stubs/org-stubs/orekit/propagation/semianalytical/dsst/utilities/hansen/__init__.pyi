
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import org.hipparchus
import org.hipparchus.analysis.polynomials
import typing



_FieldHansenTesseralLinear__T = typing.TypeVar('_FieldHansenTesseralLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenTesseralLinear(typing.Generic[_FieldHansenTesseralLinear__T]):
    """
    Hansen coefficients K(t,n,s) for t!=0 and n < 0.
    
    Implements Collins 4-236 or Danielson 2.7.3-(9) for Hansen Coefficients and Collins 4-240 for derivatives. The recursions are transformed into composition of linear transformations to obtain the associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, nMax: int, s: int, j: int, n0: int, maxHansen: int, field: org.hipparchus.Field[_FieldHansenTesseralLinear__T]):
        """
        Constructor.
        
        Parameters:
            nMax (int): the maximum (absolute) value of n parameter
            s (int): s parameter
            j (int): j parameter
            n0 (int): the minimum (absolute) value of n
            maxHansen (int): maximum power of the eccentricity to use in Hansen coefficient Kernel expansion.
            field (Field<FieldHansenTesseralLinear> field): field used by default
        
        
        """
        ...
    def computeInitValues(self, e2: _FieldHansenTesseralLinear__T, chi: _FieldHansenTesseralLinear__T, chi2: _FieldHansenTesseralLinear__T) -> None:
        """
        Compute the values for the first four coefficients and their derivatives by means of series.
        
        Parameters:
            e2 (FieldHansenTesseralLinear): e²
            chi (FieldHansenTesseralLinear): Χ
            chi2 (FieldHansenTesseralLinear): Χ²
        
        
        """
        ...
    def getDerivative(self, mnm1: int, chi: _FieldHansenTesseralLinear__T) -> _FieldHansenTesseralLinear__T:
        """
        Compute the value of the derivative dK :sub:`j` :sup:`-n-1, s` / de².
        
        Parameters:
            mnm1 (int): -n-1
            chi (FieldHansenTesseralLinear): χ
        
        Returns:
            the derivative dK :sub:`j` :sup:`-n-1, s` / de²
        
        
        """
        ...
    def getValue(self, mnm1: int, chi: _FieldHansenTesseralLinear__T) -> _FieldHansenTesseralLinear__T:
        """
        Compute the value of the Hansen coefficient K :sub:`j` :sup:`-n-1, s` .
        
        Parameters:
            mnm1 (int): -n-1
            chi (FieldHansenTesseralLinear): χ
        
        Returns:
            the coefficient K :sub:`j` :sup:`-n-1, s`
        
        
        """
        ...

_FieldHansenThirdBodyLinear__T = typing.TypeVar('_FieldHansenThirdBodyLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenThirdBodyLinear(typing.Generic[_FieldHansenThirdBodyLinear__T]):
    """
    Hansen coefficients K(t,n,s) for t=0 and n > 0.
    
    Implements Collins 4-254 or Danielson 2.7.3-(7) for Hansen Coefficients and Danielson 3.2-(3) for derivatives. The recursions are transformed into composition of linear transformations to obtain the associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, nMax: int, s: int, field: org.hipparchus.Field[_FieldHansenThirdBodyLinear__T]):
        """
        Constructor.
        
        Parameters:
            nMax (int): the maximum value of n
            s (int): the value of s
            field (Field<FieldHansenThirdBodyLinear> field): field used by default
        
        
        """
        ...
    def computeInitValues(self, chitm1: _FieldHansenThirdBodyLinear__T, chitm2: _FieldHansenThirdBodyLinear__T, chitm3: _FieldHansenThirdBodyLinear__T) -> None:
        """
        Compute the initial values (see Collins, 4-255, 4-256 and 4.259)
        
        K₀ :sup:`s, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+1)! )
        
        K₀ :sup:`s+1, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+2)! ) * (2*s+3 - χ :sup:`-2` )
        
        dK₀ :sup:`s+1, s` / dχ = = (-1) :sup:`s` * 2 * ( (2*s+1)!! / (s+2)! ) * χ :sup:`-3`
        
        Parameters:
            chitm1 (FieldHansenThirdBodyLinear): sqrt(1 - e²)
            chitm2 (FieldHansenThirdBodyLinear): sqrt(1 - e²)²
            chitm3 (FieldHansenThirdBodyLinear): sqrt(1 - e²)³
        
        
        """
        ...
    def getDerivative(self, n: int, chitm1: _FieldHansenThirdBodyLinear__T) -> _FieldHansenThirdBodyLinear__T:
        """
        Compute the value of the Hansen coefficient dK₀ :sup:`n, s` / dΧ.
        
        Parameters:
            n (int): n value
            chitm1 (FieldHansenThirdBodyLinear): χ :sup:`-1`
        
        Returns:
            the coefficient dK₀ :sup:`n, s` / dΧ
        
        
        """
        ...
    def getValue(self, n: int, chitm1: _FieldHansenThirdBodyLinear__T) -> _FieldHansenThirdBodyLinear__T:
        """
        Compute the value of the Hansen coefficient K₀ :sup:`n, s` .
        
        Parameters:
            n (int): n value
            chitm1 (FieldHansenThirdBodyLinear): χ :sup:`-1`
        
        Returns:
            the coefficient K₀ :sup:`n, s`
        
        
        """
        ...

_FieldHansenZonalLinear__T = typing.TypeVar('_FieldHansenZonalLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenZonalLinear(typing.Generic[_FieldHansenZonalLinear__T]):
    """
    Hansen coefficients K(t,n,s) for t=0 and n < 0.
    
    Implements Collins 4-242 or echivalently, Danielson 2.7.3-(6) for Hansen Coefficients and Collins 4-245 or Danielson 3.1-(7) for derivatives. The recursions are transformed into composition of linear transformations to obtain the associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, nMax: int, s: int, field: org.hipparchus.Field[_FieldHansenZonalLinear__T]):
        """
        Constructor.
        
        Parameters:
            nMax (int): the maximum (absolute) value of n coefficient
            s (int): s coefficient
            field (Field<FieldHansenZonalLinear> field): field used by default
        
        
        """
        ...
    def computeInitValues(self, chi: _FieldHansenZonalLinear__T) -> None:
        """
        Compute the roots for the Hansen coefficients and their derivatives.
        
        Parameters:
            chi (FieldHansenZonalLinear): 1 / sqrt(1 - e²)
        
        
        """
        ...
    def getDerivative(self, mnm1: int, chi: _FieldHansenZonalLinear__T) -> _FieldHansenZonalLinear__T:
        """
        Get the dK₀ :sup:`-n-1,s` / dΧ coefficient derivative.
        
        The s value is given in the class constructor.
        
        Parameters:
            mnm1 (int): (-n-1) coefficient
            chi (FieldHansenZonalLinear): The value of χ
        
        Returns:
            dK₀ :sup:`-n-1,s` / dΧ
        
        
        """
        ...
    def getValue(self, mnm1: int, chi: _FieldHansenZonalLinear__T) -> _FieldHansenZonalLinear__T:
        """
        Get the K₀ :sup:`-n-1,s` coefficient value.
        
        The s value is given in the class constructor
        
        Parameters:
            mnm1 (int): (-n-1) coefficient
            chi (FieldHansenZonalLinear): The value of χ
        
        Returns:
            K₀ :sup:`-n-1,s`
        
        
        """
        ...

class HansenTesseralLinear:
    """
    Hansen coefficients K(t,n,s) for t!=0 and n < 0.
    
    Implements Collins 4-236 or Danielson 2.7.3-(9) for Hansen Coefficients and Collins 4-240 for derivatives. The recursions are transformed into composition of linear transformations to obtain the associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, nMax: int, s: int, j: int, n0: int, maxHansen: int):
        """
        Constructor.
        
        Parameters:
            nMax (int): the maximum (absolute) value of n parameter
            s (int): s parameter
            j (int): j parameter
            n0 (int): the minimum (absolute) value of n
            maxHansen (int): maximum power of e2 in Hansen expansion
        
        
        """
        ...
    def computeInitValues(self, e2: float, chi: float, chi2: float) -> None:
        """
        Compute the values for the first four coefficients and their derivatives by means of series.
        
        Parameters:
            e2 (double): e²
            chi (double): Χ
            chi2 (double): Χ²
        
        
        """
        ...
    def getDerivative(self, mnm1: int, chi: float) -> float:
        """
        Compute the value of the derivative dK :sub:`j` :sup:`-n-1, s` / de².
        
        Parameters:
            mnm1 (int): -n-1
            chi (double): χ
        
        Returns:
            the derivative dK :sub:`j` :sup:`-n-1, s` / de²
        
        
        """
        ...
    def getValue(self, mnm1: int, chi: float) -> float:
        """
        Compute the value of the Hansen coefficient K :sub:`j` :sup:`-n-1, s` .
        
        Parameters:
            mnm1 (int): -n-1
            chi (double): χ
        
        Returns:
            the coefficient K :sub:`j` :sup:`-n-1, s`
        
        
        """
        ...

class HansenThirdBodyLinear:
    """
    Hansen coefficients K(t,n,s) for t=0 and n > 0.
    
    Implements Collins 4-254 or Danielson 2.7.3-(7) for Hansen Coefficients and Danielson 3.2-(3) for derivatives. The recursions are transformed into composition of linear transformations to obtain the associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, nMax: int, s: int):
        """
        Constructor.
        
        Parameters:
            nMax (int): the maximum value of n
            s (int): the value of s
        
        
        """
        ...
    def computeInitValues(self, chitm1: float, chitm2: float, chitm3: float) -> None:
        """
        Compute the initial values (see Collins, 4-255, 4-256 and 4.259)
        
        K₀ :sup:`s, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+1)! )
        
        K₀ :sup:`s+1, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+2)! ) * (2*s+3 - χ :sup:`-2` )
        
        dK₀ :sup:`s+1, s` / dχ = = (-1) :sup:`s` * 2 * ( (2*s+1)!! / (s+2)! ) * χ :sup:`-3`
        
        Parameters:
            chitm1 (double): sqrt(1 - e²)
            chitm2 (double): sqrt(1 - e²)²
            chitm3 (double): sqrt(1 - e²)³
        
        
        """
        ...
    def getDerivative(self, n: int, chitm1: float) -> float:
        """
        Compute the value of the Hansen coefficient dK₀ :sup:`n, s` / dΧ.
        
        Parameters:
            n (int): n value
            chitm1 (double): χ :sup:`-1`
        
        Returns:
            the coefficient dK₀ :sup:`n, s` / dΧ
        
        
        """
        ...
    def getValue(self, n: int, chitm1: float) -> float:
        """
        Compute the value of the Hansen coefficient K₀ :sup:`n, s` .
        
        Parameters:
            n (int): n value
            chitm1 (double): χ :sup:`-1`
        
        Returns:
            the coefficient K₀ :sup:`n, s`
        
        
        """
        ...

class HansenUtilities:
    """
    Utilities class.
    """
    ONE: typing.ClassVar[org.hipparchus.analysis.polynomials.PolynomialFunction] = ...
    """
    1 represented as a polynomial.
    """
    ZERO: typing.ClassVar[org.hipparchus.analysis.polynomials.PolynomialFunction] = ...
    """
    0 represented as a polynomial.
    """
    @staticmethod
    def buildIdentityMatrix2() -> 'PolynomialFunctionMatrix':
        """
        Build the identity matrix of order 2.
        
               / 1   0 \ I₂ = |       | \ 0   1 /
        
        Returns:
            the identity matrix of order 2
        
        
        """
        ...
    @staticmethod
    def buildIdentityMatrix4() -> 'PolynomialFunctionMatrix':
        """
        Build the identity matrix of order 4.
        
               / 1  0  0  0 \ |            | | 0  1  0  0 | I₄ = |            | | 0  0  1  0 | |            | \ 0  0  0  1 /
        
        Returns:
            the identity matrix of order 4
        
        
        """
        ...
    @staticmethod
    def buildZeroMatrix2() -> 'PolynomialFunctionMatrix':
        """
        Build the empty matrix of order 2.
        
               / 0   0 \ E₂ = |       | \ 0   0 /
        
        Returns:
            the identity matrix of order 2
        
        
        """
        ...
    @staticmethod
    def buildZeroMatrix4() -> 'PolynomialFunctionMatrix':
        """
        Build the empty matrix of order 4.
        
               / 0  0  0  0 \ |            | | 0  0  0  0 | E₄ = |            | | 0  0  0  0 | |            | \ 0  0  0  0 /
        
        Returns:
            the identity matrix of order 4
        
        
        """
        ...
    @staticmethod
    def generateTesseralPolynomials(n0: int, nMin: int, offset: int, slice: int, j: int, s: int, mpvec: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray], mpvecDeriv: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray]) -> None:
        """
        Generate the polynomials needed in the linear transformation.
        
        Parameters:
            n0 (int): the index of the initial condition, Petre's paper
            nMin (int): rhe minimum value for the order
            offset (int): offset used to identify the polynomial that corresponds to a negative value of n in the internal array that starts at 0
            slice (int): number of coefficients that will be computed with a set of roots
            j (int): the j coefficient
            s (int): the s coefficient
            mpvec (PolynomialFunction[][]): array to store the first vector of polynomials associated to Hansen coefficients and derivatives.
            mpvecDeriv (PolynomialFunction[][]): array to store the second vector of polynomials associated only to derivatives.
        
        
        """
        ...
    @staticmethod
    def generateThirdBodyPolynomials(n0: int, nMax: int, slice: int, s: int, mpvec: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray], mpvecDeriv: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray]) -> None:
        """
        Generate the polynomials needed in the linear transformation.
        
        Parameters:
            n0 (int): the index of the initial condition, Petre's paper
            nMax (int): the maximum order of n indexes
            slice (int): number of coefficients that will be computed with a set of roots
            s (int): the s coefficient
            mpvec (PolynomialFunction[][]): array to store the first vector of polynomials associated to Hansen coefficients and derivatives.
            mpvecDeriv (PolynomialFunction[][]): array to store the second vector of polynomials associated only to derivatives.
        
                See Petre's paper
        
        
        """
        ...
    @staticmethod
    def generateZonalPolynomials(n0: int, nMin: int, offset: int, slice: int, s: int, mpvec: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray], mpvecDeriv: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray]) -> None:
        """
        Generate the polynomials needed in the linear transformation.
        
        Parameters:
            n0 (int): the index of the initial condition, Petre's paper
            nMin (int): rhe minimum value for the order
            offset (int): offset used to identify the polynomial that corresponds to a negative value of n in the internal array that starts at 0
            slice (int): number of coefficients that will be computed with a set of roots
            s (int): the s coefficient
            mpvec (PolynomialFunction[][]): array to store the first vector of polynomials associated to Hansen coefficients and derivatives.
            mpvecDeriv (PolynomialFunction[][]): array to store the second vector of polynomials associated only to derivatives.
        
                See Petre's paper
        
        
        """
        ...

class HansenZonalLinear:
    """
    Hansen coefficients K(t,n,s) for t=0 and n < 0.
    
    Implements Collins 4-242 or echivalently, Danielson 2.7.3-(6) for Hansen Coefficients and Collins 4-245 or Danielson 3.1-(7) for derivatives. The recursions are transformed into composition of linear transformations to obtain the associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, nMax: int, s: int):
        """
        Constructor.
        
        Parameters:
            nMax (int): the maximum (absolute) value of n coefficient
            s (int): s coefficient
        
        
        """
        ...
    def computeInitValues(self, chi: float) -> None:
        """
        Compute the roots for the Hansen coefficients and their derivatives.
        
        Parameters:
            chi (double): 1 / sqrt(1 - e²)
        
        
        """
        ...
    def getDerivative(self, mnm1: int, chi: float) -> float:
        """
        Get the dK₀ :sup:`-n-1,s` / dΧ coefficient derivative.
        
        The s value is given in the class constructor.
        
        Parameters:
            mnm1 (int): (-n-1) coefficient
            chi (double): The value of χ
        
        Returns:
            dK₀ :sup:`-n-1,s` / dΧ
        
        
        """
        ...
    def getValue(self, mnm1: int, chi: float) -> float:
        """
        Get the K₀ :sup:`-n-1,s` coefficient value.
        
        The s value is given in the class constructor
        
        Parameters:
            mnm1 (int): (-n-1) coefficient
            chi (double): The value of χ
        
        Returns:
            K₀ :sup:`-n-1,s`
        
        
        """
        ...

class PolynomialFunctionMatrix:
    """
    A quadratic matrix of PolynomialFunction.
    """
    def add(self, matrix: 'PolynomialFunctionMatrix') -> 'PolynomialFunctionMatrix':
        """
        Add the argument matrix with the current matrix.
        
        Parameters:
            matrix (PolynomialFunctionMatrix): the argument matrix
        
        Returns:
            the result of the addition
        
        
        """
        ...
    def getElem(self, line: int, column: int) -> org.hipparchus.analysis.polynomials.PolynomialFunction:
        """
        Get the value of an element.
        
        Parameters:
            line (int): the line
            column (int): the column
        
        Returns:
            the value
        
        
        """
        ...
    def getMatrixLine(self, line: int) -> typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]:
        """
        Get a line of the matrix.
        
        Parameters:
            line (int): the line number
        
        Returns:
            the line of the matrix as a vector
        
        
        """
        ...
    def multiply(self, matrix: 'PolynomialFunctionMatrix') -> 'PolynomialFunctionMatrix':
        """
        Multiply the argument matrix with the current matrix.
        
        Parameters:
            matrix (PolynomialFunctionMatrix): the argument matrix
        
        Returns:
            the result of the multiplication
        
        
        """
        ...
    def setElem(self, line: int, column: int, value: org.hipparchus.analysis.polynomials.PolynomialFunction) -> None:
        """
        Set an element of the matrix.
        
        Parameters:
            line (int): the line
            column (int): the column
            value (PolynomialFunction): the value
        
        
        """
        ...
    def setMatrix(self, polynomials: typing.Union[typing.List[typing.MutableSequence[org.hipparchus.analysis.polynomials.PolynomialFunction]], jpype.JArray]) -> None:
        """
        Set values for all elements.
        
        Parameters:
            polynomials (PolynomialFunction[][]): the values that will be used for the matrix
        
        
        """
        ...
    def setMatrixLine(self, line: int, polynomials: typing.Union[typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction], jpype.JArray]) -> None:
        """
        Set the value of a line of the matrix.
        
        Parameters:
            line (int): the line number
            polynomials (PolynomialFunction[]): the values to set
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst.utilities.hansen")``.

    FieldHansenTesseralLinear: typing.Type[FieldHansenTesseralLinear]
    FieldHansenThirdBodyLinear: typing.Type[FieldHansenThirdBodyLinear]
    FieldHansenZonalLinear: typing.Type[FieldHansenZonalLinear]
    HansenTesseralLinear: typing.Type[HansenTesseralLinear]
    HansenThirdBodyLinear: typing.Type[HansenThirdBodyLinear]
    HansenUtilities: typing.Type[HansenUtilities]
    HansenZonalLinear: typing.Type[HansenZonalLinear]
    PolynomialFunctionMatrix: typing.Type[PolynomialFunctionMatrix]
