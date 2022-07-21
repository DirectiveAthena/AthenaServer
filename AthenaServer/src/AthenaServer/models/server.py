# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
from dataclasses import dataclass, field
import tracemalloc
import socket

# Custom Library
from AthenaLib.fixes.asyncio import fix_nested_asyncio

# Custom Packages
from AthenaServer.models.server_protocol import AthenaServerProtocol
from AthenaServer.models.page import Page
from AthenaServer.models.databases.database_mariadb import DatabaseMariaDB
from AthenaServer.functions.var_handlers.data_handler import set_data_handler
from AthenaServer.functions.var_handlers.database import set_database, get_database

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True)
class AthenaServer:
    host:str
    port:int
    root_page:Page
    socket:socket.socket=None

    db_host:str=None
    db_port:int=None
    db_user:str=None
    db_pass:str=None

    # non init
    server:asyncio.AbstractServer = field(init=False, default=None, repr=False)
    loop:asyncio.AbstractEventLoop=field(default_factory= asyncio.get_running_loop)
    protocol:AthenaServerProtocol = field(init=False, default=None)

    # ------------------------------------------------------------------------------------------------------------------
    # - Server starting and such -
    # ------------------------------------------------------------------------------------------------------------------
    async def start(self):
        tracemalloc.start()

        # apply some fixes
        fix_nested_asyncio()

        # define some objects that the protocol will rely on
        set_data_handler(root_page=self.root_page)
        set_database(database_type=DatabaseMariaDB)
        await get_database().connect(
            host = self.db_host,
            port = self.db_port,
            username = self.db_user,
            password = self.db_pass,
        )

        # launch the actual server
        self.server = self.loop.run_until_complete(
            self.create_server()
        )
        self.loop.run_forever()
        self.loop.close()

    async def create_server(self) -> asyncio.base_events.Server:
        return await self.loop.create_server(
            protocol_factory=AthenaServerProtocol.factory(),
            host=self.host if self.socket is None else None,
            port=self.port if self.socket is None else None,
            sock=self.socket
        )

