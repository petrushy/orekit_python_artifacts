
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.util
import org.orekit.data
import org.orekit.files.rinex.clock
import org.orekit.files.rinex.navigation
import org.orekit.files.rinex.observation
import org.orekit.files.rinex.section
import org.orekit.files.rinex.utils
import org.orekit.gnss
import typing



class AppliedDCBS:
    """
    Corrections of Differential Code Biases (DCBs) applied. Contains information on the programs used to correct the observations in RINEX or clock files for differential code biases.
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, progDCBS: str, sourceDCBS: str):
        """
        Simple constructor.
        
        Parameters:
            satelliteSystem (SatelliteSystem): satellite system
            progDCBS (String): Program name used to apply DCBs
            sourceDCBS (String): Source of corrections (URL)
        
        
        """
        ...
    def getProgDCBS(self) -> str:
        """
        Get the program name used to apply DCBs.
        
        Returns:
            Program name used to apply DCBs
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
        Get the satellite system.
        
        Returns:
            satellite system
        
        
        """
        ...
    def getSourceDCBS(self) -> str:
        """
        Get the source of corrections.
        
        Returns:
            Source of corrections (URL)
        
        
        """
        ...

class AppliedPCVS:
    """
    Corrections of antenna phase center variations (PCVs) applied. Contains information on the programs used to correct the observations in RINEX or clock files for antenna phase center variations.
    """
    def __init__(self, satelliteSystem: org.orekit.gnss.SatelliteSystem, progPCVS: str, sourcePCVS: str):
        """
        Simple constructor.
        
        Parameters:
            satelliteSystem (SatelliteSystem): satellite system
            progPCVS (String): Program name used for PCVs
            sourcePCVS (String): Source of corrections (URL)
        
        
        """
        ...
    def getProgPCVS(self) -> str:
        """
        Get the program name used to apply PCVs.
        
        Returns:
            Program name used to apply PCVs
        
        
        """
        ...
    def getSatelliteSystem(self) -> org.orekit.gnss.SatelliteSystem:
        """
        Get the satellite system.
        
        Returns:
            satellite system
        
        
        """
        ...
    def getSourcePCVS(self) -> str:
        """
        Get the source of corrections.
        
        Returns:
            Source of corrections (URL)
        
        
        """
        ...

class HatanakaCompressFilter(org.orekit.data.DataFilter):
    """
    Decompression filter for Hatanaka compressed RINEX files.
    
    Since:
        10.1
    
    Also see:
        `A Compression Format and Tools for GNSS Observation Data
        <http://cedadocs.ceda.ac.uk/1254/1/Hatanaka%5C_compressed%5C_format%5C_help.pdf>`
    """
    def __init__(self):
        """
        Empty constructor.
        
        This constructor is not strictly necessary, but it prevents spurious javadoc warnings with JDK 18 and later.
        
        Since:
            12.0
        
        
        """
        ...
    def filter(self, original: org.orekit.data.DataSource) -> org.orekit.data.DataSource:
        """
        Filter the data source.
        
        Filtering is often based on suffix. For example a gzip compressed file will have an original name of the form base.ext.gz when the corresponding uncompressed file will have a filtered name base.ext.
        
        A filter must never openStreamOnce the DataSource by itself, regardless of the fact it will return the original instance or a filtered instance. The rationale is that it is the upper layer that will decide to open (or not) the returned value and that a DataSource can be opened only once; this is the core principle of lazy-opening provided by DataSource.
        
        Beware that as the DataProvidersManager will attempt to pile all filters in a stack as long as their implementation of this method returns a value different from the original parameter. This implies that the filter, must perform some checks to see if it must be applied or not. If for example there is a need for a deciphering filter to be applied once to all data, then the filter should for example check for a suffix in the getName and create a new filtered DataSource instance only if the suffix is present, removing the suffix from the filtered instance. Failing to do so and simply creating a filtered instance with one deciphering layer without changing the name would result in an infinite stack of deciphering filters being built, until a stack overflow or memory exhaustion exception occurs.
        
        Specified by: filter in interface DataFilter
        
        Parameters:
            original (DataSource): original data source
        
        Returns:
            filtered data source, or original if this filter does not apply to this data source
        
        
        """
        ...

_RinexFile__T = typing.TypeVar('_RinexFile__T', bound=org.orekit.files.rinex.section.RinexBaseHeader)  # <T>
class RinexFile(typing.Generic[_RinexFile__T]):
    """
    Container for Rinex file.
    
    Since:
        12.0
    """
    def addComment(self, comment: org.orekit.files.rinex.section.RinexComment) -> None:
        """
        Add a comment.
        
        Parameters:
            comment (RinexComment): comment to add
        
        
        """
        ...
    def getComments(self) -> java.util.List[org.orekit.files.rinex.section.RinexComment]:
        """
        Get an unmodifiable view of the comments.
        
        Returns:
            unmodifiable view of the comments
        
        
        """
        ...
    def getHeader(self) -> _RinexFile__T:
        """
        Get the header.
        
        Returns:
            header
        
        
        """
        ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.rinex")``.

    AppliedDCBS: typing.Type[AppliedDCBS]
    AppliedPCVS: typing.Type[AppliedPCVS]
    HatanakaCompressFilter: typing.Type[HatanakaCompressFilter]
    RinexFile: typing.Type[RinexFile]
    clock: org.orekit.files.rinex.clock.__module_protocol__
    navigation: org.orekit.files.rinex.navigation.__module_protocol__
    observation: org.orekit.files.rinex.observation.__module_protocol__
    section: org.orekit.files.rinex.section.__module_protocol__
    utils: org.orekit.files.rinex.utils.__module_protocol__
