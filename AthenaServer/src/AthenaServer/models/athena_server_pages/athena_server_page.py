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
@dataclass(match_args=True, slots=True, eq=False, order=False)
class AthenaServerPage(AthenaServerPageLogic):
    # ------------------------------------------------------------------------------------------------------------------
    # - Restfull commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def GET(self, **kwargs) -> dict:
        """A method that retrieves information from the page's content"""

    async def HEAD(self, **kwargs) -> dict:
        """Same as GET, but only fetch status line and header section"""

    async def POST(self, **kwargs) -> dict:
        """A method that creates content on the page"""

    async def PUT(self, **kwargs) -> dict:
        """A method that creates or replaces content on the page"""

    async def PATCH(self, **kwargs) -> dict:
        """A method that updates the content on the page"""

    async def DELETE(self, **kwargs) -> dict:
        """A method that removes content on the page"""

    async def OPTIONS(self, **kwargs) -> dict:
        """Describe the communication options for the target resource"""
