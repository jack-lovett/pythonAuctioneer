from python_auctioneer.models import Card
from python_auctioneer.services.base import BaseService
from python_auctioneer.services.condition import ConditionService
from python_auctioneer.services.finish import FinishService


class CardService(BaseService):
    def __init__(self):
        super().__init__(Card())

    def import_cards_from_csv(self, database, csv_file_path):

        try:
            with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
                csvreader = csv.DictReader(csvfile)

                for row in csvreader:
                    condition_service = ConditionService()
                    finish_service = FinishService()

                    condition = condition_service.get_by_id(database, row["Condition"])
                    finish = finish_service.get_by_id(database, row["Foil"])

                    if condition and finish:
                        card_data = {
                            "card_name": row["Name"],
                            "card_scryfall_id": row["Scryfall ID"],
                            "card_purchase_price": float(row["Purchase price"]),
                            "card_condition_id": condition.condition_id,
                            "card_finish_id": finish.finish_id
                        }
                        self.create(database, card_data)
                    else:
                        print(f"Skipping card '{row['Name']}', condition or finish not found.")

        except Exception as e:
            database.rollback()
            print(f"Error importing cards from CSV: {e}")
        finally:
            database.close()
