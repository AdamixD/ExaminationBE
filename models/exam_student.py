from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

from database.base import Base


class ExamStudent(Base):
    __tablename__ = "exam_students"

    id = Column(Integer, primary_key=True, index=True)
    score = Column(Float)
    status = Column(String(255), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)  # in minutes

    # ForeignKeys to Exam and Student
    exam_id = Column(Integer, ForeignKey("exams.id"), nullable=False, index=True)
    student_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)

    # Relationships
    exam = relationship("Exam", back_populates="exam_students")
    student = relationship("User", back_populates="exams")
    question_results = relationship("QuestionResult", back_populates="exam_student")