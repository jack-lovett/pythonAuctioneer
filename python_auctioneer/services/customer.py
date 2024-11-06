from python_auctioneer.models import Condition, Customer
from python_auctioneer.services.base import BaseService


class CustomerService(BaseService):
    def __init__(self):
        super().__init__(Customer())