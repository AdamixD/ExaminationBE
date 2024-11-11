from typing import Optional

from pydantic import BaseModel

from models.user import Role


class UserBase(BaseModel):
    name: str
    surname: str
    role: Role
    email: str
    index: Optional[int] = None


class UserCreate(UserBase):
    password: str



class UserUpdate(UserBase):
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
