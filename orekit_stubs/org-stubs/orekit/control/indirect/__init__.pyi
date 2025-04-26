
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.control.indirect.adjoint
import org.orekit.control.indirect.shooting
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.control.indirect")``.

    adjoint: org.orekit.control.indirect.adjoint.__module_protocol__
    shooting: org.orekit.control.indirect.shooting.__module_protocol__
