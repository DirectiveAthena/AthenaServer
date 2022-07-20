# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
import json

# Custom Library

# Custom Packages
from AthenaServer.models.page import Page
from AthenaServer.models.context import Context
from AthenaServer.functions.pages import get_page
from AthenaServer.data.commands import COMMANDS

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(eq=False, order=False, match_args=False, slots=True, kw_only=True)
class DataHandler:
    root_page:Page

    async def handle(self, data:bytearray) -> Context:
        # TODO replace with something better !
        cmd, location, json_kwargs = data.decode("utf8").split(" ",2)

        # test the base cmd
        if cmd not in COMMANDS:
            pass

        # test for the location
        page = get_page(
            root_page=self.root_page,
            page_location=location
        )

        # actually execute te command
        try:
            kwargs = json.loads(json_kwargs)
        except json.JSONDecodeError:
            return Context.as_error(error_code=-1)
        result = await getattr(page, cmd)(Context(), **kwargs)

        # return a completed package
        return f"{result}\r\n".encode("utf_8")
