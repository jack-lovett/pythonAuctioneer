"""General configuration file."""
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///python_auctioneer.db")
