from flask import Flask, request, redirect
import re

app = Flask(__name)

# Define the regular expression pattern
pattern = r'^[a-zA-Z0-9\-]+\.'
regex = re.compile(pattern)

@app.route('/')
def redirect_target():
    # Get the 'target' query parameter from the URL
    target = request.args.get('target')

    # Check if 'target' matches the regular expression
    if target and regex.match(target):
        # If it matches, redirect to the target
        return redirect(target)

    # If 'target' doesn't match, redirect to the root of the site
    return redirect('/')

if __name__ == '__main__':
    app.run()