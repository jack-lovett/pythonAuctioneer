from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String, nullable=False)