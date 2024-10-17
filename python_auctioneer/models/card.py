from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base


class Card(Base):
    __tablename__ = "cards"

    card_id = Column(Integer, primary_key=True, autoincrement=True)
    card_scryfall_id = Column(String, nullable=False)
    card_name = Column(String, nullable=False)
    card_initial_price = Column(Float)
    card_purchase_price = Column(Float)
    card_lot_number = Column(Integer)
    card_caption = Column(String)
    card_finish_id = Column(Integer, ForeignKey("card_finishes.finish_id"))
    card_condition_id = Column(Integer, ForeignKey("card_conditions.condition_id"))
    card_auction_id = Column(Integer, ForeignKey("auctions.auction_id"))
    card_order_id = Column(Integer, ForeignKey("orders.order_id"))
    card_times_on_auction = Column(Integer, default=0)

    card_finish = relationship("CardFinish")
    card_condition = relationship("CardCondition")
    auction = relationship("Auction", back_populates="cards")
    order = relationship("Order")
