from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name)

# Function to initialize the database
def init_db():
    conn = sqlite3.connect("myapp/database.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user_messages (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, message TEXT)"""
    )
    conn.commit()
    conn.close()

# Initialize the database
init_db()

# Function to insert a user's message into the database
def insert_user_message_in_db(username, message):
    conn = sqlite3.connect("myapp/database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user_messages (username, message) VALUES (?, ?)", (username, message))
    conn.commit()
    conn.close()

# Route to display the main page with a form for submitting messages
@app.route("/")
def main_page():
    return render_template("main_page.html")

# Route to handle the form submission and insert data into the database
@app.route("/post", methods=["POST"])
def post():
    username = request.form["username"]
    message = request.form["message"]

    insert_user_message_in_db(username, message)

    return redirect(url_for("main_page"))

if __name__ == "__main__":
    app.run(debug=True)