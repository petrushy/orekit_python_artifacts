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
    def __init__(self): ...
    def finalize(self) -> None: ...
    def getRefraction(self, double: float) -> float: ...
    def pythonDecRef(self) -> None: ...
    @typing.overload
    def pythonExtension(self) -> int: ...
    @typing.overload
    def pythonExtension(self, long: int) -> None: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models")``.

    AtmosphericRefractionModel: typing.Type[AtmosphericRefractionModel]
    PythonAtmosphericRefractionModel: typing.Type[PythonAtmosphericRefractionModel]
    earth: org.orekit.models.earth.__module_protocol__
