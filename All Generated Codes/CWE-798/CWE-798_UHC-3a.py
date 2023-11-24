from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def get_database_connection():
    # Replace 'database_uri' with your actual database URI
    database_uri = 'your_database_uri_here'
    db = SQLAlchemy()
    db.init_app(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    return db

def get_server_name():
    # Extract server name from the database URI
    database_uri = 'your_database_uri_here'
    server_name = database_uri.split('@')[1].split('/')[0].split(':')[0]
    return server_name

def get_database_name():
    # Extract database name from the database URI
    database_uri = 'your_database_uri_here'
    database_name = database_uri.split('/')[-1]
    return database_name

def get_database_user():
    # Extract database user from the database URI
    database_uri = 'your_database_uri_here'
    user = database_uri.split('://')[1].split(':')[0]
    return user

def get_database_password():
    # Replace 'your_password' with your actual password
    password = 'your_password'
    return password
