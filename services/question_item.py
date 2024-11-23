from sqlalchemy.orm import Session
from models.question_item import QuestionItem
from schemas.question_item import QuestionItemCreate, QuestionItemUpdate

def get_all_question_items(db: Session):
    return db.query(QuestionItem).all()

def get_question_item(db: Session, question_item_id: int):
    return db.query(QuestionItem).filter(QuestionItem.id == question_item_id).first()

def create_question_item(db: Session, question_item: QuestionItemCreate):
    db_question_item = QuestionItem(
        text=question_item.text,
        image=question_item.image,
        correctness=question_item.correctness,
        question_id=question_item.question_id
    )
    db.add(db_question_item)
    db.commit()
    db.refresh(db_question_item)
    return db_question_item

def update_question_item(db: Session, question_item_id: int, question_item: QuestionItemUpdate):
    db_question_item = get_question_item(db, question_item_id)
    if not db_question_item:
        return None
    for key, value in question_item.dict(exclude_unset=True).items():
        setattr(db_question_item, key, value)
    db.commit()
    db.refresh(db_question_item)
    return db_question_item

def delete_question_item(db: Session, question_item_id: int):
    db_question_item = get_question_item(db, question_item_id)
    if db_question_item:
        db.delete(db_question_item)
        db.commit()
    return db_question_item
