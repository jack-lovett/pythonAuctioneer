from sqlalchemy import Column, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from python_auctioneer.models import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)