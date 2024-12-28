from .user import UserResponse


class StudentResponse(UserResponse):
    index: int

    class Config:
        orm_mode = True
