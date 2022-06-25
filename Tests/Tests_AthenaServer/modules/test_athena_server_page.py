# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
import unittest

# Custom Library

# Custom Packages
from Tests.Tests_AthenaServer.support import constructor_0, constructor_1

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class test_AthenaServerPage(unittest.TestCase):
    def test_structure_0(self):
        self.assertEqual(
            { # reason for a set comparison is that a set doesn't hold the index into account
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
            { # reason for a set comparison is that a set doesn't hold the index into account
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