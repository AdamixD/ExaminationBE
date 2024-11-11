from pydantic import BaseModel
from typing import List, Optional

from .question_item import QuestionItemResponse
from .question_result import QuestionResultResponse

class QuestionBase(BaseModel):
    text: str
    image: Optional[str]
    type: str
    score: float
    score_type: str
    exam_id: int

class QuestionCreate(QuestionBase):
    pass

class QuestionUpdate(QuestionBase):
    text: Optional[str]
    image: Optional[str]
    type: Optional[str]
    score: Optional[float]
    score_type: Optional[str]

class QuestionResponse(QuestionBase):
    id: int
    question_items: List["QuestionItemResponse"]
    question_results: List["QuestionResultResponse"]

    class Config:
        orm_mode = True