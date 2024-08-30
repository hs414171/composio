from typing import Dict

from pydantic import BaseModel, Field
import PyPDF2

from composio.tools.base.local import LocalAction



class ExtractTextRequest(BaseModel):
    file_path: str = Field(
        ...,
        description="The path to the PDF file to extract text from",
        json_schema_extra={"file_readable": True},
    )


class ExtractTextResponse(BaseModel):
    text: str = Field(..., description="Extracted text from the PDF")


class ExtractText(LocalAction[ExtractTextRequest, ExtractTextResponse]):
    """
    Extracts text from the specified PDF file.
    """
    _display_name = "Extracting Text"
    _request_schema = ExtractTextRequest
    _response_schema = ExtractTextResponse
    _tags = ["pdf", "text"]
    _tool_name = "pdfparser"

    def execute(self,request: ExtractTextRequest, metadata: Dict) -> ExtractTextResponse:
        with open(request.file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text += page.extract_text()
        return ExtractTextResponse(text=text)