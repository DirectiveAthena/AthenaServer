# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations

# Custom Library

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Context:
    error:bool=False
    error_code:int=None

    def set_error(self,*,error_code:int) -> Context:
        self.error = True
        self.error_code = error_code
        return self

    @classmethod
    def as_error(cls,*,error_code:int) -> Context:
        return cls().set_error(error_code=error_code)