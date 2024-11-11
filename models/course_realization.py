from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class CourseRealization(Base):
    __tablename__ = "course_realizations"

    id = Column(Integer, primary_key=True, index=True)
    semester = Column(String(3), nullable=False)

    # ForeignKey to Course
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False, index=True)

    # Relationships
    course = relationship("Course", back_populates="realizations")
    exams = relationship("Exam", back_populates="course_realization")
    users = relationship("User", back_populates="course_realization")

