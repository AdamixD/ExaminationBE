from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

from database.base import Base


class QuestionResult(Base):
    __tablename__ = 'question_results'

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float, nullable=False)
    comment = Column(Text)
    answer = Column(Text)

    # ForeignKeys to ExamStudent and Question
    exam_student_id = Column(Integer, ForeignKey('exam_students.id'), nullable=False, index=True)
    question_id = Column(Integer, ForeignKey('questions.id'), nullable=False, index=True)

    # Relationships
    exam_student = relationship("ExamStudent", back_populates="question_results")
    question = relationship("Question", back_populates="question_results")