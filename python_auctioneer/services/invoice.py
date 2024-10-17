from python_auctioneer.models import Invoice
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def create_invoice_service(database, invoice_data):
    """Create new invoice."""
    try:
        new_invoice = Invoice(**invoice_data)
        database.add(new_invoice)
        database.commit()
        database.refresh(new_invoice)
        return new_invoice
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error creating invoice: {e}")


def get_invoice_service(database):
    """View all invoices."""
    try:
        return database.query(Invoice).all()
    except SQLAlchemyError as e:
        print(f"Error viewing auctions: {e}")
        return []
