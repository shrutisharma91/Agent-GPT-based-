from pydantic import BaseModel

class SummarizationResponse(BaseModel):
    summary: str

class CitationResponse(BaseModel):
    citation: str

class QueryResponse(BaseModel):
    answer: str
