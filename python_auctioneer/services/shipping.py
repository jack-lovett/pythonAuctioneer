from python_auctioneer.crud.factory import CRUDShipping
from python_auctioneer.services.base import BaseService


class ShippingService(BaseService):
    def __init__(self):
        super().__init__(CRUDShipping())