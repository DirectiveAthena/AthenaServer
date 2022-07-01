# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.handlers.handler_data import HandlerData
from AthenaServer.models.athena_server_pages import AthenaServerStructure
from AthenaServer.models.responses.response_server import Response_AthenaServer

from AthenaServer.data.responses import NOT_FOUND, BAD_REQUEST, NOT_ACCEPTABLE, INTERNAL_ERROR
from AthenaServer.data.rest import COMMANDS as REST_COMMANDS
from AthenaServer.data.general import CURLY_BRACKET_OPEN, CURLY_BRACKET_CLOSE, UTF_8, SPACE, FORWARD_SLASH

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class HandlerData_AthenaServer(HandlerData):
    pages_structure: AthenaServerStructure

    async def handle(self, data: bytearray) -> Response_AthenaServer:
        match data.decode(UTF_8).split(SPACE, 2):
            case str(rest_cmd), str(pages), str(json_args) if (
                    rest_cmd in REST_COMMANDS
                    and self.pages_structure.root_page.name in pages
                    and json_args[0] == CURLY_BRACKET_OPEN
                    and json_args[-1] == CURLY_BRACKET_CLOSE
                    and (pages_key := tuple(pages.split(FORWARD_SLASH))) in self.pages_structure.structure.keys()
            ):
                try:
                    return await (getattr(self.pages_structure[pages_key], rest_cmd)(**json.loads(json_args)))

                except json.JSONDecodeError or PermissionError:
                    return BAD_REQUEST

                except TypeError:
                    return NOT_ACCEPTABLE

                except AttributeError:
                    return INTERNAL_ERROR


            case _:
                return NOT_FOUND




