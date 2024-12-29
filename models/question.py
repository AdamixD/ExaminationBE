import enum

from sqlalchemy import Column, Enum, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

from database.base import Base
from models.associations import exam_student_question_association


class QuestionType(enum.Enum):
    SINGLE: str = "SINGLE"
    MULTI: str = "MULTI"
    OPEN: str = "OPEN"


class QuestionScoreType(enum.Enum):
    PROPORTIONAL: str = "PROPORTIONAL"
    FULL: str = "FULL"


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    image = Column(String(255), nullable=True)  # optional image path or URL
    type = Column(String(255), nullable=False)
    # type = Column(Enum(QuestionType), nullable=False)
    score = Column(Float, nullable=False)
    score_type = Column(String(255), nullable=False)
    # score_type = Column(Enum(QuestionScoreType), nullable=False)

    # ForeignKey to Exam
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False, index=True)

    # Relationships
    exam = relationship("Exam", back_populates="questions")
    question_items = relationship("QuestionItem", back_populates="question", cascade='all, delete, delete-orphan')

    exam_students = relationship("ExamStudent", secondary=exam_student_question_association, back_populates="questions")
