import sqlite3

class DatabaseManager:
    def __init__(self, database_name="mtg_auction.db"):
        self.database_name = database_name
        self.conn = None


# Connect to SQLite (this will create the database if it doesn't exist)
# conn = sqlite3.connect('mtg_auction.db')
# cursor = conn.cursor()

# Create card finishes table
# cursor.execute('''
# CREATE TABLE card_finishes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     finish_name TEXT UNIQUE NOT NULL
# );
# ''')
#
# # Create card conditions table
# cursor.execute('''
# CREATE TABLE card_conditions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     condition_name TEXT UNIQUE NOT NULL,
#     discount_percentage REAL
# );
# ''')
#
# # Create cards table
# cursor.execute('''
# CREATE TABLE cards (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     scryfall_id TEXT NOT NULL,
#     card_name TEXT NOT NULL,
#     initial_price REAL,
#     purchase_price REAL,
#     lot_number INTEGER,
#     caption TEXT,
#     finish_id INTEGER,
#     condition_id INTEGER,
#     auction_id INTEGER,
#     order_id INTEGER,
#     times_on_auction INTEGER DEFAULT 0,
#     FOREIGN KEY (finish_id) REFERENCES card_finishes (id),
#     FOREIGN KEY (condition_id) REFERENCES card_conditions (id),
#     FOREIGN KEY (auction_id) REFERENCES auctions (id),
#     FOREIGN KEY (order_id) REFERENCES orders (id)
# );
# ''')
#
# # Create auctions table
# cursor.execute('''
# CREATE TABLE auctions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     description TEXT,
#     open_time TIMESTAMP NOT NULL,
#     close_time TIMESTAMP NOT NULL,
#     status TEXT CHECK (status IN ('active', 'completed')) DEFAULT 'active',
#     owner_id INTEGER,
#     manager_id INTEGER
# );
# ''')
#
# # Create customers table
# cursor.execute('''
# CREATE TABLE customers (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     address TEXT NOT NULL
# );
# ''')
#
# # Create orders table
# cursor.execute('''
# CREATE TABLE orders (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     customer_id INTEGER NOT NULL,
#     manager_id INTEGER,
#     shipping_id INTEGER,
#     tracking_reference TEXT,
#     status TEXT CHECK (status IN ('pending', 'fulfilled')) DEFAULT 'pending',
#     invoice_id INTEGER,
#     FOREIGN KEY (customer_id) REFERENCES customers (id),
#     FOREIGN KEY (shipping_id) REFERENCES shipping_methods (id),
#     FOREIGN KEY (invoice_id) REFERENCES invoices (id)
# );
# ''')
#
# # Create invoices table
# cursor.execute('''
# CREATE TABLE invoices (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     date_issued TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     paid_status TEXT CHECK (paid_status IN ('paid', 'unpaid', 'overdue')) DEFAULT 'unpaid',
#     shipping_status TEXT CHECK (shipping_status IN ('shipped', 'not shipped')) DEFAULT 'not shipped'
# );
# ''')
#
# # Create bank transactions table
# cursor.execute('''
# CREATE TABLE bank_transactions (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     reference TEXT NOT NULL,
#     date TIMESTAMP NOT NULL,
#     amount REAL NOT NULL,
#     invoice_id INTEGER,
#     FOREIGN KEY (invoice_id) REFERENCES invoices (id)
# );
# ''')
#
# # Create shipping methods table
# cursor.execute('''
# CREATE TABLE shipping_methods (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     type TEXT NOT NULL,
#     cost REAL NOT NULL
# );
# ''')