"""Manage cards"""

import pandas as pd
from database import SessionLocal
from python_auctioneer.services.card import import_cards_from_csv  # Make sure to import your service function
from python_auctioneer.services.card_condition import create_card_condition_service
from python_auctioneer.services.card_finish import create_card_finish_service

MENU = """Card Management
1. Add Card list
2. List cards
3. Import cards from CSV
4. Add card finishes to database
5. Add card conditions to database
6. Back to main menu"""


def card_menu():
    """Card menu."""
    database = SessionLocal()
    print(MENU)
    choice = input(">> ")
    while choice != "6":
        if choice == "1":
            # add_card()
            pass
        elif choice == "2":
            # list_cards()
            pass
        elif choice == "3":
            import_cards_from_csv_menu()
        elif choice == "4":
            fill_card_finishes(database)
        elif choice == "5":
            fill_card_conditions(database)
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


def fill_card_conditions(database):
    condition_attributes = [
        {
            "condition_name": "mint",
            "condition_discount_percentage": 0.00,
        },
        {
            "condition_name": "near_mint",
            "condition_discount_percentage": 0.00,
        },
        {
            "condition_name": "excellent",
            "condition_discount_percentage": 0.05,
        },
        {
            "condition_name": "good",
            "condition_discount_percentage": 0.10,
        },
        {
            "condition_name": "light_played",
            "condition_discount_percentage": 0.20,
        },
        {
            "condition_name": "played",
            "condition_discount_percentage": 0.25,
        },
        {
            "condition_name": "poor",
            "condition_discount_percentage": 0.3,
        }
    ]
    
    for condition_attribute in condition_attributes:
        create_card_condition_service(database, condition_attribute)
