from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

from database.base import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    image = Column(String(255))  # optional image path or URL
    type = Column(String(255), nullable=False)
    score = Column(Float, nullable=False)
    score_type = Column(String(255), nullable=False)

    # ForeignKey to Exam
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False, index=True)

    # Relationships
    exam = relationship("Exam", back_populates="questions")
    question_items = relationship("QuestionItem", back_populates="question")
    question_results = relationship("QuestionResult", back_populates="question")