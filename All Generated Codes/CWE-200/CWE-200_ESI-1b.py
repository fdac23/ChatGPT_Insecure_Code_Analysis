from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple database (for demonstration purposes)
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

    # Check if the username and password exist in the database
    if username in users_db and users_db[username] == password:
        # Successful login, redirect to the home page
        return redirect(url_for('home'))
    else:
        # Invalid login, redirect back to the login page
        return redirect(url_for('login_page'))

@app.route('/home')
def home():
    return "Welcome to the home page!"

if __name__ == '__main__':
    app.run(debug=True)