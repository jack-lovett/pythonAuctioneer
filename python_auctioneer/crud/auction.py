from sqlalchemy.orm import Session
from python_auctioneer.models.auction import Auction


def get_auction(database: Session, auction_id: int):
    return database.query(Auction).filter(Auction.auction_id == auction_id).first()


def get_auctions(database: Session, skip: int = 0, limit: int = 10):
    return database.query(Auction).offset(skip).limit(limit).all()


def create_auction(database: Session, auction_data):
    database_auction = Auction(**auction_data)
    database.add(database_auction)
    database.commit()
    database.refresh(database_auction)
    return database_auction


def update_auction(database: Session, auction_id: int, auction_data):
    database_auction = get_auction(database, auction_id)
    if database_auction:
        for key, value in auction_data.items():
            setattr(database_auction, key, value)
        database.commit()
        database.refresh(database_auction)
    return database_auction


def delete_auction(database: Session, auction_id: int):
    database_auction = get_auction(database, auction_id)
    if database_auction:
        database.delete(database_auction)
        database.commit()
    return database_auction
