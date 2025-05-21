from sqlalchemy import Column, Integer, String, Text, Boolean
from .database import Base

class FAQ(Base):
    __tablename__ = "faqs"
    __table_args__ = {'schema': 'faq_schema'}

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True, index=True)
    answer = Column(String)
    is_generated = Column(Boolean, default=False)
