from fastapi import FastAPI
from pydantic import BaseModel, Field

from src.sample_ai_pipeline import run_pipeline


app = FastAPI(
    title="AI Text Classification API",
    description="Simple API for sentiment classification",
    version="1.0"
)


class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text to classify"
    )


@app.get("/")
def root():
    return {
        "message": "AI Text Classification API is running"
    }


@app.post("/predict")
def predict(request: TextRequest):

    result = run_pipeline(request.text)

    return {
        "text": request.text,
        "sentiment": result["result"]["sentiment"]
    }