# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaServer.models.context import Context

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True, unsafe_hash=True)
class Page:
    name:str

    # non init
    content: dict[str:Page] = field(init=False, default_factory=dict, hash=False)

    # ------------------------------------------------------------------------------------------------------------------
    # - Init stuff -
    # ------------------------------------------------------------------------------------------------------------------
    def __post_init__(self):
        if " " in self.name:
            raise ValueError("the page name cannot contain spaces")

    # ------------------------------------------------------------------------------------------------------------------
    # - Special methods -
    # ------------------------------------------------------------------------------------------------------------------
    def _repr_small(self) -> str:
        return f"{type(self).__name__}(name={self.name})"

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods that assign commands -
    # ------------------------------------------------------------------------------------------------------------------
    async def POST(self, context: Context, **kwargs):
        raise AttributeError(f"POST has not been defined on the current {self._repr_small()}")
    async def GET(self, context: Context, **kwargs):
        raise AttributeError(f"GET has not been defined on the current {self._repr_small()}")
    async def REPLACE(self, context: Context, **kwargs):
        raise AttributeError(f"REPLACE has not been defined on the current {self._repr_small()}")
    async def MODIFY(self, context: Context, **kwargs):
        raise AttributeError(f"MODIFY has not been defined on the current {self._repr_small()}")
    async def DELETE(self, context: Context, **kwargs):
        raise AttributeError(f"DELETE has not been defined on the current {self._repr_small()}")

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

    def get_page_structure_and_commands(self) -> dict:
        """
        Returns a dictionary with all populated pages and page commands
        """
        return_dict = {}
        for page_name, page in self.content.items():
            return_dict[page_name] = {
                "methods": {m:doc for m in ("POST", "GET", "REPLACE", "MODIFY", "DELETE")
                            if (doc := getattr(page, m).__doc__) is not None},
                "pages": page.get_page_structure_and_commands()
            }
        return return_dict

    def get_page_structure_and_commands_of_itself(self):
        """
        Returns a dictionary with all populated pages and page commands, without the structure of any grand child pages
        """
        return_dict = {}
        for page_name, page in self.content.items():
            return_dict[page_name] = {
                "methods": {m:doc for m in ("POST", "GET", "REPLACE", "MODIFY", "DELETE")
                            if (doc := getattr(page, m).__doc__) is not None},
                "pages": {}
            }
        return return_dict



