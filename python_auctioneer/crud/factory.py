from python_auctioneer.crud.base import CRUDBase

def create_crud_class(model_class):
    class GenericCRUD(CRUDBase):
        def __init__(self):
            super().__init__(model_class)

    return GenericCRUD

from ..models.auction import Auction
from ..models.transaction import Transaction
from ..models.card import Card
from ..models.condition import Condition
from ..models.finish import Finish
from ..models.customer import Customer
from ..models.invoice import Invoice
from ..models.order import Order
from ..models.shipping import Shipping

model_classes = [Auction, Transaction, Card, Condition, Finish, Customer, Invoice, Order, Shipping]

crud_classes = {model.__name__: create_crud_class(model) for model in model_classes}

# Assign each CRUD class dynamically
CRUDAuction = crud_classes["Auction"]
CRUDTransaction = crud_classes["Transaction"]
CRUDCard = crud_classes["Card"]
CRUDCondition = crud_classes["Condition"]
CRUDFinish = crud_classes["Finish"]
CRUDCustomer = crud_classes["Customer"]
CRUDInvoice = crud_classes["Invoice"]
CRUDOrder = crud_classes["Order"]
CRUDShipping = crud_classes["Shipping"]
