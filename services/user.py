from sqlalchemy.orm import Session

from auth.auth import get_password_hash
from models.user import User, Role
from models.student import Student
from models.lecturer import Lecturer
from schemas.user import UserCreate, UserUpdate


def get_all_users(db: Session):
    """
    Fetch all users from the database.
    """
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    """
    Fetch a user by their ID.
    """
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Fetch a user by their email.
    """
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    """
    Create a new user (student or lecturer) based on their role.
    """
    if user.role == Role.STUDENT:
        if not user.index:
            raise ValueError("Student must have an index number.")
        db_user = Student(
            name=user.name,
            surname=user.surname,
            email=user.email,
            password=get_password_hash(user.password),
            role=user.role,
            index=user.index
        )
    elif user.role == Role.LECTURER:
        db_user = Lecturer(
            name=user.name,
            surname=user.surname,
            email=user.email,
            password=get_password_hash(user.password),
            role=user.role,
        )
    else:
        raise ValueError("Invalid role provided. Must be 'STUDENT' or 'LECTURER'.")

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserUpdate):
    """
    Update a user's details.
    """
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    """
    Delete a user by their ID.
    """
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user


def get_users_by_role(db: Session, role: Role):
    """
    Fetch all users with a specific role (LECTURER or STUDENT).
    """
    return db.query(User).filter(User.role == role).all()


def execute_action_based_on_role(db: Session, user_id: int, role: Role, action: str):
    """
    Perform specific actions based on the user's role.
    """
    if role == Role.STUDENT:
        # Implement actions specific to students
        student = db.query(Student).filter(Student.id == user_id).first()
        if not student:
            raise ValueError("Student not found.")
        return f"Performed '{action}' for student {student.name} {student.surname}"
    elif role == Role.LECTURER:
        # Implement actions specific to lecturers
        lecturer = db.query(Lecturer).filter(Lecturer.id == user_id).first()
        if not lecturer:
            raise ValueError("Lecturer not found.")
        return f"Performed '{action}' for lecturer {lecturer.name} {lecturer.surname}"
    else:
        raise ValueError("Invalid role.")