from python_auctioneer.models.card_condition import CardCondition


def get_card_condition_service(database, condition_id):
    return database.query(CardCondition).filter(CardCondition.condition_id == condition_id).first()


def create_card_condition_service(database, condition_data):
    try:
        database_condition = CardCondition(**condition_data)
        database.add(database_condition)
        database.commit()
        database.refresh(database_condition)
        return database_condition
    except Exception as e:
        database.rollback()
        raise ValueError(f"Error adding card finishes: {e}")
