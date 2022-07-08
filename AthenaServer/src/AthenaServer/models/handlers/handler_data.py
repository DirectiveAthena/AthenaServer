# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.responses.response import Response

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class HandlerData(ABC):

    @abstractmethod
    async def handle(self, data: bytearray) -> Response:...

