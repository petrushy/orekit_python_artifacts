
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus
import org.orekit
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org")``.

    hipparchus: org.hipparchus.__module_protocol__
    orekit: org.orekit.__module_protocol__
