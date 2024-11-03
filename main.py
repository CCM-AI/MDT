from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Define FastAPI app
app = FastAPI()

# Load model and pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Define input model for request
class QuestionRequest(BaseModel):
    question: str
    context: str

# Endpoint to answer patient questions
@app.post("/answer")
async def answer_question(request: QuestionRequest):
    result = qa_pipeline(question=request.question, context=request.context)
    return {"answer": result["answer"], "confidence": result["score"]}

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Perplexity MDT AI API"}
