from sqlalchemy import Column, Integer, String, Float
from python_auctioneer.models import Base


class ShippingMethod(Base):
    __tablename__ = "shipping_methods"

    shipping_id = Column(Integer, primary_key=True, autoincrement=True)
    shipping_type = Column(String, nullable=False)
    shipping_cost = Column(Float, nullable=False)
