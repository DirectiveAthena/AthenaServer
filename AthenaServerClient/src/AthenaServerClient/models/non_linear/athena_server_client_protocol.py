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

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, eq=False, order=False, match_args=False, kw_only=True)
class AthenaServerClientProtocol(asyncio.Protocol):
    transport: asyncio.transports.Transport = field(init=False, default=None)
    buffer:bytearray|None=None

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
