from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from python_auctioneer.crud.factory import CRUDAuction
from python_auctioneer.models.auction import Auction

crud_auction = CRUDAuction()


def create_auction_service(database, auction_data):
    """Create new auction."""
    try:
        return crud_auction.create(database, auction_data)
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error creating auction: {e}")


def get_auctions_service(database):
    """View all auctions."""
    try:
        return crud_auction.get_all(database)
    except SQLAlchemyError as e:
        print(f"Error viewing auctions: {e}")
        return []


def update_auction_service(database, auction_id, auction_data):
    """Update an existing auction."""
    try:
        auction = crud_auction.get(database, auction_id)
        if not auction:
            raise ValueError(f"Auction {auction_id} does not exist.")
        return crud_auction.update(database, auction_id, auction_data)
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error updating auction: {e}")


def get_auction_by_id(database, auction_id):
    """Retrieve an auction by its ID."""
    return database.query(Auction).filter(Auction.auction_id == auction_id).first()


def delete_auction_service(database, auction_id):
    """Delete an auction by its ID."""
    try:
        auction = crud_auction.get(database, auction_id)
        if not auction:
            raise ValueError(f"Auction {auction_id} does not exist.")
        return crud_auction.delete(database, auction_id)
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error deleting auction: {e}")
