from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from python_auctioneer.models.auction import Auction


def create_auction_service(database: Session, auction_data: dict) -> Auction:
    """
    Service function to create a new auction.
    """
    try:
        new_auction = Auction(**auction_data)
        database.add(new_auction)
        database.commit()
        database.refresh(new_auction)
        return new_auction
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error creating auction: {e}")
