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
from AthenaServer.models.athena_server_methods import _Method, MethodPing, MethodCommand
from AthenaServer.models.athena_server_command import AthenaServerCommand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True)
class AthenaServer:
    host:str|list[str]="LOCALHOST"
    port:int=None

    protocol_type:type[AthenaServerProtocol]=AthenaServerProtocol

    ssl_enabled:bool=False
    ssl_context:ssl.SSLContext=None

    # non init
    server:asyncio.AbstractServer = field(init=False, default=None, repr=False)
    loop:asyncio.AbstractEventLoop=field(default_factory=asyncio.new_event_loop)
    ping_callback:MethodPing = field(init=False, default=None, repr=False)
    protocol:AthenaServerProtocol = field(init=False, default=None)
    commands:dict[AthenaServerCommand:MethodCommand] = field(init=False, default_factory=dict)

    # ------------------------------------------------------------------------------------------------------------------
    # - store all defined method -
    # ------------------------------------------------------------------------------------------------------------------
    def __post_init__(self):
        # define the directory first, to not catch attr like "ping_callback" which will be set to a _Method
        directory = [
            attr_str for attr_str in self.__dir__()
            if isinstance(getattr(self, attr_str), _Method)
        ]
        for attr_str in directory:
            attr = getattr(self, attr_str)
            attr.owner = self # always set the owner to the server itself

            match attr:
                case MethodPing() if self.ping_callback is None:
                    self.ping_callback = attr

                case MethodPing() if self.ping_callback is not None: # only one ping command can exist
                    raise ValueError("No multiple Ping methods allowed")

                case MethodCommand() if attr.structure is not None:
                    if attr.structure in self.commands:
                        raise ValueError(f"The following command structure was already found in the commands:\n{attr.structure}")
                    self.commands[attr.structure] = attr

                case MethodCommand() if attr.structure is None:
                    raise ValueError(f"The following command has been defined without a valid structure:\n{attr}")

                case _:
                    pass


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
            protocol_factory=self.protocol_type.factory(
                data_handler=AthenaServerDataHandler(
                    commands=self.commands
                ),
                ping_callback=self.ping_callback
            ),
            host=self.host,
            port=self.port,
            ssl=self.ssl_context if self.ssl_enabled else None,
        )