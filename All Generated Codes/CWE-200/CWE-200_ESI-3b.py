from flask import Flask, request, render_template

app = Flask(__name__)

# Sample user data (replace with real user data)
users = [
    {'username': 'user1', 'email': 'user1@example.com', 'ssn': '123-45-6789'},
    {'username': 'user2', 'email': 'user2@example.com', 'ssn': '987-65-4321'},
]

@app.route('/info')
def info_page():
    # Retrieve user information (for demonstration, get the first user)
    user = users[0]
    username = user['username']
    email = user['email']
    ssn_last_4 = user['ssn'][-4:]

    return render_template('info.html', username=username, email=email, ssn_last_4=ssn_last_4)

if __name__ == '__main__':
    app.run(debug=True)