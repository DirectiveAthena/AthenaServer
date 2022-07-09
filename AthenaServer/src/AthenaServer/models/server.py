# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from dataclasses import dataclass, field
import ssl
import tracemalloc
import socket
from typing import Iterable

# Custom Library

# Custom Packages
from AthenaServer.models.server_protocol import AthenaServerProtocol
from AthenaServer.models.page import Page

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True)
class AthenaServer:
    host:str
    port:int
    root_page:Page
    socket:socket.socket=None

    # non init
    server:asyncio.AbstractServer = field(init=False, default=None, repr=False)
    loop:asyncio.AbstractEventLoop=field(default_factory=asyncio.new_event_loop)
    protocol:AthenaServerProtocol = field(init=False, default=None)

    # ------------------------------------------------------------------------------------------------------------------
    # - Server starting and such -
    # ------------------------------------------------------------------------------------------------------------------
    def start(self):
        tracemalloc.start()
        self.server = self.loop.run_until_complete(
            self.create_server()
        )
        self.loop.run_forever()
        self.loop.close()

    async def create_server(self) -> asyncio.base_events.Server:
        return await self.loop.create_server(
            protocol_factory=AthenaServerProtocol.factory(
                root_page=self.root_page
            ),
            host=self.host if self.socket is None else None,
            port=self.port if self.socket is None else None,
            sock=self.socket
        )
