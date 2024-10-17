"""Manage cards"""

import pandas as pd
from database import SessionLocal
from python_auctioneer.services.card import import_cards_from_csv  # Make sure to import your service function

MENU = """Card Management
1. Add Card list
2. List cards
3. Import cards from CSV
4. Back to main menu"""


def card_menu():
    """Card menu."""
    print(MENU)
    choice = input(">> ")
    while choice != "4":
        if choice == "1":
            # add_card()
            pass
        elif choice == "2":
            # list_cards()
            pass
        elif choice == "3":
            import_cards_from_csv_menu()
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")


def import_cards_from_csv_menu():
    file_path = input("Enter the path to the CSV file: ")
    database = SessionLocal()
    try:
        import_cards_from_csv(database, file_path)
        print("Cards imported successfully.")
    except Exception as e:
        print(f"Error importing cards: {e}")