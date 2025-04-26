
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.special.elliptic.carlson
import org.hipparchus.special.elliptic.jacobi
import org.hipparchus.special.elliptic.legendre
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.special.elliptic")``.

    carlson: org.hipparchus.special.elliptic.carlson.__module_protocol__
    jacobi: org.hipparchus.special.elliptic.jacobi.__module_protocol__
    legendre: org.hipparchus.special.elliptic.legendre.__module_protocol__
