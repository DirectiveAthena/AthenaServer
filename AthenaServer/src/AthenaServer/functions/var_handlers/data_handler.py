# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaServer.models.data_handler import DataHandler
from AthenaServer.models.page import Page

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyTypeChecker
DATA_HANDLER:DataHandler=None

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def set_data_handler(root_page:Page) -> None:
    """
    Creates a new DataHandler object if it doesn't exist yet in the global space.

    Parameters:
    - root_page: The Page that defines the root of the server.
        Has all it's contents defined with the correct child Pages
    """
    global DATA_HANDLER
    if DATA_HANDLER is None:
        DATA_HANDLER = DataHandler(
            root_page=root_page
        )

def get_data_handler() -> DataHandler:
    """
    Retrieve the DataHandler from the global space
    """
    global DATA_HANDLER
    return DATA_HANDLER