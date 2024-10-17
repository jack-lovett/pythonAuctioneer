from python_auctioneer.models.card_condition import CardCondition

def get_card_condition_service(database, condition_id):
    return database.query(CardCondition).filter(CardCondition.condition_id == condition_id).first()