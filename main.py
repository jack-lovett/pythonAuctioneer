"""Main file"""

from manage_cards import manage_cards

MENU = """\nWelcome to MTG Auction System\n
1. Manage cards\n
2. Manage auctions\n
3. Manage customers\n
4. Manage orders\n
5. Manage invoices and payments\n
6. Exit"""


def main():
    print(MENU)
    choice = input(">> ")
    while choice != "6":
        if choice == "1":
            manage_cards()
        elif choice == "2":
            # manage_auctions()
            pass
        elif choice == "3":
            # manage_customers()
            pass
        elif choice == "4":
            # manage_orders()
            pass
        elif choice == "5":
            # manage_invoices_and_payments()
            pass
        else:
            "Invalid choice"
        print(MENU)
        choice = input(">> ")
    print("Exiting program. Goodbye!")


main()
