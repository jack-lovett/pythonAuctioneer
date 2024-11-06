from python_auctioneer.models import Condition
from python_auctioneer.services.base import BaseService


class ConditionService(BaseService):
    def __init__(self):
        super().__init__(Condition())