"""Manage customers menu."""

from database import SessionLocal
from python_auctioneer.services.customer import CustomerService

MENU = """Customer Management
1. Create customer
2. View all customers
3. Update customer
4. Delete customer
5. Back to main menu"""


def customer_menu():
    """Customer menu."""
    database = SessionLocal()
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            create_customer(database)
        elif choice == "2":
            # view_customers()
            pass
        elif choice == "3":
            # update_customer()
            pass
        elif choice == "4":
            # delete_customer()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")


def create_customer(database):
    try:
        customer_firstname = input("Enter the customer first name: ")
        customer_lastname = input("Enter the customer last name: ")
        customer_address = input("Enter the customer address: ")

        customer_data = {
            "customer_firstname": customer_firstname,
            "customer_lastname": customer_lastname,
            "customer_address": customer_address,
        }
        customer_service = CustomerService()
        customer_service.create(database, customer_data)
    except ValueError as e:
        print(f"Error: {e}")
