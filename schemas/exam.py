from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

from .question import QuestionResponse


class ExamBase(BaseModel):
    title: str
    start_date: datetime
    end_date: datetime
    duration_limit: Optional[int] = None
    status: str
    course_realization_id: int
    questions_quantity: Optional[int] = None
    max_points: float
    type: str


class ExamCreate(ExamBase):
    pass


class ExamUpdate(ExamBase):
    title: str
    start_date: Optional[datetime]
    end_date: Optional[datetime]
    duration_limit: Optional[int]
    status: Optional[str]
    questions_quantity: Optional[int]
    max_points: Optional[float]
    type: Optional[str]


class ExamResponse(ExamBase):
    id: int
    questions: List["QuestionResponse"]

    class Config:
        orm_mode = True
