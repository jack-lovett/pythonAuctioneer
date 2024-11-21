from python_auctioneer.crud.factory import CRUDCustomer
from python_auctioneer.services.base import BaseService


class CustomerService(BaseService):
    def __init__(self):
        super().__init__(CRUDCustomer())