from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(255), nullable=False)
@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        username = request.form.get('username')
        message = request.form.get('message')
        
        # Call the function to insert the message in the database
        insert_user_message_in_db(username, message)

        # Redirect the user to the main page
        return redirect(url_for('main_page'))
@app.route('/')
def main_page():
    # Retrieve messages from the database
    messages = Message.query.all()

    return render_template('main_page.html', messages=messages)
