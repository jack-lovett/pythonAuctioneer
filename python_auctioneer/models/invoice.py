from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint
from sqlalchemy.sql import func
from python_auctioneer.models import Base


class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date_issued = Column(DateTime, default=func.now())
    invoice_paid_status = Column(String, CheckConstraint("invoice_paid_status IN ('paid', 'unpaid', 'overdue')"),
                                 default="unpaid")
    invoice_shipping_status = Column(String, CheckConstraint("invoice_shipping_status IN ('shipped', 'not shipped')"),
                                     default="not shipped")
