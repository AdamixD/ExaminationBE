import enum

from sqlalchemy import Column, Enum, Integer, String

from database.base import Base


class Role(enum.Enum):
    STUDENT: str = "STUDENT"
    LECTURER: str = "LECTURER"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    surname = Column(String(100), nullable=False)
    role = Column(Enum(Role), default=Role.STUDENT, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), unique=True, nullable=False)
