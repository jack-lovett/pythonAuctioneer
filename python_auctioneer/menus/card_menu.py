"""Manage cards"""

import pandas as pd
from tabulate import tabulate

from database import SessionLocal
from python_auctioneer.services.card import CardService
from python_auctioneer.services.condition import ConditionService
from python_auctioneer.services.finish import FinishService

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
            display_cards(database)
        elif choice == "3":
            import_cards_from_csv_menu()
        elif choice == "4":
            fill_finishes(database)
        elif choice == "5":
            fill_conditions(database)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")


def display_cards(database):
    card_service = CardService()
    cards = card_service.get_all(database)
    if not cards:
        print("No cards found.")
    else:
        headers = ["Card ID", "Card Name", "Card Initial Price", "Card Finish", "Card Condition"]
        table_data = []
        finish_service = FinishService()
        condition_service = ConditionService()
        for card in cards:
            card_finish = finish_service.get_by_id(database, card.card_finish_id).finish_name
            card_condition = condition_service.get_by_id(database, card.card_condition_id).condition_name
            table_data.append([
                card.card_id,
                card.card_name,
                card.card_initial_price,
                card_finish,
                card_condition,
            ])
        print(tabulate(table_data, headers=headers, tablefmt="grid"))


def import_cards_from_csv_menu():
    file_path = input("Enter the path to the CSV file: ")
    try:
        card_service = CardService()
        card_service.import_cards_from_csv(file_path)
        print("Cards imported successfully.")
    except Exception as e:
        print(f"Error importing cards: {e}")


def fill_finishes(database):
    finishes = [
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

    finish_service = FinishService()
    for finish in finishes:
        finish_service.create(database, finish)


def fill_conditions(database):
    conditions = [
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

    condition_service = ConditionService()

    for condition in conditions:
        condition_service.create(database, condition)
