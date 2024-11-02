from sqlalchemy import Column, Integer, String, Float
from python_auctioneer.models import Base


class Shipping(Base):
    __tablename__ = "shipping"

    shipping_id = Column(Integer, primary_key=True, autoincrement=True)
    shipping_type = Column(String, nullable=False)
    shipping_cost = Column(Float, nullable=False)
