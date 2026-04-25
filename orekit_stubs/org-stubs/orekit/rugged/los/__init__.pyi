
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import java.util.stream
import org.hipparchus.analysis.differentiation
import org.hipparchus.analysis.polynomials
import org.hipparchus.geometry.euclidean.threed
import org.orekit.rugged.utils
import org.orekit.time
import org.orekit.utils
import typing



class LOSBuilder:
    """
    Builder for lines-of-sight list.
    
    This class implements the builder pattern to create TimeDependentLOS instances. It does so by using a fluent API in order to clarify reading and allow later extensions with new configuration parameters.
    
    This builder aims at creating lines-of-sight directions which are the result of several transforms applied to an initial list of raw directions. It therefore allows to take into account the optical path due to mirrors and the alignments of sensors frames with respect to a spacecraft.
    
    Also see:
        TimeDependentLOS,
        Builder_pattern,
        Fluent_interface
    """
    def __init__(self, rawLOS: java.util.List[org.hipparchus.geometry.euclidean.threed.Vector3D]):
        """
        Create builder.
        
        Parameters:
            rawLOS (List<org.hipparchus.geometry.euclidean.threed.Vector3D> rawLOS): raw fixed lines-of-sight
        
        
        """
        ...
    @typing.overload
    def addTransform(self, lOSTransform: 'LOSTransform') -> 'LOSBuilder':
        """
        Add a transform to be applied after the already registered transforms.
        
        Parameters:
            transform (TimeIndependentLOSTransform): transform to be applied to the lines-of-sight
        
        Returns:
            the builder instance
        
        Add a transform to be applied after the already registered transforms.
        
        Parameters:
            transform (LOSTransform): transform to be applied to the lines-of-sight
        
        Returns:
            the builder instance
        
        
        """
        ...
    @typing.overload
    def addTransform(self, timeIndependentLOSTransform: 'TimeIndependentLOSTransform') -> 'LOSBuilder': ...
    def build(self) -> 'TimeDependentLOS':
        """
        Build a lines-of-sight provider.
        
        Returns:
            lines-of-sight provider
        
        
        """
        ...

class LOSTransform:
    """
    Interface for lines-of-sight transforms.
    
    Also see:
        LOSBuilder
    """
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for LOS parameters.
        
        Returns:
            drivers for LOS parameters
        
        Since:
            2.0
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, index: int, los: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], date: org.orekit.time.AbsoluteDate, generator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
        Transform a line-of-sight and its partial derivatives.
        
        This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used for example to model thermo-elastic effects.
        
        Parameters:
            index (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
            date (org.orekit.time.AbsoluteDate): date
            generator (DerivativeGenerator<T> generator): generator to use for building DerivativeStructure instances
        
        Returns:
            line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.Vector3D, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a line-of-sight.
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
            date (org.orekit.time.AbsoluteDate): current date
        
        Returns:
            transformed line-of-sight
        
        """
        ...

class TimeDependentLOS:
    """
    Interface representing a line-of-sight which depends on time.
    
    Also see:
        LineSensor
    """
    def getLOS(self, index: int, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Get the line of sight for a given date.
        
        Parameters:
            index (int): los pixel index
            date (org.orekit.time.AbsoluteDate): date
        
        Returns:
            line of sight
        
        
        """
        ...
    _getLOSDerivatives__T = typing.TypeVar('_getLOSDerivatives__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    def getLOSDerivatives(self, index: int, date: org.orekit.time.AbsoluteDate, generator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives__T]:
        """
        Get the line of sight and its partial derivatives for a given date.
        
        This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to the estimated parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used for example to model thermo-elastic effects.
        
        Note that in order for the partial derivatives to be properly set up, the setSelected method must have been set to true for the various parameters returned by getParametersDrivers that should be estimated.
        
        Parameters:
            index (int): los pixel index
            date (org.orekit.time.AbsoluteDate): date
            generator (DerivativeGenerator<T> generator): generator to use for building Derivative instances
        
        Returns:
            line of sight, and its first partial derivatives with respect to the parameters
        
        Since:
            2.0
        
        
        """
        ...
    def getNbPixels(self) -> int:
        """
        Get the number of pixels.
        
        Returns:
            number of pixels
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for LOS parameters.
        
        Returns:
            drivers for LOS parameters
        
        Since:
            2.0
        
        
        """
        ...

class TimeIndependentLOSTransform:
    """
    Interface for lines-of-sight tranforms that do not depend on time.
    
    Also see:
        LOSBuilder
    """
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for LOS parameters.
        
        Returns:
            drivers for LOS parameters
        
        Since:
            2.0
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, index: int, los: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], generator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
        Transform a line-of-sight and its partial derivatives.
        
        This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used for example to model thermo-elastic effects.
        
        Note that in order for the partial derivatives to be properly set up, the setSelected method must have been set to true for the various parameters returned by getParametersDrivers that should be estimated.
        
        Parameters:
            index (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
            generator (DerivativeGenerator<T> generator): generator to use for building Derivative instances
        
        Returns:
            line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a line-of-sight.
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
        
        Returns:
            transformed line-of-sight
        
        """
        ...

class FixedRotation(TimeIndependentLOSTransform):
    """
    TimeIndependentLOSTransform based on a fixed rotation.
    
    Also see:
        LOSBuilder
    """
    def __init__(self, name: str, axis: org.hipparchus.geometry.euclidean.threed.Vector3D, angle: float):
        """
        Simple constructor.
        
        The single parameter is the rotation angle.
        
        Parameters:
            name (String): name of the rotation (used for estimated parameters identification)
            axis (org.hipparchus.geometry.euclidean.threed.Vector3D): rotation axis
            angle (double): rotation angle
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for LOS parameters.
        
        Specified by: getParametersDrivers in interface TimeIndependentLOSTransform
        
        Returns:
            drivers for LOS parameters
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], generator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
        Transform a line-of-sight and its partial derivatives.
        
        This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used for example to model thermo-elastic effects.
        
        Note that in order for the partial derivatives to be properly set up, the setSelected method must have been set to true for the various parameters returned by getParametersDrivers that should be estimated.
        
        Specified by: transformLOS in interface TimeIndependentLOSTransform
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
            generator (DerivativeGenerator<T> generator): generator to use for building Derivative instances
        
        Returns:
            line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a line-of-sight.
        
        Specified by: transformLOS in interface TimeIndependentLOSTransform
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
        
        Returns:
            transformed line-of-sight
        
        """
        ...

class FixedZHomothety(TimeIndependentLOSTransform):
    """
    TimeIndependentLOSTransform based on a homothety along the Z axis.
    
    Since:
        2.0
    
    Also see:
        LOSBuilder
    """
    def __init__(self, name: str, factorvalue: float):
        """
        Simple constructor.
        
        The single parameter is the homothety factor.
        
        Parameters:
            name (String): name of the homothety (used for estimated parameters identification)
            factorvalue (double): homothety factor
        
        
        """
        ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for LOS parameters.
        
        Specified by: getParametersDrivers in interface TimeIndependentLOSTransform
        
        Returns:
            drivers for LOS parameters
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], generator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
        Transform a line-of-sight and its partial derivatives.
        
        This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used for example to model thermo-elastic effects.
        
        Note that in order for the partial derivatives to be properly set up, the setSelected method must have been set to true for the various parameters returned by getParametersDrivers that should be estimated.
        
        Specified by: transformLOS in interface TimeIndependentLOSTransform
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
            generator (DerivativeGenerator<T> generator): generator to use for building Derivative instances
        
        Returns:
            line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a line-of-sight.
        
        Specified by: transformLOS in interface TimeIndependentLOSTransform
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
        
        Returns:
            transformed line-of-sight
        
        """
        ...

class PolynomialRotation(LOSTransform):
    """
    LOSTransform based on a rotation with polynomial angle.
    
    Also see:
        LOSBuilder
    """
    @typing.overload
    def __init__(self, string: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, *double: float): ...
    @typing.overload
    def __init__(self, string: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, polynomialFunction: org.hipparchus.analysis.polynomials.PolynomialFunction): ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
        Get the drivers for LOS parameters.
        
        Specified by: getParametersDrivers in interface LOSTransform
        
        Returns:
            drivers for LOS parameters
        
        Since:
            2.0
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], date: org.orekit.time.AbsoluteDate, generator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
        Transform a line-of-sight and its partial derivatives.
        
        This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used for example to model thermo-elastic effects.
        
        Specified by: transformLOS in interface LOSTransform
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
            date (org.orekit.time.AbsoluteDate): date
            generator (DerivativeGenerator<T> generator): generator to use for building DerivativeStructure instances
        
        Returns:
            line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, i: int, los: org.hipparchus.geometry.euclidean.threed.Vector3D, date: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
        Transform a line-of-sight.
        
        Specified by: transformLOS in interface LOSTransform
        
        Parameters:
            i (int): los pixel index
            los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
            date (org.orekit.time.AbsoluteDate): current date
        
        Returns:
            transformed line-of-sight
        
        """
        ...

class PythonLOSTransformI(LOSTransform):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]: ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...

class PythonTimeDependentLOS(TimeDependentLOS):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getLOS(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...
    _getLOSDerivatives__T = typing.TypeVar('_getLOSDerivatives__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    def getLOSDerivatives(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives__T]: ...
    def getNbPixels(self) -> int: ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...

class PythonTimeIndependentLOSTransform(TimeIndependentLOSTransform):
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]: ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.los")``.

    FixedRotation: typing.Type[FixedRotation]
    FixedZHomothety: typing.Type[FixedZHomothety]
    LOSBuilder: typing.Type[LOSBuilder]
    LOSTransform: typing.Type[LOSTransform]
    PolynomialRotation: typing.Type[PolynomialRotation]
    PythonLOSTransformI: typing.Type[PythonLOSTransformI]
    PythonTimeDependentLOS: typing.Type[PythonTimeDependentLOS]
    PythonTimeIndependentLOSTransform: typing.Type[PythonTimeIndependentLOSTransform]
    TimeDependentLOS: typing.Type[TimeDependentLOS]
    TimeIndependentLOSTransform: typing.Type[TimeIndependentLOSTransform]
