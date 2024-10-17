from python_auctioneer.models import Invoice
from sqlalchemy.exc import IntegrityError


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
