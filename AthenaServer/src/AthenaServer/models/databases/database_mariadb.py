# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import asyncio
import aiomysql
from typing import Any

# Custom Library

# Custom Packages
from AthenaServer.models.databases.database import Database

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class DatabaseMariaDB(Database):
    pool:aiomysql.Pool

    async def connect(self, host:str, port:int, username:str, password:str, autocommit:bool=True):
        self.pool = await aiomysql.create_pool(
            host=host,
            port=port,
            user=username,
            password=password
        )

    async def get_cursor(self) -> aiomysql.Cursor:
        async with self.pool.acquire() as conn:
            return await conn.cursor()

    async def close(self):
        self.pool.close()
        await self.pool.wait_closed()