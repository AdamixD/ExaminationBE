from sqlalchemy.orm import Session
from models.exam import Exam
from schemas.exam import ExamCreate, ExamUpdate

def get_all_exams(db: Session):
    return db.query(Exam).all()

def get_exam(db: Session, exam_id: int):
    return db.query(Exam).filter(Exam.id == exam_id).first()

def create_exam(db: Session, exam: ExamCreate):
    db_exam = Exam(
        start_date=exam.start_date,
        end_date=exam.end_date,
        duration_limit=exam.duration_limit,
        status=exam.status,
        course_realization_id=exam.course_realization_id
    )
    db.add(db_exam)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def update_exam(db: Session, exam_id: int, exam: ExamUpdate):
    db_exam = get_exam(db, exam_id)
    if not db_exam:
        return None
    for key, value in exam.dict(exclude_unset=True).items():
        setattr(db_exam, key, value)
    db.commit()
    db.refresh(db_exam)
    return db_exam

def delete_exam(db: Session, exam_id: int):
    db_exam = get_exam(db, exam_id)
    if db_exam:
        db.delete(db_exam)
        db.commit()
    return db_exam
