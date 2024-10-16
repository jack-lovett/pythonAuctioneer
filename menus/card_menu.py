"""Manage cards"""

MENU = """Card Management
1. Add a card
2. List cards
3. Back to main menu"""


def card_menu():
    """Card menu."""
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
