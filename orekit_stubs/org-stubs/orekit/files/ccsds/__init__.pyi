
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.files.ccsds.definitions
import org.orekit.files.ccsds.ndm
import org.orekit.files.ccsds.section
import org.orekit.files.ccsds.utils
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files.ccsds")``.

    definitions: org.orekit.files.ccsds.definitions.__module_protocol__
    ndm: org.orekit.files.ccsds.ndm.__module_protocol__
    section: org.orekit.files.ccsds.section.__module_protocol__
    utils: org.orekit.files.ccsds.utils.__module_protocol__
