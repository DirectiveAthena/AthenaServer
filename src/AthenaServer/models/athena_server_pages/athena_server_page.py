# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages.athena_server_page_logic import AthenaServerPageLogic

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(match_args=True, slots=True)
class AthenaServerPage(AthenaServerPageLogic):
    # ------------------------------------------------------------------------------------------------------------------
    # - Restfull commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def GET(self, **kwargs):
        """A method that retrieves information from the page's content"""
        pass

    async def POST(self, **kwargs):
        """A method that creates content on the page"""
        pass

    async def PUT(self, **kwargs):
        """A method that creates or replaces content on the page"""
        pass

    async def PATCH(self, **kwargs):
        """A method that updates the content on the page"""
        pass

    async def DELETE(self, **kwargs):
        """A method that removes content on the page"""
        pass
