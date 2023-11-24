from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)
class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
@app.route('/buy_stock', methods=['POST'])
def buy_stock():
    stock_name = request.form.get('stock_name')
    quantity = int(request.form.get('quantity'))

    # Insert the stock into the database
    stock = Stock(name=stock_name, quantity=quantity)
    db.session.add(stock)
    db.session.commit()

    # Call the buy_function and pass the stock name
    result = buy_function(stock_name)
    return result

def buy_function(stock_name):
    # Your buy logic here
    return f"Bought stock: {stock_name}"
