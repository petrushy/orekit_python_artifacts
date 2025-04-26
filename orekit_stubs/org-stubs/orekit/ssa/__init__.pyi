
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.ssa.collision
import org.orekit.ssa.metrics
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.ssa")``.

    collision: org.orekit.ssa.collision.__module_protocol__
    metrics: org.orekit.ssa.metrics.__module_protocol__
