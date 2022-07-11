# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import abc

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Database(abc.ABC):
    @abc.abstractmethod
    async def connect(self, host:str, port:int, username:str, password:str):...

    @abc.abstractmethod
    async def get_cursor(self):...

    @abc.abstractmethod
    async def close(self):...