"""Manage auctions menu."""

MENU = """Auction Management
1. Create auction
2. View all auctions
3. Update auction
4. Delete auction
5. Back to main menu"""


def auction_menu():
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # create_auction()
            pass
        elif choice == "2":
            # view_auctions()
            pass
        elif choice == "3":
            # update_auction()
            pass
        elif choice == "4":
            # delete_auction()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")
