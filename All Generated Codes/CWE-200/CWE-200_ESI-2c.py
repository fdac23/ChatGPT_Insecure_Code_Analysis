from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name)

# Sample user data (in a real application, this data would be stored in a database)
users = {
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

    if username in users and users[username] == password:
        # If the username and password are correct, redirect to the session page
        return redirect(url_for('session'))
    else:
        # If the username or password is incorrect, display an error message
        return "Username or password is incorrect. <a href='/'>Try again</a>"

@app.route('/session')
def session():
    return "Welcome to the session page!"

if __name__ == '__main__':
    app.run()