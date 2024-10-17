from sqlalchemy import Column, Integer, String
from python_auctioneer.models import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_firstname = Column(String, nullable=False)
    customer_lastname = Column(String, nullable=False)
    customer_address = Column(String, nullable=False)
