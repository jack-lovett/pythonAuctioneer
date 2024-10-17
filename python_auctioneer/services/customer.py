from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from python_auctioneer.models.customer import Customer


def create_customer_service(database, customer_data):
    """Create new customer."""
    try:
        new_customer = Customer(**customer_data)
        database.add(new_customer)
        database.commit()
        database.refresh(new_customer)
        return new_customer
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error creating customer: {e}")

