# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import functools
import json
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.page import Page

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def get_something(text, *, defined:str):
    print(text, defined)

@dataclass()
class PageDifferent(Page):
    name:str="different"

    def GET(self, *args, **kwargs):
        """this gets something"""
        print("here")

async def main():
    root_page = Page(name="root").add_pages(
        Page(name="something").add_pages(
            PageDifferent(),
            Page(name="else"),
        ),
        Page(name="else")
    )

    with open("dump.json", "w") as file:
        file.write(json.dumps(root_page.get_page_structure_and_commands(single=True), indent=4))

if __name__ == '__main__':
    asyncio.run(main())
    # main()