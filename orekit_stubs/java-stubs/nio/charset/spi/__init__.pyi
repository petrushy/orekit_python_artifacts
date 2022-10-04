import java.nio.charset
import java.util
import typing



class CharsetProvider:
    def charsetForName(self, string: str) -> java.nio.charset.Charset: ...
    def charsets(self) -> java.util.Iterator[java.nio.charset.Charset]: ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.nio.charset.spi")``.

    CharsetProvider: typing.Type[CharsetProvider]
