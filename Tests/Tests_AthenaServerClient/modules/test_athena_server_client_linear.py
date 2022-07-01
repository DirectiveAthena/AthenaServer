# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import json
import unittest
import tracemalloc

# Custom Library

# Custom Packages
from AthenaServerClient.models.linear.athena_server_client import AthenaServerClient_Linear

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test_AthenaServerClient_Linear(unittest.TestCase):
    def test_general(self):
        async def main():
            tracemalloc.start()
            client = AthenaServerClient_Linear(
                host="localhost",
                port=41768
            )
            reader, writer = await client.connect() #type: asyncio.StreamReader, asyncio.StreamWriter
            writer.write(
                """GET root/data {"test":"something"}""".encode("utf_8")
            )

            result = await reader.readline()

            self.assertEqual(
                b'{"code": 200, "body": {"response": "here is some data according to : something "}}\r\n',
                result
            )

            # test ping
            result = await reader.readline()
            response = {
                "response": json.loads(result)["body"]["AthenaServer"]
            }
            response_str =f'POST root/ping {json.dumps(response)}'
            writer.write(
                response_str.encode("utf_8")
            )

            result = await reader.readline()
            self.assertEqual(
                b'{"code": 200, "body": {}}\r\n',
                result
            )

            await client.close()


        asyncio.run(main())