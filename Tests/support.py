# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages import AthenaServerStructure, AthenaServerPage

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class PageData(AthenaServerPage):
    name:str = "data"

    def GET(self,*,test:str):
        return f"here is some data according to : {test} "

def constructor_0() -> AthenaServerStructure:
    with (root_structure := AthenaServerStructure(name="root")) as structure:
        structure.add_page(AthenaServerPage(name="info"))
        with (page_data := PageData()) as page_:
            page_.add_page(AthenaServerPage(name="creator"))
            page_.add_page(AthenaServerPage(name="girlfriend"))
            page_.add_page(AthenaServerPage(name="twitch"))
        structure.add_page(page_data)

    return root_structure

def constructor_1() -> AthenaServerStructure:
    with (root_structure := AthenaServerStructure(name="root")) as page:
        page.add_page(AthenaServerPage(name="info"))
        with (page_data := AthenaServerPage(name="data")) as page_:
            page_.add_page(AthenaServerPage(name="creator"))
            page_.add_page(AthenaServerPage(name="girlfriend"))
            with (page_twitch := AthenaServerPage(name="twitch")) as page__:
                page__.add_page(AthenaServerPage(name="about"))
                page__.add_page(AthenaServerPage(name="channel"))
                page__.add_page(AthenaServerPage(name="mod"))
            page_.add_page(page_twitch)
        page.add_page(page_data)

    return root_structure