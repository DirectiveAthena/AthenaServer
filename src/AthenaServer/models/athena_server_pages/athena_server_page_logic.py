# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(match_args=True, slots=True)
class AthenaServerPageLogic:
    name:str
    structure: dict[str:AthenaServerPageLogic]=field(default_factory=dict)
    #non init
    manager:AthenaServerPageLogicManager=field(init=False, repr=False)

    # ------------------------------------------------------------------------------------------------------------------
    # Enter-exit structure to define it's structure
    # ------------------------------------------------------------------------------------------------------------------
    def __enter__(self) -> AthenaServerPageLogicManager:
        self.manager = AthenaServerPageLogicManager(parent_name=self.name)
        return self.manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.structure = self.manager.pages
        del self.manager

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class AthenaServerPageLogicManager:
    parent_name:str
    pages: dict[tuple:AthenaServerPageLogic]=field(default_factory=dict)

    def add_page(self, page:AthenaServerPageLogic) -> AthenaServerPageLogicManager:
        # if there are structure present, we need to flatten them
        for child_tuple, child_obj in page.structure.items():
            self.pages[(self.parent_name, *child_tuple)] = child_obj

        if (page_tuple := (self.parent_name, page.name)) in self.pages:
            raise ValueError
        self.pages[page_tuple] = page
        return self