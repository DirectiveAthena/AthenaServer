# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
import json

# Custom Library

# Custom Packages
from AthenaServer.models.responses.response import Response
from AthenaServer.data.return_codes import RETURN_CODES_UNION
from AthenaServer.data.general import UTF_8, CODE, BODY

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, match_args=True)
class Response_AthenaServer(Response):
    code: RETURN_CODES_UNION
    body: dict

    def to_dict(self):
        return {
            CODE: self.code.value,
            BODY: self.body
        }

    def encode(self) -> bytes:
        return f"{json.dumps(self.to_dict())}\r\n".encode(UTF_8)