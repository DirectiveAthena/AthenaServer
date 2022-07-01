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
from AthenaServerClient.models.non_linear.handlers.handler_data_client import HandlerData_Client

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerClient_NonLinear(AthenaServerClient):
    #non init
    loop:asyncio.AbstractEventLoop=field(init=False)
    protocol:AthenaServerClientProtocol=field(init=False)

    async def connect(self) -> AthenaServerClientProtocol:
        self.loop = asyncio.get_running_loop()
        _, self.protocol = await self.create_connection()
        return self.protocol

    async def create_connection(self):
        return await self.loop.create_connection(
            protocol_factory=AthenaServerClientProtocol.factory(
                handler_data=HandlerData_Client(root_name="root"),
            ),
            host=self.host,
            port=self.port,
        )

    async def close(self):
        self.protocol.transport.close()