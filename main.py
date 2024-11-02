"""Main file."""
import os
import platform

from database import init_db
from python_auctioneer.menus.card_menu import card_menu
from python_auctioneer.menus.auction_menu import auction_menu
from python_auctioneer.menus.customer_menu import customer_menu
from python_auctioneer.menus.order_menu import order_menu
from python_auctioneer.menus.invoice_and_payment_menu import invoice_and_payment_menu

print("Welcome to MTG Auction System")
MENU = """== Main Menu ==
1. Manage cards
2. Manage auctions
3. Manage customers
4. Manage orders
5. Manage invoices and payments
6. Exit"""


def main():
    # Initialise the database
    init_db()

    print(MENU)
    choice = input(">> ")
    while choice != "6":
        if choice == "1":
            card_menu()
        elif choice == "2":
            auction_menu()
        elif choice == "3":
            customer_menu()
        elif choice == "4":
            order_menu()
        elif choice == "5":
            invoice_and_payment_menu()
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">> ")
    print("Exiting program. Goodbye!")


main()
