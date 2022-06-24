# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages.athena_server_page_logic import AthenaServerPageLogic
from AthenaServer.models.athena_server_pages.athena_server_page import AthenaServerPage

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(match_args=True, slots=True)
class AthenaServerStructure(AthenaServerPageLogic):
    root_page:AthenaServerPage=None

    def __post_init__(self):
        if self.root_page is None:
            self.root_page = AthenaServerPage(name=self.name)
        elif not isinstance(self.root_page, AthenaServerPage):
            raise TypeError

    def __exit__(self, exc_type, exc_val, exc_tb):
        super(AthenaServerStructure, self).__exit__(exc_type, exc_val, exc_tb)
        self.structure[(self.root_page.name,)] = self.root_page # add the root page to itself

    def __getitem__(self, item:tuple):
        return self.structure[item]
