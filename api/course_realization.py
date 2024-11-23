from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

import services.course_realization as service

from database.session import get_db
from schemas.course_realization import CourseRealizationCreate, CourseRealizationResponse, CourseRealizationUpdate

router = APIRouter(prefix="/course_realizations", tags=["course_realizations"])

@router.get("/all", response_model=List[CourseRealizationResponse])
def get_all_course_realizations(db: Session = Depends(get_db)):
    return service.get_all_course_realizations(db=db)

@router.get("/{course_realization_id}", response_model=CourseRealizationResponse)
def get_course_realization(course_realization_id: int, db: Session = Depends(get_db)):
    course_realization = service.get_course_realization(db, course_realization_id)
    if course_realization is None:
        raise HTTPException(status_code=404, detail="Course Realization not found")
    return course_realization

@router.post("/", response_model=CourseRealizationResponse)
def create_course_realization(course_realization: CourseRealizationCreate, db: Session = Depends(get_db)):
    return service.create_course_realization(db, course_realization)

@router.put("/{course_realization_id}", response_model=CourseRealizationResponse)
def update_course_realization(course_realization_id: int, course_realization: CourseRealizationUpdate, db: Session = Depends(get_db)):
    updated_course_realization = service.update_course_realization(db, course_realization_id, course_realization)
    if updated_course_realization is None:
        raise HTTPException(status_code=404, detail="Course Realization not found")
    return updated_course_realization

@router.delete("/{course_realization_id}", response_model=CourseRealizationResponse)
def delete_course_realization(course_realization_id: int, db: Session = Depends(get_db)):
    deleted_course_realization = service.delete_course_realization(db, course_realization_id)
    if deleted_course_realization is None:
        raise HTTPException(status_code=404, detail="Course Realization not found")
    return deleted_course_realization
