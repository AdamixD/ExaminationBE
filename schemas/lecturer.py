from .user import UserResponse


class LecturerResponse(UserResponse):
    __mapper_args__ = {
        'polymorphic_identity': 'LECTURER',
    }

    class Config:
        orm_mode = True
