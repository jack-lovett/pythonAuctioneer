"""Manage customers menu."""

MENU = """Customer Management
1. Create customer
2. View all customers
3. Update customer
4. Delete customer
5. Back to main menu"""


def customer_menu():
    """Customer menu."""
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # create_customer()
            pass
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