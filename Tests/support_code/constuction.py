# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import copy

from AthenaServer.functions.pages import page_constructor
from AthenaServer.models.page import Page

# Custom Packages

import Tests.support_code.page_library as PageLib

# ----------------------------------------------------------------------------------------------------------------------
# - Construction -
# ----------------------------------------------------------------------------------------------------------------------
ROOT_PAGE = Page(name="server_test")
CONSTRUCTION = {
    Page(name="test_empty"):{},
    PageLib.PageTest():{
        PageLib.PageTestBasic():{}
    }
}

# ----------------------------------------------------------------------------------------------------------------------
# - Constructor -
# ----------------------------------------------------------------------------------------------------------------------
def test_server_constructor(root_page=ROOT_PAGE,page_construction=None) -> Page:
    if page_construction is None:
        page_construction = CONSTRUCTION

    return page_constructor(
        root_page=copy.deepcopy(root_page),
        page_construction=copy.deepcopy(page_construction)
    )