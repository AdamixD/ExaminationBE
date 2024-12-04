from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base
from .associations import student_course_association


class CourseRealization(Base):
    __tablename__ = "course_realizations"

    id = Column(Integer, primary_key=True, index=True)
    semester = Column(String(10), nullable=False)  # Zwiększono limit znaków do 10 dla bezpieczeństwa danych.

    # ForeignKeys
    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False, index=True)
    lecturer_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)

    # Relationships
    course = relationship("Course", back_populates="realizations", lazy="joined")
    exams = relationship("Exam", back_populates="course_realization", cascade="all, delete-orphan")
    lecturer = relationship("User", back_populates="course_realizations", lazy="joined")  # Powiązanie z wykładowcą.

    students = relationship(
        "Student",
        secondary=student_course_association,
        back_populates="courses",
        lazy="subquery",
        cascade="all"
    )