from sqlalchemy.orm import Session
from models.question import Question
from schemas.question import QuestionCreate, QuestionUpdate


def get_all_questions(db: Session):
    return db.query(Question).all()


def get_all_exam_questions(db: Session, exam_id: int):
    return db.query(Question).filter(Question.exam_id == exam_id).all()


def get_question(db: Session, question_id: int):
    return db.query(Question).filter(Question.id == question_id).first()


def create_question(db: Session, question: QuestionCreate):
    db_question = Question(
        text=question.text,
        image=question.image,
        type=question.type,
        score=question.score,
        score_type=question.score_type,
        exam_id=question.exam_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def update_question(db: Session, question_id: int, question: QuestionUpdate):
    db_question = get_question(db, question_id)
    if not db_question:
        return None
    for key, value in question.dict(exclude_unset=True).items():
        setattr(db_question, key, value)
    db.commit()
    db.refresh(db_question)
    return db_question


def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)
    if db_question:
        db.delete(db_question)
        db.commit()
    return db_question
