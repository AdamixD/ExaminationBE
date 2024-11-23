from sqlalchemy.orm import Session
from models.question_result import QuestionResult
from schemas.question_result import QuestionResultCreate, QuestionResultUpdate

def get_all_question_results(db: Session):
    return db.query(QuestionResult).all()

def get_question_result(db: Session, question_result_id: int):
    return db.query(QuestionResult).filter(QuestionResult.id == question_result_id).first()

def create_question_result(db: Session, question_result: QuestionResultCreate):
    db_question_result = QuestionResult(
        score=question_result.score,
        comment=question_result.comment,
        answer=question_result.answer,
        exam_student_id=question_result.exam_student_id
    )
    db.add(db_question_result)
    db.commit()
    db.refresh(db_question_result)
    return db_question_result

def update_question_result(db: Session, question_result_id: int, question_result: QuestionResultUpdate):
    db_question_result = get_question_result(db, question_result_id)
    if not db_question_result:
        return None
    for key, value in question_result.dict(exclude_unset=True).items():
        setattr(db_question_result, key, value)
    db.commit()
    db.refresh(db_question_result)
    return db_question_result

def delete_question_result(db: Session, question_result_id: int):
    db_question_result = get_question_result(db, question_result_id)
    if db_question_result:
        db.delete(db_question_result)
        db.commit()
    return db_question_result
