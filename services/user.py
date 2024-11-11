from sqlalchemy.orm import Session

from auth.auth import get_password_hash
from models.user import User, Role
from models.student import Student
from models.lecturer import Lecturer
from schemas.user import UserCreate, UserUpdate


def get_all_users(db: Session):
    return db.query(User).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    if user.role == Role.STUDENT:
        if not user.index:
            raise ValueError("Student must have an index number")
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
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
