# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaServer.models.outputs.output import Output
from AthenaServer.models.responses.response import Response


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class OutputConsole(Output):
    async def send(self, response:Response):
        print(response)

    async def on_receive(self, data: bytearray):
        print(data)

    async def send_ping(self):
        print("Ping has been sent")