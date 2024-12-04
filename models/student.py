from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from models.associations import student_course_association
from models.user import User, Role

class Student(User):
    """
    Represents a student in the user hierarchy, extending the base User model.
    """
    # Fixed: Set index to have a proper default value and allow nullable=True for flexibility
    index = Column(Integer, nullable=True, default=lambda: None)

    __mapper_args__ = {
        'polymorphic_identity': Role.STUDENT,
    }

    # Relationship with course realizations through the association table
    courses = relationship(
        "CourseRealization",
        secondary=student_course_association,
        back_populates="students"
    )

    # Relationship with exams for the student
    exams = relationship("ExamStudent", back_populates="student")