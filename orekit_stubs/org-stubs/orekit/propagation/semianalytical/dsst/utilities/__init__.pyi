
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.lang
import java.util
import jpype
import org.hipparchus
import org.hipparchus.analysis.differentiation
import org.hipparchus.geometry.euclidean.threed
import org.orekit.frames
import org.orekit.orbits
import org.orekit.propagation.semianalytical.dsst.utilities.hansen
import org.orekit.time
import typing



class AuxiliaryElements:
    """
    Container class for common parameters used by all DSST forces.
    
    Most of them are defined in Danielson paper at § 2.1.
    """
    def __init__(self, orbit: org.orekit.orbits.Orbit, retrogradeFactor: int):
        """
        Simple constructor.
        
        Parameters:
            orbit (Orbit): related mean orbit for auxiliary elements
            retrogradeFactor (int): retrograde factor I [Eq. 2.1.2-(2)]
        
        
        """
        ...
    def getB(self) -> float:
        """
        Get B = sqrt(1 - e²).
        
        Returns:
            B
        
        
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
    def getH(self) -> float:
        """
        Get the y component of eccentricity vector.
        
        This element called h in DSST corresponds to ey for the EquinoctialOrbit
        
        Returns:
            h
        
        
        """
        ...
    def getK(self) -> float:
        """
        Get the x component of eccentricity vector.
        
        This element called k in DSST corresponds to ex for the EquinoctialOrbit
        
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
    def getOrbit(self) -> org.orekit.orbits.Orbit:
        """
        Get the orbit.
        
        Returns:
            the orbit
        
        
        """
        ...
    def getP(self) -> float:
        """
        Get the y component of inclination vector.
        
        This element called p in DSST corresponds to hy for the EquinoctialOrbit
        
        Returns:
            p
        
        
        """
        ...
    def getQ(self) -> float:
        """
        Get the x component of inclination vector.
        
        This element called q in DSST corresponds to hx for the EquinoctialOrbit
        
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
    Compute the S :sub:`j` (k, h) and the C :sub:`j` (k, h) series and their partial derivatives with respect to k and h.
    
    Those series are given in Danielson paper by expression 2.5.3-(5):
    
    C :sub:`j` (k, h) + i S :sub:`j` (k, h) = (k+ih) :sup:`j`
    
    The C :sub:`j` (k, h) and the S :sub:`j` (k, h) elements are store as an ArrayList of Complex number, the C :sub:`j` (k, h) being represented by the real and the S :sub:`j` (k, h) by the imaginary part.
    """
    def __init__(self, k: float, h: float):
        """
        C :sub:`j` (k, h) and S :sub:`j` (k, h) constructor.
        
        Parameters:
            k (double): k value
            h (double): h value
        
        
        """
        ...
    def getCj(self, j: int) -> float:
        """
        Get the C :sub:`j` coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            C :sub:`j`
        
        
        """
        ...
    def getDcjDh(self, j: int) -> float:
        """
        Get the dC :sub:`j` / dh coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`i` / d :sub:`k`
        
        
        """
        ...
    def getDcjDk(self, j: int) -> float:
        """
        Get the dC :sub:`j` / dk coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getDsjDh(self, j: int) -> float:
        """
        Get the dS :sub:`j` / dh coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`j` / d :sub:`h`
        
        
        """
        ...
    def getDsjDk(self, j: int) -> float:
        """
        Get the dS :sub:`j` / dk coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getSj(self, j: int) -> float:
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
    This class is designed to provide coefficient from the DSST theory.
    """
    _computeGsHs_1__T = typing.TypeVar('_computeGsHs_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeGsHs(k: float, h: float, alpha: float, beta: float, order: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
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
    def computeGsHs(k: _computeGsHs_1__T, h: _computeGsHs_1__T, alpha: _computeGsHs_1__T, beta: _computeGsHs_1__T, order: int, field: org.hipparchus.Field[_computeGsHs_1__T]) -> typing.MutableSequence[typing.MutableSequence[_computeGsHs_1__T]]:
        """
        Compute recursively G :sub:`s` and H :sub:`s` polynomials from equation 3.1-(5).
        
        Parameters:
            k (T): x-component of the eccentricity vector
            h (T): y-component of the eccentricity vector
            alpha (T): 1st direction cosine
            beta (T): 2nd direction cosine
            order (int): development order
            field (Field<T> field): field of elements
        
        Returns:
            Array of G :sub:`s` and H :sub:`s` polynomials for s from 0 to order.
        
            The 1st column contains the G :sub:`s` values. The 2nd column contains the H :sub:`s` values.
        
        
        """
        ...
    _computeQns_1__T = typing.TypeVar('_computeQns_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def computeQns(gamma: float, nMax: int, sMax: int) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
        Compute the Q :sub:`n,s` coefficients evaluated at γ from the recurrence formula 2.8.3-(2).
        
        Q :sub:`n,s` coefficients are computed for n = 0 to nMax and s = 0 to sMax + 1 in order to also get the derivative dQ :sub:`n,s` /dγ = Q(n, s + 1)
        
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
    def computeQns(gamma: _computeQns_1__T, nMax: int, sMax: int) -> typing.MutableSequence[typing.MutableSequence[_computeQns_1__T]]:
        """
        Compute the Q :sub:`n,s` coefficients evaluated at γ from the recurrence formula 2.8.3-(2).
        
        Q :sub:`n,s` coefficients are computed for n = 0 to nMax and s = 0 to sMax + 1 in order to also get the derivative dQ :sub:`n,s` /dγ = Q(n, s + 1)
        
        Parameters:
            gamma (T): γ angle
            nMax (int): n max value
            sMax (int): s max value
        
        Returns:
            Q :sub:`n,s` coefficients array
        
        
        """
        ...
    @staticmethod
    def computeVns(order: int) -> java.util.SortedMap['CoefficientsFactory.NSKey', float]:
        """
        Compute the V :sub:`n,s` coefficients from 2.8.2-(1)(2).
        
        Parameters:
            order (int): Order of the computation. Computation will be done from 0 to order -1
        
        Returns:
            Map of the V :sub:`n, s` coefficients
        
        Since:
            11.3.3
        
        
        """
        ...
    @staticmethod
    def getVmns(m: int, n: int, s: int) -> float:
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
    Container class for common parameters used by all DSST forces.
    
    Most of them are defined in Danielson paper at § 2.1.
    """
    def __init__(self, orbit: org.orekit.orbits.FieldOrbit[_FieldAuxiliaryElements__T], retrogradeFactor: int):
        """
        Simple constructor.
        
        Parameters:
            orbit (FieldOrbit<FieldAuxiliaryElements> orbit): related mean orbit for auxiliary elements
            retrogradeFactor (int): retrograde factor I [Eq. 2.1.2-(2)]
        
        
        """
        ...
    def getB(self) -> _FieldAuxiliaryElements__T:
        """
        Get B = sqrt(1 - e²).
        
        Returns:
            B
        
        
        """
        ...
    def getC(self) -> _FieldAuxiliaryElements__T:
        """
        Get C = 1 + p² + q².
        
        Returns:
            C
        
        
        """
        ...
    def getDate(self) -> org.orekit.time.FieldAbsoluteDate[_FieldAuxiliaryElements__T]:
        """
        Get the date of the orbit.
        
        Returns:
            the date
        
        
        """
        ...
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
    def getH(self) -> _FieldAuxiliaryElements__T:
        """
        Get the y component of eccentricity vector.
        
        This element called h in DSST corresponds to ey for the EquinoctialOrbit
        
        Returns:
            h
        
        
        """
        ...
    def getK(self) -> _FieldAuxiliaryElements__T:
        """
        Get the x component of eccentricity vector.
        
        This element called k in DSST corresponds to ex for the EquinoctialOrbit
        
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
    def getOrbit(self) -> org.orekit.orbits.FieldOrbit[_FieldAuxiliaryElements__T]:
        """
        Get the orbit.
        
        Returns:
            the orbit
        
        
        """
        ...
    def getP(self) -> _FieldAuxiliaryElements__T:
        """
        Get the y component of inclination vector.
        
        This element called p in DSST corresponds to hy for the EquinoctialOrbit
        
        Returns:
            p
        
        
        """
        ...
    def getQ(self) -> _FieldAuxiliaryElements__T:
        """
        Get the x component of inclination vector.
        
        This element called q in DSST corresponds to hx for the EquinoctialOrbit
        
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
    def getVectorF(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAuxiliaryElements__T]:
        """
        Get equinoctial frame vector f.
        
        Returns:
            f vector
        
        
        """
        ...
    def getVectorG(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAuxiliaryElements__T]:
        """
        Get equinoctial frame vector g.
        
        Returns:
            g vector
        
        
        """
        ...
    def getVectorW(self) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_FieldAuxiliaryElements__T]:
        """
        Get equinoctial frame vector w.
        
        Returns:
            w vector
        
        
        """
        ...
    def toAuxiliaryElements(self) -> AuxiliaryElements:
        """
        Transforms the FieldAuxiliaryElements instance into an AuxiliaryElements instance.
        
        Returns:
            the AuxiliaryElements instance
        
        Since:
            11.3.3
        
        
        """
        ...

_FieldCjSjCoefficient__T = typing.TypeVar('_FieldCjSjCoefficient__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldCjSjCoefficient(typing.Generic[_FieldCjSjCoefficient__T]):
    """
    Compute the S :sub:`j` (k, h) and the C :sub:`j` (k, h) series and their partial derivatives with respect to k and h.
    
    Those series are given in Danielson paper by expression 2.5.3-(5):
    
    C :sub:`j` (k, h) + i S :sub:`j` (k, h) = (k+ih) :sup:`j`
    
    The C :sub:`j` (k, h) and the S :sub:`j` (k, h) elements are store as an ArrayList of Complex number, the C :sub:`j` (k, h) being represented by the real and the S :sub:`j` (k, h) by the imaginary part.
    """
    def __init__(self, k: _FieldCjSjCoefficient__T, h: _FieldCjSjCoefficient__T, field: org.hipparchus.Field[_FieldCjSjCoefficient__T]):
        """
        C :sub:`j` (k, h) and S :sub:`j` (k, h) constructor.
        
        Parameters:
            k (FieldCjSjCoefficient): k value
            h (FieldCjSjCoefficient): h value
            field (Field<FieldCjSjCoefficient> field): field for fieldElements
        
        
        """
        ...
    def getCj(self, j: int) -> _FieldCjSjCoefficient__T:
        """
        Get the C :sub:`j` coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            C :sub:`j`
        
        
        """
        ...
    def getDcjDh(self, j: int) -> _FieldCjSjCoefficient__T:
        """
        Get the dC :sub:`j` / dh coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`i` / d :sub:`k`
        
        
        """
        ...
    def getDcjDk(self, j: int) -> _FieldCjSjCoefficient__T:
        """
        Get the dC :sub:`j` / dk coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getDsjDh(self, j: int) -> _FieldCjSjCoefficient__T:
        """
        Get the dS :sub:`j` / dh coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`j` / d :sub:`h`
        
        
        """
        ...
    def getDsjDk(self, j: int) -> _FieldCjSjCoefficient__T:
        """
        Get the dS :sub:`j` / dk coefficient.
        
        Parameters:
            j (int): order
        
        Returns:
            :sub:`j` / d :sub:`k`
        
        
        """
        ...
    def getSj(self, j: int) -> _FieldCjSjCoefficient__T:
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
    Compute the G :sub:`js` , H :sub:`js` , I :sub:`js` and J :sub:`js` polynomials in the equinoctial elements h, k and the direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
    The expressions used are equations 4.1-(10) from the Danielson paper.
    """
    def __init__(self, k: _FieldGHIJjsPolynomials__T, h: _FieldGHIJjsPolynomials__T, alpha: _FieldGHIJjsPolynomials__T, beta: _FieldGHIJjsPolynomials__T):
        """
        Create a set of G :sub:`js` , H :sub:`js` , I :sub:`js` and J :sub:`js` polynomials.
        
        Parameters:
            k (FieldGHIJjsPolynomials): X component of the eccentricity vector
            h (FieldGHIJjsPolynomials): Y component of the eccentricity vector
            alpha (FieldGHIJjsPolynomials): direction cosine α
            beta (FieldGHIJjsPolynomials): direction cosine β
        
        
        """
        ...
    def getGjs(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the G :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the G :sub:`js`
        
        
        """
        ...
    def getHjs(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the H :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js`
        
        
        """
        ...
    def getIjs(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the I :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js`
        
        
        """
        ...
    def getJjs(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the J :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js`
        
        
        """
        ...
    def getdGjsdAlpha(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dG :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dα
        
        
        """
        ...
    def getdGjsdBeta(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dG :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dβ
        
        
        """
        ...
    def getdGjsdh(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dG :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dh
        
        
        """
        ...
    def getdGjsdk(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dG :sub:`js` / dk coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dk
        
        
        """
        ...
    def getdHjsdAlpha(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dH :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dα
        
        
        """
        ...
    def getdHjsdBeta(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dH :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dβ
        
        
        """
        ...
    def getdHjsdh(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dH :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dh
        
        
        """
        ...
    def getdHjsdk(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dH :sub:`js` / dk coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dk
        
        
        """
        ...
    def getdIjsdAlpha(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dI :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dα
        
        
        """
        ...
    def getdIjsdBeta(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dI :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dβ
        
        
        """
        ...
    def getdIjsdh(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dI :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dh
        
        
        """
        ...
    def getdIjsdk(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dI :sub:`js` / dk coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dk
        
        
        """
        ...
    def getdJjsdAlpha(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dJ :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js` / dα
        
        
        """
        ...
    def getdJjsdBeta(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dJ :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js` / dβ
        
        
        """
        ...
    def getdJjsdh(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
        """
        Get the dJ :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js` / dh
        
        
        """
        ...
    def getdJjsdk(self, j: int, s: int) -> _FieldGHIJjsPolynomials__T:
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
    Compute the G :sub:`ms` :sup:`j` and the H :sub:`ms` :sup:`j` polynomials in the equinoctial elements h, k and the direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
    The expressions used are equations 2.7.5-(1)(2) from the Danielson paper.
    """
    def __init__(self, k: _FieldGHmsjPolynomials__T, h: _FieldGHmsjPolynomials__T, alpha: _FieldGHmsjPolynomials__T, beta: _FieldGHmsjPolynomials__T, retroFactor: int, field: org.hipparchus.Field[_FieldGHmsjPolynomials__T]):
        """
        Create a set of G :sub:`ms` :sup:`j` and H :sub:`ms` :sup:`j` polynomials.
        
        Parameters:
            k (FieldGHmsjPolynomials): X component of the eccentricity vector
            h (FieldGHmsjPolynomials): Y component of the eccentricity vector
            alpha (FieldGHmsjPolynomials): direction cosine α
            beta (FieldGHmsjPolynomials): direction cosine β
            retroFactor (int): -1 if the orbit is represented as retrograde, +1 otherwise
            field (Field<FieldGHmsjPolynomials> field): field element
        
        
        """
        ...
    def getGmsj(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
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
    def getHmsj(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
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
    def getdGmsdAlpha(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdGmsdBeta(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdGmsdh(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdGmsdk(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...
    def getdHmsdAlpha(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdHmsdBeta(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdHmsdh(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdHmsdk(self, m: int, s: int, j: int) -> _FieldGHmsjPolynomials__T:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...

_FieldGammaMnsFunction__T = typing.TypeVar('_FieldGammaMnsFunction__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldGammaMnsFunction(typing.Generic[_FieldGammaMnsFunction__T]):
    """
    Compute the Γ :sup:`m` :sub:`n,s` (γ) function from equation 2.7.1-(13).
    """
    def __init__(self, nMax: int, gamma: _FieldGammaMnsFunction__T, I: int, field: org.hipparchus.Field[_FieldGammaMnsFunction__T]):
        """
        Simple constructor.
        
        Parameters:
            nMax (int): max value for n
            gamma (FieldGammaMnsFunction): γ
            I (int): retrograde factor
            field (Field<FieldGammaMnsFunction> field): field element
        
        
        """
        ...
    def getDerivative(self, m: int, n: int, s: int) -> _FieldGammaMnsFunction__T:
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
    def getValue(self, m: int, n: int, s: int) -> _FieldGammaMnsFunction__T:
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
    Interface for interpolation grids.
    
    An interpolation grid provides a grid of time points that can be used for interpolation processes.
    
    In the context of DSST propagation, an interpolation grid is used for the computation through interpolation of short periodics coefficients
    """
    def getGridPoints(self, stepStart: _FieldInterpolationGrid__T, stepEnd: _FieldInterpolationGrid__T) -> typing.MutableSequence[_FieldInterpolationGrid__T]:
        """
        Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Parameters:
            stepStart (FieldInterpolationGrid): start of the step
            stepEnd (FieldInterpolationGrid): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...

_FieldLnsCoefficients__T = typing.TypeVar('_FieldLnsCoefficients__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldLnsCoefficients(typing.Generic[_FieldLnsCoefficients__T]):
    """
    Compute the L :sub:`n` :sup:`s` (γ).
    
    The fomula used is:
    
    L :sub:`n` :sup:`s` (γ) = ( R / a ) :sup:`n` V :sub:`ns` Q :sup:`ns` (γ)
    """
    def __init__(self, nMax: int, sMax: int, Qns: typing.Union[typing.List[typing.MutableSequence[_FieldLnsCoefficients__T]], jpype.JArray], Vns: java.util.SortedMap[CoefficientsFactory.NSKey, float], roa: _FieldLnsCoefficients__T, field: org.hipparchus.Field[_FieldLnsCoefficients__T]):
        """
        Create a set of L :sub:`n` :sup:`s` (γ) coefficients.
        
        Parameters:
            nMax (int): maximum value for n
            sMax (int): maximum value for s
            Qns (FieldLnsCoefficients[][]): the Q :sup:`ns` (γ) coefficients
            Vns (SortedMap<NSKey, Double> Vns): the V :sub:`ns` coefficients
            roa (FieldLnsCoefficients): (R / a)
            field (Field<FieldLnsCoefficients> field): field used by default
        
        
        """
        ...
    def getLns(self, n: int, s: int) -> _FieldLnsCoefficients__T:
        """
        Get the value of L :sub:`n` :sup:`s` (γ).
        
        Parameters:
            n (int): n index
            s (int): s index
        
        Returns:
            L :sub:`n` :sup:`s` (γ)
        
        
        """
        ...
    def getdLnsdGamma(self, n: int, s: int) -> _FieldLnsCoefficients__T:
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
    Interpolated short periodics coefficients.
    
    Representation of a coefficient that need to be interpolated over time.
    
    The short periodics coefficients can be interpolated for faster computation. This class stores computed values of the coefficients through the method addGridPoint and gives an interpolated result through the method value.
    """
    def __init__(self, interpolationPoints: int):
        """
        Simple constructor.
        
        Parameters:
            interpolationPoints (int): number of points used in the interpolation
        
        
        """
        ...
    def addGridPoint(self, date: org.orekit.time.FieldAbsoluteDate[_FieldShortPeriodicsInterpolatedCoefficient__T], value: typing.Union[typing.List[_FieldShortPeriodicsInterpolatedCoefficient__T], jpype.JArray]) -> None:
        """
        Add a point to the interpolation grid.
        
        Parameters:
            date (FieldAbsoluteDate<FieldShortPeriodicsInterpolatedCoefficient> date): abscissa of the point
            value (FieldShortPeriodicsInterpolatedCoefficient[]): value of the element
        
        
        """
        ...
    def clearHistory(self) -> None:
        """
        Clear the recorded values from the interpolation grid.
        """
        ...
    def value(self, date: org.orekit.time.FieldAbsoluteDate[_FieldShortPeriodicsInterpolatedCoefficient__T]) -> typing.MutableSequence[_FieldShortPeriodicsInterpolatedCoefficient__T]:
        """
        Compute the value of the coefficient.
        
        Parameters:
            date (FieldAbsoluteDate<FieldShortPeriodicsInterpolatedCoefficient> date): date at which the coefficient should be computed
        
        Returns:
            value of the coefficient
        
        
        """
        ...

class GHIJjsPolynomials:
    """
    Compute the G :sub:`js` , H :sub:`js` , I :sub:`js` and J :sub:`js` polynomials in the equinoctial elements h, k and the direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
    The expressions used are equations 4.1-(10) from the Danielson paper.
    """
    def __init__(self, k: float, h: float, alpha: float, beta: float):
        """
        Create a set of G :sub:`js` , H :sub:`js` , I :sub:`js` and J :sub:`js` polynomials.
        
        Parameters:
            k (double): X component of the eccentricity vector
            h (double): Y component of the eccentricity vector
            alpha (double): direction cosine α
            beta (double): direction cosine β
        
        
        """
        ...
    def getGjs(self, j: int, s: int) -> float:
        """
        Get the G :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the G :sub:`js`
        
        
        """
        ...
    def getHjs(self, j: int, s: int) -> float:
        """
        Get the H :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js`
        
        
        """
        ...
    def getIjs(self, j: int, s: int) -> float:
        """
        Get the I :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js`
        
        
        """
        ...
    def getJjs(self, j: int, s: int) -> float:
        """
        Get the J :sub:`js` coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js`
        
        
        """
        ...
    def getdGjsdAlpha(self, j: int, s: int) -> float:
        """
        Get the dG :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dα
        
        
        """
        ...
    def getdGjsdBeta(self, j: int, s: int) -> float:
        """
        Get the dG :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dβ
        
        
        """
        ...
    def getdGjsdh(self, j: int, s: int) -> float:
        """
        Get the dG :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dh
        
        
        """
        ...
    def getdGjsdk(self, j: int, s: int) -> float:
        """
        Get the dG :sub:`js` / dk coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the dG :sub:`js` / dk
        
        
        """
        ...
    def getdHjsdAlpha(self, j: int, s: int) -> float:
        """
        Get the dH :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dα
        
        
        """
        ...
    def getdHjsdBeta(self, j: int, s: int) -> float:
        """
        Get the dH :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dβ
        
        
        """
        ...
    def getdHjsdh(self, j: int, s: int) -> float:
        """
        Get the dH :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dh
        
        
        """
        ...
    def getdHjsdk(self, j: int, s: int) -> float:
        """
        Get the dH :sub:`js` / dk coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the H :sub:`js` / dk
        
        
        """
        ...
    def getdIjsdAlpha(self, j: int, s: int) -> float:
        """
        Get the dI :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dα
        
        
        """
        ...
    def getdIjsdBeta(self, j: int, s: int) -> float:
        """
        Get the dI :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dβ
        
        
        """
        ...
    def getdIjsdh(self, j: int, s: int) -> float:
        """
        Get the dI :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dh
        
        
        """
        ...
    def getdIjsdk(self, j: int, s: int) -> float:
        """
        Get the dI :sub:`js` / dk coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the I :sub:`js` / dk
        
        
        """
        ...
    def getdJjsdAlpha(self, j: int, s: int) -> float:
        """
        Get the dJ :sub:`js` / dα coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js` / dα
        
        
        """
        ...
    def getdJjsdBeta(self, j: int, s: int) -> float:
        """
        Get the dJ :sub:`js` / dβ coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js` / dβ
        
        
        """
        ...
    def getdJjsdh(self, j: int, s: int) -> float:
        """
        Get the dJ :sub:`js` / dh coefficient.
        
        Parameters:
            j (int): j subscript
            s (int): s subscript
        
        Returns:
            the J :sub:`js` / dh
        
        
        """
        ...
    def getdJjsdk(self, j: int, s: int) -> float:
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
    Compute the G :sub:`ms` :sup:`j` and the H :sub:`ms` :sup:`j` polynomials in the equinoctial elements h, k and the direction cosines α and β and their partial derivatives with respect to k, h, α and β.
    
    The expressions used are equations 2.7.5-(1)(2) from the Danielson paper.
    """
    def __init__(self, k: float, h: float, alpha: float, beta: float, retroFactor: int):
        """
        Create a set of G :sub:`ms` :sup:`j` and H :sub:`ms` :sup:`j` polynomials.
        
        Parameters:
            k (double): X component of the eccentricity vector
            h (double): Y component of the eccentricity vector
            alpha (double): direction cosine α
            beta (double): direction cosine β
            retroFactor (int): -1 if the orbit is represented as retrograde, +1 otherwise
        
        
        """
        ...
    def getGmsj(self, m: int, s: int, j: int) -> float:
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
    def getHmsj(self, m: int, s: int, j: int) -> float:
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
    def getdGmsdAlpha(self, m: int, s: int, j: int) -> float:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdGmsdBeta(self, m: int, s: int, j: int) -> float:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdGmsdh(self, m: int, s: int, j: int) -> float:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdGmsdk(self, m: int, s: int, j: int) -> float:
        """
        Get the dG :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...
    def getdHmsdAlpha(self, m: int, s: int, j: int) -> float:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`α` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`α`
        
        
        """
        ...
    def getdHmsdBeta(self, m: int, s: int, j: int) -> float:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`β` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`β`
        
        
        """
        ...
    def getdHmsdh(self, m: int, s: int, j: int) -> float:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`h` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`h`
        
        
        """
        ...
    def getdHmsdk(self, m: int, s: int, j: int) -> float:
        """
        Get the dH :sub:`ms` :sup:`j` / d :sub:`k` coefficient.
        
        Parameters:
            m (int): m subscript
            s (int): s subscript
            j (int): order
        
        Returns:
            :sub:`ms` :sup:`j` / d :sub:`k`
        
        
        """
        ...

class GammaMnsFunction:
    """
    Compute the Γ :sup:`m` :sub:`n,s` (γ) function from equation 2.7.1-(13).
    """
    def __init__(self, nMax: int, gamma: float, I: int):
        """
        Simple constructor.
        
        Parameters:
            nMax (int): max value for n
            gamma (double): γ
            I (int): retrograde factor
        
        
        """
        ...
    def getDerivative(self, m: int, n: int, s: int) -> float:
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
    def getValue(self, m: int, n: int, s: int) -> float:
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
    Interface for interpolation grids.
    
    An interpolation grid provides a grid of time points that can be used for interpolation processes.
    
    In the context of DSST propagation, an interpolation grid is used for the computation through interpolation of short periodics coefficients
    """
    def getGridPoints(self, stepStart: float, stepEnd: float) -> typing.MutableSequence[float]:
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
    Provider of the Jacobi polynomials P :sub:`l` :sup:`v,w` .
    
    This class is used for DSSTTesseral computation and DSSTThirdBody.
    
    Since:
        6.1
    """
    _getValue_0__T = typing.TypeVar('_getValue_0__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getValue(l: int, v: int, w: int, gamma: org.hipparchus.analysis.differentiation.FieldGradient[_getValue_0__T]) -> org.hipparchus.analysis.differentiation.FieldGradient[_getValue_0__T]:
        """
        Returns the value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` evaluated at γ.
        
        This method is guaranteed to be thread-safe
        
        Parameters:
            l (int): degree of the polynomial
            v (int): v value
            w (int): w value
            gamma (FieldGradient<T> gamma): γ value
        
        Returns:
            value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` (γ)
        
        Since:
            10.2
        
        
        """
        ...
    @typing.overload
    @staticmethod
    def getValue(l: int, v: int, w: int, gamma: org.hipparchus.analysis.differentiation.Gradient) -> org.hipparchus.analysis.differentiation.Gradient:
        """
        Returns the value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` evaluated at γ.
        
        This method is guaranteed to be thread-safe
        
        It's not used in the code anymore, see getValueAndDerivative, but was kept for validation purpose.
        
        Parameters:
            l (int): degree of the polynomial
            v (int): v value
            w (int): w value
            gamma (Gradient): γ value
        
        Returns:
            value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` (γ)
        
        Since:
            10.2
        
        """
        ...
    @staticmethod
    def getValueAndDerivative(l: int, v: int, w: int, x: float) -> typing.MutableSequence[float]:
        """
        Returns the value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` evaluated at γ.
        
        This method is guaranteed to be thread-safe
        
        It was added to improve performances of DSST propagation with tesseral gravity field or third-body perturbations.
        
        See issue orekit.
        
        It appeared the "Gradient" version was degrading performances. This last was however kept for validation purposes.
        
        Parameters:
            l (int): degree of the polynomial
            v (int): v value
            w (int): w value
            x (double): x value
        
        Returns:
            value and derivatives of the Jacobi polynomial P :sub:`l` :sup:`v,w` (γ)
        
        Since:
            11.3.3
        
        
        """
        ...

class LnsCoefficients:
    """
    Compute the L :sub:`n` :sup:`s` (γ).
    
    The fomula used is:
    
    L :sub:`n` :sup:`s` (γ) = ( R / a ) :sup:`n` V :sub:`ns` Q :sup:`ns` (γ)
    """
    def __init__(self, nMax: int, sMax: int, Qns: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray], Vns: java.util.SortedMap[CoefficientsFactory.NSKey, float], roa: float):
        """
        Create a set of L :sub:`n` :sup:`s` (γ) coefficients.
        
        Parameters:
            nMax (int): maximum value for n
            sMax (int): maximum value for s
            Qns (double[][]): the Q :sup:`ns` (γ) coefficients
            Vns (SortedMap<NSKey, Double> Vns): the V :sub:`ns` coefficients
            roa (double): (R / a)
        
        
        """
        ...
    def getLns(self, n: int, s: int) -> float:
        """
        Get the value of L :sub:`n` :sup:`s` (γ).
        
        Parameters:
            n (int): n index
            s (int): s index
        
        Returns:
            L :sub:`n` :sup:`s` (γ)
        
        
        """
        ...
    def getdLnsdGamma(self, n: int, s: int) -> float:
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
    Implementation of the Modified Newcomb Operators.
    
    From equations 2.7.3 - (12)(13) of the Danielson paper, those operators are defined as:
    
    4(ρ + σ)Y :sub:`ρ,σ` :sup:`n,s` =
    
    2(2s - n)Y :sub:`ρ-1,σ` :sup:`n,s+1` + (s - n)Y :sub:`ρ-2,σ` :sup:`n,s+2`
    
    
    - 2(2s + n)Y :sub:`ρ,σ-1` :sup:`n,s-1` - (s+n)Y :sub:`ρ,σ-2` :sup:`n,s-2`
    
    + 2(2ρ + 2σ + 2 + 3n)Y :sub:`ρ-1,σ-1` :sup:`n,s`
    
    Initialization is given by : Y :sub:`0,0` :sup:`n,s` = 1
    
    Internally, the Modified Newcomb Operators are stored as an array of PolynomialFunction :
    
    Y :sub:`ρ,σ` :sup:`n,s` = P :sub:`k0` + P :sub:`k1` n + ... + P :sub:`kj` n :sup:`j`
    
    where the P :sub:`kj` are given by
    
    P :sub:`kj` = ∑ :sub:`j=0;ρ` a :sub:`j` s :sup:`j`
    """
    @staticmethod
    def getValue(rho: int, sigma: int, n: int, s: int) -> float:
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
    Interpolated short periodics coefficients.
    
    Representation of a coefficient that need to be interpolated over time.
    
    The short periodics coefficients can be interpolated for faster computation. This class stores computed values of the coefficients through the method addGridPoint and gives an interpolated result through the method value.
    """
    def __init__(self, interpolationPoints: int):
        """
        Simple constructor.
        
        Parameters:
            interpolationPoints (int): number of points used in the interpolation
        
        
        """
        ...
    def addGridPoint(self, date: org.orekit.time.AbsoluteDate, value: typing.Union[typing.List[float], jpype.JArray]) -> None:
        """
        Add a point to the interpolation grid.
        
        Parameters:
            date (AbsoluteDate): abscissa of the point
            value (double[]): value of the element
        
        
        """
        ...
    def clearHistory(self) -> None:
        """
        Clear the recorded values from the interpolation grid.
        """
        ...
    def value(self, date: org.orekit.time.AbsoluteDate) -> typing.MutableSequence[float]:
        """
        Compute the value of the coefficient.
        
        Parameters:
            date (AbsoluteDate): date at which the coefficient should be computed
        
        Returns:
            value of the coefficient
        
        
        """
        ...

class UpperBounds:
    """
    Utility class to compute upper bounds for truncation algorithms.
    """
    _getDnl_1__T = typing.TypeVar('_getDnl_1__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
    @typing.overload
    @staticmethod
    def getDnl(xx: float, xpl: float, n: int, l: int) -> float:
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
    def getDnl(xx: _getDnl_1__T, xpl: _getDnl_1__T, n: int, l: int) -> _getDnl_1__T:
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
    def getRnml(gamma: float, n: int, l: int, m: int, eps: int, irf: int) -> float:
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
    def getRnml(gamma: _getRnml_1__T, n: int, l: int, m: int, eps: int, irf: int) -> _getRnml_1__T:
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
    Interpolation grid where a fixed number of points are evenly spaced between the start and the end of the integration step.
    
    The grid is adapted to the step considered, meaning that for short steps, the grid will be dense, while for long steps the points will be far away one from each other
    """
    def __init__(self, field: org.hipparchus.Field[_FieldFixedNumberInterpolationGrid__T], pointsPerStep: int):
        """
        Constructor.
        
        Parameters:
            field (Field<FieldFixedNumberInterpolationGrid> field): field used by default
            pointsPerStep (int): number of points in the grid per step
        
        
        """
        ...
    def getGridPoints(self, stepStart: _FieldFixedNumberInterpolationGrid__T, stepEnd: _FieldFixedNumberInterpolationGrid__T) -> typing.MutableSequence[_FieldFixedNumberInterpolationGrid__T]:
        """
        Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Specified by: getGridPoints in interface FieldInterpolationGrid
        
        Parameters:
            stepStart (FieldFixedNumberInterpolationGrid): start of the step
            stepEnd (FieldFixedNumberInterpolationGrid): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...

_FieldMaxGapInterpolationGrid__T = typing.TypeVar('_FieldMaxGapInterpolationGrid__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class FieldMaxGapInterpolationGrid(FieldInterpolationGrid[_FieldMaxGapInterpolationGrid__T], typing.Generic[_FieldMaxGapInterpolationGrid__T]):
    """
    Interpolation grid where points obey a maximum time gap.
    
    The grid is adapted to the step considered, meaning that for short steps, the grid will have numerous points.
    
    Since:
        7.1
    """
    def __init__(self, field: org.hipparchus.Field[_FieldMaxGapInterpolationGrid__T], maxGap: _FieldMaxGapInterpolationGrid__T):
        """
        Constructor.
        
        Parameters:
            field (Field<FieldMaxGapInterpolationGrid> field): field used by default
            maxGap (FieldMaxGapInterpolationGrid): maximum time gap between interpolation points
        
        
        """
        ...
    def getGridPoints(self, stepStart: _FieldMaxGapInterpolationGrid__T, stepEnd: _FieldMaxGapInterpolationGrid__T) -> typing.MutableSequence[_FieldMaxGapInterpolationGrid__T]:
        """
        Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Specified by: getGridPoints in interface FieldInterpolationGrid
        
        Parameters:
            stepStart (FieldMaxGapInterpolationGrid): start of the step
            stepEnd (FieldMaxGapInterpolationGrid): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...

class FixedNumberInterpolationGrid(InterpolationGrid):
    """
    Interpolation grid where a fixed number of points are evenly spaced between the start and the end of the integration step.
    
    The grid is adapted to the step considered, meaning that for short steps, the grid will be dense, while for long steps the points will be far away one from each other
    """
    def __init__(self, pointsPerStep: int):
        """
        Constructor.
        
        Parameters:
            pointsPerStep (int): number of points in the grid per step
        
        
        """
        ...
    def getGridPoints(self, stepStart: float, stepEnd: float) -> typing.MutableSequence[float]:
        """
        Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Specified by: getGridPoints in interface InterpolationGrid
        
        Parameters:
            stepStart (double): start of the step
            stepEnd (double): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...

class MaxGapInterpolationGrid(InterpolationGrid):
    """
    Interpolation grid where points obey a maximum time gap.
    
    The grid is adapted to the step considered, meaning that for short steps, the grid will have numerous points.
    
    Since:
        7.1
    """
    def __init__(self, maxGap: float):
        """
        Constructor.
        
        Parameters:
            maxGap (double): maximum time gap between interpolation points
        
        
        """
        ...
    def getGridPoints(self, stepStart: float, stepEnd: float) -> typing.MutableSequence[float]:
        """
        Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Specified by: getGridPoints in interface InterpolationGrid
        
        Parameters:
            stepStart (double): start of the step
            stepEnd (double): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...

_PythonFieldInterpolationGrid__T = typing.TypeVar('_PythonFieldInterpolationGrid__T', bound=org.hipparchus.CalculusFieldElement)  # <T>
class PythonFieldInterpolationGrid(FieldInterpolationGrid[_PythonFieldInterpolationGrid__T], typing.Generic[_PythonFieldInterpolationGrid__T]):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getGridPoints(self, stepStart: _PythonFieldInterpolationGrid__T, stepEnd: _PythonFieldInterpolationGrid__T) -> typing.MutableSequence[_PythonFieldInterpolationGrid__T]:
        """
        Description copied from interface: getGridPoints Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Specified by: getGridPoints in interface FieldInterpolationGrid
        
        Parameters:
            stepStart (PythonFieldInterpolationGrid): start of the step
            stepEnd (PythonFieldInterpolationGrid): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...

class PythonInterpolationGrid(InterpolationGrid):
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Overrides: meth:`~org.orekit.propagation.semianalytical.dsst.utilities.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object.html?is` in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getGridPoints(self, stepStart: float, stepEnd: float) -> typing.MutableSequence[float]:
        """
        Description copied from interface: getGridPoints Get grid points that are within the current step.
        
        The step is defined by its start and its end time.
        
        Specified by: getGridPoints in interface InterpolationGrid
        
        Parameters:
            stepStart (double): start of the step
            stepEnd (double): end of the step
        
        Returns:
            time points between start and end
        
        
        """
        ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, pythonObject: int) -> None: ...


class __module_protocol__(Protocol):
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
    PythonFieldInterpolationGrid: typing.Type[PythonFieldInterpolationGrid]
    PythonInterpolationGrid: typing.Type[PythonInterpolationGrid]
    ShortPeriodicsInterpolatedCoefficient: typing.Type[ShortPeriodicsInterpolatedCoefficient]
    UpperBounds: typing.Type[UpperBounds]
    hansen: org.orekit.propagation.semianalytical.dsst.utilities.hansen.__module_protocol__
