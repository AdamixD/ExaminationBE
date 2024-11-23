from pydantic import BaseModel
from typing import Optional

from .course import CourseResponse
from .user import UserResponse

class CourseRealizationBase(BaseModel):
    semester: str
    course_id: int
    lecturer_id: int  # Added lecturer_id 

class CourseRealizationCreate(CourseRealizationBase):
    pass

class CourseRealizationUpdate(BaseModel):  
    semester: Optional[str]
    course_id: Optional[int]
    lecturer_id: Optional[int]  

class CourseRealizationResponse(CourseRealizationBase):
    id: int
    course: Optional[CourseResponse]
    lecturer: Optional[UserResponse]

    class Config:
        orm_mode = True
