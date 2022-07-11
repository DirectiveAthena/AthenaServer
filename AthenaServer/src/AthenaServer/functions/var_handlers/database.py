# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages
from AthenaServer.models.databases.database import Database

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
# noinspection PyTypeChecker
DATABASE:Database=None

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def set_database(database_type:type[Database]) -> None:
    """
    Creates a new DataHandler object if it doesn't exist yet in the global space.

    Parameters:
    - root_page: The Page that defines the root of the server.
        Has all it's contents defined with the correct child Pages
    """
    global DATABASE
    if DATABASE is None:
        DATABASE = database_type()

def get_database() -> Database:
    """
    Retrieve the DataHandler from the global space
    """
    global DATABASE
    return DATABASE