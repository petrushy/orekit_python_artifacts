import org.hipparchus
import org.hipparchus.analysis.polynomials
import typing



_FieldHansenTesseralLinear__T = typing.TypeVar('_FieldHansenTesseralLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenTesseralLinear(typing.Generic[_FieldHansenTesseralLinear__T]):
    """
    public class FieldHansenTesseralLinear<T extends CalculusFieldElement<T>> extends Object
    
        Hansen coefficients K(t,n,s) for t!=0 and n < 0.
    
        Implements Collins 4-236 or Danielson 2.7.3-(9) for Hansen Coefficients and Collins 4-240 for derivatives. The
        recursions are transformed into composition of linear transformations to obtain the associated polynomials for
        coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int, field: org.hipparchus.Field[_FieldHansenTesseralLinear__T]): ...
    def computeInitValues(self, t: _FieldHansenTesseralLinear__T, t2: _FieldHansenTesseralLinear__T, t3: _FieldHansenTesseralLinear__T) -> None:
        """
            Compute the values for the first four coefficients and their derivatives by means of series.
        
            Parameters:
                e2 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenTesseralLinear`): eÂ²
                chi (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenTesseralLinear`): Χ
                chi2 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenTesseralLinear`): ΧÂ²
        
        
        """
        ...
    def getDerivative(self, int: int, t: _FieldHansenTesseralLinear__T) -> _FieldHansenTesseralLinear__T:
        """
            Compute the value of the derivative dK :sub:`j` :sup:`-n-1, s` / deÂ².
        
            Parameters:
                mnm1 (int): -n-1
                chi (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenTesseralLinear`): Ï‡
        
            Returns:
                the derivative dK :sub:`j` :sup:`-n-1, s` / deÂ²
        
        
        """
        ...
    def getValue(self, int: int, t: _FieldHansenTesseralLinear__T) -> _FieldHansenTesseralLinear__T:
        """
            Compute the value of the Hansen coefficient K :sub:`j` :sup:`-n-1, s` .
        
            Parameters:
                mnm1 (int): -n-1
                chi (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenTesseralLinear`): Ï‡
        
            Returns:
                the coefficient K :sub:`j` :sup:`-n-1, s`
        
        
        """
        ...

_FieldHansenThirdBodyLinear__T = typing.TypeVar('_FieldHansenThirdBodyLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenThirdBodyLinear(typing.Generic[_FieldHansenThirdBodyLinear__T]):
    """
    public class FieldHansenThirdBodyLinear<T extends CalculusFieldElement<T>> extends Object
    
        Hansen coefficients K(t,n,s) for t=0 and n > 0.
    
        Implements Collins 4-254 or Danielson 2.7.3-(7) for Hansen Coefficients and Danielson 3.2-(3) for derivatives. The
        recursions are transformed into composition of linear transformations to obtain the associated polynomials for
        coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, int: int, int2: int, field: org.hipparchus.Field[_FieldHansenThirdBodyLinear__T]): ...
    def computeInitValues(self, t: _FieldHansenThirdBodyLinear__T, t2: _FieldHansenThirdBodyLinear__T, t3: _FieldHansenThirdBodyLinear__T) -> None:
        """
            Compute the initial values (see Collins, 4-255, 4-256 and 4.259)
        
            Kâ‚€ :sup:`s, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+1)! )
        
            Kâ‚€ :sup:`s+1, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+2)! ) * (2*s+3 - Ï‡ :sup:`-2` )
        
            dKâ‚€ :sup:`s+1, s` / dÏ‡ = = (-1) :sup:`s` * 2 * ( (2*s+1)!! / (s+2)! ) * Ï‡ :sup:`-3`
        
            Parameters:
                chitm1 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenThirdBodyLinear`): sqrt(1 - eÂ²)
                chitm2 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenThirdBodyLinear`): sqrt(1 - eÂ²)Â²
                chitm3 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenThirdBodyLinear`): sqrt(1 - eÂ²)Â³
        
        
        """
        ...
    def getDerivative(self, int: int, t: _FieldHansenThirdBodyLinear__T) -> _FieldHansenThirdBodyLinear__T:
        """
            Compute the value of the Hansen coefficient dKâ‚€ :sup:`n, s` / dΧ.
        
            Parameters:
                n (int): n value
                chitm1 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenThirdBodyLinear`): Ï‡ :sup:`-1`
        
            Returns:
                the coefficient dKâ‚€ :sup:`n, s` / dΧ
        
        
        """
        ...
    def getValue(self, int: int, t: _FieldHansenThirdBodyLinear__T) -> _FieldHansenThirdBodyLinear__T:
        """
            Compute the value of the Hansen coefficient Kâ‚€ :sup:`n, s` .
        
            Parameters:
                n (int): n value
                chitm1 (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenThirdBodyLinear`): Ï‡ :sup:`-1`
        
            Returns:
                the coefficient Kâ‚€ :sup:`n, s`
        
        
        """
        ...

_FieldHansenZonalLinear__T = typing.TypeVar('_FieldHansenZonalLinear__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldHansenZonalLinear(typing.Generic[_FieldHansenZonalLinear__T]):
    """
    public class FieldHansenZonalLinear<T extends CalculusFieldElement<T>> extends Object
    
        Hansen coefficients K(t,n,s) for t=0 and n < 0.
    
        Implements Collins 4-242 or echivalently, Danielson 2.7.3-(6) for Hansen Coefficients and Collins 4-245 or Danielson
        3.1-(7) for derivatives. The recursions are transformed into composition of linear transformations to obtain the
        associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, int: int, int2: int, field: org.hipparchus.Field[_FieldHansenZonalLinear__T]): ...
    def computeInitValues(self, t: _FieldHansenZonalLinear__T) -> None:
        """
            Compute the roots for the Hansen coefficients and their derivatives.
        
            Parameters:
                chi (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenZonalLinear`): 1 / sqrt(1 - eÂ²)
        
        
        """
        ...
    def getDerivative(self, int: int, t: _FieldHansenZonalLinear__T) -> _FieldHansenZonalLinear__T:
        """
            Get the dKâ‚€ :sup:`-n-1,s` / dΧ coefficient derivative.
        
            The s value is given in the class constructor.
        
            Parameters:
                mnm1 (int): (-n-1) coefficient
                chi (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenZonalLinear`): The value of Ï‡
        
            Returns:
                dKâ‚€ :sup:`-n-1,s` / dΧ
        
        
        """
        ...
    def getValue(self, int: int, t: _FieldHansenZonalLinear__T) -> _FieldHansenZonalLinear__T:
        """
            Get the Kâ‚€ :sup:`-n-1,s` coefficient value.
        
            The s value is given in the class constructor
        
            Parameters:
                mnm1 (int): (-n-1) coefficient
                chi (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.FieldHansenZonalLinear`): The value of Ï‡
        
            Returns:
                Kâ‚€ :sup:`-n-1,s`
        
        
        """
        ...

class HansenTesseralLinear:
    """
    public class HansenTesseralLinear extends Object
    
        Hansen coefficients K(t,n,s) for t!=0 and n < 0.
    
        Implements Collins 4-236 or Danielson 2.7.3-(9) for Hansen Coefficients and Collins 4-240 for derivatives. The
        recursions are transformed into composition of linear transformations to obtain the associated polynomials for
        coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, int: int, int2: int, int3: int, int4: int, int5: int): ...
    def computeInitValues(self, double: float, double2: float, double3: float) -> None:
        """
            Compute the values for the first four coefficients and their derivatives by means of series.
        
            Parameters:
                e2 (double): eÂ²
                chi (double): Χ
                chi2 (double): ΧÂ²
        
        
        """
        ...
    def getDerivative(self, int: int, double: float) -> float:
        """
            Compute the value of the derivative dK :sub:`j` :sup:`-n-1, s` / deÂ².
        
            Parameters:
                mnm1 (int): -n-1
                chi (double): Ï‡
        
            Returns:
                the derivative dK :sub:`j` :sup:`-n-1, s` / deÂ²
        
        
        """
        ...
    def getValue(self, int: int, double: float) -> float:
        """
            Compute the value of the Hansen coefficient K :sub:`j` :sup:`-n-1, s` .
        
            Parameters:
                mnm1 (int): -n-1
                chi (double): Ï‡
        
            Returns:
                the coefficient K :sub:`j` :sup:`-n-1, s`
        
        
        """
        ...

class HansenThirdBodyLinear:
    """
    public class HansenThirdBodyLinear extends Object
    
        Hansen coefficients K(t,n,s) for t=0 and n > 0.
    
        Implements Collins 4-254 or Danielson 2.7.3-(7) for Hansen Coefficients and Danielson 3.2-(3) for derivatives. The
        recursions are transformed into composition of linear transformations to obtain the associated polynomials for
        coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, int: int, int2: int): ...
    def computeInitValues(self, double: float, double2: float, double3: float) -> None:
        """
            Compute the initial values (see Collins, 4-255, 4-256 and 4.259)
        
            Kâ‚€ :sup:`s, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+1)! )
        
            Kâ‚€ :sup:`s+1, s` = (-1) :sup:`s` * ( (2*s+1)!! / (s+2)! ) * (2*s+3 - Ï‡ :sup:`-2` )
        
            dKâ‚€ :sup:`s+1, s` / dÏ‡ = = (-1) :sup:`s` * 2 * ( (2*s+1)!! / (s+2)! ) * Ï‡ :sup:`-3`
        
            Parameters:
                chitm1 (double): sqrt(1 - eÂ²)
                chitm2 (double): sqrt(1 - eÂ²)Â²
                chitm3 (double): sqrt(1 - eÂ²)Â³
        
        
        """
        ...
    def getDerivative(self, int: int, double: float) -> float:
        """
            Compute the value of the Hansen coefficient dKâ‚€ :sup:`n, s` / dΧ.
        
            Parameters:
                n (int): n value
                chitm1 (double): Ï‡ :sup:`-1`
        
            Returns:
                the coefficient dKâ‚€ :sup:`n, s` / dΧ
        
        
        """
        ...
    def getValue(self, int: int, double: float) -> float:
        """
            Compute the value of the Hansen coefficient Kâ‚€ :sup:`n, s` .
        
            Parameters:
                n (int): n value
                chitm1 (double): Ï‡ :sup:`-1`
        
            Returns:
                the coefficient Kâ‚€ :sup:`n, s`
        
        
        """
        ...

class HansenUtilities:
    """
    public class HansenUtilities extends Object
    
        Utilities class.
    """
    ONE: typing.ClassVar[org.hipparchus.analysis.polynomials.PolynomialFunction] = ...
    """
    public static final PolynomialFunction ONE
    
        1 represented as a polynomial.
    
    """
    ZERO: typing.ClassVar[org.hipparchus.analysis.polynomials.PolynomialFunction] = ...
    """
    public static final PolynomialFunction ZERO
    
        0 represented as a polynomial.
    
    """
    @staticmethod
    def buildIdentityMatrix2() -> 'PolynomialFunctionMatrix':
        """
            Build the identity matrix of order 2.
        
            .. code-block: java
            
            
                   / 1   0 \
              Iâ‚‚ = |       |
                   \ 0   1 /
             
        
            Returns:
                the identity matrix of order 2
        
        
        """
        ...
    @staticmethod
    def buildIdentityMatrix4() -> 'PolynomialFunctionMatrix':
        """
            Build the identity matrix of order 4.
        
            .. code-block: java
            
            
                   / 1  0  0  0 \
                   |            |
                   | 0  1  0  0 |
              Iâ‚„ = |            |
                   | 0  0  1  0 |
                   |            |
                   \ 0  0  0  1 /
             
        
            Returns:
                the identity matrix of order 4
        
        
        """
        ...
    @staticmethod
    def buildZeroMatrix2() -> 'PolynomialFunctionMatrix':
        """
            Build the empty matrix of order 2.
        
            .. code-block: java
            
            
                   / 0   0 \
              Eâ‚‚ = |       |
                   \ 0   0 /
             
        
            Returns:
                the identity matrix of order 2
        
        
        """
        ...
    @staticmethod
    def buildZeroMatrix4() -> 'PolynomialFunctionMatrix':
        """
            Build the empty matrix of order 4.
        
            .. code-block: java
            
            
                   / 0  0  0  0 \
                   |            |
                   | 0  0  0  0 |
              Eâ‚„ = |            |
                   | 0  0  0  0 |
                   |            |
                   \ 0  0  0  0 /
             
        
            Returns:
                the identity matrix of order 4
        
        
        """
        ...

class HansenZonalLinear:
    """
    public class HansenZonalLinear extends Object
    
        Hansen coefficients K(t,n,s) for t=0 and n < 0.
    
        Implements Collins 4-242 or echivalently, Danielson 2.7.3-(6) for Hansen Coefficients and Collins 4-245 or Danielson
        3.1-(7) for derivatives. The recursions are transformed into composition of linear transformations to obtain the
        associated polynomials for coefficients and their derivatives - see Petre's paper
    """
    def __init__(self, int: int, int2: int): ...
    def computeInitValues(self, double: float) -> None:
        """
            Compute the roots for the Hansen coefficients and their derivatives.
        
            Parameters:
                chi (double): 1 / sqrt(1 - eÂ²)
        
        
        """
        ...
    def getDerivative(self, int: int, double: float) -> float:
        """
            Get the dKâ‚€ :sup:`-n-1,s` / dΧ coefficient derivative.
        
            The s value is given in the class constructor.
        
            Parameters:
                mnm1 (int): (-n-1) coefficient
                chi (double): The value of Ï‡
        
            Returns:
                dKâ‚€ :sup:`-n-1,s` / dΧ
        
        
        """
        ...
    def getValue(self, int: int, double: float) -> float:
        """
            Get the Kâ‚€ :sup:`-n-1,s` coefficient value.
        
            The s value is given in the class constructor
        
            Parameters:
                mnm1 (int): (-n-1) coefficient
                chi (double): The value of Ï‡
        
            Returns:
                Kâ‚€ :sup:`-n-1,s`
        
        
        """
        ...

class PolynomialFunctionMatrix:
    """
    public class PolynomialFunctionMatrix extends Object
    
        A quadratic matrix of null.
    """
    def add(self, polynomialFunctionMatrix: 'PolynomialFunctionMatrix') -> 'PolynomialFunctionMatrix':
        """
            Add the argument matrix with the current matrix.
        
            Parameters:
                matrix (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.PolynomialFunctionMatrix`): the argument matrix
        
            Returns:
                the result of the addition
        
        
        """
        ...
    def getElem(self, int: int, int2: int) -> org.hipparchus.analysis.polynomials.PolynomialFunction:
        """
            Get the value of an element.
        
            Parameters:
                line (int): the line
                column (int): the column
        
            Returns:
                the value
        
        
        """
        ...
    def getMatrixLine(self, int: int) -> typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]:
        """
            Get a line of the matrix.
        
            Parameters:
                line (int): the line number
        
            Returns:
                the line of the matrix as a vector
        
        
        """
        ...
    def multiply(self, polynomialFunctionMatrix: 'PolynomialFunctionMatrix') -> 'PolynomialFunctionMatrix':
        """
            Multiply the argument matrix with the current matrix.
        
            Parameters:
                matrix (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.hansen.PolynomialFunctionMatrix`): the argument matrix
        
            Returns:
                the result of the multiplication
        
        
        """
        ...
    def setElem(self, int: int, int2: int, polynomialFunction: org.hipparchus.analysis.polynomials.PolynomialFunction) -> None:
        """
            Set an element of the matrix.
        
            Parameters:
                line (int): the line
                column (int): the column
                value (PolynomialFunction): the value
        
        
        """
        ...
    def setMatrix(self, polynomialFunctionArray: typing.List[typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]]) -> None:
        """
            Set values for all elements.
        
            Parameters:
                polynomials (PolynomialFunction[][]): the values that will be used for the matrix
        
        
        """
        ...
    def setMatrixLine(self, int: int, polynomialFunctionArray: typing.List[org.hipparchus.analysis.polynomials.PolynomialFunction]) -> None:
        """
            Set the value of a line of the matrix.
        
            Parameters:
                line (int): the line number
                polynomials (PolynomialFunction[]): the values to set
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst.utilities.hansen")``.

    FieldHansenTesseralLinear: typing.Type[FieldHansenTesseralLinear]
    FieldHansenThirdBodyLinear: typing.Type[FieldHansenThirdBodyLinear]
    FieldHansenZonalLinear: typing.Type[FieldHansenZonalLinear]
    HansenTesseralLinear: typing.Type[HansenTesseralLinear]
    HansenThirdBodyLinear: typing.Type[HansenThirdBodyLinear]
    HansenUtilities: typing.Type[HansenUtilities]
    HansenZonalLinear: typing.Type[HansenZonalLinear]
    PolynomialFunctionMatrix: typing.Type[PolynomialFunctionMatrix]
