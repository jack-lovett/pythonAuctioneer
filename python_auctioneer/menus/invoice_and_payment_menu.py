"""Manage invoice and payment menu."""
import datetime
from database import SessionLocal
from python_auctioneer.services.invoice import InvoiceService
from tabulate import tabulate



MENU = """Invoice Management
1. Create invoice
2. View all invoices
3. Update invoice
4. Register payment
5. View payment history
6. Back to main menu"""


def invoice_and_payment_menu():
    """Invoice and payment menu."""
    database = SessionLocal()
    print(MENU)
    choice = input(">> ")
    while choice != "6":
        if choice == "1":
            create_invoice(database)
        elif choice == "2":
            view_invoices(get_invoice_service(database))
        elif choice == "3":
            # update_invoice()
            pass
        elif choice == "4":
            # register_payment()
            pass
        elif choice == "5":
            # view_payment_history()
            pass
        else:
            print("Invalid choice.")
        print(MENU)
        choice = input(">> ")

def create_invoice(database):
    try:
        invoice_date_issued_str = input("Enter the invoice issue date DD/MM/YYYY: ")
        invoice_order_id = input("Enter the order id: ")

        # Convert input strings to datetime objects
        invoice_date_issued = datetime.datetime.strptime(invoice_date_issued_str, '%d/%m/%Y')

        invoice_data = {
            "invoice_date_issued": invoice_date_issued,
            "invoice_order_id": invoice_order_id,
        }
        invoice_service = InvoiceService()
        invoice_service.create(database, invoice_data)
    except ValueError as e:
        print(f"Error: {e}")

def view_invoices(invoices):
    """Print a formatted table of invoices."""
    if not invoices:
        print("No invoices found.")
    else:
        headers = ["Invoice ID", "Invoice Date Issued", "Invoice Paid Status", "Invoice Order ID"]
        table_data = []
        for invoice in invoices:
            table_data.append([
                invoice.invoice_id,
                invoice.invoice_date_issued.strftime("%Y-%m-%d %H:%M:%S"),
                invoice.invoice_paid_status,
                invoice.invoice_order_id,
            ])
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
