from sqlalchemy import Column, Integer

from models.user import User

class Student(User):
    index = Column(Integer, nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'STUDENT',
    }