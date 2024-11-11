from sqlalchemy import Column, Integer, ForeignKey, Boolean, Text, String
from sqlalchemy.orm import relationship

from database.base import Base


class QuestionItem(Base):
    __tablename__ = "question_items"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    image = Column(String(255))  # optional image path or URL
    correctness = Column(Boolean, nullable=False)

    # ForeignKey to Question
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False, index=True)

    # Relationship
    question = relationship("Question", back_populates="question_items")