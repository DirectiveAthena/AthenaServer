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

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class AthenaServerMethod:
    @staticmethod
    def Ping(interval:TimeValue=Minute(5)) -> MethodPing:
        return MethodPing(interval=interval)

# ----------------------------------------------------------------------------------------------------------------------
# - Ping Method -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class _Method:
    callback: Callable=None
    owner:Any=field(repr=False, default=None)

    def __call__(self, fnc:Callable):
        self.callback = lambda *args, **kwargs: fnc(self.owner, *args, **kwargs)
        return self

# ----------------------------------------------------------------------------------------------------------------------
# - Ping Method -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class MethodPing(_Method):
    interval: TimeValue=Minute(5)