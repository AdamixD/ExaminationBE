from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import services.exam_student as service

from database.session import get_db
from schemas.exam_student import ExamStudentCreate, ExamStudentResponse, ExamStudentUpdate, ExamStudentExamResponse

router = APIRouter(prefix="/exam_students", tags=["exam_students"])


@router.get("/all", response_model=List[ExamStudentResponse])
def get_all_exam_students(db: Session = Depends(get_db)):
    return service.get_all_exam_students(db=db)


@router.get("/{exam_student_id}", response_model=ExamStudentResponse)
def get_exam_student(exam_student_id: int, db: Session = Depends(get_db)):
    exam_student = service.get_exam_student(db, exam_student_id)
    if exam_student is None:
        raise HTTPException(status_code=404, detail="Exam Student not found")
    return exam_student


@router.get("/exam/all/{exam_id}", response_model=List[ExamStudentExamResponse])
def get_all_exam_students_exam(exam_id: int, db: Session = Depends(get_db)):
    return service.get_all_exam_students_exam(db, exam_id)


@router.get("/ids/{exam_id}/{student_id}", response_model=ExamStudentExamResponse)
def get_exam_student(exam_id: int, student_id: int, db: Session = Depends(get_db)):
    exam_student = service.get_exam_student_by_ids(db, exam_id, student_id)
    if exam_student is None:
        raise HTTPException(status_code=404, detail="Exam Student not found")
    return exam_student


@router.post("/", response_model=ExamStudentResponse)
def create_exam_student(exam_student: ExamStudentCreate, db: Session = Depends(get_db)):
    return service.create_exam_student(db, exam_student)


@router.put("/{exam_student_id}", response_model=ExamStudentResponse)
def update_exam_student(exam_student_id: int, exam_student: ExamStudentUpdate, db: Session = Depends(get_db)):
    updated_exam_student = service.update_exam_student(db, exam_student_id, exam_student)
    if updated_exam_student is None:
        raise HTTPException(status_code=404, detail="Exam Student not found")
    return updated_exam_student


@router.delete("/{exam_student_id}", response_model=ExamStudentResponse)
def delete_exam_student(exam_student_id: int, db: Session = Depends(get_db)):
    deleted_exam_student = service.delete_exam_student(db, exam_student_id)
    if deleted_exam_student is None:
        raise HTTPException(status_code=404, detail="Exam Student not found")
    return deleted_exam_student
