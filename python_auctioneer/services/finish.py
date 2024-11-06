from python_auctioneer.models import Finish
from python_auctioneer.services.base import BaseService


class FinishService(BaseService):
    def __init__(self):
        super().__init__(Finish())