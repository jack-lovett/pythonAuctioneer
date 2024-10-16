"""Database manager."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from python_auctioneer.config import DATABASE_URL
from python_auctioneer.models import Base

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get a SQLAlchemy session
def get_db():
    database = SessionLocal()
    try:
        yield database
        database.commit()
    except Exception:
        database.rollback()
        raise
    finally:
        database.close()


# Initialise the database
def init_db():
    from python_auctioneer.models import (
        card_finish, card_condition, card, auction, customer, order, invoice, bank_transaction, shipping_method
    )
    Base.metadata.create_all(bind=engine)
