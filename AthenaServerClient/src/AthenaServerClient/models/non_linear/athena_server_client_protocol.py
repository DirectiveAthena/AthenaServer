# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from dataclasses import dataclass, field
from typing import Callable

# Custom Library

# Custom Packages
from AthenaServerClient.models.non_linear.handlers.handler_data import HandlerData
from AthenaServerClient.models.non_linear.handlers.handler_data_client import HandlerData_Client
from AthenaServerClient.models.REST_request import RESTRequest

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, eq=False, order=False, match_args=False, kw_only=True)
class AthenaServerClientProtocol(asyncio.Protocol):
    handler_data:HandlerData=field(default_factory=lambda: HandlerData_Client(root_name="root"))

    # non init stuff
    transport: asyncio.transports.Transport = field(init=False, default=None)
    buffer:bytearray|None=field(init=False, default=None)

    @classmethod
    def factory(cls, **kwargs) -> Callable[[], AthenaServerClientProtocol]:
        def factory_wrapper():
            # noinspection PyArgumentList
            return cls(**kwargs)
        return factory_wrapper

    def connection_made(self, transport: asyncio.transports.Transport) -> None:
        self.transport = transport

    def data_received(self, data: bytearray) -> None:
        self.buffer = data
        asyncio.create_task(self.task_data_received(data))

    async def task_data_received(self, data:bytearray):
        for output in self.outputs:
            await output.on_receive(data)

        # only generate one response, and output it accordingly
        response: RESTRequest|None = await self.handler_data.handle(data)
        if isinstance(response, RESTRequest):
            for output in self.outputs:
                await output.send(response)

    def connection_lost(self, exc: Exception | None) -> None:
        if exc is not None:
            raise exc

    async def read_buffer(self):
        # todo fix this ugly code
        while True:
            if self.buffer is not None:
                break
            await asyncio.sleep(0)
        buffer = self.buffer
        self.buffer = None
        return buffer
