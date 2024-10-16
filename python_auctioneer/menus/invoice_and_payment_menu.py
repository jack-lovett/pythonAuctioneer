"""Manage invoice and payment menu."""

MENU = """Invoice Management
1. Create invoice
2. View all invoices
3. Update invoice
4. Register payment
5. View payment history
6. Back to main menu"""


def invoice_and_payment_menu():
    """Invoice and payment menu."""
    print(MENU)
    choice = input(">> ")
    while choice != "6":
        if choice == "1":
            # create_invoice()
            pass
        elif choice == "2":
            # view_invoices()
            pass
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
