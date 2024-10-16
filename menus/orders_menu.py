"""Manage orders"""

MENU = ("\nOrder Management\n"
        "1. Create order\n"
        "2. View all orders\n"
        "3. Update order\n"
        "4. Delete order\n"
        "5. Back to main menu")


def manage_cards():
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # create_order()
            pass
        elif choice == "2":
            # view_orders()
            pass
        elif choice == "2":
            # update_order()
            pass
        elif choice == "2":
            # delete_order()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")
