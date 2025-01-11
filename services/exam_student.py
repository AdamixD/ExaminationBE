from sqlalchemy.orm import Session
from models.exam_student import ExamStudent
from schemas.exam_student import ExamStudentCreate, ExamStudentUpdate

def get_all_exam_students(db: Session):
    return db.query(ExamStudent).all()

def get_exam_student(db: Session, exam_student_id: int):
    return db.query(ExamStudent).filter(ExamStudent.id == exam_student_id).first()

def get_all_exam_students_exam(db: Session, exam_id: int):
    return db.query(ExamStudent).filter(ExamStudent.exam_id == exam_id)

def get_exam_student_by_ids(db: Session, exam_id: int, student_id: int):
    return (db.query(ExamStudent).filter(ExamStudent.exam_id == exam_id)
                                 .filter(ExamStudent.student_id == student_id).first())

def create_exam_student(db: Session, exam_student: ExamStudentCreate):
    db_exam_student = ExamStudent(
        score=exam_student.score,
        status=exam_student.status,
        start_date=exam_student.start_date,
        end_date=exam_student.end_date,
        duration=exam_student.duration,
        exam_id=exam_student.exam_id,
        student_id=exam_student.student_id
    )
    db.add(db_exam_student)
    db.commit()
    db.refresh(db_exam_student)
    return db_exam_student

def update_exam_student(db: Session, exam_student_id: int, exam_student: ExamStudentUpdate):
    db_exam_student = get_exam_student(db, exam_student_id)
    if not db_exam_student:
        return None
    for key, value in exam_student.dict(exclude_unset=True).items():
        setattr(db_exam_student, key, value)
    db.commit()
    db.refresh(db_exam_student)
    return db_exam_student

def delete_exam_student(db: Session, exam_student_id: int):
    db_exam_student = get_exam_student(db, exam_student_id)
    if db_exam_student:
        db.delete(db_exam_student)
        db.commit()
    return db_exam_student
