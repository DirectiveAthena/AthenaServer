# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages.athena_server_page_logic import AthenaServerPageLogic
from AthenaServer.models.responses.response_server import Response_AthenaServer

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(match_args=True, slots=True, eq=False, order=False)
class AthenaServerPage(AthenaServerPageLogic):
    # ------------------------------------------------------------------------------------------------------------------
    # - Restfull commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def GET(self, **kwargs) -> Response_AthenaServer:
        """A method that retrieves information from the page's content"""
        raise PermissionError

    async def HEAD(self, **kwargs) -> Response_AthenaServer:
        """Same as GET, but only fetch status line and header section"""
        raise PermissionError

    async def POST(self, **kwargs) -> Response_AthenaServer:
        """A method that creates content on the page"""
        raise PermissionError

    async def PUT(self, **kwargs) -> Response_AthenaServer:
        """A method that creates or replaces content on the page"""
        raise PermissionError

    async def PATCH(self, **kwargs) -> Response_AthenaServer:
        """A method that updates the content on the page"""
        raise PermissionError

    async def DELETE(self, **kwargs) -> Response_AthenaServer:
        """A method that removes content on the page"""
        raise PermissionError

    async def OPTIONS(self, **kwargs) -> Response_AthenaServer:
        """Describe the communication options for the target resource"""
        raise PermissionError
