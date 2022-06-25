# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio

# Custom Library

# Custom Packages
from AthenaServer.models.outputs.output_client import OutputClient

from AthenaServer.data.output_texts import JSON_NOT_FOUND, WRONG_FORMAT

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class OutputClient_Server(OutputClient):
    transport: asyncio.Transport

    def json_not_found(self):
        self.transport.write(JSON_NOT_FOUND)

    def wrong_format(self):
        self.transport.write(WRONG_FORMAT)