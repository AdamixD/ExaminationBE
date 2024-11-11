import enum

from sqlalchemy import Column, Enum, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.base import Base


class Role(enum.Enum):
    STUDENT: str = "STUDENT"
    LECTURER: str = "LECTURER"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    role = Column(Enum(Role), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    # ForeignKey to CourseRealization
    course_realization_id = Column(Integer, ForeignKey('course_realizations.id'), index=True)

    # Relations
    course_realization = relationship("CourseRealization", back_populates="users")
    exams = relationship("ExamStudent", back_populates="student")
    lecturer_exams = relationship("Exam", back_populates="lecturer")

    # Polymorphic
    __mapper_args__ = {
        'polymorphic_identity': 'user',
        'polymorphic_on': role
    }