from flask import Flask, render_template

app = Flask(__name)

# Define a decorator function that binds a URL route to the hello() function.
@app.route('/hello/<username>')
def hello(username):
    # Pass the 'username' variable to the template for rendering.
    return render_template('hello.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
