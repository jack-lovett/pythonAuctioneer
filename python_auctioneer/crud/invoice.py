from sqlalchemy.orm import Session
from python_auctioneer.models.invoice import Invoice


def get_invoice(database: Session, invoice_id: int):
    return database.query(Invoice).filter(Invoice.invoice_id == invoice_id).first()


def get_invoices(database: Session, skip: int = 0, limit: int = 10):
    return database.query(Invoice).offset(skip).limit(limit).all()


def create_invoice(database: Session, invoice_data):
    database_invoice = Invoice(**invoice_data)
    database.add(database_invoice)
    database.commit()
    database.refresh(database_invoice)
    return database_invoice


def update_invoice(database: Session, invoice_id: int, invoice_data):
    database_invoice = get_invoice(database, invoice_id)
    if database_invoice:
        for key, value in invoice_data.items():
            setattr(database_invoice, key, value)
        database.commit()
        database.refresh(database_invoice)
    return database_invoice


def delete_invoice(database: Session, invoice_id: int):
    database_invoice = get_invoice(database, invoice_id)
    if database_invoice:
        database.delete(database_invoice)
        database.commit()
    return database_invoice
