from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name)

# Database setup (create a SQLite database and 'users' table)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

# Mock user data (You should insert real user data into the database)
users = [
    {'username': 'user1', 'password': 'password1'},
    {'username': 'user2', 'password': 'password2'},
]

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_check():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username exists in the database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    user = cursor.fetchone()
    conn.close()

    if user:
        # If the username exists, check the password
        if user[2] == password:
            # Password is correct, redirect to the home page
            return redirect(url_for('home'))
    
    # If the username or password is