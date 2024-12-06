from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from .question import QuestionResponse

class ExamBase(BaseModel):
    start_date: datetime
    end_date: datetime
    duration_limit: int
    status: str
    course_realization_id: int

class ExamCreate(ExamBase):
    pass

class ExamUpdate(ExamBase):
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    duration_limit: Optional[int]
    status: Optional[str]

class ExamResponse(ExamBase):
    id: int
    questions: List["QuestionResponse"]

    class Config:
        orm_mode = True