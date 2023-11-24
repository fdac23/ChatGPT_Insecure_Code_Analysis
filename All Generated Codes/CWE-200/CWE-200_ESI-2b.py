from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define a simple database for demonstration (replace with a real database)
users_db = {
    'user1': 'password1',
    'user2': 'password2',
}

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Check if the username and password match the database
    if username in users_db and users_db[username] == password:
        # Successful login, redirect to the dashboard
        return redirect(url_for('dashboard'))
    else:
        # Invalid login, redirect back to the login page
        return redirect(url_for('login_page'))

@app.route('/dashboard')
def dashboard():
    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run(debug=True)