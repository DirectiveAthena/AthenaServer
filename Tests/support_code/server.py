# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import tracemalloc

# Custom Library
from AthenaServer.models.server import AthenaServer

# Custom Packages
from Tests.support_code.constuction import test_server_constructor

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyTypeChecker
HOST = "localhost"
PORT = 41735

def launch_server():
    server = AthenaServer(
        host=HOST,
        port=41735,
        root_page=test_server_constructor()
    )
    server.start()

async def _launch_server():
    tracemalloc.start()

async def connect_to_server() -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    return await asyncio.open_connection(host=HOST, port=PORT)

if __name__ == '__main__':
    launch_server()