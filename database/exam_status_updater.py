from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base

from database.session import DATABASE_URL


Base = declarative_base()
class Exam(Base):
    __tablename__ = 'exams'
    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    status = Column(String)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def update_exam_status():
    try:
        current_time = datetime.now()

        # change to ACTIVE
        assigned_exams = session.query(Exam).filter(
            Exam.status == 'ASSIGNED',
            Exam.start_date <= current_time
        ).all()
        for exam in assigned_exams:
            exam.status = 'ACTIVE'
            print(f"LOG: Updated exam {exam.id} to ACTIVE")

        # change to CLOSED
        active_exams = session.query(Exam).filter(
            Exam.status == 'ACTIVE',
            Exam.end_date <= current_time
        ).all()
        for exam in active_exams:
            exam.status = 'CLOSED'
            print(f"LOG: Updated exam {exam.id} to CLOSED")
        session.commit()

    except Exception as e:
        print(f"WARN: Error while updating exam statuses: {e}\nRolling back.")
        session.rollback()


def run_update_exam_status_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_exam_status, CronTrigger(minute="*"))  # Run every minute
    scheduler.start()
