from sqlalchemy import Column, Integer

from models.user import User, Role

class Student(User):
    # TODO repair no index default value
    index = Column(Integer,nullable=False, default=0)

    __mapper_args__ = {
        'polymorphic_identity': Role.STUDENT,
    }