# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field
import functools
# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class Page():
    name:str
    POST:functools.partial   = None
    GET:functools.partial    = None
    REPLACE:functools.partial= None
    MODIFY:functools.partial = None
    DELETE:functools.partial = None

    # non init
    _content: dict[str:Page] = field(init=False, default_factory=dict)
    _allow_addition_of_pages:bool = field(init=False, default=True)

    def __post_init__(self):
        if " " in self.name:
            raise ValueError("the page name cannot contain spaces")

    # ------------------------------------------------------------------------------------------------------------------
    # - Dunder Methods -
    # ------------------------------------------------------------------------------------------------------------------
    def __getitem__(self, item:str) -> Page:
        return self._content[item]

    # ------------------------------------------------------------------------------------------------------------------
    # - Methods that affect pages -
    # ------------------------------------------------------------------------------------------------------------------
    def add_pages(self, *pages:Page) -> Page:
        # only allow the addition of pages to be done at server creation
        if not self._allow_addition_of_pages:
            raise PermissionError

        for page in pages:
            if (page_name := page.name.lower()) in self._content:
                raise ValueError(f"Cant have two pages with the same name ('{page_name}') in the same Page '{self.name}'")
            self._content[page_name] = page

        # set the ability to set pages to False not have any pages change after the structure has been defined
        self._allow_addition_of_pages = False
        return self

    def get_page(self, page_location:list[str]) -> Page:
        # assign the first step of the loop to be the self
        #   Else we can't map to anything
        mem:Page = self
        # because the page_location is meant to be inserted as a list of string this technique is possible
        for i, page_str in enumerate(page_location):
            # check if the page actually exists in the mem value
            #   If not raise the correct error with the self name
            if page_str not in mem._content:
                raise KeyError(f"'{page_str}' was not found in the '{'/'.join(page_location[:i])}' Page")
            # continue down the keys of pages
            mem = mem[page_str]
        return mem

    def get_page_structure(self) -> dict:
        return_dict = {}
        for page_name, page in self._content.items():
            return_dict[page_name] = {
                "methods": [m for m in ("POST", "GET", "REPLACE", "MODIFY", "DELETE")
                            if getattr(page, m) is not None],
                "pages":page.get_page_structure()
            }
        return return_dict


