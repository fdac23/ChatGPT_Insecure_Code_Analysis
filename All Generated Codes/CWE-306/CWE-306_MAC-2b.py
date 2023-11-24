from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple database for demonstration (replace with real data)
users_db = {
    'user1': 'password1',
    'user2': 'password2',
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

        if username in users_db and users_db[username] == password:
            # Successful login, redirect to user_page
            return redirect(url_for('user_page', username=username))
        else:
            # Invalid login, return
            return "Login failed. Please try again."

@app.route('/user/<username>')
def user_page(username):
    return f"Welcome, {username}!"

if __name__ == '__main__':
    app.run(debug=True)