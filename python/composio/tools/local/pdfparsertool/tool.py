import typing as t

from composio.tools.base.local import LocalAction, LocalTool

from .actions import ExtractText, CountPages


class Pdfparsertool(LocalTool, autoload=True):
    """Tool To Parse/Read A PDF file"""

    @classmethod
    def actions(cls) -> list[t.Type[LocalAction]]:
        return [ExtractText, CountPages]