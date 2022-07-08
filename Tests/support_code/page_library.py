# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
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

@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class PageTestBasic(Page):
    name:str="basic"

    async def GET(self, *args, **kwargs):
        return json.dumps({"result": "this should work"})
