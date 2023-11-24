from flask import Flask, jsonify
from sqlalchemy import create_engine, text

app = Flask(__name)

# Database configuration (replace with your database details)
db_url = "sqlite:///mydatabase.db"
engine = create_engine(db_url)

@app.route('/check_mod/<username>')
def check_mod(username):
    try:
        # Establish a database connection
        connection = engine.connect()

        # Define a SQL query to check if the user is a moderator
        query = text("SELECT is_moderator FROM users WHERE username = :username")
        result = connection.execute(query, username=username).fetchone()

        if result:
            is_moderator = result[0]  # Extract the value of is_moderator
            return jsonify({"is_moderator": bool(is_moderator)})
        else:
            return jsonify({"error": "User not found"})

    except Exception as e:
        return jsonify({"error": str(e)})
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
