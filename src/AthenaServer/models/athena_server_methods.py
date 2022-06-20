# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Any

# Custom Library
from AthenaLib.models.time import TimeValue, Minute

# Custom Packages
from AthenaServer.models.athena_server_command import AthenaServerCommand

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaServerMethod:
    @staticmethod
    def Ping(interval:TimeValue=Minute(5)) -> MethodPing:
        return MethodPing(interval=interval)
    @staticmethod
    def Command(structure:AthenaServerCommand) -> MethodCommand:
        return MethodCommand(structure=structure)

# ----------------------------------------------------------------------------------------------------------------------
# - Ping Method -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, match_args=True, unsafe_hash=True)
class _Method:
    callback: Callable=field(hash=False, default=None)
    owner:Any=field(hash=False,repr=False, default=None)

    def __call__(self, fnc:Callable):
        self.callback = lambda *args, **kwargs: fnc(self.owner, *args, **kwargs)
        return self

# ----------------------------------------------------------------------------------------------------------------------
# - Ping Method -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, match_args=True, unsafe_hash=True)
class MethodPing(_Method):
    interval: TimeValue = Minute(5)

@dataclass(slots=True, kw_only=True, match_args=True, unsafe_hash=True)
class MethodCommand(_Method):
    structure: AthenaServerCommand = field(hash=True, default=None)