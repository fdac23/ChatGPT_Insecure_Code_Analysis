from flask import Flask, request

app = Flask(__name)

# Simulated user data (replace with your actual user data)
users = {
    "user1": {"password": "password1", "is_mod": False},
    "user2": {"password": "password2", "is_mod": True},
    "user3": {"password": "password3", "is_mod": False},
}

# Function to authenticate and check if a user is a moderator
def auth_mod(username, password):
    if username in users and users[username]["password"] == password:
        return users[username]["is_mod"]
    return False

# Function to check if a user is a moderator based on URL parameters
@app.route('/check_mod')
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')
    session = request.args.get('session')

    # Call the auth_mod function to check if the user is a moderator
    is_mod = auth_mod(username, password)

    if is_mod:
        return f"User {username} is a moderator"
    else:
        return f"User {username} is not a moderator"

if __name__ == "__main__":
    app.run(debug=True)