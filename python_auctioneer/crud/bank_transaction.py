from sqlalchemy.orm import Session
from python_auctioneer.models.bank_transaction import BankTransaction


def get_bank_transaction(database: Session, transaction_id: int):
    return database.query(BankTransaction).filter(BankTransaction.transaction_id == transaction_id).first()


def get_bank_transactions(database: Session, skip: int = 0, limit: int = 10):
    return database.query(BankTransaction).offset(skip).limit(limit).all()


def create_bank_transaction(database: Session, transaction_data):
    database_transaction = BankTransaction(**transaction_data)
    database.add(database_transaction)
    database.commit()
    database.refresh(database_transaction)
    return database_transaction


def update_bank_transaction(database: Session, transaction_id: int, transaction_data):
    database_transaction = get_bank_transaction(database, transaction_id)
    if database_transaction:
        for key, value in transaction_data.items():
            setattr(database_transaction, key, value)
        database.commit()
        database.refresh(database_transaction)
    return database_transaction


def delete_bank_transaction(database: Session, transaction_id: int):
    database_transaction = get_bank_transaction(database, transaction_id)
    if database_transaction:
        database.delete(database_transaction)
        database.commit()
    return database_transaction
