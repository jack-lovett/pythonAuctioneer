from python_auctioneer.models import Order
from python_auctioneer.services.base import BaseService


class OrderService(BaseService):
    def __init__(self):
        super().__init__(Order())