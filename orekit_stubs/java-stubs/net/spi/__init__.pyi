
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.net
import typing



class URLStreamHandlerProvider(java.net.URLStreamHandlerFactory): ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.net.spi")``.

    URLStreamHandlerProvider: typing.Type[URLStreamHandlerProvider]
