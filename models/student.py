from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from models.associations import student_course_association
from models.user import User, Role

class Student(User):
    # TODO repair no index default value
    index = Column(Integer,nullable=False, default=0)

    __mapper_args__ = {
        'polymorphic_identity': Role.STUDENT,
    }

    courses = relationship("CourseRealization", secondary=student_course_association, back_populates="students")
    exams = relationship("ExamStudent", back_populates="student")
