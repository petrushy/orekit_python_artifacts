
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.geometry.spherical.oned
import org.hipparchus.geometry.spherical.twod
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.spherical")``.

    oned: org.hipparchus.geometry.spherical.oned.__module_protocol__
    twod: org.hipparchus.geometry.spherical.twod.__module_protocol__
