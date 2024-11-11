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

    # Polymorphic
    __mapper_args__ = {
        "polymorphic_identity": "user",
        "polymorphic_on": "role"
    }
