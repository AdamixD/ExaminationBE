from sqlalchemy.orm import Session

from models.course import Course
from schemas.course import CourseCreate, CourseUpdate


def get_all_courses(db: Session):
    return db.query(Course).all()


def get_course(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()


def create_course(db: Session, course: CourseCreate):
    db_course = Course(
        title=course.title,
        shortcut=course.shortcut,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


def update_course(db: Session, course_id: int, course: CourseUpdate):
    db_course = get_course(db, course_id)
    if not db_course:
        return None
    for key, value in course.dict(exclude_unset=True).items():
        setattr(db_course, key, value)
    db.commit()
    db.refresh(db_course)
    return db_course


def delete_course(db: Session, course_id: int):
    db_course = get_course(db, course_id)
    if db_course:
        db.delete(db_course)
        db.commit()
    return db_course
