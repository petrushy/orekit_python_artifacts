
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.files.ccsds
import org.orekit.files.general
import org.orekit.files.iirv
import org.orekit.files.ilrs
import org.orekit.files.rinex
import org.orekit.files.sinex
import org.orekit.files.sp3
import org.orekit.files.stk
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.files")``.

    ccsds: org.orekit.files.ccsds.__module_protocol__
    general: org.orekit.files.general.__module_protocol__
    iirv: org.orekit.files.iirv.__module_protocol__
    ilrs: org.orekit.files.ilrs.__module_protocol__
    rinex: org.orekit.files.rinex.__module_protocol__
    sinex: org.orekit.files.sinex.__module_protocol__
    sp3: org.orekit.files.sp3.__module_protocol__
    stk: org.orekit.files.stk.__module_protocol__
