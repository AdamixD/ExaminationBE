from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from models import Exam, ExamStudent, Question, QuestionResult, QuestionItem

from database.grading import grade_exam
from database.session import DATABASE_URL





def update_exam_status():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        current_time = datetime.now()

        # Update ASSIGNED to ACTIVE
        assigned_exams = session.query(Exam).filter(
            Exam.status == 'ASSIGNED',
            Exam.start_date <= current_time
        ).all()
        for exam in assigned_exams:
            exam.status = 'ACTIVE'
            print(f"LOG: Updated exam {exam.id} to ACTIVE")

        # Update ACTIVE to CLOSED and collect IDs
        active_exams = session.query(Exam).filter(
            Exam.status == 'ACTIVE',
            Exam.end_date <= current_time
        ).all()
        closed_exam_ids = [exam.id for exam in active_exams]
        for exam in active_exams:
            exam.status = 'CLOSED'
            # Update all related ExamStudent statuses
            exam_students = session.query(ExamStudent).filter_by(
                exam_id=exam.id
            ).all()
            for exam_2 in exam_students:
                exam_2.status = 'CLOSED'
                print(f"LOG: Updated ExamStudent {exam_2.id} to CLOSED")
            print(f"LOG: Updated exam {exam.id} to CLOSED")

        session.commit()

        # Grade each closed exam
        for exam_id in closed_exam_ids:
            grade_exam(exam_id)

    except Exception as e:
        print(f"WARN: Error while updating exam statuses: {e}\nRolling back.")
        session.rollback()
    finally:
        session.close()


def run_update_exam_status_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_exam_status, CronTrigger(minute="*"))  # Run every minute
    scheduler.start()
