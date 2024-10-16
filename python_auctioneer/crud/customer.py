from sqlalchemy.orm import Session
from python_auctioneer.models.customer import Customer


def get_customer(database: Session, customer_id: int):
    return database.query(Customer).filter(Customer.customer_id == customer_id).first()


def get_customers(database: Session, skip: int = 0, limit: int = 10):
    return database.query(Customer).offset(skip).limit(limit).all()


def create_customer(database: Session, customer_data):
    database_customer = Customer(**customer_data)
    database.add(database_customer)
    database.commit()
    database.refresh(database_customer)
    return database_customer


def update_customer(database: Session, customer_id: int, customer_data):
    database_customer = Customer(**customer_data)
    if database_customer:
        for key, value in customer_data.items():
            setattr(database_customer, key, value)
        database.commit()
        database.refresh(database_customer)
    return database_customer


def delete_customer(database: Session, customer_id: int):
    database_customer = get_customer(database, customer_id)
    if database_customer:
        database.delete(database_customer)
        database.commit()
    return database_customer
