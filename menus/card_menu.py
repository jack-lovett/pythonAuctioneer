"""Manage cards"""

MENU = ("\nCard Management\n"
        "1. Add a card\n"
        "2. List cards\n"
        "3. Back to main menu")


def manage_cards():
    print(MENU)
    choice = input(">> ")
    while choice != "3":
        if choice == "1":
            # add_card()
            pass
        elif choice == "2":
            # list_cards()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")
