
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import jpype
import org.orekit.gnss.metric.messages.ssr
import org.orekit.models.earth.ionosphere
import typing



class SsrIm201(org.orekit.gnss.metric.messages.ssr.SsrMessage['SsrIm201Header', 'SsrIm201Data']):
    """
    public class SsrIm201 extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrMessage`<:class:`~org.orekit.gnss.metric.messages.ssr.subtype.SsrIm201Header`, :class:`~org.orekit.gnss.metric.messages.ssr.subtype.SsrIm201Data`>
    
        SSR Ionosphere VTEC Spherical Harmonics Message.
    
        Since:
            11.0
    """
    def __init__(self, int: int, ssrIm201Header: 'SsrIm201Header', list: java.util.List['SsrIm201Data']): ...
    def getIonosphericModel(self) -> org.orekit.models.earth.ionosphere.SsrVtecIonosphericModel:
        """
            Get the ionospheric model adapted to the current IM201 message.
        
            Returns:
                the ionospheric model
        
        
        """
        ...

class SsrIm201Data(org.orekit.gnss.metric.messages.ssr.SsrData):
    """
    public class SsrIm201Data extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrData`
    
        Container for SSR IM201 data.
    
        One instance of this class corresponds to one ionospheric layer.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getCnm(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Get the cosine parameters of spherical harmonics expansion of degree N and order M.
        
            The size of the array is (N + 1) x (M + 1)
        
            Returns:
                the cosine parameters in TECU
        
        
        """
        ...
    def getHeightIonosphericLayer(self) -> float:
        """
            Get the height of the ionospheric layer.
        
            Returns:
                the height of the ionospheric layer in meters
        
        
        """
        ...
    def getSnm(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Get the sine parameters of spherical harmonics expansion of degree N and order M.
        
            The size of the array is (N + 1) x (M + 1)
        
            Returns:
                the sine parameters in TECU
        
        
        """
        ...
    def getSphericalHarmonicsDegree(self) -> int:
        """
            Get the degree of spherical harmonic expansion.
        
            Returns:
                the degree of spherical harmonic expansion
        
        
        """
        ...
    def getSphericalHarmonicsOrder(self) -> int:
        """
            Get the order of spherical harmonic expansion.
        
            Returns:
                the order the order of spherical harmonic expansion
        
        
        """
        ...
    def setCnm(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Set the cosine parameters of spherical harmonics expansion of degree N and order M.
        
            Parameters:
                cnm (double[][]): the parameters to set
        
        
        """
        ...
    def setHeightIonosphericLayer(self, double: float) -> None:
        """
            Set the height of the ionospheric layer.
        
            Parameters:
                heightIonosphericLayer (double): the height to set in meters
        
        
        """
        ...
    def setSnm(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> None:
        """
            Set the sine parameters of spherical harmonics expansion of degree N and order M.
        
            Parameters:
                snm (double[][]): the parameters to set
        
        
        """
        ...
    def setSphericalHarmonicsDegree(self, int: int) -> None:
        """
            Set the degree of spherical harmonic expansion.
        
            Parameters:
                sphericalHarmonicsDegree (int): the degree to set
        
        
        """
        ...
    def setSphericalHarmonicsOrder(self, int: int) -> None:
        """
            Set the order of spherical harmonic expansion.
        
            Parameters:
                sphericalHarmonicsOrder (int): the order to set
        
        
        """
        ...

class SsrIm201Header(org.orekit.gnss.metric.messages.ssr.SsrHeader):
    """
    public class SsrIm201Header extends :class:`~org.orekit.gnss.metric.messages.ssr.SsrHeader`
    
        Container for SSR IM201 header.
    
        Since:
            11.0
    """
    def __init__(self): ...
    def getNumberOfIonosphericLayers(self) -> int:
        """
            Get the number of ionospheric layers.
        
            Returns:
                the number of ionospheric layers
        
        
        """
        ...
    def getVtecQualityIndicator(self) -> float:
        """
            Get the VTEC quality indicator.
        
            Returns:
                the VTEC quality indicator in TECU
        
        
        """
        ...
    def setNumberOfIonosphericLayers(self, int: int) -> None:
        """
            Set the number of ionospheric layers.
        
            Parameters:
                numberOfIonosphericLayers (int): the number to set
        
        
        """
        ...
    def setVtecQualityIndicator(self, double: float) -> None:
        """
            Set the VTEC quality indicator.
        
            Parameters:
                vtecQualityIndicator (double): the VTEC quality indicator to set in TECU
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric.messages.ssr.subtype")``.

    SsrIm201: typing.Type[SsrIm201]
    SsrIm201Data: typing.Type[SsrIm201Data]
    SsrIm201Header: typing.Type[SsrIm201Header]
