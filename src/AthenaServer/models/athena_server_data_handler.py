# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_page import AthenaServerPage
from AthenaServer.functions.data_handler_support import check_pages_args, trim_root_page_name

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerDataHandler:
    pages:dict[tuple:AthenaServerPage]

    # ------------------------------------------------------------------------------------------------------------------
    # - factory, needed for asyncio.AbstractEventLoop.create_connection protocol_factory kwarg used in Launcher -
    # ------------------------------------------------------------------------------------------------------------------
    def handle(self, data: bytearray) -> dict:
        match data.decode("utf_8").split(" ", 2):
            case "GET", str(pages), str(args):
                print(data, "GET")

            case "PUT", str(pages), str(args):
                print(data,"PUT")

            case "POST", str(pages), str(args):
                print(data,"POST")

            case "DELETE", str(pages), str(args):
                print(data,"DELETE")

            case _:
                print(data, "UNDEFINED")

        return {}

