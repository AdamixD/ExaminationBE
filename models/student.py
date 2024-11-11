from sqlalchemy import Column, Integer

from models.user import User, Role

class Student(User):
    index = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': Role.STUDENT,
    }