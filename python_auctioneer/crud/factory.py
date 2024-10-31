from base import CRUDBase

def create_crud_class(model_class):
    class GenericCRUD(CRUDBase):
        def __init__(self):
            super().__init__(model_class)

    return GenericCRUD

from ..models.auction import Auction
from ..models.bank_transaction import BankTransaction
from ..models.card import Card
from ..models.card_condition import CardCondition
from ..models.card_finish import CardFinish
from ..models.customer import Customer
from ..models.invoice import Invoice
from ..models.order import Order
from ..models.shipping_method import ShippingMethod

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
