# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
import asyncio

# Custom Library

# Custom Packages
from AthenaServerClient.models.athena_server_client import AthenaServerClient
from AthenaServerClient.models.non_linear.athena_server_client_protocol import AthenaServerClientProtocol

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerClient_NonLinear(AthenaServerClient):
    #non init
    loop:asyncio.AbstractEventLoop=field(init=False)

    async def connect(self) -> AthenaServerClientProtocol:
        self.loop = asyncio.get_running_loop()
        _, protocol = await self.create_connection()
        return protocol

    async def create_connection(self):
        return await self.loop.create_connection(
            protocol_factory=AthenaServerClientProtocol.factory(),
            host=self.host,
            port=self.port,
        )

    def close(self):
        self.loop.close()