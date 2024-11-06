from python_auctioneer.models import Invoice
from python_auctioneer.services.base import BaseService


class InvoiceService(BaseService):
    def __init__(self):
        super().__init__(Invoice())