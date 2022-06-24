# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages import AthenaServerStructure, AthenaServerPage

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerDataHandler:
    pages_structure: AthenaServerStructure

    # ------------------------------------------------------------------------------------------------------------------
    # - factory, needed for asyncio.AbstractEventLoop.create_connection protocol_factory kwarg used in Launcher -
    # ------------------------------------------------------------------------------------------------------------------
    async def handle(self, data: bytearray) -> dict:
        match data.decode("utf_8").split(" ", 2):
            case "GET", str(pages), str(json_args):
                try:
                    page:AthenaServerPage = self.find_page(pages)
                except KeyError:
                    print("NOT FOUND", data)
                    return {}
                try:
                    json_dict = json.loads(json_args)
                except json.JSONDecodeError:
                    print("wrong format")
                    return {}
                try:
                    result = await page.GET(**json_dict)
                    print(result)
                except TypeError:
                    print("wrong arguments")
                    return {}


            case "PUT", str(pages), str(json_args):
                print(data,"PUT")

            case "PATCH", str(pages), str(json_args):
                print(data,"PATCH")

            case "POST", str(pages), str(json_args):
                print(data,"POST")

            case "DELETE", str(pages), str(json_args):
                print(data,"DELETE")

            case _:
                print(data, "UNDEFINED")

        return {}

    def find_page(self, pages:str) -> AthenaServerPage:
        return self.pages_structure[tuple(pages.split("/"))]

