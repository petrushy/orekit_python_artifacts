
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.control.heuristics
import org.orekit.control.indirect
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control")``.

    heuristics: org.orekit.control.heuristics.__module_protocol__
    indirect: org.orekit.control.indirect.__module_protocol__
