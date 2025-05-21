from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    question: str
    answer: str
    is_generated: bool

class FAQCreate(BaseModel):
    question: str
    answer: str
    is_generated: bool