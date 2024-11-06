from python_auctioneer.models import Shipping
from python_auctioneer.services.base import BaseService


class ShippingService(BaseService):
    def __init__(self):
        super().__init__(Shipping())