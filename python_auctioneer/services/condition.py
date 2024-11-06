from python_auctioneer.crud.factory import CRUDCondition
from python_auctioneer.services.base import BaseService


class ConditionService(BaseService):
    def __init__(self):
        super().__init__(CRUDCondition())