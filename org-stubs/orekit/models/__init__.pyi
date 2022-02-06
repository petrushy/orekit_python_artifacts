import java.io
import org.orekit.models.earth
import typing



class AtmosphericRefractionModel(java.io.Serializable):
    """
    public interface AtmosphericRefractionModel extends Serializable
    
        Defines an refraction model that can be used to correct for the apparent position of an object due to atmospheric
        effects.
    
        Since:
            6.1
    """
    def getRefraction(self, double: float) -> float:
        """
            Compute the refraction angle from the true (geometrical) elevation.
        
            Parameters:
                trueElevation (double): true elevation (rad)
        
            Returns:
                refraction angle (rad)
        
        
        """
        ...

class PythonAtmosphericRefractionModel(AtmosphericRefractionModel):
    """
    public class PythonAtmosphericRefractionModel extends Object implements :class:`~org.orekit.models.AtmosphericRefractionModel`
    
    
        Also see:
            :meth:`~serialized`
    """
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getRefraction(self, double: float) -> float:
        """
            Compute the refraction angle from the true (geometrical) elevation. Extension point for Python.
        
            Specified by:
                :meth:`~org.orekit.models.AtmosphericRefractionModel.getRefraction`Â in
                interfaceÂ :class:`~org.orekit.models.AtmosphericRefractionModel`
        
            Parameters:
                trueElevation (double): true elevation (rad)
        
            Returns:
                refraction angle (rad)
        
        
        """
        ...
    def pythonDecRef(self) -> None:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self) -> int:
        """
            Part of JCC Python interface to object
        
        """
        ...
    @typing.overload
    def pythonExtension(self, long: int) -> None:
        """
            Part of JCC Python interface to object
        """
        ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models")``.

    AtmosphericRefractionModel: typing.Type[AtmosphericRefractionModel]
    PythonAtmosphericRefractionModel: typing.Type[PythonAtmosphericRefractionModel]
    earth: org.orekit.models.earth.__module_protocol__
