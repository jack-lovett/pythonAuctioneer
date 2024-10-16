"""Manage customers"""

MENU = ("\nCustomer Management\n"
        "1. Create customer\n"
        "2. View all customers\n"
        "3. Update customer\n"
        "4. Delete customer\n"
        "5. Back to main menu")


def customer_menu():
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # create_customer()
            pass
        elif choice == "2":
            # view_customers()
            pass
        elif choice == "2":
            # update_customer()
            pass
        elif choice == "2":
            # delete_customer()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")
