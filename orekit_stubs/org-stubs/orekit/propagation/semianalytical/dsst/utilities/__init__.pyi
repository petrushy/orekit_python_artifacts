import java.lang
import java.util
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.semianalytical.dsst.utilities.class-use
import org.orekit.propagation.semianalytical.dsst.utilities.hansen
import org.orekit.time
import typing



class AuxiliaryElements:
    """
    public class AuxiliaryElements extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container class for common parameters used by all DSST forces.
    
        Most of them are defined in Danielson paper at § 2.1.
    """
    def __init__(self, orbit: org.orekit.orbits.Orbit, int: int): ...
    def getAlpha(self) -> float:
        """
            Get direction cosine α for central body.
        
            Returns:
                α
        
        
        """
        ...
    def getB(self) -> float:
        """
            Get B = sqrt(1 - e²).
        
            Returns:
                B
        
        
        """
        ...
    def getBeta(self) -> float:
        """
            Get direction cosine β for central body.
        
            Returns:
                β
        
        
        """
        ...
    def getC(self) -> float:
        """
            Get C = 1 + p² + q².
        
            Returns:
                C
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.AbsoluteDate:
        """
            Get the date of the orbit.
        
            Returns:
                the date
        
        
        """
        ...
    def getEcc(self) -> float:
        """
            Get the eccentricity.
        
            Returns:
                ecc
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the definition frame of the orbit.
        
            Returns:
                the definition frame
        
        
        """
        ...
    def getGamma(self) -> float:
        """
            Get direction cosine γ for central body.
        
            Returns:
                γ
        
        
        """
        ...
    def getH(self) -> float:
        """
            Get the y component of eccentricity vector.
        
            This element called h in DSST corresponds to ey for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                h
        
        
        """
        ...
    def getK(self) -> float:
        """
            Get the x component of eccentricity vector.
        
            This element called k in DSST corresponds to ex for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                k
        
        
        """
        ...
    def getKeplerianPeriod(self) -> float:
        """
            Get the Keplerian period.
        
            Returns:
                period
        
        
        """
        ...
    def getLM(self) -> float:
        """
            Get the mean longitude.
        
            Returns:
                lm
        
        
        """
        ...
    def getLf(self) -> float:
        """
            Get the eccentric longitude.
        
            Returns:
                lf
        
        
        """
        ...
    def getLv(self) -> float:
        """
            Get the true longitude.
        
            Returns:
                lv
        
        
        """
        ...
    def getMeanMotion(self) -> float:
        """
            Get the Keplerian mean motion.
        
            Returns:
                n
        
        
        """
        ...
    def getP(self) -> float:
        """
            Get the y component of inclination vector.
        
            This element called p in DSST corresponds to hy for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                p
        
        
        """
        ...
    def getQ(self) -> float:
        """
            Get the x component of inclination vector.
        
            This element called q in DSST corresponds to hx for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                q
        
        
        """
        ...
    def getRetrogradeFactor(self) -> int:
        """
            Get the retrograde factor.
        
            Returns:
                the retrograde factor I
        
        
        """
        ...
    def getSma(self) -> float:
        """
            Get the semi-major axis.
        
            Returns:
                the semi-major axis a
        
        
        """
        ...
    def getVectorF(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get equinoctial frame vector f.
        
            Returns:
                f vector
        
        
        """
        ...
    def getVectorG(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get equinoctial frame vector g.
        
            Returns:
                g vector
        
        
        """
        ...
    def getVectorW(self) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Get equinoctial frame vector w.
        
            Returns:
                w vector
        
        
        """
        ...

class CjSjCoefficient:
    """
    public class CjSjCoefficient extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the S :sub:`j` (k, h) and the C :sub:`j` (k, h) series and their partial derivatives with respect to k and h.
    
        Those series are given in Danielson paper by expression 2.5.3-(5):
    
        C :sub:`j` (k, h) + i S :sub:`j` (k, h) = (k+ih) :sup:`j`
    
        The C :sub:`j` (k, h) and the S :sub:`j` (k, h) elements are store as an
        :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.util.ArrayList?is`
        of
        :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.complex.Complex?is`
        number, the C :sub:`j` (k, h) being represented by the real and the S :sub:`j` (k, h) by the imaginary part.
    """
    def __init__(self, double: float, double2: float): ...
    def getCj(self, int: int) -> float:
        """
            Get the C :sub:`j` coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                C :sub:`j`
        
        
        """
        ...
    def getDcjDh(self, int: int) -> float:
        """
            Get the dC :sub:`j` / dh coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dC :sub:`i` / d :sub:`k`
        
        
        """
        ...
    def getDcjDk(self, int: int) -> float:
        """
            Get the dC :sub:`j` / dk coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dC :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getDsjDh(self, int: int) -> float:
        """
            Get the dS :sub:`j` / dh coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dS :sub:`j` / d :sub:`h`
        
        
        """
        ...
    def getDsjDk(self, int: int) -> float:
        """
            Get the dS :sub:`j` / dk coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dS :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getSj(self, int: int) -> float:
        """
            Get the S :sub:`j` coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                S :sub:`j`
        
        
        """
        ...

class CoefficientsFactory:
    """
    public class CoefficientsFactory extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        This class is designed to provide coefficient from the DSST theory.
    """
    _computeGsHs_1__T = typing.TypeVar('_computeGsHs_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeGsHs(double: float, double2: float, double3: float, double4: float, int: int) -> typing.List[typing.List[float]]:
        """
            Compute recursively G :sub:`s` and H :sub:`s` polynomials from equation 3.1-(5).
        
            Parameters:
                k (double): x-component of the eccentricity vector
                h (double): y-component of the eccentricity vector
                alpha (double): 1st direction cosine
                beta (double): 2nd direction cosine
                order (int): development order
        
            Returns:
                Array of G :sub:`s` and H :sub:`s` polynomials for s from 0 to order.
        
        
                The 1st column contains the G :sub:`s` values. The 2nd column contains the H :sub:`s` values.
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeGsHs(t: _computeGsHs_1__T, t2: _computeGsHs_1__T, t3: _computeGsHs_1__T, t4: _computeGsHs_1__T, int: int, field: org.hipparchus.Field[_computeGsHs_1__T]) -> typing.List[typing.List[_computeGsHs_1__T]]:
        """
            Compute recursively G :sub:`s` and H :sub:`s` polynomials from equation 3.1-(5).
        
            Parameters:
                k (T): x-component of the eccentricity vector
                h (T): y-component of the eccentricity vector
                alpha (T): 1st direction cosine
                beta (T): 2nd direction cosine
                order (int): development order
                field (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.Field?is`<T> field): field of elements
        
            Returns:
                Array of G :sub:`s` and H :sub:`s` polynomials for s from 0 to order.
        
        
                The 1st column contains the G :sub:`s` values. The 2nd column contains the H :sub:`s` values.
        
        
        """
        ...
    _computeQns_1__T = typing.TypeVar('_computeQns_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeQns(double: float, int: int, int2: int) -> typing.List[typing.List[float]]:
        """
            Compute the Q :sub:`n,s` coefficients evaluated at γ from the recurrence formula 2.8.3-(2).
        
            Q :sub:`n,s` coefficients are computed for n = 0 to nMax and s = 0 to sMax + 1 in order to also get the derivative dQ
            :sub:`n,s` /dγ = Q(n, s + 1)
        
            Parameters:
                gamma (double): γ angle
                nMax (int): n max value
                sMax (int): s max value
        
            Returns:
                Q :sub:`n,s` coefficients array
        
        """
        ...
    @typing.overload
    @staticmethod
    def computeQns(t: _computeQns_1__T, int: int, int2: int) -> typing.List[typing.List[_computeQns_1__T]]:
        """
            Compute the Q :sub:`n,s` coefficients evaluated at γ from the recurrence formula 2.8.3-(2).
        
            Q :sub:`n,s` coefficients are computed for n = 0 to nMax and s = 0 to sMax + 1 in order to also get the derivative dQ
            :sub:`n,s` /dγ = Q(n, s + 1)
        
            Parameters:
                gamma (T): γ angle
                nMax (int): n max value
                sMax (int): s max value
        
            Returns:
                Q :sub:`n,s` coefficients array
        
        
        """
        ...
    @staticmethod
    def computeVns(int: int) -> java.util.TreeMap['CoefficientsFactory.NSKey', float]: ...
    @staticmethod
    def getVmns(int: int, int2: int, int3: int) -> float:
        """
            Get the V :sub:`n,s` :sup:`m` coefficient from V :sub:`n,s` .
        
        
            See § 2.8.2 in Danielson paper.
        
            Parameters:
                m (int): m
                n (int): n
                s (int): s
        
            Returns:
                The V :sub:`n, s` :sup:`m` coefficient
        
        
        """
        ...
    class NSKey(java.lang.Comparable['CoefficientsFactory.NSKey']):
        def __init__(self, int: int, int2: int): ...
        def compareTo(self, nSKey: 'CoefficientsFactory.NSKey') -> int: ...
        def equals(self, object: typing.Any) -> bool: ...
        def getN(self) -> int: ...
        def getS(self) -> int: ...
        def hashCode(self) -> int: ...

_FieldAuxiliaryElements__T = typing.TypeVar('_FieldAuxiliaryElements__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldAuxiliaryElements(typing.Generic[_FieldAuxiliaryElements__T]):
    """
    public class FieldAuxiliaryElements<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Container class for common parameters used by all DSST forces.
    
        Most of them are defined in Danielson paper at § 2.1.
    """
    def __init__(self, fieldOrbit: org.orekit.orbits.FieldOrbit[_FieldAuxiliaryElements__T], int: int): ...
    def getAlpha(self) -> _FieldAuxiliaryElements__T:
        """
            Get direction cosine α for central body.
        
            Returns:
                α
        
        
        """
        ...
    def getB(self) -> _FieldAuxiliaryElements__T:
        """
            Get B = sqrt(1 - e²).
        
            Returns:
                B
        
        
        """
        ...
    def getBeta(self) -> _FieldAuxiliaryElements__T:
        """
            Get direction cosine β for central body.
        
            Returns:
                β
        
        
        """
        ...
    def getC(self) -> _FieldAuxiliaryElements__T:
        """
            Get C = 1 + p² + q².
        
            Returns:
                C
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldAuxiliaryElements__T]: ...
    def getEcc(self) -> _FieldAuxiliaryElements__T:
        """
            Get the eccentricity.
        
            Returns:
                ecc
        
        
        """
        ...
    def getFrame(self) -> org.orekit.frames.Frame:
        """
            Get the definition frame of the orbit.
        
            Returns:
                the definition frame
        
        
        """
        ...
    def getGamma(self) -> _FieldAuxiliaryElements__T:
        """
            Get direction cosine γ for central body.
        
            Returns:
                γ
        
        
        """
        ...
    def getH(self) -> _FieldAuxiliaryElements__T:
        """
            Get the y component of eccentricity vector.
        
            This element called h in DSST corresponds to ey for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                h
        
        
        """
        ...
    def getK(self) -> _FieldAuxiliaryElements__T:
        """
            Get the x component of eccentricity vector.
        
            This element called k in DSST corresponds to ex for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                k
        
        
        """
        ...
    def getKeplerianPeriod(self) -> _FieldAuxiliaryElements__T:
        """
            Get the Keplerian period.
        
            Returns:
                period
        
        
        """
        ...
    def getLM(self) -> _FieldAuxiliaryElements__T:
        """
            Get the mean longitude.
        
            Returns:
                lm
        
        
        """
        ...
    def getLe(self) -> _FieldAuxiliaryElements__T:
        """
            Get the eccentric longitude.
        
            Returns:
                le
        
        
        """
        ...
    def getLv(self) -> _FieldAuxiliaryElements__T:
        """
            Get the true longitude.
        
            Returns:
                lv
        
        
        """
        ...
    def getMeanMotion(self) -> _FieldAuxiliaryElements__T:
        """
            Get the Keplerian mean motion.
        
            Returns:
                n
        
        
        """
        ...
    def getP(self) -> _FieldAuxiliaryElements__T:
        """
            Get the y component of inclination vector.
        
            This element called p in DSST corresponds to hy for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                p
        
        
        """
        ...
    def getQ(self) -> _FieldAuxiliaryElements__T:
        """
            Get the x component of inclination vector.
        
            This element called q in DSST corresponds to hx for the :class:`~org.orekit.orbits.EquinoctialOrbit`
        
            Returns:
                q
        
        
        """
        ...
    def getRetrogradeFactor(self) -> int:
        """
            Get the retrograde factor.
        
            Returns:
                the retrograde factor I
        
        
        """
        ...
    def getSma(self) -> _FieldAuxiliaryElements__T:
        """
            Get the semi-major axis.
        
            Returns:
                the semi-major axis a
        
        
        """
        ...
    def getVectorF(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAuxiliaryElements__T]: ...
    def getVectorG(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAuxiliaryElements__T]: ...
    def getVectorW(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAuxiliaryElements__T]: ...

_FieldCjSjCoefficient__T = typing.TypeVar('_FieldCjSjCoefficient__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCjSjCoefficient(typing.Generic[_FieldCjSjCoefficient__T]):
    """
    public class FieldCjSjCoefficient<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the S :sub:`j` (k, h) and the C :sub:`j` (k, h) series and their partial derivatives with respect to k and h.
    
        Those series are given in Danielson paper by expression 2.5.3-(5):
    
        C :sub:`j` (k, h) + i S :sub:`j` (k, h) = (k+ih) :sup:`j`
    
        The C :sub:`j` (k, h) and the S :sub:`j` (k, h) elements are store as an
        :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.util.ArrayList?is`
        of
        :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.complex.Complex?is`
        number, the C :sub:`j` (k, h) being represented by the real and the S :sub:`j` (k, h) by the imaginary part.
    """
    def __init__(self, t: _FieldCjSjCoefficient__T, t2: _FieldCjSjCoefficient__T, field: org.hipparchus.Field[_FieldCjSjCoefficient__T]): ...
    def getCj(self, int: int) -> _FieldCjSjCoefficient__T:
        """
            Get the C :sub:`j` coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                C :sub:`j`
        
        
        """
        ...
    def getDcjDh(self, int: int) -> _FieldCjSjCoefficient__T:
        """
            Get the dC :sub:`j` / dh coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dC :sub:`i` / d :sub:`k`
        
        
        """
        ...
    def getDcjDk(self, int: int) -> _FieldCjSjCoefficient__T:
        """
            Get the dC :sub:`j` / dk coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dC :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getDsjDh(self, int: int) -> _FieldCjSjCoefficient__T:
        """
            Get the dS :sub:`j` / dh coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dS :sub:`j` / d :sub:`h`
        
        
        """
        ...
    def getDsjDk(self, int: int) -> _FieldCjSjCoefficient__T:
        """
            Get the dS :sub:`j` / dk coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                dS :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getSj(self, int: int) -> _FieldCjSjCoefficient__T:
        """
            Get the S :sub:`j` coefficient.
        
            Parameters:
                j (int): order
        
            Returns:
                S :sub:`j`
        
        
        """
        ...

_FieldGHIJjsPolynomials__T = typing.TypeVar('_FieldGHIJjsPolynomials__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGHIJjsPolynomials(typing.Generic[_FieldGHIJjsPolynomials__T]):
    """
    public class FieldGHIJjsPolynomials<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the G :sub:`js` , H :sub:`js` , I :sub:`js` and J :sub:`js` polynomials in the equinoctial elements h, k and the
        direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
        The expressions used are equations 4.1-(10) from the Danielson paper.
    """
    def __init__(self, t: _FieldGHIJjsPolynomials__T, t2: _FieldGHIJjsPolynomials__T, t3: _FieldGHIJjsPolynomials__T, t4: _FieldGHIJjsPolynomials__T): ...
    def getGjs(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the G :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the G :sub:`js`
        
        
        """
        ...
    def getHjs(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the H :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js`
        
        
        """
        ...
    def getIjs(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the I :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js`
        
        
        """
        ...
    def getJjs(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the J :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js`
        
        
        """
        ...
    def getdGjsdAlpha(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dG :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dα
        
        
        """
        ...
    def getdGjsdBeta(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dG :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dβ
        
        
        """
        ...
    def getdGjsdh(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dG :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dh
        
        
        """
        ...
    def getdGjsdk(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dG :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dk
        
        
        """
        ...
    def getdHjsdAlpha(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dH :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dα
        
        
        """
        ...
    def getdHjsdBeta(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dH :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dβ
        
        
        """
        ...
    def getdHjsdh(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dH :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dh
        
        
        """
        ...
    def getdHjsdk(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dH :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dk
        
        
        """
        ...
    def getdIjsdAlpha(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dI :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dα
        
        
        """
        ...
    def getdIjsdBeta(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dI :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dβ
        
        
        """
        ...
    def getdIjsdh(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dI :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dh
        
        
        """
        ...
    def getdIjsdk(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dI :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dk
        
        
        """
        ...
    def getdJjsdAlpha(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dJ :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dα
        
        
        """
        ...
    def getdJjsdBeta(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dJ :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dβ
        
        
        """
        ...
    def getdJjsdh(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dJ :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dh
        
        
        """
        ...
    def getdJjsdk(self, int: int, int2: int) -> _FieldGHIJjsPolynomials__T:
        """
            Get the dJ :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dk
        
        
        """
        ...

_FieldGHmsjPolynomials__T = typing.TypeVar('_FieldGHmsjPolynomials__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGHmsjPolynomials(typing.Generic[_FieldGHmsjPolynomials__T]):
    """
    public class FieldGHmsjPolynomials<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the G :sub:`ms` :sup:`j` and the H :sub:`ms` :sup:`j` polynomials in the equinoctial elements h, k and the
        direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
        The expressions used are equations 2.7.5-(1)(2) from the Danielson paper.
    """
    def __init__(self, t: _FieldGHmsjPolynomials__T, t2: _FieldGHmsjPolynomials__T, t3: _FieldGHmsjPolynomials__T, t4: _FieldGHmsjPolynomials__T, int: int, field: org.hipparchus.Field[_FieldGHmsjPolynomials__T]): ...
    def getGmsj(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the G :sub:`ms` :sup:`j` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                the G :sub:`ms` :sup:`j`
        
        
        """
        ...
    def getHmsj(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the H :sub:`ms` :sup:`j` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                the H :sub:`ms` :sup:`j`
        
        
        """
        ...
    def getdGmsdAlpha(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdGmsdBeta(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdGmsdh(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdGmsdk(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...
    def getdHmsdAlpha(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdHmsdBeta(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdHmsdh(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdHmsdk(self, int: int, int2: int, int3: int) -> _FieldGHmsjPolynomials__T:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...

_FieldGammaMnsFunction__T = typing.TypeVar('_FieldGammaMnsFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGammaMnsFunction(typing.Generic[_FieldGammaMnsFunction__T]):
    """
    public class FieldGammaMnsFunction<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the Γ :sup:`m` :sub:`n,s` (γ) function from equation 2.7.1-(13).
    """
    def __init__(self, int: int, t: _FieldGammaMnsFunction__T, int2: int, field: org.hipparchus.Field[_FieldGammaMnsFunction__T]): ...
    def getDerivative(self, int: int, int2: int, int3: int) -> _FieldGammaMnsFunction__T:
        """
            Get Γ function derivative.
        
            Parameters:
                m (int): m
                n (int): n
                s (int): s
        
            Returns:
                dΓ :sup:`m` :sub:`n,s` (γ)/dγ
        
        
        """
        ...
    def getValue(self, int: int, int2: int, int3: int) -> _FieldGammaMnsFunction__T:
        """
            Get Γ function value.
        
            Parameters:
                m (int): m
                n (int): n
                s (int): s
        
            Returns:
                Γ :sup:`m` :sub:`n, s` (γ)
        
        
        """
        ...

_FieldInterpolationGrid__T = typing.TypeVar('_FieldInterpolationGrid__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldInterpolationGrid(typing.Generic[_FieldInterpolationGrid__T]):
    """
    public interface FieldInterpolationGrid<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>>
    
        Interface for interpolation grids.
    
        An interpolation grid provides a grid of time points that can be used for interpolation processes.
    
        In the context of DSST propagation, an interpolation grid is used for the computation through interpolation of short
        periodics coefficients
    """
    def getGridPoints(self, t: _FieldInterpolationGrid__T, t2: _FieldInterpolationGrid__T) -> typing.List[_FieldInterpolationGrid__T]:
        """
            Get grid points that are within the current step.
        
            The step is defined by its start and its end time.
        
            Parameters:
                stepStart (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid`): start of the step
                stepEnd (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid`): end of the step
        
            Returns:
                time points between start and end
        
        
        """
        ...

_FieldLnsCoefficients__T = typing.TypeVar('_FieldLnsCoefficients__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLnsCoefficients(typing.Generic[_FieldLnsCoefficients__T]):
    """
    public class FieldLnsCoefficients<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the L :sub:`n` :sup:`s` (γ).
    
        The fomula used is:
    
    
        L :sub:`n` :sup:`s` (γ) = ( R / a ) :sup:`n` V :sub:`ns` Q :sup:`ns` (γ)
    """
    def __init__(self, int: int, int2: int, tArray: typing.List[typing.List[_FieldLnsCoefficients__T]], treeMap: java.util.TreeMap[CoefficientsFactory.NSKey, float], t3: _FieldLnsCoefficients__T, field: org.hipparchus.Field[_FieldLnsCoefficients__T]): ...
    def getLns(self, int: int, int2: int) -> _FieldLnsCoefficients__T:
        """
            Get the value of L :sub:`n` :sup:`s` (γ).
        
            Parameters:
                n (int): n index
                s (int): s index
        
            Returns:
                L :sub:`n` :sup:`s` (γ)
        
        
        """
        ...
    def getdLnsdGamma(self, int: int, int2: int) -> _FieldLnsCoefficients__T:
        """
            Get the value of dL :sub:`n` :sup:`s` / dγ (γ).
        
            Parameters:
                n (int): n index
                s (int): s index
        
            Returns:
                L :sub:`n` :sup:`s` (γ)
        
        
        """
        ...

_FieldShortPeriodicsInterpolatedCoefficient__T = typing.TypeVar('_FieldShortPeriodicsInterpolatedCoefficient__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldShortPeriodicsInterpolatedCoefficient(typing.Generic[_FieldShortPeriodicsInterpolatedCoefficient__T]):
    """
    public class FieldShortPeriodicsInterpolatedCoefficient<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Interpolated short periodics coefficients.
    
        Representation of a coefficient that need to be interpolated over time.
    
        The short periodics coefficients can be interpolated for faster computation. This class stores computed values of the
        coefficients through the method
        :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldShortPeriodicsInterpolatedCoefficient.addGridPoint`
        and gives an interpolated result through the method
        :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldShortPeriodicsInterpolatedCoefficient.value`.
    """
    def __init__(self, int: int): ...
    def addGridPoint(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldShortPeriodicsInterpolatedCoefficient__T], tArray: typing.List[_FieldShortPeriodicsInterpolatedCoefficient__T]) -> None: ...
    def clearHistory(self) -> None:
        """
            Clear the recorded values from the interpolation grid.
        
        """
        ...
    def value(self, fieldAbsoluteDate: org.orekit.time.FieldAbsoluteDate[_FieldShortPeriodicsInterpolatedCoefficient__T]) -> typing.List[_FieldShortPeriodicsInterpolatedCoefficient__T]: ...

class GHIJjsPolynomials:
    """
    public class GHIJjsPolynomials extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the G :sub:`js` , H :sub:`js` , I :sub:`js` and J :sub:`js` polynomials in the equinoctial elements h, k and the
        direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
        The expressions used are equations 4.1-(10) from the Danielson paper.
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float): ...
    def getGjs(self, int: int, int2: int) -> float:
        """
            Get the G :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the G :sub:`js`
        
        
        """
        ...
    def getHjs(self, int: int, int2: int) -> float:
        """
            Get the H :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js`
        
        
        """
        ...
    def getIjs(self, int: int, int2: int) -> float:
        """
            Get the I :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js`
        
        
        """
        ...
    def getJjs(self, int: int, int2: int) -> float:
        """
            Get the J :sub:`js` coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js`
        
        
        """
        ...
    def getdGjsdAlpha(self, int: int, int2: int) -> float:
        """
            Get the dG :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dα
        
        
        """
        ...
    def getdGjsdBeta(self, int: int, int2: int) -> float:
        """
            Get the dG :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dβ
        
        
        """
        ...
    def getdGjsdh(self, int: int, int2: int) -> float:
        """
            Get the dG :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dh
        
        
        """
        ...
    def getdGjsdk(self, int: int, int2: int) -> float:
        """
            Get the dG :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the dG :sub:`js` / dk
        
        
        """
        ...
    def getdHjsdAlpha(self, int: int, int2: int) -> float:
        """
            Get the dH :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dα
        
        
        """
        ...
    def getdHjsdBeta(self, int: int, int2: int) -> float:
        """
            Get the dH :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dβ
        
        
        """
        ...
    def getdHjsdh(self, int: int, int2: int) -> float:
        """
            Get the dH :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dh
        
        
        """
        ...
    def getdHjsdk(self, int: int, int2: int) -> float:
        """
            Get the dH :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the H :sub:`js` / dk
        
        
        """
        ...
    def getdIjsdAlpha(self, int: int, int2: int) -> float:
        """
            Get the dI :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dα
        
        
        """
        ...
    def getdIjsdBeta(self, int: int, int2: int) -> float:
        """
            Get the dI :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dβ
        
        
        """
        ...
    def getdIjsdh(self, int: int, int2: int) -> float:
        """
            Get the dI :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dh
        
        
        """
        ...
    def getdIjsdk(self, int: int, int2: int) -> float:
        """
            Get the dI :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the I :sub:`js` / dk
        
        
        """
        ...
    def getdJjsdAlpha(self, int: int, int2: int) -> float:
        """
            Get the dJ :sub:`js` / dα coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dα
        
        
        """
        ...
    def getdJjsdBeta(self, int: int, int2: int) -> float:
        """
            Get the dJ :sub:`js` / dβ coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dβ
        
        
        """
        ...
    def getdJjsdh(self, int: int, int2: int) -> float:
        """
            Get the dJ :sub:`js` / dh coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dh
        
        
        """
        ...
    def getdJjsdk(self, int: int, int2: int) -> float:
        """
            Get the dJ :sub:`js` / dk coefficient.
        
            Parameters:
                j (int): j subscript
                s (int): s subscript
        
            Returns:
                the J :sub:`js` / dk
        
        
        """
        ...

class GHmsjPolynomials:
    """
    public class GHmsjPolynomials extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the G :sub:`ms` :sup:`j` and the H :sub:`ms` :sup:`j` polynomials in the equinoctial elements h, k and the
        direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
        The expressions used are equations 2.7.5-(1)(2) from the Danielson paper.
    """
    def __init__(self, double: float, double2: float, double3: float, double4: float, int: int): ...
    def getGmsj(self, int: int, int2: int, int3: int) -> float:
        """
            Get the G :sub:`ms` :sup:`j` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                the G :sub:`ms` :sup:`j`
        
        
        """
        ...
    def getHmsj(self, int: int, int2: int, int3: int) -> float:
        """
            Get the H :sub:`ms` :sup:`j` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                the H :sub:`ms` :sup:`j`
        
        
        """
        ...
    def getdGmsdAlpha(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdGmsdBeta(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdGmsdh(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdGmsdk(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dG :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dG :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...
    def getdHmsdAlpha(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdHmsdBeta(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdHmsdh(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdHmsdk(self, int: int, int2: int, int3: int) -> float:
        """
            Get the dH :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
            Parameters:
                m (int): m subscript
                s (int): s subscript
                j (int): order
        
            Returns:
                dH :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...

class GammaMnsFunction:
    """
    public class GammaMnsFunction extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the Γ :sup:`m` :sub:`n,s` (γ) function from equation 2.7.1-(13).
    """
    def __init__(self, int: int, double: float, int2: int): ...
    def getDerivative(self, int: int, int2: int, int3: int) -> float:
        """
            Get Γ function derivative.
        
            Parameters:
                m (int): m
                n (int): n
                s (int): s
        
            Returns:
                dΓ :sup:`m` :sub:`n,s` (γ)/dγ
        
        
        """
        ...
    def getValue(self, int: int, int2: int, int3: int) -> float:
        """
            Get Γ function value.
        
            Parameters:
                m (int): m
                n (int): n
                s (int): s
        
            Returns:
                Γ :sup:`m` :sub:`n, s` (γ)
        
        
        """
        ...

class InterpolationGrid:
    """
    public interface InterpolationGrid
    
        Interface for interpolation grids.
    
        An interpolation grid provides a grid of time points that can be used for interpolation processes.
    
        In the context of DSST propagation, an interpolation grid is used for the computation through interpolation of short
        periodics coefficients
    """
    def getGridPoints(self, double: float, double2: float) -> typing.List[float]:
        """
            Get grid points that are within the current step.
        
            The step is defined by its start and its end time.
        
            Parameters:
                stepStart (double): start of the step
                stepEnd (double): end of the step
        
            Returns:
                time points between start and end
        
        
        """
        ...

class JacobiPolynomials:
    """
    public class JacobiPolynomials extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Provider of the Jacobi polynomials P :sub:`l` :sup:`v,w` .
    
        This class is used for :class:`~org.orekit.propagation.semianalytical.dsst.forces.DSSTTesseral` computation.
    
        Since:
            6.1
    """
    _getValue_0__T = typing.TypeVar('_getValue_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getValue(int: int, int2: int, int3: int, fieldGradient: org.hipparchus.analysis.differentiation.FieldGradient[_getValue_0__T]) -> org.hipparchus.analysis.differentiation.FieldGradient[_getValue_0__T]:
        """
            Returns the value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` evaluated at γ.
        
            This method is guaranteed to be thread-safe
        
            Parameters:
                l (int): degree of the polynomial
                v (int): v value
                w (int): w value
                gamma (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.differentiation.FieldGradient?is`<T> gamma): γ value
        
            Returns:
                value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` (γ)
        
            Since:
                10.2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getValue(int: int, int2: int, int3: int, gradient: org.hipparchus.analysis.differentiation.Gradient) -> org.hipparchus.analysis.differentiation.Gradient:
        """
            Returns the value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` evaluated at γ.
        
            This method is guaranteed to be thread-safe
        
            Parameters:
                l (int): degree of the polynomial
                v (int): v value
                w (int): w value
                gamma (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.differentiation.Gradient?is`): γ value
        
            Returns:
                value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` (γ)
        
            Since:
                10.2
        
        """
        ...

class LnsCoefficients:
    """
    public class LnsCoefficients extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Compute the L :sub:`n` :sup:`s` (γ).
    
        The fomula used is:
    
    
        L :sub:`n` :sup:`s` (γ) = ( R / a ) :sup:`n` V :sub:`ns` Q :sup:`ns` (γ)
    """
    def __init__(self, int: int, int2: int, doubleArray: typing.List[typing.List[float]], treeMap: java.util.TreeMap[CoefficientsFactory.NSKey, float], double2: float): ...
    def getLns(self, int: int, int2: int) -> float:
        """
            Get the value of L :sub:`n` :sup:`s` (γ).
        
            Parameters:
                n (int): n index
                s (int): s index
        
            Returns:
                L :sub:`n` :sup:`s` (γ)
        
        
        """
        ...
    def getdLnsdGamma(self, int: int, int2: int) -> float:
        """
            Get the value of dL :sub:`n` :sup:`s` / dγ (γ).
        
            Parameters:
                n (int): n index
                s (int): s index
        
            Returns:
                L :sub:`n` :sup:`s` (γ)
        
        
        """
        ...

class NewcombOperators:
    """
    public class NewcombOperators extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Implementation of the Modified Newcomb Operators.
    
        From equations 2.7.3 - (12)(13) of the Danielson paper, those operators are defined as:
    
        4(ρ + σ)Y :sub:`ρ,σ` :sup:`n,s` =
    
    
        2(2s - n)Y :sub:`ρ-1,σ` :sup:`n,s+1` + (s - n)Y :sub:`ρ-2,σ` :sup:`n,s+2`
    
    
        - 2(2s + n)Y :sub:`ρ,σ-1` :sup:`n,s-1` - (s+n)Y :sub:`ρ,σ-2` :sup:`n,s-2`
    
    
        + 2(2ρ + 2σ + 2 + 3n)Y :sub:`ρ-1,σ-1` :sup:`n,s`
    
        Initialization is given by : Y :sub:`0,0` :sup:`n,s` = 1
    
        Internally, the Modified Newcomb Operators are stored as an array of
        :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.analysis.polynomials.PolynomialFunction?is`
        :
    
        Y :sub:`ρ,σ` :sup:`n,s` = P :sub:`k0` + P :sub:`k1` n + ... + P :sub:`kj` n :sup:`j`
    
        where the P :sub:`kj` are given by
    
        P :sub:`kj` = ∑ :sub:`j=0;ρ` a :sub:`j` s :sup:`j`
    """
    @staticmethod
    def getValue(int: int, int2: int, int3: int, int4: int) -> float:
        """
            Get the Newcomb operator evaluated at n, s, ρ, σ.
        
            This method is guaranteed to be thread-safe
        
            Parameters:
                rho (int): ρ index
                sigma (int): σ index
                n (int): n index
                s (int): s index
        
            Returns:
                Y :sub:`ρ,σ` :sup:`n,s`
        
        
        """
        ...

class ShortPeriodicsInterpolatedCoefficient:
    """
    public class ShortPeriodicsInterpolatedCoefficient extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Interpolated short periodics coefficients.
    
        Representation of a coefficient that need to be interpolated over time.
    
        The short periodics coefficients can be interpolated for faster computation. This class stores computed values of the
        coefficients through the method
        :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.ShortPeriodicsInterpolatedCoefficient.addGridPoint` and
        gives an interpolated result through the method
        :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.ShortPeriodicsInterpolatedCoefficient.value`.
    """
    def __init__(self, int: int): ...
    def addGridPoint(self, absoluteDate: org.orekit.time.AbsoluteDate, doubleArray: typing.List[float]) -> None:
        """
            Add a point to the interpolation grid.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): abscissa of the point
                value (double[]): value of the element
        
        
        """
        ...
    def clearHistory(self) -> None:
        """
            Clear the recorded values from the interpolation grid.
        
        """
        ...
    def value(self, absoluteDate: org.orekit.time.AbsoluteDate) -> typing.List[float]:
        """
            Compute the value of the coefficient.
        
            Parameters:
                date (:class:`~org.orekit.time.AbsoluteDate`): date at which the coefficient should be computed
        
            Returns:
                value of the coefficient
        
        
        """
        ...

class UpperBounds:
    """
    public class UpperBounds extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
        Utility class to compute upper bounds for truncation algorithms.
    """
    _getDnl_1__T = typing.TypeVar('_getDnl_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getDnl(double: float, double2: float, int: int, int2: int) -> float:
        """
            Get the upper bound value D :sub:`n` :sup:`l` (Χ).
        
            Parameters:
                xx (double): value of Χ²
                xpl (double): value of Χ * (Χ² / 2) :sup:`l`
                n (int): index n (power of a/R)
                l (int): index l (power of eccentricity)
        
            Returns:
                the upper bound D :sub:`n` :sup:`l` (Χ)
        
        """
        ...
    @typing.overload
    @staticmethod
    def getDnl(t: _getDnl_1__T, t2: _getDnl_1__T, int: int, int2: int) -> _getDnl_1__T:
        """
            Get the upper bound value D :sub:`n` :sup:`l` (Χ).
        
            Parameters:
                xx (T): value of Χ²
                xpl (T): value of Χ * (Χ² / 2) :sup:`l`
                n (int): index n (power of a/R)
                l (int): index l (power of eccentricity)
        
            Returns:
                the upper bound D :sub:`n` :sup:`l` (Χ)
        
        
        """
        ...
    _getRnml_1__T = typing.TypeVar('_getRnml_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getRnml(double: float, int: int, int2: int, int3: int, int4: int, int5: int) -> float:
        """
            Get the upper bound value R :sup:`ε` :sub:`n,m,l` (γ).
        
            Parameters:
                gamma (double): value of γ
                n (int): index n
                l (int): index l
                m (int): index m
                eps (int): ε value (+1/-1)
                irf (int): retrograde factor I (+1/-1)
        
            Returns:
                the upper bound R :sup:`ε` :sub:`n,m,l` (γ)
        
        """
        ...
    @typing.overload
    @staticmethod
    def getRnml(t: _getRnml_1__T, int: int, int2: int, int3: int, int4: int, int5: int) -> _getRnml_1__T:
        """
            Get the upper bound value R :sup:`ε` :sub:`n,m,l` (γ).
        
            Parameters:
                gamma (T): value of γ
                n (int): index n
                l (int): index l
                m (int): index m
                eps (int): ε value (+1/-1)
                irf (int): retrograde factor I (+1/-1)
        
            Returns:
                the upper bound R :sup:`ε` :sub:`n,m,l` (γ)
        
        
        """
        ...

_FieldFixedNumberInterpolationGrid__T = typing.TypeVar('_FieldFixedNumberInterpolationGrid__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldFixedNumberInterpolationGrid(FieldInterpolationGrid[_FieldFixedNumberInterpolationGrid__T], typing.Generic[_FieldFixedNumberInterpolationGrid__T]):
    """
    public class FieldFixedNumberInterpolationGrid<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid`<T>
    
        Interpolation grid where a fixed number of points are evenly spaced between the start and the end of the integration
        step.
    
        The grid is adapted to the step considered, meaning that for short steps, the grid will be dense, while for long steps
        the points will be far away one from each other
    """
    def __init__(self, field: org.hipparchus.Field[_FieldFixedNumberInterpolationGrid__T], int: int): ...
    def getGridPoints(self, t: _FieldFixedNumberInterpolationGrid__T, t2: _FieldFixedNumberInterpolationGrid__T) -> typing.List[_FieldFixedNumberInterpolationGrid__T]:
        """
            Get grid points that are within the current step.
        
            The step is defined by its start and its end time.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid.getGridPoints` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid`
        
            Parameters:
                stepStart (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldFixedNumberInterpolationGrid`): start of the step
                stepEnd (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldFixedNumberInterpolationGrid`): end of the step
        
            Returns:
                time points between start and end
        
        
        """
        ...

_FieldMaxGapInterpolationGrid__T = typing.TypeVar('_FieldMaxGapInterpolationGrid__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldMaxGapInterpolationGrid(FieldInterpolationGrid[_FieldMaxGapInterpolationGrid__T], typing.Generic[_FieldMaxGapInterpolationGrid__T]):
    """
    public class FieldMaxGapInterpolationGrid<T extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.www.hipparchus.org.apidocs.org.hipparchus.CalculusFieldElement?is`<T>> extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid`<T>
    
        Interpolation grid where points obey a maximum time gap.
    
        The grid is adapted to the step considered, meaning that for short steps, the grid will have numerous points.
    
        Since:
            7.1
    """
    def __init__(self, field: org.hipparchus.Field[_FieldMaxGapInterpolationGrid__T], t: _FieldMaxGapInterpolationGrid__T): ...
    def getGridPoints(self, t: _FieldMaxGapInterpolationGrid__T, t2: _FieldMaxGapInterpolationGrid__T) -> typing.List[_FieldMaxGapInterpolationGrid__T]:
        """
            Get grid points that are within the current step.
        
            The step is defined by its start and its end time.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid.getGridPoints` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldInterpolationGrid`
        
            Parameters:
                stepStart (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldMaxGapInterpolationGrid`): start of the step
                stepEnd (:class:`~org.orekit.propagation.semianalytical.dsst.utilities.FieldMaxGapInterpolationGrid`): end of the step
        
            Returns:
                time points between start and end
        
        
        """
        ...

class FixedNumberInterpolationGrid(InterpolationGrid):
    """
    public class FixedNumberInterpolationGrid extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.utilities.InterpolationGrid`
    
        Interpolation grid where a fixed number of points are evenly spaced between the start and the end of the integration
        step.
    
        The grid is adapted to the step considered, meaning that for short steps, the grid will be dense, while for long steps
        the points will be far away one from each other
    """
    def __init__(self, int: int): ...
    def getGridPoints(self, double: float, double2: float) -> typing.List[float]:
        """
            Get grid points that are within the current step.
        
            The step is defined by its start and its end time.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.InterpolationGrid.getGridPoints` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.utilities.InterpolationGrid`
        
            Parameters:
                stepStart (double): start of the step
                stepEnd (double): end of the step
        
            Returns:
                time points between start and end
        
        
        """
        ...

class MaxGapInterpolationGrid(InterpolationGrid):
    """
    public class MaxGapInterpolationGrid extends :class:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is` implements :class:`~org.orekit.propagation.semianalytical.dsst.utilities.InterpolationGrid`
    
        Interpolation grid where points obey a maximum time gap.
    
        The grid is adapted to the step considered, meaning that for short steps, the grid will have numerous points.
    
        Since:
            7.1
    """
    def __init__(self, double: float): ...
    def getGridPoints(self, double: float, double2: float) -> typing.List[float]:
        """
            Get grid points that are within the current step.
        
            The step is defined by its start and its end time.
        
            Specified by:
                :meth:`~org.orekit.propagation.semianalytical.dsst.utilities.InterpolationGrid.getGridPoints` in
                interface :class:`~org.orekit.propagation.semianalytical.dsst.utilities.InterpolationGrid`
        
            Parameters:
                stepStart (double): start of the step
                stepEnd (double): end of the step
        
            Returns:
                time points between start and end
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.propagation.semianalytical.dsst.utilities")``.

    AuxiliaryElements: typing.Type[AuxiliaryElements]
    CjSjCoefficient: typing.Type[CjSjCoefficient]
    CoefficientsFactory: typing.Type[CoefficientsFactory]
    FieldAuxiliaryElements: typing.Type[FieldAuxiliaryElements]
    FieldCjSjCoefficient: typing.Type[FieldCjSjCoefficient]
    FieldFixedNumberInterpolationGrid: typing.Type[FieldFixedNumberInterpolationGrid]
    FieldGHIJjsPolynomials: typing.Type[FieldGHIJjsPolynomials]
    FieldGHmsjPolynomials: typing.Type[FieldGHmsjPolynomials]
    FieldGammaMnsFunction: typing.Type[FieldGammaMnsFunction]
    FieldInterpolationGrid: typing.Type[FieldInterpolationGrid]
    FieldLnsCoefficients: typing.Type[FieldLnsCoefficients]
    FieldMaxGapInterpolationGrid: typing.Type[FieldMaxGapInterpolationGrid]
    FieldShortPeriodicsInterpolatedCoefficient: typing.Type[FieldShortPeriodicsInterpolatedCoefficient]
    FixedNumberInterpolationGrid: typing.Type[FixedNumberInterpolationGrid]
    GHIJjsPolynomials: typing.Type[GHIJjsPolynomials]
    GHmsjPolynomials: typing.Type[GHmsjPolynomials]
    GammaMnsFunction: typing.Type[GammaMnsFunction]
    InterpolationGrid: typing.Type[InterpolationGrid]
    JacobiPolynomials: typing.Type[JacobiPolynomials]
    LnsCoefficients: typing.Type[LnsCoefficients]
    MaxGapInterpolationGrid: typing.Type[MaxGapInterpolationGrid]
    NewcombOperators: typing.Type[NewcombOperators]
    ShortPeriodicsInterpolatedCoefficient: typing.Type[ShortPeriodicsInterpolatedCoefficient]
    UpperBounds: typing.Type[UpperBounds]
    class-use: org.orekit.propagation.semianalytical.dsst.utilities.class-use.__module_protocol__
    hansen: org.orekit.propagation.semianalytical.dsst.utilities.hansen.__module_protocol__
