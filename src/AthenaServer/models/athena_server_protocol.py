# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from typing import Callable
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_data_handler import AthenaServerDataHandler

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class AthenaServerProtocol(asyncio.Protocol):
    data_handler_factory:Callable[[], AthenaServerDataHandler]=None

    # non init
    transport: asyncio.transports.Transport = field(init=False, default=None)
    loop:asyncio.AbstractEventLoop=field(init=False)
    data_handler:AthenaServerDataHandler=field(init=False)
    kwargs:dict=field(init=False)

    def __post_init__(self):
        self.loop = asyncio.new_event_loop()

    # ------------------------------------------------------------------------------------------------------------------
    # - factory, needed for asyncio.AbstractEventLoop.create_connection protocol_factory kwarg used in Launcher -
    # ------------------------------------------------------------------------------------------------------------------
    @classmethod
    def factory(cls, **kwargs) -> Callable[[], AthenaServerProtocol]:
        """
        Factory is used by 'asyncio.AbstractEventLoop.create_connection' to return a callable object.
        This way extra kwargs can be passed to the protocol without the need for a lambda
        """
        def factory_wrapper():
            # noinspection PyArgumentList
            return cls(**kwargs)

        return factory_wrapper

    # ------------------------------------------------------------------------------------------------------------------
    # - asyncio.Protocol methods -
    # ------------------------------------------------------------------------------------------------------------------
    def connection_made(self, transport: asyncio.transports.Transport) -> None:
        """
        Gets run when a client connects to the server
        """
        self.data_handler = self.data_handler_factory()
        self.transport = transport

    def data_received(self, data: bytearray) -> None:
        """
        Gets run when a client sends data to server
        """

        self.transport.write(
            self.data_handler.handle(data)
        )

    def connection_lost(self, exc: Exception | None) -> None:
        """
        Gets run when a client looses connection to the server
        """
        print(exc)

    def eof_received(self) -> bool | None:
        pass