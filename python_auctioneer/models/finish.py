from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base


class Finish(Base):
    __tablename__ = "finish"

    finish_id = Column(Integer, primary_key=True, autoincrement=True)
    finish_name = Column(String, unique=True, nullable=False)

    cards = relationship("Card", back_populates="finish")
