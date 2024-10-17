from sqlalchemy.exc import IntegrityError
from python_auctioneer.models.shipping_method import ShippingMethod

def add_shipping_method_service(database, shipping_method_data):
    try:
        database_shipping_method = ShippingMethod(**shipping_method_data)
        database.add(database_shipping_method)
        database.commit()
        database.refresh(database_shipping_method)
        return database_shipping_method
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error adding shipping method: {e}")