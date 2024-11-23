from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import services.exam as service

from database.session import get_db
from schemas.exam import ExamCreate, ExamResponse, ExamUpdate

router = APIRouter(prefix="/exams", tags=["exams"])

@router.get("/all", response_model=List[ExamResponse])
def get_all_exams(db: Session = Depends(get_db)):
    return service.get_all_exams(db=db)

@router.get("/{exam_id}", response_model=ExamResponse)
def get_exam(exam_id: int, db: Session = Depends(get_db)):
    exam = service.get_exam(db, exam_id)
    if exam is None:
        raise HTTPException(status_code=404, detail="Exam not found")
    return exam

@router.post("/", response_model=ExamResponse)
def create_exam(exam: ExamCreate, db: Session = Depends(get_db)):
    return service.create_exam(db, exam)

@router.put("/{exam_id}", response_model=ExamResponse)
def update_exam(exam_id: int, exam: ExamUpdate, db: Session = Depends(get_db)):
    updated_exam = service.update_exam(db, exam_id, exam)
    if updated_exam is None:
        raise HTTPException(status_code=404, detail="Exam not found")
    return updated_exam

@router.delete("/{exam_id}", response_model=ExamResponse)
def delete_exam(exam_id: int, db: Session = Depends(get_db)):
    deleted_exam = service.delete_exam(db, exam_id)
    if deleted_exam is None:
        raise HTTPException(status_code=404, detail="Exam not found")
    return deleted_exam
