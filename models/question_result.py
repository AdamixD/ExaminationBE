from sqlalchemy import Column, Integer, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

from database.base import Base
from models.associations import question_result_item_association


class QuestionResult(Base):
    __tablename__ = 'question_results'

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float, nullable=False)
    comment = Column(Text)
    answer = Column(Text)

    # ForeignKeys to ExamStudent and Question
    exam_student_id = Column(Integer, ForeignKey('exam_students.id'), nullable=False, index=True)

    # Relationships
    exam_student = relationship("ExamStudent", back_populates="question_results")

    question_items = relationship("QuestionItem", secondary=question_result_item_association, back_populates="question_results")
