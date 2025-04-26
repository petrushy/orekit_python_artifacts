
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.estimation.iod
import org.orekit.estimation.leastsquares
import org.orekit.estimation.measurements
import org.orekit.estimation.sequential
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.estimation")``.

    iod: org.orekit.estimation.iod.__module_protocol__
    leastsquares: org.orekit.estimation.leastsquares.__module_protocol__
    measurements: org.orekit.estimation.measurements.__module_protocol__
    sequential: org.orekit.estimation.sequential.__module_protocol__
