# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
import json

# Custom Library
from AthenaLib.models.version import Version

# Custom Packages
from AthenaServer.models.athena_server_methods import MethodCommand
from AthenaServer.models.athena_server_command import AthenaServerCommand
import AthenaServer.models.exceptions as exceptions

from AthenaServer.functions.casting import json_as_bytes_to_dict

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerDataHandler:
    commands:dict[AthenaServerCommand:AthenaServerCommand] = field(default_factory=dict)
    # ------------------------------------------------------------------------------------------------------------------
    # - factory, needed for asyncio.AbstractEventLoop.create_connection protocol_factory kwarg used in Launcher -
    # ------------------------------------------------------------------------------------------------------------------
    def handle(self, data: bytearray):
        try:
            handled_command = AthenaServerCommand(**json_as_bytes_to_dict(data))
        except TypeError:
            raise exceptions.WrongFormat

        if handled_command not in self.commands:
            return

        self.commands[handled_command].callback()

