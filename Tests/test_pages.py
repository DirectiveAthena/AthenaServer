# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import functools
import json

# Custom Library

# Custom Packages
from AthenaServer.models.page import Page

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
async def get_something(text, *, defined:str):
    print(text, defined)

async def main():
    root_page = Page(name="root").add_pages(
        Page(name="something").add_pages(
            Page(name="different",
                 GET=functools.partial(get_something, defined="test")
                 ),
            Page(name="else"),
        ),
        Page(name="else")
    )

    with open("dump.json", "w") as file:
        file.write(json.dumps(root_page.get_page_structure(), indent=4))

if __name__ == '__main__':
    asyncio.run(main())
    # main()