from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name)

# Secret key for session management (change it to a strong, random value)
app.secret_key = 'your_secret_key'

# Sample user data (in a real application, store user data securely, e.g., in a database)
users = {
    'user1': {
        'password': 'password1',
        'email': 'user1@example.com',
    },
    'user2': {
        'password': 'password2',
        'email': 'user2@example.com',
    },
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in users and users[username]['password'] == password:
        session['username'] = username  # Store the username in the session
        return redirect(url_for('profile'))
    else:
        return "Invalid username or password"

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' not in session:
        return redirect(url_for('login_page'))

    if request.method == 'POST':
        old_email = request.form.get('old_email')
        password = request.form.get('password')
        new_email = request.form.get('new_email')
        username = session['username']

        if users[username]['email'] == old_email and users[username]['password'] == password:
            # Update the user's email
            users[username]['email'] = new_email
            return "Email updated successfully"
        else:
            return "Invalid old email or password"

    return render_template('profile.html', username=session['username'], old_email=users[session['username']]['email'])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run()