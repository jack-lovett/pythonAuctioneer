from sqlalchemy import Column, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base


class Auction(Base):
    __tablename__ = "auctions"

    auction_id = Column(Integer, primary_key=True, autoincrement=True)
    auction_description = Column(Text)
    auction_open_time = Column(DateTime, nullable=False)
    auction_close_time = Column(DateTime, nullable=False)
    auction_status = Column(String, CheckConstraint("auction_status IN ('active', 'completed')"), default='active')

    # Add owner and manager id if this functionality is added

    cards = relationship("Card", back_populates="auction")
