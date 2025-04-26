
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import org.orekit.gnss.metric.messages
import org.orekit.gnss.metric.ntrip
import org.orekit.gnss.metric.parser
import typing


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("org.orekit.gnss.metric")``.

    messages: org.orekit.gnss.metric.messages.__module_protocol__
    ntrip: org.orekit.gnss.metric.ntrip.__module_protocol__
    parser: org.orekit.gnss.metric.parser.__module_protocol__
