# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library
from AthenaServer.models.page import Page

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class PageTest(Page):
    name:str="test"

    async def GET(self, *args, **kwargs):
        return "this was a successful test"

