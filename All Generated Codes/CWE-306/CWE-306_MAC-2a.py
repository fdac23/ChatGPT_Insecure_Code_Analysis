from flask import Flask, redirect, url_for

app = Flask(__name)

# Simulating user authentication
def is_user_logged_in():
    # You can implement your own logic to check if the user is logged in
    return True  # Replace with your authentication logic

def is_admin():
    # You can implement your own logic to check if the user is an admin
    return True  # Replace with your admin check logic

@app.route('/')
def home():
    if is_user_logged_in():
        if is_admin():
            return redirect(url_for('admin'))
        else:
            return redirect(url_for('user'))
    else:
        return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Login Page"

@app.route('/user')
def user():
    return "User Page"

@app.route('/admin')
def admin():
    return "Admin Page"

if __name__ == '__main__':
    app.run(debug=True)
