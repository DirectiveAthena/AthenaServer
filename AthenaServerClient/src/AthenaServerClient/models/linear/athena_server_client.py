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

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerClient_Linear(AthenaServerClient):
    reader:asyncio.StreamReader=field(init=False)
    writer:asyncio.StreamWriter=field(init=False)
    async def connect(self) -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
        self.reader, self.writer =await asyncio.open_connection(
            host=self.host,
            port=self.port,
        )
        return self.reader, self.writer

    async def close(self):
        self.writer.close()
