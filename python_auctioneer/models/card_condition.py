from sqlalchemy import Column, Integer, String, Float
from python_auctioneer.models import Base


class CardCondition(Base):
    __tablename__ = "card_conditions"

    condition_id = Column(Integer, primary_key=True, autoincrement=True)
    condition_name = Column(String, unique=True, nullable=False)
    condition_discount_percentage = Column(Float)
