from sqlalchemy.orm import Session
from python_auctioneer.models.card import Card


def get_card(database: Session, card_id: int):
    return database.query(Card).filter(Card.card_id == card_id).first()


def get_cards(database: Session, skip: int = 0, limit: int = 10):
    return database.query(Card).offset(skip).limit(limit).all()


def create_card(database: Session, card_data):
    database_card = Card(**card_data)
    database.add(database_card)
    database.commit()
    database.refresh(database_card)
    return database_card


def update_card(database: Session, card_id: int, card_data):
    database_card = get_card(database, card_id)
    if database_card:
        for key, value in card_data.items():
            setattr(database_card, key, value)
        database.commit()
        database.refresh(database_card)
    return database_card


def delete_card(database: Session, card_id: int):
    database_card = get_card(database, card_id)
    if database_card:
        database.delete(database_card)
        database.commit()
    return database_card
