import enum

from sqlalchemy import Column, Enum, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from database.base import Base
from models.associations import exam_student_question_association


class StudentExamStatus(enum.Enum):
    SCHEDULED: str = "SCHEDULED"
    ACTIVE: str = "ACTIVE"
    COMPLETED: str = "COMPLETED"
    CLOSED: str = "CLOSED"


class ExamStudent(Base):
    __tablename__ = "exam_students"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float, nullable=True)
    status = Column(Enum(StudentExamStatus), nullable=False)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    duration = Column(Integer, nullable=True)  # in minutes

    # ForeignKeys to Exam and Student
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # Relationships
    exam = relationship("Exam", back_populates="exam_students")
    student = relationship("Student", back_populates="exams")
    question_results = relationship("QuestionResult", back_populates="exam_student")

    questions = relationship("Question", secondary=exam_student_question_association, back_populates="exam_students")
