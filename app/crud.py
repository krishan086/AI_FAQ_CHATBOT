from sqlalchemy.orm import Session
from . import models, schemas

def get_faq_by_question(db: Session, question: str):
    return db.query(models.FAQ).filter(models.FAQ.question == question).first()

def create_faq(db: Session, faq: schemas.FAQCreate):
    db_faq = models.FAQ(
        question=faq.question,
        answer=faq.answer,
        is_generated=faq.is_generated
    )
    db.add(db_faq)
    db.commit()
    db.refresh(db_faq)
    return db_faq
