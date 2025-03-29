from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from controllers.research_controller import (
    summarize_text,
    generate_citation,
    answer_query
)

router = APIRouter()

@router.post("/process")
async def process_paper(file: UploadFile = File(...), author: str = "", title: str = "", year: int = None, publisher: str = ""):
    """
    Upload a research paper to automatically generate a summary and request citation details.
    """
    try:
        # Generate summary
        summary = summarize_text(file)

        # Ask user for citation details if not provided
        if not (author and title and year and publisher):
            raise HTTPException(status_code=400, detail="Please provide citation details: author, title, year, publisher.")

        # Generate citation
        citation = generate_citation(author, title, year, publisher)

        return {
            "summary": summary,
            "citation": citation,
            "message": "Do you have any queries about the research paper?"
        }

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/query")
async def query_paper(file: UploadFile = File(...), query: str = ""):
    """
    Answer a query based on the research paper content.
    """
    try:
        return answer_query(file, query)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
