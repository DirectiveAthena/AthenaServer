# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import unittest
import tracemalloc

# Custom Library

# Custom Packages
from AthenaServerClient.models.non_linear.athena_server_client import AthenaServerClient_NonLinear
from AthenaServerClient.models.non_linear.athena_server_client_protocol import AthenaServerClientProtocol

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test_AthenaServerClient_NonLinear(unittest.TestCase):
    def test_general(self):
        async def main():
            tracemalloc.start()
            client = AthenaServerClient_NonLinear(
                host="localhost",
                port=41768
            )
            protocol:AthenaServerClientProtocol = await client.connect()
            protocol.transport.write(
                """GET root/data {"test":"something"}""".encode("utf_8")
            )

            self.assertEqual(
                bytearray(b'{"code": 200, "body": {"response": "here is some data according to : something "}}\r\n'),
                await protocol.read_buffer()
            )

            await asyncio.sleep(60)
            await protocol.read_buffer()

            await asyncio.sleep(10)

            await client.close()

        asyncio.run(main())