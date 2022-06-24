# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
from AthenaServer.models.athena_server import AthenaServer
from AthenaServer.models.athena_server_page_structure import AthenaServerStructure

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
def create_test_server() -> AthenaServer:
    server = AthenaServer(
        host="localhost",
        port=41768,
        pages=...
    )
    return server


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    create_test_server().start()