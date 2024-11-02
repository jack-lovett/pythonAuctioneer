from sqlalchemy import Column, Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base


class Order(Base):
    __tablename__ = "order"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    order_customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    order_shipping_id = Column(Integer, ForeignKey("shipping.shipping_id"))
    order_tracking_reference = Column(String)
    order_status = Column(String, CheckConstraint("order_status IN ('pending', 'fulfilled')"), default="pending")

    customer = relationship("Customer")
    shipping_method = relationship("Shipping")
    invoice = relationship("Invoice", back_populates="order")
