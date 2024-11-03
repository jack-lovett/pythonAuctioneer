from python_auctioneer.crud.factory import CRUDAuction
from python_auctioneer.services.base import BaseService


class AuctionService(BaseService):
    def __init__(self):
        super().__init__(CRUDAuction())
