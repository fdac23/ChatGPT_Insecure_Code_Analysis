from flask import Flask, request, session

app = Flask(__name)

# Set a secret key for session management (required for session variables)
app.secret_key = 'your_secret_key'

@app.route('/info', methods=['GET'])
def info():
    # Retrieve user information from session variables
    username = session.get('username', 'No username available')
    email = session.get('email', 'No email available')
    ssn = session.get('ssn', 'No SSN available')

    info_str = f"Username: {username}, Email: {email}, SSN: {ssn}"
    return info_str

if __name__ == '__main__':
    app.run()