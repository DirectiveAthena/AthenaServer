# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class Page:
    name:str

    # non init
    content: dict[str:Page] = field(init=False, default_factory=dict, hash=False)

    def __post_init__(self):
        if " " in self.name:
            raise ValueError("the page name cannot contain spaces")

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods that assign commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def POST(self, *args, **kwargs):raise NotImplementedError
    async def GET(self, *args, **kwargs):raise NotImplementedError
    async def REPLACE(self, *args, **kwargs):raise NotImplementedError
    async def MODIFY(self, *args, **kwargs):raise NotImplementedError
    async def DELETE(self, *args, **kwargs):raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods that affect pages -
    # ------------------------------------------------------------------------------------------------------------------
    def get_page(self, page_location:list[str]) -> Page:
        """
        Get a specified page located somewhere within the page structure.
        Will throw a KeyError if no corresponding Page could be found.

        Parameters:
        - page_location : A list of strings which is the path to follow to go to the requested page
        """
        # assign the first step of the loop to be the self
        #   Else we can't map to anything
        mem:Page = self
        # because the page_location is meant to be inserted as a list of string this technique is possible
        for i, page_str in enumerate(page_location):
            # check if the page actually exists in the mem value
            #   If not raise the correct error with the self name
            if page_str not in mem.content:
                raise KeyError(f"'{page_str}' was not found in the '{'/'.join(page_location[:i])}' Page")
            # continue down the keys of pages
            mem = mem.content[page_str]
        return mem

    def get_page_structure_and_commands(self, *, single:bool=False) -> dict:
        """
        Returns a dictionary with all populated pages and page commands

        Parameters:
        - single : Boolean value, if set to True the method will not get the structure of any grand child pages
        """
        return_dict = {}
        for page_name, page in self.content.items():
            return_dict[page_name] = {
                "methods": {m:doc for m in ("POST", "GET", "REPLACE", "MODIFY", "DELETE")
                            if (doc := getattr(page, m).__doc__) is not None},
                "pages": page.get_page_structure_and_commands() if not single else {}
            }
        return return_dict


