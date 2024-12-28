from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

import services.question as service

from database.session import get_db
from schemas.question import QuestionCreate, QuestionResponse, QuestionUpdate

router = APIRouter(prefix="/questions", tags=["questions"])


@router.get("/all", response_model=List[QuestionResponse])
def get_all_questions(db: Session = Depends(get_db)):
    return service.get_all_questions(db=db)


@router.get("/exam/{exam_id}", response_model=List[QuestionResponse])
def get_all_exam_questions(
    exam_id: int,
    db: Session = Depends(get_db),
):
    return service.get_all_exam_questions(db=db, exam_id=exam_id)


@router.get("/{question_id}", response_model=QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = service.get_question(db, question_id)
    if question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return question


@router.post("/", response_model=QuestionResponse)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    return service.create_question(db, question)


@router.put("/{question_id}", response_model=QuestionResponse)
def update_question(question_id: int, question: QuestionUpdate, db: Session = Depends(get_db)):
    updated_question = service.update_question(db, question_id, question)
    if updated_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return updated_question


@router.delete("/{question_id}", response_model=QuestionResponse)
def delete_question(question_id: int, db: Session = Depends(get_db)):
    deleted_question = service.delete_question(db, question_id)
    if deleted_question is None:
        raise HTTPException(status_code=404, detail="Question not found")
    return deleted_question
