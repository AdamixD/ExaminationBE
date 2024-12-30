from sqlalchemy import Table, Column, Integer, ForeignKey

from database.base import Base

student_course_realization_association = Table(
    'students_course_realizations', Base.metadata,
    Column('student_id', Integer, ForeignKey('users.id'), primary_key=True, index=True),
    Column('course_realization_id', Integer, ForeignKey('course_realizations.id'), primary_key=True, index=True)
)

exam_student_question_association = Table(
    'exam_students_questions', Base.metadata,
    Column('exam_student_id', Integer, ForeignKey('exam_students.id'), primary_key=True, index=True),
    Column('question_id', Integer, ForeignKey('questions.id'), primary_key=True, index=True)
)

question_result_item_association = Table(
    'questions_result_items', Base.metadata,
    Column('question_result_id', Integer, ForeignKey('question_results.id'), primary_key=True, index=True),
    Column('question_item_id', Integer, ForeignKey('question_items.id'), primary_key=True, index=True)
)
