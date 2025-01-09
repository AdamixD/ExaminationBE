from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

from .question import QuestionResponse
from .question_result import QuestionResultResponse
from .student import StudentResponse
from .exam import ExamResponse


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
    questions: List["QuestionResponse"]
    question_results: List["QuestionResultResponse"]

    class Config:
        orm_mode = True

class ExamStudentExamResponse(ExamStudentBase):
    id: int
    student: "StudentResponse"
    exam: "ExamResponse"

    class Config:
        orm_mode = True