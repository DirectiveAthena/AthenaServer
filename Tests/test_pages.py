# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library
from AthenaServer.functions.pages import get_page
from AthenaServer.models.page import Page

# Custom Packages
from Tests.support_code.constuction import test_server_constructor

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class TestPages(unittest.IsolatedAsyncioTestCase):
    async def test_GET(self):
        root_page = test_server_constructor()
        self.assertEqual(
            "this was a successful test",
            await get_page(root_page, "server_test/test").GET()
        )

    async def test_Error(self):
        root_page = test_server_constructor()
        with self.assertRaises(AttributeError):
            await get_page(root_page, "server_test/test").POST()