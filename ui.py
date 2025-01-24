from flask import Flask, render_template

from database import SessionLocal
from python_auctioneer.models import Auction
from python_auctioneer.services.auction import AuctionService

app = Flask(__name__)


# Get nav
def get_navigation():
    return render_template("navigation.html")


# Define a simple route
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auctions')
def auctions():
    # Get the database session
    database = SessionLocal()
    auction_service = AuctionService()
    auctions = auction_service.get_all(database)
    return render_template('auctions.html', auctions=auctions)


@app.route('/orders')
def orders():
    return render_template('orders.html')


@app.route('/pricer')
def pricer():
    return render_template('pricer.html')


@app.route('/reconcile')
def reconcile():
    return render_template('reconcile.html')


if __name__ == '__main__':
    app.run(debug=False)
