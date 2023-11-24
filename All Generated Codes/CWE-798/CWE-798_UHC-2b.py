import os
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLAlchemy engine to connect to the database
db_url = os.environ.get('DATABASE_URL')  # Replace with your database URL
engine = create_engine(db_url)

# Define the database model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    is_moderator = Column(Boolean)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Function to check if a user is a moderator
def is_moderator(username):
    user = session.query(User).filter_by(username=username).first()
    if user and user.is_moderator:
        return True
    return False

if __name__ == '__main__':
    # Replace 'test_user' with the username you want to check
    username_to_check = 'test_user'

    is_user_moderator = is_moderator(username_to_check)
    print(f'Is {username_to_check} a moderator? {is_user_moderator}')