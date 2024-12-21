from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import services.question_item as service
from database.session import get_db
from schemas.question_item import QuestionItemCreate, QuestionItemResponse, QuestionItemUpdate

router = APIRouter(prefix="/question_items", tags=["question_items"])

@router.get("/all", response_model=List[QuestionItemResponse])
def get_all_question_items(db: Session = Depends(get_db)):
    return service.get_all_question_items(db=db)

@router.get("/{question_item_id}", response_model=QuestionItemResponse)
def get_question_item(question_item_id: int, db: Session = Depends(get_db)):
    question_item = service.get_question_item(db, question_item_id)
    if question_item is None:
        raise HTTPException(status_code=404, detail="Question Item not found")
    return question_item

@router.post("/", response_model=QuestionItemResponse)
def create_question_item(question_item: QuestionItemCreate, db: Session = Depends(get_db)):
    return service.create_question_item(db, question_item)

@router.put("/{question_item_id}", response_model=QuestionItemResponse)
def update_question_item(question_item_id: int, question_item: QuestionItemUpdate, db: Session = Depends(get_db)):
    updated_question_item = service.update_question_item(db, question_item_id, question_item)
    if updated_question_item is None:
        raise HTTPException(status_code=404, detail="Question Item not found")
    return updated_question_item

@router.delete("/{question_item_id}", response_model=QuestionItemResponse)
def delete_question_item(question_item_id: int, db: Session = Depends(get_db)):
    deleted_question_item = service.delete_question_item(db, question_item_id)
    if deleted_question_item is None:
        raise HTTPException(status_code=404, detail="Question Item not found")
    return deleted_question_item
