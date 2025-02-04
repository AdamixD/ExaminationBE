# grading.py
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging
from models import ExamStudent, Question, QuestionResult, QuestionItem, Exam
from models.associations import exam_student_question_association
from database.session import DATABASE_URL  # Import DATABASE_URL from your config
from models.question import QuestionScoreType

logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)


def grade_exam(exam_id):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Fetch all exam students for the closed exam
        exam_students = session.query(ExamStudent).filter_by(exam_id=exam_id).all()
        exam_query = session.query(Exam).filter_by(id=exam_id).one()
        max_exam_score = exam_query.max_points
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
            logger.info(f"No closed questions found for exam {exam_id}.")
            return

        # Preload question items for all closed questions
        question_items = {}
        for q in questions:
            items = session.query(QuestionItem).filter(
                QuestionItem.question_id == q.id
            ).order_by(QuestionItem.id).all()
            question_items[q.id] = [item.correctness for item in items]

        # Process each student
        for student in exam_students:
            # check max score for student
            stmt = select(exam_student_question_association.c.question_id).where(
                exam_student_question_association.c.exam_student_id == student.id
            )
            students_questions = session.execute(stmt).scalars().all()

            student_max_score = sum(
                sum(item.score for item in session.query(Question.score)
                    .filter(Question.id == q)
                    .all())
                for q in students_questions
            )

            # student_max_score = sum(students_questions)
            print(student_max_score)
            # print(student_max_score)

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
                max_task_score = sum(correctness)
                if q.score_type == QuestionScoreType.FULL:
                    points = max_task_score
                    for ans_char, correct in zip(ans_str, correctness):
                        student_ans = 1 if ans_char == 'T' else 0
                        if student_ans != correct:
                            points = 0
                            break
                elif q.score_type == QuestionScoreType.PROPORTIONAL:
                    points = 0
                    for ans_char, correct in zip(ans_str, correctness):
                        student_ans = 1 if ans_char == 'T' else 0
                        if student_ans == correct == 1:
                            points += 1
                        elif student_ans != correct:
                            points -= 1
                else:
                    points = 0
                    logger.warning(f"Unknown score_type: {q.score_type}")

                # Calculate normalized score
                q_score = (max(0, points) / max_task_score) * q.score if max_task_score > 0 else 0

                # Find the specific QuestionResult for this question and student
                for res in results:
                    if res.answer.startswith(f"{q.id}: "):
                        res.score = q_score
                        session.add(res)
                        break

                total_score += q_score

            # Update student's total score
            student.score = total_score / student_max_score * max_exam_score if max_exam_score > 0 else 0
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