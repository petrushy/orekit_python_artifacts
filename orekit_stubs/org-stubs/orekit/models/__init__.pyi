
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.io
import org.orekit.models.earth
import typing



class AtmosphericRefractionModel(java.io.Serializable):
    """
    Defines an refraction model that can be used to correct for the apparent position of an object due to atmospheric effects.
    
    Since:
        6.1
    """
    def getRefraction(self, trueElevation: float) -> float:
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
    Also see:
        serialized
    """
    def __init__(self): ...
    def finalize(self) -> None:
        """
        Part of JCC Python interface to object
        
        Overrides: Object in class Object
        
        Raises:
            Throwable: 
        
        """
        ...
    def getRefraction(self, trueElevation: float) -> float:
        """
        Compute the refraction angle from the true (geometrical) elevation. Extension point for Python.
        
        Specified by: getRefraction in interface AtmosphericRefractionModel
        
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
    def pythonExtension(self, pythonObject: int) -> None:
        """
        Part of JCC Python interface to object
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.models")``.

    AtmosphericRefractionModel: typing.Type[AtmosphericRefractionModel]
    PythonAtmosphericRefractionModel: typing.Type[PythonAtmosphericRefractionModel]
    earth: org.orekit.models.earth.__module_protocol__
