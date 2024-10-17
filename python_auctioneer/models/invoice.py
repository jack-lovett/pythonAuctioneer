from sqlalchemy import Column, Integer, String, DateTime, CheckConstraint, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from python_auctioneer.models import Base


class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    invoice_date_issued = Column(DateTime, default=func.now())
    invoice_paid_status = Column(String, CheckConstraint("invoice_paid_status IN ('paid', 'unpaid', 'overdue')"),
                                 default="unpaid")
    invoice_order_id = Column(Integer, ForeignKey("orders.order_id"), nullable=False)

    order = relationship("Order", back_populates="invoice")
