from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import services.exam as service

from auth.auth import get_authorized_user
from database.session import get_db
from models.user import Role
from schemas.exam import ExamCreate, ExamResponse, ExamUpdate

router = APIRouter(prefix="/exams", tags=["exams"])


@router.get("/user/{course_realization_id}", response_model=List[ExamResponse])
def get_user_exams_auth(
    course_realization_id: int,
    user=Depends(get_authorized_user),
    db: Session = Depends(get_db),
):
    if user.role == Role.LECTURER:
        courses = service.get_lecturer_exams(db=db, course_realization_id=course_realization_id)
    elif user.role == Role.STUDENT:
        courses = service.get_student_exams(db=db, course_realization_id=course_realization_id, student_id=user.id)
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Unauthorized role")
    return courses


@router.get("/all", response_model=List[ExamResponse])
def get_all_exams(db: Session = Depends(get_db)):
    return service.get_all_exams(db=db)


@router.get("/all/{course_realization_id}", response_model=List[ExamResponse])
def get_all_course_realization_exams(course_realization_id: int, db: Session = Depends(get_db)):
    return service.get_all_course_realization_exams(db=db, course_realization_id=course_realization_id)


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


@router.post("/assign/{exam_id}", response_model=ExamResponse)
def assign_exam_to_students(exam_id: int, db: Session = Depends(get_db)):
    try:
        db_exam = service.assign_exam(db, exam_id)
        return db_exam
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)


@router.post("/{exam_id}/grading_method", response_model=ExamResponse)
def set_grading_method(exam_id: int, grading_method: str, db: Session = Depends(get_db)):
    """
    Endpoint to set the grading method for a specific exam.
    """
    try:
        return service.set_grading_method(db, exam_id, grading_method)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))