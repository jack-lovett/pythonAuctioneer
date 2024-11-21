from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from python_auctioneer.models import Base


class Condition(Base):
    __tablename__ = "condition"

    condition_id = Column(Integer, primary_key=True, autoincrement=True)
    condition_name = Column(String, unique=True, nullable=False)
    condition_discount_percentage = Column(Float)

    cards = relationship("Card", back_populates="condition")
