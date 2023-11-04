import typing



class PCA:
    """
    public class PCA extends :class:`~org.hipparchus.stat.projection.https:.docs.oracle.com.javase.8.docs.api.java.lang.Object?is`
    
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
    def fit(self, doubleArray: typing.List[typing.List[float]]) -> 'PCA':
        """
            Fit our model to the data, ready for subsequence transforms.
        
            Parameters:
                data (double[][]): the input data
        
            Returns:
                this
        
        
        """
        ...
    def fitAndTransform(self, doubleArray: typing.List[typing.List[float]]) -> typing.List[typing.List[float]]:
        """
            Fit our model to the data and then transform it to the reduced dimensions.
        
            Parameters:
                data (double[][]): the input data
        
            Returns:
                the fitted data
        
        
        """
        ...
    def getCenter(self) -> typing.List[float]:
        """
            Get by column center (or mean) of the fitted data.
        
            Returns:
                the by column center (or mean) of the fitted data
        
        
        """
        ...
    def getComponents(self) -> typing.List[typing.List[float]]:
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
    def getVariance(self) -> typing.List[float]:
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
    def transform(self, doubleArray: typing.List[typing.List[float]]) -> typing.List[typing.List[float]]:
        """
            Transform the supplied data using our projection model.
        
            Parameters:
                data (double[][]): the input data
        
            Returns:
                the fitted data
        
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.stat.projection")``.

    PCA: typing.Type[PCA]
