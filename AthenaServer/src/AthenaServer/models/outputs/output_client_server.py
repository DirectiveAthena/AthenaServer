# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json

# Custom Library

# Custom Packages
from AthenaServer.models.outputs.output_client import OutputClient
from AthenaServer.models.responses.response import Response
from AthenaServer.models.responses.response_server import Response_AthenaServer

from AthenaServer.data.responses import INTERNAL_ERROR_ENCODED, PING_ENCODED
from AthenaServer.data.return_codes import *

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class OutputClient_Server(OutputClient):

    async def send(self, response:Response):
        try:
            self.transport.write(response.encode())
        except json.JSONDecodeError or UnicodeEncodeError:
            self.transport.write(INTERNAL_ERROR_ENCODED)

    async def on_receive(self, data: bytearray):
        pass

    async def send_ping(self):
        self.transport.write(
            PING_ENCODED
        )
