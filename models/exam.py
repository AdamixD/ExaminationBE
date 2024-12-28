import enum

from sqlalchemy import Column, DateTime, Enum, Integer, ForeignKey, Float, String
from sqlalchemy.orm import relationship

from database.base import Base


class ExamStatus(enum.Enum):
    UNDEFINED: str = "UNDEFINED"
    SCHEDULED: str = "SCHEDULED"
    ACTIVE: str = "ACTIVE"
    CLOSED: str = "CLOSED"


class ExamType(enum.Enum):
    TEST: str = "TEST"
    PROJECT: str = "PROJECT"


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    duration_limit = Column(Integer, nullable=True)
    status = Column(Enum(ExamStatus), nullable=False)
    questions_quantity = Column(Integer, nullable=True)
    max_points = Column(Float, nullable=False)
    type = Column(Enum(ExamType), nullable=False)

    # ForeignKey to CourseRealization and Lecturer
    course_realization_id = Column(Integer, ForeignKey("course_realizations.id"), nullable=False, index=True)

    # Relationships
    course_realization = relationship("CourseRealization", back_populates="exams")
    questions = relationship("Question", back_populates="exam")
    exam_students = relationship("ExamStudent", back_populates="exam")
