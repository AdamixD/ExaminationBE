from sqlalchemy.orm import Session
from models.course_realization import CourseRealization
from schemas.course_realization import CourseRealizationCreate, CourseRealizationUpdate

def get_all_course_realizations(db: Session):
    return db.query(CourseRealization).all()

def get_course_realization(db: Session, course_realization_id: int):
    return db.query(CourseRealization).filter(CourseRealization.id == course_realization_id).first()

def create_course_realization(db: Session, course_realization: CourseRealizationCreate):
    db_course_realization = CourseRealization(
        semester=course_realization.semester,
        course_id=course_realization.course_id,
        lecturer_id=course_realization.lecturer_id
    )
    db.add(db_course_realization)
    db.commit()
    db.refresh(db_course_realization)
    return db_course_realization

def update_course_realization(db: Session, course_realization_id: int, course_realization: CourseRealizationUpdate):
    db_course_realization = get_course_realization(db, course_realization_id)
    if not db_course_realization:
        return None
    for key, value in course_realization.dict(exclude_unset=True).items():
        setattr(db_course_realization, key, value)
    db.commit()
    db.refresh(db_course_realization)
    return db_course_realization

def delete_course_realization(db: Session, course_realization_id: int):
    db_course_realization = get_course_realization(db, course_realization_id)
    if db_course_realization:
        db.delete(db_course_realization)
        db.commit()
    return db_course_realization
