from sqlalchemy.exc import IntegrityError
from python_auctioneer.models.card_finish import CardFinish

def get_card_finish_service(database, finish_id):
    return database.query(CardFinish).filter(CardFinish.finish_id == finish_id).first()