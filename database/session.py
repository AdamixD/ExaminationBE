from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from database.base import Base


DATABASE_URL = "mysql+mysqlconnector://root:password@localhost/examination"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
