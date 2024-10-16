from sqlalchemy import Column, Integer, String
from python_auctioneer.models import Base


class CardFinish(Base):
    __tablename__ = "card_finishes"

    finish_id = Column(Integer, primary_key=True, autoincrement=True)
    finish_name = Column(String, unique=True, nullable=False)
