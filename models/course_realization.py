from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base
from .associations import student_course_association

class CourseRealization(Base):
    __tablename__ = "course_realizations"

    id = Column(Integer, primary_key=True, index=True)
    semester = Column(String(3), nullable=False)

    # ForeignKey
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False, index=True)
    lecturer_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    # Relationships
    course = relationship("Course", back_populates="realizations")
    exams = relationship("Exam", back_populates="course_realization")
    lecturer = relationship("Lecturer", back_populates="course_realizations")

    students = relationship("Student", secondary=student_course_association, back_populates="courses")

