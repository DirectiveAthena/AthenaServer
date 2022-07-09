# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.page import Page
from AthenaServer.functions.pages import get_page

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class DataHandler:
    root_page:Page

    async def handle(self, data:bytearray) -> bytes:
        # TODO replace with something better?
        cmd, location, args = data.decode("utf8").split(" ")
        page = get_page(
            root_page=self.root_page,
            page_location=location
        )
        return f"{await getattr(page, cmd)()}\r\n".encode("utf_8")
