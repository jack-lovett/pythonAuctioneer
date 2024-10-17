from sqlalchemy.orm import Session
from python_auctioneer.models.shipping_method import ShippingMethod


def get_shipping_method(database: Session, shipping_id: int):
    return database.query(ShippingMethod).filter(ShippingMethod.shipping_id == shipping_id).first()


def get_shipping_methods(database: Session, skip: int = 0, limit: int = 10):
    return database.query(ShippingMethod).offset(skip).limit(limit).all()


def create_shipping_method(database: Session, method_data):
    database_method = ShippingMethod(**method_data)
    database.add(database_method)
    database.commit()
    database.refresh(database_method)
    return database_method


def update_shipping_method(database: Session, method_id: int, method_data):
    database_method = get_shipping_method(database, method_id)
    if database_method:
        for key, value in method_data.items():
            setattr(database_method, key, value)
        database.commit()
        database.refresh(database_method)
    return database_method


def delete_shipping_method(database: Session, method_id: int):
    database_method = get_shipping_method(database, method_id)
    if database_method:
        database.delete(database_method)
        database.commit()
    return database_method
