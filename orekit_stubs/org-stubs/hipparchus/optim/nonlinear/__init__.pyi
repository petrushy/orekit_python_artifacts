
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.hipparchus.optim.nonlinear.scalar
import org.hipparchus.optim.nonlinear.vector
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.hipparchus.optim.nonlinear")``.

    scalar: org.hipparchus.optim.nonlinear.scalar.__module_protocol__
    vector: org.hipparchus.optim.nonlinear.vector.__module_protocol__
