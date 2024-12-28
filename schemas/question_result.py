from pydantic import BaseModel
from typing import Optional


class QuestionResultBase(BaseModel):
    score: float
    comment: Optional[str]
    answer: Optional[str]
    exam_student_id: int
    question_id: int


class QuestionResultCreate(QuestionResultBase):
    pass


class QuestionResultUpdate(QuestionResultBase):
    score: Optional[float]
    comment: Optional[str]
    answer: Optional[str]


class QuestionResultResponse(QuestionResultBase):
    id: int

    class Config:
        orm_mode = True
