import random

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from models.exam import Exam
from models.exam_student import ExamStudent
from models.question import Question
from schemas.exam import ExamCreate, ExamUpdate
from schemas.exam_student import ExamStudentCreate


def get_lecturer_exams(db: Session, course_realization_id: int):
    return db.query(Exam).filter(Exam.course_realization_id == course_realization_id).all()


def get_student_exams(db: Session, course_realization_id: int, student_id: int):
    return db.query(Exam).filter(Exam.course_realization_id == course_realization_id).all()


def get_all_exams(db: Session):
    return db.query(Exam).all()


def get_all_course_realization_exams(db: Session, course_realization_id: int):
    return db.query(Exam).filter(Exam.course_realization_id == course_realization_id).all()


def get_exam(db: Session, exam_id: int):
    return db.query(Exam).filter(Exam.id == exam_id).first()


def create_exam(db: Session, exam: ExamCreate):
    db_exam = Exam(
        title=exam.title,
        start_date=exam.start_date,
        end_date=exam.end_date,
        duration_limit=exam.duration_limit,
        status=exam.status,
        course_realization_id=exam.course_realization_id,
        questions_quantity=exam.questions_quantity,
        max_points=exam.max_points,
        type=exam.type,
        grading_method=exam.grading_method,
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


def assign_exam(db: Session, exam_id: int):
    db_exam = db.query(Exam).filter(Exam.id == exam_id).first()

    if db_exam is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exam not found")

    if len(db_exam.questions) < db_exam.questions_quantity:
        raise HTTPException(status_code=400, detail="Not enough questions available to assign")

    existing_exam_students = db.query(ExamStudent).filter(ExamStudent.exam_id == exam_id).all()
    for exam_student in existing_exam_students:
        db.delete(exam_student)
    db.commit()

    db_students = db_exam.course_realization.students

    for student in db_students:
        exam_student = ExamStudent(
            exam_id=db_exam.id,
            student_id=student.id,
            score=None,
            status="SCHEDULED",
            start_date=None,
            end_date=None,
            duration=None,
        )
        db.add(exam_student)
        db.commit()
        db.refresh(exam_student)

        db_questions = random.sample(db_exam.questions, db_exam.questions_quantity)

        for question in db_questions:
            exam_student.questions.append(question)

    db_exam.status = "ASSIGNED"
    db.commit()

    return db_exam


def set_grading_method(db: Session, exam_id: int, grading_method: str):
    """
    Assign a grading method to an exam.
    """
    db_exam = get_exam(db, exam_id)
    if not db_exam:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Exam not found")
    db_exam.grading_method = grading_method
    db.commit()
    db.refresh(db_exam)
    return db_exam