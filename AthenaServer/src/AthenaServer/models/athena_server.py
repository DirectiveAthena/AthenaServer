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
from AthenaServer.models.handlers.handler_data import HandlerData
from AthenaServer.models.handlers.handler_data_server import HandlerData_AthenaServer
from AthenaServer.models.athena_server_pages import AthenaServerStructure
from AthenaServer.models.outputs.output import Output
from AthenaServer.models.outputs.output_console import OutputConsole
from AthenaServer.models.outputs.output_client_server import OutputClient_Server

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True)
class AthenaServer:
    host:str
    port:int

    output_types:list[type[Output]]=field(default_factory=lambda : [OutputClient_Server])
    output_console_enabled:bool=True

    ssl_enabled:bool=False
    ssl_context:ssl.SSLContext=None

    pages_structure: AthenaServerStructure=field(default_factory=dict)

    # non init
    server:asyncio.AbstractServer = field(init=False, default=None, repr=False)
    loop:asyncio.AbstractEventLoop=field(default_factory=asyncio.new_event_loop)
    protocol:AthenaServerProtocol = field(init=False, default=None)

    # ------------------------------------------------------------------------------------------------------------------
    # - store all defined method -
    # ------------------------------------------------------------------------------------------------------------------
    def __post_init__(self):
        if OutputClient_Server not in self.output_types:
            self.output_types.insert(0, OutputClient_Server)

        if self.output_console_enabled and OutputConsole not in self.output_types:
            self.output_types.append(OutputConsole)

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
            protocol_factory=AthenaServerProtocol.factory(
                handler_data=self.data_handler(),
                output_types=self.output_types
            ),
            host=self.host,
            port=self.port,
            ssl=self.ssl_context if self.ssl_enabled else None,
        )

    def data_handler(self) -> HandlerData:
        """Constructor for the correct data handler for the server in question"""
        return HandlerData_AthenaServer(
            pages_structure=self.pages_structure,
        )