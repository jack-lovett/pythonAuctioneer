from sqlalchemy.exc import IntegrityError
from python_auctioneer.models.order import Order


def create_order_service(database, order_data):
    """Create new order."""
    try:
        new_order = Order(**order_data)
        database.add(new_order)
        database.commit()
        database.refresh(new_order)
        return new_order
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error creating order: {e}")