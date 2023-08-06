# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
from __future__ import annotations
from dataclasses import dataclass, field

# Custom Library

# Custom Packages
from AthenaCSS.Library.Support import NEW_LINE

from AthenaCSS.Generator.ManagerCSSGenerator import ManagerGenerator
from AthenaCSS.Generator.ConsoleColorGuide import ConsoleColorGuide

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
@dataclass(slots=True, kw_only=True)
class CSSGenerator:
    content: ManagerGenerator.content=field(init=False)
    console_color_guide:ConsoleColorGuide=field(default_factory=lambda : ConsoleColorGuide())

    # output options
    output_indentation:int = 4
    output_one_line:bool = False

    # Manager
    _manager:ManagerGenerator=field(default=None, repr=False)

    # ------------------------------------------------------------------------------------------------------------------
    # - Enter / Exit - (aka, the with statement)
    # ------------------------------------------------------------------------------------------------------------------
    def __enter__(self) -> ManagerGenerator:
        self._manager = ManagerGenerator()
        return self._manager

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.content = self._manager.content

    # ------------------------------------------------------------------------------------------------------------------
    # - String Outputs -
    # ------------------------------------------------------------------------------------------------------------------
    def _kw_to_str(self):
        return {
            "indentation":self.output_indentation,
            "one_line":self.output_one_line,
            "console_color_guide":self.console_color_guide
        }

    def to_string(self) -> str:
        # if the string is to be set on one line, don't do a \,n
        sep = NEW_LINE if not self.output_one_line else " "
        return sep.join(
            content.to_string(**self._kw_to_str())
            for content in self.content
        )

    def to_console(self) :
        for content in self.content:
            print(content.to_console(**self._kw_to_str()))

    def to_file(self, filepath:str):
        with open(filepath, "w+") as file:
            for content in self.content:
                file.write(content.to_string(**self._kw_to_str()))