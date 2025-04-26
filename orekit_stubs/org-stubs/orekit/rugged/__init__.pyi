
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.rugged.adjustment
import org.orekit.rugged.api
import org.orekit.rugged.errors
import org.orekit.rugged.intersection
import org.orekit.rugged.linesensor
import org.orekit.rugged.los
import org.orekit.rugged.raster
import org.orekit.rugged.refraction
import org.orekit.rugged.utils
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.rugged")``.

    adjustment: org.orekit.rugged.adjustment.__module_protocol__
    api: org.orekit.rugged.api.__module_protocol__
    errors: org.orekit.rugged.errors.__module_protocol__
    intersection: org.orekit.rugged.intersection.__module_protocol__
    linesensor: org.orekit.rugged.linesensor.__module_protocol__
    los: org.orekit.rugged.los.__module_protocol__
    raster: org.orekit.rugged.raster.__module_protocol__
    refraction: org.orekit.rugged.refraction.__module_protocol__
    utils: org.orekit.rugged.utils.__module_protocol__
