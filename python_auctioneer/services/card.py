from sqlalchemy.exc import IntegrityError
import pandas as pd
from python_auctioneer.models.card import Card


def import_cards_from_csv(database, file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")

    required_columns = ["Name", "Scryfall ID", "Purchase price"]

    for column in required_columns:
        if column not in df.columns:
            raise ValueError(f"Missing required column: {column}")

    for _, row in df.iterrows():
        card_data = {
            "card_scryfall_id": row["Scryfall ID"],
            "card_name": row["Name"],
            "card_purchase_price": row.get("Purchase price", 0.0),
            "card_initial_price": row.get("Purchase price", 0.0),
        }
        add_card_to_database(database, card_data)


def add_card_to_database(database, card_data):
    try:
        new_card = Card(**card_data)
        database.add(new_card)
        database.commit()
        database.refresh(new_card)
    except IntegrityError as e:
        database.rollback()
        raise ValueError(f"Error adding card: {e}")