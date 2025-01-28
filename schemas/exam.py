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
    grading_method: Optional[str] = None  # New field for grading method


class ExamCreate(ExamBase):
    pass


class ExamUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    duration_limit: Optional[int] = None
    status: Optional[str] = None
    course_realization_id: Optional[int] = None
    questions_quantity: Optional[int] = None
    max_points: Optional[float] = None
    type: Optional[str] = None
    grading_method: Optional[str] = None  # Field for grading method


class ExamResponse(ExamBase):
    id: int
    questions: List[QuestionResponse]

    class Config:
        orm_mode = True