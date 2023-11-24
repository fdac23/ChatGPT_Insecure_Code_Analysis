from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name)

# Database initialization and setup
def init_db():
    conn = sqlite3.connect("myapp/database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, quantity INTEGER)"""
    )
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Route to display the stock entry form
@app.route("/")
def stock_form():
    return render_template("stock_form.html")

# Route to handle the form submission and insert data into the database
@app.route("/buy_order", methods=["POST"])
def buy_order():
    stock_name = request.form["stock_name"]
    stock_quantity = request.form["stock_quantity"]

    conn = sqlite3.connect("myapp/database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO stocks (name, quantity) VALUES (?, ?)", (stock_name, stock_quantity))
    conn.commit()
    conn.close()

    return redirect(url_for("stock_view"))

# Route to view the stocks in the database
@app.route("/stock_view")
def stock_view():
    conn = sqlite3.connect("myapp/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, quantity FROM stocks")
    stocks = cursor.fetchall()
    conn.close()

    return render_template("stock_view.html", stocks=stocks)

if __name__ == "__main__":
    app.run(debug=True)