from python_auctioneer.crud.factory import CRUDOrder
from python_auctioneer.services.base import BaseService


class OrderService(BaseService):
    def __init__(self):
        super().__init__(CRUDOrder())