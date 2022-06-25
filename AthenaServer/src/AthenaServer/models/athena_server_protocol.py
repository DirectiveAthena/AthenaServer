# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from typing import Callable
from dataclasses import dataclass, field
import json

# Custom Library

# Custom Packages
from AthenaServer.models.handlers.handler_data import HandlerData
from AthenaServer.models.outputs.output import Output
from AthenaServer.models.responses.response import Response

from AthenaServer.data.responses import INTERNAL_ERROR_ENCODED

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class AthenaServerProtocol(asyncio.Protocol):
    output_types:list[type[Output]]
    handler_data:HandlerData

    # non init
    transport: asyncio.transports.Transport = field(init=False, repr=False)
    loop:asyncio.AbstractEventLoop=field(init=False, repr=False)
    outputs:list[Output] = field(init=False, repr=False, default_factory=list)

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
        Stores the 'asyncio.transports.Transport' as a attr of the class
        """
        self.transport = transport
        self.outputs = [o(transport=transport) for o in self.output_types]

    def data_received(self, data: bytearray) -> None:
        """
        Gets run when a client sends data to server
        """
        asyncio.create_task(self.task_data_received(data))

    async def task_data_received(self, data:bytearray):
        self.output_handler(await self.handler_data.handle(data))

    def connection_lost(self, exc: Exception | None) -> None:
        """
        Gets run when a client looses connection to the server
        """
        print(exc)

    # ------------------------------------------------------------------------------------------------------------------
    # - Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def output_handler(self,response:Response):
        try:
            self.transport.write(response.encode())
        except json.JSONDecodeError or UnicodeEncodeError:
            self.transport.write(INTERNAL_ERROR_ENCODED)

