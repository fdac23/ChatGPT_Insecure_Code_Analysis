from flask import Flask
from markupsafe import escape

app = Flask(__name)

# Define a decorator to map a URL to a function
def route_with_username(username):
    def decorator(view_func):
        def wrapper(username):
            return view_func(username)
        app.add_url_rule(f'/hello/{username}', view_func=wrapper)
        return wrapper
    return decorator

# Define the escape() function to convert special characters to HTML-safe sequences
def escape(s):
    return s  # Replace this with your actual escaping logic

# Define the hello() function
@route_with_username('<username>')
def hello(username):
    username = escape(username)  # You may apply escaping here
    return f"Hello {username}"

if __name__ == "__main__":
    app.run()