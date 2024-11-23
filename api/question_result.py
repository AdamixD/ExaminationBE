from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import services.question_result as service

from database.session import get_db
from schemas.question_result import QuestionResultCreate, QuestionResultResponse, QuestionResultUpdate

router = APIRouter(prefix="/question_results", tags=["question_results"])

@router.get("/all", response_model=List[QuestionResultResponse])
def get_all_question_results(db: Session = Depends(get_db)):
    return service.get_all_question_results(db=db)

@router.get("/{question_result_id}", response_model=QuestionResultResponse)
def get_question_result(question_result_id: int, db: Session = Depends(get_db)):
    question_result = service.get_question_result(db, question_result_id)
    if question_result is None:
        raise HTTPException(status_code=404, detail="Question Result not found")
    return question_result

@router.post("/", response_model=QuestionResultResponse)
def create_question_result(question_result: QuestionResultCreate, db: Session = Depends(get_db)):
    return service.create_question_result(db, question_result)

@router.put("/{question_result_id}", response_model=QuestionResultResponse)
def update_question_result(question_result_id: int, question_result: QuestionResultUpdate, db: Session = Depends(get_db)):
    updated_question_result = service.update_question_result(db, question_result_id, question_result)
    if updated_question_result is None:
        raise HTTPException(status_code=404, detail="Question Result not found")
    return updated_question_result

@router.delete("/{question_result_id}", response_model=QuestionResultResponse)
def delete_question_result(question_result_id: int, db: Session = Depends(get_db)):
    deleted_question_result = service.delete_question_result(db, question_result_id)
    if deleted_question_result is None:
        raise HTTPException(status_code=404, detail="Question Result not found")
    return deleted_question_result
