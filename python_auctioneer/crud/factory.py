from base import CRUDBase

def create_crud_class(model_class):
    class GenericCRUD(CRUDBase):
        def __init__(self):
            super().__init__(model_class)

    return GenericCRUD

from .auction import Auction
from .bank_transaction import BankTransaction
from .card import Card
from .card_condition import CardCondition
from .card_finish import CardFinish
from .customer import Customer
from .invoice import Invoice
from .order import Order
from .shipping_method import ShippingMethod

model_classes = [Auction, BankTransaction, Card, CardCondition, CardFinish, Customer, Invoice, Order, ShippingMethod]

crud_classes = {model.__name__: create_crud_class(model) for model in model_classes}

# Assign each CRUD class dynamically
CRUDAuction = crud_classes["Auction"]
CRUDBankTransaction = crud_classes["BankTransaction"]
CRUDCard = crud_classes["Card"]
CRUDCardCondition = crud_classes["CardCondition"]
CRUDCardFinish = crud_classes["CardFinish"]
CRUDCustomer = crud_classes["Customer"]
CRUDInvoice = crud_classes["Invoice"]
CRUDOrder = crud_classes["Order"]
CRUDShippingMethod = crud_classes["ShippingMethod"]
