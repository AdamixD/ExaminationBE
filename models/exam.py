from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from database.base import Base


class Exam(Base):
    __tablename__ = "exams"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    duration_limit = Column(Integer, nullable=False)
    status = Column(String(255), nullable=False)

    # ForeignKey to CourseRealization and Lecturer
    course_realization_id = Column(Integer, ForeignKey("course_realizations.id"), nullable=False, index=True)


    # Relationships
    course_realization = relationship("CourseRealization", back_populates="exams")
    questions = relationship("Question", back_populates="exam")
    exam_students = relationship("ExamStudent", back_populates="exam")
