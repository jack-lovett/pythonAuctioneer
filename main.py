"""Main file"""

MENU = """\nWelcome to MTG Auction System\n
1. Manage cards\n
2. Manage auctions\n
3. Manage customers\n
4. Manage orders\n
5. Manage invoices and payments\n
6. Exit"""


def main()
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            manage_cards()
        elif choice == "2":
            manage_auctions()
        elif choice == "3":
            manage_customers()
        elif choice == "4":
            manage_orders()
        elif choice == "5":
            manage_invoices_and_payments()
        else:
            "Invalid choice"
        print(MENU)
        choice = input(">> ")
    print("Exiting program. Goodbye!")


main()
