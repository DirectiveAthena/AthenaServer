# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServerClient.models.REST_request import RESTRequest

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class HandlerData(ABC):
    root_name:str

    @abstractmethod
    async def handle(self, data: bytearray) -> RESTRequest:...

