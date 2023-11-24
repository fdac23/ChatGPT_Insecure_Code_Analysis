from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stocks.db'  # SQLite database
db = SQLAlchemy(app)

# Define the database model for stock orders
class StockOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(100), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(100), nullable=False)

# Route for the form to buy stocks
@app.route('/buy', methods=['GET', 'POST'])
def buy_stock():
    if request.method == 'POST':
        stock_name = request.form['stock_name']
        stock_quantity = int(request.form['stock_quantity'])
        username = 'user123'  # Replace with the actual username (you may use user sessions)

        # Create a new stock order and add it to the database
        new_order = StockOrder(stock_name=stock_name, stock_quantity=stock_quantity, username=username)
        db.session.add(new_order)
        db.session.commit()

        # Redirect to the user's profile page (change the URL as needed)
        return redirect(url_for('user_profile'))

    return render_template('buy_stock_form.html')  # Create an HTML form for buying stocks

# Route for the user profile page (you can customize this)
@app.route('/profile')
def user_profile():
    # Retrieve and display user's profile information (e.g., purchased stocks)
    return "User Profile Page"

if __name__ == '__main__':
    db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)