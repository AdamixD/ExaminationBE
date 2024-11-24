from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    shortcut = Column(String(10), nullable=False)

    # Relationship with CourseRealization
    realizations = relationship("CourseRealization", back_populates="course")
