from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name)

# Fake user data (replace with your actual user data)
users = {
    'user': 'password',
    'admin': 'adminpass',
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            # Successful login, redirect to user_page
            return redirect(url_for('user_page', username=username))
        else:
            return "Invalid username or password"
    return render_template('login.html')

@app.route('/index', methods=['GET'])
def index():
    return "Welcome to the index page"

@app.route('/user_page/<username>', methods=['GET'])
def user_page(username):
    return f"Welcome, {username}! This is the user page."

@app.route('/admin_page', methods=['GET'])
def admin_page():
    return "Welcome to the admin page"

if __name__ == '__main__':
    app.run()