from sqlalchemy.orm import relationship

from models.user import User, Role

class Lecturer(User):
    __mapper_args__ = {
        "polymorphic_identity": Role.LECTURER,
    }

    course_realizations = relationship("CourseRealization", back_populates="lecturer")
