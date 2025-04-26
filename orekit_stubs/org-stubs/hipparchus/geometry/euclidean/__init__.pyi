
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.geometry.euclidean.oned
import org.hipparchus.geometry.euclidean.threed
import org.hipparchus.geometry.euclidean.twod
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.geometry.euclidean")``.

    oned: org.hipparchus.geometry.euclidean.oned.__module_protocol__
    threed: org.hipparchus.geometry.euclidean.threed.__module_protocol__
    twod: org.hipparchus.geometry.euclidean.twod.__module_protocol__
