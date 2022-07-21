# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import socket
import os

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

async def launch_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server = AthenaServer(
        host=HOST,
        port=PORT,
        root_page=test_server_constructor(),
        socket=s,
        # database connection stuff
        db_host="localhost",
        db_port=3306,
        db_user=os.getenv("DB_USER"),
        db_pass=os.getenv("DB_PASS"),
    )
    await server.start()


async def connect_to_server() -> tuple[asyncio.StreamReader, asyncio.StreamWriter]:
    loop = asyncio.events.get_running_loop()
    reader = asyncio.StreamReader(limit=2 ** 16 , loop=loop)
    protocol = asyncio.StreamReaderProtocol(reader, loop=loop)
    transport, _ = await loop.create_connection(lambda: protocol, HOST, PORT)
    writer = asyncio.StreamWriter(transport, protocol, reader, loop)
    return reader, writer

    # return await asyncio.open_connection(
    #     host=HOST,
    #     port=PORT,
    #     loop=asyncio.get_running_loop()
    # )

if __name__ == '__main__':
    asyncio.run(launch_server())