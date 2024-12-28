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


class UserUpdate(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None
    role: Optional[Role] = None
    email: Optional[str] = None
    index: Optional[int] = None
    password: Optional[str] = None


class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True
