# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import json

# Custom Library

# Custom Packages
import AthenaServer.models.exceptions as exceptions

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def json_as_bytes_to_dict(data: bytearray) -> dict:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        raise exceptions.JsonNotFound