# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC
import asyncio

# Custom Library

# Custom Packages
from AthenaServer.models.outputs.output import Output

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class OutputClient(Output, ABC):
    transport: asyncio.Transport
    def __init__(self, transport:asyncio.Transport, **_):
        self.transport = transport