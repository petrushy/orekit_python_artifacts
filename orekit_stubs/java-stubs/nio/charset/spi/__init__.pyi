
import sys
if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

import java.nio.charset
import java.util
import typing



class CharsetProvider:
    def charsetForName(self, string: str) -> java.nio.charset.Charset: ...
    def charsets(self) -> java.util.Iterator[java.nio.charset.Charset]: ...


class __module_protocol__(Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.charset.spi")``.

    CharsetProvider: typing.Type[CharsetProvider]
