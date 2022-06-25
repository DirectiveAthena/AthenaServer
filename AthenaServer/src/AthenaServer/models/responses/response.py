# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Any

# Custom Library
from AthenaServer.data.general import BODY

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, match_args=True)
class Response(ABC):
    body:Any

    def to_dict(self):
        return {BODY: self.body}

    @abstractmethod
    def encode(self) -> bytes:
        pass