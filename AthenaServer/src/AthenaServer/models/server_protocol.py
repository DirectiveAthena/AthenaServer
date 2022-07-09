# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from typing import Callable
from dataclasses import dataclass, field, InitVar

# Custom Library

# Custom Packages
from AthenaServer.models.page import Page
from AthenaServer.models.data_handler import DataHandler

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class AthenaServerProtocol(asyncio.Protocol):
    root_page:InitVar[Page]
    handler:type[DataHandler]=DataHandler

    # non init
    closed:bool=field(init=False, default=False)
    transport: asyncio.transports.Transport = field(init=False, repr=False)
    loop:asyncio.AbstractEventLoop=field(init=False, repr=False)
    data_handler:DataHandler=field(init=False,repr=False)

    def __post_init__(self, root_page: Page):
        self.loop = asyncio.new_event_loop()
        self.data_handler=DataHandler(
            root_page=root_page
        )


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
        Stores the 'asyncio.transports.Transport' as a attr of the class
        """
        self.transport = transport

    def data_received(self, data: bytearray) -> None:
        """
        Gets run when a client sends data to server
        This immediately gets handed of to an async coroutine
        """
        asyncio.ensure_future(self._data_received(data))

    async def _data_received(self, data: bytearray) -> None:
        output = await self.data_handler.handle(data)
        self.transport.write(output)

    def connection_lost(self, exc: Exception | None) -> None:
        """
        Gets run when a client looses connection to the server
        """
        if exc is not None:
            print(exc)
        self.transport.close()
        self.closed = True