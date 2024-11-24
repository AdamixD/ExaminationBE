from pydantic import BaseModel
from typing import Optional

from .course import CourseResponse


class CourseRealizationBase(BaseModel):
    semester: str
    course_id: int
    lecturer_id: int


class CourseRealizationCreate(CourseRealizationBase):
    pass


class CourseRealizationUpdate(CourseRealizationBase):
    semester: Optional[str]
    course_id: Optional[int]
    lecturer_id: Optional[int]


class CourseRealizationResponse(CourseRealizationBase):
    id: int
    course: Optional["CourseResponse"]

    class Config:
        orm_mode = True