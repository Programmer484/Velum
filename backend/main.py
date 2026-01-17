from fastapi import FastAPI

app = FastAPI(
    title="Velum API",
    description="Algorithm flag detection for social media posts",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "Welcome to Velum API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


@app.post("/analyze")
async def analyze_post(text: str):
    """Analyze if a post would be flagged by platform algorithms."""
    # TODO: Implement actual analysis logic
    return {
        "text": text,
        "would_be_flagged": False,
        "confidence": 0.0,
        "suggestions": [],
    }
