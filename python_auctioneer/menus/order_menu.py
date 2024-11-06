from database import SessionLocal
from python_auctioneer.services.shipping import ShippingService
from python_auctioneer.services.order import OrderService

"""Manage orders menu."""

MENU = """Order Management
1. Create order
2. View all orders
3. Update order
4. Delete order
5. Update shipping costs
6. Back to main menu"""


def order_menu():
    """Order menu."""
    database = SessionLocal()

    print(MENU)
    choice = input(">> ")
    while choice != "6":
        if choice == "1":
            create_order(database)
        elif choice == "2":
            # view_orders()
            pass
        elif choice == "3":
            # update_order()
            pass
        elif choice == "4":
            # delete_order()
            pass
        elif choice == "5":
            update_shipping_table(database)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")

def create_order(database):
    try:
        order_customer_id = input("Enter the customer id: ")

        order_data = {
            "order_customer_id": order_customer_id,
        }

        order_service = OrderService()
        order_service.create(database, order_data)

    except ValueError as e:
        print(f"Error: {e}")

def update_shipping_table(database):
    try:
        shipping_methods = [
            {
                "shipping_type": "standard",
                "shipping_cost": 2.00,
            },
            {
                "shipping_type": "tracked",
                "shipping_cost": 3.00,
            },
            {
                "shipping_type": "express",
                "shipping_cost": 4.00,
            }
        ]

        shipping_service = ShippingService()
        for shipping_method in shipping_methods:
            shipping_service.create(database, shipping_method)

    except ValueError as e:
        print(f"Error: {e}")
