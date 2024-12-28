from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from .question_result import QuestionResultResponse


class ExamStudentBase(BaseModel):
    score: Optional[float] = None
    status: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    duration: Optional[int] = None
    exam_id: int
    student_id: int


class ExamStudentCreate(ExamStudentBase):
    pass


class ExamStudentUpdate(ExamStudentBase):
    score: Optional[float]
    status: Optional[str]
    duration: Optional[int]


class ExamStudentResponse(ExamStudentBase):
    id: int
    # question_results: List["QuestionResultResponse"]

    class Config:
        orm_mode = True
