# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import Callable

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class AthenaServerClient(ABC):
    host:str
    port:int

    # ------------------------------------------------------------------------------------------------------------------
    # - ABC methods -
    # ------------------------------------------------------------------------------------------------------------------
    @abstractmethod
    async def connect(self):...
    @abstractmethod
    async def close(self): ...