from typing import Dict

from pydantic import BaseModel, Field
import PyPDF2

from composio.tools.base.local import LocalAction


class CountPagesRequest(BaseModel):
    file_path: str = Field(
        ...,
        description="The path to the PDF file to count pages in",
        json_schema_extra={"file_readable": True},
    )


class CountPagesResponse(BaseModel):
    page_count: int = Field(..., description="Number of pages in the PDF")


class CountPages(LocalAction[CountPagesRequest, CountPagesResponse]):
    """
    Counts the number of pages in the specified PDF file.
    """
    _display_name = "Counting Pages"
    _request_schema = CountPagesRequest
    _response_schema = CountPagesResponse
    _tags = ["pdf", "pages"]
    _tool_name = "pdfparser"


    def execute(self,request: CountPagesRequest, metadata: Dict) -> CountPagesResponse:
        with open(request.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return CountPagesResponse(page_count=len(reader.pages))
