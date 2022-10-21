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
    public class LOSBuilder extends Object
    
        Builder for lines-of-sight list.
    
        This class implements the *builder pattern* to create :class:`~org.orekit.rugged.los.TimeDependentLOS` instances. It
        does so by using a *fluent API* in order to clarify reading and allow later extensions with new configuration
        parameters.
    
        This builder aims at creating lines-of-sight directions which are the result of several transforms applied to an initial
        list of raw directions. It therefore allows to take into account the optical path due to mirrors and the alignments of
        sensors frames with respect to a spacecraft.
    
        Also see:
            :class:`~org.orekit.rugged.los.TimeDependentLOS`, Builder pattern (wikipedia), Fluent interface (wikipedia)
    """
    def __init__(self, list: java.util.List[org.hipparchus.geometry.euclidean.threed.Vector3D]): ...
    @typing.overload
    def addTransform(self, lOSTransform: 'LOSTransform') -> 'LOSBuilder':
        """
            Add a transform to be applied after the already registered transforms.
        
            Parameters:
                transform (:class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`): transform to be applied to the lines-of-sight
        
            Returns:
                the builder instance
        
            Add a transform to be applied after the already registered transforms.
        
            Parameters:
                transform (:class:`~org.orekit.rugged.los.LOSTransform`): transform to be applied to the lines-of-sight
        
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
    public interface LOSTransform
    
        Interface for lines-of-sight transforms.
    
        Also see:
            :class:`~org.orekit.rugged.los.LOSBuilder`
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
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
            Transform a line-of-sight and its partial derivatives.
        
            This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to
            the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used
            for example to model thermo-elastic effects.
        
            Parameters:
                index (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
                date (org.orekit.time.AbsoluteDate): date
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`DerivativeStructure` instances
        
            Returns:
                line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    public interface TimeDependentLOS
    
        Interface representing a line-of-sight which depends on time.
    
        Also see:
            :class:`~org.orekit.rugged.linesensor.LineSensor`
    """
    def getLOS(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    def getLOSDerivatives(self, int: int, absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_getLOSDerivatives__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_getLOSDerivatives__T]:
        """
            Get the line of sight and its partial derivatives for a given date.
        
            This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to
            the estimated parameters, which are typically polynomials coefficients representing rotation angles. These polynomials
            can be used for example to model thermo-elastic effects.
        
            Note that in order for the partial derivatives to be properly set up, the :code:`setSelected` method must have been set
            to :code:`true` for the various parameters returned by
            :meth:`~org.orekit.rugged.los.TimeDependentLOS.getParametersDrivers` that should be estimated.
        
            Parameters:
                index (int): los pixel index
                date (org.orekit.time.AbsoluteDate): date
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
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
    public interface TimeIndependentLOSTransform
    
        Interface for lines-of-sight tranforms that do not depend on time.
    
        Also see:
            :class:`~org.orekit.rugged.los.LOSBuilder`
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
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
            Transform a line-of-sight and its partial derivatives.
        
            This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to
            the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used
            for example to model thermo-elastic effects.
        
            Note that in order for the partial derivatives to be properly set up, the :code:`setSelected` method must have been set
            to :code:`true` for the various parameters returned by
            :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.getParametersDrivers` that should be estimated.
        
            Parameters:
                index (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
            Returns:
                line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
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
    public class FixedRotation extends Object implements :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
    
        :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform` based on a fixed rotation.
    
        Also see:
            :class:`~org.orekit.rugged.los.LOSBuilder`
    """
    def __init__(self, string: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, double: float): ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
            Get the drivers for LOS parameters.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.getParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
        
            Returns:
                drivers for LOS parameters
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
            Transform a line-of-sight and its partial derivatives.
        
            This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to
            the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used
            for example to model thermo-elastic effects.
        
            Note that in order for the partial derivatives to be properly set up, the :code:`setSelected` method must have been set
            to :code:`true` for the various parameters returned by
            :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.getParametersDrivers` that should be estimated.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.transformLOS`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
        
            Parameters:
                i (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
            Returns:
                line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a line-of-sight.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.transformLOS`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
        
            Parameters:
                i (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
        
            Returns:
                transformed line-of-sight
        
        """
        ...

class FixedZHomothety(TimeIndependentLOSTransform):
    """
    public class FixedZHomothety extends Object implements :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
    
        :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform` based on a homothety along the Z axis.
    
        Since:
            2.0
    
        Also see:
            :class:`~org.orekit.rugged.los.LOSBuilder`
    """
    def __init__(self, string: str, double: float): ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
            Get the drivers for LOS parameters.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.getParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
        
            Returns:
                drivers for LOS parameters
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
            Transform a line-of-sight and its partial derivatives.
        
            This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to
            the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used
            for example to model thermo-elastic effects.
        
            Note that in order for the partial derivatives to be properly set up, the :code:`setSelected` method must have been set
            to :code:`true` for the various parameters returned by
            :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.getParametersDrivers` that should be estimated.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.transformLOS`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
        
            Parameters:
                i (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`Derivative` instances
        
            Returns:
                line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a line-of-sight.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.TimeIndependentLOSTransform.transformLOS`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.TimeIndependentLOSTransform`
        
            Parameters:
                i (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
        
            Returns:
                transformed line-of-sight
        
        """
        ...

class PolynomialRotation(LOSTransform):
    """
    public class PolynomialRotation extends Object implements :class:`~org.orekit.rugged.los.LOSTransform`
    
        :class:`~org.orekit.rugged.los.LOSTransform` based on a rotation with polynomial angle.
    
        Also see:
            :class:`~org.orekit.rugged.los.LOSBuilder`
    """
    @typing.overload
    def __init__(self, string: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, *double: float): ...
    @typing.overload
    def __init__(self, string: str, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate, polynomialFunction: org.hipparchus.analysis.polynomials.PolynomialFunction): ...
    def getParametersDrivers(self) -> java.util.stream.Stream[org.orekit.utils.ParameterDriver]:
        """
            Get the drivers for LOS parameters.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.LOSTransform.getParametersDrivers`Â in
                interfaceÂ :class:`~org.orekit.rugged.los.LOSTransform`
        
            Returns:
                drivers for LOS parameters
        
            Since:
                2.0
        
        
        """
        ...
    _transformLOS_0__T = typing.TypeVar('_transformLOS_0__T', bound=org.hipparchus.analysis.differentiation.Derivative)  # <T>
    @typing.overload
    def transformLOS(self, int: int, fieldVector3D: org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T], absoluteDate: org.orekit.time.AbsoluteDate, derivativeGenerator: org.orekit.rugged.utils.DerivativeGenerator[_transformLOS_0__T]) -> org.hipparchus.geometry.euclidean.threed.FieldVector3D[_transformLOS_0__T]:
        """
            Transform a line-of-sight and its partial derivatives.
        
            This method is used for LOS calibration purposes. It allows to compute the Jacobian matrix of the LOS with respect to
            the parameters, which are typically polynomials coefficients representing rotation angles. These polynomials can be used
            for example to model thermo-elastic effects.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.LOSTransform.transformLOS` in interface :class:`~org.orekit.rugged.los.LOSTransform`
        
            Parameters:
                i (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.FieldVector3D<T> los): line-of-sight to transform
                date (org.orekit.time.AbsoluteDate): date
                generator (:class:`~org.orekit.rugged.utils.DerivativeGenerator`<T> generator): generator to use for building :code:`DerivativeStructure` instances
        
            Returns:
                line of sight, and its first partial derivatives with respect to the parameters
        
        
        """
        ...
    @typing.overload
    def transformLOS(self, int: int, vector3D: org.hipparchus.geometry.euclidean.threed.Vector3D, absoluteDate: org.orekit.time.AbsoluteDate) -> org.hipparchus.geometry.euclidean.threed.Vector3D:
        """
            Transform a line-of-sight.
        
            Specified by:
                :meth:`~org.orekit.rugged.los.LOSTransform.transformLOS` in interface :class:`~org.orekit.rugged.los.LOSTransform`
        
            Parameters:
                i (int): los pixel index
                los (org.hipparchus.geometry.euclidean.threed.Vector3D): line-of-sight to transform
                date (org.orekit.time.AbsoluteDate): current date
        
            Returns:
                transformed line-of-sight
        
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged.los")``.

    FixedRotation: typing.Type[FixedRotation]
    FixedZHomothety: typing.Type[FixedZHomothety]
    LOSBuilder: typing.Type[LOSBuilder]
    LOSTransform: typing.Type[LOSTransform]
    PolynomialRotation: typing.Type[PolynomialRotation]
    TimeDependentLOS: typing.Type[TimeDependentLOS]
    TimeIndependentLOSTransform: typing.Type[TimeIndependentLOSTransform]
