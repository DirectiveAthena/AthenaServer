# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages
from AthenaServer.models.athena_server_pages import AthenaServerStructure, AthenaServerPage

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
def constructor_0() -> AthenaServerStructure:
    with (root_structure := AthenaServerStructure(name="root")) as structure:
        structure.add_page(AthenaServerPage(name="info"))
        with (page_data := AthenaServerPage(name="data")) as page_:
            page_.add_page(AthenaServerPage(name="creator"))
            page_.add_page(AthenaServerPage(name="girlfriend"))
            page_.add_page(AthenaServerPage(name="twitch"))
        structure.add_page(page_data)

    return root_structure

def constructor_1() -> AthenaServerStructure:
    with (root_structure := AthenaServerStructure(name="root")) as page:
        page.add_page(AthenaServerPage(name="info"))
        with (page_data := AthenaServerPage(name="data")) as page_:
            page_.add_page(AthenaServerPage(name="creator"))
            page_.add_page(AthenaServerPage(name="girlfriend"))
            with (page_twitch := AthenaServerPage(name="twitch")) as page__:
                page__.add_page(AthenaServerPage(name="about"))
                page__.add_page(AthenaServerPage(name="channel"))
                page__.add_page(AthenaServerPage(name="mod"))
            page_.add_page(page_twitch)
        page.add_page(page_data)

    return root_structure


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class test_AthenaServerPage(unittest.TestCase):
    def test_structure_0(self):
        self.assertEqual(
            {
                ("root",),
                ("root", "info"),
                ("root", "data"),
                ("root", "data", "creator"),
                ("root", "data", "girlfriend"),
                ("root", "data", "twitch"),
            },
            set(constructor_0().structure.keys())
        )
    def test_structure_1(self):
        self.assertEqual(
            {
                ("root",),
                ("root", "info"),
                ("root", "data"),
                ("root", "data", "creator"),
                ("root", "data", "girlfriend"),
                ("root", "data", "twitch"),
                ("root", "data", "twitch", "about"),
                ("root", "data", "twitch", "channel"),
                ("root", "data", "twitch", "mod"),
            },
            set(constructor_1().structure.keys())
        )