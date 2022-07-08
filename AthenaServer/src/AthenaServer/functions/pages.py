# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library
import AthenaLib.data.text as text

# Custom Packages
from AthenaServer.models.page import Page

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
def page_constructor(root_page:Page, page_construction:dict) -> Page:
    """
    A simple page constructor to stitch pages together.
    Uses recursion to go through the entire dictionary.
    When calling this function for a first time in a project,
        make sure that the root_page has been defined with the correct server root.

    Parameters:
    - root_page: The page that will be returned with the constructed pages within it
    - page_construction: the dictionary mapping of how all pages are linked together
    """

    for page, content in page_construction.items(): #type:Page, dict[Page:dict]
        # Makes sure we don't overwrite any already assigned pages
        if (page_name := page.name.lower()) in root_page.content:
            raise ValueError(f"Cant have two pages with the same name ('{page_name}') in the '{root_page.name}' Page")
        # add recursively constructed pages to the root
        #   Recursion used here for ease of use
        #   And it works s long as the page_construction is defined in the same format each and every iteration
        root_page.content[page_name] = page_constructor(page, content)

    return root_page

# ----------------------------------------------------------------------------------------------------------------------
def get_page(root_page:Page, page_location:str, *, sep="/") -> Page:
    """
    Get a specified page located somewhere within the page structure

    Parameters:
    - root_page: The root page of the server, which has all other pages within it's content attribute
    - page_location: the location string
    - sep: The separation on which to split the page_location string
    """
    if not page_location.startswith(root_page_name := root_page.name):
        raise ValueError(f"page_location did not start with the root page name of '{root_page_name}'")

    # form the list and remove the root page name
    return root_page.get_page(page_location.split(sep)[1:])
