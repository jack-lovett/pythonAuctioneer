"""Manage auctions menu."""

import datetime
from database import SessionLocal, get_database
from python_auctioneer.models import Auction
from python_auctioneer.services.auction import AuctionService

from tabulate import tabulate

MENU = """Auction Management
1. Create auction
2. View all auctions
3. Update auction
4. Delete auction
5. Back to main menu"""


def auction_menu():
    """Auction menu."""
    database = SessionLocal()
    print(MENU)
    choice = input(">> ")
    while choice != "5":
        if choice in ["1", "2", "3", "4"]:
            with get_database() as database:
                if choice == "1":
                    create_auction(database)
                elif choice == "2":
                    display_auctions(database)
                elif choice == "3":
                    update_auction(database)
                else:
                    delete_auction(database)
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")


def create_auction(database):
    try:
        auction_description = input("Enter the auction description: ")
        auction_open_time_str = input("Enter the auction start date DD/MM/YYYY: ")
        auction_close_time_str = input("Enter the auction end date DD/MM/YYYY: ")

        # Convert input strings to datetime objects
        auction_open_time = datetime.datetime.strptime(auction_open_time_str, '%d/%m/%Y')
        auction_close_time = datetime.datetime.strptime(auction_close_time_str, '%d/%m/%Y')

        auction_data = {
            "auction_description": auction_description,
            "auction_open_time": auction_open_time,
            "auction_close_time": auction_close_time,
        }
        auction_service = AuctionService()
        auction_service.create(database, auction_data)
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid date format. Please use DD/MM/YYYY.")


def display_auctions(database):
    """Print a formatted table of auctions."""
    auction_service = AuctionService()
    auctions = auction_service.get_all(database)
    if not auctions:
        print("No auctions found.")
    else:
        headers = ["Auction ID", "Description", "Open Time", "Close Time", "Status"]
        table_data = []
        for auction in auctions:
            table_data.append([
                auction.auction_id,
                auction.auction_description,
                auction.auction_open_time.strftime("%Y-%m-%d %H:%M:%S"),
                auction.auction_close_time.strftime("%Y-%m-%d %H:%M:%S"),
                auction.auction_status
            ])
        print(tabulate(table_data, headers=headers, tablefmt="grid"))


def update_auction(database):
    auction_id = input("Enter the auction ID to update: ")
    auction_service = AuctionService()
    auction = auction_service.get_by_id(database, auction_id)

    if not auction:
        print("Auction not found.")
        return

    print("Leave the field blank to keep the current value.")
    new_description = input(
        f"Enter new description (current: {auction.auction_description}): ") or auction.auction_description
    new_open_time_str = input(
        f"Enter new start date DD/MM/YYYY (current: {auction.auction_open_time.strftime('%d/%m/%Y')}): ")
    new_close_time_str = input(
        f"Enter new end date DD/MM/YYYY (current: {auction.auction_close_time.strftime('%d/%m/%Y')}): ")

    try:
        new_open_time = datetime.datetime.strptime(new_open_time_str,
                                                   '%d/%m/%Y') if new_open_time_str else auction.auction_open_time
        new_close_time = datetime.datetime.strptime(new_close_time_str,
                                                    '%d/%m/%Y') if new_close_time_str else auction.auction_close_time
    except ValueError as e:
        print(f"Error: {e}")
        print("Invalid date format. Please use DD/MM/YYYY.")
        return

    auction_data = {
        "auction_id": auction.auction_id,
        "auction_description": new_description,
        "auction_open_time": new_open_time,
        "auction_close_time": new_close_time
    }

    success = auction_service.update(database, auction_id, auction_data)
    if success:
        print("Auction updated successfully.")
    else:
        print("Auction update failed.")


def delete_auction(database):
    auction_id = input("Enter the auction ID to delete: ")
    confirmation = input(f"Are you sure you want to delete auction ID {auction_id}? (y/n): ")
    if confirmation.lower() == 'y':
        auction_service = AuctionService()
        success = auction_service.delete(database, auction_id)
        if success:
            print("Auction deleted successfully.")
        else:
            print("Auction not found.")
    else:
        print("Deletion cancelled.")
