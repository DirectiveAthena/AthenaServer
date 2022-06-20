# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest
import tracemalloc
import asyncio

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server import AthenaServer

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test_AthenaServer(unittest.TestCase):
    def test_general(self):
        tracemalloc.start()
        server = AthenaServer(
            port=41768
        )
        server.start()