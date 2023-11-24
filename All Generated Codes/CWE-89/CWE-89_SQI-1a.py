from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form.get('email')
    
    # Check if the email address exists in the database
    user = User.query.filter_by(email=email).first()

    if user:
        # Email address exists, remove it from the database
        db.session.delete(user)
        db.session.commit()
        return "You have been unsubscribed from our service."
    else:
        return "You are not in our database."
