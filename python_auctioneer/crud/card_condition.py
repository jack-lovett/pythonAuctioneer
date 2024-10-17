from sqlalchemy.orm import Session
from python_auctioneer.models.card_condition import CardCondition


def get_card_condition(database: Session, condition_id: int):
    return database.query(CardCondition).filter(CardCondition.condition_id == condition_id).first()


def get_card_conditions(database: Session, skip: int = 0, limit: int = 10):
    return database.query(CardCondition).offset(skip).limit(limit).all()


def create_card_condition(database: Session, condition_data):
    database_condition = CardCondition(**condition_data)
    database.add(database_condition)
    database.commit()
    database.refresh(database_condition)
    return database_condition


def update_card_condition(database: Session, condition_id: int, condition_data):
    database_condition = get_card_condition(database, condition_id)
    if database_condition:
        for key, value in condition_data.items():
            setattr(database_condition, key, value)
        database.commit()
        database.refresh(database_condition)
    return database_condition


def delete_card_condition(database: Session, condition_id: int):
    database_condition = get_card_condition(database, condition_id)
    if database_condition:
        database.delete(database_condition)
        database.commit()
    return database_condition
