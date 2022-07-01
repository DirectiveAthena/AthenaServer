# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass

# Custom Library
from AthenaServer.models.athena_server import AthenaServer
from AthenaServer.models.athena_server_pages import AthenaServerStructure, AthenaServerPage
from AthenaServer.models.responses.response_server import Response_AthenaServer

from AthenaServer.data.responses import PING
from AthenaServer.data.return_codes import Success, ErrorClient

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True)
class PageData(AthenaServerPage):
    name:str="data"

    async def GET(self,*,test:str)  -> Response_AthenaServer:
        return Response_AthenaServer(
            code=Success.Ok,
            body={"response":f"here is some data according to : {test} "}
        )

@dataclass(slots=True)
class PagePing(AthenaServerPage):
    name:str="ping"

    async def POST(self,*,response:str) -> Response_AthenaServer:
        if response == PING.body["AthenaServer"]:
            return Response_AthenaServer(
                code=Success.Ok
            )
        else:
            return Response_AthenaServer(
                code=ErrorClient.RequestTimeout
            )

def test_server_page_constructor() -> AthenaServerStructure:
    with (root_structure := AthenaServerStructure(name="root")) as structure:
       (structure
        .add_page(PagePing())
        .add_page(PageData())
        )
    return root_structure

def create_test_server() -> AthenaServer:
    server = AthenaServer(
        host="localhost",
        port=41768,
        pages_structure=test_server_page_constructor()
    )
    return server


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    create_test_server().start()