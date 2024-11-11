from models.user import User, Role

class Lecturer(User):
    __mapper_args__ = {
        "polymorphic_identity": Role.LECTURER,
    }