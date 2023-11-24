from flask import Flask, request, render_template

app = Flask(__name)

# Mocked user credentials (replace with your authentication logic)
correct_username = "user123"
correct_password = "password123"

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/check_mod', methods=['POST'])
def check_mod():
    username = request.form.get('username')
    password = request.form.get('password')

    if username == correct_username and password == correct_password:
        return 'true'
    else:
        return 'false'

if __name__ == '__main__':
    app.run(debug=True)
