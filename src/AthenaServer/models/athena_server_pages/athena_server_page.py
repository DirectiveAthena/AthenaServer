# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages.athena_server_page_logic import AthenaServerPageLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(match_args=True, slots=True)
class AthenaServerPage(AthenaServerPageLogic):
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
