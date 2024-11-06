from python_auctioneer.crud.factory import CRUDInvoice
from python_auctioneer.services.base import BaseService


class InvoiceService(BaseService):
    def __init__(self):
        super().__init__(CRUDInvoice())