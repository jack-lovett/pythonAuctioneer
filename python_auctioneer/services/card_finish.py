from sqlalchemy.exc import IntegrityError
from python_auctioneer.models.card_finish import CardFinish

def get_card_finish_service(database, finish_name):
    return database.query(CardFinish).filter(CardFinish.finish_name == finish_name).first()

def create_card_finish_service(database, card_finish_data):
    try:
        database_card_finish = CardFinish(**card_finish_data)
        database.add(database_card_finish)
        database.commit()
        database.refresh(database_card_finish)
        return database_card_finish
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error adding card finishes: {e}")