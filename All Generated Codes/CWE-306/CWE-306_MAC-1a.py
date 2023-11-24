from flask import Flask, render_template, request, redirect, session

app = Flask(__name)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Sample user credentials (replace with real credentials)
valid_username = 'user'
valid_password = 'password'

@app.route('/')
def index():
    return '<a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == valid_username and password == valid_password:
            session['username'] = username
            return redirect('/secret')
        else:
            return "Invalid credentials. Please try again."

    return '<form method="POST"><input type="text" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><input type="submit" value="Log In"></form>'

@app.route('/secret')
def secret():
    if 'username' in session:
        return "Secret settings"
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
