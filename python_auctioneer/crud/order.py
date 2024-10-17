from sqlalchemy.orm import Session
from python_auctioneer.models.order import Order


def get_order(database: Session, order_id: int):
    return database.query(Order).filter(Order.order_id == order_id).first()


def get_orders(database: Session, skip: int = 0, limit: int = 10):
    return database.query(Order).offset(skip).limit(limit).all()


def create_order(database: Session, order_data):
    database_order = Order(**order_data)
    database.add(database_order)
    database.commit()
    database.refresh(database_order)
    return database_order


def update_order(database: Session, order_id: int, order_data):
    database_order = get_order(database, order_id)
    if database_order:
        for key, value in order_data.items():
            setattr(database_order, key, value)
        database.commit()
        database.refresh(database_order)
    return database_order


def delete_order(database: Session, order_id: int):
    database_order = get_order(database, order_id)
    if database_order:
        database.delete(database_order)
        database.commit()
    return database_order
