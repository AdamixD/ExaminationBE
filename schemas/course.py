from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    title: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    title: Optional[str]

class CourseResponse(CourseBase):
    id: int

    class Config:
        orm_mode = True