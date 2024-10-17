from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from python_auctioneer.models.auction import Auction


def create_auction_service(database, auction_data):
    """Create new auction."""
    try:
        new_auction = Auction(**auction_data)
        database.add(new_auction)
        database.commit()
        database.refresh(new_auction)
        return new_auction
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error creating auction: {e}")


def get_auctions_service(database):
    """View all auctions."""
    try:
        return database.query(Auction).all()
    except SQLAlchemyError as e:
        print(f"Error viewing auctions: {e}")
        return []


def update_auction_service(database, auction_id, description, open_time, close_time):
    """Update an existing auction."""
    try:
        auction = database.query(Auction).filter(Auction.auction_id == auction_id).first()
        if auction:
            auction.auction_description = description
            auction.auction_open_time = open_time
            auction.auction_close_time = close_time
            database.commit()
            database.refresh(auction)
            return auction
        else:
            raise ValueError("Auction not found.")
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error updating auction: {e}")


def get_auction_by_id(database, auction_id):
    """Retrieve an auction by its ID."""
    return database.query(Auction).filter(Auction.auction_id == auction_id).first()


def delete_auction_service(database, auction_id):
    """Delete an auction by its ID."""
    try:
        auction = database.query(Auction).filter(Auction.auction_id == auction_id).first()
        if auction:
            database.delete(auction)
            database.commit()
            return True
        else:
            return False
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error deleting auction: {e}")
