# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod

# Custom Library

# Custom Packages
from AthenaServer.models.responses.response import Response

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Output(ABC):
    def __init__(self, **kwargs):
        pass

    @abstractmethod
    async def send(self, response:Response):...
    @abstractmethod
    async def on_receive(self, data:bytearray):...
    @abstractmethod
    async def send_ping(self):...
