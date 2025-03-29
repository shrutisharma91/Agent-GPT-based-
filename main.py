from fastapi import FastAPI
from routers import research
from config import OPENAI_API_KEY, SERPER_API_KEY

app = FastAPI(
    title="Research Paper API",
    description="API for Research Paper Agent",
    version="1.0"
)

# Include routers
app.include_router(research.router, prefix="/api/research", tags=["Research"])

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Research Paper API"}

# Main entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)