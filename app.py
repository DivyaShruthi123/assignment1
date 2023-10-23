#REST API

from flask import Flask, request, jsonify

app = Flask(__name__)

stocks = [
    {"name" : "Starbucks", "ticker_symbol":"SBUX", "price":"1000"},
    {"name" : "Microsoft", "ticker_symbol":"MSFT", "price":"2000"}
]

#GET list of all stocks
@app.route("/stocks",methods=["GET"])
def get_all_stocks():
    return jsonify(stocks)

#CREATE a new stock
@app.route("/stocks",methods=["POST"])
def create_stock():
    data = request.get_json()
    if "name" not in data or "ticker_symbol" not in data or "price" not in data:
        return "Incomplete request!"
    
    new_stock = {"name" : data["name"], "ticker_symbol": data["ticker_symbol"], "price": data["price"]}
    stocks.append(new_stock)
    return "Stock added successfully!"
    
