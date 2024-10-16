from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    order_shipping_id = Column(Integer, ForeignKey("shipping_methods.shipping_id"))
    order_tracking_reference = Column(String)
    order_status = Column(String, CheckConstraint("order_status IN ('pending', 'fulfilled')"), default="pending")
    order_invoice_id = Column(Integer, ForeignKey("invoices.invoice_id"))

    customer = relationship("Customer")
    shipping_method = relationship("ShippingMethod")
    invoice = relationship("Invoice")
