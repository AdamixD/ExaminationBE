# grading.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging
from models import ExamStudent, Question, QuestionResult, QuestionItem
from database.session import DATABASE_URL  # Import DATABASE_URL from your config

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def grade_exam(exam_id):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Fetch all exam students for the closed exam
        exam_students = session.query(ExamStudent).filter_by(exam_id=exam_id).all()
        if not exam_students:
            logger.info(f"No students found for exam {exam_id}.")
            return

        # Fetch all questions for the exam (MULTI and SINGLE)
        questions = session.query(Question).filter(
            Question.exam_id == exam_id,
            Question.type.in_(['MULTI', 'SINGLE'])
        ).all()
        question_ids = [q.id for q in questions]

        if not questions:
            logger.info(f"No questions found for exam {exam_id}.")
            return

        # Preload question items for all questions
        question_items = {}
        for q in questions:
            items = session.query(QuestionItem).filter(
                QuestionItem.question_id == q.id
            ).order_by(QuestionItem.id).all()
            question_items[q.id] = [item.correctness for item in items]

        # Process each student
        for student in exam_students:
            total_score = 0.0
            results = session.query(QuestionResult).filter_by(
                exam_student_id=student.id
            ).all()

            # Parse answers into {question_id: answer_str}
            qr_dict = {}
            for res in results:
                if not res.answer:
                    continue

                try:
                    # Extract question ID from answer string
                    q_id_str, ans_str = res.answer.split(': ', 1)
                    q_id = int(q_id_str.strip())
                except (ValueError, AttributeError) as e:
                    logger.warning(f"Invalid answer format for result {res.id}: {res.answer} - {str(e)}")
                    continue

                # Skip if question doesn't belong to this exam
                if q_id not in question_ids:
                    continue

                qr_dict[q_id] = ans_str.strip().upper()

            # Calculate score per question
            # Calculate score per question
            for q in questions:
                if q.id not in qr_dict:
                    continue  # Student didn't answer this question

                ans_str = qr_dict[q.id]
                correctness = question_items.get(q.id, [])

                # Validate answer length matches number of items
                if len(ans_str) != len(correctness):
                    logger.warning(f"Answer length mismatch for Q{q.id}, Student {student.id}")
                    continue

                # Calculate points
                points = 0
                for ans_char, correct in zip(ans_str, correctness):
                    student_ans = 1 if ans_char == 'T' else 0
                    if student_ans == correct == 1:
                        points += 1
                    elif student_ans != correct:
                        points -= 1

                # Calculate normalized score (ensure non-negative)
                total_correct = sum(correctness)
                q_score = (max(0, points) / total_correct) * q.score if total_correct > 0 else 0

                # Find the specific QuestionResult for this question and student
                for res in results:
                    if res.answer.startswith(f"{q.id}: "):  # Match the question ID in the answer
                        res.score = q_score
                        session.add(res)
                        break

                total_score += q_score

            # Update student's total score
            student.score = total_score
            session.add(student)

        session.commit()
        logger.info(f"Graded exam {exam_id} successfully.")

    except SQLAlchemyError as e:
        logger.error(f"Database error grading exam {exam_id}: {e}")
        session.rollback()
    except Exception as e:
        logger.error(f"Unexpected error grading exam {exam_id}: {e}")
        session.rollback()
    finally:
        session.close()