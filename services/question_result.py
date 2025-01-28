from sqlalchemy.orm import Session
from models.question_result import QuestionResult
from models.question import Question, QuestionItem
from models.exam import Exam
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
        exam_student_id=question_result.exam_student_id,
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


def calculate_exam_result(db: Session, exam_id: int, student_answers: dict):
    """
    Calculate the exam result based on the grading method.

    :param db: Database session
    :param exam_id: ID of the exam
    :param student_answers: A dictionary mapping question IDs to selected answers
    :return: Total score for the student
    """
    exam = db.query(Exam).filter(Exam.id == exam_id).first()
    if not exam:
        raise ValueError("Exam not found")

    if exam.grading_method == "negative_marking":
        total_score = 0
        for question_id, selected_answers in student_answers.items():
            question = db.query(Question).filter(Question.id == question_id).first()
            correct_answers = {
                item.id for item in question.question_items if item.correctness
            }
            selected_answers = set(selected_answers)

            # Calculate score
            correct_selected = correct_answers.intersection(selected_answers)
            incorrect_selected = selected_answers - correct_answers

            total_score += len(correct_selected) - len(incorrect_selected)
        return max(total_score, 0)
    else:
        raise ValueError("Unsupported grading method")