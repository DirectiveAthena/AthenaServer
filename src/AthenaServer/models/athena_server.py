# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
import ssl
import tracemalloc
# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_protocol import AthenaServerProtocol
from AthenaServer.models.athena_server_data_handler import AthenaServerDataHandler

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True)
class AthenaServer:
    host:str|list[str]="LOCALHOST"
    port:int=None

    protocol:AthenaServerProtocol=field(default_factory=AthenaServerProtocol)

    ssl_enabled:bool=False
    ssl_context:ssl.SSLContext=None

    # non init
    server:asyncio.AbstractServer = field(init=False)
    loop:asyncio.AbstractEventLoop=field(default_factory=asyncio.new_event_loop)

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

    async def create_server(self) -> asyncio.AbstractServer:
        return await self.loop.create_server(
            protocol_factory=self.protocol.factory(
                data_handler_factory=AthenaServerDataHandler.factory()
            ),
            host=self.host,
            port=self.port,
            ssl=self.ssl_context if self.ssl_enabled else None,
        )