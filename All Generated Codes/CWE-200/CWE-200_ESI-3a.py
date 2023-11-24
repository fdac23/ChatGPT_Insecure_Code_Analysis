from flask import Flask, request, render_template, session

app = Flask(__name)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Set session variables (replace with real values)
session['username'] = 'john_doe'
session['email'] = 'johndoe@example.com'
session['ssn'] = '123-45-6789'

@app.route('/info', methods=['GET'])
def info():
    username = session.get('username', 'N/A')
    email = session.get('email', 'N/A')
    ssn = session.get('ssn', 'N/A')

    return render_template('info.html', username=username, email=email, ssn=ssn)

if __name__ == '__main__':
    app.run(debug=True)
