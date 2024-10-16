"""Manage orders menu."""

MENU = """Order Management
1. Create order
2. View all orders
3. Update order
4. Delete order
5. Back to main menu"""


def order_menu():
    """Order menu."""
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # create_order()
            pass
        elif choice == "2":
            # view_orders()
            pass
        elif choice == "3":
            # update_order()
            pass
        elif choice == "4":
            # delete_order()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")
