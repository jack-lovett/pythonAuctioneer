"""Manage auctions"""

MENU = ("\nAuction Management\n"
        "1. Create auction\n"
        "2. View all auctions\n"
        "3. Update auction\n"
        "4. Delete auction\n"
        "5. Back to main menu")


def manage_cards():
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # create_auction()
            pass
        elif choice == "2":
            # view_auctions()
            pass
        elif choice == "2":
            # update_auction()
            pass
        elif choice == "2":
            # delete_auction()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")
