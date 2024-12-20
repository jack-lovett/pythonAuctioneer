from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base


class Transaction(Base):
    __tablename__ = "transaction"

    transaction_id = Column(Integer, primary_key=True, autoincrement=True)
    transaction_reference = Column(String, nullable=False)
    transaction_date = Column(DateTime, nullable=False)
    transaction_amount = Column(Float, nullable=False)
    transaction_invoice_id = Column(Integer, ForeignKey("invoice.invoice_id"))

    invoice = relationship("Invoice")
