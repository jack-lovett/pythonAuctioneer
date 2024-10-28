import csv

from sqlalchemy.exc import IntegrityError
import pandas as pd

from database import SessionLocal
from python_auctioneer.services.card_finish import get_card_finish_service
from python_auctioneer.models.card import Card
from python_auctioneer.services.card_condition import get_card_condition_service


def import_cards_from_csv(csv_file_path):
    database = SessionLocal()

    try:
        with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)

            for row in csvreader:
                # Fetch condition and finish instances by name
                condition = get_card_condition_service(database, row["Condition"])
                finish = get_card_finish_service(database, row["Foil"])

                if condition and finish:
                    card_data = {
                        "card_name": row["Name"],
                        "card_scryfall_id": row["Scryfall ID"],
                        "card_purchase_price": float(row["Purchase price"]),
                        "card_condition_id": condition.condition_id,
                        "card_finish_id": finish.finish_id
                        # You can add additional fields here if necessary
                    }
                    add_card_service(database, card_data)
                else:
                    print(f"Skipping card '{row['Name']}', condition or finish not found.")

    except Exception as e:
        database.rollback()
        print(f"Error importing cards from CSV: {e}")
    finally:
        database.close()


def add_card_service(database, card_data):
    try:
        new_card = Card(**card_data)
        database.add(new_card)
        database.commit()
        database.refresh(new_card)
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error adding card: {e}")

def get_cards_service(database):
    cards = database.query(Card).all()
    return cards