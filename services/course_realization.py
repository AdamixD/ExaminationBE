from sqlalchemy.orm import Session, joinedload
from models.course_realization import CourseRealization
from schemas.course_realization import CourseRealizationCreate, CourseRealizationUpdate
from typing import Union


def get_all_course_realizations(db: Session):
    """
    Retrieve all course realizations.
    """
    return db.query(CourseRealization).options(
        joinedload(CourseRealization.course),
        joinedload(CourseRealization.lecturer)
    ).all()


def get_course_realization(db: Session, course_realization_id: int):
    """
    Retrieve a single course realization by ID with related course and lecturer data.
    """
    return db.query(CourseRealization).options(
        joinedload(CourseRealization.course),
        joinedload(CourseRealization.lecturer)
    ).filter(CourseRealization.id == course_realization_id).first()


def get_lecturer_course_realizations(db: Session, lecturer_id: int):
    return db.query(CourseRealization).filter(CourseRealization.lecturer_id == lecturer_id).all()


def get_student_course_realizations(db: Session, student_id: int):
    return (
        db.query(CourseRealization)
        .join(CourseRealization.students)
        .filter(CourseRealization.students.any(id=student_id))
        .all()
    )


def create_course_realization(db: Session, course_realization: CourseRealizationCreate):
    """
    Create a new course realization.
    """
    db_course_realization = CourseRealization(
        semester=course_realization.semester,
        course_id=course_realization.course_id,
        lecturer_id=course_realization.lecturer_id
    )
    db.add(db_course_realization)
    db.commit()
    db.refresh(db_course_realization)
    return db_course_realization


def update_course_realization(
    db: Session, course_realization_id: int, course_realization: CourseRealizationUpdate
):
    """
    Update an existing course realization.
    """
    db_course_realization = get_course_realization(db, course_realization_id)
    if not db_course_realization:
        return None
    for key, value in course_realization.dict(exclude_unset=True).items():
        setattr(db_course_realization, key, value)
    db.commit()
    db.refresh(db_course_realization)
    return db_course_realization


def delete_course_realization(db: Session, course_realization_id: int) -> Union[CourseRealization, None]:
    """
    Delete a course realization by ID.
    """
    db_course_realization = get_course_realization(db, course_realization_id)
    if db_course_realization:
        db.delete(db_course_realization)
        db.commit()
    return db_course_realization