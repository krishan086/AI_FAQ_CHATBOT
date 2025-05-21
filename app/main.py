from fastapi import FastAPI
from .routes import router

app = FastAPI(title="AI FAQ Chatbot")
app.include_router(router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "AI FAQ Chatbot API"}