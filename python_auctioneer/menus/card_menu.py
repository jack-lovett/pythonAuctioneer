"""Manage cards"""

import pandas as pd
from database import SessionLocal
from python_auctioneer.services.card import import_cards_from_csv  # Make sure to import your service function
from python_auctioneer.services.card_finish import create_card_finish_service

MENU = """Card Management
1. Add Card list
2. List cards
3. Import cards from CSV
4. Add card finish to database
5. Back to main menu"""


def card_menu():
    """Card menu."""
    database = SessionLocal()
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice == "1":
            # add_card()
            pass
        elif choice == "2":
            # list_cards()
            pass
        elif choice == "3":
            import_cards_from_csv_menu()
        elif choice == "4":
            add_card_finish(database)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")


def import_cards_from_csv_menu():
    file_path = input("Enter the path to the CSV file: ")
    database = SessionLocal()
    try:
        import_cards_from_csv(file_path)
        print("Cards imported successfully.")
    except Exception as e:
        print(f"Error importing cards: {e}")


def fill_card_finishes(database):
    card_finishes = [
        {
            "finish_name": "normal",
        },
        {
            "finish_name": "foil",
        },
        {
            "finish_name": "etched",
        }
    ]

        for card_finish in card_finishes:
            create_card_finish_service(database, card_finish)
    except ValueError as e:
        print(f"Error: {e}")

