# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
import json

# Custom Library

# Custom Packages
from AthenaServerClient.data.rest import Commands

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class RESTRequest:
    rest_command:Commands
    orm:str
    body:dict

    def encode(self) -> bytes:
        return f"{self.rest_command.value} {self.orm} {json.dumps(self.body)}".encode("UTF_8")