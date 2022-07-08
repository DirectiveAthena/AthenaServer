# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import json
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.functions.pages import page_constructor
from AthenaServer.models.page import Page

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(unsafe_hash=True)
class PageDifferent(Page):
    name:str="different"

    async def GET(self, *args, **kwargs):
        """this gets something"""
        print("here")

async def main():
    construction = {
        Page(name="something"): {
            PageDifferent(): {},
            Page(name="else"): {}
        },
        Page(name="else"): {}
    }

    root_page = page_constructor(
        root_page=Page(name="root"),
        page_construction=construction
    )

    await root_page.get_page("something/different".split("/")).GET()

if __name__ == '__main__':
    asyncio.run(main())