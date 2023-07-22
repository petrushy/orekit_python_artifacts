import java.net
import typing



class URLStreamHandlerProvider(java.net.URLStreamHandlerFactory): ...


class __module_protocol__(typing.Protocol):
    # A module protocol which reflects the result of ``jp.JPackage("java.net.spi")``.

    URLStreamHandlerProvider: typing.Type[URLStreamHandlerProvider]
