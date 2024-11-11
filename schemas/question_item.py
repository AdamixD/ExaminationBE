from pydantic import BaseModel
from typing import Optional

class QuestionItemBase(BaseModel):
    text: str
    image: Optional[str]
    correctness: bool
    question_id: int

class QuestionItemCreate(QuestionItemBase):
    pass

class QuestionItemUpdate(QuestionItemBase):
    text: Optional[str]
    image: Optional[str]
    correctness: Optional[bool]

class QuestionItemResponse(QuestionItemBase):
    id: int

    class Config:
        orm_mode = True