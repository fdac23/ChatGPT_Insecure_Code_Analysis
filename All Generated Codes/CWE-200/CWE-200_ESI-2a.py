# Sample user database (replace with a real database)
user_database = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def success():
    print("Login successful! Redirecting to the success page.")
    # You can add your success page logic here

def cant_login():
    print("Login failed. Redirecting to the can't login page.")
    # You can add your can't login page logic here

def internal_server_error():
    print("Internal server error. Redirecting to the internal server error page.")
    # You can add your internal server error page logic here

def login(username, password):
    if username in user_database and user_database[username] == password:
        success()
    else:
        cant_login()

# Sample usage:
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

login(entered_username, entered_password)
