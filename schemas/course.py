from pydantic import BaseModel
from typing import Optional


class CourseBase(BaseModel):
    title: str
    shortcut: str


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    title: Optional[str]
    shortcut: Optional[str]


class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True