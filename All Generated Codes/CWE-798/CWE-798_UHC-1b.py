from flask import Flask, request

app = Flask(__name__)

# Define a dictionary for storing correct usernames and passwords
correct_credentials = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3',
}

# Function to check if the provided username and password are correct
def check_credentials(username, password):
    if username in correct_credentials and correct_credentials[username] == password:
        return True
    return False

# Route to check if username and password are correct
@app.route('/check_mod')
def check_mod():
    username = request.args.get('username')
    password = request.args.get('password')

    if check_credentials(username, password):
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run(debug=True)