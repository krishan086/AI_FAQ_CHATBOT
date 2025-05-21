import logging
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import crud, models, schemas, llm
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/ask", response_model=schemas.AnswerResponse)
async def ask_question(question: schemas.QuestionRequest, db: Session = Depends(get_db)):
    try:
        db_faq = crud.get_faq_by_question(db, question.question)
        if db_faq:
            return {
                "question": db_faq.question,
                "answer": db_faq.answer,
                "is_generated": db_faq.is_generated
            }

        generated_answer = llm.generate_answer(question.question)

        new_faq = schemas.FAQCreate(
            question=question.question,
            answer=generated_answer,
            is_generated=True
        )
        db_faq = crud.create_faq(db, new_faq)

        return {
            "question": db_faq.question,
            "answer": db_faq.answer,
            "is_generated": db_faq.is_generated
        }

    except Exception as e:
        logging.error(f"Error in /ask endpoint: {e}", exc_info=True)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")
