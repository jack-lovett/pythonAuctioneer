from python_auctioneer.crud.factory import CRUDFinish
from python_auctioneer.services.base import BaseService


class FinishService(BaseService):
    def __init__(self):
        super().__init__(CRUDFinish())