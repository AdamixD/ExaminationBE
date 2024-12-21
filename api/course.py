from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

import services.course as service

from database.session import get_db
from schemas.course import CourseCreate, CourseResponse, CourseUpdate

router = APIRouter(prefix="/courses", tags=["courses"])


@router.get("/all", response_model=List[CourseResponse])
def get_all_courses(db: Session = Depends(get_db)):
    return service.get_all_courses(db=db)


@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = service.get_course(db, course_id)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.post("/", response_model=CourseResponse)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    return service.create_course(db, course)


@router.put("/{course_id}", response_model=CourseResponse)
def update_course(course_id: int, course: CourseUpdate, db: Session = Depends(get_db)):
    updated_course = service.update_course(db, course_id, course)
    if updated_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return updated_course


@router.delete("/{course_id}", response_model=CourseResponse)
def delete_course(course_id: int, db: Session = Depends(get_db)):
    deleted_course = service.delete_course(db, course_id)
    if deleted_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return deleted_course
