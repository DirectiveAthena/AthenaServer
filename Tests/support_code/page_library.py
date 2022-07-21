# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json
from dataclasses import dataclass

# Custom Library
from AthenaServer.models.page import Page
from AthenaServer.models.context import Context
from AthenaServer.functions.var_handlers.database import get_database

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class PageTest(Page):
    name:str="test"

    async def GET(self, context:Context, **kwargs):
        return "this was a successful test"

@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class PageTestBasic(Page):
    name:str="basic"

    async def GET(self, context:Context, **kwargs):
        return json.dumps({"result": "this should work"})

@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class PageTestDatabase(Page):
    name: str = "database"

    async def GET(self, context: Context, **kwargs):

        cursor = await get_database().get_cursor()
        await cursor.execute("SHOW AUTHORS")

        return json.dumps({"result":await cursor.fetchall()})