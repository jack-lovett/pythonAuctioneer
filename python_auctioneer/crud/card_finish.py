from sqlalchemy.orm import Session
from python_auctioneer.models.card_finish import CardFinish


def get_card_finish(database: Session, finish_id: int):
    return database.query(CardFinish).filter(CardFinish.finish_id == finish_id).first()


def get_card_finishes(database: Session, skip: int = 0, limit: int = 10):
    return database.query(CardFinish).offset(skip).limit(limit).all()


def create_card_finish(database: Session, finish_data):
    database_finish = CardFinish(**finish_data)
    database.add(database_finish)
    database.commit()
    database.refresh(database_finish)
    return database_finish


def update_card_finish(database: Session, finish_id: int, finish_data):
    database_finish = CardFinish(**finish_data)
    if database_finish:
        for key, value in finish_data.items():
            setattr(database_finish, key, value)
        database.commit()
        database.refresh(database_finish)
    return database_finish


def delete_card_finish(database: Session, finish_id: int):
    database_finish = get_card_finish(database, finish_id)
    if database_finish:
        database.delete(database_finish)
        database.commit()
    return database_finish
