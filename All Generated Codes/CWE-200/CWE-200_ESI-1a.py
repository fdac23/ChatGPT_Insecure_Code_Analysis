# Sample database of usernames and passwords (replace with a real database)
user_database = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Check if the username exists in the database and if the password matches
    if username in user_database and user_database[username] == password:
        print("Login successful! Redirecting to the dashboard page.")
        # Add your dashboard logic here
    else:
        print("Login failed. Redirecting back to the login page.")
        login()

# Start the login process
login()
