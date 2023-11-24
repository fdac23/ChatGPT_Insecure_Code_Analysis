from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure your database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.db'  # SQLite database
db = SQLAlchemy(app)

# Define the database model for user messages
class UserMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(255), nullable=False)

# Function to insert a user message into the database
def insert_user_message_in_db(username, message):
    new_message = UserMessage(username=username, message=message)
    db.session.add(new_message)
    db.session.commit()

# Route for submitting user messages
@app.route('/post', methods=['POST'])
def post_message():
    username = request.form['username']
    message = request.form['message']

    insert_user_message_in_db(username, message)

    return redirect(url_for('home'))

# Route for displaying user messages
@app.route('/')
def home():
    messages = UserMessage.query.all()
    return render_template('messages.html', messages=messages)

if __name__ == '__main__':
    db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)