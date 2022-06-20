# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library
from AthenaLib.models.version import Version

# Custom Packages
from AthenaServer.models.athena_server_methods import MethodCommand
from AthenaServer.models.athena_server_command import AthenaServerCommand

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
        handled_command = AthenaServerCommand(api_level=Version(0,0,0), name=data.decode("utf_8"))
        if handled_command not in self.commands:
            return

        self.commands[handled_command].callback()