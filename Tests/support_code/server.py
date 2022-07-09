# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import socket
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
PORT = 41736

def launch_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server = AthenaServer(
        host=HOST,
        port=PORT,
        root_page=test_server_constructor(),
        socket=s
    )
    server.start()

async def _launch_server():
    tracemalloc.start()

async def connect_to_server() -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    return await asyncio.open_connection(host=HOST, port=PORT)

if __name__ == '__main__':
    launch_server()