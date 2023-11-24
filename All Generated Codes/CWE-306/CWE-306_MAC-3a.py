class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

# Sample user data (you can replace this with your own user data or database)
users = {
    'user123': User('user123', 'password123', 'user123@example.com')
}

def change_email(username, old_email, new_email, password):
    if username in users:
        user = users[username]
        if user.password == password:
            if user.email == old_email:
                if user.email != new_email:
                    user.email = new_email
                    return "Email successfully changed!"
                else:
                    return "New email should be different from old email."
            else:
                return "Incorrect old email."
        else:
            return "Incorrect password."
    else:
        return "User not found."

# Example usage
username = 'user123'
old_email = 'user123@example.com'
new_email = 'newemail@example.com'
password = 'password123'

result = change_email(username, old_email, new_email, password)
print(result)
