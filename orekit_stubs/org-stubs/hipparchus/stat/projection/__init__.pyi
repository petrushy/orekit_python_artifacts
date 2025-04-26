
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import jpype
import typing



class PCA:
    """
    public classPCA extends :class:`~org.hipparchus.stat.projection.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object`
    
        Principal component analysis (PCA) is a statistical technique for reducing the dimensionality of a dataset.
        :class:`~org.hipparchus.stat.projection.https:.en.wikipedia.org.wiki.Principal_component_analysis` can be thought of as
        a projection or scaling of the data to reduce the number of dimensions but done in a way that preserves as much
        information as possible.
    
        Since:
            3.0
    """
    @typing.overload
    def __init__(self, int: int): ...
    @typing.overload
    def __init__(self, int: int, boolean: bool, boolean2: bool): ...
    def fit(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> 'PCA':
        """
            Fit our model to the data, ready for subsequence transforms.
        
            Parameters:
                data (double[][]): the input data
        
            Returns:
                this
        
        
        """
        ...
    def fitAndTransform(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Fit our model to the data and then transform it to the reduced dimensions.
        
            Parameters:
                data (double[][]): the input data
        
            Returns:
                the fitted data
        
        
        """
        ...
    def getCenter(self) -> typing.MutableSequence[float]:
        """
            Get by column center (or mean) of the fitted data.
        
            Returns:
                the by column center (or mean) of the fitted data
        
        
        """
        ...
    def getComponents(self) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Returns the principal components of our projection model. These are the eigenvectors of our covariance/correlation
            matrix.
        
            Returns:
                the principal components
        
        
        """
        ...
    def getNumComponents(self) -> int:
        """
            GEt number of components.
        
            Returns:
                the number of components
        
        
        """
        ...
    def getVariance(self) -> typing.MutableSequence[float]:
        """
            Get principal component variances.
        
            Returns:
                the principal component variances, ordered from largest to smallest, which are the eigenvalues of the covariance or
                correlation matrix of the fitted data
        
        
        """
        ...
    def isBiasCorrection(self) -> bool:
        """
            Check whether scaling (correlation), if in use, adjusts for bias.
        
            Returns:
                whether scaling (correlation), if in use, adjusts for bias
        
        
        """
        ...
    def isScale(self) -> bool:
        """
            Check whether scaling (correlation) or no scaling (covariance) is used.
        
            Returns:
                whether scaling (correlation) or no scaling (covariance) is used
        
        
        """
        ...
    def transform(self, doubleArray: typing.Union[typing.List[typing.MutableSequence[float]], jpype.JArray]) -> typing.MutableSequence[typing.MutableSequence[float]]:
        """
            Transform the supplied data using our projection model.
        
            Parameters:
                data (double[][]): the input data
        
            Returns:
                the fitted data
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.projection")``.

    PCA: typing.Type[PCA]
