from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple user database for demonstration (replace with real data)
users_db = {
    'user1': {'email': 'user1@example.com', 'password': 'password1'},
    'user2': {'email': 'user2@example.com', 'password': 'password2'},
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        # Render the login form
        return render_template('login.html')
    elif request.method == 'POST':
        # Process the login
        username = request.form['username']
        password = request.form['password']

        if username in users_db and users_db[username]['password'] == password:
            # Successful login, redirect to the email change form
            return redirect(url_for('change_email', username=username))
        else:
            # Invalid login, return
            return "Login failed. Please try again."

@app.route('/change_email/<username>', methods=['GET', 'POST'])
def change_email(username):
    if request.method == 'GET':
        # Render the email change form
        return render_template('change_email.html', username=username)
    elif request.method == 'POST':
        # Process the email change
        old_email = request.form['old_email']
        new_email = request.form['new_email']
        confirm_password = request.form['confirm_password']

        user_data = users_db.get(username)

        if user_data and user_data['email'] == old_email and user_data['password'] == confirm_password:
            # Update the user's email
            user_data['email'] = new_email
            return f"Email changed successfully for {username}."
        else:
            return "Email change failed. Please provide correct information."

if __name__ == '__main__':
    app.run(debug=True)