from models.user import User

class Lecturer(User):
    __mapper_args__ = {
        "polymorphic_identity": "LECTURER",
    }