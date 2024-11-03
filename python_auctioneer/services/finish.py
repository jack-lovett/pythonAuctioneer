from sqlalchemy.exc import IntegrityError
from python_auctioneer.models.finish import Finish

def get_card_finish_service(database, finish_id):
    return database.query(Finish).filter(Finish.finish_id == finish_id).first()

def create_card_finish_service(database, card_finish_data):
    try:
        database_card_finish = Finish(**card_finish_data)
        database.add(database_card_finish)
        database.commit()
        database.refresh(database_card_finish)
        return database_card_finish
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error adding card finishes: {e}")