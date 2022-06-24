# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaServer.data.shared import SHARED_PAGES

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(match_args=True, slots=True)
class AthenaServerPage:
    name:str
    children:dict[str:AthenaServerPage]=field(default_factory=dict)

    # ------------------------------------------------------------------------------------------------------------------
    # Enter-exit structure to define it's children
    # ------------------------------------------------------------------------------------------------------------------
    def add_page(self, page: AthenaServerPage) -> AthenaServerPage:
        if not isinstance(page, AthenaServerPage):
            raise TypeError("Only a AthenaServerPage class or a class inherited from it can be added as a page")
        elif page.name in self.children:
            raise ValueError(f"Duplicate child by the name of '{page.name}' is already present in the parent page")

        for child in page.children: #type: AthenaServerPage
            SHARED_PAGES[(page.name, child.name)] = child
        SHARED_PAGES[(page,)] = page

        # the return of self allows for chaining
        return self

    # ------------------------------------------------------------------------------------------------------------------
    # Restfull commands
    # ------------------------------------------------------------------------------------------------------------------
    def GET(self, **kwargs):
        pass

    def PUT(self, **kwargs):
        pass

    def POST(self, **kwargs):
        pass

    def DELETE(self, **kwargs):
        pass
