# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
import json

# Custom Library

# Custom Packages
from Tests.support_code.server import connect_to_server

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestServer(unittest.IsolatedAsyncioTestCase):
    async def test_Connect(self):
        reader, writer = await connect_to_server()
        writer.write(b"GET server_test/test/database {}")
        # writer.write(b"_ GET server_test/test/basic {}")
        # writer.write(b"GET server_test/user/directiveathena {}")
        # writer.write(b"GET server_test/user/api_key {'levels':1}")
        print(json.loads(await reader.readline()))
        writer.close()
